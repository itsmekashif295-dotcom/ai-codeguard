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
- [x] Day 9 — AI-based CWE Classification
- [x] Day 10 — Hybrid Scanner (Bandit + AI)
- [x] Day 11 — Confidence Scoring
- [x] Day 12 — Prompt Engineering + Testing
- [x] Day 13 — Evaluation on Dataset
- [x] Day 14 — Review + v0.2.0 Tag

### Week 3 Checklist (RAG & Web UI)
- [x] Day 15 — Fix RAG + Basic Web UI
- [x] Day 16 — Speed Fix & Professional UI
- [ ] Day 17 — Advanced UI Features (Mobile Responsive)
- [ ] Day 18 — File Upload Feature in UI
- [ ] Day 19 — GitHub Action Integration
- [ ] Day 20 — Dockerize the Project
- [ ] Day 21 — Review + v0.3.0 Tag

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


### Day 9 — 2025-10-31
**Time spent:** 60 min
**What I did:**
- Designed a structured prompt for security analysis.
- Added `analyze_code_with_ai()` function to ai_service.py.
- Handled JSON parsing.
- Tested on vulnerable + safe code samples.

**What I learned:**
- Prompt Engineering for structured AI responses.
- Handling Windows terminal Unicode errors.

**Blockers:** Faced emoji Unicode error, fixed by removing it from the test script.



### Day 10 — 2025-11-01
**Time spent:** 120 min
**What I did:**
- Updated Pydantic schemas to include AI fields.
- Built `hybrid_service.py` to combine Bandit + AI.
- Updated `/scan` endpoint to use hybrid scanner.
- Tested via Swagger UI and CLI.

**What I learned:**
- How to orchestrate multiple services.
- How to merge structured findings from different sources.

**Blockers:** None


### Day 11 — 2025-11-02
**Time spent:** 60 min
**What I did:**
- Added 10-second timeout to Gemini API calls.
- Updated hybrid_service to gracefully handle AI failures.
- Tested fallback (Bandit result still returned if AI fails).

**What I learned:**
- How to set timeouts in HTTP clients.
- Error handling patterns for microservices.

**Blockers:** AI timed out due to slow internet, but software handled it gracefully.


### Day 12 — 2025-11-03
**Time spent:** 120 min
**What I did:**
- Improved AI prompts and error messages.
- Added `confidence_score` to findings.
- Calculated scores: 95% (Bandit + AI), 80% (AI only), 70% (Bandit only), 50% (AI fail).

**What I learned:**
- How to merge confidence from multiple sources.
- Better UX with friendly error messages.


### Day 13 — 2025-11-04
**Time spent:** 60 min
**What I did:**
- Installed chromadb and sentence-transformers.
- Created `rag_service.py` to setup a local vector database.
- Seeded it with CWE documentation.
- Tested retrieval of CWE-78 and CWE-89 knowledge.
- Fixed Git mistake: removed local DB files from repo and added to .gitignore.

**What I learned:**
- How Vector Databases work.
- How to use sentence-transformers for embeddings.
- Why local binary files shouldn't be pushed to Git.

**Blockers:** None


### Day 14 — 2025-11-05
**Time spent:** 120 min
**What I did:**
- Integrated RAG database with AI service.
- Fixed Pydantic validation errors (500 error) related to AI output types.
- Verified fallback logic (AI offline -> returns Bandit result).

**What I learned:**
- How to handle unexpected data types from third-party APIs.
- The importance of graceful degradation in software.

**Blockers:** Internet slow, AI times out, but fallback works perfectly.


### Day 15 — 2025-11-08
**Time spent:** 120 min
**What I did:**
- Fixed RAG data type bug.
- Re-integrated RAG into AI service.
- Built basic HTML/CSS/JS Web UI.
- Served Web UI via FastAPI StaticFiles.

**What I learned:**
- How to serve static files in FastAPI.
- How to make API calls from Vanilla JS.

**Blockers:** None

### Day 16 — 2025-11-09
**Time spent:** 90 min
**What I did:**
- Reduced AI timeout to 4 seconds for better UX.
- Added loading spinner to the Web UI.
- Formatted the JSON output into beautiful UI cards.

**What I learned:**
- Frontend UI/UX improvements with CSS and JS.

**Blockers:** None