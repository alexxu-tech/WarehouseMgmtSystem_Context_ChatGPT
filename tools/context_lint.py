#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


ENTRY_RE = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)\.md$")
ADR_RE = re.compile(r"^(?P<num>\d{4})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)\.md$")

# Files to ignore in sync checks
IGNORE_NAMES = {"index.md", "README.md", "TEMPLATE.md"}


@dataclass
class Finding:
    level: str  # "warning" | "error"
    code: str
    message: str
    path: Optional[str] = None

    def to_github_annotation(self) -> str:
        loc = f" file={self.path}" if self.path else ""
        return f"::{self.level}{loc}::{self.code}: {self.message}"


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def exists(p: Path, findings: List[Finding], code: str, desc: str) -> None:
    if not p.exists():
        findings.append(Finding("warning", code, f"Missing required {desc}.", str(p.as_posix())))


def contains_ref(text: str, needle: str) -> bool:
    return needle in text


def check_structure(repo: Path) -> List[Finding]:
    f: List[Finding] = []

    # Root
    exists(repo / "README.md", f, "ROOT_README", "file README.md")
    exists(repo / "glossary.md", f, "ROOT_GLOSSARY", "file glossary.md")

    # Top-level dirs
    for d in [".github", "tools", "architecture", "decisions", "status", "workflows", "verify", "conversations"]:
        exists(repo / d, f, "ROOT_DIR", f"directory {d}")

    # .github/workflows/context-lint.yml
    exists(repo / ".github" / "workflows" / "context-lint.yml", f, "GHA_WORKFLOW", "workflow .github/workflows/context-lint.yml")

    # tools
    exists(repo / "tools" / "README.md", f, "TOOLS_README", "file tools/README.md")
    exists(repo / "tools" / "context_lint.py", f, "TOOLS_LINT", "file tools/context_lint.py")
    exists(repo / "tools" / "scripts", f, "TOOLS_SCRIPTS_DIR", "directory tools/scripts")

    # architecture
    for fn in ["overview.md", "backend.md", "frontend.md", "data_model.md"]:
        exists(repo / "architecture" / fn, f, "ARCH_FILE", f"file architecture/{fn}")

    # decisions
    exists(repo / "decisions" / "README.md", f, "DEC_README", "file decisions/README.md")
    exists(repo / "decisions" / "adr", f, "DEC_ADR_DIR", "directory decisions/adr")
    exists(repo / "decisions" / "templates", f, "DEC_TPL_DIR", "directory decisions/templates")
    exists(repo / "decisions" / "templates" / "TEMPLATE.md", f, "DEC_TPL_FILE", "file decisions/templates/TEMPLATE.md")

    # status
    for fn in ["current.md", "next-actions.md", "blockers.md", "roadmap.md"]:
        exists(repo / "status" / fn, f, "STATUS_FILE", f"file status/{fn}")
    exists(repo / "status" / "archive", f, "STATUS_ARCHIVE_DIR", "directory status/archive")

    # verify
    exists(repo / "verify" / "README.md", f, "VERIFY_README", "file verify/README.md")

    # conversations
    conv = repo / "conversations"
    exists(conv / "README.md", f, "CONV_README", "file conversations/README.md")
    exists(conv / "index.md", f, "CONV_INDEX", "file conversations/index.md")
    exists(conv / "by-date", f, "CONV_BY_DATE_DIR", "directory conversations/by-date")
    exists(conv / "entries", f, "CONV_ENTRIES_DIR", "directory conversations/entries")
    exists(conv / "entries" / "TEMPLATE.md", f, "CONV_ENTRY_TEMPLATE", "file conversations/entries/TEMPLATE.md")
    exists(conv / "topics", f, "CONV_TOPICS_DIR", "directory conversations/topics")
    exists(conv / "topics" / "index.md", f, "CONV_TOPICS_INDEX", "file conversations/topics/index.md")

    return f


def check_adr_numbering(repo: Path) -> List[Finding]:
    f: List[Finding] = []
    adr_dir = repo / "decisions" / "adr"
    if not adr_dir.exists():
        return f

    adrs = sorted([p for p in adr_dir.iterdir() if p.is_file() and p.suffix == ".md"])
    nums: List[int] = []

    for p in adrs:
        m = ADR_RE.match(p.name)
        if not m:
            f.append(Finding("warning", "ADR_NAME", "ADR filename must be '000X-kebab-case.md'.", str(p.as_posix())))
            continue
        nums.append(int(m.group("num")))

    if not nums:
        f.append(Finding("warning", "ADR_EMPTY", "No ADRs found in decisions/adr/.", str(adr_dir.as_posix())))
        return f

    nums_sorted = sorted(nums)
    if nums_sorted[0] != 1:
        f.append(Finding("warning", "ADR_START", f"ADR numbering should start at 0001, found {nums_sorted[0]:04d}.", str(adr_dir.as_posix())))

    expected = list(range(nums_sorted[0], nums_sorted[0] + len(nums_sorted)))
    if nums_sorted != expected:
        missing = sorted(set(expected) - set(nums_sorted))
        dupes = [n for n in nums_sorted if nums_sorted.count(n) > 1]
        msg = "ADR numbering must be continuous (no gaps)."
        details = []
        if missing:
            details.append("missing=" + ",".join(f"{n:04d}" for n in missing))
        if dupes:
            details.append("duplicates=" + ",".join(f"{n:04d}" for n in sorted(set(dupes))))
        if details:
            msg += " (" + "; ".join(details) + ")"
        f.append(Finding("warning", "ADR_CONTINUOUS", msg, str(adr_dir.as_posix())))

    return f


def gather_entries(repo: Path) -> List[Path]:
    entries_dir = repo / "conversations" / "entries"
    if not entries_dir.exists():
        return []
    entries: List[Path] = []
    for p in entries_dir.rglob("*.md"):
        if not p.is_file():
            continue
        if p.name in IGNORE_NAMES:
            continue
        if ENTRY_RE.match(p.name):
            entries.append(p)
    return sorted(entries)


def check_conversations_sync(repo: Path) -> List[Finding]:
    f: List[Finding] = []
    conv = repo / "conversations"
    index_p = conv / "index.md"
    topics_index_p = conv / "topics" / "index.md"

    entries = gather_entries(repo)
    if not entries:
        return f

    index_text = read_text(index_p) if index_p.exists() else ""
    topics_index_text = read_text(topics_index_p) if topics_index_p.exists() else ""

    topics_dir = conv / "topics"
    topic_files = []
    if topics_dir.exists():
        topic_files = sorted([p for p in topics_dir.glob("*.md")
                              if p.is_file() and p.name not in IGNORE_NAMES])

    topic_texts = {p: read_text(p) for p in topic_files}

    # Validate topics/index.md references exist
    if topics_index_p.exists():
        for ref in re.findall(r"(?:\(|\s)([A-Za-z0-9_\-./]+\.md)", topics_index_text):
            name = Path(ref).name
            if name in IGNORE_NAMES:
                continue
            if "/topics/" in ref or ref.startswith("topics/") or ref.startswith("conversations/topics/"):
                tp = topics_dir / name
                if not tp.exists():
                    f.append(Finding("warning", "TOPIC_REF", "topics/index.md references a missing topic file.", str(tp.as_posix())))

    for e in entries:
        m = ENTRY_RE.match(e.name)
        assert m
        yyyy, mm, _ = m.group("date").split("-")
        month_index = conv / "by-date" / yyyy / f"{yyyy}-{mm}.md"

        # by-date month index
        if not month_index.exists():
            f.append(Finding("warning", "BYDATE_MISSING", f"Missing by-date month index for entry {e.name}.", str(month_index.as_posix())))
        else:
            txt = read_text(month_index)
            if not contains_ref(txt, e.name):
                f.append(Finding("warning", "BYDATE_SYNC", f"Entry {e.name} not referenced in {month_index.name}.", str(month_index.as_posix())))

        # conversations/index.md
        if index_p.exists() and not contains_ref(index_text, e.name):
            f.append(Finding("warning", "CONV_INDEX_SYNC", f"Entry {e.name} not referenced in conversations/index.md.", str(index_p.as_posix())))

        # topics/*.md
        in_any_topic = any(contains_ref(txt, e.name) for txt in topic_texts.values())
        if not in_any_topic:
            f.append(Finding("warning", "TOPIC_SYNC", f"Entry {e.name} not referenced in any conversations/topics/*.md.", str(topics_dir.as_posix())))

    # Dangling refs in by-date
    by_date_dir = conv / "by-date"
    if by_date_dir.exists():
        for p in by_date_dir.rglob("*.md"):
            if not p.is_file():
                continue
            txt = read_text(p)
            for ref in re.findall(r"(\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md)", txt):
                if ref in IGNORE_NAMES:
                    continue
                yyyy = ref[:4]
                expected = conv / "entries" / yyyy / ref
                if not expected.exists():
                    f.append(Finding("warning", "BYDATE_DANGLING", f"By-date index references missing entry {ref}.", str(p.as_posix())))

    # Dangling refs in topics
    for tp, ttxt in topic_texts.items():
        for ref in re.findall(r"(\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md)", ttxt):
            if ref in IGNORE_NAMES:
                continue
            yyyy = ref[:4]
            expected = conv / "entries" / yyyy / ref
            if not expected.exists():
                f.append(Finding("warning", "TOPIC_DANGLING", f"Topic references missing entry {ref}.", str(tp.as_posix())))

    return f


def write_step_summary(findings: List[Finding]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines: List[str] = []
    lines.append("# Context Lint Summary")
    if not findings:
        lines.append("✅ No issues found.")
    else:
        lines.append(f"⚠️ {len(findings)} issue(s) found (warnings only).")
        lines.append("")
        lines.append("| Level | Code | Path | Message |")
        lines.append("|---|---|---|---|")
        for x in findings:
            path = x.path or ""
            msg = x.message.replace("\n", " ")
            lines.append(f"| {x.level} | {x.code} | `{path}` | {msg} |")
    Path(summary_path).write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Context repository linter (Layer 1 + Layer 3).")
    ap.add_argument("--repo", default=".", help="Path to repo root (default: current directory).")
    ap.add_argument("--github", action="store_true", help="Emit GitHub Actions annotations and step summary.")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()

    findings: List[Finding] = []
    findings.extend(check_structure(repo))
    findings.extend(check_adr_numbering(repo))
    findings.extend(check_conversations_sync(repo))

    if args.github:
        for x in findings:
            print(x.to_github_annotation())

    write_step_summary(findings)

    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
