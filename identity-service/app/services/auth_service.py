import jwt
from datetime import datetime, timedelta
from app.core.config import settings
from app.repository.user_repo import UserRepository
from sqlalchemy.orm import Session

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def generate_jwt(self, user_id: str, tenant_id: str, role: str = "member", tier: str = "free"):
        payload = {
            "user_id": str(user_id),
            "tenant_id": str(tenant_id),
            "role": role,
            "tier": tier,
            "iss": "ovanthra-auth",
            "aud": "ovanthra-api",
            "exp": datetime.utcnow() + timedelta(days=7)
        }
        return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    def process_google_login(self, db: Session, email: str):
        user = self.user_repo.get_by_email(db, email)
        if not user:
            user = self.user_repo.create(db, email)
        
        # In a standard approach, we'd fetch the user's active organization and role here
        tenant_id = "default_tenant" 
        role = "admin" # Default for first user or testing
        tier = "pro"   # Default for testing
        
        token = self.generate_jwt(user.id, tenant_id, role, tier)
        return {"access_token": token, "token_type": "bearer"}
