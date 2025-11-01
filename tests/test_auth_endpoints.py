# tests/test_auth_endpoints.py
def test_register_and_login(client):
    # Register user
    register_resp = client.post("/auth/register", json={"username": "pytest_user", "password": "pytest_pass"})
    assert register_resp.status_code in [200, 400]  # 400 if user already exists

    # Login
    login_resp = client.post("/auth/login", json={"username": "pytest_user", "password": "pytest_pass"})
    assert login_resp.status_code == 200

    data = login_resp.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
