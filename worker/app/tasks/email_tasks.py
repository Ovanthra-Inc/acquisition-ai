from app.core.celery_app import celery_app
import time
import httpx
import os
import hmac
import hashlib

INTERNAL_TOKEN = os.getenv("INTERNAL_SERVICE_TOKEN", "internal-secret")

def generate_worker_signature():
    data = "worker:system:worker"
    return hmac.new(INTERNAL_TOKEN.encode(), data.encode(), hashlib.sha256).hexdigest()

@celery_app.task(name="app.tasks.email_tasks.send_email_task", bind=True, max_retries=3, default_retry_delay=30)
def send_email_task(self, campaign_id: str, lead_id: str, to_email: str, subject: str, body: str):
    print(f"Executing queue job: Delegating email send to email-service for {to_email}")
    
    # Sign request as worker
    headers = {
        "Authorization": f"Bearer {INTERNAL_TOKEN}",
        "X-User-Id": "worker",
        "X-Tenant-Id": "system",
        "X-Service-Name": "worker",
        "X-Request-Signature": generate_worker_signature(),
    }
    
    payload = {
        "campaign_id": campaign_id,
        "lead_id": lead_id,
        "to_email": to_email,
        "subject": subject,
        "body": body
    }
    
    try:
        # The email-service now handles the SMTP logic and logging
        with httpx.Client(timeout=30.0) as client:
            res = client.post("http://email-service:8000/api/v1/emails/send", json=payload, headers=headers)
            res.raise_for_status()
            print("Email service successfully processed the send request.")
    except Exception as e:
        print(f"Email service delegation failed: {e}")
        # Retry on transient failures
        raise self.retry(exc=e)
    
    return True

