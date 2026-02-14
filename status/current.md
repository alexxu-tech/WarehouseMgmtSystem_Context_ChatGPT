# Project Current Status

> **Update rule:** After each working session, update this file first.
> Keep it short and authoritative.

## Overall Phase

Phase 1 complete: First end-to-end SKU vertical slice (DB → API → UI)
implemented and manually verified. Next: Phase 2 feature expansion and
conventions hardening.

## What's already established (from existing docs)

-   Architecture: 3-tier (Frontend Vite → Backend FastAPI →
    PostgreSQL/Redis). See `architecture/overview.md`.
-   Backend conventions: layered model, health endpoint, Alembic
    migrations. See `architecture/backend.md`.
-   Frontend conventions: Vite + pnpm, SPA-ready structure, API service
    layer.
-   Dev workflow: `dev-up.sh` / `dev-down.sh` to avoid orphan processes
    & port conflicts. See `decisions/0001-dev-workflow.md`.
-   Onboarding + daily workflow: `workflows/dev-environment.md`.
-   Manual verification procedure on Ubuntu:
    `verify/ubuntu-manual-testing-steps-with-explanations.md`.
-   Phase 1 vertical slice: SKU models + initial migration + GET /skus +
    /skus UI page (Ant Design) verified end-to-end.
-   Verification record: `verify/2026/2026-02-13-phase1-sku-e2e.md`.

## In Progress

-   Normalize API prefix convention (decide `/skus` vs `/api/skus` and
    apply consistently).
-   Add create/update SKU flows (API + UI form).
-   Expand inventory workflows after SKU CRUD stabilizes.

## Not started yet (but planned in docs)

-   JWT auth + RBAC (not implemented; noted as planned).
-   Rate limiting, CORS hardening, token storage strategy.
-   Background workers / message queue integration (future scalability
    section).

## Key constraints / conventions

-   Prefer Linux-compatible shell workflows (Ubuntu primary).
-   Scripts should manage ports 8000/5173 and log to `.devrun/`.
