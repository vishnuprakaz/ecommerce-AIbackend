import json
import asyncio
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, validator, Field
from typing import Dict, Any, AsyncGenerator, Optional
from agent import EcommerceAgent
import re

class A2AMessage(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000, description="User message")
    context_id: Optional[str] = Field(None, max_length=100, description="Optional context identifier")
    stream: bool = Field(True, description="Whether to stream the response")
    
    @validator('message')
    def validate_message(cls, v):
        if not v or not v.strip():
            raise ValueError('Message cannot be empty or whitespace only')
        # Remove excessive whitespace
        v = ' '.join(v.split())
        return v
    
    @validator('context_id')
    def validate_context_id(cls, v):
        if v is not None:
            # Allow alphanumeric, hyphens, and underscores only
            if not re.match(r'^[a-zA-Z0-9_-]+$', v):
                raise ValueError('Context ID can only contain letters, numbers, hyphens, and underscores')
        return v

class A2AServer:
    def __init__(self, agent: EcommerceAgent):
        self.agent = agent
    
    async def stream_response(self, message: str, context_id: str = None) -> AsyncGenerator[str, None]:
        """Stream A2A protocol responses with comprehensive error handling"""
        
        try:
            # Validate message length again (belt and suspenders)
            if len(message) > 2000:
                yield f"data: {json.dumps({'event': 'error', 'error': 'Message too long (max 2000 characters)', 'context_id': context_id})}\n\n"
                return
            
            # Start event
            yield f"data: {json.dumps({'event': 'start', 'context_id': context_id, 'timestamp': asyncio.get_event_loop().time()})}\n\n"
            
            # Thinking event
            yield f"data: {json.dumps({'event': 'thinking', 'content': 'Processing your request...', 'context_id': context_id})}\n\n"
            await asyncio.sleep(0.1)  # Small delay for realistic feel
            
            # Process with agent
            result = self.agent.process_message(message)
            
            # Check if agent returned an error
            if result.get("status") == "error":
                error_data = {
                    "event": "error",
                    "error": result.get("response", "Unknown agent error"),
                    "context_id": context_id
                }
                yield f"data: {json.dumps(error_data)}\n\n"
                return
            
            # Stream the response in chunks
            response_text = result.get("response", "")
            if not response_text:
                yield f"data: {json.dumps({'event': 'error', 'error': 'Empty response from agent', 'context_id': context_id})}\n\n"
                return
            
            words = response_text.split()
            chunk_delay = min(0.05, max(0.01, 3.0 / len(words)))  # Adaptive delay based on response length
            
            for i, word in enumerate(words):
                chunk_data = {
                    "event": "text_chunk",
                    "content": word + " ",
                    "chunk_id": i,
                    "context_id": context_id
                }
                yield f"data: {json.dumps(chunk_data)}\n\n"
                await asyncio.sleep(chunk_delay)
            
            # Complete event
            complete_data = {
                "event": "complete",
                "context_id": context_id,
                "status": result.get("status", "unknown"),
                "tools_available": result.get("tools_available", 0),
                "message_length": len(message),
                "response_length": len(response_text)
            }
            yield f"data: {json.dumps(complete_data)}\n\n"
            
        except asyncio.CancelledError:
            # Handle client disconnection
            yield f"data: {json.dumps({'event': 'cancelled', 'message': 'Stream cancelled by client', 'context_id': context_id})}\n\n"
        except json.JSONEncodeError as e:
            # Handle JSON serialization errors
            yield f"data: {json.dumps({'event': 'error', 'error': f'JSON encoding error: {str(e)}', 'context_id': context_id})}\n\n"
        except Exception as e:
            # Handle any other unexpected errors
            error_data = {
                "event": "error",
                "error": f"Streaming error: {str(e)}",
                "context_id": context_id,
                "error_type": type(e).__name__
            }
            yield f"data: {json.dumps(error_data)}\n\n"

def add_a2a_routes(app: FastAPI, agent: EcommerceAgent):
    """Add A2A protocol routes to FastAPI app with comprehensive error handling"""
    a2a = A2AServer(agent)
    
    @app.get("/.well-known/agent.json")
    async def agent_discovery():
        """A2A agent discovery endpoint"""
        try:
            return {
                "name": "Ecommerce Agent",
                "description": "AI agent for conversational ecommerce control",
                "version": "0.1.0",
                "capabilities": ["chat", "tools", "streaming"],
                "endpoints": {
                    "message": "/a2a/message",
                    "stream": "/a2a/message/stream"
                },
                "tools": [tool["name"] for tool in agent.tools],
                "limits": {
                    "max_message_length": 2000,
                    "max_context_id_length": 100
                },
                "supported_events": ["start", "thinking", "text_chunk", "complete", "error", "cancelled"]
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Agent discovery error: {str(e)}")
    
    @app.post("/a2a/message/stream")
    async def stream_message(msg: A2AMessage, request: Request):
        """A2A streaming message endpoint with comprehensive validation"""
        try:
            # Additional request validation
            content_type = request.headers.get("content-type", "")
            if not content_type.startswith("application/json"):
                raise HTTPException(
                    status_code=400, 
                    detail="Content-Type must be application/json"
                )
            
            # Check if agent is healthy
            if not hasattr(agent, 'tools'):
                raise HTTPException(
                    status_code=503, 
                    detail="Agent not properly initialized"
                )
            
            return StreamingResponse(
                a2a.stream_response(msg.message, msg.context_id),
                media_type="text/event-stream",
                headers={
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "X-A2A-Version": "1.0"
                }
            )
        except ValueError as e:
            # Handle Pydantic validation errors
            raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        except Exception as e:
            # Handle any other errors
            raise HTTPException(status_code=500, detail=f"Server error: {str(e)}") 