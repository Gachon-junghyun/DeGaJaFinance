# SECTOR_ROTATION — industry_US — 2026-08-06 (Thu) · **delta-only**

> 🚨🚨 **CORRECTION BANNER — added at DEEP, by this run's own later stage. READ BEFORE THE TABLE BELOW.**
> **Four of the five DEEP agents refuted the reasoning of a §2 delta, and one delta is WITHDRAWN
> outright.** The rows below are left **verbatim and uncorrected** so the error is inspectable; the
> corrections are authoritative and live in `BET_SHEET.md §0`. Summary:
>
> | §2 row | what DEEP found | status |
> |---|---|---|
> | **Health Care N → OW−** | The carrier — *"the ONLY sector whose entire green set is volume-lit"* — is **FALSE and vacuous**: `velocity` is populated on **exactly universe mcap-ranks 1–51, zero exceptions**, and HLTH's three greens sit at ranks **66 / 111 / 254**, so the velocity path never existed for them; **four** sectors have all-volume-lit green sets (DISC, HLTH, **INDU**, RE). **Δ +0.328 is 48.2% LLY alone** (🟡, OBV 중립, RS20 −7.1); the three greens are **6.8%** of it. **All six HLTH names with `vol_surge` ≥ 1.2 reported Q2 inside the window — 6 of 6** ⇒ `vol_surge` here is an **earnings-date detector**. And the **07-30 HLTH deep's own registered anti-signal FIRED on the promotion bar** (XLV 5-day excess **−6.78pp** while SPY rose **+5.53%**). | 🚨 **WITHDRAWN — reverts to N** |
| **Financials OW− → OW** | The cited leg (breadth 0.15, 5 new-🟢) is an **instrument artifact**: `velocity` was populated on **51/300 (08-03) → 0/300 (08-04) → 0/300 (08-05) → 51/300 (today)**, and FIN's breadth tracks it 1:1 (**0.106 → 0.085 → 0.043 → 0.149**). **JPM, BAC and MA were already 🟢 on 07-31** — the `new_green` flags fired because the axis blinked off across both baseline runs. Removing velocity board-wide drops FIN to **breadth 0.043, rank 6 of 11**. | ⚠ **VERDICT STANDS, REASONING REPLACED** — on legs the promotion never cited |
| **Energy OW− → N+** | The **0.285 wflow/eqflow gap is an arithmetic identity**, not a signal: XOM + CVX are ~55% of the sector's measured cap across 16 names. The informative number is **Δ −0.129**, and it is **the refiners' own** (PSX −0.318 · VLO −0.277 · MPC −0.167 are the sector's three largest negative deltas). | ⚠ **LEVEL DEFENSIBLE, REASON MIS-ARGUED** |
| **Materials UW− → N−** | **`eqflow +0.167` is 63.4% two names** (NUE+STLD of 12); **`Δ +0.204` contains steel at exactly 0.000** (NUE +0.022, STLD −0.022); and **LIN alone contributes −0.1251 of the +0.0713 wflow** ⇒ **ex-LIN, wflow +0.2609 > eqflow +0.2285 — mega-cap-led, the OPPOSITE characterisation.** ★ **S36's firing move was 63% LIN on its own 8-K day** (07-31, −6.67pp of LIN's −9.24 five-session excess); **steel contributed +0.10pp upward.** | ⚠ **ARTIFACT — both axes were right and were reading different companies** |
| **Utilities UW, conviction raised** | not contested | ✅ stands |
>
> ★ **And a consistency failure inside §3 that DEEP-HLTH caught**: Staples was declined on **S1**
> (*"a rank-2 delta on two negative levels is not a verdict"*) while **HLTH — a rank-1 delta on
> rank-7 wflow and rank-6 eqflow levels — was promoted.** **The same objection was not applied to
> both.** That is the error, not the Staples call.

> Notation used here, stated once so no sign is ambiguous: **OW · OW− (weak OW) · N+ / N / N− ·
> UW− (weak UW) · UW.** Flow numbers are from `SECTOR_FLOW_US.json` (**asof 2026-08-05 settled**,
> D74-trimmed — `SWEEP_READ.md §1`). The 11-sector reasoning lives in `MACRO_REPORT.md §G` and is
> **not** reprinted.

## §1 · Inherited from MACRO §G — one line, verbatim

`MACRO holds: ENRG OW− · FIN OW− · INDU OW− · IT N · HLTH N · DISC N · COMM UW · MATR UW− · UTIL UW · STPL UW · RE UW`

---

## §2 · Deltas — five moves, every one carried by a flow number

| sector | matrix said | flow evidence (wflow · eqflow · breadth · Δd/d · 🟢/🔴) | **new verdict** | who resolves |
|---|---|---|---|---|
| **Health Care** | **N** | **Δ +0.328 — #1 of 11.** wflow +0.075 · eqflow **+0.055** · breadth 0.09 · **3🟢/5🔴** — ★ and **all three greens clear `vol_surge` ≥ 1.2 (AMGN 1.27 · BMY 1.55 · IDXX 1.43): the ONLY sector on the board whose entire green set is volume-lit** | **OW−** | **DEEP-HLTH** (rotating slot) |
| **Financials** | **OW−** | **rank 1 on BOTH axes** — wflow **+0.317** · eqflow **+0.190** (2nd) · **breadth 0.15, the highest of 11** · Δ +0.187 (4th) · **7🟢/7🔴 with 5 new-🟢 (JPM · BAC · WFC · BRK-B · PRU)** | **OW** | **DEEP-FIN** (continuous slot) |
| **Energy** | **OW−** | **Δ −0.129 — LAST of 11.** eqflow **−0.055** against wflow **+0.230** = a **0.285 concentration gap**, the widest on the board · **5🔴 of 16** · the only positive-wflow sector with negative eqflow | **N+** *(down one notch, rule (a))* | **DEEP-ENRG** (rotating slot — see §3) |
| **Materials** | **UW−** | **eqflow +0.167 (3rd of 11)** and **Δ +0.204 (3rd)** against **0🟢 and breadth 0.00** | **N−** *(up one notch)* | **DEEP** — ⚠ **no slot this run; logged** |
| **Utilities** | **UW** | wflow **−0.398** · eqflow **−0.392** · **0🟢 / 12🔴 of 15** · breadth 0.00 — **0.411 below the next-worst sector (STPL −0.013 wflow)** | **UW, conviction RAISED** *(no verdict change)* | — |

★ **Two of the five are sign-level facts, not degrees**: **Energy is the only sector where wflow and
eqflow disagree in sign** (the concentration tell the L2 names explicitly), and **Health Care is the
only sector whose greens are all volume-confirmed** — which matters because
`SWEEP_READ.md §2` measured that **10 of the board's 28 greens are velocity-lit with `vol_surge` below
1.2**, including four of Financials' five new-🟢.

---

## §3 · Attempts DECLINED, logged rather than made

| attempt | why declined |
|---|---|
| **Consumer Staples UW → N−** on **Δ +0.246, #2 of 11** | 🚫 **Declined.** Both levels are negative (wflow −0.013, eqflow −0.085) with **0🟢**, so the only carrier is a **one-day delta = n ≈ 1 (S1)**. **A rank-2 delta on top of two negative levels is not a verdict.** ★ Recorded so the next run's delta can be read as a second observation rather than a first |
| **Comm Services UW → N−** on **Δ +0.147** | 🚫 **Declined.** **0🟢 of 13 and breadth 0.00.** The only real reason to move it is **P28 (the Alphabet leadership exodus)**, which is a **macro/news argument — explicitly not a delta** — and it post-dates the bar anyway |
| **Energy: re-point the OW from "Hormuz" to the product spread** | 🚫 **Not a sector-level delta and deliberately not made here.** The finding is **intra-sector**: the two 🟢 tags (XOM, CVX) are **velocity-lit** on a narrative measured decaying **20→4 outlets**, while the names carrying the 60-day money (**MPC RS60 +17.2 · VLO +21.1 · PSX +13.7**, OBV 매집) are 🟡 and invisible to the tag filter. **DEEP-ENRG owns it** (`EVENT_ALPHA` Card 1, `MACRO §0-b`) |
| **IT N → anything** | 🚫 **No move.** wflow **+0.246** against eqflow **+0.001** with **7🟢/17🔴** — the widest internal split on the board **confirms** the Neutral rather than challenging it (C8's shape). **Flow agrees with the matrix** |

---

## §4 · DEEP picks — N = 4 (protocol budget: 2 continuous + 2 rotating)

**Continuous track (⌈4/2⌉ = 2) — today's top OW ranks:**
- **FIN** — **new to the continuous track.** It is now the #1 sector on **both** flow axes and was
  promoted to **OW** in §2. ⚠ **It was dropped from continuous on 08-05** ("N+, no longer top-OW"),
  so this is a re-entry on a fresh number, not thrash.
- **INDU** — **anti-thrash continuity applied and stated**: it held a continuous slot on 08-05 and is
  still in the OW family today (**OW−**, eqflow **+0.179 > wflow +0.126** = the board's only
  breadth-led OW). **Slot kept.**

**Rotating track (⌊4/2⌋ = 2):**
- **HLTH** — ★ **the 08-05 DEEP_LOG pre-committed this exact pick** (*"HLTH — C7 re-check due 08-06 —
  ★next run's first rotating pick"*). **The date arrived, C7's own registered resolving observable
  fired** (`SWEEP_READ.md §5`), and the sector posted the board's #1 delta. **Last deep-dived
  2026-07-30 — 5 runs ago, the least-recently-covered non-UW sector.** Every selection criterion
  points the same way.
- **ENRG** — ⚠⚠ **taken under rule (a), and the recency violation is stated rather than hidden.**
  Rule (a) requires that when a matrix-OW sector's money is absent, the verdict rotates down **and the
  divergence becomes the #1 question the DEEP stage must resolve (early vs trap).** Energy was
  downgraded in §2 on the board's **worst delta (−0.129)** and its **only sign-split between wflow and
  eqflow.** It was covered **08-05**, so this breaks the ~3-run recency rule **deliberately**.
  ⚠ **This is a divergence-resolution assignment, not padding** — the L1 forbids padding with
  Neutral/UW to reach N, and this slot exists because rule (a) mandates it, not to fill a quota.

**N = 4 / 4.**

### DEEP mandates — one line each, so the stage cannot re-derive the sector

| slot | the one question |
|---|---|
| **DEEP-FIN** | The promote is carried by **breadth 0.15 and eqflow +0.190** — but **4 of the 5 new-🟢 (JPM · BAC · WFC · BRK-B) are velocity-lit with `vol_surge` 0.72–0.85**, and **M173 says BRK-B alone is 13.94% of sector cap**. **Does the breadth survive removing BRK-B and removing the velocity axis?** ⚠ **P13‴ (2s10s flattening three consecutive prints, 23bp from S23's kill line) points the other way** — name which side the money is on |
| **DEEP-INDU** | The board's **only** OW where eqflow **exceeds** wflow. **EMR +0.917 · ETN +0.878 · AME +0.776 are all 🟢, all OBV 매집, all volume-lit** — and **three of the four sit in S62's basket, which settles 08-07.** ⚠⚠ **S62 asks whether OW− Industrials and UW Utilities are ONE bet wearing two GICS labels. Answer that before the sector is treated as a second idea** |
| **DEEP-HLTH** | C7's resolver fired — **what exactly did it resolve?** The greens are **AMGN (cap-rank 6) · BMY (16) · IDXX (27)**; **JNJ itself is 🟡, `vol_surge` 0.88, RS20 −5.5.** ⇒ **the name that carried the contradiction is not the name that resolved it.** ⚠ **W5**: is this a *sector* signal or three unrelated single-name events? And the revision books were the original "against" leg (+0.5–1.4% CY EPS/90d) — **re-measure them** |
| **DEEP-ENRG** | ★★★ **This run's #1 question.** `MACRO §0-b` names the distillate spread's physical object as **Russian refining capacity + an EXTENDED export ban** (24-year-low processing, 24 of 34 largest refineries hit), **not** the Strait. **R46 binds: name the physical object.** Resolve: (i) is the 0.285 wflow/eqflow gap **early** or a **trap**; (ii) **the tag map and the money map point at different sub-legs** — the greens are integrated and velocity-lit, the RS60 is in refining; (iii) **PSX's Atlantic Basin margin MISSED at $14.44 vs $19.77 while every other region beat** — Europe is the geography closest to the Russian shortfall. ⚠ **S55 settles 08-11 and its branch B is now the live hypothesis** |

---

## DEEP_LOG 2026-08-06: continuous=[FIN, INDU] rotating=[HLTH, ENRG] · N=4/4 · FIN re-entered continuous (promoted to OW on rank-1-both-axes; dropped 08-05) · ENRG moved to rotating under rule (a) and its recency rule broken deliberately (covered 08-05) · uncovered=[MATR(N−, upgraded on eqflow +0.167 / Δ +0.204 vs 0🟢 — ★next run's first rotating pick; S36 FIRED-B today, S57 settles 08-12; covered 08-03), IT(N, covered 08-05, S30 FIRED-B today, S13 08-12), UTIL(UW conviction raised, covered 08-05, S35/S47 settle 08-07, S62 08-07), DISC(N, covered 08-03, two windows disagreeing a 3rd run), RE(UW, covered 08-04, S25 08-08), COMM(UW, covered 2026-07-28 — **9 runs uncovered** and it just had a head-tier event with no observable, P28), STPL(UW, delta #2 on the board but declined on n≈1 — never claimed by a proposition; ADM/CTAS on the missed ledger, recheck 08-16)]
