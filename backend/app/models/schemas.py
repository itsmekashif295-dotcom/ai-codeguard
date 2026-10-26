from pydantic import BaseModel, Field
from typing import Optional, List

# Jab user API ko request bhejega
class ScanRequest(BaseModel):
    code: str = Field(..., description="Source code to scan")
    language: str = Field("python", description="Programming language")
    filename: Optional[str] = "snippet.py"

# Ek single vulnerability ka result
class Finding(BaseModel):
    cwe: Optional[str] = None
    severity: str
    line: int
    description: str
    test_id: Optional[str] = None
    confidence: Optional[str] = None
    source: str = "bandit"

# Jab API user ko jawab degi (Response)
class ScanResponse(BaseModel):
    filename: str
    language: str
    total_findings: int
    findings: List[Finding]