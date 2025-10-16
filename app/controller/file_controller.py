# app/controller/file_controller.py
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.service.auth_dependencies import get_current_user
from app.repository.database import get_db
from app.service.file_service import upload_file, list_my_files, get_file_for_download
from app.model.schemas import FileOut
from app.model.user import User

router = APIRouter(prefix="/files", tags=["files"])

@router.post("/upload", response_model=FileOut, status_code=status.HTTP_201_CREATED)
def upload_endpoint(
    upload_file_payload: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Uploads file. Form field name: 'upload_file_payload'
    """
    file_rec = upload_file(db, upload_file_payload, current_user)
    return file_rec

@router.get("/my", response_model=list[FileOut])
def list_my_files_endpoint(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    files = list_my_files(db, current_user)
    return files

@router.get("/{file_id}")
def download_file_endpoint(file_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Stream the file to the client after authorization check.
    """
    file_rec, stream_body, content_type = get_file_for_download(db, file_id, current_user)

    # StreamingBody supports read() and iter_chunks.
    headers = {
        "Content-Disposition": f'attachment; filename="{file_rec.filename}"'
    }
    return StreamingResponse(stream_body, media_type=content_type or "application/octet-stream", headers=headers)
