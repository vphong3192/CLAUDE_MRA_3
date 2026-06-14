# rubric.md — Scoring rubric for a medical literature review

The verifier scores every finished review on 6 weighted criteria, each 0.0–1.0. **Every score must
cite specific evidence from the output** — no vague "pretty good." Ported from v1, with GRADE/RoB
folded into criteria 2 and 4.

> Load this only at the scoring step (verifier), not at the start of a run.

## Criterion 1 — Search comprehensiveness — 25%
- [ ] ≥2 independent sources searched (PubMed + ≥1 of web/Consensus/preprint/trials)?
- [ ] MeSH/keywords listed in the Methods section?
- [ ] ≥1 systematic review or meta-analysis (if any exists)?
- [ ] ≥1 authoritative guideline (if the topic has one)?
- [ ] ≥1 dedicated "research gap" search (curiosity budget)?
- [ ] Current to the present year (no missed recent evidence)?
- [ ] **Research Map (hard gate) presented and user-approved before drafting?**
- Scoring: 1.0 all pass + 20+ quality sources · 0.8 = 6/7 · 0.6 = 5/7, missing meta-analysis · 0.4 = single DB · 0.2 = thin (<5 sources)

## Criterion 2 — Source quality — 20%
- [ ] >70% of sources are SR/RCT/large cohort (tiers 1–3)?
- [ ] Q1 journals / Cochrane / major-body guidelines cited?
- [ ] Each key claim has ≥1 high-tier citation (not only case report/opinion)?
- [ ] Preprints clearly marked "not peer-reviewed"?
- [ ] GRADE certainty assigned per major outcome; no unverifiable/predatory sources?
- Scoring: 1.0 all pass + ≥80% tier 1–3 · 0.8 = 4/5 · 0.6 = 3/5 · 0.4 = 1–2 weak but not dangerous · 0.2 = predatory/untrustworthy present

## Criterion 3 — Synthesis & analysis — 20%
- [ ] Grouped by sub-theme, NOT a paper-by-paper list?
- [ ] Results compared across studies (agree where / diverge where)?
- [ ] Supporting vs. opposing sources counted for key claims?
- [ ] A general pattern extracted, not just per-paper summaries?
- [ ] Mechanism discussed where relevant?
- Scoring: 1.0 excellent + new insight · 0.8 good pattern · 0.6 ok but listy · 0.4 mostly listing · 0.2 abstract cut-paste

## Criterion 4 — Critical appraisal — 15%
- [ ] Separate "consensus" and "controversy" sections?
- [ ] Sample sizes + methodological limits of major studies noted?
- [ ] Risk-of-bias tool applied per design (RoB 2 / ROBINS-I / Newcastle-Ottawa / QUADAS-2)?
- [ ] Publication/selection bias and conflicts of interest flagged where relevant?
- [ ] Association vs. causation distinguished?
- Scoring: 1.0 deep, each key source appraised · 0.8 good for main sources · 0.6 present but generic · 0.4 minimal · 0.2 sources presented as absolute truth

## Criterion 5 — Citation accuracy — 10%
- [ ] Every claim has an inline citation (no "naked" claims)?
- [ ] Consistent format (Vancouver, not mixed)?
- [ ] PMID/DOI/NCT resolves to the real record?
- [ ] No fabricated citations (author, year, journal all real)?
- [ ] Citations represent the source faithfully (no distortion of the authors' conclusion)?
- Scoring: 1.0 = 100% correct · 0.8 = 95%+ minor format slips · 0.6 = 85%+ some missing · 0.4 = <85% or many naked claims · **0.0 (AUTO-FAIL): any fabricated citation → whole review fails (Law 1)**

## Criterion 6 — Applicability — 10%
- [ ] Concrete clinical/research/practice implications?
- [ ] Limits of applicability stated (e.g., adults only, Caucasian cohorts)?
- [ ] Technical level matches the stated audience?
- [ ] Next steps suggested?
- Scoring: 1.0 immediately actionable · 0.8 present but unspecific · 0.6 theoretical · 0.4 mostly info · 0.2 none

## Total & bands
```
Score = 0.25·T1 + 0.20·T2 + 0.20·T3 + 0.15·T4 + 0.10·T5 + 0.10·T6
```
- **≥0.85 EXCEEDED** (near publish-ready) · **0.70–0.84 MET** · **0.60–0.69 ADEQUATE** (needs edits) ·
  **0.50–0.59 BELOW** · **<0.50 FAIL**
- **Any fabricated citation → AUTO-FAIL** regardless of total (Law 1).

## Anti-inflation rules
1. No high score for "reads well" — require the checkbox evidence. 2. No 1.0 unless all boxes pass.
3. When between two levels → pick the lower. 4. Compare to prior reviews of the same criterion — do
not inflate over time.
