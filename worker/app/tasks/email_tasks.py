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
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    print(f"Executing queue job: Sending email to {to_email}")
    
    # SMTP Configuration (In production, load these from secure environment variables)
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    
    if SMTP_USER and SMTP_PASSWORD:
        try:
            msg = MIMEMultipart()
            msg['From'] = SMTP_USER
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'html')) # Assuming HTML bodies

            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.send_message(msg)
                
            print(f"SMTP send successful to {to_email}!")
        except Exception as e:
            print(f"SMTP send failed: {e}")
            raise self.retry(exc=e)
    else:
        print(f"SMTP credentials missing. Simulated send to {to_email} successful!")
        time.sleep(1) # Simulation delay if no real credentials provided
    
    # Notify email-service to log this
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
        with httpx.Client(timeout=10.0) as client:
            res = client.post("http://email-service:8000/api/v1/emails/send", json=payload, headers=headers)
            res.raise_for_status()
            print("Successfully logged to email-service.")
    except Exception as e:
        print(f"Failed to log email send: {e}")
        # Retry on transient failures
        raise self.retry(exc=e)
    
    return True

