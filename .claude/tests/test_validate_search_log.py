"""P3 — recall & reproducibility ledger validation.

The ledger is how a recall claim stops being narration and becomes a receipt. The script
checks the ledger's completeness and internal consistency — never whether the counts are
true — so these tests pin each HARD-FAIL cause and the seven-column contract.
"""
import unittest

from harness import load, categories

M = load("literature-retrieval/scripts/validate_search_log.py")

HEADER = "| id | source | query | call | total_count | retrieved | recall |"
SEP = "|----|--------|-------|------|-------------|-----------|--------|"
GOOD = ('| P1 | PubMed | ablation index AND PVI | esearch db=pubmed term="ablation index" '
        'retmax=200 | 148 | 148 | retrieved==total ✓ |')


def log(*rows, header=HEADER):
    body = "\n".join([
        "# Search Log — fixture",
        "",
        "## Recall & reproducibility ledger (P3)",
        "",
        header,
        SEP,
        *rows,
        "",
    ])
    return body


def run(*rows, **kw):
    findings, n_rows = M.validate(log(*rows, **kw))
    return categories(findings), n_rows


class ColumnContract(unittest.TestCase):
    def test_seven_required_columns(self):
        """Pinned: dropping a column silently removes a check."""
        self.assertEqual(
            M.REQUIRED,
            ["id", "source", "query", "call", "total_count", "retrieved", "recall"],
        )

    def test_missing_column_is_hard_fail(self):
        header = "| id | source | query | total_count | retrieved | recall |"   # no `call`
        cats, _ = run(GOOD, header=header)
        self.assertIn("missing_columns", cats)


class LedgerPresence(unittest.TestCase):
    def test_no_ledger_at_all(self):
        findings, _ = M.validate("# Search Log\n\nI searched PubMed. It went well.\n")
        self.assertEqual(categories(findings), {"no_ledger"})

    def test_header_without_rows(self):
        cats, n = run()
        self.assertIn("empty_ledger", cats)
        self.assertEqual(n, 0)


class ValidLedgerPasses(unittest.TestCase):
    def test_clean_row_produces_nothing(self):
        cats, n = run(GOOD)
        self.assertEqual(cats, set(), f"a clean ledger row raised findings: {cats}")
        self.assertEqual(n, 1)

    def test_capped_row_is_legitimate(self):
        row = ('| P3 | PubMed | contact force | esearch db=pubmed term="contact force" '
               'retmax=500 | 732 | 500 | capped ⚠ (landmark-filtered, see §4) |')
        cats, _ = run(row)
        self.assertEqual(cats, set())


class EachFailureCause(unittest.TestCase):
    def test_non_integer_count(self):
        row = '| P1 | PubMed | q | esearch db=pubmed term="q" | ~70 | 70 | retrieved==total ✓ |'
        self.assertIn("bad_number", run(row)[0])

    def test_call_without_params_or_url(self):
        row = '| P1 | PubMed | ablation index | I searched PubMed | 148 | 148 | retrieved==total ✓ |'
        self.assertIn("call_not_reproducible", run(row)[0])

    def test_call_that_merely_copies_the_query(self):
        row = '| P1 | PubMed | term=x | term=x | 148 | 148 | retrieved==total ✓ |'
        self.assertIn("call_not_reproducible", run(row)[0])

    def test_unknown_recall_verdict(self):
        row = '| P1 | PubMed | q | esearch db=pubmed term="q" | 148 | 148 | yes |'
        self.assertIn("unknown_recall_verdict", run(row)[0])

    def test_empty_cell(self):
        row = '| P1 | PubMed |  | esearch db=pubmed term="q" | 148 | 148 | retrieved==total ✓ |'
        self.assertIn("empty_cell", run(row)[0])

    def test_malformed_row(self):
        self.assertIn("malformed_row", run("| P1 | PubMed | q |")[0])


class RecallSelfConsistency(unittest.TestCase):
    """A verdict that contradicts its own numbers is the failure this layer exists to catch."""

    def test_complete_but_short(self):
        row = '| P1 | PubMed | q | esearch db=pubmed term="q" | 732 | 500 | retrieved==total ✓ |'
        self.assertIn("inconsistent_recall", run(row)[0])

    def test_capped_but_actually_complete(self):
        row = '| P1 | PubMed | q | esearch db=pubmed term="q" | 148 | 148 | capped ⚠ |'
        self.assertIn("inconsistent_recall", run(row)[0])


class Fixtures(unittest.TestCase):
    def _read(self, name):
        path = str(M.__file__).rsplit("/", 1)[0] + "/fixtures/" + name
        with open(path, encoding="utf-8") as fh:
            return fh.read()

    def test_valid_fixture_is_clean(self):
        findings, n = M.validate(self._read("search_log_valid.md"))
        self.assertEqual(findings, [])
        self.assertEqual(n, 4)

    def test_invalid_fixture_is_caught(self):
        findings, _ = M.validate(self._read("search_log_invalid.md"))
        self.assertTrue(findings)


class Determinism(unittest.TestCase):
    def test_identical_output_across_runs(self):
        text = log(GOOD, '| P2 | Consensus |  | search query="x" page=1 | 20 | 20 | complete ✓ |')
        self.assertEqual(M.validate(text), M.validate(text))


if __name__ == "__main__":
    unittest.main()
