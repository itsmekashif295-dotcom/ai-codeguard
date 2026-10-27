# AI CodeGuard — Architecture

```text
[ Client (CLI / Web UI) ]
          │
          ▼
   [ FastAPI Backend ] 
          │
          ▼
   [ Bandit Service ]  ──► (Runs Bandit in temp file)
          │
          ▼
   [ JSON Report ]