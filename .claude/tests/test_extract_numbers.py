"""P2 — deterministic verbatim number extraction.

The appraiser LOADS these numbers instead of hand-copying them, so the guarantees that
matter are: the right number lands in the right bucket, a metadata digit can never
masquerade as data, and an empty bucket says "(none)" rather than inviting an invention.
"""
import unittest

from harness import load

M = load("evidence-appraisal/scripts/extract_numbers.py")


class BucketContract(unittest.TestCase):
    def test_five_buckets_in_priority_order(self):
        """Order is the contract: the first pattern to claim a span owns it."""
        self.assertEqual(
            M.BUCKET_ORDER,
            ["confidence_intervals", "ratios", "p_values", "sample_sizes", "percentages"],
        )

    def test_higher_priority_bucket_claims_the_span(self):
        """'95% CI 0.60–0.96' is one interval — the '95 %' inside it is not a percentage."""
        found = M.extract("The hazard ratio was 0.76 (95% CI 0.60–0.96).")
        self.assertTrue(any("CI" in v for v in found["confidence_intervals"]))
        self.assertEqual(found["percentages"], [],
                         "the 95% inside a CI must not be double-counted as a percentage")

    def test_ratio_and_interval_coexist(self):
        found = M.extract("Adjusted HR 0.96 (95% CI 0.76–1.22) for the primary endpoint.")
        self.assertTrue(any("0.96" in v for v in found["ratios"]))
        self.assertTrue(any("0.76" in v for v in found["confidence_intervals"]))

    def test_sample_size_forms(self):
        found = M.extract("N=762 randomized; a second cohort of 353 patients was followed.")
        joined = " ".join(found["sample_sizes"])
        self.assertIn("762", joined)
        self.assertIn("353", joined)


class EffectEstimates(unittest.TestCase):
    """The effect estimate is the most important number in a trial, and both directions of
    getting it wrong were found by an integration run rather than by a unit test."""

    SPELLINGS = [
        "hazard ratio, 0.48", "hazard ratio 0.48", "HR 0.48", "HR, 0.48", "HR=0.48",
        "aHR 0,73", "odds ratio, 1.24", "risk ratio of 0.91", "adjusted hazard ratio, 0.73",
        "relative risk 1.15", "mean difference, -2.4", "standardized mean difference 0.31",
        "tỷ số nguy cơ 0,48", "khác biệt trung bình -2,4", "β = 0.12",
    ]

    def test_every_spelling_journals_actually_use(self):
        for text in self.SPELLINGS:
            with self.subTest(text=text):
                self.assertTrue(M.extract(text)["ratios"],
                                "a missed effect estimate forces the appraiser to hand-copy it — "
                                "the exact hazard P2 exists to remove")

    def test_the_english_word_or_is_not_an_odds_ratio(self):
        """`\\bOR\\b` under IGNORECASE turned "cryoballoon or 12 patients" into a ratio of 12.
        A fabricated number in front of the appraiser is worse than a missing one."""
        for text in ("cryoballoon or 12 patients were excluded",
                     "drug therapy or 3 months of follow-up",
                     "either ablation or 2 drugs",
                     "Or 5 patients withdrew"):
            with self.subTest(text=text):
                self.assertEqual(M.extract(text)["ratios"], [])

    def test_abbreviations_are_case_sensitive_but_names_are_not(self):
        self.assertTrue(M.extract("Hazard Ratio, 0.48")["ratios"])
        self.assertEqual(M.extract("hr 0.48")["ratios"], [])

    def test_a_full_results_sentence_partitions_correctly(self):
        found = M.extract("Recurrence 42.9% vs 67.8% (hazard ratio, 0.48; 95% CI, 0.35 to 0.66; P<0.001).")
        self.assertEqual(found["ratios"], ["hazard ratio, 0.48"])
        self.assertTrue(any("0.35" in v for v in found["confidence_intervals"]))
        self.assertEqual(found["percentages"], ["42.9%", "67.8%"])


class VietnameseAndUnicode(unittest.TestCase):
    def test_decimal_comma_p_value(self):
        """Vietnamese decimal commas are data, not typos."""
        found = M.extract("Khác biệt có ý nghĩa (p < 0,001).")
        self.assertTrue(any("0,001" in v for v in found["p_values"]),
                        f"decimal-comma p-value lost: {found['p_values']}")

    def test_decimal_comma_percentage(self):
        found = M.extract("Tỷ lệ tái phát 12,5% sau 12 tháng.")
        self.assertTrue(any("12,5" in v for v in found["percentages"]))

    def test_vietnamese_sample_size_noun(self):
        found = M.extract("Nghiên cứu trên 240 bệnh nhân rung nhĩ.")
        self.assertTrue(any("240" in v for v in found["sample_sizes"]))


class WordBoundaryGuards(unittest.TestCase):
    def test_journal_abbreviation_is_not_a_confidence_interval(self):
        """`\\bCI\\b` is what stops "Circ 2016;134" becoming an interval.

        Verified by mutation: drop the word boundary and this string yields
        ['Circ 2016;134']. "Circ" is the standard abbreviation for Circulation, so this
        is a citation line every cardiology store contains.
        """
        found = M.extract("Circ 2016;134:1-10.")
        self.assertEqual(found["confidence_intervals"], [])

    def test_drug_name_is_not_a_confidence_interval(self):
        """Same guard, second witness: without it this yields ['cin 500-750']."""
        found = M.extract("Ciprofloxacin 500-750 mg daily.")
        self.assertEqual(found["confidence_intervals"], [])

    def test_bare_ci_word_still_matches(self):
        found = M.extract("CI 0.60–0.96 for the primary outcome.")
        self.assertTrue(found["confidence_intervals"])


class MetadataScrubbing(unittest.TestCase):
    """Identifiers are scrubbed as SPANS, so a findings sentence keeps its own numbers."""

    STORE = """# Store

### [REF-001] Author 2024 — a trial
- **PMID/DOI:** PMID 40201666 / DOI 10.1001/jama.2024.1234 / NCT01234567
- **Retrieved:** 2026-06-15
- **Key findings:** Giảm 12,5% biến cố (Source: https://doi.org/10.1001/jama.2024.1234).
"""

    def _found(self):
        records = list(M.split_records(self.STORE))
        self.assertEqual(len(records), 1)
        return M.extract(records[0][2])

    def test_real_finding_survives_the_scrub(self):
        self.assertTrue(any("12,5" in v for v in self._found()["percentages"]),
                        "a finding ending in a DOI must keep its own number")

    def test_identifier_digits_never_become_data(self):
        blob = " ".join(v for vals in self._found().values() for v in vals)
        for leaked in ("40201666", "01234567", "2026-06-15"):
            self.assertNotIn(leaked, blob, f"metadata leaked into a bucket: {leaked}")


class RecordSplitting(unittest.TestCase):
    def test_structural_headers_are_not_records(self):
        text = "## Section 1 — overview\ntext\n\n### [REF-001] Author 2020 — a trial\n- N=100\n"
        ids = [cid for cid, _, _ in M.split_records(text)]
        self.assertEqual(ids, ["REF-001"])

    def test_citekey_forms(self):
        self.assertEqual(M.record_id("### [REF-042] Author"), "REF-042")
        self.assertEqual(M.record_id("### CBA-01 — Author 2021"), "CBA-01")


class EmptyBucketRendering(unittest.TestCase):
    def test_empty_bucket_says_none_not_a_placeholder(self):
        """An empty bucket must read as an absence, never as something to fill in."""
        records = [("REF-001", "### [REF-001] Author 2020", M.extract("No numbers here at all."))]
        out = M.render(records, "reference/test.md")
        self.assertIn("(none)", out)
        for placeholder in ("TODO", "N/A", "[?]", "CITATION_NEEDED", "TBD"):
            self.assertNotIn(placeholder, out)

    def test_all_five_buckets_always_rendered(self):
        records = [("REF-001", "### [REF-001] Author 2020", M.extract("N=100."))]
        out = M.render(records, "reference/test.md")
        for name in M.BUCKET_ORDER:
            self.assertIn(f"- {name}:", out)


class Determinism(unittest.TestCase):
    def test_identical_output_across_runs(self):
        body = "HR 0.96 (95% CI 0.76–1.22); p < 0,001; N=762; recurrence 34,6%."
        self.assertEqual(M.extract(body), M.extract(body))

    def test_values_are_deduplicated_in_first_seen_order(self):
        found = M.extract("N=100 in the first arm and N=100 in the second, then N=250.")
        self.assertEqual(found["sample_sizes"], ["N=100", "N=250"])


if __name__ == "__main__":
    unittest.main()
