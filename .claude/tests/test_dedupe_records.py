"""P4 — deterministic deduplication.

One row per STUDY. The guarantees that matter: identifiers match across formatting, a
preprint and its journal version merge inside the year guard but are only REPORTED
outside it, and a merged study takes its identity from the published record.
"""
import unittest

from harness import load

M = load("literature-retrieval/scripts/dedupe_records.py")


def rec(**kw):
    base = {"record_id": "x", "source": "pubmed", "title": "A study of things",
            "year": 2020, "pmid": None, "doi": None, "nct": None}
    base.update(kw)
    return base


def cluster_sizes(records):
    clusters, _, _ = M.dedupe(records)
    return sorted(len(c) for c in clusters)


class ThresholdsArePinned(unittest.TestCase):
    """Hardcoded on purpose. Loosening any of these dismantles the guarantee."""

    def test_values(self):
        self.assertEqual(M.FUZZY_THRESHOLD, 0.92)
        self.assertEqual(M.YEAR_GUARD, 1)
        self.assertEqual(M.BLOCK_PREFIX, 12)


class Normalisation(unittest.TestCase):
    def test_doi_prefix_forms_are_one_value(self):
        for raw in ("10.1056/NEJMoa1", "https://doi.org/10.1056/NEJMoa1",
                    "http://dx.doi.org/10.1056/nejmoa1", " 10.1056/NEJMOA1 "):
            self.assertEqual(M.norm_doi(raw), "10.1056/nejmoa1")

    def test_identifier_case_and_punctuation(self):
        self.assertEqual(M.norm_id("nct04198701"), "NCT04198701")
        self.assertEqual(M.norm_id("NCT-04198701"), "NCT04198701")

    def test_title_accents_and_punctuation(self):
        self.assertEqual(M.norm_title("Rung nhĩ: Cryo-balloon, versus PFA!"),
                         "rung nhi cryo balloon versus pfa")


class IdentifierMerging(unittest.TestCase):
    def test_doi_across_url_forms(self):
        self.assertEqual(cluster_sizes([
            rec(record_id="a", doi="10.1/x"), rec(record_id="b", doi="https://doi.org/10.1/X")]), [2])

    def test_pmid(self):
        self.assertEqual(cluster_sizes([
            rec(record_id="a", pmid="123"), rec(record_id="b", pmid="123", title="Other title")]), [2])

    def test_nct_case_insensitive(self):
        self.assertEqual(cluster_sizes([
            rec(record_id="a", nct="NCT04198701"), rec(record_id="b", nct="nct04198701")]), [2])

    def test_distinct_studies_stay_apart(self):
        self.assertEqual(cluster_sizes([
            rec(record_id="a", doi="10.1/x", title="Cryoballoon ablation trial"),
            rec(record_id="b", doi="10.1/y", title="Wholly unrelated nephrology work")]), [1, 1])


class YearGuard(unittest.TestCase):
    TITLE = "Long-term outcomes of contact force guided pulmonary vein isolation"

    def test_preprint_and_journal_merge_inside_the_guard(self):
        self.assertEqual(cluster_sizes([
            rec(record_id="pre", doi="10.1101/2022.1", title=self.TITLE, year=2022),
            rec(record_id="pub", doi="10.1016/j.jacc.1", title=self.TITLE, year=2023)]), [2])

    def test_outside_the_guard_is_reported_not_merged(self):
        records = [rec(record_id="pre", doi="10.1101/2013.1", title=self.TITLE, year=2013),
                   rec(record_id="pub", doi="10.1016/j.jacc.1", title=self.TITLE, year=2018)]
        clusters, _, suspected = M.dedupe(records)
        self.assertEqual(sorted(len(c) for c in clusters), [1, 1], "must not merge across the guard")
        self.assertEqual(len(suspected), 1, "a same-title pair outside the guard must be reported")

    def test_dissimilar_titles_never_merge(self):
        self.assertEqual(cluster_sizes([
            rec(record_id="a", title="Cryoballoon ablation in elderly patients with AF"),
            rec(record_id="b", title="Cryoballoon ablation in paediatric supraventricular tachycardia")]),
            [1, 1])


class MergedStudyIdentity(unittest.TestCase):
    def _merged(self, records):
        clusters, _, _ = M.dedupe(records)
        self.assertEqual(len(clusters), 1)
        return M.merge_cluster(records, clusters[0])

    def test_published_doi_beats_preprint_doi(self):
        """Law 3 downgrades preprints, so identity follows the peer-reviewed record."""
        s = self._merged([
            rec(record_id="pre", source="medrxiv", doi="10.1101/2022.1", title="A trial of X", year=2022),
            rec(record_id="pub", source="pubmed", doi="10.1056/NEJMoa1", title="A trial of X", year=2023)])
        self.assertEqual(s["study_id"], "doi:10.1056/nejmoa1")
        self.assertEqual(s["doi"], "10.1056/NEJMoa1")

    def test_formatting_difference_is_not_a_conflict(self):
        s = self._merged([rec(record_id="a", doi="10.1/x"),
                          rec(record_id="b", doi="https://doi.org/10.1/X")])
        self.assertNotIn("id_conflicts", s)

    def test_genuinely_different_identifiers_are_reported_and_kept(self):
        s = self._merged([
            rec(record_id="pre", doi="10.1101/2022.1", title="A trial of X", year=2022),
            rec(record_id="pub", doi="10.1056/NEJMoa1", title="A trial of X", year=2023)])
        self.assertIn("doi", s["id_conflicts"])
        self.assertEqual(len(s["id_conflicts"]["doi"]), 2, "both values must survive the merge")

    def test_sources_and_search_ids_are_unioned(self):
        s = self._merged([
            rec(record_id="a", source="pubmed", search_id="P1", pmid="123"),
            rec(record_id="b", source="elicit", search_id="E1", pmid="123")])
        self.assertEqual(s["sources"], ["elicit", "pubmed"])
        self.assertEqual(s["search_ids"], ["E1", "P1"])

    def test_earliest_year_is_the_studys_first_appearance(self):
        s = self._merged([rec(record_id="a", pmid="1", year=2023), rec(record_id="b", pmid="1", year=2022)])
        self.assertEqual(s["year"], 2022)

    def test_retraction_anywhere_marks_the_study(self):
        s = self._merged([rec(record_id="a", pmid="1", retracted=False),
                          rec(record_id="b", pmid="1", retracted=True)])
        self.assertTrue(s["retracted"])


class Determinism(unittest.TestCase):
    def test_input_order_does_not_change_the_clusters(self):
        records = [rec(record_id="a", doi="10.1/x"), rec(record_id="b", pmid="9", doi="10.1/x"),
                   rec(record_id="c", title="Something else entirely different here"),
                   rec(record_id="d", pmid="9")]
        forward = cluster_sizes(records)
        backward = cluster_sizes(list(reversed(records)))
        self.assertEqual(forward, backward)

    def test_repeated_runs_are_identical(self):
        records = [rec(record_id="a", doi="10.1/x"), rec(record_id="b", doi="10.1/x")]
        self.assertEqual(M.dedupe(records), M.dedupe(records))


if __name__ == "__main__":
    unittest.main()
