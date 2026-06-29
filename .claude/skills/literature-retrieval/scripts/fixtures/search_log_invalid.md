# Search Log (PRISMA-ready) — fixture (invalid ledger, defects injected)

**Run date:** 2026-06-29 · Retriever: evidence-retriever agent.

## Recall & reproducibility ledger (P3)

| id | source | query | call | total_count | retrieved | recall |
|----|--------|-------|------|-------------|-----------|--------|
| P1 | PubMed | ablation index AND PVI | ablation index AND PVI | 148 | 148 | retrieved==total ✓ |
| P3 | PubMed | contact force AND PVI | esearch db=pubmed term="contact+force" retmax=500 | 732 | 500 | retrieved==total ✓ |
| C2 | Consensus | LSI durable PVI outcomes | search query="LSI durable PVI" page=1 | 10/20 | 10 | capped ⚠ |
| G1 | PubMed | contradiction set | esearch db=pubmed term="CF AND AI discordant" retmax=50 | 20 |  | capped ⚠ |
| T9 | ClinicalTrials.gov | ongoing AI trials | https://clinicaltrials.gov/api/v2/studies?query.term=AI+AF | 5 | 5 | done |
