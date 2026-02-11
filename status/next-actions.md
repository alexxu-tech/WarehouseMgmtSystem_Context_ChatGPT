# Next Actions

A short, actionable checklist for the next session.

## Environment + workflow
- [ ] Ensure `.env.example` matches required settings (DATABASE_URL, REDIS_URL, etc.)
- [ ] Confirm `dev-up.sh` writes logs to `.devrun/` and passes health check

## Backend
- [ ] Define minimal domain schema (SKU, Inventory, Order) and create first Alembic migration
- [ ] Add one real endpoint beyond `/health` (e.g., `GET /skus` returning empty list)
- [ ] Establish error response format for validation failures

## Frontend
- [ ] Create pages layout skeleton (page → layout → component)
- [ ] Add API service wrapper and call backend endpoint(s)
- [ ] Implement visible error handling (network / backend errors)

## Documentation
- [ ] Add a conversation summary for today’s work in `conversations/`
- [ ] If any decision changes, add ADR in `decisions/`
