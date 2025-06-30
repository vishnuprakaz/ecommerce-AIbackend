"""
Simple FastAPI server for UI Control Agent.
Clean, straightforward server implementation.
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..agent import UIControlAgent

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Create FastAPI application with UI Control Agent"""
    
    # Initialize agent
    agent = UIControlAgent()
    
    # Create FastAPI app
    app = FastAPI(
        title="UI Control Agent API",
        description="Simple, clean API for UI control operations",
        version="2.0.0"
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Store agent in app state for access in routes
    app.state.agent = agent
    
    logger.info("FastAPI app created successfully")
    return app 