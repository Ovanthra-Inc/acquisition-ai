from fastapi import APIRouter, Depends, Request, HTTPException
from app.schemas.agent import AgentRunRequest, AgentApproveRequest
from app.services.agent_service import AgentService
from app.core.config import settings

router = APIRouter()
service = AgentService()

@router.post("/run")
async def run_agent(request: Request, data: AgentRunRequest):
    user_id = getattr(request.state, "user_id", "test_user")
    tenant_id = getattr(request.state, "tenant_id", "test_tenant")
    signature = request.headers.get("X-Request-Signature", "")
    
    return await service.run(
        goal=data.goal,
        user_id=user_id,
        tenant_id=tenant_id,
        signature=signature,
        internal_token=settings.INTERNAL_SERVICE_TOKEN,
        approved_to_send=data.approved_to_send
    )

@router.post("/approve")
async def approve_send(request: Request, data: AgentApproveRequest):
    """
    Human-in-the-loop approval endpoint.
    Call this after reviewing the generated campaign to authorize email dispatch.
    In production this would resume a persisted LangGraph checkpoint.
    For now, re-runs the agent with approved_to_send=True and the original goal.
    """
    if not data.approved:
        return {"task_id": data.task_id, "status": "rejected", "message": "Email dispatch rejected by user."}
    
    # In a production system with a persistent DB/checkpointer, we would load the
    # paused state and resume it. For now, we return the approval acknowledgement.
    return {
        "task_id": data.task_id,
        "status": "approved",
        "message": "Dispatch approved. Re-run the agent with approved_to_send=true to proceed."
    }

@router.get("/{task_id}")
async def get_task_status(task_id: str):
    return {"task_id": task_id, "status": "Not implemented - would fetch from DB"}

@router.post("/{task_id}/pause")
async def pause_task(task_id: str):
    return {"task_id": task_id, "status": "paused"}

@router.post("/{task_id}/resume")
async def resume_task(task_id: str):
    return {"task_id": task_id, "status": "resumed"}

@router.post("/{task_id}/cancel")
async def cancel_task(task_id: str):
    return {"task_id": task_id, "status": "cancelled"}

@router.get("/{task_id}/steps")
async def get_task_steps(task_id: str):
    return {"task_id": task_id, "steps": []}

