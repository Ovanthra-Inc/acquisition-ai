from sqlalchemy.orm import Session
from app.repository.notification_repo import NotificationRepository
from uuid import UUID

class NotificationService:
    def __init__(self):
        self.repo = NotificationRepository()

    def create_notification(self, db: Session, data: dict):
        return self.repo.create(db, data)

    def get_notifications(self, db: Session, user_id: UUID, unread_only: bool = False):
        return self.repo.get_by_user(db, user_id, unread_only)

    def mark_as_read(self, db: Session, notif_id: UUID, user_id: UUID):
        return self.repo.mark_read(db, notif_id, user_id)
