from typing import List
from app.models.schemas import Finding
from app.services.bandit_service import run_bandit
from app.services.ai_service import analyze_code_with_ai

def run_hybrid_scan(code: str) -> List[Finding]:
    findings = run_bandit(code)
    try:
        ai_result = analyze_code_with_ai(code)
    except Exception:
        ai_result = {"error": "AI Failed"}

    if "error" in ai_result:
        for finding in findings:
            finding.ai_explanation = "AI offline"
            finding.confidence_score = 50
        return findings

    if findings:
        for finding in findings:
            finding.ai_explanation = str(ai_result.get("explanation", ""))
            finding.ai_fix = str(ai_result.get("fix", ""))
            finding.confidence_score = 95
    elif not findings and ai_result.get("is_vulnerable"):
        findings.append(Finding(
            cwe=str(ai_result.get("cwe_id", "Unknown")),
            severity=str(ai_result.get("severity", "MEDIUM")),
            line=0,
            description=str(ai_result.get("explanation", "AI detected issue")),
            source="ai",
            ai_explanation=str(ai_result.get("explanation", "")),
            ai_fix=str(ai_result.get("fix", "")),
            confidence_score=80
        ))

    return findings