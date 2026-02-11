# Roadmap

This roadmap is inferred from the existing architecture + workflow docs and should be refined as features land.

## Phase 1 — Foundation (now)
- Solid local dev workflow (`dev-up.sh` / `dev-down.sh`) and onboarding
- Baseline backend structure (FastAPI + SQLAlchemy + Alembic) + `/health`
- Baseline frontend scaffold (Vite + pnpm) + health-check UI
- Docker Compose services (PostgreSQL + Redis)

## Phase 2 — Core WMS Features (next)
- Inventory + SKU basics
- Orders (inbound/outbound/transfer) model + APIs
- First DB schema migrations (Alembic)
- Simple role model (Admin/Operator/Supervisor) → groundwork for RBAC

## Phase 3 — Hardening
- JWT auth + RBAC enforcement
- Structured error model end-to-end
- Logging conventions + troubleshooting playbook
- Test strategy (unit/integration)

## Phase 4 — Scalability (future)
- Horizontal scaling of backend services
- Background workers / message queue integration
- Distributed caching and DB read replicas
