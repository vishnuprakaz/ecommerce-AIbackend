from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from agent import EcommerceAgent

load_dotenv()

# Initialize the ecommerce agent
agent = EcommerceAgent()

app = FastAPI(
    title="Ecommerce Agent",
    description="AI agent for conversational ecommerce",
    version="0.1.0"
)

class ChatMessage(BaseModel):
    message: str
    user_id: str = "anonymous"

@app.get("/")
async def root():
    return {"message": "Ecommerce Agent API"}

@app.get("/health")
async def health():
    # Check if OpenAI is configured
    api_key = os.getenv("OPENAI_API_KEY")
    return {
        "status": "ok",
        "openai_configured": bool(api_key and api_key != "your_api_key_here"),
        "tools_loaded": len(agent.tools)
    }

@app.post("/chat")
async def chat(msg: ChatMessage):
    try:
        # Use the agent to process the message
        result = agent.process_message(msg.message)
        
        return {
            "response": result["response"],
            "user_id": msg.user_id,
            "status": result["status"],
            "tools_available": result.get("tools_available", 0)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")

@app.get("/tools")
async def get_tools():
    """Get available tools"""
    return {"tools": agent.tools}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 