#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Context repository linter (PR gate).

Checks:
- Required directories/files exist
- Naming conventions
- Index synchronization:
  - every conversations/entries/YYYY/YYYY-MM-DD-*.md must appear in conversations/by-date/YYYY/YYYY-MM.md
  - every conversations/topics/*.md (except index.md) must appear in conversations/topics/index.md
- README "NOT the WMS product" notice exists (recommended guardrail)

Exit code:
- 0 pass
- 1 fail
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRS = [
    "architecture",
    "decisions",
    "status",
    "workflows",
    "verify",
    "conversations",
]

REQUIRED_CONV_ITEMS = [
    "conversations/README.md",
    "conversations/index.md",
    "conversations/by-date",
    "conversations/entries",
    "conversations/topics",
    "conversations/topics/index.md",
]

DECISION_RE = re.compile(r"^decisions/\d{4}-[a-z0-9].*\.md$")
ENTRY_RE = re.compile(r"^conversations/entries/(\d{4})/(\d{4})-(\d{2})-(\d{2})-[^/]+\.md$")
BYDATE_RE = re.compile(r"^conversations/by-date/(\d{4})/(\d{4})-(\d{2})\.md$")

README_GUARD_PHRASE = "NOT the Warehouse Management System (WMS) product"


def fail(errors: list[str]) -> int:
    for e in errors:
        print(f"[FAIL] {e}")
    return 1


def ok(msg: str) -> None:
    print(f"[OK] {msg}")


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # fallback
        return p.read_text(errors="replace")


def iter_md_files(root: Path) -> Iterable[Path]:
    for p in root.rglob("*.md"):
        if p.is_file():
            yield p


def normalize_rel(p: Path) -> str:
    return str(p.relative_to(REPO_ROOT)).replace("\\", "/")


def main() -> int:
    errors: list[str] = []

    # 1) required dirs
    for d in REQUIRED_DIRS:
        if not (REPO_ROOT / d).exists():
            errors.append(f"Missing required directory: {d}")
    # required conversation structure
    for item in REQUIRED_CONV_ITEMS:
        if not (REPO_ROOT / item).exists():
            errors.append(f"Missing required conversations item: {item}")

    # 2) naming conventions
    # decisions
    decisions_dir = REPO_ROOT / "decisions"
    if decisions_dir.exists():
        for p in decisions_dir.glob("*.md"):
            rel = normalize_rel(p)
            if not DECISION_RE.match(rel):
                errors.append(
                    f"Invalid ADR filename: {rel} (expected decisions/000X-*.md)"
                )

    # entries: enforce yyyy folder + yyyy-mm-dd prefix
    entries_dir = REPO_ROOT / "conversations" / "entries"
    entry_paths: list[tuple[str, str, str]] = []  # (rel, yyyy, yyyy-mm)
    if entries_dir.exists():
        for p in iter_md_files(entries_dir):
            rel = normalize_rel(p)
            m = ENTRY_RE.match(rel)
            if not m:
                errors.append(
                    f"Invalid entry filename: {rel} "
                    f"(expected conversations/entries/YYYY/YYYY-MM-DD-*.md)"
                )
                continue
            yyyy = m.group(1)
            yyyy_mm = f"{m.group(2)}-{m.group(3)}"
            entry_paths.append((rel, yyyy, yyyy_mm))

    # by-date indexes existence + naming
    bydate_dir = REPO_ROOT / "conversations" / "by-date"
    bydate_index_files: set[str] = set()
    if bydate_dir.exists():
        for p in iter_md_files(bydate_dir):
            rel = normalize_rel(p)
            if not BYDATE_RE.match(rel):
                errors.append(
                    f"Invalid by-date index filename: {rel} "
                    f"(expected conversations/by-date/YYYY/YYYY-MM.md)"
                )
            else:
                bydate_index_files.add(rel)

    # 3) index synchronization: entries must appear in monthly by-date index
    # Build map YYYY-MM -> set(entries)
    entries_by_month: dict[tuple[str, str], list[str]] = {}
    for rel, yyyy, yyyy_mm in entry_paths:
        entries_by_month.setdefault((yyyy, yyyy_mm), []).append(rel)

    for (yyyy, yyyy_mm), rel_entries in sorted(entries_by_month.items()):
        idx_rel = f"conversations/by-date/{yyyy}/{yyyy_mm}.md"
        idx_path = REPO_ROOT / idx_rel
        if not idx_path.exists():
            errors.append(
                f"Missing monthly by-date index: {idx_rel} "
                f"(needed for entries in {yyyy_mm})"
            )
            continue

        idx_text = read_text(idx_path)
        # Require each entry filename (basename) to appear in the index text.
        for entry_rel in sorted(rel_entries):
            basename = Path(entry_rel).name
            if basename not in idx_text:
                errors.append(
                    f"Entry not indexed in {idx_rel}: missing reference to {basename}"
                )

    # 4) topics index synchronization
    topics_dir = REPO_ROOT / "conversations" / "topics"
    topics_index = topics_dir / "index.md"
    if topics_dir.exists() and topics_index.exists():
        idx_text = read_text(topics_index)
        for p in topics_dir.glob("*.md"):
            if p.name == "index.md":
                continue
            # Require the topic filename to appear in topics/index.md
            if p.name not in idx_text:
                errors.append(
                    f"Topic file not listed in conversations/topics/index.md: {p.name}"
                )

    # 5) README guard phrase
    readme = REPO_ROOT / "README.md"
    if readme.exists():
        t = read_text(readme)
        if README_GUARD_PHRASE not in t:
            errors.append(
                f"README.md missing guard phrase: '{README_GUARD_PHRASE}'. "
                f"(Add a clear notice that this repo is not the WMS product.)"
            )
    else:
        errors.append("Missing README.md at repo root")

    if errors:
        return fail(errors)

    ok("Context lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
