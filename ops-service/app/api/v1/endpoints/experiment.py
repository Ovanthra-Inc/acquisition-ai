from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.services.experiment_service import ExperimentService
from pydantic import BaseModel
from uuid import UUID

engine = create_engine(settings.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()
service = ExperimentService()

class ExperimentCreate(BaseModel):
    campaign_id: str
    experiment_type: str

class VariantCreate(BaseModel):
    experiment_id: str
    variant_name: str
    configuration: dict

@router.post("/")
def create_experiment(request: Request, data: ExperimentCreate, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    campaign_id = UUID(data.campaign_id)
    exp = service.create_experiment(db, user_id, campaign_id, data.experiment_type)
    return {"id": str(exp.id), "status": "created"}

@router.post("/variants")
def add_variant(data: VariantCreate, db: Session = Depends(get_db)):
    exp_id = UUID(data.experiment_id)
    var = service.add_variant(db, exp_id, data.variant_name, data.configuration)
    return {"id": str(var.id), "status": "added"}

@router.get("/{experiment_id}")
def get_experiment(experiment_id: str, db: Session = Depends(get_db)):
    exp_id = UUID(experiment_id)
    exp = service.get_experiment(db, exp_id)
    if not exp:
        return {"status": "not_found"}
    
    variants = service.get_variants(db, exp_id)
    return {
        "id": str(exp.id),
        "type": exp.experiment_type,
        "status": exp.status,
        "variants": [{"id": str(v.id), "name": v.variant_name} for v in variants]
    }

@router.post("/{experiment_id}/conclude")
def conclude_experiment(experiment_id: str, db: Session = Depends(get_db)):
    exp_id = UUID(experiment_id)
    exp = service.conclude_experiment(db, exp_id)
    return {"id": str(exp.id), "status": exp.status if exp else "not_found"}
