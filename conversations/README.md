# Conversations

## Purpose
This directory contains curated summaries of important human--AI and human--human discussions related to the Warehouse Management System (WMS) project. It exists to preserve **context, decisions, and reasoning** without storing raw chat logs.

This allows future readers (including AI tools) to quickly understand *what was discussed* and *what was decided*.

------------------------------------------------------------------------

## What Belongs Here
Documents in this directory should capture:
- High-level context of the discussion
- Key questions or problems raised
- Final conclusions or decisions
- Important trade-offs or constraints identified
- Follow-up actions or next steps

Each file should represent a **summarized outcome**, not a transcript.

------------------------------------------------------------------------

## What Does NOT Belong Here
The following should not be stored:
- Raw chat transcripts
- Copy-pasted conversation logs
- Step-by-step debugging messages
- Temporary questions without lasting value

This directory is intentionally kept concise and readable.

------------------------------------------------------------------------

## File Naming Convention
Use a date-based and topic-based naming scheme:

YYYY-MM-DD-topic.md

Examples:
- 2026-02-09-dev-environment-setup.md
- 2026-02-09-dev-up-dev-down-design.md
- 2026-02-10-auth-strategy-discussion.md

------------------------------------------------------------------------

## Recommended Document Structure
Each conversation summary should follow this structure:

### Context
Why the discussion happened.

### Key Questions
What problems or uncertainties were explored.

### Decisions / Conclusions
What was ultimately decided or clarified.

### Rationale
Why those decisions were made.

### Follow-ups
Any future work implied by the discussion.

------------------------------------------------------------------------

## Relationship to Other Docs
- Final decisions should be captured in `decisions/` (ADR files)
- Architecture implications should be reflected in `architecture/`
- Development workflows belong in `workflows/`

This directory acts as a bridge between raw discussion and formal documentation.

------------------------------------------------------------------------

## Guiding Principle
If a future contributor (or AI assistant) can read a file in this directory and quickly understand *what mattered* without reading the original conversation, then the document is written correctly.
