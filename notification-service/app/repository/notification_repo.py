from sqlalchemy.orm import Session
from app.models.notification import Notification
from uuid import UUID

class NotificationRepository:
    def create(self, db: Session, data: dict):
        notif = Notification(**data)
        db.add(notif)
        db.commit()
        db.refresh(notif)
        return notif

    def get_by_user(self, db: Session, user_id: UUID, unread_only: bool = False):
        query = db.query(Notification).filter(Notification.user_id == user_id)
        if unread_only:
            query = query.filter(Notification.is_read == False)
        return query.order_by(Notification.created_at.desc()).all()

    def mark_read(self, db: Session, notif_id: UUID, user_id: UUID):
        notif = db.query(Notification).filter(Notification.id == notif_id, Notification.user_id == user_id).first()
        if notif:
            notif.is_read = True
            db.commit()
            db.refresh(notif)
        return notif
