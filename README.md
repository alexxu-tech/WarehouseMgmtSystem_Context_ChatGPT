# Warehouse Management System --- Context Hub

This repository is the long-term context and memory system for the
Warehouse Management System (WMS) project:

https://github.com/alexxu-tech/WarehouseMgmtSystem

⚠️ This repository does NOT contain production source code. All
implementation lives in the main WMS repository.

This repository preserves architectural knowledge, decisions, reasoning
history, workflows, and validation evidence.

------------------------------------------------------------------------

# 1. Purpose of This Repository

WarehouseMgmtSystem_Context_ChatGPT is a structured context repository
designed to support long-term AI-assisted development and knowledge
retention.

It enables:

-   Accurate restoration of project context
-   Cross-session continuity for AI and humans
-   Traceable technical decision-making
-   Reproducible operational workflows
-   Auditable manual verification history
-   Preservation of reasoning processes

The repository acts as the project's long-term memory.

------------------------------------------------------------------------

# 2. Scope and Boundaries

Included:

-   Architecture documentation
-   Architecture Decision Records (ADR)
-   Project status tracking
-   Development and operation workflows
-   Manual verification records
-   Conversation and reasoning archives

Excluded:

-   Application source code
-   Build artifacts
-   Runtime configurations
-   Deployment packages

All production implementation lives in the main WMS repository.

------------------------------------------------------------------------

# 3. Repository Structure

    WarehouseMgmtSystem_Context_ChatGPT/
    ├─ README.md
    ├─ glossary.md
    ├─ .github/
    ├─ tools/
    ├─ architecture/
    ├─ decisions/
    ├─ status/
    ├─ workflows/
    ├─ verify/
    └─ conversations/

------------------------------------------------------------------------

# 4. Directory Responsibilities

This section defines the authoritative responsibility, content scope,
and maintenance rules for each directory.

------------------------------------------------------------------------

## 4.1 .github/ --- Automation Layer

    .github/
    └─ workflows/
       └─ context-lint.yml

Purpose: 
- Centralizes GitHub Actions configuration.
- Enforces structural and consistency rules on PRs.

Key File:

-   `context-lint.yml`\
    Executes `tools/context_lint.py` on pull requests. Blocks merges
    when repository rules are violated.

Rules: - Only CI-related files are allowed here. - All automation must
be explicitly reviewed.

------------------------------------------------------------------------

## 4.2 tools/ --- Maintenance and Validation Tools

    tools/
    ├─ README.md
    ├─ context_lint.py
    └─ scripts/

Purpose: 
- Hosts all scripts that maintain repository integrity.

Key Files:

-   `README.md`\
    Documents available tools, usage, and exit codes.

-   `context_lint.py`\
    Primary validation entry point. Performs directory, naming, and
    index checks.

-   `scripts/`\
    Auxiliary utilities (generators, analyzers, helpers).

Rules: - CI must only invoke `context_lint.py`. - No production code
allowed.

------------------------------------------------------------------------

## 4.3 architecture/ --- Product Architecture Layer

    architecture/
    ├─ overview.md
    ├─ backend.md
    ├─ frontend.md
    └─ data-model.md

Purpose: 
- Describes the technical structure of the WMS product.

File Responsibilities:

-   `overview.md`\
    High-level system architecture and major components.

-   `backend.md`\
    Service layout, APIs, persistence, and integrations.

-   `frontend.md`\
    UI structure, data flow, and interaction patterns.

-   `data-model.md`\
    Canonical definition of entities, relations, and constraints.

Rules: - Describes the product, not this context repository. - Must
reflect accepted decisions.

------------------------------------------------------------------------

## 4.4 decisions/ --- Architecture Decision Records

    decisions/
    ├─ README.md
    ├─ adr/
    │  └─ 000X-*.md
    └─ templates/
       └─ TEMPLATE.md

Purpose: 
- Maintains a formal record of technical decisions.

File Responsibilities:

-   `README.md`\
    Defines ADR format, lifecycle, and status semantics.

-   `adr/`\
    Immutable accepted decision records.

-   `templates/`\
    Standard templates for new ADR creation.

Rules: - All significant technical choices must be documented. -
Superseded ADRs must reference replacements.

------------------------------------------------------------------------

## 4.5 status/ --- Project State Tracking

    status/
    ├─ current.md
    ├─ next-actions.md
    ├─ blockers.md
    ├─ roadmap.md
    └─ archive/
       └─ YYYY-QX.md

Purpose: 
- Tracks real-time and strategic project state.

File Responsibilities:

-   `current.md`\
    Current development phase and priorities.

-   `next-actions.md`\
    Short-term actionable tasks.

-   `blockers.md`\
    Active impediments and risks.

-   `roadmap.md`\
    Medium and long-term objectives.

-   `archive/`\
    Historical status snapshots.

Rules: - Root files reflect current reality only. - Obsolete information
must be archived.

------------------------------------------------------------------------

## 4.6 workflows/ --- Operational Playbooks

    workflows/
    ├─ setup/
    ├─ dev/
    ├─ test/
    └─ release/

Purpose: 
- Provides reproducible procedures.

Subdirectories:

-   `setup/`\
    Environment initialization.

-   `dev/`\
    Daily development routines.

-   `test/`\
    Testing procedures.

-   `release/`\
    Release and delivery workflows.

Rules: - All procedures must be executable as written. - Avoid
speculative instructions.

------------------------------------------------------------------------

## 4.7 verify/ --- Manual Verification Records

    verify/
    ├─ README.md
    └─ YYYY/
       └─ YYYY-MM-DD-<slug>.md

Purpose: 
- Records evidence of manual validation.

File Responsibilities:

-   `README.md`\
    Verification format and triggers.

-   `YYYY/`\
    Year-based validation logs.

Rules: - Each file documents one real validation session. - Must include
local time and environment context.

------------------------------------------------------------------------

## 4.8 conversations/ --- Reasoning and Discussion Archive

    conversations/
    ├─ README.md
    ├─ index.md
    ├─ by-date/
    │  └─ YYYY/
    │     └─ YYYY-MM.md
    ├─ entries/
    │  ├─ TEMPLATE.md
    │  └─ YYYY/
    │     └─ YYYY-MM-DD-*.md
    └─ topics/
       ├─ index.md
       └─ *.md

Purpose: 
- Preserves the project's reasoning history.

File Responsibilities:

-   `README.md`\
    Recording rules and lifecycle.

-   `index.md`\
    Main navigation entry.

-   `by-date/`\
    Chronological indexes.

-   `entries/`\
    Append-only discussion records.

-   `entries/TEMPLATE.md`\
    Standard entry format.

-   `topics/`\
    Semantic classification.

Rules: - Entries are append-only with same-day update exceptions. -
Indexes must be synchronized.

------------------------------------------------------------------------

# 5. Standard Operating Workflow

1.  Review `status/current.md`.
2.  Consult relevant ADRs.
3.  Follow workflows.
4.  Implement in main WMS repo.
5.  Perform manual validation.
6.  Record results in `verify/`.
7.  Capture key reasoning in `conversations/`.

------------------------------------------------------------------------

# 6. Governance and Maintenance Rules

-   This README is the authoritative specification.
-   Directory boundaries must not be violated.
-   Historical records are immutable.
-   Structural violations are treated as defects.
-   Automated linting is mandatory.

------------------------------------------------------------------------

# 7. Long-Term Objective

To maintain a comprehensive, reliable, and machine-readable knowledge
base supporting long-term AI-human collaboration.
