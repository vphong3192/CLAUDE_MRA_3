"""Rubric arithmetic — snapping to the grid, box ceilings, weights, bands, Law-1 AUTO-FAIL.

The script exists because the verifier reported 0.82 on a run the rubric scores 0.80 (Entry #11):
off-grid scores err upward, so every guarantee here is about never rounding in the review's favour.
The weights, box counts and band floors are asserted against rubric.md itself, so the script and
the document cannot drift apart silently.
"""
import contextlib
import io
import re
import unittest

from harness import SKILLS, load

M = load("citation-verification/scripts/rubric_total.py")
RUBRIC = (SKILLS / "citation-verification" / "references" / "rubric.md").read_text(encoding="utf-8")

ALL_PASS = {c: f"{n}/{n}" for c, n in M.BOXES.items()}


def scores(**kw):
    base = {c: "0.8" for c in M.CRITERIA}
    base.update({k: str(v) for k, v in kw.items()})
    return base


def final(rows, crit):
    return next(r["final"] for r in rows if r["crit"] == crit)


class MatchesRubricDocument(unittest.TestCase):
    def test_weights_match_the_formula(self):
        m = re.search(r"Score = (.+)", RUBRIC)
        doc = {f"T{n}": round(float(w) * 100) for w, n in re.findall(r"([\d.]+)·T(\d)", m.group(1))}
        self.assertEqual(doc, M.WEIGHTS)
        self.assertEqual(sum(M.WEIGHTS.values()), 100)

    def test_box_counts_match_each_criterion(self):
        sections = re.split(r"^## Criterion (\d)", RUBRIC, flags=re.MULTILINE)[1:]
        doc = {f"T{n}": body.count("- [ ]") for n, body in zip(sections[::2], sections[1::2])}
        self.assertEqual(doc, M.BOXES)

    def test_band_floors_match(self):
        self.assertIn("≥0.85 EXCEEDED", RUBRIC)
        self.assertIn("0.70–0.84 MET", RUBRIC)
        self.assertIn("0.60–0.69 ADEQUATE", RUBRIC)
        self.assertIn("0.50–0.59 BELOW", RUBRIC)
        self.assertEqual(dict((n, f) for f, n in M.BANDS),
                         {"EXCEEDED": 850, "MET": 700, "ADEQUATE": 600, "BELOW": 500, "FAIL": 0})


class Snapping(unittest.TestCase):
    def test_entry_11_case(self):
        """The run that motivated the script: 0.9 is off-grid, the rubric total is 0.80 not 0.82."""
        rows, total, reported, band = M.score(scores(T5=0.9, T6=0.9), ALL_PASS)
        self.assertEqual((final(rows, "T5"), final(rows, "T6")), (0.8, 0.8))
        self.assertEqual(total, 800)
        self.assertEqual(round(reported), 820)
        self.assertEqual(band, "MET")

    def test_always_rounds_down(self):
        for raw, want in [("0.75", 0.6), ("0.99", 0.8), ("0.41", 0.4), ("0.2", 0.2)]:
            with self.subTest(raw=raw):
                rows, *_ = M.score(scores(T3=raw), ALL_PASS)
                self.assertEqual(final(rows, "T3"), want)

    def test_on_grid_values_are_untouched(self):
        """A grid value is never moved, and every two-decimal score floors to the right tenth."""
        for x in range(20, 101):
            raw = f"{x / 100:.2f}"
            with self.subTest(raw=raw):
                rows, *_ = M.score(scores(T4=raw), ALL_PASS)
                self.assertEqual(final(rows, "T4"), max(g for g in (0.2, 0.4, 0.6, 0.8, 1.0)
                                                        if g <= x / 100 + 1e-12))
        for raw in ("0.2", "0.4", "0.6", "0.8", "1.0"):
            with self.subTest(raw=raw):
                rows, *_ = M.score(scores(T4=raw), ALL_PASS)
                self.assertEqual(final(rows, "T4"), float(raw))
                self.assertEqual(next(r for r in rows if r["crit"] == "T4")["reasons"], [])

    def test_vietnamese_decimal_comma(self):
        rows, *_ = M.score(scores(T2="0,8"), ALL_PASS)
        self.assertEqual(final(rows, "T2"), 0.8)

    def test_below_lowest_level_is_an_error(self):
        with self.assertRaises(ValueError):
            M.score(scores(T3=0.1), ALL_PASS)


class BoxEvidence(unittest.TestCase):
    def test_no_one_point_zero_without_every_box(self):
        boxes = dict(ALL_PASS, T3="5/6")
        rows, *_ = M.score(scores(T3=1.0), boxes)
        self.assertEqual(final(rows, "T3"), 0.8)

    def test_one_point_zero_with_every_box_stands(self):
        rows, *_ = M.score(scores(T3=1.0), ALL_PASS)
        self.assertEqual(final(rows, "T3"), 1.0)

    def test_t1_and_t2_box_ceilings(self):
        for crit, boxes, raw, want in [("T1", "6/7", 1.0, 0.8), ("T1", "5/7", 0.8, 0.6),
                                       ("T1", "3/7", 0.8, 0.6), ("T2", "4/5", 1.0, 0.8),
                                       ("T2", "3/5", 0.8, 0.6)]:
            with self.subTest(crit=crit, boxes=boxes):
                rows, *_ = M.score(scores(**{crit: raw}), dict(ALL_PASS, **{crit: boxes}))
                self.assertEqual(final(rows, crit), want)

    def test_a_ceiling_never_raises(self):
        rows, *_ = M.score(scores(T1=0.4), dict(ALL_PASS, T1="6/7"))
        self.assertEqual(final(rows, "T1"), 0.4)

    def test_boxes_are_required(self):
        boxes = dict(ALL_PASS)
        del boxes["T4"]
        with self.assertRaises(ValueError):
            M.score(scores(), boxes)

    def test_wrong_box_total_is_rejected(self):
        with self.assertRaises(ValueError):
            M.score(scores(), dict(ALL_PASS, T1="6/6"))


class TotalsAndLaw1(unittest.TestCase):
    def test_band_edges_are_exact(self):
        """0.85 is EXCEEDED; float arithmetic must not leave it at 0.8499…"""
        # T1..T6 = 1.0,0.8,0.8,1.0,0.8,0.8 → 0.25+0.16+0.16+0.15+0.08+0.08 = 0.88
        rows, total, _, band = M.score(scores(T1=1.0, T4=1.0), ALL_PASS)
        self.assertEqual((total, band), (880, "EXCEEDED"))
        # all 0.6 except T1=1.0, T2=1.0: 0.25+0.2+0.12+0.09+0.06+0.06 = 0.78
        rows, total, _, band = M.score(
            {"T1": "1", "T2": "1", "T3": "0.6", "T4": "0.6", "T5": "0.6", "T6": "0.6"}, ALL_PASS)
        self.assertEqual((total, band), (780, "MET"))
        rows, total, _, band = M.score({c: "0.6" for c in M.CRITERIA}, ALL_PASS)
        self.assertEqual((total, band), (600, "ADEQUATE"))

    def test_fabricated_citation_auto_fails_regardless_of_total(self):
        rows, total, _, band = M.score({c: "1.0" for c in M.CRITERIA}, ALL_PASS, fabricated=True)
        self.assertEqual(final(rows, "T5"), 0.0)
        self.assertEqual(band, "AUTO-FAIL")

    def test_exit_codes(self):
        args = sum([["--score", f"{c}=0.8", "--boxes", f"{c}={ALL_PASS[c]}"] for c in M.CRITERIA], [])
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(M.main(args), 0)
            self.assertEqual(M.main(args + ["--fabricated"]), 1)
            self.assertEqual(M.main(args[:4]), 2)

    def test_deterministic(self):
        a = M.render(*M.score(scores(T5=0.9), ALL_PASS))
        b = M.render(*M.score(scores(T5=0.9), ALL_PASS))
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
