
# 🧠 CORE RULE (NON-NEGOTIABLE)

👉 **ONLY external clients use the API Gateway**
👉 **Internal services DO NOT go through API Gateway**

---

# 🧩 1. WHO USES API GATEWAY?

## ✅ Uses API Gateway:

* Frontend (Next.js)
* Mobile apps (future)
* External integrations (public APIs)

---

## ❌ Does NOT use API Gateway:

* Lead Service → AI Service
* Agent Service → Campaign Service
* Campaign Service → Email Service

👉 These use **internal service-to-service communication**

---

# 🌐 2. HIGH-LEVEL FLOW

## External Request

```text
Client → NGINX → API Gateway → BFF → Services
```

---

## Internal Communication

```text
Agent Service → Lead Service → AI Service → Campaign Service → Email Service
```

👉 NO gateway here

---

# ⚠️ WHY NOT USE GATEWAY INTERNALLY?

If you do:

* Adds latency ❌
* Creates bottleneck ❌
* Breaks scalability ❌
* Complicates auth ❌

---

# 🧠 3. HOW SERVICES TALK TO EACH OTHER


---

## 🔹 REST

Example:

```python
# Agent → Lead Service
POST http://lead-service:8000/internal/leads/search
```

---


# 🔐 4. INTERNAL SECURITY (VERY IMPORTANT)

Even without gateway, services must be secured.

---

## Use:

### 🔑 Internal Service Token

Every request includes:

(Optimized Internal Header)

Gateway validates JWT → then forwards:

X-User-Id: 123
X-Tenant-Id: abc
X-Roles: admin
X-Request-Signature: <HMAC signature>

👉 Services:

Trust only if signature is valid
---

---

# 🌐 5. API GATEWAY RESPONSIBILITIES (FINAL)

---

## 🔐 Security

* JWT validation
* API keys
* Rate limiting

---

## 🔄 Routing

```text
/api/v1/leads → lead-service  
/api/v1/campaigns → campaign-service  
/api/v1/agent → agent-service  
```

---

## ⚡ Control

* Request validation
* Throttling per tier

---

## ❌ NOT RESPONSIBLE FOR

* Business logic
* DB access
* Internal orchestration

---

# 🧩 6. BFF ROLE (IMPORTANT)

👉 Gateway routes → BFF → Services

---

## Why BFF?

Instead of frontend calling 5 services:

Frontend → BFF → aggregates:

* leads
* campaigns
* analytics

---

---

# 🔄 7. COMPLETE FLOW EXAMPLE

---

## User clicks “Run Recipe”

---

### Step 1: External

```text
Frontend → API Gateway → BFF → Agent Service
```

---

### Step 2: Internal

```text
Agent Service:
   → Lead Service (search)
   → Enrichment Service
   → AI Service (email)
   → Campaign Service
   → Email Service
```

---

### Step 3: Async

```text
Queue → Email sending → Follow-ups
```

---

---

# 🧠 8. URL DESIGN (IMPORTANT)

---

## External APIs (via Gateway)

```text
/api/v1/leads
/api/v1/campaigns
/api/v1/agent/run
```

---

## Internal APIs (service-to-service)

```text
/internal/leads/search
/internal/ai/generate
/internal/email/send
```

---

👉 Separate namespaces = clean design

---

---

# 🔐 9. RATE LIMITING FLOW

---

## Gateway Level:

* Per user
* Per plan

---

## Service Level:

* Critical endpoints (email send, AI calls)

---
SERVICE AUTH (Who is calling?)

Even with user identity, you must verify:

👉 “Which service is making this call?”

Use:
Authorization: Bearer INTERNAL_SERVICE_TOKEN

OR

X-Service-Name: agent-service
X-Service-Signature: <HMAC>
---

# ⚠️ COMMON MISTAKES (DON’T DO THIS)

---

## ❌ Calling gateway from services

* Wrong architecture

---

## ❌ No internal auth

* Security risk

---

## ❌ Mixing external + internal APIs

* Messy system

---

---

# 🧠 FINAL MENTAL MODEL

---

### Gateway = Guard + Traffic Controller

### BFF = Translator

### Services = Workers

### Agents = Brain

---

---



# 🚀 STEP 1 — API GATEWAY (FOUNDATION)

Before anything else, you must build:

👉 **API Gateway (Guard + Router + Rate Limiter)**

This enforces:

* JWT validation
* Rate limiting
* Routing to services
* Injecting internal headers

---

# 🧠 1. RESPONSIBILITY (RECAP)

Gateway must:

* Validate JWT
* Extract user context
* Enforce rate limits
* Route request
* Inject:

  * `X-User-Id`
  * `X-Tenant-Id`
  * `X-Roles`
  * `X-Request-Signature`
  * `Authorization: INTERNAL_TOKEN`

---

# 🧩 2. ARCHITECTURE

```text
Client → NGINX → API Gateway → BFF → Services
```

We’ll implement **API Gateway (FastAPI)**.

---

# 📁 3. FOLDER STRUCTURE (API GATEWAY)

```text
api-gateway/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── rate_limiter.py
│   │
│   ├── middleware/
│   │   ├── auth_middleware.py
│   │   ├── rate_limit_middleware.py
│   │   ├── context_middleware.py
│   │
│   ├── routes/
│   │   └── proxy.py
│   │
│   ├── services/
│   │   └── router_service.py
│   │
│   └── utils/
│       └── signature.py
│
├── requirements.txt
└── Dockerfile
```

---

# ⚙️ 4. CONFIG

## `core/config.py`

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    JWT_SECRET: str = "supersecret"
    INTERNAL_SERVICE_TOKEN: str = "internal-secret"
    REDIS_URL: str = "redis://localhost:6379"

settings = Settings()
```

---

# 🔐 5. JWT VALIDATION

## `core/security.py`

```python
import jwt
from fastapi import HTTPException
from app.core.config import settings

def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
```

---

# ⚡ 6. RATE LIMITING (REDIS)

## `core/rate_limiter.py`

```python
import redis
from fastapi import HTTPException

r = redis.Redis(host="localhost", port=6379, db=0)

def check_rate_limit(user_id: str, limit: int = 100):
    key = f"rate:{user_id}"
    count = r.get(key)

    if count and int(count) >= limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    r.incr(key)
    r.expire(key, 60)
```

---

# 🔐 7. SIGNATURE GENERATION

## `utils/signature.py`

```python
import hmac
import hashlib
from app.core.config import settings

def generate_signature(data: str):
    return hmac.new(
        settings.INTERNAL_SERVICE_TOKEN.encode(),
        data.encode(),
        hashlib.sha256
    ).hexdigest()
```

---

# 🧠 8. AUTH MIDDLEWARE

## `middleware/auth_middleware.py`

```python
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from app.core.security import verify_jwt

class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return await call_next(request)

        token = auth_header.split(" ")[1]
        payload = verify_jwt(token)

        request.state.user = payload

        return await call_next(request)
```

---

# ⚡ 9. RATE LIMIT MIDDLEWARE

## `middleware/rate_limit_middleware.py`

```python
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from app.core.rate_limiter import check_rate_limit

class RateLimitMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        user = getattr(request.state, "user", None)

        if user:
            check_rate_limit(user["user_id"])

        return await call_next(request)
```

---

# 🔄 10. PROXY ROUTER

## `routes/proxy.py`

```python
from fastapi import APIRouter, Request
import httpx
from app.utils.signature import generate_signature
from app.core.config import settings

router = APIRouter()

SERVICE_MAP = {
    "/api/v1/leads": "http://lead-service:8000",
    "/api/v1/campaigns": "http://campaign-service:8000",
    "/api/v1/agent": "http://agent-service:8000",
}

@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(request: Request, path: str):

    url_path = f"/{path}"

    for route, service_url in SERVICE_MAP.items():
        if url_path.startswith(route):
            target_url = service_url + url_path.replace("/api/v1", "")
            break
    else:
        return {"error": "Route not found"}

    user = getattr(request.state, "user", {})

    headers = dict(request.headers)

    # Inject internal headers
    headers.update({
        "X-User-Id": str(user.get("user_id", "")),
        "X-Tenant-Id": str(user.get("tenant_id", "")),
        "Authorization": f"Bearer {settings.INTERNAL_SERVICE_TOKEN}",
        "X-Request-Signature": generate_signature(str(user)),
    })

    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            target_url,
            headers=headers,
            content=await request.body()
        )

    return response.json()
```

---

# 🚀 11. MAIN APP

## `main.py`

```python
from fastapi import FastAPI
from app.middleware.auth_middleware import AuthMiddleware
from app.middleware.rate_limit_middleware import RateLimitMiddleware
from app.routes.proxy import router

app = FastAPI(title="API Gateway")

app.add_middleware(AuthMiddleware)
app.add_middleware(RateLimitMiddleware)

app.include_router(router)
```

---

# 🔥 12. WHAT YOU JUST BUILT

You now have:

✅ JWT validation
✅ Rate limiting
✅ Service routing
✅ Internal header injection
✅ Service authentication base
✅ Signature system

---

# ⚠️ NEXT STEP (DO NOT SKIP)

Now you must:

👉 Build **internal service middleware** that:

* Validates `INTERNAL_SERVICE_TOKEN`
* Verifies `X-Request-Signature`
* Extracts user context


so one by one start implementing 

