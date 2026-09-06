"""P7 — importing author-supplied bibliographic exports.

The harness cannot reach Scopus, Web of Science, Embase or CENTRAL, and must not try: an
automated agent using someone's institutional subscription breaks their licence. The author
exports; this reads the file. Two things decide whether that is rigorous or merely convenient —
the manifest that records the search, and the truncation check that catches a capped download.
"""
import json
import pathlib
import tempfile
import unittest

from harness import load

M = load("literature-retrieval/scripts/import_external.py")
FIX = pathlib.Path(M.__file__).parent / "fixtures"
EXPORTS = FIX / "exports"
MANIFEST = FIX / "exports_manifest.json"


def run(export_dir=EXPORTS, manifest=MANIFEST):
    return M.import_dir(export_dir, manifest)


def by_label(records, label):
    return [r for r in records if r["source"] == f"external:{label}"]


class EveryFormatParses(unittest.TestCase):
    def test_all_four_formats_produce_records(self):
        records, per_file, errors = run()
        self.assertEqual(errors, [])
        self.assertEqual({f["kind"] for f in per_file}, {"ris", "csv", "nbib", "bibtex"})
        for label in ("scopus", "wos", "embase", "central"):
            self.assertTrue(by_label(records, label), f"{label} produced no records")

    def test_ris_pulls_identifiers_and_folded_abstract(self):
        rec = by_label(run()[0], "scopus")[0]
        self.assertEqual(rec["pmid"], "33652425")
        self.assertEqual(rec["doi"], "10.1056/NEJMoa2029980")
        self.assertEqual(rec["year"], 2021)
        self.assertIn("paroxysmal atrial fibrillation", rec["abstract"],
                      "text from a WRAPPED continuation line must be folded in, not dropped — "
                      "a truncated abstract loses recall silently in concept matching")
        self.assertTrue(rec["abstract"].endswith("."),
                        "an abstract cut at the first physical line has no terminal period")

    def test_nbib_pulls_doi_out_of_the_lid_tag(self):
        """PubMed/Embase put the DOI in `LID - 10.x/y [doi]`, never in a DOI field."""
        rec = by_label(run()[0], "embase")[0]
        self.assertEqual(rec["pmid"], "37634145")
        self.assertEqual(rec["doi"], "10.1056/NEJMoa2307291")

    def test_nbib_flags_a_retracted_publication_type(self):
        retracted = [r for r in by_label(run()[0], "embase") if r["retracted"]]
        self.assertEqual(len(retracted), 1)
        self.assertEqual(retracted[0]["doi"], "10.1093/europace/euz111")

    def test_csv_header_aliases(self):
        """WoS writes "Article Title" and "PubMed Id"; Scopus writes "Title" and "PubMed ID"."""
        recs = by_label(run()[0], "wos")
        self.assertEqual({r["pmid"] for r in recs}, {"27042964", "33197159"})
        self.assertTrue(all(r["title"] and r["journal"] for r in recs))

    def test_bibtex_entry(self):
        rec = by_label(run()[0], "central")[0]
        self.assertEqual(rec["doi"], "10.1056/NEJMoa2029980")
        self.assertEqual(rec["year"], 2021)


class RecordsJoinThePipelineUnchanged(unittest.TestCase):
    def test_schema_matches_what_p4_consumes(self):
        for rec in run()[0]:
            for field in ("record_id", "source", "search_id", "pmid", "doi", "title",
                          "year", "abstract", "publication_types", "prisma_column"):
                self.assertIn(field, rec)

    def test_provenance_is_recorded_as_user_export(self):
        self.assertTrue(all(r["provenance"] == "user_export" for r in run()[0]))

    def test_record_ids_are_stable_and_unique(self):
        ids = [r["record_id"] for r in run()[0]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(ids, [r["record_id"] for r in run()[0]])


class ManifestIsMandatory(unittest.TestCase):
    """An export carries records but not the search that produced them."""

    def _dir_with(self, manifest, filename="scopus_2026-09-05.ris"):
        tmp = pathlib.Path(tempfile.mkdtemp())
        (tmp / filename).write_text((EXPORTS / "scopus_2026-09-05.ris").read_text(encoding="utf-8"),
                                    encoding="utf-8")
        mpath = tmp / "manifest.json"
        mpath.write_text(json.dumps(manifest), encoding="utf-8")
        return tmp, mpath

    def _entry(self, **over):
        base = {"file": "scopus_2026-09-05.ris", "label": "scopus", "database": "Scopus",
                "query_string": "TITLE-ABS-KEY(x)", "date_searched": "2026-09-05",
                "n_reported": 2, "prisma_column": "database"}
        base.update(over)
        return base

    def test_file_with_no_entry_is_an_error_not_a_silent_import(self):
        d, m = self._dir_with({"exports": []})
        records, _, errors = M.import_dir(d, m)
        self.assertEqual(records, [], "nothing may be imported from an unrecorded search")
        self.assertTrue(any("no manifest entry" in e for e in errors))

    REQUIRED = ("file", "label", "database", "query_string", "date_searched",
                "n_reported", "prisma_column")

    def test_the_required_set_is_pinned(self):
        """Named explicitly, not read from the module — shrinking the tuple must fail here,
        not quietly shrink the loop below."""
        self.assertEqual(tuple(M.REQUIRED_MANIFEST_FIELDS), self.REQUIRED)

    def test_every_prisma_s_field_is_required(self):
        for field in self.REQUIRED:
            with self.subTest(missing=field):
                entry = self._entry()
                del entry[field]
                d, m = self._dir_with({"exports": [entry]})
                self.assertTrue(M.import_dir(d, m)[2], f"missing {field} must be an error")

    def test_prisma_column_must_be_a_valid_value(self):
        d, m = self._dir_with({"exports": [self._entry(prisma_column="databases")]})
        self.assertTrue(any("prisma_column" in e for e in M.import_dir(d, m)[2]))

    def test_n_reported_must_be_an_integer(self):
        d, m = self._dir_with({"exports": [self._entry(n_reported="about 400")]})
        self.assertTrue(any("n_reported" in e for e in M.import_dir(d, m)[2]))


class TruncationIsSurfaced(unittest.TestCase):
    """Most platforms cap a single download well below the result count. Silently importing the
    cap as if it were the whole result set is the commonest recall loss in a manual export."""

    def test_a_short_file_is_flagged(self):
        _, per_file, _ = run()
        embase = next(f for f in per_file if f["label"] == "embase")
        self.assertLess(embase["n_parsed"], embase["n_reported"])

    def test_the_shortfall_marker_reaches_the_table(self):
        """The per-file table must mark the short row, not only the prose below it."""
        records, per_file, errors = run()

        class Args:
            export_dir, manifest = str(EXPORTS), str(MANIFEST)
        row = next(l for l in M.render(records, per_file, errors, Args()).splitlines()
                   if "embase_2026-09-05.nbib" in l)
        self.assertIn("⚠", row)

    def test_the_report_names_the_shortfall(self):
        records, per_file, errors = run()

        class Args:
            export_dir, manifest = str(EXPORTS), str(MANIFEST)
        text = M.render(records, per_file, errors, Args())
        self.assertIn("Truncated exports", text)
        self.assertIn("3 missing", text)

    def test_the_search_strategy_table_is_written_for_the_methods_section(self):
        records, per_file, errors = run()

        class Args:
            export_dir, manifest = str(EXPORTS), str(MANIFEST)
        text = M.render(records, per_file, errors, Args())
        self.assertIn("TITLE-ABS-KEY", text)
        self.assertIn("Web of Science Core Collection", text)


class NoNetworkAccess(unittest.TestCase):
    def test_the_module_never_queries_a_platform(self):
        """Reading a file is licensed; an agent querying the subscription is not."""
        src = pathlib.Path(M.__file__).read_text(encoding="utf-8")
        for token in ("urllib", "http.client", "socket", "requests", "fetch("):
            self.assertNotIn(f"import {token}", src)


class Determinism(unittest.TestCase):
    def test_identical_across_runs(self):
        self.assertEqual(run(), run())


if __name__ == "__main__":
    unittest.main()
