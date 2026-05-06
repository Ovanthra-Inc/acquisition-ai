from sqlalchemy.orm import Session
from app.models.email_log import EmailLog
from uuid import UUID
import datetime

class EmailRepository:
    def create_log(self, db: Session, campaign_id: UUID, lead_id: UUID, subject: str, body: str):
        log = EmailLog(campaign_id=campaign_id, lead_id=lead_id, subject=subject, body=body)
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def mark_sent(self, db: Session, log_id: UUID):
        log = db.query(EmailLog).filter(EmailLog.id == log_id).first()
        if log:
            log.status = "sent"
            log.sent_at = datetime.datetime.utcnow()
            db.commit()
            db.refresh(log)
        return log
