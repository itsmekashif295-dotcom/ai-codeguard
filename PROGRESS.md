# AI CodeGuard — Progress Tracker

**Started:** 2025-10-23
**Target:** 8 weeks (1 hour/day)

---

## 🎯 Current Week: Week 1 — Foundation

### Week 1 Checklist
- [x] Day 1 — GitHub repo + local setup
- [x] Day 2 — Project structure + venv
- [x] Day 3 — FastAPI skeleton
- [x] Day 4 — /scan endpoint + Bandit
- [ ] Day 5 — CLI tool
- [ ] Day 6 — Tests + Docs
- [ ] Day 7 — Review + v0.1.0 tag

---

## 📅 Daily Log

### Day 1 — 2025-10-23
**Time spent:** 60 min
**What I did:**
- Created GitHub repo `ai-codeguard`
- Cloned locally to `Ai-CodeGuard` folder
- Added `.gitignore`, `LICENSE`, `README.md`, `PROGRESS.md`

**What I learned:**
- How to connect local git repo to GitHub

**Blockers:** 
- Initially cloned into wrong folder, but fixed it by deleting and cloning fresh.

---

### Day 2 — 2025-10-24
**Time spent:** 60 min
**What I did:**
- Created backend folder structure (api, services, models, tests)
- Setup Python virtual environment (venv)
- Installed dependencies (FastAPI, Bandit, Pydantic, etc.)

**What I learned:**
- Virtual environment kya hota hai aur kyun zaroori hai.
- requirements.txt se libraries install karna.

**Blockers:** Pydantic version error aya tha, usko update karke fix kiya.

**Commit:** (fill after push)


### Day 3 — 2025-10-25
**Time spent:** 60 min
**What I did:**
- Created FastAPI application in `app/main.py`
- Added root `/` and `/health` endpoints
- Ran uvicorn server and tested in browser
- Explored auto-generated Swagger docs at `/docs`

**What I learned:**
- How FastAPI works
- What `uvicorn --reload` does (auto-restarts on code change)

**Blockers:** Faced Windows Uvicorn red error, but server was running. Fixed git repository path issue.


### Day 4 — 2025-10-26
**Time spent:** 60 min
**What I did:**
- Created Pydantic schemas for request/response
- Built Bandit service to run scans securely in temp files
- Created `/scan` endpoint
- Tested API via Swagger UI and successfully detected CWE-78.

**What I learned:**
- How to run external commands (`subprocess`) in Python.
- How to fix environment compatibility issues (Python 3.14 vs 3.12).

**Blockers:** Faced Bandit crash due to Python 3.14, fixed by downgrading to Python 3.12.