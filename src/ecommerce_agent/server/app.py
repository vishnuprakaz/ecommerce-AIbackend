"""
FastAPI application factory
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from ..core.agent import EcommerceAgent
from ..a2a.server import add_a2a_routes
from .routes import add_api_routes
from .middleware import add_middleware

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application"""
    
    # Initialize the ecommerce agent
    agent = EcommerceAgent()
    
    # Create FastAPI app
    app = FastAPI(
        title="Ecommerce Agent API",
        description="AI-powered conversational ecommerce backend with A2A protocol support",
        version="0.2.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Add middleware
    add_middleware(app)
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, specify actual origins
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
    )
    
    # Add API routes
    add_api_routes(app, agent)
    
    # Add A2A protocol routes
    add_a2a_routes(app, agent)
    
    logger.info("FastAPI application created successfully")
    return app 