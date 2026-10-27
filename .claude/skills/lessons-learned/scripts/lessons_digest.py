#!/usr/bin/env python3
"""Role-filtered lessons digest — what one agent needs from lessons.md, and nothing else.

WHY THIS EXISTS
  lessons.md is ~12K tokens and grows with every run. Every agent used to read all of it, and
  most of that text is the *Why* and *Origin* of each lesson — the incident narrative that
  justified the rule to the human who approved it. An agent applying the rule needs the Trigger
  and the Rule; the narrative stays in lessons.md (and in evolution-log.md) for whoever asks
  why a rule exists. A writer also has no use for the retriever's PMID protocol.

  This replaces the lessons-curator's "inject" pass: an LLM reading the whole store in order to
  decide which lessons are relevant is a mechanical filter, so it moves into a script (L-039).
  Filtering by the lesson's own Role tag is deterministic, cannot drop a lesson by judgement, and
  costs no agent spin-up.

WHAT IT DOES
  Parses every `### L-NNN:` block in lessons.md and prints, for each lesson whose `Role:` line
  names the requested role (or one of its aliases), the title + Trigger + Rule. `--full` adds
  Why/Origin back. Lesson order and wording are preserved verbatim.

WHAT IT DOES NOT DO
  It does not judge relevance to the topic, summarise, or rewrite a rule. A lesson tagged for a
  role is always printed for that role. Mis-tagged lessons are a lessons.md problem — fix the tag.

Python stdlib only; no network; same input -> identical output.

  python3 .claude/skills/lessons-learned/scripts/lessons_digest.py --role synthesis-writer
  python3 .claude/skills/lessons-learned/scripts/lessons_digest.py --list-roles
"""
import argparse
import re
import sys
from pathlib import Path

DEFAULT_STORE = Path(__file__).resolve().parents[1] / "lessons.md"

# Canonical role -> words that mean that role in a lesson's free-text `Role:` line.
# Matched as whole words, so "synthesis-writer" matches `writer` and "(lead)" matches `lead`.
ROLES = {
    # The lead writes the protocol (Phase 1) since the strategist agent was folded into it, so
    # lessons still tagged `strategist` route to the lead rather than to an agent that never runs.
    "orchestrator": ("orchestrator", "lead", "strategist"),
    "evidence-retriever": ("retriever",),
    "critical-appraiser": ("appraiser",),
    "synthesis-writer": ("writer",),
    "quality-coach": ("coach",),
    "citation-verifier": ("verifier",),
    "lessons-curator": ("curator",),
}

HEADER_RE = re.compile(r"^### (L-\d{3}): (.+)$")
FIELD_RE = re.compile(r"^- \*\*(Role|Trigger|Rule|Why|Origin):\*\*\s?(.*)$")
BRIEF_FIELDS = ("Trigger", "Rule")
FULL_FIELDS = ("Trigger", "Rule", "Why", "Origin")


def parse(text):
    """Return [{'id', 'title', 'Role', 'Trigger', 'Rule', 'Why', 'Origin'}] in file order."""
    lessons, cur, field = [], None, None
    for line in text.splitlines():
        m = HEADER_RE.match(line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2).strip()}
            lessons.append(cur)
            field = None
            continue
        if cur is None:
            continue
        if line.startswith("## ") or line.strip() == "---":   # a section break ends a lesson
            cur, field = None, None
            continue
        f = FIELD_RE.match(line)
        if f:
            field = f.group(1)
            cur[field] = f.group(2).rstrip()
        elif field and line.strip():
            cur[field] += "\n" + line.rstrip()
    return lessons


def role_matches(role_line, role):
    words = ROLES[role]
    return any(re.search(rf"(?<![\w]){re.escape(w)}(?![\w])", role_line, re.IGNORECASE)
               for w in words)


def select(lessons, role):
    return [l for l in lessons if role_matches(l.get("Role", ""), role)]


def render(selected, role, full=False, total=None):
    fields = FULL_FIELDS if full else BRIEF_FIELDS
    out = [f"# Lessons for `{role}` — {len(selected)} of {total} "
           f"({'full' if full else 'Trigger + Rule only; Why/Origin in lessons.md'})", ""]
    if not selected:
        out.append("(none)")
    for l in selected:
        out.append(f"### {l['id']}: {l['title']}")
        for f in fields:
            if l.get(f):
                sep = "" if l[f].startswith("\n") else " "
                out.append(f"- **{f}:**{sep}{l[f]}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--role", choices=sorted(ROLES))
    ap.add_argument("--store", default=str(DEFAULT_STORE))
    ap.add_argument("--full", action="store_true", help="include Why and Origin")
    ap.add_argument("--list-roles", action="store_true", help="count lessons per role and exit")
    args = ap.parse_args(argv)

    lessons = parse(Path(args.store).read_text(encoding="utf-8"))
    if not lessons:
        print(f"no `### L-NNN:` lessons parsed from {args.store}", file=sys.stderr)
        return 1

    if args.list_roles:
        for role in sorted(ROLES):
            print(f"{role:20} {len(select(lessons, role))}")
        untagged = [l["id"] for l in lessons if not any(role_matches(l.get("Role", ""), r) for r in ROLES)]
        print(f"{'(no role matched)':20} {len(untagged)} {' '.join(untagged)}")
        return 0

    if not args.role:
        ap.error("--role is required (or --list-roles)")
    sys.stdout.write(render(select(lessons, args.role), args.role, args.full, len(lessons)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
