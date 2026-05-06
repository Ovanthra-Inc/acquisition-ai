from sqlalchemy.orm import Session
from app.repository.email_repo import EmailRepository
from uuid import UUID

class EmailService:
    def __init__(self):
        self.repo = EmailRepository()

    def send_email(self, db: Session, campaign_id: UUID, lead_id: UUID, to_email: str, subject: str, body: str):
        # 1. Log the attempt
        log = self.repo.create_log(db, campaign_id, lead_id, subject, body)
        
        # 2. Integrate with Gmail / SMTP
        # ... logic ...
        print(f"Sending email to {to_email} with subject {subject}")
        
        # 3. Update log
        return self.repo.mark_sent(db, log.id)
