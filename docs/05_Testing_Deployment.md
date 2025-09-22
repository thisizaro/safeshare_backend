# Testing & Deployment Document

## Test Strategy
- **Unit tests:** auth, file upload, sharing.  
- **Integration tests:** DB + API + storage.  
- **Manual tests:** API calls via Postman.

## Test Cases
- Register → login → upload → download.  
- Unauthorized user cannot access others’ files.  
- Admin can view all logs.

## Bug Tracking Method
- GitHub Issues + labels (bug, feature, enhancement).

## Deployment Plan
- Dockerize FastAPI + PostgreSQL + MinIO.  
- Deploy on Render/Fly.io (public demo).  
- Use `.env` for secrets.

## Maintenance Notes
- Future improvements: OAuth2/SSO, 2FA, file encryption at rest, scalable storage.

