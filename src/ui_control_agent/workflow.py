"""
Simple workflow for UI Control Agent.
Handles LLM calls + UI tool execution + streaming.
UI-first architecture: Agent → UI → Data callback → Final response
Now with conversation memory for context!
"""

import asyncio
import json
import logging
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, AsyncGenerator, List

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from .memory import ConversationMemory

logger = logging.getLogger(__name__)


class SimpleWorkflow:
    """
    UI-first workflow with conversation memory and proper callback coordination.
    The stream endpoint now waits for UI callback results before finishing the response.
    """
    
    def __init__(self, openai_model: str = "gpt-4o-mini"):
        """Initialize with clean UI-first approach + conversation memory"""
        self.llm = ChatOpenAI(model=openai_model, temperature=0)
        self.llm_with_tools = None  # Will be set when tools are provided
        self.tools = []
        self.prompts = self._load_prompts()
        self.pending_actions = {}  # Store actions waiting for UI callback
        self.callback_events = {}  # Store asyncio events for coordinating responses
        self.callback_results = {}  # Store callback results
        
        # Initialize conversation memory
        self.memory = ConversationMemory()
        
        logger.info("UI-first workflow initialized with conversation memory and proper callback coordination")
    
    def _load_prompts(self) -> dict:
        """Load prompts from YAML file"""
        prompts_path = Path(__file__).parent / "prompts" / "system.yaml"
        try:
            with open(prompts_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            logger.warning(f"Prompts file not found: {prompts_path}")
            return {}
    
    def set_tools(self, tools: List):
        """Set tools and create LLM with tools"""
        self.tools = tools
        if tools:
            self.llm_with_tools = self.llm.bind_tools(tools)
            logger.info(f"Workflow configured with {len(tools)} UI-only tools")
    
    async def process_message(self, user_query: str, session_id: str = "default") -> dict:
        """Process message in UI-first mode with conversation memory"""
        try:
            # Store user message in conversation memory
            self.memory.add_message(session_id, "user", user_query)
            
            # Get conversation context
            conversation_context = self.memory.get_conversation_context(session_id)
            
            # Build system message with conversation context
            system_content = self.prompts.get("system_prompt", "")
            if conversation_context:
                system_content += f"\n\n{conversation_context}"
            
            messages = [
                SystemMessage(content=system_content),
                HumanMessage(content=user_query)
            ]
            
            # Get response from LLM with tools
            response = self.llm_with_tools.invoke(messages)
            
            # Process tool calls - UI only
            actions = []
            
            if hasattr(response, 'tool_calls') and response.tool_calls:
                for tool_call in response.tool_calls:
                    tool_name = tool_call["name"]
                    tool_args = tool_call["args"]
                    
                    # Execute the UI tool
                    for tool in self.tools:
                        if tool.name == tool_name:
                            try:
                                result = tool.func(**tool_args)
                                
                                # All tools should be UI actions now
                                if isinstance(result, dict) and result.get("tool_type") == "ui_action":
                                    action_id = f"{session_id}_{len(actions)}_{datetime.now().strftime('%H%M%S')}"
                                    action_data = {
                                        "id": action_id,
                                        "function": result["function"],
                                        "params": result["parameters"],
                                        "description": result["description"]
                                    }
                                    actions.append(action_data)
                                    
                                    # Store for UI callback coordination
                                    self.pending_actions[action_id] = {
                                        "user_query": user_query,
                                        "action": action_data,
                                        "session_id": session_id
                                    }
                                    
                                    # Create asyncio event for coordination
                                    self.callback_events[action_id] = asyncio.Event()
                                    
                            except Exception as e:
                                logger.error(f"Tool execution error: {e}")
                            break
            
            # Store agent response in memory
            response_content = response.content or ""
            agent_metadata = {
                "actions": [action["function"] for action in actions],
                "has_tool_calls": len(actions) > 0
            }
            self.memory.add_message(session_id, "agent", response_content, agent_metadata)
            
            return {
                "response": response_content,
                "actions": actions,
                "tools_used": [tc["name"] for tc in response.tool_calls] if hasattr(response, 'tool_calls') and response.tool_calls else [],
                "pending_ui_callback": len(actions) > 0,
                "conversation_stats": self.memory.get_conversation_summary(session_id)
            }
            
        except Exception as e:
            logger.error(f"Workflow processing error: {e}")
            return {
                "response": self.prompts.get("error_message", "An error occurred"),
                "actions": [],
                "tools_used": [],
                "pending_ui_callback": False,
                "conversation_stats": self.memory.get_conversation_summary(session_id)
            }
    
    async def process_ui_callback(self, action_id: str, ui_data: Dict[Any, Any]) -> dict:
        """Process data callback from UI after action execution - now with proper coordination"""
        try:
            if action_id not in self.pending_actions:
                logger.error(f"Unknown action_id: {action_id}")
                return {"error": "Unknown action ID"}
            
            pending = self.pending_actions[action_id]
            user_query = pending["user_query"]
            action = pending["action"]
            session_id = pending["session_id"]
            
            # Store UI result in conversation memory
            ui_metadata = {
                "action_id": action_id,
                "action_function": action["function"],
                "summary": f"UI executed {action['function']} successfully"
            }
            self.memory.add_message(session_id, "ui_result", json.dumps(ui_data), ui_metadata)
            
            # Get conversation context for final response
            conversation_context = self.memory.get_conversation_context(session_id)
            
            # Create follow-up prompt with UI results and conversation context
            follow_up_prompt = f"""
            {conversation_context}
            
            CURRENT SITUATION:
            The user's most recent request was: "{user_query}"
            I executed: {action['function']}({action['params']})
            
            The UI just returned this data:
            {json.dumps(ui_data, indent=2)}
            
            Based on the conversation history and these actual UI results, provide a helpful conversational response to the user.
            """
            
            # Get final response from LLM based on real UI data + context
            messages = [
                SystemMessage(content=self.prompts.get("system_prompt", "")),
                HumanMessage(content=follow_up_prompt)
            ]
            
            response = self.llm.invoke(messages)
            
            # Store final response in memory
            final_metadata = {
                "triggered_by_ui_callback": True,
                "action_id": action_id,
                "ui_data_summary": f"Responded to UI callback with {len(str(ui_data))} chars of data"
            }
            self.memory.add_message(session_id, "agent", response.content, final_metadata)
            
            # Store result for the waiting stream endpoint
            self.callback_results[action_id] = {
                "response": response.content,
                "action_id": action_id,
                "ui_data": ui_data,
                "conversation_stats": self.memory.get_conversation_summary(session_id)
            }
            
            # Signal the waiting stream endpoint
            if action_id in self.callback_events:
                self.callback_events[action_id].set()
            
            # Clean up pending action
            del self.pending_actions[action_id]
            
            return {
                "status": "success",
                "message": "UI callback processed successfully",
                "action_id": action_id
            }
            
        except Exception as e:
            logger.error(f"UI callback processing error: {e}")
            # Signal error to waiting stream
            if action_id in self.callback_events:
                self.callback_results[action_id] = {"error": str(e)}
                self.callback_events[action_id].set()
            return {"error": str(e)}
    
    async def stream_response(self, user_query: str, session_id: str = "default") -> AsyncGenerator[str, None]:
        """Stream workflow response with events - now waits for UI callback results"""
        try:
            # Initial status
            yield json.dumps({
                "event_type": "status",
                "data": {"status": "working", "message": "Processing your request..."}
            }) + "\n"
            
            # Process message
            result = await self.process_message(user_query, session_id)
            
            # Emit action events
            for action in result["actions"]:
                yield json.dumps({
                    "event_type": "action",
                    "data": action
                }) + "\n"
            
            # If no UI callbacks needed, emit response immediately
            if not result["pending_ui_callback"]:
                yield json.dumps({
                    "event_type": "response", 
                    "data": {"text": result["response"], "final": True, "conversation_stats": result["conversation_stats"]}
                }) + "\n"
                
                yield json.dumps({
                    "event_type": "status",
                    "data": {"status": "complete", "message": "Task completed"}
                }) + "\n"
            else:
                # Wait for UI callback results
                yield json.dumps({
                    "event_type": "status",
                    "data": {"status": "waiting_ui", "message": "Waiting for UI results..."}
                }) + "\n"
                
                # Wait for all actions to complete
                for action in result["actions"]:
                    action_id = action["id"]
                    if action_id in self.callback_events:
                        try:
                            # Wait for UI callback (with timeout)
                            await asyncio.wait_for(self.callback_events[action_id].wait(), timeout=30.0)
                            
                            # Get the result
                            if action_id in self.callback_results:
                                callback_result = self.callback_results[action_id]
                                
                                if "error" in callback_result:
                                    yield json.dumps({
                                        "event_type": "status",
                                        "data": {"status": "error", "message": f"UI callback error: {callback_result['error']}"}
                                    }) + "\n"
                                else:
                                    # Emit final response based on UI results
                                    yield json.dumps({
                                        "event_type": "response",
                                        "data": {
                                            "text": callback_result["response"], 
                                            "final": True,
                                            "action_id": action_id,
                                            "conversation_stats": callback_result.get("conversation_stats", {})
                                        }
                                    }) + "\n"
                                    
                                    yield json.dumps({
                                        "event_type": "status",
                                        "data": {"status": "complete", "message": "Task completed with UI results"}
                                    }) + "\n"
                                
                                # Clean up
                                del self.callback_results[action_id]
                                del self.callback_events[action_id]
                                
                        except asyncio.TimeoutError:
                            yield json.dumps({
                                "event_type": "status",
                                "data": {"status": "timeout", "message": "UI callback timeout - no response from UI"}
                            }) + "\n"
                            
                            # Clean up
                            if action_id in self.callback_events:
                                del self.callback_events[action_id]
                            if action_id in self.callback_results:
                                del self.callback_results[action_id]
            
        except Exception as e:
            logger.error(f"Stream workflow error: {e}")
            yield json.dumps({
                "event_type": "status",
                "data": {"status": "error", "message": str(e)}
            }) + "\n"
    
    def get_conversation_history(self, session_id: str) -> Dict[str, Any]:
        """Get conversation history for a session"""
        return {
            "session_id": session_id,
            "summary": self.memory.get_conversation_summary(session_id),
            "context": self.memory.get_conversation_context(session_id)
        }
    
    def cleanup_old_conversations(self) -> int:
        """Clean up old conversation sessions"""
        return self.memory.cleanup_old_sessions()
    
    def get_all_conversations(self) -> Dict[str, Any]:
        """Get all active conversation sessions"""
        return self.memory.get_all_sessions() 