from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

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
    return {"status": "ok"}

@app.post("/chat")
async def chat(msg: ChatMessage):
    # TODO: Add actual AI processing here
    return {
        "response": f"You said: {msg.message}",
        "user_id": msg.user_id
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 