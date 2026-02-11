# Conversations

## Purpose
This directory contains curated summaries of important human–AI and human–human discussions related to the Warehouse Management System (WMS) project. It preserves **context, decisions, and reasoning** without storing raw chat logs.

## Structure (Index-First, Scalable)
This directory is organized so you can find conversations in two ways:

1) **By date** (timeline)
- Monthly index files live under: `conversations/by-date/YYYY/YYYY-MM.md`

2) **By topic** (subject-based)
- Topic index files live under: `conversations/topics/<topic>.md`
- The topic catalog lives at: `conversations/topics/index.md`

3) **Full entries** (the actual summaries)
- Full conversation summaries live under: `conversations/entries/YYYY/YYYY-MM-DD-topic.md`

`conversations/index.md` is the short entry-point linking to the latest month indexes and topic indexes.

## What Belongs Here
Each entry should capture:
- Context
- Key Questions
- Decisions / Conclusions
- Rationale
- Follow-ups

## What Does NOT Belong Here
- Raw transcripts
- Step-by-step debugging logs
- Temporary questions without lasting value

## File Naming Convention
Entries must follow:
`YYYY-MM-DD-topic.md`

### Same-day merge rule (recommended)
If an entry for the same **date + topic** already exists, append to it rather than creating a new file.

## Relationship to Other Docs
- Final decisions → `decisions/` (ADR files)
- Architecture changes → `architecture/`
- Dev workflows → `workflows/`

## Guiding Principle
If a future contributor (or AI assistant) can read an entry and quickly understand what mattered without the original chat, it’s written correctly.
