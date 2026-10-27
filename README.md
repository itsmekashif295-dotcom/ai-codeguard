# 🛡️ AI CodeGuard

> AI-Generated Code Vulnerability Detection System

Detect security vulnerabilities in AI-generated (and human-written) code using static analysis + AI. Get CWE-mapped findings with severity, line numbers, and secure fix suggestions.

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-v0.1.0-orange)

---

## 🎯 Problem

AI coding assistants (ChatGPT, Copilot, Claude) generate code fast — but often with vulnerabilities. **AI CodeGuard** scans this code and reports issues before they reach production.

## ✨ Features (v0.1.0)

- [x] Python code scanning via REST API
- [x] Bandit integration for static analysis
- [x] CWE-mapped findings (Severity, Line number)
- [x] Command Line Interface (CLI) tool
- [x] Automated tests using Pytest
- [ ] AI/LLM-based CWE classification (Week 2)
- [ ] Web dashboard (Week 3)

---

## 🚀 Quickstart

### 1. Setup Backend
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --port 8000