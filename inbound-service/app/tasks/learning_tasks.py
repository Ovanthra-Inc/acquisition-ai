from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "inbound_tasks",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

@celery_app.task(name="app.tasks.learning_tasks.extract_patterns_task")
def extract_patterns_task(tenant_id: str, original_email: str, positive_reply: str):
    """Background task to trigger learning in the intelligence-service."""
    import httpx
    # Call the intelligence-service internal learning endpoint
    url = f"http://intelligence-service:8000/api/v1/internal/learn"
    payload = {
        "tenant_id": tenant_id,
        "original_email": original_email,
        "positive_reply": positive_reply
    }
    # Fire and forget or handle response
    httpx.post(url, json=payload)
