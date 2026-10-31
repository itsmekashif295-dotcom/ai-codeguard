from pydantic import BaseModel, Field
from typing import Optional, List

class ScanRequest(BaseModel):
    code: str = Field(..., description="Source code to scan")
    language: str = Field("python", description="Programming language")
    filename: Optional[str] = "snippet.py"

class Finding(BaseModel):
    cwe: Optional[str] = None
    severity: str
    line: int
    description: str
    test_id: Optional[str] = None
    confidence: Optional[str] = None
    source: str = "bandit"
    # Naye fields AI ke liye:
    ai_explanation: Optional[str] = None
    ai_fix: Optional[str] = None

class ScanResponse(BaseModel):
    filename: str
    language: str
    total_findings: int
    findings: List[Finding]