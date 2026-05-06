from sqlalchemy.orm import Session
from app.models.audit import AuditLog
from uuid import UUID
from typing import Optional

class AuditRepository:
    def create(self, db: Session, org_id: UUID, user_id: UUID, action: str, metadata: dict = None):
        log = AuditLog(
            organization_id=org_id,
            user_id=user_id,
            action=action,
            metadata_json=metadata or {}
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def get_by_org(self, db: Session, org_id: UUID, limit: int = 50):
        return db.query(AuditLog).filter(
            AuditLog.organization_id == org_id
        ).order_by(AuditLog.created_at.desc()).limit(limit).all()

    def get_by_user(self, db: Session, user_id: UUID, limit: int = 50):
        return db.query(AuditLog).filter(
            AuditLog.user_id == user_id
        ).order_by(AuditLog.created_at.desc()).limit(limit).all()
