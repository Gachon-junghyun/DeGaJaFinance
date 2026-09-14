# SECTOR_ROTATION — industry_US — 2026-07-25 (Sat)

> Stage 5/10. **Delta-only.** MACRO §E owns the 11-sector verdict and `SECTOR_FLOW_US.json` owns the
> flow numbers; both are on disk all run. Nothing unchanged gets a row here.
> Flow `asof` **2026-07-24 settled**. Benchmark **SPY** on every RS number (C1). OBV = **C-grade (D6)**.

## §1 · Inherited — MACRO §E, verbatim, one line

`ENRG OW− · IT N · FIN OW− · INDU OW− · HLTH N · COMM N− · UTIL N− · RE N · MATR UW · DISC N− · STPL N`

## §2 · Deltas — five changes, each carried by a flow number

| Sector | Matrix said | Flow evidence (`SECTOR_FLOW_US.json §sector_rotation`) | New | Who resolves |
|---|---|---|---|---|
| **Financials** | OW− | **eqflow +0.342 > wflow +0.278** (gap **+0.064**, *widening* against M40's +0.145→+0.067 narrowing) · **Δ +0.021 = 3rd on the board** · 5🟢/3🔴 of 47 | **OW** | — (promote by rule (b): breadth-led, money moved before the thesis) |
| **Real Estate** | N | **Δ +0.226 = #1 on the board, 2.6× the next sector** · **0 🔴 of 12 — the only sector on the board with zero reds** · wflow +0.163 = 4th of 11 · DLR Δ **+1.099 = the largest single-name delta of all 300** | **OW−** | **DEEP (rotating slot)** |
| **Industrials** | OW− | **wflow −0.049 = 7th of 11** · **17 🔴 of 50** · **Δ −0.068** | **N** | **PREMORTEM** — ⚠ **W5**: the downgrade is on the *label*. The node (UNP +0.867 · CSX +0.856 · LMT +0.856 · NOC +0.744, all 🟢) is untouched by it; capital goods (GEV/CAT/BA/ROK/CARR/CMI, all 🔴) is what the label is measuring |
| **Health Care** | N *(MACRO upgraded it this run)* | **Δ −0.057** · **greens 6 → 5, and UNH is the one that dropped out with Δ −0.305 = the sector's worst** · ABT still 🟡 blocked by `vol_surge` 0.86 alone | **N−** | **DEEP — but no slot; see §3** |
| **Utilities** | N− | **Δ −0.105 = 2nd-worst on the board** · the AI-power leg carries the three worst deltas in the sector (**VST −0.470 · NEE −0.229 · CEG −0.212**) | **UW** | **PREMORTEM** — ⚠ **W5**: PCG is the sector's only 🟢 and a `new_green` with **Δ +0.448**. The regulated leg is being bought and the AI leg sold |
| **Comm Services** | N− | **eqflow +0.047 > wflow −0.064 — an inversion**: breadth positive, mega-caps negative · **breadth 0.15 = 2nd best on the board** · Δ +0.021 | **N** | ⚠ **n = 13 and GOOGL (🔴, flow −0.183) dominates the cap-weight.** Small-n; stated |

★ **Health Care's row reverses an upgrade MACRO made in this same run** — and it does so on flow, not
on a macro re-argument. MACRO upgraded on the **07-24 tape** (XLV +0.70% vs SPY +0.10%, ABT +0.78σ);
the **20-day flow axis** says the green block **thinned from 6 to 5** and the sector delta is negative.
Both are true and they are different windows. **The tape read is one session; the flow read is twenty.**

### Changes DECLINED — and why (logged rather than made)

| Sector | The change that was available | Why it was declined |
|---|---|---|
| **Information Technology** | N → **UW**. The numbers are there: **eqflow −0.206 (2nd-worst on the board)**, **25 🔴 of 56 = the board's worst red count**, breadth 0.07, Δ −0.038, and `wflow +0.155 ≫ eqflow` = mega-cap-narrow | ⚠⚠ **DECLINED on rule D6.** The reds are **OBV-derived, C-grade** — and the names carrying them hold **A-grade RS60 vs SPY of +78.8 (MU) · +39.5 (SNDK) · +36.9 (AMAT) · +29.1 (WDC) · +22.9 (MRVL) · +17.7 (LRCX) · +12.5 (KLAC)**. **A C-grade tag may not override an A-grade one.** Downgrading IT on this evidence would short the exact leg **S6 FIRED-A** on. **The red count is real; its signal grade is not sufficient for a verdict** |
| **Energy** | OW− → **N**, on Δ −0.019 and three negative refiner deltas | **DECLINED.** Energy is still **#1 wflow (+0.440)** and the refiners hold the sector's best RS60 (**MPC +29.1 · VLO +22.1 · PSX +21.4**). MACRO **already** downgraded OW→OW− this run on the same evidence; doing it twice would double-count one observation |
| **Materials** | UW → **UW−** on the board's worst wflow (−0.358), 0🟢/5🔴, breadth 0.00 | **DECLINED — no lower notch exists in this scheme.** Logged so the flow confirmation is on record: MACRO declared a tape disagreement (XLB +1.93% on 07-24) and **the flow resolves it in favour of the UW** |
| **Consumer Staples** | N → N−, on **0 🟢 of 19, breadth 0.00** | **DECLINED.** Δ **+0.058 = 4th-best on the board** cuts the other way. Mixed evidence is not a delta |
| **Cons. Discretionary** | N− → UW, on eqflow −0.143 and 1🟢/8🔴 | **DECLINED.** Δ **+0.088 = 2nd-best**. Same reason |

**Post-delta board:** `FIN OW · ENRG OW− · RE OW− · IT N · COMM N · STPL N · HLTH N− · INDU N ·
DISC N− · UTIL UW · MATR UW`

## §3 · DEEP picks — 3, by the rule, not padded

**Recency input, read from disk (`DEEP_LOG` lines):** `07-15 [INDU/FIN,IT,UTIL]` · `07-17 [FIN,HLTH/ENRG]`
· `07-19 [ENRG,HLTH,FIN]` *(+ RE nominated, **never delivered**)* · `07-21 [ENRG,HLTH/FIN]` ·
`07-22 [ENRG,FIN]` *(+ RE rested again)* · `07-23 [ENRG,FIN/HLTH]` · `07-24 [ENRG,FIN/HLTH]` (+INDU, +IT by PREMORTEM).

**① Continuous-track 2 — the two highest OW-side sectors, both keeping their slots by the anti-thrash rule:**

- **FINANCIALS (OW)** — held a continuous slot 07-22/23/24 and is still the board's top OW today.
  ⚠ **Recency-starved (4 consecutive runs).** Mandate **narrowed, not re-surveyed**: the run's own
  measurement says the sector's answer is inside its sub-nodes, not its label —
  **exchanges are 7-for-7 non-🟢 and 6-for-7 negative on RS60 (NDAQ −3.0 · ICE −10.6 · CME −14.1 ·
  MSCI −11.2 · COIN −22.3) while 6 of 7 are positive on RS20**, exactly M103/M107's registered shape.
  **Mandate: does the exchanges node's confirm test (≥3 crossing to positive RS60 by 2026-08-08) have
  any path, or is the 20-day inflection a dead-cat inside a 60-day de-rate?** Plus **S14 lands 07-30**.

- **ENERGY (OW−)** — held continuously since 07-22, still #1 wflow.
  ⚠ **Recency-starved (6 of the last 7 runs).** Mandate **narrowed to one question, because the run
  produced two-sided primary evidence for the first time**: *the settled 07-24 gap narrowing
  (35.50 → 32.96, first of the run-up) versus Morgan Stanley's and Argus's inventory evidence
  (European diesel to multi-year lows by year-end; PADD1/PADD3/ARA/Fujairah/Singapore all below the
  five-year seasonal range).* **Mandate: which of those two is the operative frame, resolved on
  primary sources — not another RS re-count.** **VLO prints 07-30.**

**② Rotating 1 — the slot the flow demands:**

- ★★ **REAL ESTATE (OW−) — the rotating pick, and it is overdue by every criterion the rule names.**
  - **Recency**: **nominated on 07-19 and never delivered; rested again on 07-22; never deep-dived in
    this entire stretch.** It is the single most recency-starved sector on the board.
  - **Flow**: **Δ +0.226 = #1**, **zero reds — the only such sector**, DLR Δ **+1.099 = the largest
    single-name delta of all 300**.
  - **Coverage**: HANDOVER §7a measured **WELL, AMT, VTR at ZERO ledger reports** while R7/M88 has
    been **replicated on four independent dates** — a belief with four replications and no coverage.
  - **The question that makes it worth a slot**: EVENT_ALPHA Card 4 shows **the carried explanation
    is contradicted by a primary print** (DLR: revenue +29%, AFFO beat 42.5%, guide raised on
    *"robust data center demand"*, $3.5bn Blackstone acquisition) **while the RS60 measurement
    replicates a fifth time (19.1pp)**. **Mandate: separate the measurement from its driver, and
    settle whether "digital infrastructure" is one bucket or three (towers AMT/CCI · data centres
    DLR/EQIX · industrial PLD — the sector's only 🟢 and a `new_green`, which no prior run has named).**

**No 4th pick. NOT padded** — after §2 there is no fourth OW-side sector, and the rule forbids
filling with a Neutral.

### Escalated to PREMORTEM as the promotable extra — **INFORMATION TECHNOLOGY**, for the second run running

ROTATION cannot promote a Neutral, and IT sits at N **only because this stage declined to downgrade it
on a C-grade axis** (§2). Every reason to look at it is larger than it was yesterday:
**S13's cross-condition lands 2026-07-29 (D-4)** · **C8 is the desk's last remaining single-label
sector** after R7 and M26/M108 split the other two · MACRO **self-scored P3's KPI as reversing sign in
one session** while SWEEP measured the split intact **on a different time axis** (spenders own the
20-day, suppliers own the 60-day) · and EVENT_ALPHA Card 1 surfaced **DELL (RS60 +108.6) and HPE
(+66.8) — the two highest RS60 readings on the entire board, in no thread title, with no standing
thesis and no ledger coverage.** **PREMORTEM owns the promotion decision.**

## ✅ EXIT CHECK
- [x] **§1 is ONE line**, inherited verbatim from MACRO §E. No unchanged sector has a row.
- [x] **Every §2 delta cites a flow number** (wflow / eqflow / breadth / Δ / 🟢🔴). **Five changes that
      would have rested on something else were DECLINED and logged** — including **the IT downgrade,
      declined explicitly on rule D6** (a C-grade OBV tag may not override an A-grade RS60).
- [x] Every matrix × flow divergence named **with a resolution owner** (§2, six rows).
- [x] **3 DEEP targets by the rule**: anti-thrash continuity applied and stated (FIN, ENRG, both
      declared recency-starved with **narrowed** mandates); rotating slot to **RE** with its recency,
      flow, coverage and question all stated. **No padding**; the 4th is escalated to PREMORTEM.
- [x] Linter run on this file (result in the run log).
- [x] DEEP_LOG line appended below.
- [x] No sizing, no buy/sell language (P4).

## DEEP_LOG 2026-07-25: continuous=[ENRG, FIN] rotating=[RE]
3 picks — after §2 only three sectors sit at OW/OW−; **NOT padded**. ENRG and FIN keep continuous slots by the anti-thrash rule (both held 07-24, both still top-OW) and **both are declared recency-starved** (ENRG 6 of the last 7 runs; FIN 4 consecutive) — mitigated by **narrowed mandates**: ENRG → *settle the two-sided primary evidence on the diesel bottleneck (07-24 gap narrowing vs Morgan Stanley/Argus inventories), not another RS re-count*; FIN → *the exchanges node's RS20/RS60 contradiction and whether its 08-08 confirm test has a path*. **RE takes the rotating slot — nominated 07-19 and never delivered, never deep-dived in this stretch, #1 delta on the board (+0.226), the only sector with zero reds, zero ledger coverage on WELL/AMT/VTR against four replications of R7, and a carried explanation now contradicted by DLR's primary print.** Deltas this run: **FIN OW−→OW** (eqflow>wflow gap widening to +0.064, Δ +0.021, 5🟢) · **RE N→OW−** (Δ +0.226 #1, 0🔴) · **INDU OW−→N** (wflow −0.049 7th, 17🔴/50; W5 — the rail/defense node is untouched) · **HLTH N→N−** (Δ −0.057, greens 6→5, UNH Δ −0.305; reverses MACRO's same-run tape upgrade, on flow) · **UTIL N−→UW** (Δ −0.105, AI-power leg the three worst deltas; W5 — PCG is a `new_green` at Δ +0.448) · **COMM N−→N** (eqflow +0.047 > wflow −0.064 inversion, breadth 0.15 2nd-best; ⚠ n=13). **Declined: IT N→UW on rule D6** (25🔴/56 and eqflow −0.206 are C-grade against RS60 +12.5~+78.8 A-grade — declining this is the single most consequential call in the file) · ENRG double-downgrade · MATR (no lower notch; flow confirms the UW and resolves MACRO's declared tape disagreement) · STPL and DISC (mixed — both carry top-4 deltas). **Escalated to PREMORTEM as the promotable 4th: INFORMATION TECHNOLOGY**, 2nd consecutive run — S13 lands 07-29, C8 is the last single-label sector, and DELL/HPE carry the board's two highest RS60 (+108.6 / +66.8) with no thesis and no coverage.

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **PREMORTEM**.
