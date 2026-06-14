---
name: evidence-appraisal
description: >
  Critically appraises a medical evidence corpus — assigns study designs in the evidence hierarchy,
  applies the design-appropriate risk-of-bias tool (Cochrane RoB 2, ROBINS-I, Newcastle-Ottawa,
  QUADAS-2), grades certainty per outcome with GRADE, and surfaces contradictions and gaps. Used by
  the critical-appraiser agent and whenever a review needs quality assessment, evidence grading,
  risk-of-bias analysis, or a summary-of-findings table.
---

# Evidence Appraisal

Judge how much each study can be trusted and how certain the overall evidence is, so the writer
reports findings proportionate to their strength. Produce `_workspace/03_appraisal.md`.

## 0. Landmark scan (do this first, before appraising the corpus)
Before grading individual studies, identify **2–3 systematic reviews or meta-analyses** that meet
all of:
- Published in the **last 5 years** (prefer <3 years if available)
- In a high-impact journal (IF >5, or equivalent: NEJM, Lancet, JAMA, BMJ, Circulation, JACC,
  Eur Heart J, Cochrane Database, Ann Intern Med, etc.)
- Directly on the review's PICO/PECO question

For each landmark: read the abstract and, if available, the Methods + Conclusions. Extract:
- The review's own GRADE/evidence-certainty summary
- Key contradictions or debates it identifies
- Frameworks or outcome groupings it uses

**Record in the assumption register:** "Landmark pre-reads: [Author Year Journal] — used to inform
appraisal structure and identify known controversies; did not anchor individual study judgments."

**Anchoring guard:** use landmark reviews to *orient* the appraisal (known landscape, existing
debates), not to copy their conclusions. If your independent appraisal disagrees with a landmark,
state both views — the disagreement is informative. If a landmark itself is in the corpus as a
primary source, appraise it normally in Step 1.

## 1. Evidence hierarchy
Rank each study by design:
`systematic review / meta-analysis > RCT > prospective cohort > case-control > case series > expert opinion`.
**Preprints are downgraded** pending peer review regardless of design. Label every study's design
explicitly — the hierarchy drives later weighting.

## 2. Risk of bias — pick the tool for the design

| Design | Tool | Key domains |
|---|---|---|
| RCT | **Cochrane RoB 2** | randomization, deviations, missing data, measurement, selective reporting |
| Non-randomized intervention | **ROBINS-I** | confounding, selection, classification, deviations, missing data, measurement, reporting |
| Observational (cohort/case-control) | **Newcastle-Ottawa** | selection, comparability, outcome/exposure ascertainment |
| Diagnostic accuracy | **QUADAS-2** | patient selection, index test, reference standard, flow & timing |

Record the **per-domain judgment** (low / some concerns / high), not just a global label. Note
funding source and conflicts as a bias consideration.

## 3. GRADE certainty (per outcome)
Rate each major outcome **High / Moderate / Low / Very Low**. Start from design (RCT = High,
observational = Low) then adjust:
- **Downgrade:** risk of bias, inconsistency (heterogeneous results), indirectness, imprecision
  (wide CI / small N), publication bias.
- **Upgrade (observational):** large effect, dose-response, plausible confounding would reduce the
  effect.
State the reason for every up/downgrade.

## 4. Evidence table
One row per study: design, N, population, key effect estimate **with CI**, risk-of-bias judgment,
notes. Capture effect sizes, CIs, sample sizes, follow-up duration — never invent a number; if it
isn't in the source, write "not reported."

## 5. Contradictions & gaps (do this actively)
- **Contradictions:** list every place studies disagree, with both sides cited and a methodological
  reason for the discrepancy (different populations? dosing? bias?).
- **Gaps:** what is unknown, underpowered, or untested. The writer needs these for the Discussion.

## 6. Assumption Register (mandatory)
Log every extrapolation you make during appraisal — each becomes a line in the review's Limitations:
- "Assuming the European-cohort effect applies to the Vietnamese population (no local data found)."
- "Assuming the 2022 guideline is still current — no 2024/2025 update located."
- "Assuming the adult-trial result generalizes to adolescents."
Surfacing assumptions is honesty about generalizability (Law 5), not weakness.

## 7. Per-claim strength labels
For each finding the writer will report, emit a label: `[GRADE: High|Moderate|Low|Very Low]`. The
writer must carry these into the draft so language strength matches evidence strength, and the QA
verifier checks the alignment.

## Why grading matters
Treating a small unblinded preprint as equal to a large RCT is the most damaging error a review can
make. Explicit hierarchy + risk-of-bias + GRADE is the guardrail. If full text is missing for a
pivotal study, appraise from the abstract but mark it provisional and ask the retriever to fetch it.
