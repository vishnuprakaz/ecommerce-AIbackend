"""
Configuration management for the UI control agent
"""

import os
import yaml
import json
import logging
from typing import Dict, Any, Optional
from pathlib import Path

logger = logging.getLogger(__name__)


class AgentConfig:
    """Enhanced configuration class for the UI control agent"""
    
    def __init__(self, config_file: str = "src/ui_control_agent/core/agent_config.yaml"):
        self.config_file = config_file
        self.config = self._load_yaml_config()
        
        # OpenAI Configuration (environment overrides config)
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        
        # LLM settings from config
        llm_config = self.config.get("llm", {})
        self.openai_model = os.getenv("OPENAI_MODEL", llm_config.get("model", "gpt-4o-mini"))
        self.temperature = llm_config.get("temperature", 0.7)
        self.max_tokens = llm_config.get("max_tokens", 1000)
        self.stream_responses = llm_config.get("stream", True)
        
        # Agent settings
        agent_config = self.config.get("agent", {})
        self.agent_name = agent_config.get("name", "UI Control Assistant")
        self.agent_version = agent_config.get("version", "1.0.0")
        
        # Prompt configuration
        self.prompts = self.config.get("prompts", {})
        
        # Memory configuration
        self.memory_config = self.config.get("memory", {})
        
        # Tool configuration
        tool_config = self.config.get("tools", {})
        self.ui_tools_file = tool_config.get("ui_tools", {}).get("config_file", "tools.json")
        self.backend_tools_enabled = tool_config.get("backend_tools", {}).get("enabled", False)
        self.backend_tool_functions = tool_config.get("backend_tools", {}).get("functions", [])
        
        # Legacy tools file (fallback)
        self.tools_file = os.getenv("TOOLS_FILE", "tools.json")
        
        # Response configuration
        self.response_config = self.config.get("responses", {})
        
        # Error handling
        self.error_config = self.config.get("error_handling", {})
        
        # Server Configuration
        self.debug_mode = os.getenv("DEBUG", "false").lower() == "true"
        self.debug = self.debug_mode  # Alias for compatibility
        self.host = os.getenv("HOST", "0.0.0.0")
        self.port = int(os.getenv("PORT", "8000"))
        
        logger.info(f"Agent configuration loaded from {config_file}")
    
    def _load_yaml_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        config_path = Path(self.config_file)
        
        if not config_path.exists():
            logger.warning(f"Config file {self.config_file} not found, using defaults")
            return {}
        
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            logger.info(f"Loaded configuration from {self.config_file}")
            return config
        except Exception as e:
            logger.error(f"Failed to load config file {self.config_file}: {e}")
            return {}
    
    def get_system_prompt(self) -> str:
        """Get the system prompt with current context"""
        base_prompt = self.prompts.get("system", "You are a helpful UI control assistant.")
        
        # Add tool information
        ui_tools_info = ""
        backend_tools_info = ""
        
        try:
            # Load UI tools info
            ui_tools = self.load_ui_tools()
            if ui_tools and "tools" in ui_tools.get("ui_tools", {}):
                ui_tool_names = [tool["name"] for tool in ui_tools["ui_tools"]["tools"]]
                ui_tools_info = f"\nUI Tools available: {', '.join(ui_tool_names)}"
            
            # Backend tools info
            if self.backend_tool_functions:
                backend_tools_info = f"\nBackend Tools available: {', '.join(self.backend_tool_functions)}"
        
        except Exception as e:
            logger.warning(f"Could not load tool info for prompt: {e}")
        
        return base_prompt + ui_tools_info + backend_tools_info
    
    def get_user_greeting(self) -> str:
        """Get the user greeting message"""
        return self.prompts.get("user_greeting", "Hello! How can I help you today?")
    
    def load_ui_tools(self) -> Dict[str, Any]:
        """Load UI tools configuration"""
        try:
            with open(self.ui_tools_file, 'r') as f:
                ui_tools = json.load(f)
            logger.info(f"Loaded UI tools from {self.ui_tools_file}")
            return ui_tools
        except FileNotFoundError:
            logger.warning(f"UI tools file {self.ui_tools_file} not found")
            return {}
        except Exception as e:
            logger.error(f"Failed to load UI tools: {e}")
            return {}
    
    def load_legacy_tools(self) -> Dict[str, Any]:
        """Load legacy tools configuration (fallback)"""
        try:
            with open(self.tools_file, 'r') as f:
                tools = json.load(f)
            logger.info(f"Loaded legacy tools from {self.tools_file}")
            return tools
        except FileNotFoundError:
            logger.warning(f"Legacy tools file {self.tools_file} not found")
            return {}
        except Exception as e:
            logger.error(f"Failed to load legacy tools: {e}")
            return {}
    
    def get_response_config(self) -> Dict[str, Any]:
        """Get response configuration"""
        return self.response_config
    
    def get_memory_config(self) -> Dict[str, Any]:
        """Get memory configuration"""
        return self.memory_config
    
    def get_error_config(self) -> Dict[str, Any]:
        """Get error handling configuration"""
        return self.error_config
    
    def is_openai_configured(self) -> bool:
        """Check if OpenAI is properly configured"""
        return bool(self.openai_api_key)
    
    def is_memory_enabled(self) -> bool:
        """Check if conversational memory is enabled"""
        return self.memory_config.get("enabled", False)
    
    def is_backend_tools_enabled(self) -> bool:
        """Check if backend tools are enabled"""
        return self.backend_tools_enabled


def get_config() -> AgentConfig:
    """Get the global agent configuration"""
    return AgentConfig()

# Export for imports
__all__ = ['AgentConfig', 'get_config'] 