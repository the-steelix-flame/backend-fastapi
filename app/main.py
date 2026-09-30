from fastapi import FastAPI, APIRouter
from app.routers import users

app = FastAPI()
router = APIRouter()
app.include_router(users.router)