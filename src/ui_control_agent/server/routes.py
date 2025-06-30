"""
Simple API routes for UI Control Agent.
Clean, easy to understand route definitions.
Now with conversation management!
"""

import logging
import json
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Dict, Any

logger = logging.getLogger(__name__)


class ChatRequest(BaseModel):
    """Simple chat request model"""
    message: str
    session_id: str = "default"


class UICallbackRequest(BaseModel):
    """UI callback request model for sending results back to agent"""
    action_id: str
    ui_data: Dict[str, Any]
    session_id: str = "default"


def add_routes(app: FastAPI):
    """Add all routes to the FastAPI app"""
    
    @app.get("/health")
    async def health_check():
        """Health check endpoint"""
        return app.state.agent.get_health_status()
    
    @app.get("/tools")
    async def get_tools():
        """Get available tools"""
        agent = app.state.agent
        return {
            "tools": [{"name": tool.name, "description": tool.description} for tool in agent.workflow.tools if hasattr(tool, 'name')],
            "count": len(agent.workflow.tools),
            "agent_mode": "ui_first_with_memory"
        }
    
    @app.post("/chat")
    async def chat(request: ChatRequest):
        """Simple chat endpoint (non-streaming)"""
        agent = app.state.agent
        result = await agent.process_message(request.message, request.session_id)
            
        return {
            "response": result["response"],
            "user_id": "anonymous",
            "status": result["status"],
            "tools_available": len(agent.workflow.tools),
            "conversation_stats": result.get("conversation_stats", {}),
            "note": "For streaming responses, use /stream"
        }
    
    @app.post("/stream")
    async def stream_chat(request: ChatRequest):
        """Streaming chat endpoint - UI first architecture with conversation memory"""
        agent = app.state.agent
        
        return StreamingResponse(
            agent.stream_message(request.message, request.session_id),
            media_type="application/x-ndjson"
            )
    
    @app.post("/ui/callback")
    async def ui_callback(request: UICallbackRequest):
        """UI callback endpoint for sending action results back to agent"""
        try:
            agent = app.state.agent
            result = await agent.workflow.process_ui_callback(request.action_id, request.ui_data)
            
            # Just acknowledge receipt - the stream endpoint is waiting for results
            return {
                "status": result.get("status", "success"),
                "message": result.get("message", "Callback processed"),
                "action_id": request.action_id
            }
            
        except Exception as e:
            logger.error(f"UI callback error: {e}")
            return {"status": "error", "message": str(e)}
    
    # === CONVERSATION MANAGEMENT ROUTES ===
    
    @app.get("/conversations")
    async def get_all_conversations():
        """Get all active conversation sessions"""
        agent = app.state.agent
        conversations = agent.workflow.get_all_conversations()
        
        return {
            "conversations": conversations,
            "total_sessions": len(conversations),
            "active_sessions": sum(1 for conv in conversations.values() if conv.get("exists", False))
        }
    
    @app.get("/conversations/{session_id}")
    async def get_conversation_history(session_id: str):
        """Get conversation history for a specific session"""
        agent = app.state.agent
        history = agent.workflow.get_conversation_history(session_id)
        
        return history
    
    @app.delete("/conversations/{session_id}")
    async def clear_conversation(session_id: str):
        """Clear conversation history for a specific session"""
        try:
            agent = app.state.agent
            # Clear the session from memory
            if session_id in agent.workflow.memory.conversations:
                del agent.workflow.memory.conversations[session_id]
                del agent.workflow.memory.session_last_activity[session_id]
                
                return {
                    "status": "success",
                    "message": f"Conversation {session_id} cleared",
                    "session_id": session_id
                }
            else:
                return {
                    "status": "not_found",
                    "message": f"Conversation {session_id} not found",
                    "session_id": session_id
                }
        except Exception as e:
            logger.error(f"Error clearing conversation {session_id}: {e}")
            return {"status": "error", "message": str(e)}
    
    @app.post("/conversations/cleanup")
    async def cleanup_old_conversations():
        """Clean up old inactive conversations"""
        try:
            agent = app.state.agent
            cleaned_count = agent.workflow.cleanup_old_conversations()
            
            return {
                "status": "success",
                "message": f"Cleaned up {cleaned_count} old conversations",
                "cleaned_sessions": cleaned_count
            }
        except Exception as e:
            logger.error(f"Error cleaning up conversations: {e}")
            return {"status": "error", "message": str(e)}
    
    # Legacy A2A-style streaming endpoint for compatibility
    @app.post("/a2a/message/stream")
    async def a2a_stream_chat(request: ChatRequest):
        """A2A-compatible streaming endpoint"""
        agent = app.state.agent
        
        return StreamingResponse(
            agent.stream_message(request.message, request.session_id),
            media_type="text/plain"
        )
    
    logger.info("Routes added successfully") 