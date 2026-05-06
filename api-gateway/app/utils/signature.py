import hmac
import hashlib
from app.core.config import settings

def generate_signature(user_id: str, tenant_id: str, service_name: str = ""):
    data = f"{user_id}:{tenant_id}:{service_name}"
    return hmac.new(
        settings.INTERNAL_SERVICE_TOKEN.encode(),
        data.encode(),
        hashlib.sha256
    ).hexdigest()
