# 🛡️ AI CodeGuard

> AI-Generated Code Vulnerability Detection System

Detect security vulnerabilities in AI-generated (and human-written) code using static analysis + AI. Get CWE-mapped findings with severity, line numbers, and secure fix suggestions.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🎯 Problem

AI coding assistants (ChatGPT, Copilot, Claude) generate code fast — but often with vulnerabilities:
- SQL Injection (CWE-89)
- Command Injection (CWE-78)
- Hardcoded Secrets (CWE-798)
- Weak Crypto (CWE-327)

**AI CodeGuard** scans this code and reports issues before they reach production.

---

## ✨ Features (Planned)

- [x] Python code scanning
- [ ] AI/LLM-based CWE classification
- [ ] RAG-powered fix suggestions
- [ ] Web dashboard
- [ ] CLI tool
- [ ] GitHub Action

---

## 🚀 Quickstart

```bash
# Coming in Week 1