"""
Ecommerce Agent - AI-powered conversational ecommerce backend
"""

__version__ = "0.2.0"
__author__ = "Ecommerce Agent Team"

from .core.agent import EcommerceAgent
from .core.config import get_config

__all__ = ["EcommerceAgent", "get_config"] 