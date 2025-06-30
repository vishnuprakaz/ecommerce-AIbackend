"""
Main entry point for UI Control Agent server.
Simple, clean startup script.
"""

import logging
import uvicorn

from src.ui_control_agent.server import create_server
from src.ui_control_agent.config import SimpleConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    """Main entry point"""
    try:
        # Load configuration
        config = SimpleConfig()
        
        # Create server
        app = create_server()
        
        # Get server config
        server_config = config.get_server_config()
        
        logger.info(f"Starting UI Control Agent server on {server_config['host']}:{server_config['port']}")
        
        # Run server
        uvicorn.run(
            app,
            host=server_config["host"],
            port=server_config["port"],
            log_level="info" if not server_config["debug"] else "debug"
        )
        
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise


if __name__ == "__main__":
    main() 