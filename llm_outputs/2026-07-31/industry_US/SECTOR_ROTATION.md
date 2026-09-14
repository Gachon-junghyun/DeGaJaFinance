# SECTOR_ROTATION — industry_US · 2026-07-31

> Delta-only. MACRO owns the 11-sector verdict (`MACRO_REPORT.md §E`); `SECTOR_FLOW_US.json §sector_rotation`
> owns the flow numbers. This file writes only what the money **changes** and the DEEP picks. Benchmark
> SPY inline throughout (C1). Sweep is asof the **previous close (07-30)**; MACRO's tape legs are the
> live-unsettled 07-31 bar (S6) — the two are not the same clock and are labelled where they meet.

## §1 · Inherited (verbatim from MACRO §E)

`MACRO holds: ENRG OW− · FIN OW− · IT N(split) · CONS-DISC N+(live-only) · COMM N · RE N · STPL N · HLTH N · INDU UW− · MATR UW · UTIL UW−`

## §2 · Deltas — where the money disagrees with the thesis

**Delta count that flips a verdict: 0.** The 07-30 flow sweep **confirms the matrix's direction on all 11**
— the three top-wflow sectors (Energy, Info Tech, Financials) are exactly MACRO's two OW− + the N-split, and
the bottom-three wflow (Materials −0.364 worst · Utilities −0.332 · Comm Svc −0.152) are all matrix-N/UW.
No sector is promoted or demoted on flow. Two **divergences are named** (below) — neither changes a verdict;
both are handed to DEEP as the early-vs-trap question the sweep cannot answer.

| sector | matrix said | flow evidence (`SECTOR_FLOW_US.json §sector_rotation`, asof 07-30) | verdict | who resolves |
|---|---|---|---|---|
| **Info Tech** | N (split unresolved) | wflow **+0.199 ≫ eqflow −0.113** (breadth negative; only mega-caps up) · new-🟢 STX/CSCO/NVDA | **N held** — the flow *confirms* the split rather than resolving it: money is mega-cap-narrow, storage (STX new-🟢) is the one breadth-up leg | **DEEP-IT** — is storage/STX the real early leg, or is the whole complex a mega-cap mirage ahead of S30 (08-05)? |
| **Energy** | OW− (5d excess −1.99 vs SPY) | wflow **+0.471 (#1) AND eqflow +0.358 (#1 breadth 0.19, best on board)** — accumulating *broadly*, not a mega-cap head-fake | **OW− held** — the 5d fade + the broad OBV-매집 are consistent with *war-premium deflation*, not distribution; do not promote on a broad accumulation whose driver could be the deflating-crude leg | **DEEP-ENRG** — deflation (S31/S8 branch B) vs the distillate-crunch refining margin (S49/P4 branch A) |

⚠ **Declined macro re-arguments** (would-be deltas reverted to MACRO's verdict): none attempted — every §2 row above is carried by a flow number, not a macro thesis. Materials/Utilities UW were left at MACRO's verdict (flow agrees; no re-argument added here).

⚠ **Shortlist artifact carried forward from SWEEP (not a delta, a data caveat for DEEP):** Energy's 🟢-tagged
shortlist names (XOM/CVX/BKR) are the *wrong three* — the refining thesis **VLO/MPC/PSX is OBV-매집 (RS20
+16.7/+18.3/+20.2) but tagged 🟡** because they sit in the news-demoted mcap tail (only 48/300 names got the
news-velocity axis this run — a documented sweep throttle, not evidence). DEEP-ENRG reads the refiners directly.

## §3 · DEEP picks and DEEP_LOG

**Recency input, `DEEP_LOG` lines read from disk:** `07-28 [ENRG,FIN]/[IT,COMM]` · `07-29 [ENRG,FIN]/[INDU]` · `07-30 [ENRG,FIN]/[HLTH,RE]`.

**N = 4** (protocol DEEP budget: 2 continuous + 2 rotating; the budget line is unchanged 2026-07-31 and a US-specific measurement would be needed to shrink it).

- **Continuous ⌈N/2⌉ = [ENRG, FIN].** Both are today's top-2 OW ranks **and** both held the continuous slot in the 07-30 run → anti-thrash continuity **KEEPS** both. ENRG carries the run's live both-branch node (P4/S49 vs S31/S8, MPC 08-04 · PSX 08-05 inside the window); FIN gained a *fresh measured mechanism* this run (the bear steepener 2s10s +0.35→+0.45 is NIM-positive, S23 flattener receding — the OW no longer rests on the retracted breadth reason R32, which is exactly what DEEP must now re-argue on the insurance/bank node).
- **Rotating ⌊N/2⌋ = [IT, UTIL].** ⚠ **The board carries only 2 OW sectors (ENRG, FIN), both taken by the continuous track — there is no third/fourth OW to rotate.** Rather than pad with an uninformative slot, the two rotating slots go to the run's **two sharpest matrix×flow divergences** (the anti-tunnel purpose of the US desk's N=4):
  - **IT** — the #2-wflow sector with the unresolved N-split (§2); recency-eligible (last IT rotate **07-28**, >3 runs ago). DEEP resolves supplier-vs-spender / storage-vs-equipment before S30 settles 08-05.
  - **UTIL** — the two-leg split (regulated-defensive vs the AI-power leg CEG/VST/GEV/VRT); **least-recently-covered** of all sectors (absent from the entire recent DEEP_LOG window), and MACRO's demote is being *vindicated* on the tape (XLU worst, −4.74pp 5d vs SPY) precisely as the AI-power selloff dominates — DEEP separates the two legs (S24/S35/S47; CEG/LNG 08-06, VST 08-07).
- **OW sectors left without a DEEP slot: none** (both OW sectors are on the continuous track). The two rotating slots are explicitly *non-OW divergence picks*, stated so the next run's recency rule distinguishes "looked and passed" from "never looked."

## DEEP_LOG 2026-07-31: continuous=[ENRG, FIN] rotating=[IT, UTIL]

## ✅ EXIT CHECK
- [x] §1 is ONE line inheriting MACRO's matrix verbatim; no unchanged sector gets a row/paragraph.
- [x] Every §2 delta cites a flow number; no macro re-argument smuggled in as a delta (none attempted).
- [x] Every matrix×flow divergence named with a resolution owner (DEEP-IT, DEEP-ENRG).
- [x] N=4 DEEP targets picked by the rule (continuity + recency stated); no OW padding — rotating slots are declared non-OW divergence picks because only 2 OW sectors exist.
- [x] Linter run on this file — see below.
- [x] DEEP_LOG line appended for the next run.
- [x] Delta count 0-flip stated honestly as a valid informative run, not manufactured differences.
