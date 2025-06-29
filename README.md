# Ecommerce Agent Backend

Building an AI agent for conversational ecommerce using A2A protocol and LangGraph.

## What I'm Building

Trying to create an AI agent that can control ecommerce UIs through natural language. User says "show me red bags under $100" and the agent navigates, filters, and manipulates the interface automatically.

## Tech Stack

- A2A Protocol for agent communication
- LangGraph for workflow management  
- OpenAI for the LLM
- FastAPI for the backend
- UV for Python package management

## Status

✅ Basic FastAPI app with agent integration  
✅ OpenAI chat completion working  
✅ Tool loading from JSON configuration  
✅ A2A protocol server with streaming responses  
✅ Proper UV project setup with dependencies  
🚧 Working on LangGraph workflow integration  

## Setup

1. Install UV (if you haven't already):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone and set up the project:
```bash
git clone <your-repo>
cd ecommerce-backend
```

3. Install dependencies (uv handles virtual env automatically):
```bash
uv sync
```

4. Set up environment:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

5. Run the app:
```bash
uv run python app.py
```

6. Test it:
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

## Development Commands

```bash
# Run the app
uv run python app.py

# Install new dependencies
uv add package_name

# Run with different Python versions
uv run --python 3.11 python app.py

# Run tests (when we add them)
uv run pytest

# Check dependencies
uv tree
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
├── pyproject.toml      # UV project configuration
├── uv.lock             # UV dependency lock file
├── .venv/              # Virtual environment (created by uv)
└── README.md           # This file
```

## Notes

This is part of a larger ecommerce project. The frontend will consume the A2A streams to update the UI in real-time.

The A2A protocol implementation follows the standard for agent-to-agent communication. Using UV for fast, reliable Python package management - much better than pip/venv! 