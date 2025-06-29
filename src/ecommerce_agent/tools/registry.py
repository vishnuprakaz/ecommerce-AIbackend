"""
Tool registry for managing available tools and their schemas
"""

import json
from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger(__name__)


class ToolRegistry:
    """Registry for managing ecommerce tools"""
    
    def __init__(self, config_file: str = "tools.json"):
        self.config_file = config_file
        self._tools = {}
        self._load_tools()
    
    def _load_tools(self):
        """Load tools from configuration file"""
        try:
            with open(self.config_file, "r") as f:
                config = json.load(f)
            
            tools = config.get("tools", [])
            for tool in tools:
                self._tools[tool["name"]] = tool
            
            logger.info(f"Loaded {len(self._tools)} tools from {self.config_file}")
        except FileNotFoundError:
            logger.error(f"Tools configuration file {self.config_file} not found")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {self.config_file}: {e}")
    
    def get_tool(self, name: str) -> Optional[Dict[str, Any]]:
        """Get a tool by name"""
        return self._tools.get(name)
    
    def get_all_tools(self) -> List[Dict[str, Any]]:
        """Get all available tools"""
        return list(self._tools.values())
    
    def get_tool_names(self) -> List[str]:
        """Get all tool names"""
        return list(self._tools.keys())
    
    def is_tool_available(self, name: str) -> bool:
        """Check if a tool is available"""
        return name in self._tools
    
    def get_tool_schema(self, name: str) -> Optional[Dict[str, Any]]:
        """Get the schema for a specific tool"""
        tool = self.get_tool(name)
        if tool:
            return tool.get("schema", {})
        return None
    
    def validate_tool_parameters(self, name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Validate parameters for a specific tool"""
        tool = self.get_tool(name)
        if not tool:
            return {"valid": False, "error": f"Tool '{name}' not found"}
        
        schema = tool.get("schema", {})
        required_params = schema.get("required", [])
        
        # Check for required parameters
        missing_params = [param for param in required_params if param not in parameters]
        if missing_params:
            return {
                "valid": False, 
                "error": f"Missing required parameters: {', '.join(missing_params)}"
            }
        
        # Basic type validation could be added here
        # For now, just check that required params are present
        
        return {"valid": True}
    
    def reload_tools(self):
        """Reload tools from configuration file"""
        self._tools.clear()
        self._load_tools() 