from fastapi import APIRouter, Request, Depends
from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from app.services.audit_service import AuditService
from app.db.base import Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()
service = AuditService()

class AuditLogRequest(BaseModel):
    action: str
    metadata: Optional[dict] = None

@router.post("/")
async def create_audit_log(request: Request, body: AuditLogRequest, db: Session = Depends(get_db)):
    user_id = getattr(request.state, "user_id", "unknown")
    org_id = body.metadata.get("org_id", user_id) if body.metadata else user_id
    log = service.log_event(db, org_id, user_id, body.action, body.metadata)
    return {"id": str(log.id), "action": log.action, "created_at": str(log.created_at)}

@router.get("/user/{user_id}")
async def get_user_audit_logs(user_id: str, db: Session = Depends(get_db)):
    logs = service.get_user_logs(db, user_id)
    return {"logs": [{"id": str(l.id), "action": l.action, "created_at": str(l.created_at)} for l in logs]}

@router.get("/org/{org_id}")
async def get_org_audit_logs(org_id: str, db: Session = Depends(get_db)):
    logs = service.get_org_logs(db, org_id)
    return {"logs": [{"id": str(l.id), "action": l.action, "created_at": str(l.created_at)} for l in logs]}
