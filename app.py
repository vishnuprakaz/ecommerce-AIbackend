from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, validator, Field
import os
from dotenv import load_dotenv
from agent import EcommerceAgent
from a2a_server import add_a2a_routes
from typing import Dict, Any, Optional
import re

load_dotenv()

# Initialize the ecommerce agent
agent = EcommerceAgent()

app = FastAPI(
    title="Ecommerce Agent",
    description="AI agent for conversational ecommerce",
    version="0.1.0"
)

# Add A2A protocol routes
add_a2a_routes(app, agent)

class ChatMessage(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000, description="User message")
    user_id: str = Field("anonymous", max_length=50, description="User identifier")
    
    @validator('message')
    def validate_message(cls, v):
        if not v or not v.strip():
            raise ValueError('Message cannot be empty')
        return v.strip()
    
    @validator('user_id') 
    def validate_user_id(cls, v):
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('User ID can only contain letters, numbers, hyphens, and underscores')
        return v

class ToolRequest(BaseModel):
    tool_name: str = Field(..., min_length=1, max_length=50)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    
    @validator('tool_name')
    def validate_tool_name(cls, v):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', v):
            raise ValueError('Tool name must be a valid identifier')
        return v

@app.get("/")
async def root():
    return {
        "message": "Ecommerce Agent API", 
        "a2a_discovery": "/.well-known/agent.json",
        "test_client": "/test"
    }

@app.get("/test", response_class=HTMLResponse)
async def test_client():
    """Serve the HTML test client for streaming"""
    try:
        with open("test_client.html", "r") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Test client not found")

@app.get("/health")
async def health():
    try:
        # Check if OpenAI is configured
        api_key = os.getenv("OPENAI_API_KEY")
        return {
            "status": "ok",
            "openai_configured": bool(api_key and api_key != "your_api_key_here"),
            "tools_loaded": len(agent.tools),
            "a2a_enabled": True,
            "agent_mode": "openai" if agent.is_openai_available() else "mock"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")

@app.post("/chat")
async def chat(msg: ChatMessage):
    """Legacy chat endpoint - use /a2a/message/stream for A2A protocol"""
    try:
        # Validate agent is ready
        if not hasattr(agent, 'tools'):
            raise HTTPException(status_code=503, detail="Agent not ready")
        
        # Use the agent to process the message
        result = agent.process_message(msg.message)
        
        return {
            "response": result["response"],
            "user_id": msg.user_id,
            "status": result["status"],
            "tools_available": result.get("tools_available", 0),
            "note": "For streaming responses, use /a2a/message/stream"
        }
    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")

@app.get("/tools")
async def get_tools():
    """Get available tools"""
    try:
        return {
            "tools": agent.tools,
            "count": len(agent.tools),
            "agent_mode": "openai" if agent.is_openai_available() else "mock"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching tools: {str(e)}")

@app.post("/tools/execute")
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
        
        result = agent.execute_tool(request.tool_name, request.parameters)
        return result
    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing tool: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 