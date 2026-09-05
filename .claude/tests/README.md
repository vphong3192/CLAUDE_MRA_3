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
| `test_dedupe_records.py` | P4. The three merge thresholds; identifiers matched across formatting; a preprint and its paper merge inside the year guard and are only *reported* outside it; a merged study takes its identity from the published record; clustering independent of input order |
| `test_prefilter_records.py` | P4. The scope bonus is worth strictly less than one concept hit; an empty scope signal is unknown, never out; both recall floors, including through the CLI so the shipped defaults are what runs; ranking independent of input order |
| `test_prisma_flow.py` | P4. Boxes appear only for steps that ran; preprint servers count as databases; retraction and deferral are their own lines, never exclusions; the flow must add up |
| `test_harness_integrity.py` | The harness's own wiring: no dead `L-NNN` pointers in operational files, every agent named by the orchestrator exists, every script a doc points at exists, every `_workspace/` artifact is declared in the CLAUDE.md contract and has a producer outside its consumer, the deterministic layer stays dependency-free |

## Validate by mutation, not by count

A test that cannot fail is theatre. Before trusting a new test, break the thing it guards and
confirm the suite goes red. Every guard here was validated that way, and the first sweep found
three defects in the tests themselves — including a loader that served stale `__pycache__`
bytecode, so the suite ran green against code that was not on disk.

Three traps these sweeps exposed, all variants of *the test examining itself*. Every one of them
produced a green suite over a broken guarantee, so check for all three in any new test:

- **Testing your own copy.** A threshold test that rebuilds the script's `argparse` tests the
  copy, not the script. Read the real value, or go through `main()`.
- **Injecting every default.** If a test always passes its own config, the module's shipped
  constants are never executed and a mutation to them survives. Exercise at least one path
  through the CLI.
- **Filtering by the rule you are asserting.** A test that collects artifacts with
  `[0-9]{2}[a-z]?_…` and then asserts they match `[0-9]{2}[a-z]?_…` can never fail — the
  malformed name is excluded before the assertion sees it. Collect broadly, assert narrowly.
  The same shape appears whenever an exclusion list is keyed differently from the data it
  filters (`path.name` vs a relative path), which silently makes the exclusion a no-op.

## Two rules for adding a test

1. **Pin the number, not the vibe.** A threshold that is not asserted somewhere will drift.
   `min-coverage-frac` defaults to 0.4 because a test says so.
2. **Never loosen a threshold to make a test pass.** If a real store trips a check, the finding
   is the point. Fix the store, or fix the check for a stated reason — never widen it quietly.
