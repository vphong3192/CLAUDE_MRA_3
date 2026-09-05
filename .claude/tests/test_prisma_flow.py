"""P4 — deterministic PRISMA 2020 flow.

The failure this guards is not an arithmetic slip, it is a false claim about the method:
drawing a full-text eligibility box for a review that never opened a full text, or
counting an unread study as "excluded". Every test below is about the diagram telling
the truth of what ran.
"""
import unittest

from harness import load

M = load("literature-retrieval/scripts/prisma_flow.py")


def r(source="pubmed", **kw):
    return {"source": source, **kw}


def s(sid, retracted=False):
    return {"study_id": sid, "retracted": retracted}


def v(sid, verdict, reason=""):
    return {"study_id": sid, "verdict": verdict, "reason": reason}


class SourceClassification(unittest.TestCase):
    def test_preprint_servers_count_as_databases(self):
        """A preprint server is a database you searched, not a hand-found record."""
        db, other = M.source_split([r("biorxiv"), r("medrxiv"), r("pubmed")])
        self.assertEqual(db, 3)
        self.assertEqual(other, {})

    def test_registries_count_as_databases_and_registers(self):
        db, other = M.source_split([r("ctgov")])
        self.assertEqual((db, other), (1, {}))

    def test_author_supplied_and_web_are_other_methods(self):
        db, other = M.source_split([r("source_folder"), r("web"), r("pubmed")])
        self.assertEqual(db, 1)
        self.assertEqual(sum(other.values()), 2)

    def test_unknown_source_is_named_not_silently_binned(self):
        _, other = M.source_split([r("typo_source")])
        self.assertIn("typo_source", other)


class BoxesOnlyForStepsThatRan(unittest.TestCase):
    def _flow(self, **kw):
        base = dict(records=[r()], studies=[s("a")], candidates=[s("a")], deferred=[],
                    verdicts=[v("a", "include")], fulltext_assessed=None, fulltext_excluded=None)
        base.update(kw)
        return M.build(**base)

    def test_no_fulltext_box_without_a_fulltext_assessment(self):
        flow = self._flow()
        self.assertNotIn("fulltext_assessed", flow["stages"])
        self.assertNotIn("Full text assessed", M.mermaid(flow))
        self.assertFalse(flow["labels"]["fulltext_box_drawn"])

    def test_fulltext_box_appears_when_it_actually_ran(self):
        flow = self._flow(fulltext_assessed=3, fulltext_excluded=1)
        self.assertIn("Full text assessed", M.mermaid(flow))

    def test_other_methods_box_only_when_such_a_record_exists(self):
        without = M.build([r("pubmed")], [s("a")], [s("a")], [], [v("a", "include")], None, None)
        self.assertNotIn("other methods", M.mermaid(without))
        with_other = M.build([r("pubmed"), r("source_folder")], [s("a")], [s("a")], [],
                             [v("a", "include")], None, None)
        self.assertIn("other methods", M.mermaid(with_other))

    def test_eligibility_is_labelled_title_and_abstract(self):
        flow = self._flow()
        self.assertEqual(flow["labels"]["eligibility_basis"], "title and abstract")


class DeferredIsNotExcluded(unittest.TestCase):
    def test_deferred_counted_separately_and_named_unread(self):
        flow = M.build([r(), r()], [s("a"), s("b")], [s("a")], [s("b")],
                       [v("a", "include")], None, None)
        self.assertEqual(flow["stages"]["deferred_not_screened"], 1)
        self.assertEqual(flow["stages"].get("excluded_title_abstract", 0), 0)
        self.assertIn("NOT screened, not excluded", M.mermaid(flow))


class RetractionIsItsOwnRemoval(unittest.TestCase):
    def test_not_folded_into_duplicates_or_exclusions(self):
        flow = M.build([r(), r()], [s("a"), s("bad", retracted=True)], [s("a")], [],
                       [v("a", "include")], None, None)
        st = flow["stages"]
        self.assertEqual(st["retracted_removed"], 1)
        self.assertEqual(st["duplicates_removed"], 0)
        self.assertEqual(st["eligible_for_screening"], 1)
        self.assertEqual(flow["retracted_ids"], ["bad"])
        self.assertNotIn("bad", flow.get("exclusion_reasons", {}))


class VerdictAccounting(unittest.TestCase):
    def test_maybe_is_reported_and_not_included(self):
        flow = M.build([r()] * 3, [s("a"), s("b"), s("c")], [s("a"), s("b"), s("c")], [],
                       [v("a", "include"), v("b", "maybe"), v("c", "exclude", "off topic")],
                       None, None)
        st = flow["stages"]
        self.assertEqual((st["included"], st["maybe_not_included"], st["excluded_title_abstract"]),
                         (1, 1, 1))

    def test_exclusion_reasons_are_tallied(self):
        flow = M.build([r()] * 2, [s("a"), s("b")], [s("a"), s("b")], [],
                       [v("a", "exclude", "wrong population"), v("b", "exclude", "wrong population")],
                       None, None)
        self.assertEqual(flow["exclusion_reasons"], {"wrong population": 2})

    def test_exclusion_without_a_reason_is_flagged(self):
        flow = M.build([r()], [s("a")], [s("a")], [], [v("a", "exclude", "")], None, None)
        self.assertTrue(any("reason" in w for w in flow["warnings"]))


class ConsistencyChecks(unittest.TestCase):
    def test_screened_plus_deferred_must_equal_eligible(self):
        flow = M.build([r()] * 5, [s(x) for x in "abcde"], [s("a")], [s("b")],
                       [v("a", "include")], None, None)
        self.assertTrue(any("eligible for screening" in w for w in flow["warnings"]))

    def test_every_screened_study_needs_a_verdict(self):
        flow = M.build([r()] * 2, [s("a"), s("b")], [s("a"), s("b")], [],
                       [v("a", "include")], None, None)
        self.assertTrue(any("verdict" in w for w in flow["warnings"]))

    def test_a_consistent_flow_raises_nothing(self):
        flow = M.build([r()] * 2, [s("a"), s("b")], [s("a"), s("b")], [],
                       [v("a", "include"), v("b", "exclude", "off topic")], None, None)
        self.assertEqual(flow["warnings"], [])


class Degradation(unittest.TestCase):
    def test_missing_stage_files_omit_boxes_rather_than_inventing_numbers(self):
        flow = M.build(None, None, None, None, None, None, None)
        self.assertEqual(flow["stages"], {})
        self.assertEqual(flow["warnings"], [])


class Determinism(unittest.TestCase):
    def test_identical_output_across_runs(self):
        args = ([r(), r("source_folder")], [s("a"), s("b")], [s("a")], [s("b")],
                [v("a", "include")], None, None)
        self.assertEqual(M.build(*args), M.build(*args))
        self.assertEqual(M.mermaid(M.build(*args)), M.mermaid(M.build(*args)))


if __name__ == "__main__":
    unittest.main()
