from fastapi import APIRouter
from app.api import users, blood_requests, health

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(users.router)
api_router.include_router(blood_requests.router)
