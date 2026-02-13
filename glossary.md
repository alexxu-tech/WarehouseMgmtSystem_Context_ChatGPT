# Project Glossary

This glossary defines key terms used in the
WarehouseMgmtSystem_Context_ChatGPT repository.

------------------------------------------------------------------------

## WMS

Warehouse Management System. The main product project hosted at:
https://github.com/alexxu-tech/WarehouseMgmtSystem

------------------------------------------------------------------------

## Context Repository

The WarehouseMgmtSystem_Context_ChatGPT repository. A structured
knowledge base that preserves long-term project memory, reasoning
history, and operational context.

------------------------------------------------------------------------

## ADR (Architecture Decision Record)

A formal document that records a significant technical decision. Stored
under `decisions/adr/` and maintained as immutable records.

------------------------------------------------------------------------

## Entry

A single conversation record stored under `conversations/entries/`.
Entries preserve technical discussions, reasoning, and conclusions.

------------------------------------------------------------------------

## Conversation Index

A navigational document under `conversations/index.md` and
`conversations/by-date/` that links and organizes entries.

------------------------------------------------------------------------

## Verify Record

A manual validation document stored under `verify/YYYY/`. Each file
records one real verification session.

------------------------------------------------------------------------

## Workflow

A reproducible operational or development procedure documented under
`workflows/`.

------------------------------------------------------------------------

## Context Lint

The automated validation system implemented by `tools/context_lint.py`
and executed via GitHub Actions. It enforces repository structure and
consistency rules.

------------------------------------------------------------------------

## Dev-Up / Dev-Down

The local development environment lifecycle defined in ADR-0001,
including startup and teardown procedures.

------------------------------------------------------------------------

## Append-Only Rule

A governance rule stating that historical records must not be rewritten,
except for same-day updates to active conversation entries.

------------------------------------------------------------------------

## By-Date Index

Chronological index files under `conversations/by-date/` that organize
entries by year and month.

------------------------------------------------------------------------

## Topic Index

Semantic classification files under `conversations/topics/` used to
group related conversation entries.

------------------------------------------------------------------------

## Validation Session

A real-world manual testing activity whose results are documented in a
verify record.

------------------------------------------------------------------------

## Standard Operating Workflow

The recommended sequence of activities defined in README, covering
status review, decision review, implementation, verification, and
documentation.

------------------------------------------------------------------------

## Governance Rules

The set of structural and behavioral constraints defined in README and
enforced by context lint.
