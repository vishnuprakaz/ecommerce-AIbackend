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
🚧 Working on A2A protocol integration  

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

# Chat with the agent
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "show me red handbags under $100"}'

# View available tools
curl http://localhost:8000/tools
```

## Current Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check (shows OpenAI config and tools loaded)
- `POST /chat` - Chat with the ecommerce agent
- `GET /tools` - View available tools

## Available Tools

The agent currently has these tools configured:
- **navigate** - Navigate to different pages
- **search_products** - Search for products with filters  
- **add_to_cart** - Add products to cart

## Next Steps

- [ ] Add A2A protocol server endpoints
- [ ] Implement streaming responses 
- [ ] Add LangGraph workflow for complex tool orchestration
- [ ] Create tool execution handlers
- [ ] Add context/session management

## Project Structure

```
ecommerce-backend/
├── app.py              # FastAPI application
├── agent.py            # Main agent logic
├── tools.json          # Tool configurations
├── pyproject.toml      # Dependencies
└── README.md           # This file
```

## Notes

This is part of a larger ecommerce project. The frontend will consume the A2A streams to update the UI in real-time.

Still experimenting with the architecture - might refactor into a more organized structure as it grows. 