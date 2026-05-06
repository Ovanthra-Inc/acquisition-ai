from sqlalchemy.orm import Session
from app.models.event import Event
from uuid import UUID

class EventRepository:
    def create(self, db: Session, user_id: UUID, data: dict):
        event = Event(user_id=user_id, **data)
        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    def get_events_by_type(self, db: Session, user_id: UUID, event_type: str):
        return db.query(Event).filter(Event.user_id == user_id, Event.type == event_type).all()
