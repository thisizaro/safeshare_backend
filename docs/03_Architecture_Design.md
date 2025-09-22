# System Architecture & Design Document

## Technology Stack
- **Backend:** Python FastAPI  
- **Database:** PostgreSQL  
- **Storage:** MinIO (S3-compatible)  
- **Auth:** JWT

## High-Level Architecture Diagram
Client → FastAPI Backend → PostgreSQL (users, logs, metadata)  
                → MinIO (file storage)

## Data Design (Schema)
- **users**(id, username, password_hash, role)  
- **files**(id, owner_id, filename, storage_path)  
- **file_shares**(file_id, shared_with_user_id)  
- **logs**(id, user_id, action, timestamp)

## Module Descriptions
- **Auth Module:** signup/login, JWT issue/verify.  
- **File Module:** upload/download/share.  
- **Audit Module:** logs actions.  
- **Admin Module:** admin-only access.

## API Specifications (Examples)
- `POST /auth/signup` → create user.  
- `POST /auth/login` → return JWT.  
- `POST /files/upload` → upload file.  
- `GET /files/{id}` → download file.  
- `POST /files/share` → share file with another user.  
- `GET /logs` → view audit logs (admin only).

## Security & Performance
- Passwords hashed with bcrypt.  
- JWT expiration & refresh.  
- File size limit (e.g., 10 MB per file).

