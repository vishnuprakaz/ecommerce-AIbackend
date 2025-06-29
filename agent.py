import json
import os
from typing import Dict, Any, List, Optional
from openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import uuid
from datetime import datetime
import logging

# Set up logging
logger = logging.getLogger(__name__)

load_dotenv()

class EcommerceAgent:
    def __init__(self):
        self.tools = self.load_tools()
        # Initialize OpenAI client only if API key is available
        self.openai_client = None
        self.llm = None
        self._init_openai()
    
    def _init_openai(self):
        """Initialize OpenAI clients if API key is available"""
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key and api_key != "your_api_key_here":
            try:
                self.openai_client = OpenAI(api_key=api_key)
                self.llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")
                logger.info("OpenAI client initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize OpenAI client: {e}")
        else:
            logger.warning("OpenAI API key not found - agent will work in mock mode")
    
    def load_tools(self) -> List[Dict[str, Any]]:
        """Load tools from configuration file"""
        try:
            with open("tools.json", "r") as f:
                config = json.load(f)
            tools = config.get("tools", [])
            logger.info(f"Loaded {len(tools)} tools from configuration")
            return tools
        except FileNotFoundError:
            logger.error("tools.json not found")
            return []
    
    def is_openai_available(self) -> bool:
        """Check if OpenAI client is available"""
        return self.openai_client is not None
    
    def process_message(self, message: str) -> Dict[str, Any]:
        """Process a user message and determine actions"""
        logger.debug(f"Processing message: {message[:50]}...")
        
        if not self.is_openai_available():
            logger.debug("Using mock mode for message processing")
            return {
                "response": f"🤖 Mock response to: '{message}' (OpenAI not configured - set OPENAI_API_KEY)",
                "tools_available": len(self.tools),
                "status": "mock_mode"
            }
        
        try:
            # Create a system prompt that includes tool descriptions
            tool_descriptions = "\n".join([
                f"- {tool['name']}: {tool['description']}" 
                for tool in self.tools
            ])
            
            system_prompt = f"""You are an AI assistant for an ecommerce website. 
You can help users with these actions:
{tool_descriptions}

When a user asks for something, determine if you need to use any tools and respond accordingly.
If you need to use a tool, mention what action you would take."""

            logger.debug("Sending request to OpenAI")
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                max_tokens=200
            )
            
            result = {
                "response": response.choices[0].message.content,
                "tools_available": len(self.tools),
                "status": "success"
            }
            logger.debug("Message processed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return {
                "response": f"Sorry, I encountered an error: {str(e)}",
                "status": "error"
            }

    def execute_tool(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool with given parameters"""
        timestamp = datetime.now().isoformat()
        request_id = str(uuid.uuid4())[:8]
        
        logger.info(f"Executing tool '{tool_name}' with request_id {request_id}")
        logger.debug(f"Tool parameters: {parameters}")
        
        try:
            if tool_name == "navigate":
                return self._handle_navigation(parameters, request_id, timestamp)
            elif tool_name == "search_products":
                return self._handle_product_search(parameters, request_id, timestamp)
            elif tool_name == "add_to_cart":
                return self._handle_add_to_cart(parameters, request_id, timestamp)
            else:
                logger.warning(f"Unknown tool requested: {tool_name}")
                return {
                    "error": f"Unknown tool: {tool_name}",
                    "request_id": request_id,
                    "timestamp": timestamp
                }
        except Exception as e:
            logger.error(f"Tool execution failed for {tool_name}: {e}")
            return {
                "error": f"Tool execution failed: {str(e)}",
                "tool": tool_name,
                "request_id": request_id,
                "timestamp": timestamp
            }
    
    def _handle_navigation(self, params: Dict[str, Any], request_id: str, timestamp: str) -> Dict[str, Any]:
        """Handle navigation tool execution"""
        page = params.get("page")
        category = params.get("category")
        
        logger.debug(f"Navigation request: page={page}, category={category}")
        
        if not page:
            return {
                "error": "Page parameter is required",
                "request_id": request_id,
                "timestamp": timestamp
            }
        
        # Build navigation response
        nav_response = {
            "action": "navigate",
            "target_page": page,
            "success": True,
            "ui_updates": [
                {"type": "route_change", "path": f"/{page}"},
                {"type": "update_breadcrumb", "path": [{"name": "Home", "url": "/"}, {"name": page.title(), "url": f"/{page}"}]}
            ],
            "request_id": request_id,
            "timestamp": timestamp
        }
        
        # Add category-specific updates
        if category and page == "products":
            nav_response["ui_updates"].extend([
                {"type": "set_category_filter", "category": category},
                {"type": "update_page_title", "title": f"{category.title()} Products"}
            ])
            nav_response["category"] = category
        
        logger.info(f"Navigation successful: {page}")
        return nav_response
    
    def _handle_product_search(self, params: Dict[str, Any], request_id: str, timestamp: str) -> Dict[str, Any]:
        """Handle product search tool execution"""
        query = params.get("query")
        filters = params.get("filters", {})
        
        logger.debug(f"Product search: query='{query}', filters={filters}")
        
        if not query:
            return {
                "error": "Query parameter is required",
                "request_id": request_id,
                "timestamp": timestamp
            }
        
        # Simulate search results (in real app, this would query a database)
        mock_products = [
            {
                "id": "prod_001",
                "name": f"Red Leather Handbag",
                "price": 89.99,
                "image": "/images/red-handbag-1.jpg",
                "rating": 4.5,
                "in_stock": True
            },
            {
                "id": "prod_002", 
                "name": f"Crimson Tote Bag",
                "price": 65.00,
                "image": "/images/red-tote-1.jpg",
                "rating": 4.2,
                "in_stock": True
            }
        ]
        
        # Apply filters
        filtered_products = mock_products
        if filters.get("max_price"):
            filtered_products = [p for p in filtered_products if p["price"] <= filters["max_price"]]
        if filters.get("min_price"):
            filtered_products = [p for p in filtered_products if p["price"] >= filters["min_price"]]
        
        logger.info(f"Search returned {len(filtered_products)} products for query '{query}'")
        
        return {
            "action": "search_products",
            "query": query,
            "filters": filters,
            "results": filtered_products,
            "result_count": len(filtered_products),
            "ui_updates": [
                {"type": "update_search_results", "products": filtered_products},
                {"type": "update_result_count", "count": len(filtered_products)},
                {"type": "highlight_search_term", "term": query}
            ],
            "success": True,
            "request_id": request_id,
            "timestamp": timestamp
        }
    
    def _handle_add_to_cart(self, params: Dict[str, Any], request_id: str, timestamp: str) -> Dict[str, Any]:
        """Handle add to cart tool execution"""
        product_id = params.get("product_id")
        quantity = params.get("quantity", 1)
        
        logger.debug(f"Add to cart: product_id={product_id}, quantity={quantity}")
        
        if not product_id:
            return {
                "error": "Product ID is required",
                "request_id": request_id,
                "timestamp": timestamp
            }
        
        # Simulate adding to cart
        cart_item = {
            "product_id": product_id,
            "quantity": quantity,
            "added_at": timestamp,
            "cart_id": f"cart_{request_id}"
        }
        
        logger.info(f"Added {quantity} of product {product_id} to cart")
        
        return {
            "action": "add_to_cart",
            "cart_item": cart_item,
            "success": True,
            "ui_updates": [
                {"type": "show_cart_notification", "message": f"Added {quantity} item(s) to cart"},
                {"type": "update_cart_badge", "count": f"+{quantity}"},
                {"type": "animate_cart_icon"},
                {"type": "show_cart_sidebar", "auto_hide_after": 3000}
            ],
            "request_id": request_id,
            "timestamp": timestamp
        } 