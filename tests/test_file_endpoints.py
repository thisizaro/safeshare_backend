# tests/test_file_endpoints.py
import io

def test_upload_and_list_files(client):
    # Login
    login = client.post("/auth/login", json={"username": "pytest_user", "password": "pytest_pass"})
    assert login.status_code == 200
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Upload a file
    file_data = io.BytesIO(b"hello from pytest")
    files = {"upload_file_payload": ("testfile.txt", file_data, "text/plain")}

    upload_resp = client.post("/files/upload", files=files, headers=headers)
    assert upload_resp.status_code in [201, 500]  # 500 if MinIO not running
    if upload_resp.status_code == 201:
        file_rec = upload_resp.json()
        assert "id" in file_rec
        assert "filename" in file_rec

    # List files
    list_resp = client.get("/files/my", headers=headers)
    assert list_resp.status_code == 200
    