from fastapi import APIRouter, Response, status, HTTPException
from ..schemas import AdminCredentials
from ..config import ADMIN_USERNAME, ADMIN_PASSWORD


router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/login")
def login(data: AdminCredentials):
    if data.username == ADMIN_USERNAME and data.password == ADMIN_PASSWORD:
        return {"status": "success", "message": "Ви успішно увійшли в акаунт!"}
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Логін чи пароль хибні")
