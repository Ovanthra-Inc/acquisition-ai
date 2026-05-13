from sqlalchemy.orm import Session
from app.models.pipeline import PipelineStage, Deal
from uuid import UUID

class PipelineRepository:
    def create_stage(self, db: Session, user_id: UUID, name: str, order: float):
        stage = PipelineStage(user_id=user_id, name=name, order=order)
        db.add(stage)
        db.commit()
        db.refresh(stage)
        return stage

    def get_stages(self, db: Session, user_id: UUID):
        return db.query(PipelineStage).filter(PipelineStage.user_id == user_id).order_by(PipelineStage.order).all()

    def create_deal(self, db: Session, user_id: UUID, lead_id: UUID, stage_id: UUID, campaign_id: UUID = None, value: float = 0.0):
        deal = Deal(
            user_id=user_id,
            lead_id=lead_id,
            stage_id=stage_id,
            campaign_id=campaign_id,
            value=value
        )
        db.add(deal)
        db.commit()
        db.refresh(deal)
        return deal

    def get_deals(self, db: Session, user_id: UUID):
        return db.query(Deal).filter(Deal.user_id == user_id).all()

    def update_deal_stage(self, db: Session, deal_id: UUID, user_id: UUID, new_stage_id: UUID):
        deal = db.query(Deal).filter(Deal.id == deal_id, Deal.user_id == user_id).first()
        if deal:
            deal.stage_id = new_stage_id
            db.commit()
            db.refresh(deal)
        return deal
