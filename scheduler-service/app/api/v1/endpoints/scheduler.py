from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
from datetime import datetime
from app.core.celery_app import celery_app

router = APIRouter()

class JobRequest(BaseModel):
    task_name: str
    run_at: datetime
    kwargs: Dict[str, Any] = {}

@router.post("/job")
async def schedule_job(job: JobRequest):
    """
    Schedules a Celery task to run at a specific UTC datetime.
    Example task_name: 'app.tasks.agent_tasks.run_agent_task'
    """
    try:
        # Send task to Celery with an ETA (Estimated Time of Arrival)
        result = celery_app.send_task(
            job.task_name,
            kwargs=job.kwargs,
            eta=job.run_at,
            queue="agent_queue" if "agent" in job.task_name else "default"
        )
        return {
            "message": "Job scheduled successfully", 
            "job_id": result.id,
            "run_at": job.run_at.isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to schedule job: {str(e)}")

@router.get("/jobs")
async def list_jobs():
    return {"message": "Job listing requires querying the Celery backend, currently unsupported."}

