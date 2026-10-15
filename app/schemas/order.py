from pydantic import BaseModel,ConfigDict

class OrderCreate(BaseModel):
    product: str
    amount: int
    user_id: int

class OrderResponse(BaseModel):
    id: int
    product: str
    amount: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
    