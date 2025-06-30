"""
Core UI control agent implementation
"""

import json
import uuid
from typing import Dict, Any, List, Optional, AsyncGenerator
from datetime import datetime
import logging
from openai import OpenAI
from langchain_openai import ChatOpenAI

from .config import AgentConfig
from .workflow import UIControlWorkflow

# Set up logging
logger = logging.getLogger(__name__)


class UIControlAgent:
    """Main UI control agent class for processing messages and executing tools"""
    
    def __init__(self):
        self.config = AgentConfig()
        self.tools = self.load_tools()
        self.openai_client = None
        self.llm = None
        self.workflow = None
        self._init_openai()
    
    def _init_openai(self):
        """Initialize OpenAI clients - required for operation"""
        if not self.config.is_openai_configured():
            logger.error("OpenAI API key not found. Set OPENAI_API_KEY environment variable.")
            logger.error("Agent requires OpenAI API key to function. No mock mode available.")
            return
        
        try:
            self.openai_client = OpenAI(api_key=self.config.openai_api_key)
            self.llm = ChatOpenAI(api_key=self.config.openai_api_key, model=self.config.openai_model)
            
            # Initialize LangGraph workflow
            try:
                self.workflow = UIControlWorkflow(self)
                logger.info("OpenAI client and LangGraph workflow initialized successfully")
            except Exception as workflow_error:
                logger.error(f"Failed to initialize workflow: {workflow_error}")
                logger.error("Workflow initialization is required for agent operation.")
                raise workflow_error
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            logger.error("OpenAI initialization is required for agent operation.")
            raise e
    
    def load_tools(self) -> List[Dict[str, Any]]:
        """Load tools from configuration file"""
        try:
            with open(self.config.tools_file, "r") as f:
                config = json.load(f)
            tools = config.get("tools", [])
            logger.info(f"Loaded {len(tools)} tools from configuration")
            return tools
        except FileNotFoundError:
            logger.error(f"{self.config.tools_file} not found")
            return []
    
    def is_openai_available(self) -> bool:
        """Check if OpenAI client is available"""
        return self.openai_client is not None
    
    def process_message(self, message: str) -> Dict[str, Any]:
        """Process a user message and determine actions - OpenAI only"""
        logger.debug(f"Processing message: {message[:50]}...")
        
        if not self.is_openai_available():
            logger.error("OpenAI not available for message processing")
            return {
                "error": "OpenAI API key not configured. Set OPENAI_API_KEY environment variable.",
                "status": "error"
            }
        
        try:
            # Create a system prompt that includes tool descriptions
            tool_descriptions = "\n".join([
                f"- {tool['name']}: {tool['description']}" 
                for tool in self.tools
            ])
            
            system_prompt = f"""You are an AI assistant for a web application. 
You can help users with these actions:
{tool_descriptions}

When a user asks for something, determine if you need to use any tools and respond accordingly.
If you need to use a tool, mention what action you would take."""

            logger.debug("Sending request to OpenAI")
            response = self.openai_client.chat.completions.create(
                model=self.config.openai_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                max_tokens=200
            )
            
            result = {
                "response": response.choices[0].message.content,
                "tools_available": len(self.tools),
                "status": "success"
            }
            logger.debug("Message processed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return {
                "error": f"Failed to process message: {str(e)}",
                "status": "error"
            }

    async def stream_workflow(self, user_query: str, context_id: str = None) -> AsyncGenerator[str, None]:
        """Stream the LangGraph workflow execution"""
        if self.workflow is None:
            # No fallback - require proper initialization
            context_id = context_id or str(uuid.uuid4())[:8]
            error_msg = "Workflow not initialized. Check OpenAI configuration and tool setup."
            yield f"data: {json.dumps({'event': 'workflow_error', 'error': error_msg, 'context_id': context_id})}\n\n"
            return
        
        if not self.is_openai_available():
            # No fallback - require OpenAI API key
            context_id = context_id or str(uuid.uuid4())[:8]
            error_msg = "OpenAI API key not configured. Set OPENAI_API_KEY environment variable."
            yield f"data: {json.dumps({'event': 'workflow_error', 'error': error_msg, 'context_id': context_id})}\n\n"
            return
        
        # Use the LangGraph workflow with real OpenAI
        async for chunk in self.workflow.stream_workflow(user_query, context_id):
            yield chunk

    def execute_tool(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool with given parameters"""
        timestamp = datetime.now().isoformat()
        request_id = str(uuid.uuid4())[:8]
        
        logger.info(f"Executing tool '{tool_name}' with request_id {request_id}")
        logger.debug(f"Tool parameters: {parameters}")
        
        # Import tool handlers here to avoid circular imports
        from ..tools.handlers import ToolHandlers
        
        try:
            handlers = ToolHandlers()
            
            if tool_name == "navigate":
                return handlers.handle_navigation(parameters, request_id, timestamp)
            elif tool_name == "search_products":
                return handlers.handle_product_search(parameters, request_id, timestamp)
            elif tool_name == "add_to_cart":
                return handlers.handle_add_to_cart(parameters, request_id, timestamp)
            else:
                logger.warning(f"Unknown tool requested: {tool_name}")
                return {
                    "error": f"Unknown tool: {tool_name}",
                    "request_id": request_id,
                    "timestamp": timestamp
                }
        except Exception as e:
            logger.error(f"Tool execution failed for {tool_name}: {e}")
            return {
                "error": f"Tool execution failed: {str(e)}",
                "tool": tool_name,
                "request_id": request_id,
                "timestamp": timestamp
            } 