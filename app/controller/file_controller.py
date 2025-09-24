from fastapi import APIRouter, Depends
from app.service.auth_dependencies import get_current_user

router = APIRouter(prefix="/files", tags=["files"])

@router.get("/")
def list_files(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}, these are your files"}
