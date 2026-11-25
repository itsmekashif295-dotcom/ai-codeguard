# 🛡️ AI CodeGuard

AI-Generated Code Vulnerability Detection System

Yeh project AI se banaye gaye code mein security vulnerabilities (jaise SQL Injection, Command Injection) dhoondta hai aur unko fix karne ka tareeqa batata hai.

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Version](https://img.shields.io/badge/version-v0.3.0-orange)

---

## 🎯 Kya Karta Hai?

- Code scan karta hai (Bandit + Google Gemini AI).
- Vulnerability ka naam (CWE) aur line number batata hai.
- Fix karne ka mashwara deta hai.
- Iska ek Web UI hai jahan aap file upload karke scan kar sakte hain.

---

## 🚀 Kaise Chalayein? (Docker ke zariye)

Agar aapke paas Docker hai, toh bas yeh commands chalayein:

```bash
git clone https://github.com/itsmekashif295-dotcom/ai-codeguard.git
cd ai-codeguard
echo "GEMINI_API_KEY=your_api_key_here" > backend/.env
docker compose up --build