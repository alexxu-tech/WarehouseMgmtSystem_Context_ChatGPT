# Project Current Status

> **Update rule:** After each working session, update this file first. Keep it short and authoritative.

## Overall Phase
Local dev environment + baseline architecture established. Next: implement core domain features.

## What’s already established (from existing docs)
- Architecture: 3-tier (Frontend Vite → Backend FastAPI → PostgreSQL/Redis). See `architecture/overview.md`.
- Backend conventions: layered model, health endpoint, Alembic migrations. See `architecture/backend.md`.
- Frontend conventions: Vite + pnpm, SPA-ready structure, API service layer. See `architecture/frontend.md`.
- Dev workflow: `dev-up.sh` / `dev-down.sh` to avoid orphan processes & port conflicts. See `decisions/0001-dev-workflow.md`.
- Onboarding + daily workflow: `workflows/dev-environment.md`.
- Manual verification procedure on Ubuntu: `verify/ubuntu-manual-testing-steps-with-explanations.md`.

## In Progress
- Define DB schema + first migrations (inventory/order baseline).
- Implement minimal API endpoints beyond `/health`.
- Create initial frontend pages + wiring for API calls.

## Not started yet (but planned in docs)
- JWT auth + RBAC (not implemented; noted as planned).
- Rate limiting, CORS hardening, token storage strategy.
- Background workers / message queue integration (future scalability section).

## Key constraints / conventions
- Prefer Linux-compatible shell workflows (Ubuntu primary).
- Scripts should manage ports 8000/5173 and log to `.devrun/`.
