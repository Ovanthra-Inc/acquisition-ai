from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.models.scheduled_job import ScheduledJob
import datetime
import logging

@celery_app.task(name="app.tasks.scheduler_tasks.poll_scheduled_jobs")
def poll_scheduled_jobs():
    """
    Polls the database for jobs that are due to run and dispatches them.
    """
    db = SessionLocal()
    try:
        now = datetime.datetime.utcnow()
        # Find jobs that are due and not yet processed
        due_jobs = db.query(ScheduledJob).filter(
            ScheduledJob.run_at <= now,
            ScheduledJob.is_processed == False
        ).all()
        
        for job in due_jobs:
            logging.info(f"Dispatching scheduled job: {job.task_name} (ID: {job.id})")
            
            # Dispatch to Celery
            celery_app.send_task(
                job.task_name,
                kwargs=job.kwargs,
                # No ETA here because it's due NOW
                queue="agent_queue" if "agent" in job.task_name else "default"
            )
            
            # Mark as processed
            job.is_processed = True
            job.processed_at = datetime.datetime.utcnow()
            
        db.commit()
    except Exception as e:
        logging.error(f"Error polling scheduled jobs: {e}")
        db.rollback()
    finally:
        db.close()
