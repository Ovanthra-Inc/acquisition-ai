from typing import Annotated, Sequence, TypedDict, Dict, Any, List
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    # The list of messages in the conversation
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # Current goal
    goal: str
    # List of steps to execute
    steps: List[str]
    # Current step index
    current_step_index: int
    # Context data passed between tools
    context: Dict[str, Any]
    # Results of each step
    results: Dict[str, Any]
    # Human-in-the-loop approval status
    approved_to_send: bool
    # User and Tenant IDs for multi-tenancy
    user_id: str
    tenant_id: str
    internal_token: str
    status: str # 'active', 'paused', 'completed', 'failed'
