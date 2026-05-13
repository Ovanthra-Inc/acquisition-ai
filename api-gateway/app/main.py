from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.auth_middleware import AuthMiddleware
from app.middleware.rate_limit_middleware import RateLimitMiddleware
from app.routes.proxy import router as proxy_router
from app.api.v1.endpoints import dashboard
from app.core.config import settings
from app.core.ws_manager import manager
import json

app = FastAPI(title=settings.PROJECT_NAME)

# CORS: When using credentials, origins MUST be explicit (never "*")
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["Authorization", "Content-Type"],
)

app.add_middleware(AuthMiddleware)
app.add_middleware(RateLimitMiddleware)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(websocket, user_id)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket, user_id)

@app.post("/api/v1/internal/notify/{user_id}")
async def internal_notify(user_id: str, request: Request):
    data = await request.json()
    await manager.send_personal_message(json.dumps(data), user_id)
    return {"status": "sent"}

app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["BFF"])
app.include_router(proxy_router)
