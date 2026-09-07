# Claim → card → source contract

The lead annotates each citation-bearing paragraph or complete pipe-table data row immediately
with `<!-- claim:CLM-001 -->` (inline or the next line without a blank line). It is invisible in
rendered Markdown and remains in the delivered file. No citation-bearing headings/table headers.

`05b_claim_links.jsonl` contains one JSON object per annotated unit:
```json
{"claim_id":"CLM-001","text":"Exact draft paragraph including its [1] citation.","card_ids":["REF-001-c1"],"citation_numbers":[1],"study_ids":["pmid:33652425"]}
```
Text matches the unit exactly except whitespace normalization; arrays are unique/nonempty. Card study
IDs, mapped study IDs and the identities of references cited in this unit must agree. A synthesis
unit can reference several cards; the verifier still decides whether they support the inference.

Use a Markdown heading `## References` / `## Bibliography` / `## Tài liệu tham khảo`, followed by
one line per entry: `1. Authors. Title. Journal. Year. PMID:33652425. <source link>` (real verified metadata).
Supported citations are [1], [1,3] and ascending [1–3], maximum range span 20. Numeric Markdown links,
footnotes/superscripts, HTML body or code-fenced review content are unsupported; use the documented
format instead of disabling checks. Fulltext cards must contain a nonempty abstract for FULLTEXT checks.

```bash
python .claude/skills/citation-verification/scripts/verify_claim_links.py --draft _workspace/06_final_review.md --cards _workspace/04b_cards.jsonl --source-dir source/TOPIC --links _workspace/05b_claim_links.jsonl --out _workspace/06d_claim_audit.json
```
Run on draft before semantic QA, then on the exact final file. A stale/missing/duplicate link, rejected
card or mismatched citation identity blocks delivery. --out is a JSON report; stdout is compact.
This proves linkage and reruns source locks; it does not prove semantic support or discover every
uncited factual assertion. Verifier must read uncited prose, source context and outcome-level appraisal.
These CLI checks are required by the workflow; there is no host-enforced delivery hook.
