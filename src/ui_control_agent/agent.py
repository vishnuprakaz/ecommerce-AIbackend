"""
Simple UI Control Agent.
Clean, straightforward agent implementation.
"""

import logging
from typing import Dict, Any, AsyncGenerator

from .config import SimpleConfig
from .workflow import SimpleWorkflow
from .tools.wrapper import ToolWrapper

logger = logging.getLogger(__name__)


class UIControlAgent:
    """Simple, clean UI control agent with proper callback coordination"""
    
    def __init__(self):
        """Initialize agent with minimal setup"""
        self.config = SimpleConfig()
        
        # Validate OpenAI configuration
        if not self.config.is_openai_configured():
            raise ValueError("OPENAI_API_KEY environment variable is required")
        
        # Initialize workflow
        self.workflow = SimpleWorkflow(openai_model=self.config.openai_model)
        
        # Initialize and set tools
        self.tool_wrapper = ToolWrapper()
        tools = self.tool_wrapper.create_langchain_tools()
        self.workflow.set_tools(tools)
        
        logger.info("UI Control Agent initialized successfully")
    
    async def process_message(self, message: str, session_id: str = "default") -> Dict[str, Any]:
        """Process a user message and return response with conversation memory"""
        try:
            result = await self.workflow.process_message(message, session_id)
            
            return {
                "response": result["response"],
                "status": "success",
                "actions": result["actions"],
                "tools_used": result["tools_used"],
                "pending_ui_callback": result["pending_ui_callback"],
                "conversation_stats": result.get("conversation_stats", {}),
                "session_id": session_id
            }
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return {
                "response": "I apologize, but I encountered an error processing your request.",
                "status": "error",
                "actions": [],
                "tools_used": [],
                "pending_ui_callback": False,
                "conversation_stats": {},
                "session_id": session_id
            }
    
    async def stream_message(self, message: str, session_id: str = "default") -> AsyncGenerator[str, None]:
        """Stream response for a user message with proper UI callback coordination"""
        try:
            async for chunk in self.workflow.stream_response(message, session_id):
                yield chunk
        except Exception as e:
            logger.error(f"Error streaming message: {e}")
            yield f'{{"event_type": "status", "data": {{"status": "error", "message": "{str(e)}"}}}}\n'
    
    def get_health_status(self) -> Dict[str, Any]:
        """Get agent health status"""
        return {
            "status": "ok",
            "openai_configured": self.config.is_openai_configured(),
            "tools_loaded": len(self.workflow.tools),
            "agent_mode": "ui_first_with_callback_coordination",
            "memory_enabled": True
        } 