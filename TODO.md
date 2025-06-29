# TODO

## Immediate
- [ ] Test the streaming endpoint properly - need to build a simple HTML client  
- [ ] Fix the tool execution - currently just returning mock data
- [ ] Add proper error handling for malformed requests

## Next Sprint
- [ ] LangGraph integration - the current agent is too simple
- [ ] Session management - users lose context between requests  
- [ ] Add more ecommerce tools (filters, sorting, etc.)
- [ ] Rate limiting - don't want to blow through OpenAI credits

## Architecture
- [ ] Might need to refactor into proper modules soon
- [ ] Database for session storage? 
- [ ] Consider using Pydantic models for tool parameters
- [ ] Add logging - using print statements like a noob right now

## Testing
- [ ] Unit tests for agent logic
- [ ] Integration tests for A2A endpoints
- [ ] Load testing for streaming

## Nice to Have
- [ ] Docker setup for easier deployment
- [ ] CI/CD pipeline  
- [ ] Monitoring and observability
- [ ] Frontend demo app

## Bugs
- None found yet but probably lurking somewhere 😅

## Notes
- The A2A streaming works but feels a bit slow - might need to optimize chunk sizes
- Need to research LangGraph patterns more - current approach feels basic
- Should probably add authentication at some point 