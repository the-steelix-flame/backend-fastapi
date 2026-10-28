from app.database import SessionLocal
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

from app.core.security import SECRET_KEY, ALGORITHM
from app.repositories import user_repository


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

bearer_scheme = HTTPBearer(auto_error=False)

def get_current_user(credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme), db = Depends(get_db)):
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Missing token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    try:
        token = credentials.credentials
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        try:
            user_id = int(payload.get("sub"))
        except (TypeError, ValueError):
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"}
            )

        user = user_repository.get_user(db, user_id)
        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return user

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}
        )
