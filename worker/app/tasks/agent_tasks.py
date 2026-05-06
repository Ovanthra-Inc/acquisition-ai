from app.core.celery_app import celery_app
import httpx
import os
import hmac
import hashlib
import logging

INTERNAL_TOKEN = os.getenv("INTERNAL_SERVICE_TOKEN", "internal-secret")

def generate_agent_task_signature():
    data = "worker:system:worker"
    return hmac.new(INTERNAL_TOKEN.encode(), data.encode(), hashlib.sha256).hexdigest()

def get_internal_headers():
    return {
        "Authorization": f"Bearer {INTERNAL_TOKEN}",
        "X-User-Id": "worker",
        "X-Tenant-Id": "system",
        "X-Service-Name": "worker",
        "X-Request-Signature": generate_agent_task_signature(),
    }

@celery_app.task(name="app.tasks.agent_tasks.run_recipe_steps", bind=True, max_retries=3, default_retry_delay=60)
def run_recipe_steps(self, recipe_id: str, steps: list, context: dict, user_id: str):
    """
    Phase 3: Async recipe execution via Celery.
    Triggers the agent-service to run a planned set of steps.
    This allows fully automated, scheduled recipe execution without user input.
    """
    logging.info(f"[Worker] Executing recipe {recipe_id} with steps: {steps}")
    
    headers = get_internal_headers()
    
    # Override user context from recipe execution
    if user_id:
        headers["X-User-Id"] = user_id
    
    payload = {
        "goal": f"Execute recipe steps: {', '.join(steps)}",
        "approved_to_send": False,  # Recipes still respect human-in-the-loop
    }
    
    try:
        with httpx.Client(timeout=60.0) as client:
            res = client.post(
                "http://agent-service:8000/api/v1/agent/run",
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
