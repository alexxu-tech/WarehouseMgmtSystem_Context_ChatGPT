# System Architecture Overview

## Purpose
This document describes the high-level architecture of the Warehouse Management System (WMS). It explains how major system components interact and why this structure was chosen.
This document serves as the primary reference for understanding the overall system design.

---

## High-Level Architecture
The system follows a standard three-tier architecture:

+----------------------+
| Frontend             |
| (Vite Web App)       |
+----------+-----------+
           |
           | HTTP / REST API
+----------v-----------+
| Backend              |
| (FastAPI Service)    |
+----------+-----------+
           |
           |
  +--------v------+   +------------+
  | PostgreSQL    |   | Redis      |
  | Database      |   | Cache      |
  +---------------+   +------------+

---

## Core Components

### Frontend
- Runs in the browser
- Built with Vite and modern JavaScript
- Handles user interaction and UI rendering
- Communicates with backend via HTTP API

### Backend
- Built with FastAPI and Uvicorn
- Implements business logic
- Exposes REST APIs
- Manages database and cache access

### Database (PostgreSQL)
- Stores persistent business data
- Runs in Docker during development
- Managed through Alembic migrations

### Cache (Redis)
- Provides fast in-memory storage
- Used for caching and future background tasks
- Runs in Docker during development

---

## Communication Flow

### Request Flow
1. User interacts with the frontend UI
2. Frontend sends HTTP request to backend
3. Backend validates and processes request
4. Backend queries PostgreSQL and/or Redis
5. Backend returns JSON response
6. Frontend updates UI

### Example
Browser → Frontend → Backend → Database/Redis → Backend → Frontend → Browser

---

## Development Architecture
Local development environment consists of:
- Docker containers:
  - PostgreSQL
  - Redis
- Local processes:
  - FastAPI backend (port 8000)
  - Vite frontend (port 5173)

Unified control is provided by:
- dev-up.sh
- dev-down.sh

These scripts ensure consistent startup and shutdown.

---

## Deployment Model (Current)
At the current stage, the system is designed for:
- Local development
- Single-instance backend
- Single database instance

Cloud deployment and scaling will be introduced later.

---

## Design Principles

### 1. Clear Separation of Responsibilities
Each component has a well-defined role:
- Frontend: Presentation and interaction
- Backend: Business logic and APIs
- Database: Persistent storage
- Redis: Performance optimization

### 2. Modularity
Components are loosely coupled and can be replaced or upgraded independently.

### 3. Developer Productivity
Local-first development is prioritized to enable:
- Fast iteration
- Easy debugging
- Minimal setup friction

### 4. Maintainability
System structure favors:
- Readable code
- Explicit interfaces
- Documented decisions

---

## Scalability Considerations (Future)
Planned architectural improvements include:
- Horizontal scaling of backend services
- Background worker processes
- Message queue integration
- Distributed caching
- Read replicas for database

These will be introduced when required by usage.

---

## Related Documents
- architecture/backend.md
- architecture/frontend.md
- decisions/0001-dev-workflow.md
