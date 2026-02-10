# Warehouse Management System — Project Context

This repository contains architectural decisions, workflows, and design context
for the Warehouse Management System (WMS) project.

It serves as a long-term knowledge base for:

- System design rationale
- Development workflows
- Technical trade-offs
- Historical decisions
- AI-assisted development context

This repository is NOT source code.
It documents *why* and *how* things are built.

---

## Project Goals

- Build a scalable, cloud-ready Warehouse Management System
- Backend: FastAPI + PostgreSQL + Redis
- Frontend: Vite + modern JS framework
- Focus on maintainability and automation
- Support AI-assisted development

---

## Main Repositories

- Source Code:
  https://github.com/wwpswwps/WarehouseMgmtSystem

- Context Repository:
  (this repository)

---

## Repository Structure

| Directory     | Purpose                                  |
|---------------|------------------------------------------|
| architecture/ | System design and component layout       |
| decisions/    | Architecture Decision Records (ADR)      |
| workflows/    | Development and release workflows        |
| conversations/| Curated AI/human discussion summaries    |
| glossary.md   | Project terminology                      |

---

## How to Use This Repo

1. All major technical decisions must be documented in `decisions/`
2. Development workflows go in `workflows/`
3. Architecture updates go in `architecture/`
4. Important AI discussions should be summarized in `conversations/`

This repo is the single source of truth for project context.
