# Blockers / Risks

## Current Known Risks (from docs)
- Orphan processes and port conflicts are addressed by dev scripts; ensure scripts stay maintained (ADR-0001).
- Windows/macOS support is secondary/untested; official workflows assume Linux shell.

## Likely upcoming blockers (based on what’s *not yet specified* in docs)
- DB schema ownership (what tables/entities first; migration cadence)
- Auth/RBAC details (token lifecycle, refresh, storage, permissions matrix)
- API versioning strategy (when to introduce v1, breaking changes policy)
