from typing import TypedDict, List, Dict, Any, Optional

class AgentState(TypedDict):
    task_id: str
    goal: str
    user_id: str
    tenant_id: str
    internal_token: str
    signature: str
    approved_to_send: bool
    steps: List[str]
    current_step_index: int
    context: Dict[str, Any]
    results: Dict[str, Any]
    status: str
    reason: Optional[str]
    error: Optional[str]

