# safeshare_backend/app/model/schemas.py

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class FileOut(BaseModel):
    id: int
    filename: str
    owner_id: int

    class Config:
        orm_mode = True
