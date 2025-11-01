# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    """
    Fixture that provides a FastAPI TestClient.
    Used for integration tests on API routes.
    """
    with TestClient(app) as c:
        yield c
