from sqlalchemy.orm import Session
from app.models.learning import LearningMemory, StrategyPerformance
from uuid import UUID

class LearningService:
    def store_memory(self, db: Session, key: str, value: dict, score: float = 0.0):
        memory = LearningMemory(key=key, value=value, performance_score=score)
        db.add(memory)
        db.commit()
        db.refresh(memory)
        return memory

    def get_memory(self, db: Session, key: str):
        return db.query(LearningMemory).filter(LearningMemory.key == key).order_by(LearningMemory.created_at.desc()).first()

    def record_strategy_performance(self, db: Session, strategy_name: str, reply_rate: float, conversion_rate: float, metadata: dict):
        perf = StrategyPerformance(
            strategy_name=strategy_name,
            reply_rate=reply_rate,
            conversion_rate=conversion_rate,
            metadata_json=metadata
        )
        db.add(perf)
        db.commit()
        db.refresh(perf)
        return perf

    def get_best_strategies(self, db: Session, limit: int = 5):
        return db.query(StrategyPerformance).order_by(StrategyPerformance.conversion_rate.desc(), StrategyPerformance.reply_rate.desc()).limit(limit).all()
