from fastapi import FastAPI
from app.api import scan

app = FastAPI(
    title="AI CodeGuard",
    description="AI-Generated Code Vulnerability Detection System",
    version="0.1.0"
)

# Yahan hum naya scan router attach kar rahe hain
app.include_router(scan.router)

@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "Welcome to AI CodeGuard API!",
        "version": "0.1.0"
    }

@app.get("/health")
def health_check():
    return {
        "healthy": True,
        "message": "AI CodeGuard server is running perfectly!"
    }