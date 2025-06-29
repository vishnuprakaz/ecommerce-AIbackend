"""
Main entry point for the ecommerce agent server
"""

import uvicorn
import logging
from src.ecommerce_agent.server.app import create_app
from src.ecommerce_agent.core.config import get_config

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
    
    logger.info(f"Starting ecommerce agent server on {config.host}:{config.port}")
    logger.info(f"OpenAI configured: {config.is_openai_configured()}")
    logger.info(f"Debug mode: {config.debug}")
    
    # Run the server
    uvicorn.run(
        app,
        host=config.host,
        port=config.port,
        reload=config.debug,
        log_level="info"
    ) 