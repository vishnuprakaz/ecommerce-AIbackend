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

✅ Basic FastAPI app with agent integration  
✅ OpenAI chat completion working  
✅ Tool loading from JSON configuration  
✅ A2A protocol server with streaming responses  
🚧 Working on LangGraph workflow integration  

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
# Health check
curl http://localhost:8000/health

# A2A agent discovery
curl http://localhost:8000/.well-known/agent.json

# Legacy chat endpoint
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "show me red handbags under $100"}'

# A2A streaming chat (use SSE client or browser)
curl -X POST http://localhost:8000/a2a/message/stream \
  -H "Content-Type: application/json" \
  -d '{"message": "find me some red bags", "context_id": "test123"}'
```

## Current Endpoints

### Core Endpoints
- `GET /` - Root endpoint with A2A discovery link
- `GET /health` - Health check (shows OpenAI config, tools loaded, A2A status)
- `GET /tools` - View available tools

### Chat Endpoints
- `POST /chat` - Legacy chat endpoint (non-streaming)
- `POST /a2a/message/stream` - A2A streaming chat with SSE

### A2A Protocol
- `GET /.well-known/agent.json` - Agent discovery (A2A standard)

## Available Tools

The agent currently has these tools configured:
- **navigate** - Navigate to different pages
- **search_products** - Search for products with filters  
- **add_to_cart** - Add products to cart

## A2A Streaming Events

The streaming endpoint sends these event types:
- `start` - Stream initialization
- `thinking` - Agent processing status
- `text_chunk` - Response text chunks
- `complete` - Stream completion with metadata
- `error` - Error handling

## Next Steps

- [ ] Add LangGraph workflow for complex tool orchestration
- [ ] Implement actual tool execution handlers
- [ ] Add context/session management
- [ ] Create more sophisticated ecommerce tools
- [ ] Add user authentication

## Project Structure

```
ecommerce-backend/
├── app.py              # FastAPI application
├── agent.py            # Main agent logic
├── a2a_server.py       # A2A protocol server
├── tools.json          # Tool configurations
├── pyproject.toml      # Dependencies
└── README.md           # This file
```

## Notes

This is part of a larger ecommerce project. The frontend will consume the A2A streams to update the UI in real-time.

The A2A protocol implementation follows the standard for agent-to-agent communication. Still experimenting with the best architecture as this grows. 