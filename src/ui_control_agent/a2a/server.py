"""
A2A (Agent-to-Agent) protocol server implementation
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator, Dict, Any, Optional
from pydantic import BaseModel
import json
import time
import logging

logger = logging.getLogger(__name__)


class A2AMessage(BaseModel):
    """A2A message format"""
    message: str
    user_id: str = "anonymous"
    context_id: Optional[str] = None


class A2AServer:
    """A2A protocol server for handling agent communication"""
    
    def __init__(self, agent):
        self.agent = agent
    
    async def stream_response(self, message: A2AMessage) -> AsyncGenerator[str, None]:
        """Stream A2A response with SSE format using LangGraph workflow"""
        try:
            logger.info(f"A2A stream request from user {message.user_id}: {message.message[:50]}...")
            
            # Use the agent's workflow streaming
            async for chunk in self.agent.stream_workflow(message.message, message.context_id):
                yield chunk
                
        except Exception as e:
            logger.error(f"Error in A2A streaming: {e}")
            error_data = {
                'event': 'workflow_error', 
                'error': str(e), 
                'context_id': message.context_id,
                'timestamp': time.time()
            }
            yield f"data: {json.dumps(error_data)}\n\n"
    



def add_a2a_routes(app: FastAPI, agent):
    """Add A2A protocol routes to the FastAPI app"""
    a2a_server = A2AServer(agent)
    
    @app.get("/.well-known/agent.json")
    async def agent_discovery():
        """A2A agent discovery endpoint"""
        return {
            "name": "UI Control Agent",
            "description": "AI agent for conversational UI control interactions",
            "version": "0.2.0",
            "capabilities": [
                "product_search",
                "navigation",
                "cart_management"
            ],
            "tools": agent.tools,
            "endpoints": {
                "message": "/a2a/message",
                "stream": "/a2a/message/stream"
            },
            "protocols": ["A2A-v1", "SSE"]
        }
    
    @app.post("/a2a/message/stream")
    async def a2a_stream_message(message: A2AMessage):
        """A2A streaming message endpoint"""
        try:
            logger.info(f"A2A stream request from user {message.user_id}: {message.message[:50]}...")
            
            return StreamingResponse(
                a2a_server.stream_response(message),
                media_type="text/plain",
                headers={
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type"
                }
            )
            
        except ValueError as e:
            logger.warning(f"A2A validation error: {e}")
            raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        except Exception as e:
            logger.error(f"A2A streaming error: {e}")
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    
    @app.post("/a2a/message")
    async def a2a_message(message: A2AMessage):
        """A2A non-streaming message endpoint"""
        try:
            logger.info(f"A2A message from user {message.user_id}: {message.message[:50]}...")
            
            # Process message with agent
            result = agent.process_message(message.message)
            
            return {
                "response": result["response"],
                "user_id": message.user_id,
                "context_id": message.context_id,
                "status": result["status"],
                "tools_available": result.get("tools_available", 0),
                "timestamp": time.time()
            }
            
        except ValueError as e:
            logger.warning(f"A2A validation error: {e}")
            raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        except Exception as e:
            logger.error(f"A2A message error: {e}")
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}") 