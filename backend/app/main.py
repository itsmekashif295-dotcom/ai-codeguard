from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import scan
from app.services.database import init_db

# Database tables banayein
init_db()

app = FastAPI(title="AI CodeGuard", version="0.3.0")

app.include_router(scan.router)

# Frontend serve karne ke liye
app.mount("/app", StaticFiles(directory="../frontend", html=True), name="frontend")

@app.get("/health")
def health():
    return {"healthy": True}