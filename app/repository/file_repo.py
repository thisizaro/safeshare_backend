# app/repository/file_repo.py
from sqlalchemy.orm import Session
from app.model.file import File
from typing import List, Optional

def create_file(db: Session, owner_id: int, filename: str, storage_path: str) -> File:
    file = File(owner_id=owner_id, filename=filename, storage_path=storage_path)
    db.add(file)
    db.commit()
    db.refresh(file)
    return file

def get_file_by_id(db: Session, file_id: int) -> Optional[File]:
    return db.query(File).filter(File.id == file_id).first()

def list_files_by_owner(db: Session, owner_id: int) -> List[File]:
    return db.query(File).filter(File.owner_id == owner_id).order_by(File.id.desc()).all()

def is_shared_with(db: Session, file_id: int, user_id: int) -> bool:
    # Check file_shares table if it exists
    from app.model.file_shares import FileShare
    row = db.query(FileShare).filter(
        FileShare.file_id == file_id,
        FileShare.shared_with_user_id == user_id
    ).first()
    return row is not None
