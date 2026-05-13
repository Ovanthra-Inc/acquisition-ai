from app.models.event import Event
from acquisition_core.repository import BaseRepository
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

class EventRepository(BaseRepository[Event]):
    def __init__(self):
        super().__init__(Event)

    def create(self, db: Session, user_id: UUID, data: dict) -> Event:
        event = Event(
            user_id=user_id,
            type=data.get("type"),
            payload=data.get("payload", {})
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    def get_events_by_type(self, db: Session, user_id: UUID, event_type: str) -> List[Event]:
        return db.query(Event).filter(
            Event.user_id == user_id,
            Event.type == event_type
        ).all()
