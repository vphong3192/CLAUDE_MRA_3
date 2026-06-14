# Search Log (PRISMA-ready) — Ablation Metrics in RF-PVI for AF

**Run date:** 2026-06-14 · **Date window:** 2015–2026 (landmark CF trials pre-2015 retained as context).
**Retriever:** evidence-retriever agent. **Protocol:** `_workspace/00_protocol.md`.

---

## 0. source/ folder reconciliation (L-012)

- **Checked:** YES. `/home/user/CLAUDE_MRA_2/source/` **does not exist** (no subfolders, no files).
- **User-supplied PDFs:** none this run.
- **Action for orchestrator:** ask the user whether any paywalled full-text PDFs should be placed in
  `source/<folder>/` — especially relevant because full-text retrieval tools were unavailable (below).
- **Records added/upgraded from source/:** 0 (none available).

## 0b. TOOL AVAILABILITY / ERRORS (transparency — Error Handling section)

| Tool | Status | Effect |
|---|---|---|
| `mcp__PubMed__search_articles` | OK (permitted) | Used for all PMID-list searches + L-009 title confirmation |
| `mcp__Consensus__search` | OK (permitted; intermittent rate-limit) | Primary metadata + abstract source |
| `mcp__PubMed__get_article_metadata` | **DENIED** | Could not pull titles/authors via PubMed; worked around via Consensus + title-confirm |
| `mcp__PubMed__get_full_text_article` | **DENIED** | **No full text retrieved** — appraiser must re-fetch (L-005 numbers provisional) |
| `mcp__PubMed__convert_article_ids` | **DENIED** | Could not map PMID→PMCID |
| `mcp__bioRxiv__search_preprints` | **DENIED** (after 1st attempt) | Preprint sweep not completed via MCP |
| WebFetch (NCBI eutils) | **BLOCKED (403)** | Fallback metadata channel unavailable |
| Bash curl (eutils.ncbi.nlm.nih.gov) | **BLOCKED (egress allowlist)** | Fallback metadata channel unavailable |

> **Net effect:** the corpus is built from PMID-list searches (verified IDs) + Consensus metadata, with
> **every cited PMID independently title-confirmed against PubMed (L-009).** Gaps explicitly flagged:
> (1) no full text; (2) preprint sweep incomplete; (3) 2 records left UNCONFIRMED → uncited.

---

## 1. PubMed / MEDLINE searches (PMID-list tool; counts = total_count)

| # | Query (abbrev.) | Total hits | Selected |
|---|---|---|---|
| P1 | "ablation index"/AI-guided AND PVI/AF-ablation AND radiofrequency | 148 | AI core set |
| P2 | "lesion size index"/LSI/VISITAG AND PVI/AF-ablation | 64 | LSI core set |
| P3 | "contact force" AND PVI/RF/AF | 732 | CF landmark trials |
| P4 | "impedance drop"/"impedance monitoring"/"local impedance" AND PVI/RF/AF | 166 | LID core set |
| P5 | (AI/lesion index) AND (CF/impedance) AND AF [comparative] | 128 | head-to-head candidates |
| P6 | (first-pass/dormant conduction/reconnection) AND (AI/CF) AND AF | 171 | outcome studies |
| P7 | (AI/CF/LSI) AND AF AND (meta-analysis/systematic review) | 34 | Ioannou MA |
| P8 | catheter ablation AF AND (guideline/consensus/HRS/EHRA/ESC) | 242 | guidelines |
| G1 | (CF AND AI) AND (no difference/not predictive/discordant/comparison) | 20 | contradiction set |
| G2 | (AI/CF) AND (Asian/Japan/Korea/China) AND AF | 241 | population gap |
| G3 | (AI/LSI) AND (threshold/target/posterior wall) AND persistent AF | 20 | threshold heterogeneity |
| G4 | (AI/LSI) AND randomized AND AF | 42 | RCT evidence |
| G5 | (AI/local impedance) AND (HPSD/workflow/real-world) AND AF | 97 | implementation |

> Counts feed the PRISMA "records identified" pool. PubMed returned **abundant** evidence for every
> metric and every gap — no metric was thin at the identification stage. (Note: head-to-head **AI-vs-LSI
> RCTs remain sparse** — confirmed as a real evidence gap, not a search artifact; see §4.)

## 2. Consensus searches (full metadata + abstract; L-009 confirmation required)

| # | Query | Returned | Notable confirmed records |
|---|---|---|---|
| C1 | ablation index vs contact force PVI outcomes | 10/20 | Phlips, Pedersen*, Hussein, Chen, Dhillon, Ullah |
| C2 | LSI/TactiCath PVI outcomes durable | 10/20 | Cai 2023, Katić, Mattia, Prasad, Kuo, Taghji, Cai 2022, Kanamori, Lian |
| C3 | AI-guided vs conventional RCT (drifted to substrate trials) | 10/20 | mostly off-topic (excluded) |
| C4 | local impedance DirectSense/IntellaNav outcomes | 10/20 | Solimene, Szegedi, Fukaya, Lyan, Segreti*, Lepillier, Perge, Martin, Masuda |
| C5 | AI meta-analysis PVI recurrence | 10/20 | PRAISE (Hussein 2018), Ioannou MA |
| C6 | CF-sensing RCT SMART-AF/TOCCASTAR | 10/19 | TOCCASTAR, SMART-AF, SMART-SF, PRECEPT, TactiSense, Ullah |
| (impedance drop/reconnection) | rate-limited ×2 | retried within other queries |

\* Pedersen and Segreti = PMID-unconfirmed → left uncited (see reference store UNCONFIRMED list).

> **Consensus compliance:** results were used for metadata only; the writer cites PubMed PMIDs, not
> Consensus URLs. Consensus sign-up/upgrade message acknowledged. Rate-limit hit twice; queries retried
> singly per the 3-call batch guidance.

## 3. bioRxiv / medRxiv (L-004)

- **Attempted:** `medrxiv`, category cardiovascular medicine, 2022–2026. **Tool DENIED** after first call.
- bioRxiv MCP also lacks keyword text-search (category+date only, per its own tool docs), so it is a weak
  channel for this niche RF-metric topic regardless.
- **Result:** preprint sweep **incomplete**. **No preprints entered the corpus.** Flagged as a
  coverage limitation (Law 5). If preprints are required, re-grant the bioRxiv tool or search medRxiv web.

## 4. ClinicalTrials.gov (L-008 broad-first)

- Direct ClinicalTrials.gov MCP/web tools were not available this run; **trial registry coverage came via
  the NCT numbers embedded in the included publications** (captured in the reference store):
  - NCT02628730 (PRAISE), NCT01278953 (TOCCASTAR), NCT01385202 (SMART-AF), NCT02817776 (PRECEPT),
    NCT03906461 (LSI Workflow), NCT03793998 (CHARISMA / Lepillier), NCT05752487 (SmartfIRE DE).
- **Gap:** a dedicated broad-first ClinicalTrials.gov sweep for *ongoing/unpublished* AI/LSI/impedance
  trials was **not performed** (no registry tool). Recorded as a known gap; recommend a follow-up
  registry search before the review is finalized.

## 5. Guideline bodies (L-011)

- 2024 ESC AF Guidelines — **PMID 39210723** (confirmed).
- 2023 ACC/AHA/ACCP/HRS AF Guideline — **PMID 38033089** (lead; companion records 38857333/38408149/38153996).
- 2017 HRS/EHRA/ECAS/APHRS/SOLAECE Consensus — **PMID 29021841** (lead; companions 29016841/29016840).

---

## 6. PRISMA-ready flow (this run)

- **Records identified (PubMed, sum of search totals, pre-dedup):** ~2,185 (overlapping).
- **Records screened via metadata (PubMed + Consensus):** ~70 distinct candidates inspected.
- **Logical studies selected & PMID-verified into the citable store:** **32**
  (29 primary studies + 3 guideline documents).
- **Excluded at selection:** off-topic substrate/PWI/linear-ablation RCTs (CAPLA, PROMPT-AF, DECAAF-II,
  REAFFIRM, Deisenhofer, Kircher, etc.) — not lesion-metric comparisons; cryoballoon/PFA-only; duplicates.
- **Left UNCONFIRMED → uncited:** 2 (Pedersen 2020; Segreti 2020 CHARISMA pilot).
- **Preprints included:** 0 (sweep incomplete — tool denied).
- **Full text retrieved:** 0 (tool denied) — appraiser to re-fetch.

## 7. Coverage check by metric (no metric left thin)

| Metric | Records | Designs present |
|---|---|---|
| Ablation Index (AI) | A001–A007 (7) | pilot, prospective cohort, registry, meta-analysis |
| Lesion Size Index (LSI) | A008–A014 (7) | prospective/retrospective cohort, multinational observational |
| Contact Force (CF) | A015–A020 (6) | 2 RCTs (TOCCASTAR, Ullah) + landmark prospective trials |
| Impedance drop / LID | A021–A029 (9) | first-in-human, pilots, registries, 1 head-to-head vs LSI |
| Guidelines | A030–A032 (3) | ESC 2024, ACC/AHA 2023, HRS/EHRA 2017 |
