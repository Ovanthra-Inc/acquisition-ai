from sqlalchemy.orm import Session
from app.repository.email_repo import EmailRepository
from uuid import UUID

class EmailService:
    def __init__(self):
        self.repo = EmailRepository()

    def send_email(self, db: Session, campaign_id: UUID, lead_id: UUID, to_email: str, subject: str, body: str):
        # 1. Log the attempt (creates DB record)
        log = self.repo.create_log(db, campaign_id, lead_id, subject, body)
        
        # 2. Dispatch the Celery task (Async)
        from app.tasks.email_worker import send_smtp_email
        send_smtp_email.apply_async(
            args=[str(log.id), to_email, subject, body],
            queue="email-queue"
        )
        
        # 3. Return immediately
        return log
