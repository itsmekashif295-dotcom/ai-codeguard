from fastapi import APIRouter, HTTPException
from app.models.schemas import ScanRequest, ScanResponse
from app.services.hybrid_service import run_hybrid_scan

router = APIRouter(prefix="/scan", tags=["Scan"])

@router.post("/", response_model=ScanResponse)
def scan_code(request: ScanRequest):
    if request.language.lower() != "python":
        raise HTTPException(status_code=400, detail="Currently only Python is supported")

    # Bandit + AI dono chalao
    findings = run_hybrid_scan(request.code)
    
    return ScanResponse(
        filename=request.filename or "snippet.py",
        language=request.language,
        total_findings=len(findings),
        findings=findings,
    )