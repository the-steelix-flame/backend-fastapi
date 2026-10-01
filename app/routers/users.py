from fastapi import APIRouter, HTTPException, Depends
from app.services import user_service
from app.dependencies import get_db

router = APIRouter(
            prefix="/users",
            tags=["users"]
            )

@router.get('/')
async def get_users(db = Depends(get_db)):
    users = await user_service.get_all_users(db)
    return users

@router.get("/{user_id}")
async def get_spec_user(user_id: int, db = Depends(get_db)):
    try:
        user = await user_service.get_spec_user(db, user_id)
        return user
    except user_service.UserNotFoundError:
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )
