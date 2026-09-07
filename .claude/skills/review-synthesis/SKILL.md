---
name: review-synthesis
description: >
  Writes an in-depth medical literature review from the appraised evidence — standard review
  structure, thematic narrative synthesis (not a paper-by-paper list), inline Vancouver numbered
  citations mapped to a hyperlinked reference list, language strength matched to GRADE certainty,
  and honest treatment of controversy and gaps. Used by the lead agent whenever the
  review draft is written or revised.
---

# Review Synthesis & Writing

Organize and interpret the appraised evidence into a rigorous, readable review. Produce
`_workspace/05_draft_review.md`. You do not generate facts — every substantive claim is anchored to
a corpus record and carries the appraiser's strength label.

## Language (confirm in Phase 0 — default Vietnamese)
Write in the confirmed language. For **Vietnamese**, load `references/vi-terminology.md` and use the
verified term mappings: Vietnamese first, English in parentheses on first appearance, abbreviation
after. Never silently invent a Vietnamese term for a key concept — mark provisional and flag for the
user. Learn style from any `source/` file the user provided rather than guessing.

**Compose natively — never literal-translate (L-033).** Write directly in the target language for that
audience. Do NOT render English sentence-by-sentence: break English run-on sentences into short Vietnamese
clauses, use native connectors (*vì, do đó, ngược lại, trong khi đó, nói cách khác*), and follow
topic–comment order rather than mirroring English word order. Avoid calques ("ở nơi… và ở nơi…", "mà ở
đó…"). If an English draft already exists, treat it as a **content source** and re-compose for fluency —
do not transliterate its syntax. Read each paragraph as a native clinician would: if a Vietnamese
cardiologist wouldn't phrase it that way, rewrite it. Preserve all numerics/CIs/P-values/GRADE labels/`[n]`
citations and the reference list **verbatim** while doing so.

## Provenance discipline (cite only from the store)
Cite **only** from `reference/<topic>.md`. Before writing any sentence with a number or named study,
re-read its line in that file. The conversation and any context summary are NOT citation sources — if
it isn't in the reference store, it isn't citable (this severs citations from fallible memory).

**Landmark reviews are no exception.** A landmark review article read for orientation is citable only
if it was promoted into `reference/<topic>.md` as a Level III (expert-opinion) record. If you draw a
direct opinion/claim from a landmark, it must have an entry there with a stable ID; if it has no entry,
do not cite it — request the appraiser/retriever add it, or drop the claim. Landmark-sourced sentences
get hedged expert-opinion language (Level III), never quantitative-finding language.

## Document structure
1. **Title + structured abstract/summary** (background, methods, key findings, conclusion).
2. **Background** — why the question matters, what's at stake clinically.
3. **Methods** — the protocol in brief + PRISMA numbers (identified/screened/included) + sources searched + date window. This is what makes it systematic.
4. **Results / Synthesis** — organized **thematically** (by outcome, mechanism, or population), not one-paragraph-per-paper.
5. **Discussion** — strength of the evidence, contradictions, limitations of the review, evidence gaps, ongoing trials.
6. **Conclusions** — proportionate to the evidence; no overreach.
7. **Summary-of-findings / evidence table** (from the appraisal).
8. **References** — numbered Vancouver list, each hyperlinked to its DOI/PMID/NCT URL.

## Depth calibration — word count as soft guide, not floor
Any word-count target agreed in Phase 0 is a **soft suggestion**, not a minimum to pad toward.
Write to the depth the evidence supports:
- Sparse corpus (few studies, thin data) → a tighter, honest review beats a bloated one.
- Rich corpus (many studies, nuanced debates) → expand as needed; do not truncate real analysis to
  hit an upper limit.
- If your draft is significantly shorter than the Phase-0 target, note why (e.g., "corpus has only
  4 relevant studies; expanding would require repetition") rather than padding.

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

## Strength-matched language (bidirectional)
Use the appraiser's `[GRADE]` labels. The label calibrates language in **both** directions — it is not
a license to hedge below what the evidence supports:
- **High/Moderate:** confident — "X reduces Y." Do NOT downgrade to "may suggest / raises the question /
  could indicate" when the evidence has already answered. Under-claiming strong evidence is a defect.
- **Low:** hedged — "evidence suggests X may reduce Y."
- **Very Low:** explicitly tentative — "a single small trial reported... ; this requires confirmation."
Never state a Low/Very-Low finding as established fact; equally, never bury a High/Moderate finding in
weasel verbs. Watch for hedging tics ("đặt ra câu hỏi", "có thể gợi ý", "dường như") used where the data
is actually decisive — if the evidence answered it, say so.

## Honesty rules
- Show controversy where the appraiser flagged it — both sides, cited.
- **Steelman before concluding (≠ false balance).** For each major conclusion, state the strongest
  opposing interpretation the evidence allows, then conclude — stronger or corrected. False balance
  avoids a conclusion; a steelman stress-tests it and still reaches one. Do not merely confirm the
  expected answer.
- State gaps and the review's own limitations plainly.
- Foreground recent evidence and ongoing trials; flag every preprint-based claim as not-yet-peer-reviewed.

## Revision behavior
When the citation-verifier returns FIX/BLOCK items, correct the claim, swap the citation, or remove
the statement — don't defend an unsupported sentence. Preserve citation numbering stability across
revisions where possible.


## Claim links and economical revisions
Follow `docs/claim-links.md`: every cited paragraph or table row has an invisible claim ID and an
exact-text mapping in `_workspace/05b_claim_links.jsonl` to accepted cards. Use one-line numbered
references with explicit PMID/DOI/NCT under a References/Tài liệu tham khảo heading. Keep IDs
stable on revisions; update link text when prose changes. Do not split a paragraph solely to
pad coverage. Reference-store entries and accepted cards are the on-disk source of citation facts;
load each relevant entry once per batch rather than one tool call per sentence. Re-read when its
content changes or an interpretation is uncertain. Patch affected sections, then refresh dependent
summary/conclusions and run global checks. Evidence table comes from the renderer, not retyping.
