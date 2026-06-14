---
name: review-synthesis
description: >
  Writes an in-depth medical literature review from the appraised evidence — standard review
  structure, thematic narrative synthesis (not a paper-by-paper list), inline Vancouver numbered
  citations mapped to a hyperlinked reference list, language strength matched to GRADE certainty,
  and honest treatment of controversy and gaps. Used by the synthesis-writer agent whenever the
  review draft is written or revised.
---

# Review Synthesis & Writing

Organize and interpret the appraised evidence into a rigorous, readable review. Produce
`_workspace/04_draft_review.md`. You do not generate facts — every substantive claim is anchored to
a corpus record and carries the appraiser's strength label.

## Language (confirm in Phase 0 — default Vietnamese)
Write in the confirmed language. For **Vietnamese**, load `references/vi-terminology.md` and use the
verified term mappings: Vietnamese first, English in parentheses on first appearance, abbreviation
after. Never silently invent a Vietnamese term for a key concept — mark provisional and flag for the
user. Learn style from any `source/` file the user provided rather than guessing.

## Provenance discipline (cite only from the store)
Cite **only** from `reference/<topic>.md`. Before writing any sentence with a number or named study,
re-read its line in that file. The conversation and any context summary are NOT citation sources — if
it isn't in the reference store, it isn't citable (this severs citations from fallible memory).

## Document structure
1. **Title + structured abstract/summary** (background, methods, key findings, conclusion).
2. **Background** — why the question matters, what's at stake clinically.
3. **Methods** — the protocol in brief + PRISMA numbers (identified/screened/included) + sources searched + date window. This is what makes it systematic.
4. **Results / Synthesis** — organized **thematically** (by outcome, mechanism, or population), not one-paragraph-per-paper.
5. **Discussion** — strength of the evidence, contradictions, limitations of the review, evidence gaps, ongoing trials.
6. **Conclusions** — proportionate to the evidence; no overreach.
7. **Summary-of-findings / evidence table** (from the appraisal).
8. **References** — numbered Vancouver list, each hyperlinked to its DOI/PMID/NCT URL.

## Synthesis, not summary
A review integrates studies into an argument: where they converge, where they diverge, and *why*
(methodological reasons). If you find yourself writing "Study A found X. Study B found Y. Study C
found Z." with no connective reasoning, you are listing, not synthesizing — fix it.

## Citations — Vancouver numbered
- Cite every substantive claim inline as `[n]`; `[n]` maps to the reference list in citation order.
- Multiple: `[3,5,7]` or ranges `[3–5]`.
- **Never write a claim you cannot cite to a real corpus record.** No supporting record → soften,
  remove, or request retrieval. Fabricating a citation is the cardinal sin; the QA verifier will
  catch it and it will block the review.
- Reference entry format: `Authors. Title. Journal. Year;Vol(Issue):Pages. DOI/PMID — hyperlinked.`
- For preprints: append `[Preprint, not peer-reviewed]`. For trials: cite the NCT number.

## Strength-matched language
Use the appraiser's `[GRADE]` labels:
- **High/Moderate:** confident — "X reduces Y."
- **Low:** hedged — "evidence suggests X may reduce Y."
- **Very Low:** explicitly tentative — "a single small trial reported... ; this requires confirmation."
Never state a Low/Very-Low finding as established fact.

## Honesty rules
- Show controversy where the appraiser flagged it — both sides, cited.
- State gaps and the review's own limitations plainly.
- Foreground recent evidence and ongoing trials; flag every preprint-based claim as not-yet-peer-reviewed.

## Revision behavior
When the citation-verifier returns FIX/BLOCK items, correct the claim, swap the citation, or remove
the statement — don't defend an unsupported sentence. Preserve citation numbering stability across
revisions where possible.
