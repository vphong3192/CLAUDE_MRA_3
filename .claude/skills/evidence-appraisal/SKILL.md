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

**Appraise only user-approved sources.** The Phase 3 Research Map gate ends with the user approving
the source list (with HIGH/MEDIUM/LOW tiers). Summarize and grade only those approved records — do
not pull in sources the user dropped, and respect any re-tiering. If you need a source that wasn't
approved, ask the lead to re-open the gate, don't smuggle it in.

## 0. Landmark scan (do this first, before appraising the corpus)
Before grading individual studies, identify **2–3 review articles** (narrative/topic reviews,
state-of-the-art reviews, expert overviews — **NOT** systematic reviews or meta-analyses, which are
primary research and belong in the corpus) that meet all of:
- Published in the **last 5 years** (prefer <3 years if available)
- In a high-impact journal (IF >5, or equivalent: NEJM, Lancet, JAMA, BMJ, Circulation, JACC,
  Eur Heart J, Nat Rev *, Ann Intern Med, etc.), and ideally well-cited
- Directly on the review's topic

These are read primarily **for orientation** — to learn how experts frame the topic, how they group
subtopics, and what debates they highlight.

**Full text is mandatory for landmarks.** Read the full text, not just the abstract — the value is
in the framing and structure, which the abstract does not convey. If a landmark review's full text
is **unavailable** via any MCP tool (paywalled), **alert the user explicitly** — title, DOI, why it
looks pivotal — and ask them to supply the PDF to `source/`. Do not appraise off the abstract alone
for a landmark; either get full text or drop it and pick another.

Extract from each: how it organizes subtopics, key contradictions/debates it names, and any outcome
or mechanism groupings useful for structuring the synthesis.

**If the writer will quote or paraphrase a direct opinion/claim from a landmark**, that landmark
**must enter the corpus** as a verified record (stable ID + metadata) and be appraised as
**Level III evidence — expert opinion** (lowest tier of the hierarchy below). It is then cited
normally with its `[n]`. The rule is absolute: **no sentence carrying an idea taken from a landmark
may be written without a citation to it.** Reserve landmark-sourced claims for framing, expert
interpretation, or context — never for quantitative findings, which must come from primary studies.

**Record in the assumption register:** "Landmark pre-reads: [Author Year Journal] — read in full to
inform synthesis structure; cited as Level III (expert opinion) only where a direct claim is drawn,
otherwise orientation only."

**Anchoring guard:** use landmark reviews to *orient* the appraisal (known landscape, existing
debates), not to copy their conclusions. If your independent appraisal disagrees with a landmark,
state both views — the disagreement is informative.

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

**Load the numbers — do not hand-copy them.** Hand-retyping N / CI / effect sizes from the store is
where a decimal breaks or a Methods figure gets pasted as a result (Law 1). Run the deterministic
extractor first and pull each cell from its verbatim buckets:
```
python3 .claude/skills/evidence-appraisal/scripts/extract_numbers.py \
  --store reference/<topic>.md --out _workspace/03b_numbers.md
```
It emits, per record, five verbatim buckets — `sample_sizes · percentages · p_values ·
confidence_intervals · ratios` (OR/RR/HR/aHR/MD/SMD/β/coef). Copy table cells from `03b_numbers.md`,
not from memory. The extractor types numbers by **surface pattern, not meaning**: it cannot tell the
primary outcome from a baseline figure, so YOU still decide which number belongs in which row and
whether it is the result being graded. An empty bucket = no number found → write "not reported"
(never a placeholder). Numbers it cannot bucket (e.g. mean±SD) you still read from the store
directly. No LLM, no network; same store → identical buckets every run.

Carry each study's **own `study_context`, `study_limitations`, and `author_suggestions`** (from the
reference store) into the appraisal so the writer can reflect per-study IMRAD faithfully — the
authors' background/rationale and framing of the topic (Introduction), the study's own limitations
(Discussion), and the next steps they propose. This is the per-study counterpart to the corpus-level
summary, not a replacement for it. Where a record is still abstract-only and these read
`not captured`, note it and (for HIGH-relevance records) flag for full-text upgrade.

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
