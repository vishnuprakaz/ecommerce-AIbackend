"""
Simple configuration for UI Control Agent.
Clean, easy to understand configuration management.
"""

import os
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class SimpleConfig:
    """Clean, simple configuration class"""
    
    def __init__(self):
        """Initialize configuration with environment variables and defaults"""
        # OpenAI Configuration
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        
        # Server Configuration
        self.host = os.getenv("HOST", "0.0.0.0")
        self.port = int(os.getenv("PORT", "8000"))
        self.debug = os.getenv("DEBUG", "false").lower() == "true"
        
        # Tools Configuration
        self.tools_config_file = os.getenv("TOOLS_FILE", "tools.json")
        
        logger.info("Simple configuration initialized")
    
    def is_openai_configured(self) -> bool:
        """Check if OpenAI is properly configured"""
        return bool(self.openai_api_key)
    
    def get_server_config(self) -> Dict[str, Any]:
        """Get server configuration"""
        return {
            "host": self.host,
            "port": self.port,
            "debug": self.debug
        }
    
    def get_llm_config(self) -> Dict[str, Any]:
        """Get LLM configuration"""
        return {
            "model": self.openai_model,
            "api_key": self.openai_api_key
        } 