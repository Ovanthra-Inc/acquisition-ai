from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.session import get_db
from app.schemas.email import SendEmailRequest, EmailLogResponse
from app.services.email_service import EmailService

router = APIRouter()
service = EmailService()

@router.post("/send", response_model=EmailLogResponse)
def send_email(request: Request, data: SendEmailRequest, db: Session = Depends(get_db)):
    return service.send_email(db, data.campaign_id, data.lead_id, data.to_email, data.subject, data.body)
