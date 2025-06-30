"""
Conversational memory system for maintaining context across interactions
"""

import json
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from collections import defaultdict, deque

logger = logging.getLogger(__name__)


class ConversationMemory:
    """Manages conversational context and user session memory"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.max_history = config.get("max_history", 10)
        self.context_window = config.get("context_window", 4000)
        self.remember_types = config.get("remember", [])
        
        # Memory storage
        self.conversations = defaultdict(lambda: deque(maxlen=self.max_history))
        self.user_contexts = defaultdict(dict)
        self.session_data = defaultdict(dict)
        
        logger.info(f"Memory initialized - max_history: {self.max_history}, context_window: {self.context_window}")
    
    def add_message(self, context_id: str, role: str, content: str, metadata: Dict[str, Any] = None):
        """Add a message to conversation history"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        
        self.conversations[context_id].append(message)
        
        # Extract and store relevant information
        if metadata:
            self._extract_context_info(context_id, metadata)
        
        logger.debug(f"Added {role} message to context {context_id}")
    
    def add_tool_interaction(self, context_id: str, tool_name: str, parameters: Dict[str, Any], result: Dict[str, Any]):
        """Record tool interactions for context"""
        interaction = {
            "tool": tool_name,
            "parameters": parameters,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }
        
        # Add to conversation as system message
        self.add_message(
            context_id, 
            "system", 
            f"Tool used: {tool_name}",
            {"tool_interaction": interaction}
        )
        
        # Update user context based on tool type
        self._update_context_from_tool(context_id, tool_name, parameters, result)
    
    def get_conversation_history(self, context_id: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get conversation history for a context"""
        history = list(self.conversations[context_id])
        
        if limit:
            history = history[-limit:]
        
        return history
    
    def get_user_context(self, context_id: str) -> Dict[str, Any]:
        """Get accumulated user context and preferences"""
        return self.user_contexts[context_id].copy()
    
    def get_formatted_context(self, context_id: str) -> str:
        """Get formatted context for LLM prompt"""
        context = self.user_contexts[context_id]
        history = self.get_conversation_history(context_id, limit=5)  # Last 5 messages
        
        formatted_context = []
        
        # Add user preferences
        if context.get("preferences"):
            prefs = context["preferences"]
            pref_text = []
            if prefs.get("search_queries"):
                pref_text.append(f"Recent searches: {', '.join(prefs['search_queries'][-3:])}")
            if prefs.get("favorite_categories"):
                pref_text.append(f"Interested in: {', '.join(prefs['favorite_categories'])}")
            if prefs.get("price_range"):
                pref_text.append(f"Price preference: {prefs['price_range']}")
            
            if pref_text:
                formatted_context.append(f"User preferences: {'; '.join(pref_text)}")
        
        # Add recent activities
        if context.get("recent_activities"):
            activities = context["recent_activities"][-3:]  # Last 3 activities
            activity_text = [f"{act['action']} ({act.get('details', '')})" for act in activities]
            formatted_context.append(f"Recent activities: {'; '.join(activity_text)}")
        
        # Add cart info
        if context.get("cart_items"):
            cart_count = len(context["cart_items"])
            formatted_context.append(f"Cart: {cart_count} items")
        
        return "\n".join(formatted_context) if formatted_context else ""
    
    def _extract_context_info(self, context_id: str, metadata: Dict[str, Any]):
        """Extract relevant information from message metadata"""
        user_context = self.user_contexts[context_id]
        
        # Initialize context structure
        if "preferences" not in user_context:
            user_context["preferences"] = {
                "search_queries": [],
                "favorite_categories": [],
                "price_range": None,
                "brands": []
            }
        
        if "recent_activities" not in user_context:
            user_context["recent_activities"] = []
        
        # Extract search queries
        if "search_query" in metadata:
            search_queries = user_context["preferences"]["search_queries"]
            query = metadata["search_query"]
            if query not in search_queries:
                search_queries.append(query)
                if len(search_queries) > 10:  # Keep last 10 searches
                    search_queries.pop(0)
        
        # Extract categories
        if "category" in metadata:
            categories = user_context["preferences"]["favorite_categories"]
            category = metadata["category"]
            if category not in categories:
                categories.append(category)
                if len(categories) > 5:  # Keep top 5 categories
                    categories.pop(0)
    
    def _update_context_from_tool(self, context_id: str, tool_name: str, parameters: Dict[str, Any], result: Dict[str, Any]):
        """Update user context based on tool interactions"""
        user_context = self.user_contexts[context_id]
        
        # Track activities
        activity = {
            "action": tool_name,
            "timestamp": datetime.now().isoformat(),
            "details": self._summarize_tool_action(tool_name, parameters)
        }
        
        if "recent_activities" not in user_context:
            user_context["recent_activities"] = []
        
        user_context["recent_activities"].append(activity)
        if len(user_context["recent_activities"]) > 20:  # Keep last 20 activities
            user_context["recent_activities"].pop(0)
        
        # Tool-specific context updates
        if tool_name == "search_products_ui":
            self._update_search_context(context_id, parameters)
        elif tool_name == "navigate_ui":
            self._update_navigation_context(context_id, parameters)
        elif tool_name == "add_to_cart_ui":
            self._update_cart_context(context_id, parameters)
    
    def _update_search_context(self, context_id: str, parameters: Dict[str, Any]):
        """Update context from search interactions"""
        user_context = self.user_contexts[context_id]
        prefs = user_context.setdefault("preferences", {})
        
        # Track search query
        if "query" in parameters:
            search_queries = prefs.setdefault("search_queries", [])
            query = parameters["query"]
            if query not in search_queries:
                search_queries.append(query)
                if len(search_queries) > 10:
                    search_queries.pop(0)
        
        # Track price preferences
        if "filters" in parameters and parameters["filters"]:
            filters = parameters["filters"]
            if "price_max" in filters or "price_min" in filters:
                price_max = filters.get("price_max", float('inf'))
                price_min = filters.get("price_min", 0)
                
                if price_max < 50:
                    prefs["price_range"] = "budget"
                elif price_max < 200:
                    prefs["price_range"] = "mid-range"
                else:
                    prefs["price_range"] = "premium"
    
    def _update_navigation_context(self, context_id: str, parameters: Dict[str, Any]):
        """Update context from navigation"""
        user_context = self.user_contexts[context_id]
        prefs = user_context.setdefault("preferences", {})
        
        if "category" in parameters:
            categories = prefs.setdefault("favorite_categories", [])
            category = parameters["category"]
            if category and category not in categories:
                categories.append(category)
                if len(categories) > 5:
                    categories.pop(0)
    
    def _update_cart_context(self, context_id: str, parameters: Dict[str, Any]):
        """Update context from cart interactions"""
        user_context = self.user_contexts[context_id]
        
        if "cart_items" not in user_context:
            user_context["cart_items"] = []
        
        if "product_id" in parameters:
            cart_items = user_context["cart_items"]
            product_id = parameters["product_id"]
            quantity = parameters.get("quantity", 1)
            
            # Add or update cart item
            existing_item = next((item for item in cart_items if item["product_id"] == product_id), None)
            if existing_item:
                existing_item["quantity"] += quantity
            else:
                cart_items.append({
                    "product_id": product_id,
                    "quantity": quantity,
                    "added_at": datetime.now().isoformat()
                })
    
    def _summarize_tool_action(self, tool_name: str, parameters: Dict[str, Any]) -> str:
        """Create a summary of tool action for context"""
        if tool_name == "search_products_ui":
            query = parameters.get("query", "products")
            filters = parameters.get("filters", {})
            filter_text = ""
            if filters:
                if "price_max" in filters:
                    filter_text += f" under ${filters['price_max']}"
                if "color" in filters:
                    filter_text += f" in {filters['color']}"
            return f"searched for '{query}'{filter_text}"
        
        elif tool_name == "navigate_ui":
            page = parameters.get("page", "unknown")
            category = parameters.get("category", "")
            return f"navigated to {page}" + (f" > {category}" if category else "")
        
        elif tool_name == "add_to_cart_ui":
            product_id = parameters.get("product_id", "unknown")
            quantity = parameters.get("quantity", 1)
            return f"added {quantity}x {product_id} to cart"
        
        return f"used {tool_name}"
    
    def clear_context(self, context_id: str):
        """Clear conversation and context for a session"""
        if context_id in self.conversations:
            del self.conversations[context_id]
        if context_id in self.user_contexts:
            del self.user_contexts[context_id]
        if context_id in self.session_data:
            del self.session_data[context_id]
        
        logger.info(f"Cleared context for {context_id}")
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get memory usage statistics"""
        return {
            "active_conversations": len(self.conversations),
            "total_messages": sum(len(conv) for conv in self.conversations.values()),
            "user_contexts": len(self.user_contexts),
            "memory_config": {
                "max_history": self.max_history,
                "context_window": self.context_window
            }
        } 