# Verify --- Manual Verification Records

This directory contains **manual verification records** that capture
*exactly what was run*, *why each step was necessary*, and *what the
outcome was*.

All verification documents in this directory **must follow the same
level of detail and structure** as the canonical reference:

-   `2026-02-13-ubuntu-manual-testing.md`

This file is the **gold standard** for verify documents.

------------------------------------------------------------------------

## Purpose

Verify records exist to answer, unambiguously:

-   When verification happened
-   In what environment
-   What exact commands were executed
-   What each command does
-   Why each step matters
-   What the result was

They are **not plans** and **not summaries** --- they are factual
execution records.

------------------------------------------------------------------------

## Directory Structure

``` text
verify/
├─ README.md
└─ YYYY/
   └─ YYYY-MM-DD-<slug>.md
```

------------------------------------------------------------------------

## Naming Convention (Required)

All verify files **must** be named:

    YYYY-MM-DD-<slug>.md

Example:

    2026-02-13-ubuntu-manual-testing.md

-   Date uses **local Los Angeles time**
-   `<slug>` is kebab-case and descriptive
-   No version numbers, no prefixes

------------------------------------------------------------------------

## Required Header Fields

Each verify file **must begin** with the following header block:

``` text
Verified At: YYYY-MM-DD HH:MM PST/PDT
Environment: OS / Runtime / Toolchain
Scope: What was verified
```

------------------------------------------------------------------------

## Step Documentation Standard (MANDATORY)

All steps must match the depth and structure of
`2026-02-13-ubuntu-manual-testing.md`.

Each step must include: - Command - What this step does - Why it
matters - Expected result (if applicable)

------------------------------------------------------------------------

## Verify Document Template

``` md
# Verification — <Short Title>

Verified At: YYYY-MM-DD HH:MM PST/PDT
Environment: <OS / Runtime / Toolchain>
Scope: <What was verified>

---

## Purpose

## Assumptions

## Step 1 — <Title>

### Command
```bash
<exact command>
```

### What this step does

### Why it matters

### Expected result

------------------------------------------------------------------------

(Repeat for all steps)

------------------------------------------------------------------------

## Results

## Issues / Notes

## Conclusion

## Related

\`\`\`

------------------------------------------------------------------------

## Governance

Verify records are historical evidence. Accuracy and reproducibility
come first.
