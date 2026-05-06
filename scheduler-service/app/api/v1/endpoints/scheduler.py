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

from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.scheduled_job import ScheduledJob

@router.post("/job")
async def schedule_job(job: JobRequest, db: Session = Depends(get_db)):
    """
    Schedules a job by persisting it to the database.
    A Celery Beat task will pick this up and execute it at the right time.
    """
    try:
        db_job = ScheduledJob(
            task_name=job.task_name,
            run_at=job.run_at,
            kwargs=job.kwargs
        )
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        
        return {
            "message": "Job persisted successfully", 
            "job_id": str(db_job.id),
            "run_at": db_job.run_at.isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to persist job: {str(e)}")

@router.get("/jobs")
async def list_jobs():
    return {"message": "Job listing requires querying the Celery backend, currently unsupported."}

