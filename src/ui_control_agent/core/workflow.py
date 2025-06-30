"""
Core workflow implementation for UI Control Agent
Handles conversation flow and tool execution with dual backend/UI approach
"""

import json
import logging
from typing import Any, Dict, List, Optional, AsyncGenerator
from dataclasses import dataclass

from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from pydantic import BaseModel, Field, create_model

from .config import AgentConfig
from .backend_tools import BackendTools
from .memory import ConversationMemory

logger = logging.getLogger(__name__)


@dataclass
class WorkflowState:
    """Simple state for workflow tracking"""
    messages: List[Any]
    user_input: str
    response: str
    completed: bool = False
    iteration: int = 0


class UIControlWorkflow:
    """Simplified workflow for UI control operations without LangGraph"""
    
    def __init__(self, agent_or_config, memory: ConversationMemory = None):
        # Handle both agent object and config object
        if hasattr(agent_or_config, 'config'):
            # It's an agent object
            self.config = agent_or_config.config
            self.agent = agent_or_config
        else:
            # It's a config object
            self.config = agent_or_config
            self.agent = None
        
        self.memory = memory
        self.backend_tools = BackendTools()
        
        # Initialize OpenAI model
        self.llm = ChatOpenAI(
            model=self.config.openai_model,
            temperature=0.1,
            max_tokens=2000
        )
        
        # Create backend tools
        self.available_backend_tools = self._create_backend_tools()
        
        # Load UI tools configuration
        self.ui_tools = self._load_ui_tools()
        
        logger.info(f"Workflow initialized with {len(self.available_backend_tools)} backend tools and {len(self.ui_tools)} UI tools")
    
    def _create_backend_tools(self):
        """Create backend tools for direct data execution"""
        backend_tools = []
        
        # Search products data tool  
        if "search_products_data" in self.config.backend_tool_functions:
            @tool
            def search_products_data(query: str, category: str = None, max_price: float = None, limit: int = 10) -> dict:
                """Search for products and return actual product data with details"""
                filters = {}
                if category: filters["category"] = category
                if max_price: filters["max_price"] = max_price
                if limit: filters["limit"] = limit
                
                return self.backend_tools.search_products_data(query, **filters)
            backend_tools.append(search_products_data)
        
        logger.info(f"Created {len(backend_tools)} backend tools")
        return backend_tools
    
    def _load_ui_tools(self):
        """Load UI tools configuration"""
        try:
            with open("tools.json", "r") as f:
                tools_config = json.load(f)
            return tools_config.get("tools", [])
        except Exception as e:
            logger.error(f"Failed to load UI tools: {e}")
            return []
    
    def _create_all_tools(self):
        """Create all tools in LangChain format with proper schemas"""
        all_tools = []
        
        # Create UI tools with proper parameter schemas
        for tool_config in self.ui_tools:
            tool_name = tool_config["name"]
            tool_desc = tool_config["description"]
            tool_params = tool_config.get("parameters", {})
            
            # Convert JSON schema to Pydantic model
            pydantic_fields = {}
            properties = tool_params.get("properties", {})
            required = tool_params.get("required", [])
            
            for param_name, param_config in properties.items():
                param_type = param_config.get("type", "string")
                param_desc = param_config.get("description", "")
                
                # Map JSON types to Python types
                if param_type == "string":
                    field_type = str
                elif param_type == "number":
                    field_type = float
                elif param_type == "integer":
                    field_type = int
                elif param_type == "boolean":
                    field_type = bool
                else:
                    field_type = str
                
                # Handle optional fields
                if param_name not in required:
                    field_type = Optional[field_type]
                    pydantic_fields[param_name] = (field_type, Field(default=None, description=param_desc))
                else:
                    pydantic_fields[param_name] = (field_type, Field(description=param_desc))
            
            # Create Pydantic model dynamically
            PydanticModel = create_model(f"{tool_name.title()}Input", **pydantic_fields)
            
            # Create tool with proper schema
            def create_ui_tool(name, description, schema):
                @tool(description=description, args_schema=schema)
                def ui_tool(**kwargs) -> dict:
                    """UI tool that returns action events"""
                    return {
                        "tool_type": "ui_action",
                        "function": name,
                        "parameters": kwargs,
                        "description": f"Executing {name} on the UI"
                    }
                ui_tool.name = name  # Set the name explicitly
                return ui_tool
            
            ui_tool = create_ui_tool(tool_name, tool_desc, PydanticModel)
            all_tools.append(ui_tool)
        
        # Add backend tools
        all_tools.extend(self.available_backend_tools)
        
        logger.info(f"Created {len(all_tools)} total tools for LLM (UI: {len(self.ui_tools)}, Backend: {len(self.available_backend_tools)})")
        return all_tools
    
    async def process_message(self, user_query: str, context_id: str = None) -> dict:
        """Enhanced message processing with actual tool execution"""
        try:
            # Create all tools
            all_tools = self._create_all_tools()
            
            # Bind tools to LLM
            llm_with_tools = self.llm.bind_tools(all_tools)
            
            # Create system prompt
            system_prompt = f"""
{self.config.get_system_prompt()}

You are a helpful UI control agent. When users ask you to do something, USE THE TOOLS to take action.

Available Tools:
- navigate: Navigate between pages (home, products, cart, checkout, account)  
- search_products: Display search results on the UI
- search_products_data: Get real product data

CRITICAL INSTRUCTIONS:
- For navigation requests: Use the navigate tool with the correct page parameter
- For search requests: ALWAYS use BOTH tools:
  1. First call search_products_data to get the actual product data
  2. Then call search_products to display the results on the UI
- Always provide helpful conversational responses explaining what you did

Example for "search for red dresses":
1. Call search_products_data(query="red dresses") 
2. Call search_products(query="red dresses")
3. Respond with details about what was found

Always use tools when appropriate, don't just describe what you would do.
"""
            
            # Prepare messages
            messages = [
                HumanMessage(content=system_prompt),
                HumanMessage(content=user_query)
            ]
            
            # Get response from LLM with tools
            response = llm_with_tools.invoke(messages)
            
            # Process tool calls if any
            actions = []
            data_events = []
            
            if hasattr(response, 'tool_calls') and response.tool_calls:
                for tool_call in response.tool_calls:
                    tool_name = tool_call["name"]
                    tool_args = tool_call["args"]
                    
                    # Execute the tool
                    for tool in all_tools:
                        if tool.name == tool_name:
                            try:
                                result = tool.func(**tool_args)
                                
                                # Handle UI tools (generate actions)
                                if isinstance(result, dict) and result.get("tool_type") == "ui_action":
                                    actions.append({
                                        "function": result["function"],
                                        "params": result["parameters"],
                                        "description": result["description"]
                                    })
                                
                                # Handle backend tools (generate data events)
                                elif "products" in str(result):
                                    data_events.append({
                                        "source": "products",
                                        "payload": result
                                    })
                                    
                            except Exception as e:
                                logger.error(f"Tool execution error: {e}")
                            break
            
            return {
                "response": response.content,
                "status": "success",
                "actions": actions,
                "data_events": data_events,
                "tools_used": [tc["name"] for tc in response.tool_calls] if hasattr(response, 'tool_calls') and response.tool_calls else []
            }
            
        except Exception as e:
            logger.error(f"Workflow processing error: {e}")
            return {
                "response": f"I apologize, but I encountered an error: {str(e)}",
                "status": "error",
                "actions": [],
                "data_events": [],
                "tools_used": []
            }
    
    async def stream_workflow(self, user_query: str, context_id: str = None) -> AsyncGenerator[str, None]:
        """Enhanced streaming implementation with action events"""
        try:
            # Yield initial status
            yield json.dumps({
                "event_type": "status",
                "data": {"status": "working", "message": "Processing your request..."}
            }) + "\n"
            
            # Process the message with tools
            result = await self.process_message(user_query, context_id)
            
            # Emit action events first
            for action in result.get("actions", []):
                yield json.dumps({
                    "event_type": "action",
                    "data": action
                }) + "\n"
            
            # Emit data events
            for data_event in result.get("data_events", []):
                yield json.dumps({
                    "event_type": "data", 
                    "data": data_event
                }) + "\n"
            
            # Emit final response
            yield json.dumps({
                "event_type": "response", 
                "data": {"text": result["response"], "final": True}
            }) + "\n"
            
            # Final status
            yield json.dumps({
                "event_type": "status",
                "data": {"status": "complete", "message": "Task completed"}
            }) + "\n"
            
        except Exception as e:
            logger.error(f"Stream workflow error: {e}")
            yield json.dumps({
                "event_type": "status",
                "data": {"status": "error", "message": str(e)}
            }) + "\n" 