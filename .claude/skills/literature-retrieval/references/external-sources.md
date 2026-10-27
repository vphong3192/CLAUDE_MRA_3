# Widening recall beyond the MCP source map (P7)

Loaded on demand from `literature-retrieval/SKILL.md` — read it when the author has supplied database
exports, or when you call Europe PMC / OpenAlex / Semantic Scholar.


The MCP source map is not the whole literature. Three additions, in descending order of value.

### 1 · Author-supplied exports — the biggest gain, and it costs no credential

The harness has no Scopus, Web of Science, Embase or CENTRAL access and **must never try to get
it**: an automated agent querying those platforms uses someone's institutional subscription in a
way their licence forbids. The author has that login. They export; the script reads the file.

Ask at Phase 0, not at retrieval — the answer changes the whole search plan, and by Phase 2 it is
too late to redo the strategy around a source you did not know you had. Files go in
`source/<folder>/_exports/`, with a manifest beside them:

```json
{"exports": [
  {"file": "scopus_2026-09-05.ris", "label": "scopus", "database": "Scopus",
   "query_string": "TITLE-ABS-KEY(cryoballoon AND \"atrial fibrillation\")",
   "date_searched": "2026-09-05", "n_reported": 412, "prisma_column": "database"}
]}
```

```bash
python3 .claude/skills/literature-retrieval/scripts/import_external.py \
  --export-dir source/<folder>/_exports/ --manifest source/<folder>/_exports/manifest.json \
  --out-records _workspace/02b_records_external.jsonl --out _workspace/02b_import.md
```

Then concatenate into `02b_records.jsonl` before running dedupe — imported records use the same
schema, so P4 handles them with no special casing.

RIS · NBIB/MEDLINE · BibTeX · CSV are parsed. **Three things this refuses to do quietly:**
- **A file with no manifest entry is not imported.** An export carries records but not the search
  that produced them, and PRISMA-S needs the query, the date, the database and the reported count.
  An unrecorded search is an unreproducible one, and it would sit in the corpus looking recorded.
- **`prisma_column` is declared, never guessed.** A Scopus export arrived by hand but is still a
  *database search*. Filing it under "other methods" understates the systematic search — a false
  claim about the method. A colleague's suggested reference genuinely is `other`.
- **`n_reported` vs records parsed is compared.** Most platforms cap one download far below the
  result count, so a truncated export is the commonest silent recall loss in a manual workflow.
  A shortfall is reported per file; re-export in batches before trusting the corpus.

### 2 · Three no-key APIs, via `WebFetch`

**Europe PMC · OpenAlex · Semantic Scholar** need no key and cover ground PubMed does not
(Europe PMC adds European and grey literature; OpenAlex and S2 reach beyond biomedicine and expose
citation graphs). They have no MCP here, so the retriever calls them with `WebFetch` and records
the URL verbatim in the ledger's `call` column — a URL is the most reproducible call form there is.

```
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json&pageSize=100
https://api.openalex.org/works?filter=title_and_abstract.search:...&per-page=200&mailto=<email>
https://api.semanticscholar.org/graph/v1/paper/search?query=...&limit=100&fields=title,year,externalIds,abstract
```

Every hit still needs its PMID or DOI confirmed in PubMed before entering the store, exactly as
for the web-supplementary protocol above. OpenAlex's `mailto` is a courtesy that buys a faster
pool — use the author's address only with their say-so.

### 3 · Pacing — a discipline, not a mechanism

Nothing in this harness throttles anything: the deterministic layer never touches the network and
the MCP servers pace themselves. So this is a rule **you** follow, and saying otherwise would be
claiming a safeguard that does not exist. Space unauthenticated calls to the same host — roughly
3/second at NCBI without a key, 1/second at Semantic Scholar. On a 429, slow that host down for
the rest of the run rather than retrying politely and returning to the old rhythm; retrying at the
same rate is how an IP gets blocked for everyone sharing it.
