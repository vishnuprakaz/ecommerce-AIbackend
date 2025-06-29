from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
        "openai_configured": bool(api_key and api_key != "your_api_key_here")
    }

@app.post("/chat")
async def chat(msg: ChatMessage):
    try:
        # Create a simple chat completion
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant for an ecommerce website. Help users find products and navigate the site."},
                {"role": "user", "content": msg.message}
            ],
            max_tokens=150
        )
        
        return {
            "response": response.choices[0].message.content,
            "user_id": msg.user_id,
            "model": "gpt-3.5-turbo"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 