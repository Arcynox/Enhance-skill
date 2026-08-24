#!/usr/bin/env python3
"""Validate skills structure and SKILL.md frontmatter.

Checks per skills/<name>/SKILL.md:
  - frontmatter block exists and parses (name, description keys)
  - name is kebab-case and matches the parent directory
  - description >= 40 chars
  - code fences are balanced
  - EVALS.md exists next to SKILL.md
  - no known typos ("enchance")

Run locally: python3 .github/scripts/validate_skills.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MIN_DESC_LEN = 40


def fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def parse_frontmatter(text: str, errors: list[str], label: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail(errors, f"{label}: missing frontmatter opening '---'")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        fail(errors, f"{label}: frontmatter not closed")
        return {}

    meta: dict[str, str] = {}
    current_key: str | None = None
    for line in lines[1:end]:
        if not line.strip() or line.strip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            current_key = m.group(1)
            meta[current_key] = m.group(2).strip()
        elif line[:1] in (" ", "\t") and current_key:
            meta[current_key] += " " + line.strip()
        else:
            fail(errors, f"{label}: unparseable frontmatter line: {line!r}")

    for key in ("name", "description"):
        if key not in meta or not meta[key]:
            fail(errors, f"{label}: frontmatter missing '{key}'")
            del meta[key]
    return meta


def validate_skill(skill_dir: Path, errors: list[str]) -> None:
    label = skill_dir.name
    if not KEBAB.match(label):
        fail(errors, f"{label}: directory name is not kebab-case")

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        fail(errors, f"{label}: missing SKILL.md")
        return

    text = skill_md.read_text(encoding="utf-8")
    meta = parse_frontmatter(text, errors, f"{label}/SKILL.md")

    if "name" in meta:
        if not KEBAB.match(meta["name"]):
            fail(errors, f"{label}: name '{meta['name']}' is not kebab-case")
        elif meta["name"] != label:
            fail(errors, f"{label}: name '{meta['name']}' does not match directory")

    if "description" in meta and len(meta["description"]) < MIN_DESC_LEN:
        fail(
            errors,
            f"{label}: description too short ({len(meta['description'])} chars, min {MIN_DESC_LEN})",
        )

    fences = sum(1 for line in text.splitlines() if line.lstrip().startswith("```"))
    if fences % 2 != 0:
        fail(errors, f"{label}/SKILL.md: unbalanced code fences ({fences})")

    if not (skill_dir / "EVALS.md").is_file():
        fail(errors, f"{label}: missing EVALS.md")

    if "enchance" in text.lower():
        fail(errors, f"{label}/SKILL.md: contains typo 'enchance'")


def main() -> int:
    errors: list[str] = []
    if not SKILLS_DIR.is_dir():
        print(f"error: {SKILLS_DIR} not found", file=sys.stderr)
        return 1

    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if not skill_dirs:
        fail(errors, "no skill directories found under skills/")

    for skill_dir in skill_dirs:
        validate_skill(skill_dir, errors)

    if errors:
        print("FAILED:\n" + "\n".join(f"  - {e}" for e in errors))
        return 1

    print(f"OK: {len(skill_dirs)} skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
