# tests/test_db_connection.py
from app.repository.database import SessionLocal
from sqlalchemy import text

def test_database_connection():
    db = SessionLocal()
    result = db.execute(text("SELECT 1")).scalar()
    assert result == 1
    db.close()
