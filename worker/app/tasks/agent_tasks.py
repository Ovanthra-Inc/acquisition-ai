from app.core.celery_app import celery_app
import httpx
import logging
from app.core.config import settings
from acquisition_core.middleware.internal_auth import generate_internal_signature


@celery_app.task(name="app.tasks.agent_tasks.run_recipe_steps", bind=True, max_retries=3, default_retry_delay=60)
def run_recipe_steps(self, recipe_id: str, steps: list, context: dict, user_id: str):
    """
    Phase 3: Async recipe execution via Celery.
    Triggers the agent-service to run a planned set of steps.
    """

    logging.info(f"[Worker] Executing recipe {recipe_id} with steps: {steps}")
    
    # Sign request as worker
    sig = generate_internal_signature(settings.INTERNAL_SERVICE_TOKEN, "worker", "system", "worker")
    headers = {
        "Authorization": f"Bearer {settings.INTERNAL_SERVICE_TOKEN}",
        "X-User-Id": user_id or "worker",
        "X-Tenant-Id": "system",
        "X-Service-Name": "worker",
        "X-Request-Signature": sig,
    }
    
    payload = {
        "goal": f"Execute recipe steps: {', '.join(steps)}",
        "approved_to_send": False,  # Recipes still respect human-in-the-loop
    }
    
    try:
        with httpx.Client(timeout=60.0) as client:
            res = client.post(
                f"{settings.AGENT_SERVICE_URL}/api/v1/agent/run",
                json=payload,
                headers=headers
            )
            res.raise_for_status()
            result = res.json()
            logging.info(f"[Worker] Recipe {recipe_id} execution result: {result.get('status')}")
            return result
    except Exception as e:
        logging.error(f"[Worker] Recipe execution failed for {recipe_id}: {e}")
        return {"status": "failed", "error": str(e)}

@celery_app.task(name="app.tasks.agent_tasks.retry_job")
def retry_job(task_name: str, args: list, queue: str = "default-queue", countdown: int = 60):
    """
    Phase 3: Retry a failed task after a delay.
    """
    logging.info(f"[Worker] Retrying job {task_name} in {countdown}s")
    celery_app.send_task(task_name, args=args, queue=queue, countdown=countdown)
    return {"status": "retry_scheduled", "task": task_name, "delay_seconds": countdown}
