"""Role-filtered lessons digest — replaces every agent reading all of lessons.md.

The guarantee that matters is that filtering can only ever save tokens, never lose a rule:
every lesson in the real store is parsed, every lesson reaches at least one role, and a rule's
text arrives verbatim — nested bullets included.
"""
import re
import unittest

from harness import AGENTS, SKILLS, load

M = load("lessons-learned/scripts/lessons_digest.py")
STORE = SKILLS / "lessons-learned" / "lessons.md"

SAMPLE = """# Lessons

### L-001: Cite everything
- **Role:** synthesis-writer
- **Trigger:** writing a claim
- **Rule:** Map it to a record.
  1. nested step kept verbatim
- **Why:** a long incident narrative
- **Origin:** Entry #1

### L-002: Probe counts first
- **Role:** retriever (and the lead)
- **Trigger:** before a pull
- **Rule:** Ask for the total.
- **Why:** recall
- **Origin:** Entry #2

### L-003: Not a writer lesson
- **Role:** rewriter-of-titles
- **Trigger:** x
- **Rule:** y

---
## Appendix
Text after a section break belongs to no lesson.
"""


class RealStore(unittest.TestCase):
    def setUp(self):
        self.text = STORE.read_text(encoding="utf-8")
        self.lessons = M.parse(self.text)

    def test_every_header_is_parsed(self):
        headers = re.findall(r"^### (L-\d{3}):", self.text, re.MULTILINE)
        self.assertEqual([l["id"] for l in self.lessons], headers)

    def test_every_lesson_has_a_rule_and_a_role(self):
        for l in self.lessons:
            with self.subTest(lesson=l["id"]):
                self.assertTrue(l.get("Rule"), "lesson with no Rule would inject nothing")
                self.assertTrue(l.get("Role"), "lesson with no Role reaches no agent")

    def test_no_lesson_is_orphaned(self):
        """A lesson no role matches is never injected — filtering would silently drop it."""
        orphans = [l["id"] for l in self.lessons
                   if not any(M.role_matches(l["Role"], r) for r in M.ROLES)]
        self.assertEqual(orphans, [], f"lessons whose Role names no known agent: {orphans}")

    def test_every_agent_has_a_role(self):
        """Each agent is told to run the digest for its own name, so the name must be a choice."""
        agents = {p.stem for p in AGENTS.glob("*.md")}
        self.assertEqual(agents - set(M.ROLES), set())

    def test_no_role_for_an_agent_that_does_not_exist(self):
        """A role key with no agent file routes its lessons to nobody. When the strategist was
        folded into the lead, its lessons had to move to `orchestrator` or they would be lost."""
        agents = {p.stem for p in AGENTS.glob("*.md")}
        self.assertEqual(set(M.ROLES) - agents - {"orchestrator"}, set())

    def test_digest_is_smaller_than_the_store(self):
        for role in M.ROLES:
            with self.subTest(role=role):
                out = M.render(M.select(self.lessons, role), role, total=len(self.lessons))
                self.assertLess(len(out), len(self.text) // 2)


class Filtering(unittest.TestCase):
    def setUp(self):
        self.lessons = M.parse(SAMPLE)

    def ids(self, role):
        return [l["id"] for l in M.select(self.lessons, role)]

    def test_role_filter(self):
        self.assertEqual(self.ids("synthesis-writer"), ["L-001"])
        self.assertEqual(self.ids("evidence-retriever"), ["L-002"])

    def test_alias_lead_reaches_orchestrator(self):
        self.assertIn("L-002", self.ids("orchestrator"))

    def test_whole_word_match_only(self):
        """'rewriter-of-titles' contains 'writer' but is not the writer role."""
        self.assertNotIn("L-003", self.ids("synthesis-writer"))

    def test_brief_drops_why_full_keeps_it(self):
        sel = M.select(self.lessons, "synthesis-writer")
        brief = M.render(sel, "synthesis-writer", total=3)
        full = M.render(sel, "synthesis-writer", full=True, total=3)
        self.assertNotIn("incident narrative", brief)
        self.assertIn("incident narrative", full)
        self.assertIn("Entry #1", full)

    def test_nested_rule_lines_kept_verbatim(self):
        out = M.render(M.select(self.lessons, "synthesis-writer"), "synthesis-writer", total=3)
        self.assertIn("  1. nested step kept verbatim", out)

    def test_section_break_ends_the_last_lesson(self):
        last = M.parse(SAMPLE)[-1]
        self.assertNotIn("Appendix", last["Rule"])
        self.assertNotIn("belongs to no lesson", last["Rule"])

    def test_empty_selection_says_none(self):
        out = M.render([], "lessons-curator", total=3)
        self.assertIn("(none)", out)

    def test_deterministic(self):
        a = M.render(M.select(M.parse(SAMPLE), "orchestrator"), "orchestrator", total=3)
        b = M.render(M.select(M.parse(SAMPLE), "orchestrator"), "orchestrator", total=3)
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
