from fastapi import APIRouter, Request
from app.services.dashboard_service import DashboardService

router = APIRouter()
service = DashboardService()

@router.get("/")
async def get_dashboard(request: Request):
    user_id = getattr(request.state, "user_id", "test_user")
    tenant_id = getattr(request.state, "tenant_id", "test_tenant")
    signature = request.headers.get("X-Request-Signature", "")
    
    return await service.get_dashboard_data(user_id, tenant_id, signature)
