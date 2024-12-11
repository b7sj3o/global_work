from fastapi import APIRouter
from ..db import Session
from ..db.models import Vacancy
from ..schemas.vacancy import VacandyData

router = APIRouter(prefix="", tags=["base"])

@router.get("/")
def home():
    return {"HELLO": "WORLD"}