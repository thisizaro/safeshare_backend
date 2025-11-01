# tests/test_auth_service.py
from app.service.auth_service import hash_password, verify_password, create_access_token
from jose import jwt

def test_hash_and_verify_password():
    password = "super_secret"
    hashed = hash_password(password)
    assert hashed != password
    assert verify_password(password, hashed)

def test_jwt_token_creation():
    token = create_access_token({"sub": "testuser", "role": "user"})
    decoded = jwt.get_unverified_claims(token)
    assert decoded["sub"] == "testuser"
    assert decoded["role"] == "user"
