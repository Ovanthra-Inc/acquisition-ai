from acquisition_core.client import get_internal_client
from app.core.config import settings
import httpx

def get_internal_headers(state: dict):
    # Keep for backwards compatibility if needed
    user_id = state.get("user_id", "")
    tenant_id = state.get("tenant_id", "")
    from acquisition_core.middleware.internal_auth import generate_internal_signature
    return {
        "Authorization": f"Bearer {settings.INTERNAL_SERVICE_TOKEN}",
        "X-User-Id": user_id,
        "X-Tenant-Id": tenant_id,
        "X-Service-Name": "agent-service",
        "X-Request-Signature": generate_internal_signature(settings.INTERNAL_SERVICE_TOKEN, user_id, tenant_id, "agent-service")
    }

def get_agent_client(state: dict) -> httpx.AsyncClient:
    user_id = state.get("user_id", "")
    tenant_id = state.get("tenant_id", "")
    return get_internal_client(settings.INTERNAL_SERVICE_TOKEN, user_id, tenant_id, "agent-service")
