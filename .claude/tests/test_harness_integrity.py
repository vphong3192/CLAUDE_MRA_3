"""Structural integrity of the harness itself.

Both checks in `Wiring` guard a bug that actually shipped in this repo:

  * `quality-coach` was spawned by the orchestrator while no agent file defined it —
    TeamCreate would have failed at run time (fixed 2026-06-23).
  * a rule pointed at `L-023`, a lesson ID that had been consolidated away — the pointer
    read as authority but resolved to nothing (fixed 2026-06-23).

Neither is visible by reading any single file, which is exactly why they need a test.
"""
import ast
import re
import sys
import unittest

from harness import AGENTS, CLAUDE, REPO, SKILLS

LESSON_RE = re.compile(r"\bL-(\d{3})\b")

# Operational files: a rule here that cites a lesson is invoking it as authority, so the
# pointer must resolve. Deliberately excluded: lessons.md (its own `Origin:` lines record
# which retired IDs were consolidated into a lesson), evolution-log.md and CLAUDE.md's
# changelog (historical records, where a retired ID is the correct thing to name).
def operational_files():
    return (
        sorted(AGENTS.glob("*.md"))
        + sorted(SKILLS.glob("*/SKILL.md"))
        + sorted(SKILLS.glob("*/references/*.md"))
        + [CLAUDE / "constitution.md"]
    )


def defined_lessons():
    text = (SKILLS / "lessons-learned" / "lessons.md").read_text(encoding="utf-8")
    return {m.group(1) for m in re.finditer(r"^### L-(\d{3}):", text, re.MULTILINE)}


def frontmatter_name(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    block = text.split("---", 2)[1]
    m = re.search(r"^name:\s*(\S+)", block, re.MULTILINE)
    return m.group(1) if m else None


class Wiring(unittest.TestCase):
    def test_no_dead_lesson_pointers(self):
        defined = defined_lessons()
        dead = {}
        for path in operational_files():
            for m in LESSON_RE.finditer(path.read_text(encoding="utf-8")):
                if m.group(1) not in defined:
                    dead.setdefault(str(path.relative_to(REPO)), set()).add("L-" + m.group(1))
        self.assertEqual(dead, {}, f"lesson pointers that resolve to nothing: {dead}")

    def test_every_agent_the_orchestrator_names_exists(self):
        text = (SKILLS / "medical-review-orchestrator" / "SKILL.md").read_text(encoding="utf-8")
        on_disk = {p.stem for p in AGENTS.glob("*.md")}
        # the team table lists each member as `subagent_type` in a backticked cell
        named = {m.group(1) for m in re.finditer(r"^\| `([a-z-]+)`", text, re.MULTILINE)}
        self.assertTrue(named, "no agents parsed out of the orchestrator team table")
        self.assertEqual(named - on_disk, set(),
                         f"orchestrator names agents with no file: {named - on_disk}")

    def test_agent_frontmatter_name_matches_filename(self):
        for path in sorted(AGENTS.glob("*.md")):
            with self.subTest(agent=path.name):
                self.assertEqual(frontmatter_name(path), path.stem)

    def test_skill_frontmatter_name_matches_directory(self):
        for path in sorted(SKILLS.glob("*/SKILL.md")):
            with self.subTest(skill=path.parent.name):
                self.assertEqual(frontmatter_name(path), path.parent.name)


class WorkspaceContract(unittest.TestCase):
    """Every `_workspace/` artifact an operational file names must be declared in CLAUDE.md.

    Guards the orphan-artifact bug: P4 required `_workspace/01a_concepts.json` while no agent was
    told to write it, so the pipeline depended on a file nothing produced. An artifact nobody
    declares is an artifact nobody owns.
    """

    # Match ANY path under _workspace/, then check its shape separately. Filtering with the same
    # pattern the naming test asserts would make that test unable to fail.
    ANY_ARTIFACT = re.compile(r"_workspace/([A-Za-z0-9_.-]+\.[a-z]+)")
    WELL_FORMED = re.compile(r"[0-9]{2}[a-z]?_[a-z_]+\.[a-z]+")
    DECLARED = re.compile(r"`([0-9]{2}[a-z]?_[a-z_]+\.[a-z]+)`")

    def named_in_operational_files(self):
        found = {}
        for path in operational_files():
            rel = str(path.relative_to(REPO))
            for m in self.ANY_ARTIFACT.finditer(path.read_text(encoding="utf-8")):
                found.setdefault(m.group(1), set()).add(rel)
        return found

    def declared(self):
        text = (REPO / "CLAUDE.md").read_text(encoding="utf-8")
        return set(self.DECLARED.findall(text))

    def test_every_named_artifact_is_declared(self):
        undeclared = {a: sorted(w) for a, w in self.named_in_operational_files().items()
                      if a not in self.declared()}
        self.assertEqual(undeclared, {},
                         f"artifacts used but not in the CLAUDE.md contract: {undeclared}")

    def test_numbering_rule_holds(self):
        """NN = the phase; an optional single letter = a supporting artifact of that phase."""
        bad = {a: sorted(w) for a, w in self.named_in_operational_files().items()
               if not self.WELL_FORMED.fullmatch(a)}
        self.assertEqual(bad, {}, f"artifacts breaking the NN[a-z]_name.ext rule: {bad}")

    def test_pipeline_inputs_have_a_producer_outside_their_consumer(self):
        """A file a script READS must be WRITTEN by some agent, not assumed into existence.

        `literature-retrieval/SKILL.md` is where both of these are consumed, so a mention there
        proves nothing — the producer has to be somewhere else.
        """
        consumer = ".claude/skills/literature-retrieval/SKILL.md"
        named = self.named_in_operational_files()
        for artifact in ("01a_concepts.json", "02b_records.jsonl"):
            with self.subTest(artifact=artifact):
                producers = named.get(artifact, set()) - {consumer}
                self.assertTrue(producers,
                                f"{artifact} is consumed by the P4 pipeline but no agent outside "
                                f"{consumer} is told to write it")


class ScriptPointers(unittest.TestCase):
    def test_every_script_a_doc_points_at_exists(self):
        docs = operational_files() + [REPO / "README.md", REPO / "CLAUDE.md"]
        missing = {}
        for doc in docs:
            for m in re.finditer(r"[\w./-]*scripts/[\w_]+\.py", doc.read_text(encoding="utf-8")):
                ref = m.group(0)
                name = ref.rsplit("/", 1)[1]
                if not list(SKILLS.glob(f"*/scripts/{name}")):
                    missing.setdefault(str(doc.relative_to(REPO)), set()).add(ref)
        self.assertEqual(missing, {}, f"docs point at scripts that do not exist: {missing}")


class DeterministicLayerIsSelfContained(unittest.TestCase):
    """No pip install, no network client, no LLM call — the layer must run anywhere."""

    def scripts(self):
        found = sorted(SKILLS.glob("*/scripts/*.py"))
        self.assertTrue(found, "no deterministic scripts found")
        return found

    def test_stdlib_imports_only(self):
        third_party = {}
        for path in self.scripts():
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    mods = [a.name.split(".")[0] for a in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0:
                    mods = [(node.module or "").split(".")[0]]
                else:
                    continue
                for mod in mods:
                    if mod and mod not in sys.stdlib_module_names:
                        third_party.setdefault(path.name, set()).add(mod)
        self.assertEqual(third_party, {}, f"non-stdlib imports: {third_party}")

    def test_no_network_calls(self):
        forbidden = ("urllib.request", "http.client", "socket", "requests", "httpx")
        offenders = {}
        for path in self.scripts():
            text = path.read_text(encoding="utf-8")
            for token in forbidden:
                if re.search(rf"\b(?:import|from)\s+{re.escape(token)}\b", text):
                    offenders.setdefault(path.name, set()).add(token)
        self.assertEqual(offenders, {}, f"deterministic scripts must not reach the network: {offenders}")

    def test_each_script_is_executable_as_a_module(self):
        for path in self.scripts():
            with self.subTest(script=path.name):
                compile(path.read_text(encoding="utf-8"), str(path), "exec")


if __name__ == "__main__":
    unittest.main()
