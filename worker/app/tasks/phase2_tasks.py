from app.core.celery_app import celery_app
import time
import httpx

@celery_app.task(name="app.tasks.phase2_tasks.enrich_lead_task")
def enrich_lead_task(lead_id: str):
    print(f"[Queue] Processing enrichment for lead {lead_id}")
    time.sleep(2)
    # httpx.post("http://enrichment-service:8000/api/v1/enrichment/enrich", ...)
    return True

@celery_app.task(name="app.tasks.phase2_tasks.score_leads_task")
def score_leads_task(lead_id: str):
    print(f"[Queue] Scoring lead {lead_id}")
    time.sleep(1)
    return True

@celery_app.task(name="app.tasks.phase2_tasks.fetch_replies_task")
def fetch_replies_task():
    print("[Queue] Polling IMAP/SMTP for incoming replies...")
    time.sleep(3)
    # Send found replies to conversation-service
    return True

@celery_app.task(name="app.tasks.phase2_tasks.track_event_task")
def track_event_task(event_data: dict):
    print(f"[Queue] Async tracking event: {event_data.get('type')}")
    # httpx.post("http://analytics-service:8000/api/v1/analytics/track", ...)
    return True
