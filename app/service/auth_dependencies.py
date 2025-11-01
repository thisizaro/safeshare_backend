from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.service.auth_service import jwt
from app.config.settings import SECRET_KEY, ALGORITHM

from app.repository.database import get_db
from app.model.user import User


# This tells FastAPI to look for a token in "Authorization: Bearer ..."
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    from jose import JWTError, jwt
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        role = payload.get("role")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        
        # ✅ Fetch actual user from DB
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        return user   # Return full SQLAlchemy User object

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
