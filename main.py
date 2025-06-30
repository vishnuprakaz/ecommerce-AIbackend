"""
Main entry point for the UI control agent server
"""

import uvicorn
import logging
from src.ui_control_agent.server.app import create_app
from src.ui_control_agent.core.config import get_config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    # Get configuration
    config = get_config()
    
    # Create the application
    app = create_app()
    
    logger.info(f"Starting UI control agent server on {config.host}:{config.port}")
    logger.info(f"OpenAI configured: {config.is_openai_configured()}")
    logger.info(f"Debug mode: {config.debug}")
    
    # Run the server
    if config.debug:
        # Use import string for reload mode
        uvicorn.run(
            "src.ui_control_agent.server.app:create_app",
            factory=True,
            host=config.host,
            port=config.port,
            reload=True,
            log_level="info"
        )
    else:
        # Use app object for production
        uvicorn.run(
            app,
            host=config.host,
            port=config.port,
            log_level="info"
        ) 