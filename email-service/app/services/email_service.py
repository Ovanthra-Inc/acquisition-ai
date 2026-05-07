from sqlalchemy.orm import Session
from app.repository.email_repo import EmailRepository
from uuid import UUID

class EmailService:
    def __init__(self):
        self.repo = EmailRepository()

    def send_email(self, db: Session, campaign_id: UUID, lead_id: UUID, to_email: str, subject: str, body: str):
        # 1. Log the attempt
        log = self.repo.create_log(db, campaign_id, lead_id, subject, body)
        
        # 2. DELIVERABILITY CHECK (Phase 5)
        # Extract domain from to_email (or from SMTP_USER)
        # In a real scenario, we'd check the reputation of our sending domain.
        import os
        from acquisition_core.client import get_internal_client
        from app.core.config import settings
        import asyncio
        
        domain = to_email.split("@")[-1]
        
        def check_reputation():
            from acquisition_core.client import get_sync_internal_client
            with get_sync_internal_client(settings.INTERNAL_SERVICE_TOKEN, "system", "system", "email-service") as client:
                try:
                    res = client.get(f"{settings.DELIVERABILITY_SERVICE_URL}/api/v1/deliverability/reputation/{domain}")
                    if res.status_code == 200:
                        rep = res.json()
                        if rep.get("status") == "critical":
                            return False
                    return True
                except:
                    return True # Fallback to true if service is down

        if not check_reputation():
            print(f"Aborting send to {to_email} due to critical domain reputation.")
            return self.repo.mark_failed(db, log.id, "Critical domain reputation")

        # 3. SMTP Sending
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

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
                msg.attach(MIMEText(body, 'html'))

                with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                    server.starttls()
                    server.login(SMTP_USER, SMTP_PASSWORD)
                    server.send_message(msg)
                print(f"SMTP send successful to {to_email}!")
            except Exception as e:
                print(f"SMTP send failed: {e}")
                return self.repo.mark_failed(db, log.id, str(e))
        else:
            print(f"SMTP credentials missing. Simulated send to {to_email} successful!")
        
        # 4. Update log
        return self.repo.mark_sent(db, log.id)
