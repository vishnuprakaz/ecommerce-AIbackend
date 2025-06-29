"""
API routes for the ecommerce agent server
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import logging
from ..models.requests import ChatMessage, ToolRequest
from ..models.responses import (
    ChatResponse, 
    ToolResponse, 
    HealthResponse, 
    ToolsResponse,
    ResponseStatus
)

logger = logging.getLogger(__name__)


def add_api_routes(app: FastAPI, agent):
    """Add all API routes to the FastAPI app"""
    
    @app.get("/", tags=["General"])
    async def root():
        """Root endpoint with API information"""
        return {
            "message": "Ecommerce Agent API", 
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
        """Health check endpoint"""
        try:
            # Check if OpenAI is configured
            api_key = os.getenv("OPENAI_API_KEY")
            return HealthResponse(
                status="ok",
                openai_configured=bool(api_key and api_key != "your_api_key_here"),
                tools_loaded=len(agent.tools),
                a2a_enabled=True,
                agent_mode="openai" if agent.is_openai_available() else "mock"
            )
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")

    @app.post("/chat", response_model=ChatResponse, tags=["Chat"])
    async def chat(msg: ChatMessage):
        """Legacy chat endpoint - use /a2a/message/stream for A2A protocol"""
        try:
            # Validate agent is ready
            if not hasattr(agent, 'tools'):
                raise HTTPException(status_code=503, detail="Agent not ready")
            
            # Use the agent to process the message
            result = agent.process_message(msg.message)
            
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
            return ToolsResponse(
                tools=agent.tools,
                count=len(agent.tools),
                agent_mode="openai" if agent.is_openai_available() else "mock"
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