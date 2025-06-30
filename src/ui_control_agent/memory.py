"""
Conversation memory for UI Control Agent.
Maintains context and history for each conversation session.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class ConversationMessage:
    """Single message in conversation"""
    role: str  # "user", "agent", "ui_result"
    content: str
    timestamp: datetime
    metadata: Dict[str, Any] = None
    
    def to_dict(self) -> dict:
        return {
            "role": self.role,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata or {}
        }


class ConversationMemory:
    """Manages conversation history for multiple sessions"""
    
    def __init__(self, max_messages_per_session: int = 50, session_timeout_hours: int = 24):
        """Initialize conversation memory"""
        self.conversations: Dict[str, List[ConversationMessage]] = {}
        self.session_last_activity: Dict[str, datetime] = {}
        self.max_messages = max_messages_per_session
        self.session_timeout = timedelta(hours=session_timeout_hours)
        
        logger.info(f"Conversation memory initialized (max_messages={max_messages_per_session}, timeout={session_timeout_hours}h)")
    
    def add_message(self, session_id: str, role: str, content: str, metadata: Dict[str, Any] = None):
        """Add a message to conversation history"""
        if session_id not in self.conversations:
            self.conversations[session_id] = []
        
        message = ConversationMessage(
            role=role,
            content=content,
            timestamp=datetime.now(),
            metadata=metadata or {}
        )
        
        self.conversations[session_id].append(message)
        self.session_last_activity[session_id] = datetime.now()
        
        # Trim conversation if too long
        if len(self.conversations[session_id]) > self.max_messages:
            # Keep recent messages + summarize older ones
            self._trim_conversation(session_id)
        
        logger.debug(f"Added {role} message to session {session_id}")
    
    def get_conversation_context(self, session_id: str, max_recent_messages: int = 10) -> str:
        """Get conversation context for LLM prompt"""
        if session_id not in self.conversations:
            return ""
        
        messages = self.conversations[session_id]
        if not messages:
            return ""
        
        # Get recent messages
        recent_messages = messages[-max_recent_messages:]
        
        context_parts = []
        context_parts.append("=== CONVERSATION HISTORY ===")
        
        for msg in recent_messages:
            if msg.role == "user":
                context_parts.append(f"User: {msg.content}")
            elif msg.role == "agent":
                context_parts.append(f"Agent: {msg.content}")
            elif msg.role == "ui_result":
                # Summarize UI results for context
                try:
                    ui_data = json.loads(msg.content)
                    if "products" in ui_data:
                        count = len(ui_data["products"])
                        context_parts.append(f"UI Result: Found {count} products for previous search")
                    else:
                        context_parts.append(f"UI Result: {msg.metadata.get('summary', 'UI action completed')}")
                except:
                    context_parts.append(f"UI Result: {msg.metadata.get('summary', 'UI action completed')}")
        
        context_parts.append("=== END CONVERSATION HISTORY ===")
        return "\n".join(context_parts)
    
    def get_conversation_summary(self, session_id: str) -> Dict[str, Any]:
        """Get conversation summary and stats"""
        if session_id not in self.conversations:
            return {"exists": False}
        
        messages = self.conversations[session_id]
        user_messages = [msg for msg in messages if msg.role == "user"]
        agent_messages = [msg for msg in messages if msg.role == "agent"]
        ui_results = [msg for msg in messages if msg.role == "ui_result"]
        
        return {
            "exists": True,
            "total_messages": len(messages),
            "user_messages": len(user_messages),
            "agent_responses": len(agent_messages),
            "ui_interactions": len(ui_results),
            "last_activity": self.session_last_activity.get(session_id).isoformat() if session_id in self.session_last_activity else None,
            "first_message": messages[0].timestamp.isoformat() if messages else None
        }
    
    def _trim_conversation(self, session_id: str):
        """Trim conversation and create summary of older messages"""
        messages = self.conversations[session_id]
        if len(messages) <= self.max_messages:
            return
        
        # Keep recent half, summarize older half
        keep_count = self.max_messages // 2
        old_messages = messages[:-keep_count]
        recent_messages = messages[-keep_count:]
        
        # Create summary of old messages
        summary_content = self._create_conversation_summary(old_messages)
        summary_message = ConversationMessage(
            role="system",
            content=f"[CONVERSATION SUMMARY] {summary_content}",
            timestamp=datetime.now(),
            metadata={"type": "summary", "summarized_count": len(old_messages)}
        )
        
        # Replace with summary + recent messages
        self.conversations[session_id] = [summary_message] + recent_messages
        
        logger.info(f"Trimmed conversation {session_id}: summarized {len(old_messages)} messages")
    
    def _create_conversation_summary(self, messages: List[ConversationMessage]) -> str:
        """Create a summary of conversation messages"""
        user_queries = []
        agent_actions = []
        
        for msg in messages:
            if msg.role == "user":
                user_queries.append(msg.content)
            elif msg.role == "agent" and msg.metadata and msg.metadata.get("action"):
                agent_actions.append(msg.metadata["action"])
        
        summary_parts = []
        if user_queries:
            summary_parts.append(f"User asked about: {', '.join(user_queries[-3:])}")  # Last 3 queries
        if agent_actions:
            summary_parts.append(f"Agent performed: {', '.join(set(agent_actions))}")  # Unique actions
        
        return "; ".join(summary_parts) if summary_parts else "Previous conversation activity"
    
    def cleanup_old_sessions(self):
        """Remove old inactive sessions"""
        now = datetime.now()
        expired_sessions = []
        
        for session_id, last_activity in self.session_last_activity.items():
            if now - last_activity > self.session_timeout:
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            del self.conversations[session_id]
            del self.session_last_activity[session_id]
            logger.info(f"Cleaned up expired session: {session_id}")
        
        return len(expired_sessions)
    
    def get_all_sessions(self) -> Dict[str, Dict[str, Any]]:
        """Get info about all active sessions"""
        return {
            session_id: self.get_conversation_summary(session_id)
            for session_id in self.conversations.keys()
        } 