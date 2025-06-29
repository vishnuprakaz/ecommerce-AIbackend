# Development TODO

## 🔥 Critical Issues - SPRINT 2 FOCUS
- [x] ✅ **Code Restructure** - Reorganize into proper modules (agents/, tools/, a2a/, server/)
- [x] ✅ **Fix Pydantic Deprecation** - Migrate from V1 `@validator` to V2 `@field_validator`
- [x] ✅ **Fix A2A Async Streaming** - Resolve async generator issue in streaming responses
- [ ] **LangGraph Integration** - Add proper agent workflows with function calling
- [ ] **Tool Parameter Validation** - Enhanced validation with proper schemas

## ✅ Sprint 1 - Core Functionality - COMPLETE! 
- [x] ✅ Fix OpenAI initialization - app crashes without API key, should gracefully handle missing keys
- [x] ✅ Tool execution is returning mock data - need actual implementations
- [x] ✅ Add proper error handling for malformed A2A requests
- [x] ✅ Implement basic tool handlers (navigate, search_products, add_to_cart)
- [x] ✅ Add request validation and error responses
- [x] ✅ Create simple HTML test client for streaming endpoint
- [x] ✅ Add basic logging (replace print statements)

## 🧠 Sprint 2 - Smart Agent & Clean Architecture (MOSTLY COMPLETE)
- [x] ✅ **Restructure codebase** into proper modules:
  - [x] ✅ `src/ecommerce_agent/models/` - Pydantic models and schemas
  - [x] ✅ `src/ecommerce_agent/core/` - Agent logic and configuration
  - [x] ✅ `src/ecommerce_agent/tools/` - Tool registry and handlers
  - [x] ✅ `src/ecommerce_agent/a2a/` - A2A protocol implementation
  - [x] ✅ `src/ecommerce_agent/server/` - FastAPI server and routes
- [x] ✅ Migrate to Pydantic V2 `@field_validator` 
- [ ] Integrate LangGraph for proper agent workflows
- [ ] Add function calling to OpenAI requests (currently just chat)
- [ ] Implement enhanced tool parameter validation
- [ ] Add conversation context/memory

## 🔧 Sprint 3 - Production Ready
- [ ] Session management for multi-turn conversations
- [ ] Rate limiting for OpenAI API calls
- [ ] Add more ecommerce tools (filters, sorting, wishlist)
- [ ] Database setup for session storage

## ✅ Testing & Quality
- [ ] Unit tests for agent and tool logic
- [ ] Integration tests for A2A streaming
- [ ] Add basic monitoring/health checks
- [ ] Performance testing for streaming

## 📦 Deployment
- [ ] Docker setup 
- [ ] Environment configuration management
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Demo frontend app

## 🐛 Known Issues
- ~~A2A streaming has async generator issue~~ ✅ Fixed - streaming now works perfectly!
- ~~Need to clean up old files after restructuring~~ ✅ Done - old files removed
- A2A streaming chunks might be too fast/slow - need testing

## 📝 Development Notes
- OpenAI integration working perfectly with real API key! 🎉
- **MAJOR RESTRUCTURE COMPLETE** - Clean modular architecture! 🏗️
- Pydantic V2 migration complete - no more deprecation warnings
- Tool handlers in separate module with proper separation of concerns
- A2A protocol properly modularized
- Server components cleanly organized with middleware
- Configuration management centralized
- HTML test client moved to static/ directory
- LangGraph will enable much more sophisticated agent workflows

## 🎯 Current Focus
🎉 **Major Restructure Complete!** Clean modular architecture with proper separation of concerns. Next: Fix A2A streaming and integrate LangGraph for advanced workflows.

---
*Last updated: Code restructuring session* 