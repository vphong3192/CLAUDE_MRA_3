#!/usr/bin/env python3
"""Rubric total — the arithmetic of `references/rubric.md`, taken out of the verifier's hands.

WHY THIS EXISTS
  The verifier judges each criterion; that is judgment and stays with it. What follows the
  judgment is arithmetic and two written rules, and the LLM got them wrong: regression Case 1
  (Entry #11) reported T5 = T6 = 0.9 on a scale whose levels are 1.0/0.8/0.6/0.4/0.2, so the total
  read 0.82 where the rubric gives 0.80. Same band that time — but an off-grid score always errs
  upward, so across runs it drifts every comparison in the harness's favour, which is exactly what
  the ratchet exists to prevent (L-039: a mechanical step does not stay with the LLM).

WHAT IT DOES
  1. Snaps every score DOWN to the rubric's grid (anti-inflation rule 3: "when between two levels,
     pick the lower"). 0.9 -> 0.8, 0.75 -> 0.6.
  2. Caps a score by its checkbox evidence: no 1.0 unless every box passed (rule 2); T1 and T2
     also map box counts to a ceiling, as the rubric writes them (T1 6/7 -> 0.8, 5/7 -> 0.6;
     T2 4/5 -> 0.8, 3/5 -> 0.6). A cap only lowers; it never raises a score.
  3. Weighted total (0.25/0.20/0.20/0.15/0.10/0.10) and band, in exact integer arithmetic.
  4. `--fabricated` -> T5 = 0.0 and AUTO-FAIL regardless of the total (Law 1), exit 1.
  Every score it moved is listed with the rule that moved it, beside what the verifier reported.

WHAT IT DOES NOT DO
  It does not decide which level a criterion deserves, read the review, or count the boxes —
  the verifier supplies the scores and the box counts. T1's "20+ quality sources" condition for
  1.0 is not checkable here and stays with the verifier.

Python stdlib only; no network; same input -> identical output.
Exit: 0 scored · 1 AUTO-FAIL (fabricated citation) · 2 bad input.

  python3 .claude/skills/citation-verification/scripts/rubric_total.py \
    --score T1=0.8 --score T2=0.8 --score T3=0.8 --score T4=0.8 --score T5=0.9 --score T6=0.9 \
    --boxes T1=6/7 --boxes T2=4/5 --boxes T3=5/6 --boxes T4=5/6 --boxes T5=5/5 --boxes T6=4/4
"""
import argparse
import re
import sys

CRITERIA = ("T1", "T2", "T3", "T4", "T5", "T6")
NAMES = {"T1": "Search comprehensiveness", "T2": "Source quality", "T3": "Synthesis & analysis",
         "T4": "Critical appraisal", "T5": "Citation accuracy", "T6": "Applicability"}
# Weights in hundredths and scores in tenths keep the total exact: no 0.8*0.15 float drift
# can push a review across a band edge.
WEIGHTS = {"T1": 25, "T2": 20, "T3": 20, "T4": 15, "T5": 10, "T6": 10}
BOXES = {"T1": 7, "T2": 5, "T3": 6, "T4": 6, "T5": 5, "T6": 4}
GRID = (2, 4, 6, 8, 10)                     # 0.2 … 1.0 in tenths; T5 alone can be 0.0 (AUTO-FAIL)
# Ceilings the rubric states by box count (passed boxes -> highest level, in tenths).
BOX_CEILING = {"T1": {6: 8, 5: 6}, "T2": {4: 8, 3: 6}}
# Lower bound of each band, in thousandths of the total (weights*tenths = thousandths).
BANDS = ((850, "EXCEEDED"), (700, "MET"), (600, "ADEQUATE"), (500, "BELOW"), (0, "FAIL"))


def parse_pairs(items, kind):
    out = {}
    for item in items or []:
        m = re.fullmatch(r"\s*(T[1-6])\s*=\s*(\S+)\s*", item)
        if not m:
            raise ValueError(f"--{kind} expects T<n>=<value>, got {item!r}")
        if m.group(1) in out:
            raise ValueError(f"--{kind} {m.group(1)} given twice")
        out[m.group(1)] = m.group(2)
    return out


def parse_score(text):
    try:
        v = float(text.replace(",", "."))   # a Vietnamese decimal comma is still a decimal
    except ValueError:
        raise ValueError(f"score {text!r} is not a number")
    if not 0.0 <= v <= 1.0:
        raise ValueError(f"score {text!r} is outside 0–1")
    return v


def parse_boxes(text, crit):
    m = re.fullmatch(r"(\d+)/(\d+)", text)
    if not m:
        raise ValueError(f"--boxes {crit} expects passed/total like 6/7, got {text!r}")
    passed, total = int(m.group(1)), int(m.group(2))
    if total != BOXES[crit]:
        raise ValueError(f"{crit} has {BOXES[crit]} boxes in rubric.md, got /{total}")
    if passed > total:
        raise ValueError(f"{crit} passed {passed} > total {total}")
    return passed, total


def snap_down(v):
    """Highest grid level <= v, in tenths. Exact for every score written to two decimals (checked
    for all 0.00–1.00 in steps of 0.01), which is the precision the rubric uses."""
    tenths = int(v * 10)
    levels = [g for g in GRID if g <= tenths]
    return levels[-1] if levels else None


def score(scores_raw, boxes_raw, fabricated=False):
    """Return (rows, total_thousandths, reported_thousandths, band). Raises ValueError on bad input."""
    missing = [c for c in CRITERIA if c not in scores_raw]
    if missing:
        raise ValueError(f"missing --score for {', '.join(missing)}")
    missing = [c for c in CRITERIA if c not in boxes_raw]
    if missing:
        raise ValueError(f"missing --boxes for {', '.join(missing)} (anti-inflation rule 1: "
                         f"a score needs its checkbox evidence)")
    rows, total, reported = [], 0, 0
    for c in CRITERIA:
        raw = parse_score(scores_raw[c])
        passed, nboxes = parse_boxes(boxes_raw[c], c)
        reported += raw * WEIGHTS[c] * 10           # verifier's own arithmetic, for the record only
        reasons = []
        if c == "T5" and fabricated:
            final, reasons = 0, ["fabricated citation → 0.0 (Law 1 AUTO-FAIL)"]
        else:
            final = snap_down(raw)
            if final is None:
                raise ValueError(f"{c}={raw} is below the lowest level 0.2 — no rubric level fits")
            if abs(final - raw * 10) > 1e-9:
                reasons.append(f"off-grid {raw:g} → {final / 10:.1f} (rule 3: pick the lower level)")
            if final == 10 and passed < nboxes:
                final = 8
                reasons.append(f"1.0 with {passed}/{nboxes} boxes → 0.8 (rule 2: no 1.0 unless all pass)")
            ceilings = BOX_CEILING.get(c, {})
            if passed < nboxes and ceilings:
                cap = ceilings.get(passed, min(ceilings.values()))
                if final > cap:
                    reasons.append(f"{passed}/{nboxes} boxes caps {c} at {cap / 10:.1f} (rubric level)")
                    final = cap
        total += final * WEIGHTS[c]
        rows.append({"crit": c, "raw": raw, "final": final / 10, "boxes": f"{passed}/{nboxes}",
                     "reasons": reasons})
    band = "AUTO-FAIL" if fabricated else next(name for floor, name in BANDS if total >= floor)
    return rows, total, reported, band


def render(rows, total, reported, band):
    out = ["## Rubric total (`rubric_total.py`, deterministic)", "",
           "| Criterion | Weight | Boxes | Verifier | Scored | Adjustment |",
           "|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['crit']} {NAMES[r['crit']]} | {WEIGHTS[r['crit']] / 100:.2f} | {r['boxes']} "
                   f"| {r['raw']:g} | {r['final']:.1f} | {'; '.join(r['reasons']) or '—'} |")
    out += ["", f"**Total: {total / 1000:.2f} — {band}**"
                f" (verifier's own arithmetic: {round(reported) / 1000:.3f})"]
    if any(r["reasons"] for r in rows):
        out.append("Scores were adjusted; report the **Total** line above, not the verifier's arithmetic.")
    out.append("Checks only the arithmetic and the rubric's written rules — which level each "
               "criterion deserves is the verifier's judgment.")
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--score", action="append", metavar="T<n>=<0..1>", help="one per criterion")
    ap.add_argument("--boxes", action="append", metavar="T<n>=<passed>/<total>", help="one per criterion")
    ap.add_argument("--fabricated", action="store_true", help="any fabricated citation (Law 1)")
    args = ap.parse_args(argv)
    try:
        rows, total, reported, band = score(parse_pairs(args.score, "score"),
                                            parse_pairs(args.boxes, "boxes"), args.fabricated)
    except ValueError as e:
        print(f"rubric_total: {e}", file=sys.stderr)
        return 2
    sys.stdout.write(render(rows, total, reported, band))
    return 1 if band == "AUTO-FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
