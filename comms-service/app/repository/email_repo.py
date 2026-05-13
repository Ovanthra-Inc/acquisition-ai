from app.models.email_log import EmailLog
from acquisition_core.repository import BaseRepository
from sqlalchemy.orm import Session
from uuid import UUID
import datetime

class EmailRepository(BaseRepository[EmailLog]):
    def __init__(self):
        super().__init__(EmailLog)

    def create_log(self, db: Session, campaign_id: UUID, lead_id: UUID, subject: str, body: str) -> EmailLog:
        log = EmailLog(
            campaign_id=campaign_id,
            lead_id=lead_id,
            subject=subject,
            body=body,
            status="pending"
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def update_status(self, db: Session, log_id: UUID, status: str):
        log = self.get(db, log_id)
        if log:
            log.status = status
            if status == "sent":
                log.sent_at = datetime.datetime.utcnow()
            db.add(log)
            db.commit()
            db.refresh(log)
        return log
