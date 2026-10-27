from fastapi.testclient import TestClient
from app.main import app

# TestClient FastAPI ke sath aata hai, isse hum server start kiye bina API test kar sakte hain
client = TestClient(app)

def test_health_check():
    """Test karein ke /health endpoint chal raha hai"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["healthy"] is True

def test_scan_command_injection():
    """Test karein ke Bandit command injection pakad raha hai"""
    payload = {
        "code": "import os\nos.system('ls ' + input())",
        "language": "python",
        "filename": "test.py"
    }
    response = client.post("/scan/", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    # Check karein ke vulnerability mili
    assert data["total_findings"] > 0
    # Check karein ke woh CWE-78 hai
    assert data["findings"][0]["cwe"] == "CWE-78"

def test_scan_safe_code():
    """Test karein ke safe code par koi vulnerability nahi milti"""
    payload = {
        "code": "print('Hello World')",
        "language": "python",
        "filename": "safe.py"
    }
    response = client.post("/scan/", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    # Safe code par 0 findings honi chahiye
    assert data["total_findings"] == 0