from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.session import get_db
from app.schemas.notification import NotificationCreate, NotificationResponse, ReadRequest
from app.services.notification_service import NotificationService

router = APIRouter()
service = NotificationService()

@router.get("/", response_model=list[NotificationResponse])
def get_notifications(request: Request, unread_only: bool = False, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.get_notifications(db, user_id, unread_only)

@router.post("/read", response_model=NotificationResponse)
def mark_read(request: Request, data: ReadRequest, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    notif = service.mark_as_read(db, data.notification_id, user_id)
    if not notif:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notif

# Internal endpoint for other services to create notifications
@router.post("/internal/create", response_model=NotificationResponse)
def internal_create_notification(request: Request, data: NotificationCreate, db: Session = Depends(get_db)):
    return service.create_notification(db, data.dict())
