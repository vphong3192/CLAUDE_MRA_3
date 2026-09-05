# Harness test-suite

Automated regression tests for the harness's deterministic layer (P1/P2/P3) and for the
structural integrity of the harness files themselves.

```bash
python3 -m unittest discover -s .claude/tests -t .claude/tests -v   # verbose
python3 -m unittest discover -s .claude/tests -t .claude/tests      # quiet; exit 1 on failure
```

Stdlib only — no pip install, no network, no LLM, no fixtures fetched at run time. Same
constraints as the scripts under test, so the suite runs anywhere Python 3 runs.

## What each file guards

| File | Guards |
|---|---|
| `test_citation_audit.py` | P1. Every HARD-FAIL category fires on its own trigger; WARNs never block; the 40% coverage default; Law 1's exit-code contract |
| `test_extract_numbers.py` | P2. The five buckets and their priority order; Vietnamese decimal commas; metadata scrubbing; the `CI` word-boundary guard; empty bucket renders `(none)`, never a placeholder |
| `test_validate_search_log.py` | P3. The seven required ledger columns; each HARD-FAIL cause in isolation; recall verdicts consistent with their own numbers |
| `test_harness_integrity.py` | The harness's own wiring: no dead `L-NNN` pointers in operational files, every agent named by the orchestrator exists, every script a doc points at exists, the deterministic layer stays dependency-free |

## Two rules for adding a test

1. **Pin the number, not the vibe.** A threshold that is not asserted somewhere will drift.
   `min-coverage-frac` defaults to 0.4 because a test says so.
2. **Never loosen a threshold to make a test pass.** If a real store trips a check, the finding
   is the point. Fix the store, or fix the check for a stated reason — never widen it quietly.
