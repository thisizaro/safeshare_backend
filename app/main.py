from fastapi import FastAPI
from app.controller import auth_controller, file_controller

app = FastAPI(title="SafeShare API")

@app.get("/")
def read_root():
    return {"message": "SafeShare API is running!"}


# Include routers
app.include_router(auth_controller.router)
app.include_router(file_controller.router)
