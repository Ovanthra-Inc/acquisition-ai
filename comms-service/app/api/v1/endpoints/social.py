from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
from app.repository.message_repo import MessageRepository

router = APIRouter()

class SocialMessage(BaseModel):
    platform: str # 'linkedin' or 'slack'
    target_id: str
    content: str
    metadata: Optional[dict] = {}

@router.post("/send")
async def send_social_message(data: SocialMessage, repo: MessageRepository = Depends()):
    """Sends a message to a social platform and logs it."""
    # In a real app, integrate with LinkedIn/Slack APIs here.
    print(f"[Social] Sending {data.platform} message to {data.target_id}: {data.content}")
    
    # Log the outgoing message
    logged_msg = repo.create({
        "channel": data.platform,
        "recipient": data.target_id,
        "content": data.content,
        "direction": "outbound",
        "metadata": data.metadata
    })
    
    return {"status": "sent", "message_id": logged_msg.get("id"), "platform": data.platform}

@router.post("/linkedin/connect")
async def linkedin_connect(target_id: str, note: Optional[str] = None, repo: MessageRepository = Depends()):
    """Sends a LinkedIn connection request and logs the intent."""
    print(f"[Social] LinkedIn Connection request to {target_id} with note: {note}")
    
    repo.create({
        "channel": "linkedin",
        "recipient": target_id,
        "content": note or "Connection Request",
        "direction": "outbound",
        "metadata": {"type": "connection_request"}
    })
    
    return {"status": "request_sent"}
