import jwt
from fastapi import HTTPException
from app.core.config import settings

def verify_jwt(token: str):
    try:
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET, 
            algorithms=["HS256"],
            issuer="ovanthra-auth",
            audience="ovanthra-api"
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidIssuerError:
        raise HTTPException(status_code=401, detail="Invalid token issuer")
    except jwt.InvalidAudienceError:
        raise HTTPException(status_code=401, detail="Invalid token audience")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

