from sqlalchemy import Column, Integer, ForeignKey
from app.repository.database import Base

class FileShare(Base):
    __tablename__ = "file_shares"

    file_id = Column(Integer, ForeignKey("files.id"), primary_key=True)
    shared_with_user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
