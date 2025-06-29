"""
Response models for API endpoints
"""

from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List
from enum import Enum


class ResponseStatus(str, Enum):
    """Response status enumeration"""
    SUCCESS = "success"
    ERROR = "error"
    PARTIAL = "partial"


class ChatResponse(BaseModel):
    """Chat endpoint response model"""
    response: str = Field(..., description="Agent response")
    user_id: str = Field(..., description="User identifier")
    status: ResponseStatus = Field(ResponseStatus.SUCCESS, description="Response status")
    tools_available: int = Field(0, description="Number of available tools")
    note: Optional[str] = Field(None, description="Additional notes")


class ToolResponse(BaseModel):
    """Tool execution response model"""
    result: Dict[str, Any] = Field(..., description="Tool execution result")
    status: ResponseStatus = Field(ResponseStatus.SUCCESS, description="Execution status")
    tool_name: str = Field(..., description="Executed tool name")
    execution_time: Optional[float] = Field(None, description="Execution time in seconds")


class A2AResponse(BaseModel):
    """A2A protocol response model"""
    event: str = Field(..., description="Event type")
    content: Optional[str] = Field(None, description="Response content")
    context_id: Optional[str] = Field(None, description="Context identifier")
    status: Optional[ResponseStatus] = Field(None, description="Response status")
    tools_available: Optional[int] = Field(None, description="Number of available tools")
    chunk_id: Optional[int] = Field(None, description="Chunk identifier for streaming")
    timestamp: Optional[float] = Field(None, description="Event timestamp")


class HealthResponse(BaseModel):
    """Health check response model"""
    status: str = Field(..., description="Health status")
    openai_configured: bool = Field(..., description="OpenAI configuration status")
    tools_loaded: int = Field(..., description="Number of loaded tools")
    a2a_enabled: bool = Field(..., description="A2A protocol status")
    agent_mode: str = Field(..., description="Agent mode (openai/mock)")


class ToolsResponse(BaseModel):
    """Tools listing response model"""
    tools: List[Dict[str, Any]] = Field(..., description="Available tools")
    count: int = Field(..., description="Number of tools")
    agent_mode: str = Field(..., description="Agent mode (openai/mock)") 