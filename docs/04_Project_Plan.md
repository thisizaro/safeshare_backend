# Project Plan & Development Standards

## Timeline / Milestones

- **Day 1:** Setup & Auth.
- **Day 2:** File Handling.
- **Day 3:** Audit Logs & Tests.
- **Day 4:** Deployment.

## Roles & Responsibilities

- **Developer:** Aranya Dutta (thisizaro)

## Coding Standards

- Follow Python PEP8 style guide.
- Include docstrings for all functions.
- Use consistent naming (snake_case).

## Version Control Strategy

- **Repository:** GitHub.
- **Branching:** `main` (stable), `dev` (feature work).
- **Commit format:** `[module] action (short desc)`.

## Tools & Environment

- **IDE:** VS Code.
- **Version Control:** GitHub.
- **Deployment:** Docker + Render/Heroku.

## Project Structure

```
safeshare-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── controller/
│   │   ├── __init__.py
│   │   ├── file_controller.py
│   │   └── auth_controller.py
│   ├── service/
│   │   ├── __init__.py
│   │   ├── file_service.py
│   │   └── auth_service.py
│   ├── model/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── file.py
│   ├── repository/
│   │   ├── __init__.py
│   │   └── database.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_file.py
│
├── docs/
│   ├── Project_Overview.md
│   ├── System_Requirements_Spec.md
│   ├── System_Architecture_Design.md
│   ├── Project_Plan_Development_Standards.md
│   └── Testing_Strategy.md
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```
