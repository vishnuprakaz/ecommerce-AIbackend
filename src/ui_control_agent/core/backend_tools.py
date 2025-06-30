"""
Backend tools for direct data operations
Simplified to essential tools only
"""

import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class BackendTools:
    """Simplified backend tools for data operations"""
    
    def __init__(self):
        """Initialize backend tools"""
        logger.info("Backend tools initialized - simplified version")
    
    def search_products_data(self, query: str, **filters) -> dict:
        """Search for products and return actual product data"""
        
        # Mock product database (in real app, this would query your database)
        mock_products = [
            {
                "id": "dress_001",
                "name": "Princess Red Dress",
                "price": 45.99,
                "original_price": 59.99,
                "rating": 4.8,
                "reviews_count": 124,
                "color": "red",
                "category": "dress",
                "sizes": ["4T", "5T", "6T"],
                "in_stock": True,
                "brand": "Little Princess",
                "description": "Beautiful red dress perfect for special occasions",
                "image_url": "/images/red-dress-001.jpg",
                "sale": True
            },
            {
                "id": "dress_002", 
                "name": "Cotton Red Sundress",
                "price": 29.99,
                "rating": 4.5,
                "reviews_count": 89,
                "color": "red",
                "category": "dress",
                "sizes": ["4T", "5T", "6T", "7T"],
                "in_stock": True,
                "brand": "Comfy Kids",
                "description": "Comfortable cotton dress for everyday wear",
                "image_url": "/images/red-dress-002.jpg"
            },
            {
                "id": "dress_003",
                "name": "Velvet Red Party Dress", 
                "price": 89.99,
                "rating": 4.9,
                "reviews_count": 67,
                "color": "red",
                "category": "dress",
                "sizes": ["5T", "6T"],
                "in_stock": False,
                "brand": "Elegant Kids",
                "description": "Luxurious velvet dress for special events",
                "image_url": "/images/red-dress-003.jpg"
            },
            {
                "id": "shoes_001",
                "name": "Red High Heels",
                "price": 79.99,
                "rating": 4.3,
                "reviews_count": 156,
                "color": "red",
                "category": "shoes",
                "sizes": ["6", "7", "8", "9"],
                "in_stock": True,
                "brand": "Elegant Steps",
                "description": "Stylish red high heels",
                "image_url": "/images/red-heels-001.jpg"
            }
        ]
        
        # Apply basic filters
        results = []
        query_lower = query.lower()
        
        for product in mock_products:
            # Improved text matching - split query into words and check each
            query_words = query_lower.split()
            match_score = 0
            
            # Check if any query word matches product fields
            for word in query_words:
                if (word in product["name"].lower() or 
                    word in product["description"].lower() or
                    word in product["color"].lower() or
                    word in product["category"].lower()):
                    match_score += 1
            
            # Include product if at least one word matches
            if match_score > 0:
                # Apply category filter
                if filters.get("category") and filters["category"].lower() != product["category"].lower():
                    continue
                
                # Apply price filter
                if filters.get("max_price") and product["price"] > float(filters["max_price"]):
                    continue
                
                results.append(product)
        
        # Sort by relevance (rating * reviews for simplicity)
        results.sort(key=lambda x: x["rating"] * x["reviews_count"], reverse=True)
        
        # Limit results
        limit = filters.get("limit", 10)
        results = results[:limit]
        
        return {
            "query": query,
            "filters": filters,
            "total_results": len(results),
            "products": results,
            "search_metadata": {
                "price_range": {
                    "min": min([p["price"] for p in results]) if results else 0,
                    "max": max([p["price"] for p in results]) if results else 0
                },
                "avg_rating": sum([p["rating"] for p in results]) / len(results) if results else 0,
                "in_stock_count": len([p for p in results if p["in_stock"]]),
                "brands": list(set([p["brand"] for p in results]))
            }
        } 