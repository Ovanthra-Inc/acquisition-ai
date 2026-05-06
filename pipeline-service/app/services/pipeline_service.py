from sqlalchemy.orm import Session
from app.repository.pipeline_repo import PipelineRepository
from uuid import UUID

class PipelineService:
    def __init__(self):
        self.repo = PipelineRepository()

    def initialize_default_stages(self, db: Session, user_id: UUID):
        existing = self.repo.get_stages(db, user_id)
        if existing:
            return existing
            
        defaults = [
            ("Lead", 1.0),
            ("Contacted", 2.0),
            ("Replied", 3.0),
            ("Meeting Booked", 4.0),
            ("Closed/Won", 5.0)
        ]
        
        stages = []
        for name, order in defaults:
            stages.append(self.repo.create_stage(db, user_id, name, order))
        return stages

    def create_deal(self, db: Session, user_id: UUID, lead_id: UUID, campaign_id: UUID = None, value: float = 0.0):
        stages = self.initialize_default_stages(db, user_id)
        first_stage_id = stages[0].id
        return self.repo.create_deal(db, user_id, lead_id, first_stage_id, campaign_id, value)

    def get_deals(self, db: Session, user_id: UUID):
        return self.repo.get_deals(db, user_id)

    def get_stages(self, db: Session, user_id: UUID):
        return self.initialize_default_stages(db, user_id)

    def update_deal_stage(self, db: Session, deal_id: UUID, user_id: UUID, new_stage_id: UUID):
        return self.repo.update_deal_stage(db, deal_id, user_id, new_stage_id)
