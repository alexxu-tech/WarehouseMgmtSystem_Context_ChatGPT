# ADR-0001: Local Development Workflow (dev-up / dev-down)

## Status

Accepted

## Date

2026-02-09

------------------------------------------------------------------------

## Context

The Warehouse Management System (WMS) requires a reliable, repeatable
local development environment across different platforms and setups.

Development was performed in a mixed environment: - Windows host -
Ubuntu VM accessed via VSCode Remote SSH

The local system includes multiple moving parts: - PostgreSQL and Redis
running in Docker - FastAPI backend running locally - Vite frontend
running locally

Initial manual startup and shutdown led to multiple issues: - Orphaned
backend processes - Port conflicts (8000, 5173) - Unreliable shutdown
due to process forking - Inconsistent developer experience

A standardized workflow was required to ensure predictable startup and
shutdown behavior.

------------------------------------------------------------------------

## Goals and Non-Goals

### Goals

-   Provide one-command startup for local development
-   Provide one-command shutdown that reliably cleans resources
-   Avoid orphaned processes and port conflicts
-   Work consistently across Ubuntu environments
-   Minimize developer cognitive load

### Non-Goals

-   Full production deployment automation
-   Containerizing frontend and backend runtime
-   Solving CI/CD or cloud orchestration

------------------------------------------------------------------------

## Decision

Introduce two standardized scripts at the repository root:

-   `dev-up.sh`
-   `dev-down.sh`

### dev-up.sh

Responsibilities: - Verify required ports (8000, 5173) are free - Start
Docker services (PostgreSQL, Redis) - Start backend service in
background (without `--reload`) - Start frontend service in background -
Perform backend health check - Write logs to `.devrun/`

### dev-down.sh

Responsibilities: - Stop backend and frontend processes by port - Clean
up orphaned processes - Shut down Docker services

------------------------------------------------------------------------

## Rationale

-   `uvicorn --reload` spawns child processes, making PID-based shutdown
    unreliable
-   `pnpm dev` may spawn subprocesses not tracked by simple PID files
-   Killing processes by listening port is the only consistently
    reliable strategy
-   Background execution enables fast iteration and automation
-   Centralized scripts reduce setup errors and onboarding time

------------------------------------------------------------------------

## Alternatives Considered

### Manual Startup and Shutdown

Pros: - Simple to understand - No additional scripts

Cons: - Error-prone - Easy to forget cleanup steps - Leads to port
conflicts and orphaned processes

Rejected due to unreliability.

### Docker-Only Development

Pros: - Single orchestration layer - Environment parity

Cons: - Slower iteration - Poor hot-reload experience - Increased
complexity

Deferred for future consideration.

### tmux-Based Workflow

Pros: - Structured multi-process management - Interactive control

Cons: - Additional tooling requirement - Steeper learning curve

Rejected to keep onboarding simple.

------------------------------------------------------------------------

## Consequences

### Positive Consequences

-   Consistent local development experience
-   Predictable startup and shutdown behavior
-   Reduced environment-related debugging
-   Faster onboarding for new contributors

### Negative Consequences

-   Additional shell scripts to maintain
-   Requires bash-compatible environment

------------------------------------------------------------------------

## Implementation Notes

-   Scripts are located at repository root
-   `.devrun/` directory is used for logs and runtime artifacts
-   `.devrun/` is excluded from version control
-   Backend script intentionally omits `--reload`

------------------------------------------------------------------------

## Follow-Up Actions

-   Document dev workflow in README
-   Revisit workflow if Windows-native development is reintroduced
-   Extend scripts if background workers are added

------------------------------------------------------------------------

## Review and Evolution

This decision should be revisited when: - The project introduces
multiple backend services - Production deployment automation is added -
Developer workflow requirements significantly change

------------------------------------------------------------------------

## Related Documents

-   decisions/TEMPLATE.md
-   architecture/overview.md
-   architecture/backend.md
-   architecture/frontend.md
