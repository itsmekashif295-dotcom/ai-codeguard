from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import json

from app.models.schemas import ScanRequest, ScanResponse
from app.services.hybrid_service import run_hybrid_scan
from app.services.database import get_db, ScanHistory

router = APIRouter(prefix="/scan", tags=["Scan"])

@router.post("/", response_model=ScanResponse)
def scan_code(request: ScanRequest, db: Session = Depends(get_db)):
    if request.language.lower() != "python":
        raise HTTPException(status_code=400, detail="Currently only Python is supported")

    # Bandit + AI dono chalao
    findings = run_hybrid_scan(request.code)
    
    response = ScanResponse(
        filename=request.filename or "snippet.py",
        language=request.language,
        total_findings=len(findings),
        findings=findings,
    )

    # Database mein save karein
    history_entry = ScanHistory(
        filename=response.filename,
        language=response.language,
        total_findings=response.total_findings,
        result_json=response.model_dump_json(),
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    db.add(history_entry)
    db.commit()
    db.refresh(history_entry)

    return response

from typing import List

@router.get("/history")
def get_scan_history(db: Session = Depends(get_db)):
    # Sabse nayi scans pehle dikhayein
    history = db.query(ScanHistory).order_by(ScanHistory.id.desc()).limit(50).all()
    return [
        {
            "id": h.id,
            "filename": h.filename,
            "language": h.language,
            "total_findings": h.total_findings,
            "created_at": h.created_at,
            "result": json.loads(h.result_json)
        }
        for h in history
    ]