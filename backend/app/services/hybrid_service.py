from typing import List
from app.models.schemas import Finding
from app.services.bandit_service import run_bandit
from app.services.ai_service import analyze_code_with_ai

def run_hybrid_scan(code: str) -> List[Finding]:
    findings = run_bandit(code)
    ai_result = analyze_code_with_ai(code)

    if "error" in ai_result:
        for finding in findings:
            finding.ai_explanation = f"AI unavailable: {ai_result['error']}"
        return findings

    if not findings and ai_result.get("is_vulnerable"):
        findings.append(Finding(
            cwe=ai_result.get("cwe_id"),
            severity=ai_result.get("severity", "MEDIUM"),
            line=0,
            description=ai_result.get("explanation", "AI detected a potential issue"),
            source="ai",
            ai_explanation=ai_result.get("explanation"),
            ai_fix=ai_result.get("fix")
        ))
    elif findings:
        for finding in findings:
            finding.ai_explanation = ai_result.get("explanation")
            finding.ai_fix = ai_result.get("fix")

    return findings