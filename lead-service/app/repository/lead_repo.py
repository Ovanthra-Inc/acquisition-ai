from sqlalchemy.orm import Session
from app.models.lead import Lead
from uuid import UUID

class LeadRepository:

    def create(self, db: Session, lead_data: dict):
        lead = Lead(**lead_data)
        db.add(lead)
        db.commit()
        db.refresh(lead)
        return lead

    def get_all(self, db: Session, user_id: UUID):
        return db.query(Lead).filter(Lead.user_id == user_id).all()
