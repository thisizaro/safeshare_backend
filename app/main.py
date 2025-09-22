from fastapi import FastAPI

app = FastAPI(title="SafeShare")

@app.get("/")
def read_root():
    return {"message": "SafeShare API is running!"}
