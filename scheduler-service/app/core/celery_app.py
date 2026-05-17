import os
from celery import Celery

broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
backend_url = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

celery_app = Celery(
    "scheduler",
    broker=broker_url,
    backend=backend_url
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    beat_schedule={
        "poll-scheduled-jobs-every-minute": {
            "task": "app.tasks.scheduler_tasks.poll_scheduled_jobs",
            "schedule": 60.0,
        },
        "check-domain-reputation-daily": {
            "task": "app.tasks.deliverability_tasks.check_reputation_task",
            "schedule": 86400.0, # 24 hours
            "args": ("ovanthra.com",)
        },
        "dispatch-warmup-emails-every-6h": {
            "task": "app.tasks.deliverability_tasks.warmup_dispatch_task",
            "schedule": 21600.0, # 6 hours
            "args": ("ovanthra.com", 15)
        },
    },
)
