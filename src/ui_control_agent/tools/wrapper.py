"""
Tool wrapper for unified tool interface.
Provides a common way to load and execute UI tools only.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from pathlib import Path

from langchain.tools import tool
from pydantic import BaseModel, Field, create_model

from .ui import UITools

logger = logging.getLogger(__name__)


class ToolWrapper:
    """Unified wrapper for UI tools only"""
    
    def __init__(self, tools_config_file: str = "tools.json"):
        """Initialize tool wrapper with configuration"""
        self.ui_tools = UITools()
        self.tools_config = self._load_tools_config(tools_config_file)
        
        logger.info("UI-only tool wrapper initialized")
    
    def _load_tools_config(self, config_file: str) -> dict:
        """Load tools configuration from JSON file"""
        try:
            with open(config_file, "r") as f:
                config = json.load(f)
            logger.info(f"Loaded tools config from {config_file}")
            return config
        except Exception as e:
            logger.error(f"Failed to load tools config: {e}")
            return {"tools": []}
    
    def create_langchain_tools(self) -> List:
        """Create LangChain tools from configuration - UI only"""
        langchain_tools = []
        
        # Create UI tools from configuration
        for tool_config in self.tools_config.get("tools", []):
            tool_name = tool_config["name"]
            tool_desc = tool_config["description"]
            tool_params = tool_config.get("parameters", {})
            
            # Create Pydantic schema from JSON schema
            pydantic_model = self._create_pydantic_model(tool_name, tool_params)
            
            # Create LangChain tool
            langchain_tool = self._create_langchain_tool(tool_name, tool_desc, pydantic_model)
            langchain_tools.append(langchain_tool)
        
        logger.info(f"Created {len(langchain_tools)} UI-only tools")
        return langchain_tools
    
    def _create_pydantic_model(self, tool_name: str, tool_params: dict):
        """Convert JSON schema to Pydantic model"""
        pydantic_fields = {}
        properties = tool_params.get("properties", {})
        required = tool_params.get("required", [])
        
        for param_name, param_config in properties.items():
            param_type = param_config.get("type", "string")
            param_desc = param_config.get("description", "")
            
            # Map JSON types to Python types
            type_mapping = {
                "string": str,
                "number": float,
                "integer": int,
                "boolean": bool
            }
            field_type = type_mapping.get(param_type, str)
            
            # Handle optional fields
            if param_name not in required:
                field_type = Optional[field_type]
                pydantic_fields[param_name] = (field_type, Field(default=None, description=param_desc))
            else:
                pydantic_fields[param_name] = (field_type, Field(description=param_desc))
        
        # Create dynamic Pydantic model
        return create_model(f"{tool_name.title()}Input", **pydantic_fields)
    
    def _create_langchain_tool(self, tool_name: str, tool_desc: str, pydantic_model):
        """Create LangChain tool for UI actions"""
        def create_ui_tool(name, description, schema):
            @tool(description=description, args_schema=schema)
            def ui_tool(**kwargs) -> dict:
                """UI tool that returns action events"""
                # Route to appropriate UI tool method
                if name == "navigate":
                    return self.ui_tools.navigate(**kwargs)
                elif name == "search_products":
                    return self.ui_tools.search_products(**kwargs)
                else:
                    return {
                        "tool_type": "ui_action",
                        "function": name,
                        "parameters": kwargs,
                        "description": f"Executing {name} on the UI"
                    }
            
            ui_tool.name = name
            return ui_tool
        
        return create_ui_tool(tool_name, tool_desc, pydantic_model) 