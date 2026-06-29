# Search Log (PRISMA-ready) — fixture (valid ledger)

**Run date:** 2026-06-29 · Retriever: evidence-retriever agent.

## Recall & reproducibility ledger (P3)

| id | source | query | call | total_count | retrieved | recall |
|----|--------|-------|------|-------------|-----------|--------|
| P1 | PubMed | ablation index AND PVI | esearch db=pubmed term="ablation+index AND PVI" retmax=200 | 148 | 148 | retrieved==total ✓ |
| P3 | PubMed | contact force AND PVI/RF/AF | esearch db=pubmed term="contact+force AND PVI" retmax=500 | 732 | 500 | capped ⚠ (500/732; landmark-filtered, see §4) |
| C1 | Consensus | ablation index vs contact force outcomes | search query="ablation index vs contact force PVI outcomes" page=1..2 | 20 | 20 | complete ✓ |
| T1 | ClinicalTrials.gov | AI/LSI/impedance ablation AF | https://clinicaltrials.gov/api/v2/studies?query.term=ablation+index+AF | 12 | 12 | retrieved==total ✓ |
