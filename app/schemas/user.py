from pydantic import BaseModel, ConfigDict

class createuser(BaseModel):
    name:str
    email:str

    model_config= ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    id:int
    name:str
    email:str

    model_config= ConfigDict(from_attributes=True)