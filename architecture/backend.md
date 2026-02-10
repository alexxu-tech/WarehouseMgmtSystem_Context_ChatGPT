# Backend Architecture

## Purpose

This document describes the backend architecture of the Warehouse
Management System (WMS).

It defines responsibilities, internal structure, configuration, runtime
conventions, and future extension principles.

------------------------------------------------------------------------

## Responsibilities

The backend is responsible for:

-   Exposing REST APIs
-   Implementing business logic
-   Validating input and output data
-   Persisting data in PostgreSQL
-   Using Redis for caching
-   Providing health and monitoring endpoints

------------------------------------------------------------------------

## Technology Stack

-   Language: Python 3
-   Framework: FastAPI
-   Server: Uvicorn
-   Database: PostgreSQL
-   Cache: Redis
-   ORM: SQLAlchemy
-   Migration Tool: Alembic
-   Dependency Management: pip + requirements.txt
-   Configuration: .env + environment variables

------------------------------------------------------------------------

## Repository Location

Backend source code is located at:

src/dev/backend/

------------------------------------------------------------------------

## Project Structure

Typical layout:

src/dev/backend/ ├── app/ │ ├── main.py │ ├── api/ │ ├── core/ │ ├── db/
│ ├── models/ │ ├── schemas/ │ └── services/ ├── alembic/ │ └──
versions/ ├── requirements.txt └── .venv/

Notes:

-   .venv is local-only
-   alembic/versions contains committed migrations only

------------------------------------------------------------------------

## Runtime Entry Point

Main entry:

app.main:app

Development startup:

uvicorn app.main:app --reload --port 8000

Script-based startup uses no --reload to avoid orphan processes.

------------------------------------------------------------------------

## API Design

### Endpoint Style

-   REST-style JSON APIs
-   Predictable status codes
-   Structured error responses
-   Centralized validation

### Health Check

Endpoint:

GET /health

Response:

{"status":"ok"}

Used for environment validation and automation.

------------------------------------------------------------------------

## Layered Architecture

The backend follows a layered model.

### API Layer

-   Defines routes
-   Handles validation
-   Maps requests and responses

### Service Layer

-   Implements business rules
-   Coordinates workflows
-   Manages transactions

### Data Layer

-   SQLAlchemy models
-   Database queries
-   Redis access helpers

### Guidelines

-   No business logic in routes
-   No SQL in controllers

------------------------------------------------------------------------

## Database and Migrations

### PostgreSQL

-   Runs in Docker for development
-   Configured via environment variables
-   Stores persistent domain data

### Alembic

Migration generation:

alembic revision --autogenerate -m "message"

Guidelines:

-   Commit only intentional migrations
-   Delete temporary test migrations

------------------------------------------------------------------------

## Configuration

### Sources

-   .env files
-   Environment variables

### Common Settings

-   DATABASE_URL
-   REDIS_URL
-   API_PORT
-   SECRET_KEY
-   CORS_ORIGINS

### Rules

-   Never commit .env
-   Maintain .env.example

------------------------------------------------------------------------

## Logging and Debugging

### Logging

-   Script mode: .devrun/backend.log
-   Manual mode: stdout/stderr

### Debugging

-   Enable reload only in manual mode
-   Use structured logs
-   Avoid silent failures

------------------------------------------------------------------------

## Security (Planned)

Future security features:

-   JWT authentication
-   Role-based access control
-   Input sanitization
-   Rate limiting
-   CORS enforcement

------------------------------------------------------------------------

## Extension Strategy

New features should follow:

1.  Add models
2.  Add services
3.  Add APIs
4.  Add migrations
5.  Add tests

Avoid coupling layers directly.

------------------------------------------------------------------------

## Related Documents

-   architecture/overview.md
-   architecture/frontend.md
-   decisions/0001-dev-workflow.md
