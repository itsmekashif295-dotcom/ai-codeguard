from typing import List
from app.models.schemas import Finding
from app.services.bandit_service import run_bandit
from app.services.ai_service import analyze_code_with_ai

def run_hybrid_scan(code: str) -> List[Finding]:
    # Step 1: Bandit scan
    findings = run_bandit(code)

    # Step 2: AI se poocho (Chahe Bandit ko kuch mile ya na mile)
    ai_result = analyze_code_with_ai(code)

    # Agar Bandit ko kuch nahi mila, par AI ko laga ke vulnerability hai
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
    # Agar Bandit ko vulnerabilities mili, toh AI ki explanation add karo
    elif findings and ai_result.get("is_vulnerable"):
        for finding in findings:
            finding.ai_explanation = ai_result.get("explanation")
            finding.ai_fix = ai_result.get("fix")

    return findings