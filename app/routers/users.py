from fastapi import APIRouter, HTTPException, status
from app.services import user_service

router = APIRouter(
            prefix="/users",
            tags=["users"]
            )

@router.get('/')
async def get_users():
    users = await user_service.get_all_users()
    return users

@router.get("/{user_id}")
async def get_spec_user(user_id: int):
    try:
        return await user_service.get_spec_user(user_id)
    except user_service.UserNotFoundError:
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )
