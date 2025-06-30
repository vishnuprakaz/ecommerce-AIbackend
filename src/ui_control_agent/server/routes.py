"""
API routes for the UI control agent server
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional, List
from enum import Enum
import logging


# Simple models to replace deleted legacy models
class ChatMessage(BaseModel):
    message: str
    user_id: str = "anonymous"


class ToolRequest(BaseModel):
    tool_name: str
    parameters: Dict[str, Any] = {}


class ResponseStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"
    PENDING = "pending"


class ChatResponse(BaseModel):
    response: str
    user_id: str
    status: ResponseStatus
    tools_available: int
    note: Optional[str] = None


class ToolResponse(BaseModel):
    result: Dict[str, Any]
    status: ResponseStatus
    tool_name: str
    execution_time: float


class HealthResponse(BaseModel):
    status: str
    openai_configured: bool
    tools_loaded: int
    a2a_enabled: bool
    agent_mode: str


class ToolsResponse(BaseModel):
    tools: List[Dict[str, Any]]
    count: int
    agent_mode: str

logger = logging.getLogger(__name__)


def add_api_routes(app: FastAPI, agent):
    """Add all API routes to the FastAPI app"""
    
    @app.get("/", tags=["General"])
    async def root():
        """Root endpoint with API information"""
        return {
            "message": "UI Control Agent API", 
            "version": "0.2.0",
            "a2a_discovery": "/.well-known/agent.json",
            "test_client": "/test",
            "documentation": "/docs"
        }

    @app.get("/test", response_class=HTMLResponse, tags=["Testing"])
    async def test_client():
        """Serve the HTML test client for streaming"""
        try:
            with open("static/test_client.html", "r") as f:
                return HTMLResponse(content=f.read())
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="Test client not found")

    @app.get("/health", response_model=HealthResponse, tags=["Health"])
    async def health():
        """Health check endpoint - OpenAI required"""
        try:
            # Check OpenAI configuration
            if not agent.is_openai_available():
                return HealthResponse(
                    status="error",
                    openai_configured=False,
                    tools_loaded=len(agent.tools),
                    a2a_enabled=False,
                    agent_mode="error"
                )
            
            # Check workflow initialization
            if not hasattr(agent, 'workflow') or agent.workflow is None:
                return HealthResponse(
                    status="error",
                    openai_configured=True,
                    tools_loaded=len(agent.tools),
                    a2a_enabled=False,
                    agent_mode="error"
                )
            
            # All systems operational
            return HealthResponse(
                status="ok",
                openai_configured=True,
                tools_loaded=len(agent.tools),
                a2a_enabled=True,
                agent_mode="openai"
            )
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return HealthResponse(
                status="error",
                openai_configured=False,
                tools_loaded=0,
                a2a_enabled=False,
                agent_mode="error"
            )

    @app.post("/chat", response_model=ChatResponse, tags=["Chat"])
    async def chat(msg: ChatMessage):
        """Legacy chat endpoint - use /a2a/message/stream for A2A protocol"""
        try:
            # Validate agent is ready
            if not hasattr(agent, 'tools'):
                raise HTTPException(status_code=503, detail="Agent not ready")
            
            # Validate OpenAI is available
            if not agent.is_openai_available():
                raise HTTPException(status_code=503, detail="OpenAI API not configured")
            
            # Use the agent to process the message
            result = agent.process_message(msg.message)
            
            # Check for errors in result
            if result.get("status") == "error":
                raise HTTPException(status_code=500, detail=result.get("error", "Unknown error"))
            
            return ChatResponse(
                response=result["response"],
                user_id=msg.user_id,
                status=ResponseStatus(result["status"]),
                tools_available=result.get("tools_available", 0),
                note="For streaming responses, use /a2a/message/stream"
            )
        except ValueError as e:
            logger.warning(f"Chat validation error: {e}")
            raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        except Exception as e:
            logger.error(f"Chat processing error: {e}")
            raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")

    @app.get("/tools", response_model=ToolsResponse, tags=["Tools"])
    async def get_tools():
        """Get available tools"""
        try:
            if not agent.is_openai_available():
                raise HTTPException(status_code=503, detail="OpenAI API not configured")
            
            return ToolsResponse(
                tools=agent.tools,
                count=len(agent.tools),
                agent_mode="openai"
            )
        except Exception as e:
            logger.error(f"Tools listing error: {e}")
            raise HTTPException(status_code=500, detail=f"Error fetching tools: {str(e)}")

    @app.post("/tools/execute", response_model=ToolResponse, tags=["Tools"])
    async def execute_tool(request: ToolRequest):
        """Execute a specific tool for testing"""
        try:
            # Check if tool exists
            available_tools = [tool["name"] for tool in agent.tools]
            if request.tool_name not in available_tools:
                raise HTTPException(
                    status_code=404, 
                    detail=f"Tool '{request.tool_name}' not found. Available: {available_tools}"
                )
            
            import time
            start_time = time.time()
            result = agent.execute_tool(request.tool_name, request.parameters)
            execution_time = time.time() - start_time
            
            return ToolResponse(
                result=result,
                status=ResponseStatus.SUCCESS if result.get("success") else ResponseStatus.ERROR,
                tool_name=request.tool_name,
                execution_time=execution_time
            )
        except ValueError as e:
            logger.warning(f"Tool execution validation error: {e}")
            raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        except Exception as e:
            logger.error(f"Tool execution error: {e}")
            raise HTTPException(status_code=500, detail=f"Error executing tool: {str(e)}") 