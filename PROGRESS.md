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
- [x] Day 5 — CLI tool
- [x] Day 6 — Tests + Docs
- [x] Day 7 — Review + v0.1.0 tag
### Week 2 Checklist (AI Layer)
- [x] Day 8 — Gemini AI Setup + API Connection
- [ ] Day 9 — AI-based CWE Classification
- [ ] Day 10 — Hybrid Scanner (Bandit + AI)
- [ ] Day 11 — Confidence Scoring
- [ ] Day 12 — Prompt Engineering + Testing
- [ ] Day 13 — Evaluation on Dataset
- [ ] Day 14 — Review + v0.2.0 Tag

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

### Day 5 — 2025-10-27
**Time spent:** 60 min
**What I did:**
- Added `typer` and `requests` to dependencies.
- Built CLI tool in `cli/codeguard.py`.
- Tested CLI against a local vulnerable file.

**What I learned:**
- How to create command-line applications using Typer.
- How to make HTTP requests in Python using `requests`.

**Blockers:** None



### Day 6 — 2025-10-28
**Time spent:** 60 min
**What I did:**
- Wrote automated tests using Pytest (test_scan.py).
- Fixed module import error using pytest.ini.
- Ran tests and verified 3 tests pass.
- Created `docs/scope.md` and `docs/architecture.md`.

**What I learned:**
- How to test FastAPI endpoints using TestClient.
- Importance of documentation in real projects.

**Blockers:** Faced ModuleNotFoundError, fixed by adding pythonpath to pytest.ini.



### Day 8 — 2025-10-30
**Time spent:** 60 min
**What I did:**
- Got Gemini API key from Google AI Studio.
- Created `.env` file to securely store API key.
- Installed `google-genai` SDK.
- Built `ai_service.py` to interact with Gemini.
- Fixed model name error (updated to gemini-3.8-flash).
- Tested AI connection successfully.

**What I learned:**
- How to use environment variables for secrets.
- How to integrate LLMs in a Python project.
- How to debug API model version changes.

**Blockers:** Faced model not found error, fixed by updating the model name.