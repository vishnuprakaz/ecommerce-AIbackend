"""
LangGraph workflow for ecommerce agent with iterative tool calling
"""

from typing import Dict, Any, List, Optional, TypedDict, AsyncGenerator
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from pydantic import BaseModel, Field
import json
import logging
import asyncio

logger = logging.getLogger(__name__)


# Pydantic models for tool schemas
class NavigationInput(BaseModel):
    """Input schema for navigation tool"""
    page: str = Field(description="Page to navigate to (home, products, cart, checkout)")
    category: Optional[str] = Field(default=None, description="Product category (optional)")


class ProductSearchInput(BaseModel):
    """Input schema for product search tool"""
    query: str = Field(description="Search query for products")
    max_price: Optional[float] = Field(default=None, description="Maximum price filter")
    min_price: Optional[float] = Field(default=None, description="Minimum price filter")
    color: Optional[str] = Field(default=None, description="Color filter")


class AddToCartInput(BaseModel):
    """Input schema for add to cart tool"""
    product_id: str = Field(description="ID of the product to add")
    quantity: int = Field(default=1, description="Quantity to add")


class AgentState(TypedDict):
    """State for the agent workflow"""
    messages: List[Dict[str, Any]]
    user_query: str
    context_id: Optional[str]
    iteration: int
    tool_calls_made: List[Dict[str, Any]]
    final_answer: Optional[str]
    streaming_chunks: List[str]


class EcommerceWorkflow:
    """LangGraph workflow for ecommerce agent with iterative tool execution"""
    
    def __init__(self, agent):
        self.agent = agent
        self.tools = self._create_langchain_tools()
        self.workflow = self._build_workflow()
    
    def _create_langchain_tools(self):
        """Convert our ecommerce tools to LangChain format"""
        from ..tools.handlers import ToolHandlers
        
        handlers = ToolHandlers()
        
        @tool(args_schema=NavigationInput)
        def navigate(page: str, category: str = None) -> dict:
            """Navigate to different pages in the ecommerce site."""
            import uuid
            from datetime import datetime
            request_id = str(uuid.uuid4())[:8]
            timestamp = datetime.now().isoformat()
            return handlers.handle_navigation(
                {"page": page, "category": category}, 
                request_id, 
                timestamp
            )
        
        @tool(args_schema=ProductSearchInput)
        def search_products(query: str, max_price: float = None, min_price: float = None, color: str = None) -> dict:
            """Search for products in the ecommerce store."""
            import uuid
            from datetime import datetime
            request_id = str(uuid.uuid4())[:8]
            timestamp = datetime.now().isoformat()
            
            filters = {}
            if max_price: filters["max_price"] = max_price
            if min_price: filters["min_price"] = min_price
            if color: filters["color"] = color
            
            return handlers.handle_product_search(
                {"query": query, "filters": filters},
                request_id,
                timestamp
            )
        
        @tool(args_schema=AddToCartInput)
        def add_to_cart(product_id: str, quantity: int = 1) -> dict:
            """Add a product to the shopping cart."""
            import uuid
            from datetime import datetime
            request_id = str(uuid.uuid4())[:8]
            timestamp = datetime.now().isoformat()
            return handlers.handle_add_to_cart(
                {"product_id": product_id, "quantity": quantity},
                request_id,
                timestamp
            )
        
        return [navigate, search_products, add_to_cart]
    
    def _build_workflow(self) -> StateGraph:
        """Build the LangGraph workflow"""
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("agent", self._agent_node)
        workflow.add_node("tools", self._tool_node)
        
        # Set entry point
        workflow.set_entry_point("agent")
        
        # Add conditional edges
        workflow.add_conditional_edges(
            "agent",
            self._should_continue,
            {
                "tools": "tools",
                "end": END
            }
        )
        
        # Tools always go back to agent
        workflow.add_edge("tools", "agent")
        
        return workflow.compile()
    
    async def _agent_node(self, state: AgentState) -> AgentState:
        """Agent reasoning node with function calling"""
        logger.info(f"Agent node - iteration {state['iteration']}")
        
        # Build message history
        messages = []
        
        # System message
        system_msg = """You are an AI assistant for an ecommerce website. You can help users with:
- Navigating to different pages 
- Searching for products with filters
- Adding products to cart

You have access to tools and should use them to help users accomplish their goals.
When you have completed the user's request and don't need any more tools, provide a final helpful response."""
        
        # Add user query
        if state["iteration"] == 1:
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": state["user_query"]})
        
        # Add conversation history
        messages.extend(state["messages"])
        
        try:
            # Get OpenAI response with function calling
            response = self.agent.openai_client.chat.completions.create(
                model=self.agent.config.openai_model,
                messages=messages,
                tools=[self._tool_to_openai_format(tool) for tool in self.tools],
                tool_choice="auto",
                max_tokens=500
            )
            
            response_message = response.choices[0].message
            
            # Add AI response to state
            new_messages = state["messages"].copy()
            
            ai_message = {
                "role": "assistant",
                "content": response_message.content or ""
            }
            
            # Handle tool calls
            if response_message.tool_calls:
                ai_message["tool_calls"] = [
                    {
                        "id": tool_call.id,
                        "type": "function",
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    }
                    for tool_call in response_message.tool_calls
                ]
                
                # Track tool calls
                tool_calls_made = state["tool_calls_made"].copy()
                for tool_call in response_message.tool_calls:
                    tool_calls_made.append({
                        "iteration": state["iteration"],
                        "tool": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    })
                
                state["tool_calls_made"] = tool_calls_made
            
            new_messages.append(ai_message)
            
            return {
                **state,
                "messages": new_messages,
                "iteration": state["iteration"] + 1
            }
            
        except Exception as e:
            logger.error(f"Error in agent node: {e}")
            # Fallback response
            new_messages = state["messages"].copy()
            new_messages.append({
                "role": "assistant", 
                "content": f"I encountered an error: {str(e)}. How else can I help you?"
            })
            
            return {
                **state,
                "messages": new_messages,
                "final_answer": f"Error: {str(e)}",
                "iteration": state["iteration"] + 1
            }
    
    async def _tool_node(self, state: AgentState) -> AgentState:
        """Tool execution node"""
        logger.info(f"Tool node - iteration {state['iteration']}")
        
        last_message = state["messages"][-1]
        tool_calls = last_message.get("tool_calls", [])
        
        new_messages = state["messages"].copy()
        
        for tool_call in tool_calls:
            try:
                # Parse tool call
                tool_name = tool_call["function"]["name"]
                tool_args = json.loads(tool_call["function"]["arguments"])
                
                logger.info(f"Executing tool: {tool_name} with args: {tool_args}")
                
                # Execute tool
                tool_result = None
                for tool in self.tools:
                    if tool.name == tool_name:
                        tool_result = await asyncio.to_thread(tool.func, **tool_args)
                        break
                
                if tool_result is None:
                    tool_result = {"error": f"Tool {tool_name} not found"}
                
                # Add tool result to messages
                tool_message = {
                    "role": "tool",
                    "content": json.dumps(tool_result, default=str),
                    "tool_call_id": tool_call["id"]
                }
                new_messages.append(tool_message)
                
            except Exception as e:
                logger.error(f"Tool execution error: {e}")
                tool_message = {
                    "role": "tool",
                    "content": json.dumps({"error": str(e)}),
                    "tool_call_id": tool_call["id"]
                }
                new_messages.append(tool_message)
        
        return {
            **state,
            "messages": new_messages
        }
    
    def _should_continue(self, state: AgentState) -> str:
        """Decide whether to continue with tools or end"""
        last_message = state["messages"][-1]
        
        # If last message has tool calls, go to tools
        if last_message.get("tool_calls"):
            return "tools"
        
        # If we've reached max iterations, end
        if state["iteration"] > 10:  # Safety limit
            return "end"
        
        # Otherwise, end the conversation
        return "end"
    
    def _tool_to_openai_format(self, tool) -> dict:
        """Convert LangChain tool to OpenAI function format"""
        return {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.args_schema.schema() if tool.args_schema else {"type": "object", "properties": {}}
            }
        }
    
    async def stream_workflow(self, user_query: str, context_id: str = None) -> AsyncGenerator[str, None]:
        """Stream the entire workflow execution"""
        
        # Initialize state
        initial_state = AgentState(
            messages=[],
            user_query=user_query,
            context_id=context_id,
            iteration=1,
            tool_calls_made=[],
            final_answer=None,
            streaming_chunks=[]
        )
        
        try:
            # Start event
            yield f"data: {json.dumps({'event': 'workflow_start', 'context_id': context_id, 'query': user_query})}\n\n"
            
            # Run workflow and track state
            async for output in self.workflow.astream(initial_state):
                for node_name, node_output in output.items():
                    # Update final state
                    final_state = node_output
                    
                    if node_name == "agent":
                        # Stream agent thinking
                        yield f"data: {json.dumps({'event': 'agent_thinking', 'iteration': node_output['iteration'], 'context_id': context_id})}\n\n"
                        
                        # Check for tool calls
                        if node_output["messages"] and node_output["messages"][-1].get("tool_calls"):
                            tool_calls = node_output["messages"][-1]["tool_calls"]
                            yield f"data: {json.dumps({'event': 'tool_calls_planned', 'tool_calls': [tc['function']['name'] for tc in tool_calls], 'context_id': context_id})}\n\n"
                        
                        # Stream partial response if available
                        if node_output["messages"] and node_output["messages"][-1].get("content"):
                            content = node_output["messages"][-1]["content"]
                            if content and not node_output["messages"][-1].get("tool_calls"):
                                # Only stream content if there are no tool calls (final response)
                                yield f"data: {json.dumps({'event': 'final_response', 'content': content, 'iteration': node_output['iteration'], 'context_id': context_id})}\n\n"
                    
                    elif node_name == "tools":
                        # Stream tool execution
                        yield f"data: {json.dumps({'event': 'tools_executing', 'context_id': context_id})}\n\n"
                        
                        # Get tool results from the last tool messages
                        tool_messages = [msg for msg in node_output["messages"] if msg.get("role") == "tool"]
                        if tool_messages:
                            # Count new tool results
                            latest_results = [msg for msg in node_output["messages"][-5:] if msg.get("role") == "tool"]
                            yield f"data: {json.dumps({'event': 'tool_results', 'results': len(latest_results), 'context_id': context_id})}\n\n"
            
            # Track final state during iteration
            final_state = initial_state
            
            # Complete event
            yield f"data: {json.dumps({'event': 'workflow_complete', 'iterations': final_state.get('iteration', 1), 'tool_calls_made': len(final_state.get('tool_calls_made', [])), 'context_id': context_id})}\n\n"
            
        except Exception as e:
            logger.error(f"Workflow streaming error: {e}")
            yield f"data: {json.dumps({'event': 'workflow_error', 'error': str(e), 'context_id': context_id})}\n\n" 