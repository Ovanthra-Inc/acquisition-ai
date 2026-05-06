from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.services.organization_service import OrganizationService
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
service = OrganizationService()

class OrganizationCreate(BaseModel):
    name: str
    plan: str = "starter"

class MemberAdd(BaseModel):
    user_id: str
    role: str = "viewer"

@router.post("/")
def create_organization(request: Request, data: OrganizationCreate, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    org = service.create_organization(db, data.name, data.plan)
    service.add_member(db, org.id, user_id, "owner") # the creator is the owner
    return {"id": str(org.id), "status": "created"}

@router.get("/")
def get_user_organizations(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    orgs = service.get_user_organizations(db, user_id)
    return {"organizations": [{"id": str(o.id), "name": o.name, "plan": o.plan} for o in orgs]}

@router.post("/{org_id}/members")
def add_organization_member(org_id: str, data: MemberAdd, db: Session = Depends(get_db)):
    o_id = UUID(org_id)
    u_id = UUID(data.user_id)
    member = service.add_member(db, o_id, u_id, data.role)
    return {"id": str(member.id), "status": "added"}
