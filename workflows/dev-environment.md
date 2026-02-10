# Development Environment Workflow

## Purpose

This document defines the standard development environment setup and
daily workflow for the Warehouse Management System (WMS).

It serves as the long-term reference for onboarding, maintenance, and
troubleshooting of local development environments.

------------------------------------------------------------------------

## Supported Platforms

Primary development platform:

-   Ubuntu (via native install or VM with VSCode Remote SSH)

Secondary / limited support:

-   Windows (via VM or WSL)
-   macOS (untested, best-effort)

All official workflows assume a Linux-compatible shell.

------------------------------------------------------------------------

## System Requirements

### Required Software

-   Git (latest stable)
-   Docker Engine + Docker Compose Plugin
-   Python 3 (python-is-python3 recommended)
-   Node.js (LTS)
-   pnpm (via corepack)
-   curl

### Recommended Versions

  Component   Version
  ----------- ----------
  Python      \>= 3.10
  Node.js     \>= 18
  Docker      \>= 24

------------------------------------------------------------------------

## Repository Setup

### Clone Repository

``` bash
git clone git@github.com:wwpswwps/WarehouseMgmtSystem.git
cd WarehouseMgmtSystem
```

### Initialize Environment File

``` bash
cp .env.example .env
```

Edit `.env` as needed for local configuration.

------------------------------------------------------------------------

## Backend Environment Setup

### Create Virtual Environment

``` bash
cd src/dev/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Verify Backend

``` bash
uvicorn app.main:app --reload --port 8000
curl http://localhost:8000/health
```

Expected:

``` json
{"status":"ok"}
```

Stop server with Ctrl+C after verification.

------------------------------------------------------------------------

## Frontend Environment Setup

### Install Dependencies

``` bash
cd src/dev/frontend
pnpm install
```

### Verify Frontend

``` bash
pnpm dev
```

Open in browser:

http://localhost:5173

------------------------------------------------------------------------

## Docker Services

### Start Services

``` bash
docker compose -f src/env/docker/docker-compose.yml up -d
```

### Verify Services

``` bash
docker compose -f src/env/docker/docker-compose.yml ps
```

PostgreSQL and Redis must be in `Up` state.

### Stop Services

``` bash
docker compose -f src/env/docker/docker-compose.yml down
```

------------------------------------------------------------------------

## Standard Daily Workflow

### Start Development

From repository root:

``` bash
./dev-up.sh
```

This will:

-   Check port availability
-   Start Docker services
-   Launch backend and frontend
-   Perform health checks

### Stop Development

``` bash
./dev-down.sh
```

This will:

-   Stop application processes
-   Release ports
-   Shutdown Docker services

------------------------------------------------------------------------

## Log Management

### Log Locations

  Component   Location
  ----------- ----------------------
  Backend     .devrun/backend.log
  Frontend    .devrun/frontend.log

`.devrun/` is ignored by Git and local-only.

### Viewing Logs

``` bash
tail -f .devrun/backend.log
tail -f .devrun/frontend.log
```

------------------------------------------------------------------------

## Common Tasks

### Regenerate Database Migrations

``` bash
cd src/dev/backend
source .venv/bin/activate
alembic revision --autogenerate -m "message"
alembic upgrade head
```

### Reset Local Database

``` bash
docker compose -f src/env/docker/docker-compose.yml down -v
docker compose -f src/env/docker/docker-compose.yml up -d
```

------------------------------------------------------------------------

## Troubleshooting

### Ports Already in Use

Symptoms:

-   dev-up.sh fails
-   Backend or frontend does not start

Check:

``` bash
ss -lptn 'sport = :8000'
ss -lptn 'sport = :5173'
```

Resolve:

``` bash
./dev-down.sh
```

------------------------------------------------------------------------

### Backend Not Responding

Check logs:

``` bash
tail -n 100 .devrun/backend.log
```

Verify Docker:

``` bash
docker compose -f src/env/docker/docker-compose.yml ps
```

------------------------------------------------------------------------

### Frontend Not Loading

Check:

``` bash
tail -n 100 .devrun/frontend.log
pnpm dev
```

Verify API connectivity:

``` bash
curl http://localhost:8000/health
```

------------------------------------------------------------------------

## Environment Maintenance

### Updating Dependencies

Backend:

``` bash
pip install --upgrade -r requirements.txt
```

Frontend:

``` bash
pnpm update
```

Docker:

``` bash
docker system prune
```

------------------------------------------------------------------------

## Security Practices

-   Never commit `.env`
-   Do not store secrets in scripts
-   Rotate credentials if leaked
-   Use least-privilege access

------------------------------------------------------------------------

## Onboarding Checklist

New developer setup:

-   [ ] Install system requirements
-   [ ] Configure SSH for GitHub
-   [ ] Clone repository
-   [ ] Create `.env`
-   [ ] Setup backend venv
-   [ ] Install frontend dependencies
-   [ ] Run `dev-up.sh`
-   [ ] Verify health endpoint

------------------------------------------------------------------------

## Related Documents

-   architecture/overview.md
-   architecture/backend.md
-   architecture/frontend.md
-   decisions/0001-dev-workflow.md
-   conversations/README.md
