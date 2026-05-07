from app.core.celery_app import celery_app
import time
import httpx
from app.core.config import settings
from acquisition_core.middleware.internal_auth import generate_internal_signature

@celery_app.task(name="app.tasks.email_tasks.send_email_task", bind=True, max_retries=3, default_retry_delay=30)
def send_email_task(self, campaign_id: str, lead_id: str, to_email: str, subject: str, body: str):
    print(f"Executing queue job: Delegating email send to email-service for {to_email}")

    # Sign request as worker
    sig = generate_internal_signature(settings.INTERNAL_SERVICE_TOKEN, "worker", "system", "worker")
    headers = {
        "Authorization": f"Bearer {settings.INTERNAL_SERVICE_TOKEN}",
        "X-User-Id": "worker",
        "X-Tenant-Id": "system",
        "X-Service-Name": "worker",
        "X-Request-Signature": sig,
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
            res = client.post(f"{settings.EMAIL_SERVICE_URL}/api/v1/emails/send", json=payload, headers=headers)
            res.raise_for_status()
            print("Email service successfully processed the send request.")
    except Exception as e:
        print(f"Email service delegation failed: {e}")
        # Retry on transient failures
        raise self.retry(exc=e)
    
    return True

