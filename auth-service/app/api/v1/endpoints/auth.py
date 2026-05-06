from fastapi import APIRouter, Depends, Request
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from app.schemas.auth import TokenResponse
from app.services.auth_service import AuthService
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.core.config import settings

router = APIRouter()
oauth = OAuth()

oauth.register(
    name='google',
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

auth_service = AuthService()

@router.get("/login/google")
async def login_google(request: Request):
    # This will redirect to google
    redirect_uri = settings.GOOGLE_CALLBACK_URL
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/callback/google", response_model=TokenResponse)
async def auth_google(request: Request, db: Session = Depends(get_db)):
    try:
        token = await oauth.google.authorize_access_token(request)
        userinfo = token.get('userinfo')
        if not userinfo or 'email' not in userinfo:
            from fastapi import HTTPException
            raise HTTPException(status_code=400, detail="Could not fetch user info")
        
        email = userinfo['email']
        return auth_service.process_google_login(db, email)
    except Exception as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=f"OAuth error: {str(e)}")

@router.get("/me")
def get_me(request: Request):
    # This is an internal protected route. It relies on the API Gateway injecting user context.
    user_id = getattr(request.state, "user_id", None)
    return {"message": "Protected info", "user_id": user_id}
