import hmac
import hashlib
from app.core.config import settings

def generate_signature(user_id: str, tenant_id: str, service_name: str = "agent-service"):
    data = f"{user_id}:{tenant_id}:{service_name}"
    return hmac.new(
        settings.INTERNAL_SERVICE_TOKEN.encode(),
        data.encode(),
        hashlib.sha256
    ).hexdigest()

def get_internal_headers(state: dict):
    user_id = state.get("user_id", "")
    tenant_id = state.get("tenant_id", "")
    return {
        "Authorization": f"Bearer {settings.INTERNAL_SERVICE_TOKEN}",
        "X-User-Id": user_id,
        "X-Tenant-Id": tenant_id,
        "X-Service-Name": "agent-service",
        "X-Request-Signature": generate_signature(user_id, tenant_id)
    }
