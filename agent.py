import json
import os
from typing import Dict, Any, List
from openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class EcommerceAgent:
    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-3.5-turbo"
        )
        self.tools = self.load_tools()
    
    def load_tools(self) -> List[Dict[str, Any]]:
        """Load tools from configuration file"""
        try:
            with open("tools.json", "r") as f:
                config = json.load(f)
            return config.get("tools", [])
        except FileNotFoundError:
            print("Warning: tools.json not found")
            return []
    
    def process_message(self, message: str) -> Dict[str, Any]:
        """Process a user message and determine actions"""
        # Simple tool calling for now
        try:
            # Create a system prompt that includes tool descriptions
            tool_descriptions = "\n".join([
                f"- {tool['name']}: {tool['description']}" 
                for tool in self.tools
            ])
            
            system_prompt = f"""You are an AI assistant for an ecommerce website. 
You can help users with these actions:
{tool_descriptions}

When a user asks for something, determine if you need to use any tools and respond accordingly.
If you need to use a tool, mention what action you would take."""

            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                max_tokens=200
            )
            
            return {
                "response": response.choices[0].message.content,
                "tools_available": len(self.tools),
                "status": "success"
            }
        except Exception as e:
            return {
                "response": f"Sorry, I encountered an error: {str(e)}",
                "status": "error"
            }

    def execute_tool(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool with given parameters"""
        # For now, just return mock responses
        if tool_name == "navigate":
            return {"action": "navigate", "page": parameters.get("page"), "success": True}
        elif tool_name == "search_products":
            return {"action": "search", "query": parameters.get("query"), "results": []}
        elif tool_name == "add_to_cart":
            return {"action": "add_to_cart", "product_id": parameters.get("product_id"), "success": True}
        else:
            return {"error": f"Unknown tool: {tool_name}"} 