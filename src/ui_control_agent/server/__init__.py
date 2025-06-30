"""
Simple server package for UI Control Agent.
"""

from .app import create_app
from .routes import add_routes

def create_server():
    """Create complete server with routes"""
    app = create_app()
    add_routes(app)
    return app

__all__ = ["create_app", "add_routes", "create_server"] 