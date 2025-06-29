"""
Request models for API endpoints
"""

from pydantic import BaseModel, Field, field_validator
from typing import Dict, Any, Optional
import re


class ChatMessage(BaseModel):
    """Chat message request model"""
    message: str = Field(..., min_length=1, max_length=1000, description="User message")
    user_id: str = Field("anonymous", max_length=50, description="User identifier")
    
    @field_validator('message')
    @classmethod
    def validate_message(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Message cannot be empty')
        return v.strip()
    
    @field_validator('user_id') 
    @classmethod
    def validate_user_id(cls, v: str) -> str:
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('User ID can only contain letters, numbers, hyphens, and underscores')
        return v


class ToolRequest(BaseModel):
    """Tool execution request model"""
    tool_name: str = Field(..., min_length=1, max_length=50)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    
    @field_validator('tool_name')
    @classmethod
    def validate_tool_name(cls, v: str) -> str:
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', v):
            raise ValueError('Tool name must be a valid identifier')
        return v


class A2AMessage(BaseModel):
    """A2A protocol message request model"""
    message: str = Field(..., min_length=1, max_length=2000, description="User message")
    user_id: str = Field("anonymous", max_length=50, description="User identifier")
    context_id: Optional[str] = Field(None, max_length=100, description="Context identifier")
    
    @field_validator('message')
    @classmethod
    def validate_message(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Message cannot be empty')
        return v.strip()
    
    @field_validator('user_id') 
    @classmethod
    def validate_user_id(cls, v: str) -> str:
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('User ID can only contain letters, numbers, hyphens, and underscores')
        return v
    
    @field_validator('context_id')
    @classmethod
    def validate_context_id(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('Context ID can only contain letters, numbers, hyphens, and underscores')
        return v 