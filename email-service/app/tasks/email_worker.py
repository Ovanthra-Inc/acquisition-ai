import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.celery_app import celery_app
from app.repository.email_repo import EmailRepository
from app.db.session import SessionLocal
from acquisition_core.client import get_sync_internal_client
from app.core.config import settings
from uuid import UUID

@celery_app.task(name="app.tasks.email_worker.send_smtp_email", bind=True, max_retries=3)
def send_smtp_email(self, log_id: str, to_email: str, subject: str, body: str):
    db = SessionLocal()
    repo = EmailRepository()
    try:
        domain = to_email.split("@")[-1]
        
        # Check Reputation
        def check_reputation():
            with get_sync_internal_client(settings.INTERNAL_SERVICE_TOKEN, "system", "system", "email-service") as client:
                try:
                    res = client.get(f"{settings.DELIVERABILITY_SERVICE_URL}/api/v1/deliverability/reputation/{domain}")
                    if res.status_code == 200:
                        rep = res.json()
                        if rep.get("status") == "critical":
                            return False
                    return True
                except:
                    return True
                    
        if not check_reputation():
            print(f"Aborting send to {to_email} due to critical domain reputation.")
            repo.mark_failed(db, UUID(log_id), "Critical domain reputation")
            return
            
        SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
        SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
        SMTP_USER = os.getenv("SMTP_USER")
        SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

        if SMTP_USER and SMTP_PASSWORD:
            msg = MIMEMultipart()
            msg['From'] = SMTP_USER
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'html'))

            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.send_message(msg)
            print(f"SMTP send successful to {to_email}!")
        else:
            print(f"SMTP credentials missing. Simulated send to {to_email} successful!")
            
        repo.mark_sent(db, UUID(log_id))
        
    except Exception as e:
        print(f"SMTP send failed: {e}")
        repo.mark_failed(db, UUID(log_id), str(e))
        raise self.retry(exc=e, countdown=60)
    finally:
        db.close()
