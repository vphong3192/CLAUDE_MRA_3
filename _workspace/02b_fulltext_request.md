# Gate 2b — Full-text supplement request + corpus integrity sweep

**Date:** 2026-06-29 · **By:** lead (orchestrator)

## A. Corpus integrity sweep (lead re-verified ALL new records REF-041…072 via `get_article_metadata`)

Retriever's new set had a meaningful defect rate concentrated in the GAP families (Vietnamese, AERP/AFCL,
conduction velocity) — the well-known landmark P-wave/SAECG/IAB papers were retrieved correctly.

| Record | Problem found | Resolution |
|---|---|---|
| REF-046 Manios | PMID 12843685 → actually a drug RCT (amiodarone/diltiazem, Cardiovasc Drugs Ther); AERP 194–211/AFCL 161–180 ms unverified | ⛔ QUARANTINED (do not cite) |
| REF-050 "Takahashi CV" | PMID 37350738 → actually a histology paper; CV 0.43±0.12 m/s fabricated | ⛔ QUARANTINED (do not cite) |
| REF-051 Ye 2024 | False title/DOI/values (ECGI, 0.52/0.44 m/s); real = epicardial CV 46–66 cm/s | ✅ corrected to true content |
| REF-052 Vickneson 2025 | False title/DOI/values (omnipolar multicenter, 0.38 m/s); real = peri-atrial fat, CV 0.627/0.683 m/s | ✅ corrected |
| REF-071 Nguyen | Reconstructed citation; real = AECOPD study | ✅ corrected, re-tier MEDIUM |
| REF-072 Tran | Reconstructed citation + false "LA EP" claim; real = CF-catheter economics, no EP data | ✅ corrected, re-tier LOW |
| REF-038 Bayés/imaging | Wrong first author/title | ✅ corrected (Hernandez-Betancor); PMC5730959 |
| REF-067 centenarians | Year 2016 → 2015 | ✅ corrected |
| REF-041–045, 047–049, 053–066, 068–070 (26 records) | verified — title/author/year/DOI match store | ✅ OK |

**Citable corpus after sweep:** 70 records (72 − 2 quarantined). The citation-verifier (Phase 6) will
re-verify every record again before delivery.

## B. PMC open-access full texts — LEAD will retrieve (user need NOT supply)

| REF | PMID | PMC | Why valuable |
|---|---|---|---|
| **064 Chen 2022 ISE/ISHNE consensus** ⭐ | 35333097 | PMC9070127 | Gold-standard P-wave parameter definitions/thresholds |
| 063 Alexander 2021 | 33438553 | PMC8142376 | P-wave indices taxonomy (IAB, P-axis, PTF-V1, PWD, MVP) |
| 060 Dilaveris 2001 | 11333174 | PMC7027606 | PWD normative + measurement standards |
| 058 Kawczynski 2022 | 35993895 | PMC9492265 | SAECG MA (N=20,201) |
| 070 Chattopadhyay 2022 | 36454918 | PMC9714955 | P-axis MA (N=78,222) |
| 038 Hernandez-Betancor 2017 | 28707575 | PMC5730959 | Bayés syndrome + imaging |

## C. Paywalled — PLEASE SUPPLY PDF into `source/la-ep-elderly-af/` (prioritized)

### ⭐⭐⭐ Top priority (anchor the core CRF thresholds)
| REF | PMID | DOI | Anchors |
|---|---|---|---|
| 042 Kistler 2004 | 15234418 | 10.1016/j.jacc.2004.03.044 | **THE age-stratified normative**: AERP, cSNRT, P-wave, voltage by age |
| 053 Fukunami 1991 | 1984879 | 10.1161/01.cir.83.1.162 | SAECG landmark: filtered-P Ad>120 ms |
| 059 Dilaveris 1998 | 9588401 | 10.1016/s0002-8703(98)70030-4 | PWD landmark: Pmax≥110 ms, PWD≥40 ms |
| 043 Lee 2016 | 27005930 | 10.1016/j.hrthm.2016.03.037 | AERP≥280 ms → new-onset AF (12-y) |

### ⭐⭐ High value
| REF | PMID | DOI | Anchors |
|---|---|---|---|
| 048 Laredo 2018 | 30404745 | 10.1016/j.cjca.2018.08.007 | AERP aging paradox review |
| 066 BAYES registry 2020 | 32449904 | 10.1093/europace/euaa114 | advanced IAB in ≥70y → AF/stroke |
| 041 Michelucci 1984 | 6693212 | 10.1016/0167-5273(84)90060-3 | earliest aging AERP-dispersion data |
| 055 Guidera 1993 | 8123070 | 10.1016/0735-1097(93)90381-a | filtered-P ≥155 ms |
| 054 Steinberg 1993 | 8252672 | 10.1161/01.cir.88.6.2618 | SAECG >140 ms → post-op AF |

### ⭐ Useful (supply if convenient)
| REF | PMID | DOI |
|---|---|---|
| 047 Raitt 2004 | 15149416 | 10.1046/j.1540-8167.2004.03217.x |
| 049 Hocini 2003 | 12952840 | 10.1161/01.CIR.0000090685.13169.07 |
| 065 Bayés de Luna 2020 | 32684442 | 10.1016/j.rec.2020.04.026 |
| 068 Escobar-Robledo 2018 | 29801761 | 10.1016/j.ijcard.2018.05.050 |
| 069 Lampert 2023 | 37354170 | 10.1016/j.jacep.2023.04.006 |
| 062 Wattanachayakul 2024 | 39368070 | 10.1111/pace.15084 |
| 061 Aytemir 2000 | 10914366 | 10.1111/j.1540-8159.2000.tb00910.x |
| 067 Martínez-Sellés 2015 (centenarians) | 26520207 | 10.1016/j.hrthm.2015.10.034 |
| 056 Darbar 2002 | 12418742 | 10.1046/j.1460-9592.2002.01447.x |
| 057 Palano 2020 | 32451990 | 10.1007/s40292-020-00390-1 |
| 044 Yu 1998 | 9639377 | 10.1161/01.cir.97.23.2331 |
| 045 Yu 1999 | 10533582 | 10.1016/s0008-6363(99)00030-9 |

### To RE-FIND (quarantined; supply restores the anchor)
- **REF-046 Manios** — intended paper: *"Atrial electrophysiological properties associated with successful
  or failed cardioversion after chronic atrial fibrillation," PACE 2003;26:1545* (different PMID than the
  bad one stored). If you have this PDF it restores the AERP/AFCL persistent-AF anchor.
