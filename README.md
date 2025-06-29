# Ecommerce Agent Backend

Building an AI agent for conversational ecommerce using A2A protocol and LangGraph.

## What I'm Building

Trying to create an AI agent that can control ecommerce UIs through natural language. User says "show me red bags under $100" and the agent navigates, filters, and manipulates the interface automatically.

## Tech Stack

- A2A Protocol for agent communication
- LangGraph for workflow management  
- OpenAI for the LLM
- FastAPI for the backend

## Status

�� Work in progress - basic FastAPI app is working

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Set up environment:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

3. Run the app:
```bash
uv run python app.py
```

4. Test it:
```bash
curl http://localhost:8000/health
```

## Current Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /chat` - Basic chat (placeholder for now)

## Next Steps

- [ ] Add OpenAI integration
- [ ] Implement A2A protocol
- [ ] Add LangGraph workflows
- [ ] Create tool handlers for ecommerce actions

## Notes

This is part of a larger ecommerce project. The frontend will consume the A2A streams to update the UI in real-time. 