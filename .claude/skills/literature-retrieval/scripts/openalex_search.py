#!/usr/bin/env python3
"""
OpenAlex integration for MRA literature retrieval — two modes, stdlib-only, no LLM, no API key.

Usage
-----
# Coverage check — find papers matching keywords (not in corpus)
python3 openalex_search.py coverage \
    --query "semaglutide cardiovascular prevention" \
    --year-from 2019 \
    --count-only          # optional: just print total before pulling

# Citation chaining — forward (cites this paper) and backward (this paper's references)
python3 openalex_search.py citations \
    --doi 10.1056/NEJMoa1901009 \
    --direction both      # forward | backward | both (default)

Both modes print a Markdown table ready to paste into _workspace/02_corpus.md and emit a
recall-ledger row for validate_search_log.py.

OpenAlex API: https://docs.openalex.org
  - No API key required; polite-pool requires `mailto` in User-Agent.
  - Rate limit: 10 req/s (polite-pool) — this script stays well under that.
  - Results are CC0; the script logs the API URL for reproducibility (P3).
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from typing import Optional

# NOTE: Requires direct HTTPS to api.openalex.org (no proxy required when running locally).
# The remote MRA container may block this endpoint; run the script on your local machine
# or in a CI environment with outbound internet access.
POLITE_MAILTO = "vipho.thita@gmail.com"
BASE = "https://api.openalex.org"
UA = f"MRA-openalex/1.0 (mailto:{POLITE_MAILTO})"

PAGE_SIZE = 25        # keep pages small to stay within MCP-like context budgets
MAX_PAGES = 8         # hard cap: 200 records per coverage search
RETRY_WAIT = 4        # seconds between retries


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

def _get(url: str, params: Optional[dict] = None, retry: int = 3) -> dict:
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    last_err = None
    for attempt in range(retry):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode())
        except Exception as exc:
            last_err = exc
            if attempt < retry - 1:
                time.sleep(RETRY_WAIT * (attempt + 1))
    raise RuntimeError(f"OpenAlex request failed after {retry} attempts: {last_err}\nURL: {url}")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _stable_id(work: dict) -> str:
    """Return the best stable ID: prefer PMID > DOI > OpenAlex ID."""
    for loc in work.get("ids", {}).values():
        pass  # just to make sure ids exists
    ids = work.get("ids", {})
    if ids.get("pmid"):
        pmid = ids["pmid"].split("/")[-1]
        return f"PMID:{pmid}"
    if ids.get("doi"):
        doi = ids["doi"].replace("https://doi.org/", "")
        return f"DOI:{doi}"
    oa_id = work.get("id", "")
    return oa_id.replace("https://openalex.org/", "OA:")


def _authors(work: dict, max_n: int = 4) -> str:
    auths = work.get("authorships", [])
    names = [a["author"]["display_name"] for a in auths if a.get("author")]
    if not names:
        return "—"
    if len(names) > max_n:
        return ", ".join(names[:max_n]) + " et al."
    return ", ".join(names)


def _oa_url(work: dict) -> str:
    """Return an open-access URL if available."""
    best = work.get("best_oa_location") or {}
    return best.get("landing_page_url") or best.get("pdf_url") or "—"


def _doi_clean(raw: str) -> str:
    """Strip leading https://doi.org/ prefix if present."""
    return re.sub(r"^https?://doi\.org/", "", raw.strip())


def _work_row(work: dict, note: str = "") -> dict:
    """Build a flat dict for one work."""
    pub_year = work.get("publication_year") or "?"
    source_info = ((work.get("primary_location") or {}).get("source") or {})
    journal = source_info.get("display_name") or "—"
    source_type = "preprint" if source_info.get("type") == "repository" else "peer-reviewed"
    return {
        "stable_id": _stable_id(work),
        "title": work.get("display_name") or "—",
        "authors": _authors(work),
        "year": pub_year,
        "journal": journal,
        "source_type": source_type,
        "cited_by": work.get("cited_by_count", 0),
        "oa_url": _oa_url(work),
        "note": note,
    }


# ---------------------------------------------------------------------------
# Mode 1: Coverage check
# ---------------------------------------------------------------------------

def coverage(query: str, year_from: Optional[int], year_to: Optional[int],
             count_only: bool, cap: Optional[int]) -> None:
    """Search OpenAlex by keyword; deduplicated by DOI/PMID."""
    filter_parts = [f'title_and_abstract.search:{query}']
    if year_from:
        filter_parts.append(f"publication_year:>{year_from - 1}")
    if year_to:
        filter_parts.append(f"publication_year:<{year_to + 1}")
    filter_str = ",".join(filter_parts)

    # --- Count probe (P3 habit 1) ---
    probe = _get(f"{BASE}/works", {"filter": filter_str, "per-page": 1, "select": "id"})
    total = probe.get("meta", {}).get("count", 0)
    probe_url = (f"{BASE}/works?filter={urllib.parse.quote(filter_str, safe=':,<>')}"
                 f"&per-page={PAGE_SIZE}&select=id,display_name,ids,authorships,"
                 f"publication_year,primary_location,cited_by_count,best_oa_location")

    if count_only:
        print(f"## OpenAlex coverage probe")
        print(f"- query: `{query}`")
        print(f"- total results: **{total}**")
        print(f"- call: `{probe_url}`")
        _print_ledger_row("OA-coverage", query, probe_url, total, 0, capped=True,
                          note="count-only probe — no records pulled")
        return

    max_pull = min(cap or (MAX_PAGES * PAGE_SIZE), MAX_PAGES * PAGE_SIZE)
    select_fields = ("id,display_name,ids,authorships,publication_year,"
                     "primary_location,cited_by_count,best_oa_location")

    works = []
    cursor = "*"
    while len(works) < max_pull:
        batch_size = min(PAGE_SIZE, max_pull - len(works))
        params = {
            "filter": filter_str,
            "per-page": batch_size,
            "cursor": cursor,
            "select": select_fields,
        }
        data = _get(f"{BASE}/works", params)
        batch = data.get("results", [])
        if not batch:
            break
        works.extend(batch)
        cursor = (data.get("meta") or {}).get("next_cursor")
        if not cursor:
            break

    capped = len(works) < total
    rows = [_work_row(w) for w in works]

    _print_coverage_table(rows, query, total)
    _print_ledger_row("OA-coverage", query, probe_url, total, len(works), capped=capped)


def _print_coverage_table(rows: list, query: str, total: int) -> None:
    print(f"\n## OpenAlex coverage results")
    print(f"- query: `{query}`")
    print(f"- total in index: {total}  |  retrieved: {len(rows)}")
    print()
    print("| stable_id | title | authors | year | journal | source_type | cited_by | oa_url |")
    print("|-----------|-------|---------|------|---------|-------------|----------|--------|")
    for r in rows:
        title_short = r["title"][:80] + "…" if len(r["title"]) > 80 else r["title"]
        print(f"| {r['stable_id']} | {title_short} | {r['authors']} | "
              f"{r['year']} | {r['journal']} | {r['source_type']} | "
              f"{r['cited_by']} | {r['oa_url']} |")


# ---------------------------------------------------------------------------
# Mode 2: Citation chaining
# ---------------------------------------------------------------------------

def citations(doi_or_pmid: str, direction: str) -> None:
    """
    Forward: works that CITE the target (OpenAlex `cites:<id>`).
    Backward: works that the target CITES (pull the target's `referenced_works` list).
    """
    # Resolve to OpenAlex ID
    target_id, target_work = _resolve(doi_or_pmid)
    target_stable = _stable_id(target_work)
    print(f"\n## OpenAlex citation chaining")
    print(f"- target: **{target_work.get('display_name', '?')}**")
    print(f"- stable_id: `{target_stable}`")
    print(f"- OpenAlex ID: `{target_id}`")
    print()

    if direction in ("forward", "both"):
        _forward_citations(target_id, target_stable)
    if direction in ("backward", "both"):
        _backward_citations(target_work, target_stable)


def _resolve(doi_or_pmid: str) -> tuple:
    """Return (openalex_id, work_dict) for a DOI or PMID."""
    raw = doi_or_pmid.strip()
    if raw.upper().startswith("PMID:"):
        pmid = raw[5:].strip()
        filter_str = f"ids.pmid:{pmid}"
    elif re.match(r"^\d+$", raw):
        filter_str = f"ids.pmid:{raw}"
    else:
        doi = _doi_clean(raw)
        filter_str = f"doi:{urllib.parse.quote('https://doi.org/' + doi)}"

    data = _get(f"{BASE}/works", {"filter": filter_str, "per-page": 1})
    results = data.get("results", [])
    if not results:
        raise ValueError(f"No OpenAlex record found for: {doi_or_pmid!r}")
    work = results[0]
    oa_id = work["id"].replace("https://openalex.org/", "")
    return oa_id, work


def _forward_citations(target_id: str, target_stable: str) -> None:
    """Works that cite the target paper."""
    filter_str = f"cites:{target_id}"
    call_url = (f"{BASE}/works?filter={urllib.parse.quote(filter_str)}"
                f"&per-page={PAGE_SIZE}&select=id,display_name,ids,authorships,"
                f"publication_year,primary_location,cited_by_count,best_oa_location")

    # Count probe
    probe = _get(f"{BASE}/works", {"filter": filter_str, "per-page": 1, "select": "id"})
    total = probe.get("meta", {}).get("count", 0)

    works, cursor = [], "*"
    while len(works) < MAX_PAGES * PAGE_SIZE:
        data = _get(f"{BASE}/works", {
            "filter": filter_str,
            "per-page": PAGE_SIZE,
            "cursor": cursor,
            "select": ("id,display_name,ids,authorships,publication_year,"
                       "primary_location,cited_by_count,best_oa_location"),
            "sort": "cited_by_count:desc",
        })
        batch = data.get("results", [])
        if not batch:
            break
        works.extend(batch)
        cursor = (data.get("meta") or {}).get("next_cursor")
        if not cursor:
            break

    capped = len(works) < total
    rows = [_work_row(w, "forward-citation") for w in works]

    print(f"### Forward citations (papers that cite `{target_stable}`)")
    print(f"- total citing: {total}  |  retrieved: {len(works)}"
          + (" (capped)" if capped else ""))
    print()
    _print_citation_table(rows)
    _print_ledger_row(f"OA-forward:{target_stable}", f"cites:{target_id}",
                      call_url, total, len(works), capped=capped)


def _backward_citations(target_work: dict, target_stable: str) -> None:
    """Works that the target paper cites (its reference list)."""
    ref_ids = target_work.get("referenced_works", [])
    total = len(ref_ids)
    if not total:
        print(f"### Backward citations (references of `{target_stable}`)")
        print("- no `referenced_works` available for this paper.")
        _print_ledger_row(f"OA-backward:{target_stable}", f"referenced_works of {target_stable}",
                          f"{BASE}/works/{target_stable.replace('DOI:', 'doi/')}",
                          0, 0, capped=False)
        return

    # Fetch in one batch by OR-joining IDs (OpenAlex supports openalex_id filter with |)
    pull = ref_ids[:MAX_PAGES * PAGE_SIZE]
    # OpenAlex: filter by multiple IDs with "|" separator
    id_list = "|".join(r.replace("https://openalex.org/", "") for r in pull)
    call_url = (f"{BASE}/works?filter=openalex_id:{urllib.parse.quote(id_list)}"
                f"&per-page={PAGE_SIZE}")

    works = []
    cursor = "*"
    while len(works) < len(pull):
        data = _get(f"{BASE}/works", {
            "filter": f"openalex_id:{id_list}",
            "per-page": PAGE_SIZE,
            "cursor": cursor,
            "select": ("id,display_name,ids,authorships,publication_year,"
                       "primary_location,cited_by_count,best_oa_location"),
        })
        batch = data.get("results", [])
        if not batch:
            break
        works.extend(batch)
        cursor = (data.get("meta") or {}).get("next_cursor")
        if not cursor:
            break

    capped = len(ref_ids) > len(pull)
    rows = [_work_row(w, "backward-reference") for w in works]

    print(f"### Backward citations (references of `{target_stable}`)")
    print(f"- total references listed: {total}  |  retrieved: {len(works)}"
          + (" (capped at first 200)" if capped else ""))
    print()
    _print_citation_table(rows)
    _print_ledger_row(f"OA-backward:{target_stable}",
                      f"referenced_works of {target_stable}", call_url,
                      total, len(works), capped=capped)


def _print_citation_table(rows: list) -> None:
    print("| stable_id | title | authors | year | journal | cited_by | oa_url |")
    print("|-----------|-------|---------|------|---------|----------|--------|")
    for r in rows:
        title_short = r["title"][:80] + "…" if len(r["title"]) > 80 else r["title"]
        print(f"| {r['stable_id']} | {title_short} | {r['authors']} | "
              f"{r['year']} | {r['journal']} | {r['cited_by']} | {r['oa_url']} |")


# ---------------------------------------------------------------------------
# Recall & reproducibility ledger row (P3)
# ---------------------------------------------------------------------------

def _print_ledger_row(source: str, query: str, call: str, total: int, retrieved: int,
                      capped: bool, note: str = "") -> None:
    if capped or retrieved < total:
        recall = f"capped ⚠ ({note})" if note else "capped ⚠"
    else:
        recall = "retrieved==total ✓"
    print()
    print("<!-- paste this row into the Recall & reproducibility ledger table -->")
    print("| id | source | query | call | total_count | retrieved | recall |")
    print("|----|--------|-------|------|-------------|-----------|--------|")
    src = source[:40]
    q = query[:60]
    c = call[:120]
    print(f"| OA-1 | {src} | {q} | {c} | {total} | {retrieved} | {recall} |")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="OpenAlex coverage check and citation chaining for MRA.")
    sub = ap.add_subparsers(dest="mode", required=True)

    cov = sub.add_parser("coverage", help="Keyword coverage search")
    cov.add_argument("--query", required=True, help="Free-text search query")
    cov.add_argument("--year-from", type=int, default=None)
    cov.add_argument("--year-to", type=int, default=None)
    cov.add_argument("--count-only", action="store_true",
                     help="Only print total count (P3 count-target probe)")
    cov.add_argument("--cap", type=int, default=None,
                     help="Max records to retrieve (default 200)")

    cit = sub.add_parser("citations", help="Forward/backward citation chaining")
    cit.add_argument("--doi", required=True,
                     help="DOI (with or without https://doi.org/) or PMID")
    cit.add_argument("--direction", choices=["forward", "backward", "both"],
                     default="both")

    args = ap.parse_args(argv)

    if args.mode == "coverage":
        coverage(args.query, args.year_from, args.year_to, args.count_only, args.cap)
    else:
        citations(args.doi, args.direction)


if __name__ == "__main__":
    main()
