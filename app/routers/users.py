from starlette._utils import get_route_path
from fastapi import APIRouter, HTTPException, Depends, status

router = APIRouter(
            prefix="/users",
            tags=["users"]
            )

@router.get('/')
async def get_users():
    return {"message": "Users route working"}

@router.get("/{user_id}")
async def getspecuser(user_id: int):
    return {
        "user_id": user_id
    }
