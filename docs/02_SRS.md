# Software Requirements Specification (SRS)

## Introduction
This software allows users to securely upload and share files, with access restricted by authentication and roles. Intended for demonstration of backend development and security practices.

## Overall Description
- **Environment:** Python (FastAPI), PostgreSQL, MinIO/S3.  
- **Assumptions:** Small user base (<100).  
- **Constraints:** Must run on local or cloud VM with Docker.

## Functional Requirements
- The system shall allow users to register and log in.  
- The system shall allow file upload, download, and sharing.  
- The system shall enforce role-based access control.  
- The system shall maintain logs of all activities.

## Non-Functional Requirements
- **Performance:** Handle 50 concurrent requests.  
- **Security:** JWT authentication, encrypted storage paths.  
- **Usability:** REST API with Swagger UI.  
- **Reliability:** Error handling and retries on storage.

## Use Cases / User Stories
- As a user, I can upload a file and share it with another user.  
- As an admin, I can view all uploaded files.  
- As a user, I can only see files I uploaded or files shared with me.

## Acceptance Criteria
- Users cannot access files without proper authentication.  
- Uploads and downloads succeed for valid users.  
- All actions appear in the audit log.

