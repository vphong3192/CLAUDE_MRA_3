# 07_proposed_lessons.md — Phase 7 proposals (NOT applied) · regression Case 1 (EASY), metformin in adult T2D · 2026-10-27

Status: **PROPOSED.** Nothing here has been appended to `lessons.md`, `evolution-log.md` or `vi-terminology.md`.
Approve / edit / reject per item. Role tags use real agent names (what `lessons_digest.py --role` matches), not the legacy
orchestrator/retriever/... shorthand. Next free ID is L-045.

Evidence base: `06a_verification_report.md` (rounds 1–2, §E/§F), `04_appraisal.md` §0/§11, `02a_search_log.md`,
`05b_writer_notes.md`, `00_scope.md` amendment, `06c_manifest.md`, `source/metformin-t2d/_PROVENANCE.md`.

---

## 1. Disposition of the lead's 8 candidates (each checked against the artifacts)

| # | Candidate | Verified? | Disposition |
|---|---|---|---|
| 1 | Prefilter sank guidelines | **Yes** — `02a` line 71: min_candidates=150 cut at 150/218; ADA SOC 2026 s9, KDIGO 2022 (+exec summary), ADA/KDIGO 2022, ADA/EASD 2022 (+ Phan 2025, Clegg 2021, Chapman 2016) landed in deferred-unread; 6 rescued by hand. L-011 says *search* the guideline body; it says nothing about the prefilter dropping what was found. | **New L-045** (retriever). Plus harness-code option, §4-A. |
| 2 | MCP full text empty, E-utilities worked | **Yes** — `02a` L98 (MCP body empty ×3, WebFetch DNS-blocked); `04_appraisal` §0.1 and `_PROVENANCE.md`: direct efetch via proxy gave 16 full-text bodies at Phase 4. L-022 handles "ask the user" but not "try the machine route first". | **New L-047** (retriever). |
| 3 | Machine text in `source/` vs "user-supplied" contract | **Yes** — user chose "Giữ ở source/ kèm nhãn" at Gate 4b (`04_appraisal` §13). `critical-appraiser.md` L79–85 already prefers machine extraction but never says where machine-fetched text lives. | **Not a lesson — a CLAUDE.md contract edit; user decision D1.** Interim rule folded into L-047. |
| 4 | Agent summaries in `abstract` field | **Yes** — `04_appraisal` §0.5: H13, M07, M08, M10, M11, M15, M16, S03 hold 93–269-char agent summaries, M06 empty; H13's real abstract has no numbers. Nothing downstream used them (appraisal says so). No existing lesson; SKILL.md schema only says "captured text". | **New L-048** (retriever). |
| 5 | Vietnamese length counting | **Yes, with a discrepancy to note** — `00_scope` says first draft "~4,700 syllable-tokens"; `05b` §0 says 4,158 by the script. Either way ≈ 2.8–3.1× the confirmed "~1500 từ". User resolved by amending to 1,800–2,000. Not covered by L-015 (asks depth, not unit). Side-effect: the cut dropped the Silverii direct-comparison datum (F5) and the MeSH/keywords and COI items (rubric T1/T4 lost points). | **New L-049** (orchestrator + synthesis-writer). |
| 6 | `extract_numbers.py` CI regex | **Yes, reproduced** — `CI_PATTERN` requires a literal "CI": `RR 0.96 (0.84-1.09)` and `aHR 1.09 (0.83–1.44)` give `[]`; `95% CI 0.80-1.03` matches. `04a` CI bucket was empty. Impact contained this run (cards + P8 locks carried the CIs). | **Not a lesson — a code defect + regression test.** §4-B; user decision D3. |
| 7 | Verifier F1–F5 | **Yes** — all five confirmed in `06a` §B; all 104 locks were green and caught none (§A "Residual"). L-003 already says "population, intervention, endpoint match" but is silent on *stratum* and on locks creating false confidence; L-028 covers N only. F2 and F4 were *inherited from the appraisal* (§E.1–E.2). | **Edit L-003** (verifier) + **new L-050, L-051** (synthesis-writer) + **new L-052** (critical-appraiser). |
| 8 | Prefilter not re-run after supplementary search | **Yes** — `02a` L108: 10 new studies "appended to 02e_candidates.jsonl by hand (prefilter not re-run: it would displace 6 earlier candidates)". Disclosed and PRISMA reconciles (260/30/130/68, exit 0), so no Law breach — but a mechanical step was done by hand, against L-039. | **New L-046** (evidence-retriever). Plus §4-A. |

Additional findings from the artifacts (not in the lead's list):
- **Stale map header** — `03_research_map.md` still says "AWAITING USER APPROVAL" after clearance (`06a` §E.3). **Edit to L-019** (orchestrator).
- **Reader-facing process overclaim** — "mọi con số đã khoá" / "đăng ký trước" (F6) = `04_appraisal` §0 wording scoped to cards, lost in translation. One occurrence → **L-053 proposed as optional** (recommend fold into L-050 or defer).
- **Verifier's own suggested fix over-read** (R2-1: "ước tính điểm chỉ nghiêng về nhồi máu") → included in the L-003 edit.

---

## 2. Proposed new lessons (L-045 … L-053)

### L-045: Known-item lane — documents the protocol names by identity must bypass the prefilter
- **Role:** evidence-retriever
- **Trigger:** the corpus pool exceeds `min_candidates` (so `prefilter_records.py` cuts), AND the topic has guideline/consensus documents or any record the protocol/user names by identity (society standards, KDIGO/ADA/ESC-type reports, a landmark trial)
- **Rule:** Before running `prefilter_records.py`, list the guideline/consensus/named-item records already in the pool and carry them into `02e_candidates.jsonl` (or the worksheet) as a seeded, declared "known-item lane" — they are never ranked against ordinary records. After the prefilter, check `02f_deferred.jsonl` for the same set; any guideline found there is a defect to fix before Gate 2b, not a note. Reason: guideline PubMed records are metadata-poor (empty abstract, no MeSH, "Practice Guideline" type only), so a score built from title+abstract+metadata systematically ranks them last, and a recall floor of N only protects pools ≤ N. Do not loosen thresholds to fix this.
- **Why:** This run the cut at 150 of 218 deferred-unread ADA SOC 2026 s9, KDIGO 2022 and its executive summary, ADA/KDIGO 2022 and ADA/EASD 2022 — exactly the documents rubric T1 and L-011 require; six were rescued by hand via known-item searches, the rest stayed unread. A rescue by hand works only if someone notices.
- **Origin:** Evolution-log Entry #11 (2026-10-27) — `02a_search_log.md` "Prefilter defect to note".

### L-046: A supplementary search is a declared second pass on the NEW records only — never hand-edit the candidate stream
- **Role:** evidence-retriever
- **Trigger:** after Gate 2b or the Research Map, the user approves a supplementary search (coverage hole, new subgroup) and new records must enter the screened stream
- **Rule:** Add the new records to `02b_records.jsonl` with a distinct `search_pass` / query tag, rebuild `02c`/`02d` with `dedupe_records.py`, and run the prefilter on the new records only (or with the pool treated as ≤ `min_candidates` so nothing is cut) — never re-run it over the full pool if that would displace earlier candidates, and never append rows to `02e`/`02h` by hand. State in the search log and PRISMA notes that a second pass ran, its query ids, how many records it added, and that the first-pass cut was not altered. Re-run `prisma_flow.py` and confirm exit 0 and that the identified/screened/deferred counts reconcile.
- **Why:** Hand-appended candidates are an un-reproducible step in an otherwise deterministic pipeline (L-039), and re-running the full prefilter silently changes which first-pass records were read (here: 6 would have been displaced). This run disclosed the hand edit and PRISMA reconciled, so it was not a breach — but a reviewer cannot reproduce it. Better: add an `--only-new`/`--append` mode to the script (§4-A).
- **Origin:** Evolution-log Entry #11 — `02a_search_log.md`, "Phase 3 supplementary search".

### L-047: Try the machine full-text route (NCBI E-utilities efetch) at Phase 2, and keep fetched text provenance-labelled
- **Role:** evidence-retriever
- **Trigger:** `get_full_text_article` (MCP) returns empty or abstract-only bodies for records that have a PMCID, or WebFetch is DNS-blocked — i.e. before you count "abstract-only HIGH" for Gate 2b (L-022)
- **Rule:** Before declaring full text unavailable, run a deterministic script that calls `efetch` (`db=pmc` for the article, `db=pubmed` for the record) through the session proxy for every PMCID-bearing HIGH/MEDIUM record, writes the response bytes unchanged, and records URL, byte count, SHA-256 and `has_body` per file in a manifest. Recount abstract-only HIGH records from the manifest and present that recount at Gate 2b. Say plainly which records have no PMC record at all (paywalled/no PMCID) — those still need the user (L-022). Fetched files go beside user-supplied text only with a `_PROVENANCE.md` stating "machine-fetched, not user-supplied" and listing which are body vs front-matter-only; never fetch records outside the approved candidate set.
- **Why:** This run discovered at Phase 4 what was available at Phase 2: 16 full-text bodies via efetch while Gate 2b had been asked on "8 of 14 HIGH abstract-only" and the user chose "Tải PMC + thử web" on information that was avoidably poor. Text written by a script (not a model) is also what makes `verify_quotes.py` locks meaningful. Where it lives is contract question D1.
- **Origin:** Evolution-log Entry #11 — `02a` L98; `04_appraisal` §0.1/§11.2; `_PROVENANCE.md`.

### L-048: `02b_records.jsonl` `abstract` is verbatim source text or empty — never an agent summary
- **Role:** evidence-retriever
- **Trigger:** writing a record to `02b_records.jsonl`/the store when the tool returned a truncated, missing or number-free abstract (or the record came from a Consensus snippet)
- **Rule:** The `abstract` field holds exactly the text the source returned. If you have only a summary, a snippet or your own condensation, leave `abstract` empty and put the condensation in a separate field (e.g. `agent_note`, flagged as agent-written) with `text_provenance` set. After writing a batch, scan for `abstract` values shorter than ~300 characters and either replace them from PubMed (`efetch`) or blank them. Never let a downstream quote lock, number extraction or screening decision read an `abstract` you wrote.
- **Why:** 8 records here (H13, M07, M08, M10, M11, M15, M16, S03) carried agent-written summaries of 93–269 characters in `abstract`, M06 was empty, and H13's real abstract contains no numbers at all. The appraiser caught it and bypassed those fields, but screening ran on them and any quote lock would have "verified" model text against model text (the failure P8 exists to prevent).
- **Origin:** Evolution-log Entry #11 — `04_appraisal` §0.5, §11.1.

### L-049: Fix the length unit in Phase 0 (Vietnamese: syllable-tokens), count by script before handoff, and protect rubric-mandated items under a cap
- **Role:** orchestrator, synthesis-writer
- **Trigger:** the user states a length target ("~N từ"/"~N words") for a Vietnamese (or other non-space-delimited-word) review
- **Rule:** *Orchestrator:* at Phase 0 state the counting unit back to the user — Vietnamese words are counted per syllable, as Word does (`len(line.split())`) — record unit + scope (excluding title/references/SoF table/appendix) in `00_scope.md`, and pass the exact count method to the writer. *Writer:* count the main text with that script before handoff and again after every revision; a draft more than ~15% over the target is rewritten, not sent. When the cap is tight, reserve budget FIRST for items the rubric scores — MeSH/keywords in Methods, COI note, the Law 4/5 sections — and cut narrative before them. After any cut, re-run L-051.
- **Why:** The first draft came to 4,158–4,700 tokens against "~1500 từ" (≈3×), cost a user round-trip (amended to 1,800–2,000), and the compression then dropped Silverii's direct metformin–SGLT2i comparison (F5), the MeSH/keyword list (T1 lost a box) and the COI note (T4 lost a box; A5 "not applied for length"). The unit ambiguity, not the writer's care, was the root cause.
- **Origin:** Evolution-log Entry #11 — `00_scope.md` amendment; `05b` §0; `06a` F5/A5/rubric T1,T4.

### L-050: Self-check every number's stratum, every "inconsistent", every "only", and every "not from X" before handoff
- **Role:** synthesis-writer
- **Trigger:** writing or revising any sentence that (a) attaches an effect estimate to a population label (eGFR band, age, subgroup, "overall"), (b) calls two findings inconsistent/contradictory, (c) uses an exclusivity word (chỉ/only/solely), or (d) interprets a non-significant result
- **Rule:** (a) Name the stratum the number was reported for; if the card's quote says "overall", write "overall" — a real number from the wrong stratum is still a mismatch. (b) Before writing "không nhất quán/inconsistent", confirm both sources report the same endpoint (CV mortality ≠ all-cause mortality; MACE ≠ its components). (c) Delete "chỉ/only" unless a source reports the exclusion (a pooled estimate cannot show the effect is confined to a subgroup). (d) For a null result write the CI-compatible range ("tương thích với giảm tới 27% hay tăng 48%"), never "không đến từ …"/"no effect". Run these four greps on the draft before handing it to the verifier.
- **Why:** Round 1 found five substantive misreads (F1 overall aHR 0.98 labelled eGFR ≥30 although the overall cohort includes eGFR <30; F2 CV vs all-cause mortality called inconsistent; F3 unsupported "chỉ"; F4a null CI read as absence; F4c wrong CI) while 104/104 quote locks were green, because locks prove the number is in the quote, not what it describes. Only the verifier's side-by-side read caught them — late and at the cost of a round.
- **Origin:** Evolution-log Entry #11 — `06a` F1–F4, §A "Residual", §F candidates (i),(iii).

### L-051: After any cut or merge, re-verify every scoped-absence claim and every "all/every" against the cards
- **Role:** synthesis-writer
- **Trigger:** a draft was shortened, merged or restructured (length amendment, FIX round), or a sentence says "không có/chưa có/no source…", "mọi/every/all", "không nguồn nào"
- **Rule:** List each absence claim and universal quantifier in the revised text and check it against the cards and the contradiction register of `04_appraisal.md`; a datum cut for length that contradicts a general absence claim must be restored or the claim narrowed to what is true (e.g. "no source tests X *first-line in drug-naive adults on hard outcomes*"). Scope "every point estimate favours X" to the outcome and comparison it was counted over, and cite the source that reports it, not a neighbour.
- **Why:** The length cut removed Silverii's finding that metformin was superior in the direct metformin-vs-SGLT2i comparison; the surviving "không có thử nghiệm đối đầu" was then false and mis-cited to [9] (F5). The steelman "mọi ước tính điểm từ RCT … nghiêng về metformin" was false as worded (F4b). Both were true before compression/inheritance.
- **Origin:** Evolution-log Entry #11 — `06a` F4b, F5, §F candidate (ii).

### L-052: An "inconsistency" downgrade or contradiction entry needs the same endpoint; steelmen must not carry "every/any"
- **Role:** critical-appraiser
- **Trigger:** recording a GRADE −1 for inconsistency, or writing a contradiction (C-n) / steelman for the writer
- **Rule:** Before recording inconsistency or a contradiction, state the endpoint and stratum of each side from its card; if the endpoints differ (e.g. CV mortality vs all-cause mortality), it is not inconsistency — downgrade, if at all, for imprecision/indirectness and say so. Write steelmen and "Must-mention" lines with scoped quantifiers (outcome, comparison, design) and back each "every/any/none" with a count of the cards it was drawn from.
- **Why:** The writer inherited both errors from the appraisal (`06a` §E.1: "CV mortality vs SU" rated Low for "inconsistency" where Cochrane's 4-vs-8 CV deaths points the *same* way as AHRQ; §E.2: C-L-010 "any MACE benefit is not carried by stroke or CV death" and "every RCT point estimate … favours metformin" were over-absolute). Upstream errors propagate into F2/F4.
- **Origin:** Evolution-log Entry #11 — `06a` §E.1–E.2.

### L-053 (optional — single occurrence; recommend fold into L-050 or defer): Reader-facing process claims carry the scope of the check behind them
- **Role:** synthesis-writer
- **Trigger:** the Methods/Summary describes a verification or registration step ("mọi con số đã khoá", "đăng ký trước", "đã xác minh")
- **Rule:** Restate the claim at the scope of the artifact that proves it (cards locked ≠ every number; a protocol saved before the search ≠ a PROSPERO-type registration); if the reader would need a clause the artifact does not support, drop the claim.
- **Why:** F6 — appraisal wording scoped to quote-locked cards became "every number is locked" in a reader-facing Methods line, and "pre-registered" would be read by internists as PROSPERO. This is the R4 pattern (claiming a step beyond its receipt) in the deliverable rather than the process.
- **Origin:** Evolution-log Entry #11 — `06a` F6, §E.4.

---

## 3. Proposed edits to existing lessons

**E-1 — L-003 (verifier). Strengthen, do not duplicate.** Append to the Rule:
> "…Also match the *stratum* (overall vs subgroup/eGFR band, monotherapy vs add-on) of each number to the sentence's label. A green P8 number lock proves only that the number is in the quote — not which stratum or endpoint it describes — so reading claim vs source side by side is not replaceable by the lock. When you propose replacement wording to the writer, quote the CI-compatible range rather than coining a new absolute ("không từ X"); your own suggestions can over-read (R2-1)."

Why: F1/F2 passed 104/104 locks and L-003's current text ("population, intervention, endpoint") omits the stratum; R2-1 shows the verifier's own FIX wording can over-read.

**E-2 — L-019 (orchestrator).** Append: "At the same moment, change the header of `03_research_map.md` from 'AWAITING USER APPROVAL' to 'CLEARED — see 03a_gate_approval.md'; a stale header lets a reader of the map alone conclude the gate is open (`06a` §E.3)."

**E-3 (optional) — L-011 (legacy tag `strategist`).** Its Role tag `strategist` is a legacy route (to the lead). Suggest retagging to `orchestrator`, and add cross-reference "(see L-045 for keeping found guidelines through the prefilter)". Low priority.

Nothing proposed for deletion. No proposal duplicates an existing lesson (L-011, L-022, L-005, L-043, L-038, L-028 all considered; cited above).

**Rejected-proposal log:** none yet (nothing has been shown to the user).

---

## 4. Not lessons — harness changes the user may want (separate from the digest)

**A. `prefilter_records.py` (supports L-045, L-046).** Add (1) `--seed <ids|--seed-type guideline>` to force-keep named/guideline records before ranking, and (2) `--append` / `--only-new` so a supplementary pass screens new records without re-cutting the pool. Add a regression test in `.claude/tests/`. Changes a script threshold-adjacent behaviour; run the suite and add a CHANGELOG row.

**B. `evidence-appraisal/scripts/extract_numbers.py` (candidate 6).** `CI_PATTERN` needs a branch for the bare form `ratio (a–b)` after OR/RR/HR/aHR/MD (reproduced: `RR 0.96 (0.84-1.09)` and `aHR 1.09 (0.83–1.44)` → no match; `95% CI 0.80-1.03` → match). Add the branch plus a test in `test_extract_numbers.py`; check it does not turn "(0.5-1.0 mg)"-type ranges into CIs (require a preceding ratio token). Impact this run was nil because cards were locked directly.

**C. Contract text (candidate 3).** See D1.

---

## 5. Decisions the user must make

- **D1 — Where machine-fetched text lives.** Today CLAUDE.md calls `source/<folder>/` "user-supplied" while this run (with the user's Gate 4b OK) put 56 NCBI XML files there with `_PROVENANCE.md`. Options: (a) **keep** `source/<folder>/` and amend the contract: "machine-fetched text is allowed only with `_PROVENANCE.md` + SHA-256 manifest; the retriever must ask at Gate 2b" (smallest change; L-012's 'list and ask' stays truthful); (b) new `source/<folder>/_fetched/` (underscore, like `_exports/`) so user-supplied and machine text never mix (cleanest; `verify_quotes.py` path handling to be checked). Recommendation: **(b)** — it parallels `_exports/`, keeps "source/ = what the author gave us" auditable. Needs a CLAUDE.md edit + CHANGELOG row; not made here.
- **D2 — Which of L-045…L-053 to accept**, particularly L-053 (optional) and E-3.
- **D3 — Fix `extract_numbers.py` and `prefilter_records.py` now or log as backlog** (§4-A/B).
- **D4 — Vi-terminology:** no new Vietnamese term was user-confirmed this run, so no change to `vi-terminology.md` is proposed.

---

## 6. Proposed evolution-log entry (text to append after approval — NOT appended)

```
═══════════════════════════════════════════════
### Entry #11 — 2026-10-27 — Metformin efficacy & safety in adult T2D (regression Case 1, EASY, harness of 2026-10-27)
**Task:** Tổng quan hiệu quả + an toàn metformin trong ĐTĐ týp 2 ở người lớn; hỗ trợ quyết định lâm sàng; bác sĩ nội khoa;
"~1500 từ" → amended by the user at Phase 5 to ~1,800–2,000 syllable-tokens ("Rút còn ~1800–2000 từ (Recommended)");
tiếng Việt; nguồn 2015–nay; effort normal (coach SKIPPED, declared). Branch review/regression-2026-10-27. MCP sources only.
**Rubric total:** 0.82 → MET (round 1: 0.785; verifier rounds 1–2, independent)
**Per-criterion:** T1 0.8 · T2 0.8 · T3 0.8 · T4 0.8 · T5 0.9 · T6 0.9   (round 1: 0.8 · 0.8 · 0.8 · 0.7 · 0.7 · 0.9)
**Process:** 8/8 phases PASS; four human gates all cleared with quotable approvals ("Duyệt, tiếp tục" at Gate 2b, Research Map,
Gate 4b; scope confirmed item by item); content decisions asked separately from each gate-closing question (L-044); gate commit
54b04d4 precedes appraisal and draft; source/ listed and asked (L-012); coach SKIPPED declared (L-025); manifest before QA (L-027).
Corpus: identified 260 → included 30 (+6 hand-rescued −3 dropped at the map = 33; 16 HIGH, 17 MEDIUM); deferred-unread 68;
104 quote-locked cards 104/0 rejected; citation_audit PASS exit 0 (33/33 refs, 3 formatting WARNs).
**Violations found:** none of the Supreme-rule type; Law 1 clean (33/33 refs match PubMed, NCT02915198 exists). Round-1 QA:
12 FIX, no BLOCK — five substantive misreads (F1 stratum mislabel; F2 endpoint mismatch; F3 unsupported "chỉ"; F4 null CI read as
absence + over-absolute steelman; F5 dropped direct comparison after the length cut) that all 104 green quote locks did not catch;
F6 reader-facing process overclaim (R4-adjacent, corrected). Process defects (not breaches): prefilter sank key guidelines;
supplementary pass hand-appended; agent-written text in `abstract`; machine text in source/ against the contract; stale map header.
**Ratchet vs prior Case 1 (Entry #2 corrected 0.81: T1 0.70 · T2–T6 0.85; Entry #3 brief 0.81 is a 500-word case, not comparable):**
T1 0.70→0.80 (+) · T2 0.85→0.80 (−0.05) · T3 0.85→0.80 (−0.05) · T4 0.85→0.80 (−0.05) · T5 0.85→0.90 (+) · T6 0.85→0.90 (+).
On the rubric's own 0.2-step scale, 0.85 sits between 0.8 and 1.0 and anti-inflation rule 3 would assign 0.8, so no criterion
dropped a band; the 0.05 moves are inside the stated self-scoring noise. Law/gate checks: Research Map gate fires and is
receipted (Entry #2 violated it), scope confirmed, no check newly fails. **Judgement: KEEP — improvement on T1/T5/T6, no band
regression, gates intact.** Caveats: (1) Entry #2 was self-scored by the lead, this run by an independent verifier with box
counts — scoring regime tightened, so equal numbers are a stronger result than they look; (2) this run changed many things at
once vs June (6-agent team, gates 2b/4b, P8 locks, L-044), so improvement cannot be attributed to a single edit; (3) length
was amended and 33 sources vs ~7 in Entry #2, so depth is not like-for-like; (4) the remaining 0.8s are specific: T1 keywords not
in Methods (length cap), T2 67% tiers 1–3 and 9/16 HIGH abstract-only, T3 mechanism barely discussed, T4 COI unflagged.
**Lessons applied (fired correctly):** L-012, L-014, L-019, L-022, L-024, L-025, L-027, L-032, L-038, L-043, L-044.
**Lessons learned → proposed:** L-045 (known-item lane bypasses prefilter) · L-046 (supplementary = declared second pass, no hand-edit)
· L-047 (efetch at Phase 2, labelled) · L-048 (verbatim abstract) · L-049 (length unit + protect rubric items) · L-050/L-051
(writer self-checks) · L-052 (appraiser inconsistency needs same endpoint) · L-053 optional · edits E-1 (L-003), E-2 (L-019).
**Actions taken:** 07_proposed_lessons.md; code defect extract_numbers.py CI regex reproduced (not fixed); prefilter seed/append
option proposed (not built); source/ contract question D1 raised to user. No change to constitution.
**New rules proposed:** see lesson list above (roles: evidence-retriever ×4, orchestrator+synthesis-writer ×1, synthesis-writer ×3,
critical-appraiser ×1, verifier edit ×1, orchestrator edit ×1).
═══════════════════════════════════════════════
```

Notes for the appender: Entry #11 follows #10 (the log's existing order is not strictly numeric; append at the end).
After appending lessons, run `python3 -m unittest discover -s .claude/tests -t .claude/tests` and
`lessons_digest.py --list-roles` (every new Role must match an agent; this file uses `evidence-retriever`, `synthesis-writer`,
`critical-appraiser`, `orchestrator`, `citation-verifier`). Per the CLAUDE.md workflow, the cross-session knowledge goes to `main`
as a small commit touching only lessons.md, evolution-log.md, vi-terminology.md. A CHANGELOG row is needed for any harness edit (§4).

---

## 7. User decisions (2026-10-27, lead-recorded verbatim)
- D2 lessons: **"L-045–L-052, gộp L-053 (Recommended)"** → accept L-045…L-052; fold L-053 into L-050 as item (e); apply E-1 (L-003) and E-2 (L-019). E-3 (L-011 retag) was optional and not part of the approved option → not applied.
- D1 machine-fetched text location: **"source/<folder>/_fetched/ (Recommended)"** → harness backlog (CLAUDE.md contract edit + `verify_quotes.py` path check); this run's files stay where they are (Gate 4b decision).
- D3 scripts: **"Ghi backlog (Recommended)"** → `extract_numbers.py` CI branch and `prefilter_records.py --seed/--only-new` logged as backlog, not implemented.
- Where to persist: **"Review + claude/lucid-… (Recommended)"** → this review branch + a small knowledge-only commit on `claude/lucid-brahmagupta-1ys4ne`; main untouched.
- D4: no vi-terminology change.
