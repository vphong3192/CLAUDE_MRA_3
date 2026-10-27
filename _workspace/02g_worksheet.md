# Deterministic Relevance Prioritisation (P4)

> Ranks studies by concept coverage so the LLM screens the most promising first.
> **A deferred study is UNREAD, not excluded** — the PRISMA flow must say so in those
> words. Scores only ever add; an empty scope signal means unknown, never out; a study
> matching every concept is never cut. No LLM, no network; identical output every run.

- input: `_workspace/02c_studies.jsonl` · concepts: `_workspace/01a_concepts.json`
- config: target_percent=25 · min_candidates=150 · max_candidates=600 · full_coverage_floor=True
- concepts (4): `population`, `intervention`, `comparator`, `outcome`

## Counts
- studies in: **219**
- **retracted, excluded before ranking: 1** (a retracted study cites cleanly — real PMID, real record, withdrawn science)
- ranked: **218**
- selection rule: 25% of 218 = 55, capped at max_candidates 600, then raised to min_candidates 150 if lower → k=150
- candidates to screen: **150** (of which 0 kept by the full-coverage floor)
- deferred (unread, NOT excluded): **68**
- scope split: in 212 · out 2 · unknown 4

## Retracted — excluded, never citable (1)
- `doi:10.1371/journal.pone.0321032` — RETRACTED: Cardiovascular and mortality outcomes of DPP-4 inhibitors vs. sulfony

## Screening worksheet — the LLM fills `verdict` and `reason`

| study_id | year | concepts matched | scope | score | verdict | reason |
|---|---|---|---|---|---|---|
| `doi:10.1111/dom.71315` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.diabres.2026.113503` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/s0140-6736(26)01865-9` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.4067/s0034-98872026000701070` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1186/s13098-026-02226-9` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/s41999-026-01608-6` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1186/s12933-026-03346-2` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.3389/fendo.2026.1877839` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1111/dom.71128` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.2337/db26-0267` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1186/s12902-026-02483-9` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1111/dom.71211` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.diabres.2026.113400` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.phrs.2026.108420` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1186/s12877-026-08386-7` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.2337/dc25-2008` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1111/dom.71396` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.jhsg.2026.101148` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1001/jama.2026.9512` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.phrs.2026.108456` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1186/s12916-026-05182-3` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.jacadv.2026.102681` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/s13300-026-01913-0` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.7326/annals-25-05602` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.19540/j.cnki.cjcmm.20251111.401` | 2026 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1001/jamainternmed.2024.5982` | 2025 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/s12325-025-03323-3` | 2025 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/s2213-8587(25)00196-2` | 2025 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.jdiacomp.2025.109214` | 2025 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/s2213-8587(25)00022-1` | 2025 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1111/dom.16647` | 2025 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1111/dom.70320` | 2025 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.2337/dc24-2825` | 2025 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.jacc.2024.05.069` | 2024 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1136/bmj-2023-077097` | 2024 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.4093/dmj.2023.0077` | 2024 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/s12325-024-03037-y` | 2024 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/978-3-031-63657-8_17` | 2024 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.5114/pm.2024.141090` | 2024 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1053/j.ajkd.2024.08.012` | 2024 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1111/dom.15724` | 2024 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.diabres.2024.111717` | 2024 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.2147/dmso.s396621` | 2023 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `nct:NCT02915198` | 2023 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.3390/ijms242417147` | 2023 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1111/dom.15058` | 2023 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.3390/jcm11237094` | 2022 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1002/dmrr.3515` | 2022 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.21037/jtd-22-550` | 2022 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1186/s12933-020-01202-5` | 2021 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1371/journal.pone.0244689` | 2021 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1055/a-1555-2797` | 2021 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1002/dmrr.3460` | 2021 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/s10741-020-09942-y` | 2021 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1186/s13063-021-05500-5` | 2021 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.18632/aging.202945` | 2021 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.7326/m20-0864` | 2020 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.3389/fendo.2020.559446` | 2020 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1002/14651858.cd012906.pub2` | 2020 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1002/14651858.cd013516.pub2` | 2020 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.diabres.2019.01.025` | 2019 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/s2213-8587(19)30311-0` | 2019 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.diabres.2019.04.008` | 2019 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1177/1060028019889064` | 2019 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.dsx.2019.04.028` | 2019 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/s00592-018-1271-3` | 2019 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/s11892-018-1043-z` | 2018 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.3310/hta21020` | 2017 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/j.hlc.2017.02.030` | 2017 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/s2213-8587(17)30317-0` | 2017 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/s2213-8587(17)30085-2` | 2017 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1016/s2213-8587(17)30092-x` | 2017 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/s00125-017-4337-9` | 2017 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1001/jama.2016.9400` | 2016 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.7326/m15-2650` | 2016 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1002/14651858.cd012151.pub2` | 2016 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1007/s00125-015-3844-9` | 2016 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.25011/cim.v39i2.26481` | 2016 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1038/srep32714` | 2016 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.1177/1479164115570301` | 2015 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `nct:NCT00379769` | 2001 | 4/4 (population, intervention, comparator, outcome) | in | 9 |  |  |
| `doi:10.3389/fendo.2025.1659740` | 2026 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1002/edm2.70316` | 2026 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.3390/jcm15197532` | 2026 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.2337/dc26-0298` | 2026 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1111/ahg.70049` | 2026 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1093/gpbjnl/qzag079` | 2026 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1111/dom.71271` | 2026 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.1007/s00125-026-06855-7` | 2026 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1007/s40262-026-01699-1` | 2026 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1111/dom.71062` | 2026 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1159/000551916` | 2026 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.3390/diseases14100387` | 2026 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1016/j.ejphar.2026.178560` | 2026 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.7759/cureus.116607` | 2026 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1111/dom.70915` | 2026 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1186/s12933-026-03292-z` | 2026 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.1080/14786419.2026.2689480` | 2026 | 3/4 (population, intervention, comparator) | in | 7 |  |  |
| `doi:10.1111/jdi.70125` | 2025 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1136/bmjnph-2024-000950` | 2025 | 3/4 (population, intervention, comparator) | in | 7 |  |  |
| `doi:10.2337/dc25-0241` | 2025 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1111/jdi.70103` | 2025 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1111/jdi.70037` | 2025 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1186/s13098-025-02040-9` | 2025 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.1186/s12967-025-06357-x` | 2025 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `title:medication time of metformin and sulfonylureas and incidence` | 2025 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1136/bmj-2024-083039` | 2025 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1161/circulationaha.124.071689` | 2024 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1111/1753-0407.13553` | 2024 | 3/4 (population, intervention, comparator) | in | 7 |  |  |
| `doi:10.1016/s2213-8587(24)00271-7` | 2024 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1007/s00125-024-06133-4` | 2024 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `nct:NCT06846411` | 2024 | 3/4 (population, intervention, comparator) | in | 7 |  |  |
| `doi:10.1186/s12902-024-01727-w` | 2024 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.2337/dc22-2494` | 2024 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.17925/ee.2024.20.2.7` | 2024 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.12688/wellcomeopenres.19455.2` | 2024 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.1002/14651858.cd013414.pub2` | 2024 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.1101/2024.01.07.24300938` | 2024 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.7326/m23-2788` | 2024 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.7326/m23-1490` | 2024 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1093/ageing/afad254` | 2024 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `title:the impact of metformin on mortality in patients with type 2` | 2024 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1371/journal.pone.0302500` | 2024 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1136/bmj-2022-074068` | 2023 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1016/j.trsl.2023.08.001` | 2023 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.7326/m22-3018` | 2023 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1080/17474124.2022.2118112` | 2022 | 3/4 (population, intervention, comparator) | in | 7 |  |  |
| `doi:10.1007/s40265-021-01665-0` | 2022 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.3389/fendo.2022.975912` | 2022 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1056/nejmoa2200433` | 2022 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1016/s0140-6736(22)02074-8` | 2022 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1016/s2213-8587(21)00203-5` | 2021 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1186/s12978-021-01207-7` | 2021 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.3389/fendo.2021.735824` | 2021 | 3/4 (population, intervention, comparator) | in | 7 |  |  |
| `doi:10.3389/fendo.2021.609110` | 2021 | 3/4 (population, intervention, comparator) | in | 7 |  |  |
| `doi:10.3389/fphar.2021.669814` | 2021 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1136/bmj.m4573` | 2021 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1186/s12888-020-02992-4` | 2021 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.1016/j.diabres.2020.108001` | 2020 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1016/j.cct.2020.106067` | 2020 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.2337/dc19-0936` | 2020 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `pmid:30845101` | 2019 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1016/s2213-8587(19)30249-9` | 2019 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1111/dom.13642` | 2019 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1016/s0140-6736(18)32261-x` | 2018 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `doi:10.1158/1055-9965.epi-17-0936` | 2018 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.1111/dom.13553` | 2018 | 3/4 (population, comparator, outcome) | in | 7 |  |  |
| `nct:NCT03627039` | 2018 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |
| `doi:10.2337/dc17-2231` | 2018 | 3/4 (population, intervention, outcome) | in | 7 |  |  |
| `doi:10.3233/jad-180263` | 2018 | 3/4 (intervention, comparator, outcome) | in | 7 |  |  |

## Deferred — unread, available if the corpus proves thin (68)
- `doi:10.1186/s12889-018-5419-4` (2018) score 7 — Protocol for the CHORD project (community health outreach to reduce di
- `doi:10.1016/s0140-6736(18)32590-x` (2018) score 7 — SGLT2 inhibitors for primary and secondary prevention of cardiovascula
- `doi:10.1016/j.jcjd.2018.04.004` (2018) score 7 — Safe Use of Metformin in Adults With Type 2 Diabetes and Chronic Kidne
- `pmid:30136463` (2018) score 7 — [Cardiovascular safety of DPP-4 inhibitors compared to that of sulfony
- `doi:10.2337/dc17-0417` (2017) score 7 — Efficacy and Safety of Once-Weekly Semaglutide Versus Exenatide ER in 
- `doi:10.1016/j.arr.2017.08.003` (2017) score 7 — Metformin reduces all-cause mortality and diseases of ageing independe
- `doi:10.1016/j.diabet.2016.03.008` (2016) score 7 — Association between metformin and vitamin B12 deficiency in patients w
- `doi:10.1097/md.0000000000002749` (2016) score 7 — Metformin Is Associated With Slightly Reduced Risk of Colorectal Cance
- `doi:10.1002/dmrr.2713` (2015) score 7 — Comparative efficacy of anti-diabetic agents on nonalcoholic fatty liv
- `doi:10.4103/2230-8210.146861` (2015) score 7 — Incretin response in Asian type 2 diabetes: Are Indians different?
- `doi:10.1007/s12020-015-0841-1` (2015) score 7 — Systematic review and meta-analysis of vildagliptin for treatment of t
- `title:metformin in patients with type 2 diabetes and kidney diseas` (2014) score 7 — Metformin in Patients With Type 2 Diabetes and Kidney Disease
- `title:reduced cardiovascular morbidity and mortality associated wi` (2005) score 7 — Reduced cardiovascular morbidity and mortality associated with metform
- `doi:10.1080/15563650.2025.2607437` (2026) score 5 — Hemodynamic instability in severe metformin-associated lactic acidosis
- `title:identification of a genetic risk factor for metformin induce` (2026) score 5 — Identification of a genetic risk factor for metformin-induced vitamin 
- `title:metformin beyond glycemic control cardiovascular protection ` (2026) score 5 — Metformin Beyond Glycemic Control: Cardiovascular Protection and Diabe
- `doi:10.1002/edm2.70232` (2026) score 5 — The Impact of Metformin on Vitamin B12 Levels in Children and Adolesce
- `doi:10.1136/bmjopen-2025-100672` (2025) score 5 — Association between vitamin B12 deficiency and metformin use in type 2
- `doi:10.1111/jdi.70185` (2025) score 5 — Prevalence and risk factors of sarcopenia in Asian adults with type 2 
- `doi:10.1371/journal.pntd.0013281` (2025) score 5 — Safety and tolerability of metformin in overweight and obese patients 
- `doi:10.1210/clinem/dgaf238` (2025) score 5 — The Microbial Regulation Spectrum of Metformin in Patients With Type 2
- `title:vitamin b12 deficiency in long term metformin use and clinic` (2025) score 5 — Vitamin B12 deficiency in long-term metformin use and clinician awaren
- `doi:10.3390/cancers16173017` (2024) score 5 — A Narrative Review: Repurposing Metformin as a Potential Therapeutic A
- `title:metformin for type 2 diabetes mellitus` (2024) score 5 — Metformin for Type 2 diabetes mellitus
- `doi:10.1016/j.diabres.2024.111691` (2024) score 5 — Progress toward universal health coverage in Vietnam: Evidence on disp
- `nct:NCT06627322` (2024) score 5 — Registry Based Randomized Controlled Trial of Multiple Combination Str
- `doi:10.1016/j.diabres.2024.111930` (2024) score 5 — The prognostic significance of diabetes in non-small cell lung cancer 
- `title:vitamin b12 deficiency in patients taking metformin pathogen` (2024) score 5 — Vitamin B12 Deficiency in Patients Taking Metformin: Pathogenesis and 
- `title:vitamin b12 deficiency in diabetic patients treated with met` (2024) score 5 — Vitamin B12 deficiency in diabetic patients treated with metformin: A 
- `doi:10.23750/abm.v94is3.14405` (2023) score 5 — Metformin and Covid-19: a systematic review of systematic reviews with
- `doi:10.2337/dci22-0027` (2022) score 5 — Diabetes Management in Chronic Kidney Disease: A Consensus Report by t
- `doi:10.1097/cad.0000000000001254` (2022) score 5 — Effect of metformin use on the risk and prognosis of colorectal cancer
- `doi:10.1016/j.kint.2022.06.013` (2022) score 5 — Executive summary of the KDIGO 2022 Clinical Practice Guideline for Di
- `doi:10.1136/dtb.2022.000004` (2022) score 5 — Extended versus immediate-release metformin.
- `doi:10.1007/s00125-022-05787-2` (2022) score 5 — Management of hyperglycaemia in type 2 diabetes, 2022. A consensus rep
- `title:metformin induced vitamin b12 deficiency can cause or worsen` (2022) score 5 — Metformin-induced vitamin B12 deficiency can cause or worsen distal sy
- `doi:10.1111/dom.14313` (2021) score 5 — Cardiovascular and renal safety of metformin in patients with diabetes
- `doi:10.1210/clinem/dgaa692` (2021) score 5 — Exenatide, Metformin, or Both for Prediabetes in PCOS: A Randomized, O
- `title:long term metformin therapy and vitamin b12 deficiency an as` (2021) score 5 — Long-term metformin therapy and vitamin B12 deficiency: An association
- `doi:10.2217/fca-2020-0195` (2021) score 5 — Metformin in the era of new antidiabetics.
- `doi:10.1002/jmv.26498` (2020) score 5 — Mortality risk with preadmission metformin use in patients with COVID-
- `doi:10.2337/dci20-0040` (2020) score 5 — Response to Comment on Kwon et al. The Long-term Effects of Metformin 
- `title:significance of metformin use in diabetic kidney disease` (2020) score 5 — Significance of Metformin Use in Diabetic Kidney Disease
- `doi:10.1016/j.jceh.2019.06.003` (2019) score 5 — Antidiabetic Drugs and Statins in Nonalcoholic Fatty Liver Disease.
- `doi:10.1016/j.diabet.2019.101117` (2019) score 5 — Efficacy and safety of once-weekly semaglutide 1.0mg vs once-daily lir
- `title:metformin time to review its role and safety in chronic kidn` (2019) score 5 — Metformin: time to review its role and safety in chronic kidney diseas
- `title:long term metformin use and vitamin b12 deficiency in the di` (2016) score 5 — Long-term Metformin Use and Vitamin B12 Deficiency in the Diabetes Pre
- `title:reappraisal of metformin efficacy in the treatment of type 2` (2012) score 5 — Reappraisal of Metformin Efficacy in the Treatment of Type 2 Diabetes:
- `doi:10.3390/ijms27167211` (2026) score 3 — Paracetamol and Metformin Reduce NK-Cell Susceptibility in MCF-7 Breas
- `doi:10.1158/1055-9965.epi-25-1306` (2026) score 3 — The Potential Impact of Histamine-2 Receptor Antagonists on Gynecologi
- … and 18 more (full list in the deferred JSONL)
