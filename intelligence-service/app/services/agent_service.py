from langgraph.graph import StateGraph, END
from app.core.state_manager import AgentState
from app.core.planner import PlannerNode
from app.core.executor import ExecutorNode, should_continue
from langgraph.checkpoint.redis.aio import RedisSaver
from app.core.config import settings
import uuid
from typing import Dict, Any, Optional

class AgentService:
    def __init__(self):
        # Initialize LangGraph
        self.graph = StateGraph(AgentState)
        
        # Add nodes
        self.graph.add_node("planner", PlannerNode())
        self.graph.add_node("executor", ExecutorNode())
        
        # Define edges
        self.graph.set_entry_point("planner")
        self.graph.add_edge("planner", "executor")
        
        # Conditional edge for execution loop
        self.graph.add_conditional_edges(
            "executor",
            should_continue,
            {
                "execute": "executor",
                "end": END
            }
        )
    
    async def run(self, goal: str, user_id: str, tenant_id: str, signature: str, internal_token: str, approved_to_send: bool = False, task_id: Optional[str] = None) -> Dict[str, Any]:
        task_id = task_id or str(uuid.uuid4())
        config = {"configurable": {"thread_id": task_id}}
        
        initial_state = {
            "task_id": task_id,
            "goal": goal,
            "user_id": user_id,
            "tenant_id": tenant_id,
            "internal_token": internal_token,
            "signature": signature,
            "approved_to_send": approved_to_send,
            "steps": [],
            "current_step_index": 0,
            "context": {},
            "results": {},
            "status": "pending"
        }
        
        try:
            async with RedisSaver.from_conn_string(settings.REDIS_URL) as checkpointer:
                app = self.graph.compile(checkpointer=checkpointer)
                final_state = await app.ainvoke(initial_state, config=config)
                return self._format_response(task_id, final_state)
        except Exception as e:
            return {"task_id": task_id, "status": "failed", "error": str(e)}

    async def resume(self, task_id: str, approved_to_send: bool = True) -> Dict[str, Any]:
        """Resumes a paused agent execution."""
        config = {"configurable": {"thread_id": task_id}}
        try:
            async with RedisSaver.from_conn_string(settings.REDIS_URL) as checkpointer:
                app = self.graph.compile(checkpointer=checkpointer)
                # When resuming, we only want to update the 'approved_to_send' flag
                final_state = await app.ainvoke(
                    {"approved_to_send": approved_to_send}, 
                    config=config
                )
                return self._format_response(task_id, final_state)
        except Exception as e:
            return {"task_id": task_id, "status": "failed", "error": str(e)}

    def _format_response(self, task_id: str, state: Dict[str, Any]) -> Dict[str, Any]:
        status = state.get("status")
        response = {
            "task_id": task_id,
            "status": status,
            "results": state.get("results"),
            "message": "Agent execution completed."
        }
        if status == "paused":
            response["message"] = state.get("reason", "Awaiting human approval.")
            response["action_required"] = "Call /agent/approve with task_id to proceed."
        return response
