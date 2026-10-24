from fastapi import FastAPI

# FastAPI application initialize kar rahe hain
app = FastAPI(
    title="AI CodeGuard",
    description="AI-Generated Code Vulnerability Detection System",
    version="0.1.0"
)

# Root endpoint (Jab koi main page kholay ga)
@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "Welcome to AI CodeGuard API!",
        "version": "0.1.0"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "healthy": True,
        "message": "AI CodeGuard server is running perfectly!"
    }