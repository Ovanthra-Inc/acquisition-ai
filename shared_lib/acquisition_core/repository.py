from typing import TypeVar, Generic, Type, Optional, List, Any
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from uuid import UUID

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100, tenant_id: Optional[str] = None
    ) -> List[ModelType]:
        query = db.query(self.model)
        if tenant_id and hasattr(self.model, "tenant_id"):
            query = query.filter(self.model.tenant_id == tenant_id)
        return query.offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: dict, tenant_id: Optional[str] = None) -> ModelType:
        if tenant_id and hasattr(self.model, "tenant_id"):
            obj_in["tenant_id"] = tenant_id
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: ModelType, obj_in: dict
    ) -> ModelType:
        for field in obj_in:
            if hasattr(db_obj, field):
                setattr(db_obj, field, obj_in[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: Any) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
