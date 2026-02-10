# Project Glossary

This document defines standard terminology used in the
Warehouse Management System (WMS) project.

All contributors and AI assistants should follow these
definitions to ensure consistent communication.

---

## Business Terms

### Order
A customer or internal request to move, ship, or receive goods.

May include inbound, outbound, or transfer operations.

---

### Inventory
The quantity of physical goods stored in a warehouse
and tracked by the system.

---

### SKU (Stock Keeping Unit)
A unique identifier representing a specific product type.

Each SKU maps to one logical product definition.

---

### Warehouse
A physical location where goods are stored and processed.

May contain multiple zones and locations.

---

### Location
A specific storage position inside a warehouse
(e.g., shelf, bin, rack position).

---

### Batch
A grouped set of operations processed together
(e.g., picking batch, receiving batch).

---

## User Roles

### Admin
A system-level administrator with full configuration privileges.

---

### Operator
A warehouse staff member responsible for daily operations.

---

### Supervisor
A user responsible for monitoring and managing operators.

---

## System and Architecture Terms

### Backend
The FastAPI-based service providing APIs and business logic.

---

### Frontend
The Vite-based web application used by end users.

---

### Service Layer
The backend layer responsible for business rules and workflows.

---

### ADR (Architecture Decision Record)
A formal document describing a significant technical decision.

Stored under `decisions/`.

---

### Context Repository
A documentation-only repository storing architectural
and historical project context.

---

### Health Check
A lightweight API endpoint used to verify service availability.

Usually exposed at `/health`.

---

### Dev Scripts
The `dev-up.sh` and `dev-down.sh` scripts used to manage
local development environment lifecycle.

---

## Development Conventions

### Local Development
Development performed using Docker, local backend,
and local frontend.

Managed via standardized scripts.

---

### Production Environment
The deployed system running in cloud or on-premise
infrastructure.

Not yet implemented.

---

## Update Policy

- New terms must be added here when introduced
- Deprecated terms should be marked clearly
- Definitions should be concise and unambiguous
