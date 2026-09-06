"""P1 — deterministic citation audit.

The audit is the mechanical floor under Law 1: it proves every citation traces to the
closed reference store. These tests pin each HARD-FAIL category to its own trigger, so a
future edit cannot quietly stop one of them from firing.
"""
import contextlib
import io
import pathlib
import tempfile
import unittest

from harness import load, categories

M = load("citation-verification/scripts/citation_audit.py")

STORE = """# Reference Store — test fixture

### [REF-001] Author A 2020 — trial one
- **PMID/DOI:** PMID 11111111 / DOI 10.1000/real.001
- **Key findings:** HR 0.76 (95% CI 0.60–0.96); N=762 randomized.

### [REF-002] Author B 2021 — trial two
- **PMID/DOI:** PMID 22222222 / DOI 10.1000/real.002
- **Key findings:** Recurrence 34.6% vs 35.9%; p=0.04.
"""

BIG_STORE = STORE + "".join(
    f"""
### [REF-{n:03d}] Author {n} 2022 — trial {n}
- **PMID/DOI:** PMID {n}{n}{n}{n}{n}{n}{n}{n} / DOI 10.1000/real.{n:03d}
- **Key findings:** Some finding {n}.
"""
    for n in range(3, 8)
)

REFLIST = """
## Tài liệu tham khảo
1. Author A, et al. Trial one. Journal. 2020. PMID: [11111111](https://pubmed.ncbi.nlm.nih.gov/11111111/).
2. Author B, et al. Trial two. Journal. 2021. PMID: [22222222](https://pubmed.ncbi.nlm.nih.gov/22222222/).
"""


def draft(body, reflist=REFLIST):
    return "# Draft\n\n" + body + "\n" + reflist


def run(body, reflist=REFLIST, frac=0.4):
    return M.audit(draft(body, reflist), STORE, frac)


class CleanDraftPasses(unittest.TestCase):
    def test_no_hard_findings(self):
        hard, _, _ = run("The hazard ratio was 0.76 [1]. Recurrence was 34.6% [2].")
        self.assertEqual(hard, [], f"clean draft produced HARD-FAILs: {hard}")

    def test_counts_are_reported(self):
        _, _, stats = run("Finding one [1]. Finding two [2].")
        self.assertEqual(stats["store_records"], 2)
        self.assertEqual(stats["draft_refs"], 2)
        self.assertEqual(stats["cited_records"], 2)
        self.assertAlmostEqual(stats["coverage_frac"], 1.0)


class EachHardCategoryFires(unittest.TestCase):
    def test_fabricated_citation(self):
        """A reference whose PMID is not in the store is the Law 1 auto-fail."""
        reflist = REFLIST + (
            "3. Ghost Author. A study not in the store. Journal. 2099. "
            "PMID: [99999999](https://pubmed.ncbi.nlm.nih.gov/99999999/).\n"
        )
        hard, _, _ = run("A [1]. B [2]. A fabricated claim [3].", reflist)
        self.assertIn("fabricated_citation", categories(hard))

    def test_reference_with_no_identifier(self):
        reflist = REFLIST + "3. Someone. A paper with no PMID, DOI or NCT at all. Journal. 2020.\n"
        hard, _, _ = run("A [1]. B [2]. C [3].", reflist)
        self.assertIn("missing_in_store", categories(hard))

    def test_inline_citation_absent_from_reference_list(self):
        hard, _, _ = run("A [1]. B [2]. An orphan inline citation [9].")
        self.assertIn("missing_in_store", categories(hard))

    def test_every_placeholder_form(self):
        """All five placeholder forms must block; none may be silently tolerated."""
        for marker in ("[N]", "[?]", "CITATION_NEEDED", "TODO", "[@NEW:pmid-123]"):
            with self.subTest(marker=marker):
                hard, _, _ = run(f"A [1]. B [2]. Unfinished text {marker} here.")
                self.assertIn("placeholder_leftover", categories(hard))

    def test_coverage_below_threshold(self):
        """7 citable records, 1 cited = 14% — under the 40% floor."""
        hard, _, _ = M.audit(draft("Only the first source is cited [1]."), BIG_STORE, 0.4)
        self.assertIn("coverage_below_threshold", categories(hard))


class CoverageThreshold(unittest.TestCase):
    def test_default_is_forty_percent_in_the_source(self):
        """Read the literal out of the script's own parser — not a copy of it."""
        import ast
        tree = ast.parse(pathlib.Path(M.__file__).read_text(encoding="utf-8"))
        found = []
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call)
                    and getattr(node.func, "attr", None) == "add_argument"
                    and node.args
                    and getattr(node.args[0], "value", None) == "--min-coverage-frac"):
                for kw in node.keywords:
                    if kw.arg == "default":
                        found.append(kw.value.value)
        self.assertEqual(found, [0.4], "the coverage floor moved without a test being updated")

    def test_default_floor_blocks_a_thin_draft_end_to_end(self):
        """Behavioural pin: 1 of 7 records cited (14%) must FAIL with no flag passed.

        Verified by mutation — loosening the default to 0.1 makes this draft pass.
        """
        with tempfile.TemporaryDirectory() as tmp:
            d = pathlib.Path(tmp) / "draft.md"
            st = pathlib.Path(tmp) / "store.md"
            d.write_text(draft("Only the first source is cited [1]."), encoding="utf-8")
            st.write_text(BIG_STORE, encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                rc = M.main(["--draft", str(d), "--store", str(st)])
        self.assertEqual(rc, 1, "a 14%-coverage draft must not pass the default floor")

    def test_zero_disables_the_check(self):
        hard, _, _ = M.audit(draft("Only the first source is cited [1]."), BIG_STORE, 0.0)
        self.assertNotIn("coverage_below_threshold", categories(hard))

    def test_half_coverage_passes_forty_percent(self):
        """1 of 2 records = 50%, above the 40% floor — must not fire."""
        hard, _, _ = run("Only the first source is cited [1].", frac=0.4)
        cats = categories(hard)
        self.assertNotIn("coverage_below_threshold", cats)


class WarnsNeverBlock(unittest.TestCase):
    def test_uncited_statistic_warns_but_does_not_fail(self):
        hard, warn, _ = run("An effect of 88% was reported with no citation at all.",
                            reflist=REFLIST, frac=0.0)
        self.assertEqual(hard, [], "a WARN-only defect must not produce a HARD-FAIL")
        self.assertTrue(warn, "an uncited statistic should raise at least one WARN")


class Determinism(unittest.TestCase):
    def test_identical_output_across_runs(self):
        body = "A [1]. B [2]. An effect of 88% with no citation."
        first = run(body)
        second = run(body)
        self.assertEqual(first, second)


class ExitCodeContract(unittest.TestCase):
    """Law 1: a fabricated citation makes the review not-deliverable — exit 1."""

    def _fixture(self, name):
        return str(M.__file__).rsplit("/", 1)[0] + "/fixtures/" + name

    def _rc(self, draft_name):
        with contextlib.redirect_stdout(io.StringIO()):
            return M.main(["--draft", self._fixture(draft_name),
                           "--store", self._fixture("store_good.md")])

    def test_clean_fixture_exits_zero(self):
        self.assertEqual(self._rc("draft_clean.md"), 0)

    def test_bad_fixture_exits_one(self):
        self.assertEqual(self._rc("draft_bad.md"), 1)


if __name__ == "__main__":
    unittest.main()
