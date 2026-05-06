from sqlalchemy.orm import Session
from app.repository.campaign_repo import CampaignRepository
from uuid import UUID
from typing import List
from celery import Celery
import os

# Singleton Celery app — never create per-request
redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
_celery_app = Celery("campaign", broker=redis_url)

class CampaignService:
    def __init__(self):
        self.repo = CampaignRepository()

    def create(self, db: Session, user_id: UUID, name: str):
        return self.repo.create_campaign(db, user_id, name)

    def list_all(self, db: Session, user_id: UUID):
        return self.repo.get_campaigns(db, user_id)

    def get_by_id(self, db: Session, campaign_id: UUID, user_id: UUID):
        """Fetch a single campaign, enforcing ownership."""
        campaign = self.repo.get_campaign_by_id(db, campaign_id)
        if not campaign or str(campaign.user_id) != str(user_id):
            return None
        return campaign

    def attach_leads(self, db: Session, campaign_id: UUID, lead_ids: List[UUID]):
        self.repo.add_leads(db, campaign_id, lead_ids)
        return {"message": f"Added {len(lead_ids)} leads to campaign"}

    def send_campaign(self, db: Session, campaign_id: UUID, user_id: UUID):
        """Enqueue emails for all leads attached to this campaign."""
        campaign = self.repo.get_campaign_by_id(db, campaign_id)
        if not campaign:
            return {"error": "Campaign not found"}
        if str(campaign.user_id) != str(user_id):
            return {"error": "Unauthorized: campaign does not belong to user"}
        
        # Get all leads attached to this campaign
        campaign_leads = self.repo.get_campaign_leads(db, campaign_id)
        
        if not campaign_leads:
            return {"error": "No leads attached to campaign"}
        
        enqueued = 0
        for cl in campaign_leads:
            if not cl.email_sent:
                _celery_app.send_task(
                    "app.tasks.email_tasks.send_email_task",
                    args=[
                        str(campaign_id), 
                        str(cl.lead_id), 
                        cl.email or "unknown@example.com",
                        f"Campaign: {campaign.name}",  # Subject — in production, use AI-generated
                        f"Hello from {campaign.name}"   # Body — in production, use AI-generated
                    ],
                    queue="email-queue"
                )
                enqueued += 1
        
        # Update campaign status
        self.repo.update_status(db, campaign_id, "sending")
        
        return {"message": f"Enqueued {enqueued} emails for campaign", "campaign_id": str(campaign_id)}

