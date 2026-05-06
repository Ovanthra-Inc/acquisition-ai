from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.services.learning_service import LearningService
from pydantic import BaseModel
from typing import Optional

engine = create_engine(settings.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()
service = LearningService()

class MemoryStoreRequest(BaseModel):
    key: str
    value: dict
    score: float = 0.0

class StrategyPerformanceRequest(BaseModel):
    strategy_name: str
    reply_rate: float
    conversion_rate: float
    metadata: dict = {}

@router.post("/memory")
def store_memory(request: MemoryStoreRequest, db: Session = Depends(get_db)):
    mem = service.store_memory(db, request.key, request.value, request.score)
    return {"id": str(mem.id), "status": "stored"}

@router.get("/memory/{key}")
def get_memory(key: str, db: Session = Depends(get_db)):
    mem = service.get_memory(db, key)
    if not mem:
        return {"status": "not_found"}
    return {"key": mem.key, "value": mem.value, "score": mem.performance_score}

@router.post("/strategy")
def record_strategy(request: StrategyPerformanceRequest, db: Session = Depends(get_db)):
    perf = service.record_strategy_performance(db, request.strategy_name, request.reply_rate, request.conversion_rate, request.metadata)
    return {"id": str(perf.id), "status": "recorded"}

@router.get("/strategy/best")
def get_best_strategies(limit: int = 5, db: Session = Depends(get_db)):
    strats = service.get_best_strategies(db, limit)
    return {"strategies": [{"name": s.strategy_name, "reply_rate": s.reply_rate, "conversion_rate": s.conversion_rate} for s in strats]}
