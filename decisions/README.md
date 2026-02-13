# Decisions (ADR)

This directory contains **Architecture Decision Records (ADRs)** for the WMS project.
ADRs capture significant technical decisions so they remain understandable and traceable over time.

---

## Directory Structure

```text
decisions/
├─ README.md
├─ adr/
│  └─ 000X-*.md
└─ templates/
   └─ TEMPLATE.md
```

---

## What belongs here

ADRs should be created when a decision:
- Changes the developer workflow or operating model
- Introduces/removes a major dependency or technology
- Locks in an architectural boundary or data model direction
- Has meaningful trade-offs and long-term consequences
- Would be hard to reconstruct later from code alone

Non-ADR documents:
- Day-to-day progress → `status/`
- How-to procedures → `workflows/`
- Reasoning transcripts → `conversations/`
- Manual validation evidence → `verify/`

---

## ADR lifecycle and statuses

Each ADR must include a `Status` section.

Recommended statuses:
- **Proposed** — drafted but not agreed
- **Accepted** — agreed and considered current
- **Deprecated** — still true historically, but not recommended going forward
- **Superseded** — replaced by a newer ADR (must link to replacement)

Rules:
- Prefer **Superseded** when a newer ADR replaces an older one.
- Deprecated/Superseded ADRs must remain in place (do not delete).

---

## Naming and numbering rules

ADR files must be named:

```
decisions/adr/000X-some-title.md
```

- `000X` is a 4-digit increasing number (no reuse)
- `some-title` is `kebab-case`
- No dates in filenames (dates belong in ADR content)

---

## Required ADR sections

Minimum required sections (see `templates/TEMPLATE.md`):
- Title
- Status
- Date
- Context
- Decision
- Rationale
- Consequences
- Follow-Up Actions

Optional sections:
- Alternatives Considered
- Implementation Notes
- References

---

## How to add a new ADR

1. Copy `decisions/templates/TEMPLATE.md`
2. Create a new file under `decisions/adr/` with the next number
3. Fill required sections
4. If replacing an older ADR, mark the old ADR as **Superseded** and link both ways
