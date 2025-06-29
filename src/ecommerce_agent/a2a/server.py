"""
A2A (Agent-to-Agent) protocol server implementation
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator, Dict, Any
import json
import time
import logging
from ..models.requests import A2AMessage

logger = logging.getLogger(__name__)


class A2AServer:
    """A2A protocol server for handling agent communication"""
    
    def __init__(self, agent):
        self.agent = agent
    
    async def stream_response(self, message: A2AMessage) -> AsyncGenerator[str, None]:
        """Stream A2A response with SSE format"""
        try:
            start_time = time.time()
            
            # Start event
            yield f"data: {json.dumps({'event': 'start', 'context_id': message.context_id, 'timestamp': start_time})}\n\n"
            
            # Thinking event
            yield f"data: {json.dumps({'event': 'thinking', 'content': 'Processing your request...', 'context_id': message.context_id})}\n\n"
            
            # Get response from agent
            if not self.agent.is_openai_available():
                # Mock streaming for development
                mock_response = f"🤖 Mock A2A response to: '{message.message}' (OpenAI not configured)"
                async for chunk in self._stream_text_chunks(mock_response, message.context_id):
                    yield chunk
            else:
                # Real OpenAI streaming
                async for chunk in self._stream_openai_response(message):
                    yield chunk
            
            # Complete event
            response_length = len(message.message.split()) * 8  # Rough estimate
            yield f"data: {json.dumps({'event': 'complete', 'context_id': message.context_id, 'status': 'success', 'tools_available': len(self.agent.tools), 'message_length': len(message.message.split()), 'response_length': response_length})}\n\n"
            
        except Exception as e:
            logger.error(f"Error in A2A streaming: {e}")
            error_data = {
                'event': 'error', 
                'error': str(e), 
                'context_id': message.context_id,
                'timestamp': time.time()
            }
            yield f"data: {json.dumps(error_data)}\n\n"
    
    async def _stream_text_chunks(self, text: str, context_id: str) -> AsyncGenerator[str, None]:
        """Stream text as individual word chunks"""
        import asyncio
        words = text.split()
        for i, word in enumerate(words):
            chunk_data = {
                'event': 'text_chunk',
                'content': word + (' ' if i < len(words) - 1 else ''),
                'chunk_id': i,
                'context_id': context_id
            }
            yield f"data: {json.dumps(chunk_data)}\n\n"
            # Small delay to simulate streaming
            await asyncio.sleep(0.05)
    
    async def _stream_openai_response(self, message: A2AMessage) -> AsyncGenerator[str, None]:
        """Stream response from OpenAI with proper chunking"""
        try:
            # Create system prompt with tool descriptions
            tool_descriptions = "\n".join([
                f"- {tool['name']}: {tool['description']}" 
                for tool in self.agent.tools
            ])
            
            system_prompt = f"""You are an AI assistant for an ecommerce website. 
You can help users with these actions:
{tool_descriptions}

When a user asks for something, determine if you need to use any tools and respond accordingly.
Provide helpful, conversational responses about ecommerce tasks."""

            response = self.agent.openai_client.chat.completions.create(
                model=self.agent.config.openai_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message.message}
                ],
                max_tokens=500,
                stream=True
            )
            
            chunk_id = 0
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    chunk_data = {
                        'event': 'text_chunk',
                        'content': content,
                        'chunk_id': chunk_id,
                        'context_id': message.context_id
                    }
                    yield f"data: {json.dumps(chunk_data)}\n\n"
                    chunk_id += 1
                    
        except Exception as e:
            logger.error(f"Error streaming OpenAI response: {e}")
            # Fallback to mock response
            mock_response = f"I'd be happy to help you with '{message.message}'. Let me search for relevant products and information."
            async for chunk in self._stream_text_chunks(mock_response, message.context_id):
                yield chunk


def add_a2a_routes(app: FastAPI, agent):
    """Add A2A protocol routes to the FastAPI app"""
    a2a_server = A2AServer(agent)
    
    @app.get("/.well-known/agent.json")
    async def agent_discovery():
        """A2A agent discovery endpoint"""
        return {
            "name": "Ecommerce Agent",
            "description": "AI agent for conversational ecommerce interactions",
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