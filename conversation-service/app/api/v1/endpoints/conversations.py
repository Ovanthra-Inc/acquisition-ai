from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.session import get_db
from app.schemas.conversation import ConversationCreate, ConversationResponse
from app.schemas.message import MessageCreate, MessageResponse, ClassifyRequest
from app.services.conversation_service import ConversationService

router = APIRouter()
service = ConversationService()

@router.get("/", response_model=list[ConversationResponse])
def get_conversations(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.get_conversations(db, user_id)

@router.get("/{id}", response_model=ConversationResponse)
def get_conversation(request: Request, id: UUID, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    conv = service.get_conversation(db, user_id, id)
    if not conv:
        raise HTTPException(status_code=404, detail="Not found")
    return conv

@router.post("/", response_model=ConversationResponse)
def create_conversation(request: Request, data: ConversationCreate, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.create_conversation(db, user_id, data.dict())

@router.post("/reply", response_model=MessageResponse)
def post_reply(request: Request, data: MessageCreate, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    try:
        return service.handle_reply(db, user_id, data.dict())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/classify")
def classify_message(data: ClassifyRequest):
    return {"classification": service.classify(data.message_text)}
