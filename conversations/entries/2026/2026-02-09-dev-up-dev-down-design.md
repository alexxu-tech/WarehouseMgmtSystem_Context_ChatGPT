# 2026-02-09 — dev-up / dev-down design

## Context
Local development required running multiple components:
- Docker services (PostgreSQL, Redis)
- Backend (FastAPI/Uvicorn)
- Frontend (Vite/pnpm)

Manual startup/shutdown caused orphan processes and port conflicts.

## Key Questions
- How do we ensure consistent startup/shutdown across Ubuntu-based environments?
- Why not just rely on PID files / reload mode?
- What’s the most reliable way to stop dev processes?

## Decisions / Conclusions
- Adopt two root scripts: `dev-up.sh` and `dev-down.sh`.
- Start backend **without** `--reload` in script mode.
- Stop backend/frontend by **killing processes by listening port** (8000, 5173).
- Write logs to `.devrun/`.

## Rationale
- Uvicorn `--reload` spawns child processes → PID shutdown unreliable.
- `pnpm dev` can spawn subprocesses → PID shutdown unreliable.
- Port-based termination is consistently reliable.

## Follow-ups
- Keep `workflows/dev-environment.md` as the onboarding reference.
- Maintain ADR-0001 if workflow changes significantly.
