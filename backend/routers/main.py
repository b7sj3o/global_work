from fastapi import APIRouter
from . import home, vacancy, vacancy_request

api_router = APIRouter()

api_router.include_router(home.router)
api_router.include_router(vacancy.router)
api_router.include_router(vacancy_request.router)