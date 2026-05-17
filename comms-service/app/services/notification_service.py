import httpx
from sqlalchemy.orm import Session
from app.repository.notification_repo import NotificationRepository
from app.core.config import settings
from uuid import UUID
import logging

class NotificationService:
    def __init__(self):
        self.repo = NotificationRepository()

    async def create_notification(self, data: dict):
        # In this architecture, we might not always have a DB session here if it's called from an async task
        # For now, let's just use the repo stub
        notification = self.repo.create(data)
        
        # Forward to API Gateway for real-time delivery
        user_id = data.get("user_id")
        if user_id:
            try:
                async with httpx.AsyncClient() as client:
                    await client.post(
                        f"{settings.API_GATEWAY_URL}/api/v1/internal/notify/{user_id}",
                        json=notification,
                        headers={"Authorization": f"Bearer {settings.INTERNAL_SERVICE_TOKEN}"}
                    )
            except Exception as e:
                logging.error(f"Failed to notify API Gateway: {e}")
        
        return notification

    def get_notifications(self, user_id: UUID, unread_only: bool = False):
        return self.repo.get_user_notifications(user_id)

    def mark_as_read(self, notification_ids: list[UUID]):
        return self.repo.mark_as_read(notification_ids)
