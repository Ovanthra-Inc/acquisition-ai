from acquisition_core.repository import BaseRepository
from app.models.inbox import InboxReply
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

class InboxRepository(BaseRepository[InboxReply]):
    def __init__(self, db: Session):
        super().__init__(InboxReply, db)

    def get_by_category(self, tenant_id: UUID, category: str) -> List[InboxReply]:
        return self.db.query(self.model).filter(
            self.model.tenant_id == tenant_id,
            self.model.category == category
        ).all()

    def get_interested_leads(self, tenant_id: UUID) -> List[InboxReply]:
        return self.get_by_category(tenant_id, "INTERESTED")
