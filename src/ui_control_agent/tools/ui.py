"""
UI action tools for the UI control agent.
These tools generate action events for the frontend to execute.
"""

import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class UITools:
    """UI tools for frontend actions"""
    
    def __init__(self):
        """Initialize UI tools"""
        logger.info("UI tools initialized")
    
    def navigate(self, page: str, category: str = None) -> dict:
        """Navigate to a specific page"""
        return {
            "tool_type": "ui_action",
            "function": "navigate",
            "parameters": {"page": page, "category": category} if category else {"page": page},
            "description": f"Navigating to {page} page"
        }
    
    def search_products(self, query: str, category: str = None, max_price: float = None) -> dict:
        """Display search results on the UI"""
        params = {"query": query}
        if category:
            params["category"] = category
        if max_price:
            params["max_price"] = max_price
            
        return {
            "tool_type": "ui_action",
            "function": "search_products",
            "parameters": params,
            "description": f"Displaying search results for '{query}'"
        } 