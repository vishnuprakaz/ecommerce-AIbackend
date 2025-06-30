"""
UI Control Agent - AI-powered conversational UI control backend
"""

__version__ = "0.2.0"
__author__ = "UI Control Agent Team"

from .core.agent import UIControlAgent
from .core.config import get_config

__all__ = ["UIControlAgent", "get_config"] 