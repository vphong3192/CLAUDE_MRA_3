"""End-to-end smoke run of the deterministic spine.

Why this exists: every script here was unit-tested in isolation and all of them passed while the
chain still had a real defect. Running the whole pipeline in the documented order found it in one
pass — the P2 ratio pattern matched only `HR 0.48`, so "hazard ratio, 0.48" (how journals actually
write it) never reached a bucket, and `\\bOR\\b` under IGNORECASE turned the English word "or" into
a fabricated ratio. Neither is visible from inside a single script's tests.

This runs the documented commands in the documented order, on a corpus small enough to assert
exact numbers, and checks that each stage's output is what the next stage expects.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

from harness import REPO, SKILLS

LR = SKILLS / "literature-retrieval" / "scripts"
CV = SKILLS / "citation-verification" / "scripts"
EA = SKILLS / "evidence-appraisal" / "scripts"

MCP_RECORDS = [
    {"record_id": "P1-001", "source": "pubmed", "search_id": "P1", "pmid": "33652425",
     "doi": "10.1056/NEJMoa2029980", "title": "Cryoballoon or Drug Therapy for Initial Treatment of Atrial Fibrillation",
     "authors": "Andrade JG", "year": 2021, "journal": "N Engl J Med",
     "abstract": "Cryoballoon ablation versus antiarrhythmic drug therapy for paroxysmal atrial fibrillation; recurrence outcomes.",
     "publication_types": ["Randomized Controlled Trial"], "retracted": False},
    {"record_id": "P1-002", "source": "pubmed", "search_id": "P1", "pmid": "37634145",
     "doi": "10.1056/NEJMoa2307291", "title": "Pulsed Field or Conventional Thermal Ablation for Paroxysmal Atrial Fibrillation",
     "authors": "Reddy VY", "year": 2023, "journal": "N Engl J Med",
     "abstract": "Pulsed field ablation versus cryoballoon ablation; freedom from recurrence in paroxysmal AF.",
     "publication_types": ["Randomized Controlled Trial"], "retracted": False},
    {"record_id": "E1-007", "source": "elicit", "search_id": "E1", "pmid": None,
     "doi": "10.1056/NEJMoa2029554", "title": "Cryoballoon Ablation as Initial Therapy for Atrial Fibrillation",
     "authors": "Wazni OM", "year": 2021, "journal": "NEJM",
     "abstract": "First-line cryoablation versus drug therapy; atrial fibrillation recurrence.",
     "publication_types": ["RCT"], "retracted": False},
]

STORE = """# Reference Store — smoke

### [REF-001] Andrade 2021 — Cryoballoon or Drug Therapy
- **PMID/DOI:** PMID 33652425 / DOI 10.1056/NEJMoa2029980
- **Key findings:** Atrial tachyarrhythmia recurrence occurred in 42.9% of the ablation group and in 67.8% of the antiarrhythmic drug group (hazard ratio, 0.48; 95% CI, 0.35 to 0.66; P<0.001).

### [REF-002] Reddy 2023 — Pulsed Field or Conventional Thermal Ablation
- **PMID/DOI:** PMID 37634145 / DOI 10.1056/NEJMoa2307291
- **Key findings:** The primary efficacy end point was met in 73.3% of patients in the pulsed field group and 71.3% in the cryoballoon group.
"""

DRAFT = """# Triệt đốt rung nhĩ kịch phát (smoke)

## Đồng thuận đã xác lập
Tái phát 42,9% so với 67,8% (hazard ratio, 0,48; 95% CI, 0,35 to 0,66; P<0,001) [1].

## Còn tranh cãi
Tiêu chí hiệu quả chính đạt 73,3% so với 71,3% [2].

## Tài liệu tham khảo
1. Andrade JG, et al. N Engl J Med. 2021. PMID: [33652425](https://pubmed.ncbi.nlm.nih.gov/33652425/).
2. Reddy VY, et al. N Engl J Med. 2023. PMID: [37634145](https://pubmed.ncbi.nlm.nih.gov/37634145/).
"""

CARDS = [
    {"card_id": "REF-001-c1", "study_id": "pmid:33652425",
     "source_file": "33652425_Andrade_2021.html", "tier": "fulltext",
     "claim": "Tái phát 42,9% so với 67,8% (HR 0,48; KTC 95% 0,35–0,66; p<0,001).",
     "quote": "Atrial tachyarrhythmia recurrence occurred in 42.9% of the ablation group and in "
              "67.8% of the antiarrhythmic drug group (hazard ratio, 0.48; 95% CI, 0.35 to 0.66; P<0.001).",
     "abstract": "In this trial, initial treatment with cryoballoon ablation was compared with "
                 "antiarrhythmic drug therapy in patients with symptomatic paroxysmal atrial fibrillation."},
]


class DeterministicSpine(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        cls.tmp = pathlib.Path(tempfile.mkdtemp())
        cls.ws = cls.tmp / "_workspace"
        cls.src = cls.tmp / "source" / "afib"
        (cls.src / "_exports").mkdir(parents=True)
        cls.ws.mkdir()
        (cls.tmp / "reference").mkdir()

        fx = LR / "fixtures"
        for name in ("scopus_2026-09-05.ris", "wos_2026-09-05.csv"):
            shutil.copy(fx / "exports" / name, cls.src / "_exports" / name)
        manifest = json.loads((fx / "exports_manifest.json").read_text(encoding="utf-8"))
        manifest["exports"] = [e for e in manifest["exports"]
                               if e["file"].endswith((".ris", ".csv"))]
        (cls.src / "_exports" / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        for f in (CV / "fixtures" / "source_sample").glob("*.html"):
            shutil.copy(f, cls.src / f.name)

        (cls.ws / "01a_concepts.json").write_text(
            (fx / "concepts_sample.json").read_text(encoding="utf-8"), encoding="utf-8")
        (cls.ws / "02b_records_mcp.jsonl").write_text(
            "".join(json.dumps(r) + "\n" for r in MCP_RECORDS), encoding="utf-8")
        (cls.tmp / "reference" / "afib.md").write_text(STORE, encoding="utf-8")
        (cls.ws / "06_final_review.md").write_text(DRAFT, encoding="utf-8")
        (cls.ws / "04b_cards.jsonl").write_text(
            "".join(json.dumps(c) + "\n" for c in CARDS), encoding="utf-8")
        cls.failures = []

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def run_step(self, script, *args, expect=0):
        cmd = [sys.executable, str(script), *[str(a) for a in args]]
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO))
        self.assertEqual(r.returncode, expect,
                         f"{script.name} exited {r.returncode}\nSTDERR: {r.stderr[:600]}")
        return r.stdout

    def lines(self, path):
        return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]

    def test_01_import_external_exports(self):
        self.run_step(LR / "import_external.py",
                      "--export-dir", self.src / "_exports",
                      "--manifest", self.src / "_exports" / "manifest.json",
                      "--out-records", self.ws / "02b_records_external.jsonl",
                      "--out", self.ws / "02b_import.md")
        self.assertEqual(len(self.lines(self.ws / "02b_records_external.jsonl")), 4)

    def test_02_concatenate_the_record_stream(self):
        combined = (self.ws / "02b_records_mcp.jsonl").read_text(encoding="utf-8") + \
                   (self.ws / "02b_records_external.jsonl").read_text(encoding="utf-8")
        (self.ws / "02b_records.jsonl").write_text(combined, encoding="utf-8")
        self.assertEqual(len(self.lines(self.ws / "02b_records.jsonl")), 7)

    def test_03_dedupe_merges_across_sources(self):
        self.run_step(LR / "dedupe_records.py",
                      "--records", self.ws / "02b_records.jsonl",
                      "--out-studies", self.ws / "02c_studies.jsonl",
                      "--out", self.ws / "02d_dedup.md")
        studies = self.lines(self.ws / "02c_studies.jsonl")
        self.assertEqual(len(studies), 4, "7 records from 3 sources collapse to 4 studies")
        multi = [s for s in studies if s["members"] > 1]
        self.assertTrue(multi, "the same trial arriving from MCP and an export must merge")

    def test_04_prefilter_screens_a_small_pool_whole(self):
        self.run_step(LR / "prefilter_records.py",
                      "--studies", self.ws / "02c_studies.jsonl",
                      "--concepts", self.ws / "01a_concepts.json",
                      "--out-candidates", self.ws / "02e_candidates.jsonl",
                      "--out-deferred", self.ws / "02f_deferred.jsonl",
                      "--out", self.ws / "02g_worksheet.md")
        self.assertEqual(len(self.lines(self.ws / "02e_candidates.jsonl")), 4)
        self.assertEqual(self.lines(self.ws / "02f_deferred.jsonl"), [],
                         "a 4-study pool is under every floor — nothing may be deferred")

    def test_05_prisma_counts_the_stage_files(self):
        verdicts = [{"study_id": s["study_id"], "verdict": "include" if i < 3 else "exclude",
                     "reason": "" if i < 3 else "wrong comparator"}
                    for i, s in enumerate(self.lines(self.ws / "02e_candidates.jsonl"))]
        (self.ws / "02h_verdicts.jsonl").write_text(
            "".join(json.dumps(v) + "\n" for v in verdicts), encoding="utf-8")
        self.run_step(LR / "prisma_flow.py",
                      "--records", self.ws / "02b_records.jsonl",
                      "--studies", self.ws / "02c_studies.jsonl",
                      "--candidates", self.ws / "02e_candidates.jsonl",
                      "--deferred", self.ws / "02f_deferred.jsonl",
                      "--verdicts", self.ws / "02h_verdicts.jsonl",
                      "--out-json", self.ws / "02i_prisma.json",
                      "--out", self.ws / "02j_prisma.md")
        flow = json.loads((self.ws / "02i_prisma.json").read_text(encoding="utf-8"))
        self.assertEqual(flow["warnings"], [], "the flow must add up")
        st = flow["stages"]
        self.assertEqual(st["identified"], 7)
        self.assertEqual(st["duplicates_removed"], 3)
        self.assertEqual(st["included"], 3)
        self.assertEqual(st["identified_databases_registers"], 7,
                         "hand-exported database searches are still database searches")

    def test_06_extract_numbers_reaches_the_effect_estimate(self):
        """The integration defect that started this file: 'hazard ratio, 0.48' must reach a bucket."""
        out = self.run_step(EA / "extract_numbers.py",
                            "--store", self.tmp / "reference" / "afib.md",
                            "--out", self.ws / "04a_numbers.md")
        text = (self.ws / "04a_numbers.md").read_text(encoding="utf-8")
        self.assertIn("hazard ratio, 0.48", text)
        self.assertIn("42.9%", text)
        self.assertIn("95% CI, 0.35 to 0.66", text)

    def test_07_quote_locks_accept_a_sound_card(self):
        self.run_step(CV / "verify_quotes.py",
                      "--cards", self.ws / "04b_cards.jsonl",
                      "--source-dir", self.src,
                      "--out", self.ws / "04c_quote_locks.md")
        self.assertIn("REJECTED: 0", (self.ws / "04c_quote_locks.md").read_text(encoding="utf-8"))

    def test_08_citation_audit_passes_a_vietnamese_draft(self):
        """A Vietnamese draft with decimal commas, audited against an English store."""
        self.run_step(CV / "citation_audit.py",
                      "--draft", self.ws / "06_final_review.md",
                      "--store", self.tmp / "reference" / "afib.md",
                      "--out", self.ws / "06b_citation_audit.md")
        report = (self.ws / "06b_citation_audit.md").read_text(encoding="utf-8")
        self.assertIn("VERDICT: PASS", report)
        self.assertIn("HARD-FAIL findings (0)", report)


if __name__ == "__main__":
    unittest.main()
