# source/metformin-t2d/ — provenance of the text files in this folder

**Not user-supplied.** Every `.xml` file here was fetched on 2026-10-27 (Phase 4, critical-appraiser)
by a deterministic script that called NCBI E-utilities directly
(`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi`, `db=pubmed` for the abstract record,
`db=pmc` for the PMC full-text article) and wrote the response bytes to disk unchanged.
No model transcribed, edited or summarised any of this text. Per-file URL, byte count, SHA-256 and
whether a full-text `<body>` was served are in `_fetch_manifest.json`.

- Scope: only the 33 user-approved records of the Research Map gate (`_workspace/03_research_map.md`,
  final list). Dropped records MET-M02, M13, M17 were NOT fetched.
- Naming: `<store id>_<PMID>_pubmed.xml` (PubMed record incl. abstract) and
  `<store id>_<PMID>_pmc.xml` (PMC article; full text only where `has_body` is true in the manifest).
- PMC served a full-text body for: MET-H04, H05, H08, H10, H12, H13, S02, M04, M07, M08, M09, M10,
  M11, M12, M14, M19. PMC returned front matter only (no body) for MET-H02, H06, H14, S01, S03.
  No PMC record exists for MET-H01, H03, H07, H09, H11, M01, M03, M05, M06, M15, M16, M18.
- What a green `verify_quotes.py` lock against these files proves: the quote is literally present in
  text served by NCBI (not written by a model), and the file carries the study's own PMID. It does
  not prove the PMC rendering is identical to the publisher's version of record, nor that the
  claim reads the quote correctly.
- Why this happened at Phase 4: at Phase 2/Gate 2b the MCP returned empty bodies and WebFetch was
  DNS-blocked; direct HTTPS to eutils.ncbi.nlm.nih.gov through the session proxy works. The user's
  Gate 2b choice was "Tải PMC + thử web" (fetch PMC texts), so this completes that instruction;
  it adds no new study.
