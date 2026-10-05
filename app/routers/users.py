from fastapi import APIRouter, HTTPException, Depends
from app.services import user_service
from app.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter(
            prefix="/users",
            tags=["users"]
            )

@router.get('/', response_model=list[UserResponse])
async def get_users(db = Depends(get_db)):
    users = await user_service.get_all_users(db)
    return users

@router.get("/{user_id}", response_model=UserResponse)
async def get_spec_user(user_id: int, db = Depends(get_db)):
    try:
        user = await user_service.get_spec_user(db, user_id)
        return user
    except user_service.UserNotFoundError:
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )

@router.post('/', status_code=201, response_model=UserResponse)
async def create_spec_user(user:UserCreate, db = Depends(get_db)):
    try:
        return await user_service.create_user(db, user)

    except user_service.UserAlreadyExistsError:
        raise HTTPException(
            status_code=409,
        detail="User with this email already exists"
    )


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user: UserUpdate,
    db=Depends(get_db)
):
    try:
        return await user_service.update_user(db, user_id, user)

    except user_service.UserNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    except user_service.UserAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail="User with this email already exists"
        )

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int, db=Depends(get_db)):
    try:
        await user_service.delete_user(db, user_id)
    except user_service.UserNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )