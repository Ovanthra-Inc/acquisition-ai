from langgraph.graph import StateGraph, END
from app.core.state_manager import AgentState
from app.core.planner import PlannerNode
from app.core.executor import ExecutorNode, should_continue
import uuid
from typing import Dict, Any

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
        
        # Compile graph
        self.app = self.graph.compile()

    async def run(self, goal: str, user_id: str, tenant_id: str, signature: str, internal_token: str, approved_to_send: bool = False) -> Dict[str, Any]:
        task_id = str(uuid.uuid4())
        
        initial_state = {
            "task_id": task_id,
            "goal": goal,
            "user_id": user_id,
            "tenant_id": tenant_id,
            "internal_token": internal_token,
            "signature": signature,
            "approved_to_send": approved_to_send,  # Human-in-the-loop gate
            "steps": [],
            "current_step_index": 0,
            "context": {},
            "results": {},
            "status": "pending"
        }
        
        try:
            final_state = await self.app.ainvoke(initial_state)
            status = final_state.get("status")
            
            response = {
                "task_id": task_id,
                "status": status,
                "results": final_state.get("results"),
                "message": "Agent execution completed."
            }
            
            # Surface human-in-the-loop pause reason to caller
            if status == "paused":
                response["message"] = final_state.get("reason", "Awaiting human approval.")
                response["action_required"] = "Call /agent/approve with task_id to proceed."
                
            return response
        except Exception as e:
            return {
                "task_id": task_id,
                "status": "failed",
                "error": str(e)
            }

