from sqlalchemy.orm import Session
from app.repository.audit_repo import AuditRepository
from uuid import UUID

class AuditService:
    def __init__(self):
        self.repo = AuditRepository()

    def log_event(self, db: Session, org_id: UUID, user_id: UUID, action: str, metadata: dict = None):
        return self.repo.create(db, org_id, user_id, action, metadata)

    def get_org_logs(self, db: Session, org_id: UUID, limit: int = 50):
        return self.repo.get_by_org(db, org_id, limit)

    def get_user_logs(self, db: Session, user_id: UUID, limit: int = 50):
        return self.repo.get_by_user(db, user_id, limit)
