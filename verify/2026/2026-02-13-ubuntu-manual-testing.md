# Manual Testing Steps (Ubuntu) — With Explanations

## Purpose
This document records the **Ubuntu-adapted** manual testing steps for the WMS project, including **what each step is doing** and **why it matters**.

These steps are useful when:
- Troubleshooting environment issues
- Verifying components independently (Docker, backend, frontend)
- Debugging without `dev-up.sh` / `dev-down.sh`

> Note: These steps reflect the modified Ubuntu workflow (Linux shell),
> not the original Windows PowerShell version.

---

## Assumptions
- You are working on **Ubuntu** (native/VM) and using a bash-compatible shell
- `python-is-python3` is installed (so `python` points to Python 3)
- You are running commands from the **project root** unless stated otherwise

---

## Step 1 — Create `.env` from template

### Command
From repository root:
```bash
cp .env.example .env
```

### What this step does
- Creates a local environment configuration file (`.env`) based on a shared template (`.env.example`).

### Why it matters
- `.env` supplies runtime settings such as database connection strings and ports.
- `.env` should **not** be committed; it can contain local secrets or machine-specific settings.

---

## Step 2 — Start PostgreSQL + Redis via Docker Compose

### Commands
Start containers:
```bash
docker compose -f src/env/docker/docker-compose.yml up -d
```
Verify containers:
```bash
docker compose -f src/env/docker/docker-compose.yml ps
```

### What this step does
- Spins up **PostgreSQL** (database) and **Redis** (cache) services as containers.
- The `-d` flag runs them in the background (detached).

### Why it matters
- The backend depends on these services (now or soon).
- Running them via Compose ensures consistent versions and ports across machines.

### Expected result
In `docker compose ps`, you should see containers like:
- `postgres` → `Up`
- `redis` → `Up`

---

## Step 3 — Start Backend (FastAPI via Uvicorn)

### Commands
Go to backend folder:
```bash
cd src/dev/backend
```

Create Python virtual environment (first time only):
```bash
python -m venv .venv
```

Activate virtual environment:
```bash
source .venv/bin/activate
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Start backend server:
```bash
uvicorn app.main:app --reload --port 8000
```

### What this step does
- Creates and activates an isolated Python environment (`.venv`) so dependencies do not pollute system Python.
- Installs backend dependencies listed in `requirements.txt`.
- Starts the FastAPI application using Uvicorn on port **8000**.
- `--reload` watches source code changes and restarts the server automatically (development convenience).

### Why it matters
- Confirms the backend can boot and serve requests.
- Ensures your Python dependencies are correctly installed.
- Establishes the API endpoint needed by the frontend integration test.

---

## Step 4 — Test Backend Health Endpoint

### Command
Open a **new terminal** (keep backend terminal running), then:
```bash
curl http://localhost:8000/health
```

### What this step does
- Sends a simple HTTP request to the backend health endpoint.

### Why it matters
- Validates that the backend is reachable and responding correctly.
- Health endpoints are the quickest way to confirm “server is alive.”

### Expected result
```json
{"status":"ok"}
```

---

## Step 5 — Test Alembic Migration Setup

### Commands
In a **new terminal** (or reuse one), activate the same venv:
```bash
cd src/dev/backend
source .venv/bin/activate
```

Generate a migration file:
```bash
alembic revision --autogenerate -m "init"
```

### What this step does
- Runs Alembic autogeneration to create a migration script under `alembic/versions/`.

### Why it matters
- Confirms that Alembic is installed and configured correctly.
- Confirms Alembic can connect to the database and inspect models metadata.

### Expected result
- A new file appears under: `src/dev/backend/alembic/versions/`
- Command exits without errors.

### Cleanup note
If this migration was created only to validate tooling (and contains no real schema changes), you can delete it afterward.

---

## Step 6 — Start Frontend (Vite)

### Commands
Open another terminal:
```bash
cd src/dev/frontend
```

Install JS dependencies (first time only, or when package.json changes):
```bash
pnpm install
```

Start dev server:
```bash
pnpm dev
```

### What this step does
- Installs frontend dependencies into `node_modules` using `pnpm`.
- Starts Vite dev server (typically on port **5173**).

### Why it matters
- Confirms frontend toolchain is correctly installed and runnable.
- Enables browser-based integration testing against the backend.

---

## Step 7 — Verify Frontend UI + API Integration

### Action
Open in browser:
```
http://localhost:5173
```

Expected UI (example from generated skeleton):
- A page/card titled similar to: “WMS Admin Skeleton”
- A button like: “Check API Health”

Click the health button.

### What this step does
- Frontend performs an API call to the backend (usually `/health`).

### Why it matters
- Confirms end-to-end path is working:
  Browser → Frontend → Backend → Response → Frontend UI update

### Expected result
- UI shows a success indicator (e.g., green “ok”).

---

## Step 8 — Teardown / Cleanup

### Stop backend and frontend
In the terminals running Uvicorn and Vite:
- Press `Ctrl + C`

### Stop Docker services
From repository root:
```bash
docker compose -f src/env/docker/docker-compose.yml down
```

### What this step does
- Stops application servers and shuts down containers.

### Why it matters
- Frees ports (8000, 5173, 5432, 6379)
- Prevents orphan processes and resource leaks
- Keeps your machine clean between sessions

---

## Quick Diagnostics (Optional)

### Check whether ports are still in use
```bash
ss -lptn 'sport = :8000'
ss -lptn 'sport = :5173'
ss -lptn 'sport = :5432'
ss -lptn 'sport = :6379'
```

### Check docker containers
```bash
docker compose -f src/env/docker/docker-compose.yml ps
```

---

## Related Documents
- workflows/dev-environment.md
- manual-testing-workflow.md
- decisions/0001-dev-workflow.md
