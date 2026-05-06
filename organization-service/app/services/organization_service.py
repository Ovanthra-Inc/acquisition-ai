from sqlalchemy.orm import Session
from app.models.organization import Organization, OrganizationMember
from uuid import UUID

class OrganizationService:
    def create_organization(self, db: Session, name: str, plan: str = "starter"):
        org = Organization(name=name, plan=plan)
        db.add(org)
        db.commit()
        db.refresh(org)
        return org

    def add_member(self, db: Session, org_id: UUID, user_id: UUID, role: str):
        member = OrganizationMember(
            organization_id=org_id,
            user_id=user_id,
            role=role
        )
        db.add(member)
        db.commit()
        db.refresh(member)
        return member

    def get_organization(self, db: Session, org_id: UUID):
        return db.query(Organization).filter(Organization.id == org_id).first()

    def get_user_organizations(self, db: Session, user_id: UUID):
        memberships = db.query(OrganizationMember).filter(OrganizationMember.user_id == user_id).all()
        org_ids = [m.organization_id for m in memberships]
        return db.query(Organization).filter(Organization.id.in_(org_ids)).all()
