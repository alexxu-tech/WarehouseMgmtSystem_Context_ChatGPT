# Context Lint --- Repository Validation Rules

This document describes the validation rules implemented by
`tools/context_lint.py` and executed by GitHub Actions.

The goal of context lint is to enforce structural consistency and
maintain long-term integrity of the context repository, without blocking
normal development.

All checks currently run in warnings-only mode.

------------------------------------------------------------------------

## 1. Execution Model

Context lint runs automatically on:

-   Pull request creation
-   Pull request update
-   Pull request reopen

via:

.github/workflows/context-lint.yml

The workflow is configured with:

continue-on-error: true

Therefore:

-   Findings are reported as warnings
-   Merges are NOT blocked

------------------------------------------------------------------------

## 2. Scope of Validation

Context lint enforces:

-   Layer 1: Repository structure
-   Layer 3: Conversations synchronization

It intentionally does NOT check:

-   File content quality
-   Business logic correctness
-   Verify step completeness
-   Status file semantics

------------------------------------------------------------------------

## 3. Layer 1 --- Structure Validation

### Root Files

README.md\
glossary.md

### Required Directories

.github/\
tools/\
architecture/\
decisions/\
status/\
workflows/\
verify/\
conversations/

### Automation

.github/workflows/context-lint.yml

### Tools

tools/README.md\
tools/context_lint.py\
tools/scripts/

### Architecture

architecture/overview.md\
architecture/backend.md\
architecture/frontend.md\
architecture/data_model.md

### Decisions

decisions/README.md\
decisions/adr/\
decisions/templates/\
decisions/templates/TEMPLATE.md

### Status

status/current.md\
status/next-actions.md\
status/blockers.md\
status/roadmap.md\
status/archive/

### Verify

verify/README.md

### Conversations

conversations/README.md\
conversations/index.md\
conversations/by-date/\
conversations/entries/\
conversations/entries/TEMPLATE.md\
conversations/topics/\
conversations/topics/index.md

------------------------------------------------------------------------

## 4. ADR Numbering Rules

ADR files under decisions/adr/ must follow:

000X-kebab-case.md

Rules:

-   Start at 0001
-   Must be continuous
-   No gaps
-   No duplicates

------------------------------------------------------------------------

## 5. Layer 3 --- Conversations Synchronization

### Entry Discovery

Valid entries:

conversations/entries/YYYY/YYYY-MM-DD-\*.md

Ignored:

index.md\
README.md\
TEMPLATE.md

------------------------------------------------------------------------

### Required References

Each entry must appear in:

1.  conversations/index.md
2.  conversations/by-date/YYYY/YYYY-MM.md
3.  At least one conversations/topics/\*.md

------------------------------------------------------------------------

### Dangling Reference Detection

Indexes are scanned for references to missing entries in:

-   by-date/
-   topics/

------------------------------------------------------------------------

## 6. Ignored Files

index.md\
README.md\
TEMPLATE.md

------------------------------------------------------------------------

## 7. Reporting

Findings are reported via:

-   GitHub Annotations
-   GitHub Step Summary

------------------------------------------------------------------------

## 8. Exit Behavior

Local run:

python tools/context_lint.py

Exit code:

0 = no issues\
1 = warnings

CI does not block merges.

------------------------------------------------------------------------

## 9. Design Philosophy

1.  Warnings over blocking
2.  Structure before semantics
3.  Avoid false positives
4.  Long-term maintainability
5.  Human + AI collaboration

------------------------------------------------------------------------

## 10. Future Extensions

Possible upgrades:

-   Blocking mode
-   Content schema validation
-   Auto-fix tools
-   Per-directory rules
-   Drift detection
