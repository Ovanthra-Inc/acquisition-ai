from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.inbox_service import InboxService
from app.repository.inbox_repository import InboxRepository
from typing import List, Any
from uuid import UUID

router = APIRouter()
service = InboxService()

@router.post("/process-reply")
async def process_reply(request: Request, db: Session = Depends(get_db)):
    """Receives an email reply, classifies it, and stores it."""
    data = await request.json()
    tenant_id = request.headers.get("X-Tenant-Id")
    
    if not tenant_id:
        raise HTTPException(status_code=400, detail="X-Tenant-Id header required")
        
    # 1. Classify
    classification = await service.classify_reply(data["subject"], data["body"])
    
    # 2. Store
    repo = InboxRepository(db)
    reply = repo.create({
        "lead_id": data["lead_id"],
        "tenant_id": UUID(tenant_id),
        "subject": data["subject"],
        "body": data["body"],
        "category": classification.get("category"),
        "reason": classification.get("reason"),
        "suggested_next_step": classification.get("suggested_next_step"),
        "status": "new"
    })
    
    # 3. [NEW] Trigger Learning if interested
    if reply.category == "INTERESTED":
        from app.tasks.learning_tasks import extract_patterns_task
        extract_patterns_task.delay(
            tenant_id=str(tenant_id),
            original_email=data.get("original_email", ""),
            positive_reply=data["body"]
        )
    
    return {"status": "processed", "reply_id": str(reply.id), "category": reply.category}

@router.get("/interested")
def get_interested_leads(request: Request, db: Session = Depends(get_db)):
    tenant_id = request.headers.get("X-Tenant-Id")
    if not tenant_id:
        raise HTTPException(status_code=400, detail="X-Tenant-Id header required")
        
    repo = InboxRepository(db)
    return repo.get_interested_leads(UUID(tenant_id))
