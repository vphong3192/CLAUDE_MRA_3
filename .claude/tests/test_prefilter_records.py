"""P4 — deterministic relevance prioritisation.

Three rules carry the whole design: the score only ADDS, an empty scope signal means
UNKNOWN, and the two recall floors override the percentage. Each has its own test,
because each names a way a relevant study gets lost silently.
"""
import contextlib
import io
import json
import pathlib
import tempfile
import unittest

from harness import load

M = load("literature-retrieval/scripts/prefilter_records.py")

SPEC = {
    "concepts": [
        {"name": "population", "terms": ["atrial fibrillation"]},
        {"name": "intervention", "terms": ["cryoballoon"]},
        {"name": "comparator", "terms": ["versus"]},
        {"name": "outcome", "terms": ["recurrence"]},
    ],
    "scope_terms": ["ablation"],
}
CFG = {"target_percent": 25, "min_candidates": 150, "max_candidates": 600, "full_coverage_floor": True}


def compiled(spec=SPEC):
    return M.compile_concepts(spec)


def study(sid, title, abstract="", year=2020, retracted=False):
    return {"study_id": sid, "title": title, "abstract": abstract, "year": year,
            "retracted": retracted}


def run(studies, **over):
    cfg = {**CFG, **over}
    concepts, scope = compiled()
    return M.prioritise(studies, concepts, scope, cfg)


class ScoringOnlyAdds(unittest.TestCase):
    def test_bonus_is_strictly_smaller_than_a_concept_hit(self):
        """The asymmetry IS the rule — pin the relation, not just the numbers."""
        self.assertEqual(M.CONCEPT_WEIGHT, 2)
        self.assertEqual(M.SCOPE_BONUS, 1)
        self.assertLess(M.SCOPE_BONUS, M.CONCEPT_WEIGHT,
                        "a scope bonus worth a whole concept lets scope outrank topicality")

    def test_out_of_scope_is_not_penalised(self):
        """Same topicality must give the same base score — the bonus is added, never subtracted."""
        concepts, scope = compiled()
        in_scope = M.score_study(study("a", "atrial fibrillation cryoballoon ablation"), concepts, scope)
        out_scope = M.score_study(study("b", "atrial fibrillation cryoballoon", "nephrology cohort"),
                                  concepts, scope)
        self.assertEqual(in_scope["n_concepts"], out_scope["n_concepts"])
        self.assertEqual(in_scope["score"] - out_scope["score"], M.SCOPE_BONUS)
        self.assertGreater(out_scope["score"], 0, "an out-of-scope study keeps its concept score")

    def test_scope_bonus_cannot_outrank_topicality(self):
        """One extra concept must always beat the scope bonus."""
        concepts, scope = compiled()
        two_out = M.score_study(study("a", "atrial fibrillation cryoballoon", "x"), concepts, scope)
        one_in = M.score_study(study("b", "atrial fibrillation ablation", "x"), concepts, scope)
        self.assertGreater(two_out["score"], one_in["score"])


class EmptyMeansUnknown(unittest.TestCase):
    def test_no_scope_terms_declared_leaves_everything_unknown(self):
        concepts, scope = M.compile_concepts({**SPEC, "scope_terms": []})
        sc = M.score_study(study("a", "atrial fibrillation cryoballoon"), concepts, scope)
        self.assertEqual(sc["scope"], "unknown")
        self.assertEqual(sc["score"], 2 * M.CONCEPT_WEIGHT,
                         "no scope declared means no bonus and no penalty")

    def test_missing_abstract_is_unknown_not_out(self):
        concepts, scope = compiled()
        sc = M.score_study(study("a", "some unrelated title", abstract=""), concepts, scope)
        self.assertEqual(sc["scope"], "unknown")


class RecallFloors(unittest.TestCase):
    def test_small_pool_is_screened_in_full(self):
        studies = [study(f"s{i}", "atrial fibrillation cryoballoon") for i in range(40)]
        cand, deferred, _, stats = run(studies)
        self.assertEqual(len(cand), 40)
        self.assertEqual(deferred, [])
        self.assertIn("screen in full", stats["rule"])

    def test_percentage_applies_above_the_floor(self):
        studies = [study(f"s{i}", "atrial fibrillation cryoballoon") for i in range(1000)]
        cand, _, _, stats = run(studies)
        self.assertEqual(len(cand), 250, "25% of 1000")

    def test_ceiling_caps_the_percentage_only(self):
        studies = [study(f"s{i}", "atrial fibrillation cryoballoon") for i in range(1000)]
        cand, _, _, stats = run(studies, max_candidates=100)
        self.assertEqual(len(cand), 150, "the min_candidates floor overrides the ceiling")
        self.assertTrue(stats["over_cap"], "exceeding the ceiling must be reported, not trimmed")

    def test_full_coverage_floor_when_matches_outnumber_the_cut(self):
        """The reachable case, and the one Evisyn measured: a large pool where far more
        studies match every concept than the percentage is willing to keep. Ranking alone
        keeps k of them and drops the rest purely for being further down an arbitrary list.
        """
        studies = [study(f"all{i:04d}", f"atrial fibrillation cryoballoon versus recurrence {i}",
                         abstract="no scope term", year=2020) for i in range(400)]
        kept = run(studies, min_candidates=10, target_percent=10)[0]
        self.assertEqual(len(kept), 400,
                         "every study matching all four concepts must survive the cut")

        without = run(studies, min_candidates=10, target_percent=10, full_coverage_floor=False)[0]
        self.assertEqual(len(without), 40, "without the floor the percentage cuts 360 of them")


class RetractedHandling(unittest.TestCase):
    def test_retracted_removed_before_ranking(self):
        studies = [study("ok", "atrial fibrillation cryoballoon"),
                   study("bad", "atrial fibrillation cryoballoon", retracted=True)]
        cand, _, retracted, stats = run(studies)
        self.assertEqual([s["study_id"] for s in retracted], ["bad"])
        self.assertNotIn("bad", {s["study_id"] for s in cand})
        self.assertEqual(stats["retracted_excluded"], 1)


class ReportWording(unittest.TestCase):
    def test_deferred_is_called_unread_not_excluded(self):
        studies = [study(f"s{i}", "atrial fibrillation cryoballoon") for i in range(1000)]
        cand, deferred, retracted, stats = run(studies)
        concepts, _ = compiled()

        class Args:
            studies = "x.jsonl"; concepts = "c.json"; target_percent = 25
            min_candidates = 150; max_candidates = 600; no_full_coverage_floor = False
        text = M.render(cand, deferred, retracted, stats, concepts, Args())
        self.assertIn("NOT excluded", text)
        self.assertIn("unread", text)


class ModuleDefaultsAreLive(unittest.TestCase):
    """Exercise the defaults through the CLI.

    Every other test here injects its own config, so the module constants were never
    actually run — a mutation zeroing MIN_CANDIDATES or flipping FULL_COVERAGE_FLOOR
    passed the whole suite. These two go through main(), so the shipped defaults are
    what is under test.
    """

    def _run_cli(self, studies, *extra):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            (tmp / "s.jsonl").write_text(
                "".join(json.dumps(x) + "\n" for x in studies), encoding="utf-8")
            (tmp / "c.json").write_text(json.dumps(SPEC), encoding="utf-8")
            out = tmp / "cand.jsonl"
            with contextlib.redirect_stdout(io.StringIO()):
                M.main(["--studies", str(tmp / "s.jsonl"), "--concepts", str(tmp / "c.json"),
                        "--out-candidates", str(out), *extra])
            return [json.loads(l) for l in out.read_text(encoding="utf-8").splitlines() if l.strip()]

    def test_default_min_candidates_screens_a_small_pool_in_full(self):
        studies = [study(f"s{i:03d}", "atrial fibrillation cryoballoon") for i in range(40)]
        self.assertEqual(len(self._run_cli(studies)), 40,
                         "the shipped min_candidates floor must screen a 40-study pool whole")
        self.assertGreaterEqual(M.MIN_CANDIDATES, 40)

    def test_full_coverage_floor_is_on_by_default(self):
        studies = [study(f"all{i:04d}", f"atrial fibrillation cryoballoon versus recurrence {i}",
                         abstract="no scope term") for i in range(400)]
        kept = self._run_cli(studies, "--target-percent", "10", "--min-candidates", "10")
        self.assertEqual(len(kept), 400,
                         "the shipped default must keep every study matching all concepts")
        self.assertTrue(M.FULL_COVERAGE_FLOOR)


class Determinism(unittest.TestCase):
    def test_ties_are_broken_reproducibly(self):
        studies = [study(f"s{i}", "atrial fibrillation cryoballoon", year=2020) for i in range(300)]
        first = [s["study_id"] for s in run(studies)[0]]
        second = [s["study_id"] for s in run(list(reversed(studies)))[0]]
        self.assertEqual(first, second, "input order must not change which studies are screened")


if __name__ == "__main__":
    unittest.main()
