import subprocess
import tempfile
import os
import json
from typing import List
from app.models.schemas import Finding

def run_bandit(code: str) -> List[Finding]:
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, "codeguard_temp.py")
    
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(code)

    try:
        # Bandit chalao
        result = subprocess.run(
            ["bandit", "-f", "json", temp_path],
            capture_output=True, text=True
        )
        
        # AGAR ERROR AAYE TOH YAHAN PRINT HOGA
        if result.stderr:
            print("BANDIT ERROR:", result.stderr)
            
        print("BANDIT OUTPUT:", result.stdout) # Dekhne ke liye output kya aa raha hai
            
        data = json.loads(result.stdout or "{}")
    
    except Exception as e:
        print("EXCEPTION:", str(e))
        return []
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)

    findings: List[Finding] = []
    for issue in data.get("results", []):
        cwe = None
        if issue.get("issue_cwe"):
            cwe = f"CWE-{issue['issue_cwe'].get('id')}"
            
        findings.append(Finding(
            cwe=cwe,
            severity=issue.get("issue_severity", "UNKNOWN"),
            line=issue.get("line_number", 0),
            description=issue.get("issue_text", ""),
            test_id=issue.get("test_id"),
            confidence=issue.get("issue_confidence"),
        ))
        
    return findings