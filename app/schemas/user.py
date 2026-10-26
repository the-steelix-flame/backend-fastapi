from pydantic import BaseModel, ConfigDict

class UserRegister(BaseModel):
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    id:int
    name:str
    email:str

    model_config= ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    name: str
    email: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str