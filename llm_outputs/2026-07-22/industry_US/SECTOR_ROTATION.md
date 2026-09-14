# SECTOR_ROTATION — industry_US — 2026-07-22

> Stage 4/10. **Delta-only.** MACRO §E owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow
> numbers; both stay on disk. This file writes what *changes*, why, and the 4-DEEP pick. Zero buy/sell.
> Inputs: MACRO §E (top-down) × `SECTOR_FLOW_US.json` **asof 2026-07-21 close** (money now) ×
> `EVENT_ALPHA.md` cards (bottom-up). Every RS figure is **vs SPY** (C1).

## §1 · Inherited from MACRO §E (verbatim, one line)

`ENRG OW+ · FIN OW · IT N · COMM N · INDU N+ · UTIL N− · RE UW · HLTH UW · MATR UW · DISC N− · STPL N`

## §2 · Deltas — sectors where the money disagrees with the thesis

| Sector | Matrix said | Flow evidence (wflow · eqflow · breadth · Δd/d · 🟢/🔴 of n) | New verdict | Who resolves |
|---|---|---|---|---|
| **Health Care** | UW | **wflow +0.453 = #1 of 11** · eqflow +0.318 · breadth **0.06 (best on board)** · Δ +0.024 · **🟢2 / 🔴2 of 32** | **UW → Neutral** (one notch) | **DEEP** — the run's #1 divergence |
| **Info Tech** | N | wflow −0.118 · **eqflow −0.289 (worst on board)** · breadth **0.00** · **🟢0 / 🔴29 of 56** | **N → UW** | PREMORTEM (binary tonight), then DEEP next run |
| **Industrials** | N+ | wflow **−0.167 (#9)** · eqflow −0.116 · breadth 0.04 · Δ −0.046 · 🟢2 / **🔴17 of 50** | **N+ → N−** | — (resolved here) |
| **Utilities** | N− | wflow −0.078 · eqflow −0.110 · **Δ −0.183 = worst deterioration of the 11** · 🟢0 / 🔴2 of 15 | **N− → UW** | — (resolved here) |
| **Cons. Discretionary** | N− | wflow +0.022 but **eqflow −0.103** · breadth 0.00 · Δ −0.066 · **🟢0 / 🔴8 of 28** | **N− → UW** | — (resolved here) |

**Why each delta is admissible (every one is carried by a flow number, not a macro re-argument):**

- **Health Care.** The matrix is UW on two narrative legs (only negative Q2 EPS growth; the up-to-200%
  pharma tariff). The money did the opposite: it is the **#1 sector on mega-cap-weighted flow with the
  best breadth on the board**. ⚠ **The divergence is dated, not resolved** — the sweep closes 07-21
  and the tariff printed 07-22 [11 articles / 7 outlets]. One notch, not a reversal: *the flow is real
  but it is pre-catalyst.* EVENT_ALPHA Card 5 splits the sector — the tariff hits **pharma**
  (LLY/MRK/ABBV/BMY/AMGN), while the sector's actual RS leadership is **managed care**, which has no
  import exposure (**HUM RS60 +82.5**, CVS +34.6, UNH +17.4 vs SPY). **DEEP must decide whether the
  07-21 bid was early or a trap.**
- **Info Tech.** **0 greens of 56 and 29 reds** is the worst breadth on the board and is *not* a
  filter artifact — IT names fail even the OBV+RS20 pre-gate (see SWEEP_READ §3, where 99 names pass
  that pre-gate and IT contributes 13, none of which clear). This is a **flow verdict, not a
  directional bet into tonight's print**; PREMORTEM must still bracket the binary both ways.
  ⚠ **The sector label is the wrong unit here (W5)**: MU −20.4 / SNDK −30.6 / WDC −25.7 / INTC −25.7 /
  LRCX −21.9 / KLAC −19.7 on RS20 vs SPY against AAPL +9.8 / MSFT +7.8 — a **~40pp intra-sector spread**.
  The UW describes the memory/equipment complex, not the mega-cap platform names.
- **Industrials.** MACRO's N+ rested on nuclear + defense order flow. The flow says money is *leaving*:
  #9 of 11, 17 reds of 50, and the two greens (CTAS, TRI) are business services, not defense. EVENT_ALPHA
  Card 6 independently removed the nuclear leg — the Saudi civil-nuclear epicenter (BWXT, SMR,
  Westinghouse) is **not in `us_top300`**, and the in-universe adjacents are declining (GEV RS20 −4.8 /
  RS60 −11.8; CEG 🔴). Defense itself is split: GD +0.508 and RTX +0.444 positive, NOC RS60 −18.4.
- **Utilities.** The **worst day-over-day deterioration of the 11** (Δ −0.183) with zero greens — flow
  agrees with the bond-proxy-into-a-120-day-high-real-yield read rather than merely restating it.
- **Cons. Discretionary.** The wflow/eqflow inversion runs the *wrong* way (mega-cap positive, breadth
  −0.103) on 0 greens and 8 reds of 28 — the sector's positive headline number is a small number of
  large names, and TSLA (−0.583 🟡, RS20 −7.0) prints tonight.

**Attempts declined, logged rather than made:**
- **Comm Services N → (no change).** wflow −0.271 is #10, but eqflow is +0.003 and Δ +0.145 is the
  2nd-best improvement on the board — the negative *is one name*, GOOGL (−0.428, RS20 −1.2 / RS60 −3.2),
  being de-risked into its own print, while META is +0.578. **A one-name sector number is not a sector
  verdict.** Logged as a watch.
- **Cons. Staples N → (no change).** eqflow **+0.129** against wflow **−0.131** — a breadth-positive /
  mega-cap-negative inversion, the same shape logged as a watch on 07-21. **Watch, not a tilt** —
  an inversion is a question, and this stage does not have the input to answer it.
- **Energy OW+ → (held, with a stated caveat).** By rule (a) a matrix-OW sector with **breadth 0.00**
  and **0 greens of 16** should rotate down a notch. **Declined, and here is the measured reason:**
  the 🟢 gate on the US path requires `OBV 매집 AND RS20>0 AND vol_surge≥1.2` (news velocity is `None`
  for all 300 rows, so a 4-axis majority becomes 3-axis unanimity). **99 of 300 names pass OBV+RS20 and
  are blocked solely by `vol_surge<1.2`; Energy's four are XOM, VLO, MPC, PSX** — exactly the refining
  complex. Energy's zero-green is a **volume-surge artifact**, not absent money: VLO/MPC/PSX carry
  **RS20 +25 to +29 and RS60 +27 to +39 vs SPY**. Energy is also **Δ +0.218 = the largest day-over-day
  improvement of the 11**. Held at OW+, with the breadth question handed to DEEP.

## §3 · DEEP picks

**Recency input — US `DEEP_LOG` lines read from disk:**
- `DEEP_LOG 2026-07-21 (US_2): continuous=[Energy, Financials] rotating=[HealthCare, InfoTech] · swing=[Industrials/Defense]`
- `DEEP_LOG 2026-07-21 (industry_US): continuous=[ENRG, HLTH] rotating=[FIN]`
- `DEEP_LOG 2026-07-19: continuous=[ENRG, HLTH, FIN] rotating=[]` (+ RE nominated, **never delivered**)
- `DEEP_LOG 2026-07-17: continuous=[FIN, HLTH] rotating=[ENRG]` (+ SEMI) · `07-15: continuous=[INDU] rotating=[FIN, IT, UTIL]` (+ SEMI)

**Selection by rule — ① continuous-track 2 = today's top-2 OW:**

- **① ENERGY** — rank-1 OW+. Held a continuous slot on 07-21 and is still top-OW today → **anti-thrash
  keeps the slot**. **Mandate narrowed to the refining node**: the money is in VLO/MPC/PSX (RS20 +25~29,
  RS60 +27~39 vs SPY, OBV accumulating), **not** in services (SLB RS60 −20.5, BKR −18.2) and **not** in
  midstream (KMI RS20 −0.1). Questions DEEP must answer: (a) is the crack-spread lead real or a
  war-premium echo that reverses with the next headline (the variable reversed twice in two sessions);
  (b) is breadth 0.00 fully explained by the `vol_surge` artifact; (c) the book carries a **🚨 0.0%
  epicenter GAP** against an 8.0% requirement on exactly this cycle.
- **② FINANCIALS** — rank-2 OW. Held a continuous slot on 07-21, still top-OW → slot kept.
  **Mandate narrowed by the flow's own dissent**: this is the only sector where **eqflow +0.357 >
  wflow +0.212** (breadth-led, 5 of the board's 11 greens) — but **the investment banks are 🔴분산**
  (GS −0.450, MS −0.333, C −0.611). The confirm lives in insurers/custody/payments (TRV, CB, STT, USB,
  PYPL). DEEP must resolve whether the steepening thesis is being expressed somewhere it was not
  written for.

**② rotating 2 — NOT TAKEN. No third OW sector exists after §2, and this stage does not pad with
Neutral/UW.** Recorded honestly: with only ENRG and FIN at OW, both of which were covered in **all**
of the last three US runs, this run is **RECENCY-STARVED** on every eligible pick. Mitigation used is
the same as 2026-07-22 KR: keep the sectors, **narrow the mandates** so the DEEP is a delta against the
prior coverage rather than a re-run of it.

**Escalated to PREMORTEM as promotable extras (not DEEP picks — both are UW/N and therefore ineligible):**
1. **HEALTH CARE — the run's largest matrix×flow divergence.** #1 flow, best breadth, moved UW→Neutral,
   and a same-day tariff the flow could not see. This is where the run is most likely to be wrong.
   Covered 07-21 (US_2) and 07-19 — so it is *also* recency-starved; a promotion must be a delta on the
   pharma-vs-managed-care split, not a re-run.
2. **INFO TECH — the run's largest breadth failure** (0/56 green, 29 red) sitting on top of tonight's
   binary. Promotable only *after* the GOOGL capex line prints; before that any tilt is a one-way bet
   into a known binary.

**Rested, with reasons:** RE (UW, flow confirms; nominated 07-19 and **never delivered** — first claim
next run) · MATR (UW, flow confirms on both axes) · UTIL (just downgraded to UW; covered 07-15/07-17) ·
INDU (downgraded to N−; covered 07-15 and as the 07-21 swing) · COMM/STPL/DISC (no OW case).

## ✅ EXIT CHECK
- [x] §1 is one line, inherited verbatim; no unchanged sector gets a row or a restated flow number.
- [x] Every §2 delta cites wflow/eqflow/breadth/Δ/green-red. Three change attempts were **declined**
      (COMM, STPL, ENRG-downgrade) and logged with the reason rather than made.
- [x] Every matrix×flow divergence named with a resolution owner: HLTH → DEEP · IT → PREMORTEM then
      DEEP · ENRG breadth → DEEP · FIN sub-node → DEEP · COMM/STPL inversions → watch.
- [x] DEEP picks made by the rule: **2 picks, NOT padded**, continuity stated, recency-starvation
      declared, mandates narrowed as the mitigation.
- [x] Linter run on this file.
- [x] DEEP_LOG line appended below.

## DEEP_LOG 2026-07-22: continuous=[ENRG, FIN] rotating=[] (2 picks — only 2 OW sectors exist after §2; NOT padded. Both kept continuous slots by the anti-thrash rule (held 07-21, still top-OW today) and both are declared RECENCY-STARVED — covered in all 3 of the last US runs — mitigated by narrowed mandates: ENRG→refining node only (VLO/MPC/PSX; services and midstream excluded on RS60 −18~−21 vs SPY), FIN→non-bank financials (GS/MS/C are 🔴분산; the confirm is in insurers/custody/payments). Deltas this run: HLTH UW→Neutral (flow #1, breadth best-on-board, but sweep predates the 07-22 pharma tariff) · IT N→UW (0 green of 56, eqflow −0.289 worst on board) · INDU N+→N− (#9 wflow, 17 red of 50; nuclear leg removed by EVENT_ALPHA Card 6 — epicenter not in us_top300) · UTIL N−→UW (Δ −0.183 worst deterioration) · DISC N−→UW (eqflow −0.103, 0 green / 8 red). Declined: COMM (one-name sector number — GOOGL pre-print) · STPL (eqflow inversion logged as watch) · ENRG downgrade on breadth 0.00 (measured as a vol_surge filter artifact: 99 of 300 names blocked by that axis alone, Energy's four being XOM/VLO/MPC/PSX). Escalated to PREMORTEM as promotable extras: HLTH #1, IT #2. RE rested again — nominated 07-19, never delivered; first claim next run.)
