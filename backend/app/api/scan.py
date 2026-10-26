from fastapi import APIRouter, HTTPException
from app.models.schemas import ScanRequest, ScanResponse
from app.services.bandit_service import run_bandit

# Router banaya taake code clean rahe
router = APIRouter(prefix="/scan", tags=["Scan"])

@router.post("/", response_model=ScanResponse)
def scan_code(request: ScanRequest):
    # Sirf Python support karte hain abhi
    if request.language.lower() != "python":
        raise HTTPException(status_code=400, detail="Currently only Python is supported")

    # Bandit chalao
    findings = run_bandit(request.code)
    
    # Result return karo
    return ScanResponse(
        filename=request.filename or "snippet.py",
        language=request.language,
        total_findings=len(findings),
        findings=findings,
    )