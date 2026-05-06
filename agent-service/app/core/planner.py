from app.core.state_manager import AgentState
from typing import Dict, Any

class PlannerNode:
    def __init__(self):
        pass

    async def __call__(self, state: AgentState) -> Dict[str, Any]:
        goal = state["goal"]
        steps = []
        
        # Phase 4: Multi-Domain Intelligent Planning
        goal_lower = goal.lower()
        if "hiring" in goal_lower:
            steps = ["search_domain_hiring", "detect_signal", "merge_lead_data", "generate_email", "send_email"]
        elif "local" in goal_lower or "maps" in goal_lower:
            steps = ["search_domain_local", "merge_lead_data", "score_lead", "generate_email", "send_email"]
        elif "saas" in goal_lower:
            steps = ["search_domain_website", "enrich_lead", "score_lead", "generate_email", "create_campaign", "send_email"]
        else:
            steps = ["search_domain_website", "index_search_data"]
            
        return {
            "steps": steps,
            "current_step_index": 0,
            "status": "executing"
        }
