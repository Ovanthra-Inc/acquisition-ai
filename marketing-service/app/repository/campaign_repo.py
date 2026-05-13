from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models.campaign import Campaign, CampaignLead
from uuid import UUID
from typing import List

class CampaignRepository:
    def create_campaign(self, db: Session, user_id: UUID, name: str):
        campaign = Campaign(user_id=user_id, name=name)
        db.add(campaign)
        db.commit()
        db.refresh(campaign)
        return campaign

    def get_campaigns(self, db: Session, user_id: UUID):
        return db.query(Campaign).filter(Campaign.user_id == user_id).all()

    def get_campaign_by_id(self, db: Session, campaign_id: UUID):
        return db.query(Campaign).filter(Campaign.id == campaign_id).first()

    def get_campaign_leads(self, db: Session, campaign_id: UUID):
        """Get campaign_leads with email and personalization from leads table via raw join."""
        result = db.execute(
            text("""
                SELECT cl.id, cl.campaign_id, cl.lead_id, cl.email_sent, cl.replied, 
                       cl.personalized_subject, cl.personalized_body, l.email
                FROM campaign_leads cl
                LEFT JOIN leads l ON cl.lead_id = l.id
                WHERE cl.campaign_id = :cid
            """),
            {"cid": str(campaign_id)}
        ).fetchall()
        return result

    def add_leads(self, db: Session, campaign_id: UUID, leads_data: List[dict]):
        campaign_leads = []
        for lead in leads_data:
            cl = CampaignLead(
                campaign_id=campaign_id, 
                lead_id=lead["lead_id"],
                personalized_subject=lead.get("personalized_subject"),
                personalized_body=lead.get("personalized_body")
            )
            db.add(cl)
            campaign_leads.append(cl)
        db.commit()
        return campaign_leads

    def update_status(self, db: Session, campaign_id: UUID, status: str):
        campaign = self.get_campaign_by_id(db, campaign_id)
        if campaign:
            campaign.status = status
            db.commit()
        return campaign

