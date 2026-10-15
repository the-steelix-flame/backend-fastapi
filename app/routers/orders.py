from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.services import order_service

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post(
    "/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_order(
    order: OrderCreate,
    db=Depends(get_db)
):
    try:
        return await order_service.create_order(db, order)

    except order_service.UserNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


