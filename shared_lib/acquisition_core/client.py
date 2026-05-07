import httpx
from typing import Optional
from .middleware.internal_auth import generate_internal_signature

def get_internal_client(
    internal_token: str, 
    user_id: Optional[str] = "", 
    tenant_id: Optional[str] = "", 
    service_name: str = "agent-service"
) -> httpx.AsyncClient:
    """
    Returns an httpx.AsyncClient pre-configured with the required zero-trust
    internal headers so that it can pass through the InternalAuthMiddleware
    of downstream services.
    """
    signature = generate_internal_signature(internal_token, str(user_id or ""), str(tenant_id or ""), service_name)
    headers = {
        "Authorization": f"Bearer {internal_token}",
        "X-User-Id": str(user_id or ""),
        "X-Tenant-Id": str(tenant_id or ""),
        "X-Service-Name": service_name,
        "X-Request-Signature": signature
    }
    return httpx.AsyncClient(headers=headers, timeout=30.0)

def get_sync_internal_client(
    internal_token: str, 
    user_id: Optional[str] = "", 
    tenant_id: Optional[str] = "", 
    service_name: str = "worker"
) -> httpx.Client:
    """
    Returns a synchronous httpx.Client pre-configured with the required zero-trust
    internal headers. Use this in Celery workers or sync service layers.
    """
    signature = generate_internal_signature(internal_token, str(user_id or ""), str(tenant_id or ""), service_name)
    headers = {
        "Authorization": f"Bearer {internal_token}",
        "X-User-Id": str(user_id or ""),
        "X-Tenant-Id": str(tenant_id or ""),
        "X-Service-Name": service_name,
        "X-Request-Signature": signature
    }
    return httpx.Client(headers=headers, timeout=30.0)
