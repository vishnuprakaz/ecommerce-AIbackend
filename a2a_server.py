import json
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Dict, Any, AsyncGenerator
from agent import EcommerceAgent

class A2AMessage(BaseModel):
    message: str
    context_id: str = None
    stream: bool = True

class A2AServer:
    def __init__(self, agent: EcommerceAgent):
        self.agent = agent
    
    async def stream_response(self, message: str, context_id: str = None) -> AsyncGenerator[str, None]:
        """Stream A2A protocol responses"""
        
        # Start event
        yield f"data: {json.dumps({'event': 'start', 'context_id': context_id})}\n\n"
        
        # Thinking event
        yield f"data: {json.dumps({'event': 'thinking', 'content': 'Processing your request...'})}\n\n"
        await asyncio.sleep(0.1)  # Small delay for realistic feel
        
        try:
            # Process with agent
            result = self.agent.process_message(message)
            
            # Stream the response in chunks
            response_text = result["response"]
            words = response_text.split()
            
            for i, word in enumerate(words):
                chunk_data = {
                    "event": "text_chunk",
                    "content": word + " ",
                    "chunk_id": i
                }
                yield f"data: {json.dumps(chunk_data)}\n\n"
                await asyncio.sleep(0.05)  # Realistic typing speed
            
            # Complete event
            complete_data = {
                "event": "complete",
                "context_id": context_id,
                "status": result["status"],
                "tools_available": result.get("tools_available", 0)
            }
            yield f"data: {json.dumps(complete_data)}\n\n"
            
        except Exception as e:
            # Error event
            error_data = {
                "event": "error",
                "error": str(e),
                "context_id": context_id
            }
            yield f"data: {json.dumps(error_data)}\n\n"

def add_a2a_routes(app: FastAPI, agent: EcommerceAgent):
    """Add A2A protocol routes to FastAPI app"""
    a2a = A2AServer(agent)
    
    @app.get("/.well-known/agent.json")
    async def agent_discovery():
        """A2A agent discovery endpoint"""
        return {
            "name": "Ecommerce Agent",
            "description": "AI agent for conversational ecommerce control",
            "version": "0.1.0",
            "capabilities": ["chat", "tools", "streaming"],
            "endpoints": {
                "message": "/a2a/message",
                "stream": "/a2a/message/stream"
            },
            "tools": [tool["name"] for tool in agent.tools]
        }
    
    @app.post("/a2a/message/stream")
    async def stream_message(msg: A2AMessage):
        """A2A streaming message endpoint"""
        return StreamingResponse(
            a2a.stream_response(msg.message, msg.context_id),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Access-Control-Allow-Origin": "*",
            }
        ) 