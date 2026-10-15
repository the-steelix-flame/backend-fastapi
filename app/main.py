from fastapi import FastAPI
from app.routers import users, orders

app = FastAPI()
app.include_router(users.router)
app.include_router(orders.router)