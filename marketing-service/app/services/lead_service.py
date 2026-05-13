from app.repository.lead_repo import LeadRepository
from uuid import UUID

class LeadService:

    def __init__(self):
        self.repo = LeadRepository()

    def create_lead(self, db, lead_data: dict):
        return self.repo.create(db, lead_data)

    def list_leads(self, db, user_id: UUID):
        return self.repo.get_all(db, user_id)
