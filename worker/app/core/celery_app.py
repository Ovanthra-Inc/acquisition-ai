from celery import Celery
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "worker",
    broker=redis_url,
    backend=redis_url,
    include=["app.tasks.email_tasks", "app.tasks.agent_tasks", "app.tasks.deliverability_tasks"]
)

celery_app.conf.task_routes = {
    "app.tasks.email_tasks.*": {"queue": "email-queue"},
    "app.tasks.agent_tasks.*": {"queue": "default-queue"},
    "*": {"queue": "default-queue"},
}

celery_app.conf.task_queues = {
    "default-queue": {
        "exchange": "default",
        "routing_key": "default",
    },
    "email-queue": {
        "exchange": "email",
        "routing_key": "email",
    },
    "scrape-queue": {
        "exchange": "scrape",
        "routing_key": "scrape",
    },
}
