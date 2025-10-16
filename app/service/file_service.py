# app/service/file_service.py
import uuid
import re
from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.s3_client import S3ClientWrapper
from app.repository.file_repo import create_file, get_file_by_id, list_files_by_owner, is_shared_with
from app.config.settings import (
    S3_ENDPOINT_URL,
    S3_ACCESS_KEY,
    S3_SECRET_KEY,
    S3_REGION,
    S3_USE_SSL,
    S3_BUCKET,
    STORAGE_PROVIDER,
)
from app.model.user import User

# Helper: sanitize filename
_filename_re = re.compile(r"[^A-Za-z0-9_.-]+")

def _sanitize_filename(name: str) -> str:
    return _filename_re.sub("_", name)

def _generate_storage_key(user_id: int, original_filename: str) -> str:
    safe = _sanitize_filename(original_filename)
    uid = uuid.uuid4().hex
    return f"{user_id}/{uid}_{safe}"

def _get_s3_client() -> S3ClientWrapper:
    if STORAGE_PROVIDER == "minio":
        return S3ClientWrapper(
            access_key=S3_ACCESS_KEY,
            secret_key=S3_SECRET_KEY,
            endpoint_url=S3_ENDPOINT_URL,
            region_name=S3_REGION,
            use_ssl=S3_USE_SSL,
            bucket=S3_BUCKET,
        )
    else:
        # AWS default (endpoint_url None)
        return S3ClientWrapper(
            access_key=None,
            secret_key=None,
            endpoint_url=None,
            region_name=S3_REGION,
            use_ssl=True,
            bucket=S3_BUCKET,
        )

def upload_file(db: Session, upload_file: UploadFile, current_user: User):
    """
    Uploads the given UploadFile to storage, persists metadata, returns DB model.
    """
    # Validate simple sanity: filename present
    original_name = upload_file.filename or "file"
    if not original_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid filename")

    key = _generate_storage_key(current_user.id, original_name)
    s3 = _get_s3_client()

    # Ensure bucket exists (helpful for MinIO dev)
    try:
        s3.ensure_bucket_exists()
    except Exception:
        # ignore error creating bucket; we'll try upload and raise if it fails
        pass

    # Seek to start (safe)
    try:
        upload_file.file.seek(0)
    except Exception:
        pass

    # Upload (this is blocking; okay for hobby project)
    try:
        s3.upload_fileobj(upload_file.file, key, content_type=upload_file.content_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Storage upload failed: {e}")

    # Save metadata in DB
    file_record = create_file(db, current_user.id, original_name, key)
    return file_record

def get_file_for_download(db: Session, file_id: int, current_user: User):
    file_rec = get_file_by_id(db, file_id)
    if not file_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

    # Access control: owner OR shared with user
    if file_rec.owner_id != current_user.id:
        shared = is_shared_with(db, file_id, current_user.id)
        if not shared:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this file")

    s3 = _get_s3_client()
    try:
        stream_body, content_type = s3.download_stream(file_rec.storage_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch file from storage: {e}")

    return file_rec, stream_body, content_type

def list_my_files(db: Session, current_user: User):
    return list_files_by_owner(db, current_user.id)
