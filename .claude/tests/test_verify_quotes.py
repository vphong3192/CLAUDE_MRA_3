"""P8 — verbatim quote & number locks.

P1 proves a citation is traceable; this proves the quote is really in the file on disk and that
the claim's numbers are in that quote. Each lock gets its own test, because each names a distinct
way a claim detaches from its source — and one of them (IDENTITY) names the failure the other
four structurally cannot see.
"""
import json
import pathlib
import tempfile
import unittest

from harness import load

M = load("citation-verification/scripts/verify_quotes.py")
FIX = pathlib.Path(M.__file__).parent / "fixtures"
SRC = FIX / "source_sample"
ABSTRACTS = json.loads((FIX / "abstracts_sample.json").read_text(encoding="utf-8"))

QUOTE = ("Atrial tachyarrhythmia recurrence occurred in 42.9% of the ablation group and in 67.8% "
         "of the antiarrhythmic drug group (hazard ratio, 0.48; 95% CI, 0.35 to 0.66; P<0.001).")


def card(**kw):
    base = {"card_id": "T", "study_id": "pmid:33652425", "tier": "fulltext",
            "source_file": "33652425_Andrade_2021.html",
            "claim": "Recurrence 42.9% versus 67.8%.", "quote": QUOTE}
    base.update(kw)
    return base


def locks(c, abstracts=None):
    return {lock for lock, _ in M.check_card(c, SRC, abstracts if abstracts is not None else ABSTRACTS)}


class CleanCardPasses(unittest.TestCase):
    def test_no_locks_trip(self):
        self.assertEqual(locks(card()), set())

    def test_fixture_file_passes_end_to_end(self):
        results = [M.check_card(c, SRC, ABSTRACTS)
                   for c in M.read_cards(FIX / "cards_clean.jsonl")]
        self.assertTrue(results)
        self.assertEqual([f for f in results if f], [], "the clean fixture must accept every card")

    def test_rejected_fixture_trips_every_lock_it_is_built_for(self):
        tripped = set()
        for c in M.read_cards(FIX / "cards_rejected.jsonl"):
            tripped |= {lock for lock, _ in M.check_card(c, SRC, ABSTRACTS)}
        for lock in ("IDENTITY", "QUOTE", "NUMBER", "LENGTH", "FULLTEXT"):
            self.assertIn(lock, tripped)


class VietnameseDecimalCommas(unittest.TestCase):
    """The default output language writes 42,9% where the English source writes 42.9%.

    A lock comparing strings would reject every correctly-transcribed Vietnamese claim, which is
    the fastest way to get a lock switched off.
    """

    def test_comma_decimal_claim_matches_period_decimal_source(self):
        vi = ("Tái phát xảy ra ở 42,9% nhóm triệt đốt so với 67,8% nhóm thuốc "
              "(HR 0,48; KTC 95% 0,35–0,66; p<0,001).")
        self.assertEqual(locks(card(claim=vi)), set())

    def test_canonical_number_equivalences(self):
        self.assertEqual(M.canonical_number("0,76"), M.canonical_number("0.76"))
        self.assertEqual(M.canonical_number("1,234"), M.canonical_number("1234"))
        self.assertEqual(M.canonical_number("42,9"), "42.9")

    def test_a_genuinely_different_number_is_still_caught(self):
        """Normalising commas must not blur 0.48 into 0.84."""
        self.assertIn("NUMBER", locks(card(claim="Hazard ratio 0,84.")))


class EachLock(unittest.TestCase):
    def test_number_absent_from_its_own_quote(self):
        """The number is nowhere in the quote the claim rests on — even if it were in the paper."""
        self.assertIn("NUMBER", locks(card(claim="Absolute risk reduction was 31,2%.")))

    def test_quote_not_literally_in_the_file(self):
        altered = QUOTE.replace("ablation group", "ablation arm")
        self.assertIn("QUOTE", locks(card(quote=altered)))

    def test_quote_attached_to_the_wrong_paper(self):
        """A real quote on the wrong citation — the failure the other locks cannot see."""
        self.assertIn("IDENTITY", locks(card(study_id="pmid:37634145")))

    def test_missing_source_file(self):
        self.assertIn("IDENTITY", locks(card(source_file="nope.html")))

    def test_card_without_an_identifier_cannot_prove_identity(self):
        self.assertIn("IDENTITY", locks(card(study_id="", pmid=None)))

    def test_quote_too_short(self):
        self.assertIn("LENGTH", locks(card(claim="3,2%.", quote="in 3.2% of patients", tier="abstract")))

    def test_quote_too_long(self):
        long_quote = QUOTE + " " + "x" * M.MAX_QUOTE_CHARS
        self.assertIn("LENGTH", locks(card(quote=long_quote)))

    def test_fulltext_card_quoting_only_the_abstract(self):
        abstract_line = ("initial treatment with cryoballoon ablation was compared with "
                         "antiarrhythmic drug therapy in patients with symptomatic paroxysmal "
                         "atrial fibrillation")
        self.assertIn("FULLTEXT", locks(card(claim="So sánh cryoballoon với thuốc.",
                                             quote=abstract_line)))

    def test_the_same_quote_is_fine_when_the_card_does_not_claim_fulltext(self):
        abstract_line = ("initial treatment with cryoballoon ablation was compared with "
                         "antiarrhythmic drug therapy in patients with symptomatic paroxysmal "
                         "atrial fibrillation")
        self.assertNotIn("FULLTEXT", locks(card(claim="So sánh cryoballoon với thuốc.",
                                                quote=abstract_line, tier="abstract")))


class AbstractSourceForTheFulltextLock(unittest.TestCase):
    """The abstract travels ON the card, so no fourth artifact duplicates what the store holds."""

    ABSTRACT_LINE = ("initial treatment with cryoballoon ablation was compared with antiarrhythmic "
                     "drug therapy in patients with symptomatic paroxysmal atrial fibrillation")

    def test_card_carries_its_own_abstract(self):
        c = card(claim="So sánh cryoballoon với thuốc.", quote=self.ABSTRACT_LINE,
                 abstract="In this trial, " + self.ABSTRACT_LINE + ".")
        self.assertIn("FULLTEXT", locks(c, abstracts={}))

    def test_without_any_abstract_the_lock_stays_silent_rather_than_guessing(self):
        c = card(claim="So sánh cryoballoon với thuốc.", quote=self.ABSTRACT_LINE)
        self.assertNotIn("FULLTEXT", locks(c, abstracts={}))


class BoundsArePinned(unittest.TestCase):
    def test_values(self):
        self.assertEqual((M.MIN_QUOTE_CHARS, M.MAX_QUOTE_CHARS), (40, 1500))


class NormalisationBoundary(unittest.TestCase):
    """Normalisation is what "verbatim" is allowed to forgive. Anything more lets a merely
    similar quote pass, which is the entire thing being prevented."""

    def test_forgives_whitespace_entities_and_typography(self):
        noisy = QUOTE.replace("antiarrhythmic drug", "antiarrhythmic \n  drug") \
                     .replace("0.35 to 0.66", "0.35 to 0.66")
        self.assertEqual(locks(card(quote=noisy)), set())

    def test_does_not_fold_case(self):
        self.assertIn("QUOTE", locks(card(quote=QUOTE.upper())))

    def test_does_not_forgive_a_changed_word(self):
        self.assertIn("QUOTE", locks(card(quote=QUOTE.replace("recurrence", "occurrence"))))

    def test_embedded_json_metadata_is_not_quotable(self):
        """Publisher HTML embeds JSON-LD. Without the script/style skip it becomes quotable, and
        a card could cite machine metadata as though it were the authors' prose."""
        from_metadata = ("Cryoablation reduced recurrence by 24.9 percentage points in this analysis.")
        self.assertIn("QUOTE", locks(card(claim="Giảm 24,9 điểm phần trăm.", quote=from_metadata)))

    def test_the_metadata_string_really_is_in_the_raw_file(self):
        """Proves the test above discriminates: the string IS in the file, just not in its prose."""
        raw = (SRC / "33652425_Andrade_2021.html").read_text(encoding="utf-8")
        self.assertIn("24.9 percentage points", raw)


class PdfIsOutOfScope(unittest.TestCase):
    def test_pdf_is_refused_with_an_actionable_message(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            (tmp / "paper.pdf").write_bytes(b"%PDF-1.4 not readable by stdlib")
            fails = M.check_card(card(source_file="paper.pdf"), tmp, {})
        self.assertEqual({lock for lock, _ in fails}, {"IDENTITY"})
        self.assertIn("convert", " ".join(d for _, d in fails).lower())


class ExitCodeContract(unittest.TestCase):
    def _rc(self, cards_file):
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            return M.main(["--cards", str(FIX / cards_file), "--source-dir", str(SRC),
                           "--abstracts", str(FIX / "abstracts_sample.json")])

    def test_clean_exits_zero(self):
        self.assertEqual(self._rc("cards_clean.jsonl"), 0)

    def test_any_rejection_exits_one(self):
        self.assertEqual(self._rc("cards_rejected.jsonl"), 1)


class Determinism(unittest.TestCase):
    def test_identical_across_runs(self):
        c = card()
        self.assertEqual(M.check_card(c, SRC, ABSTRACTS), M.check_card(c, SRC, ABSTRACTS))


if __name__ == "__main__":
    unittest.main()
