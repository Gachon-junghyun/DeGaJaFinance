# SECTOR_DEEP_FIN — Financials · industry_US · 2026-09-08 (Tue) · Stage 8 / L1·DEEP

> **ROTATING TRACK — PREMORTEM-PROMOTED (Lens 1) ⇒ FULL FRESH MAP.** Last DEEP **2026-08-30 = 6 runs
> ago**, the 2nd-longest recency gap on the board.
> Price numbers filtered to `index <= 2026-09-04` (`D577`). Benchmark `SPY` named inline (`C1`).

## 0 · Mandate — one question

*"Three dated binaries land on this sector inside eight sessions (PPI 09-10 · CPI 09-11 · FOMC+SEP
09-16) and its own bracket **`P128` is BLOCKED by `D427` for a sixth run**, so nothing else will
resolve it. **Resolve the curve leg on something that actually settles.**"*

## ★ 1 · The answer to the mandate — and it is a construction answer, not a market answer

**`P128` cannot be settled and probably will not be.** It reads `hy_oas` `[FRED]` at *"the first
`[FRED]` close covering 2026-09-08"*, and this run **proved at the FRED REST API, module bypassed**,
that `BAMLH0A0HYM2` stops at **2026-09-03** while `T10YIE` carries **09-04** (`M1455`). The desk's
model of when that unblocks was **retracted today** (`R147`) — the block predates the Labor Day
holiday it was blamed on and survived the first post-holiday business morning.

⇒ **The mandate is discharged by registering a settleable object instead**: **`P148`** (PREMORTEM),
`IEF` − `SHY` **2-session excess** over **09-15 → 09-17**, i.e. **the curve SLOPE across the FOMC**,
deliberately **ETF-based so `D427` cannot block it**. Thresholds **A ≤ −0.3469% / B ≥ +0.2856%**
(trailing-252 p15/p85), registration state **54.0th percentile**. ★ **Branch B — a dovish steepening —
falsifies `RE`+`STPL`+`UTIL` at once and would put `FIN` on the other side of the same trade.**

## 2 · Flow — the sector splits, and the split is NOT banks-vs-non-banks

| sub-node | n | eqflow | exc5 median | 🟢 | note |
|---|--:|--:|--:|--:|---|
| **Financial Exchanges & Data** | 7 | ★ **+0.338** | −0.77 | 0 | flow-positive, **price-negative** |
| Asset Mgmt & Custody | 7 | +0.152 | −0.98 | 0 | same shape |
| **Diversified Banks** | 7 | +0.032 | ★ **+1.33** | 0 | **flow-flat, price-positive — the inverse** |
| Insurance Brokers | 3 | +0.019 | 🔻 **−3.69** | 0 | `AON` −0.299 / `exc5` **−9.20** carries it |
| Investment Banking & Brokerage | 5 | +0.002 | +0.34 | 1 (`HOOD`) | |
| Life & Health Insurance | 3 | −0.147 | +1.04 | 0 | |
| Transaction & Payment Processing | 4 | −0.199 | −1.45 | 0 | |
| **Regional Banks** | **2** | −0.299 | +0.52 | 0 | 🚨 **n=2 — see §3** |
| **Property & Casualty Insurance** | 5 | 🔻 **−0.323** | −0.24 | 0 | **5 of 5 are 🔴 분산** |
| Consumer Finance | 2 | −0.354 | −0.25 | 0 | |
| Multi-Sector Holdings | 1 | −0.469 | +0.09 | 0 | `BRK-B`, the sector's `top1` |

★★ **The two largest sub-nodes read in opposite directions on the two axes.** Exchanges/Data is the
**most flow-positive** node and the **most price-negative** of the top three; Diversified Banks is
**flow-flat** and the **most price-positive**. ⇒ *"Financials is flat"* (`eqflow` −0.023, the flattest
reading on the board) is **an average of two opposite things**, which is exactly what a sector-level
verdict should not be built on.

★ **Dispersion / sector-move = 3.420 / 0.067 = 50.9×** — **by far the worst on the board** (`D566`
measured UTIL ≈23×, HLTH 5.72×, IT 4.6×, ENRG 0.92×). The sector mean is near zero *because* the
names cancel, not because they agree. ⇒ **`FIN N` is arithmetically correct and analytically empty**,
and this file states that rather than converting it into a verdict.

**Insurance is the one clean node-level fact**: P&C `eqflow` **−0.323** with **5 of 5 names 🔴 분산**
(`CB` −0.291 · `ALL` −0.512 · `HIG` −0.514 · `TRV` −0.579 · `PGR` +0.282 is the only non-🔴 and it is
🟡). A node where every name agrees is a node a verdict can attach to; the sector is not.

## 3 · 🚨 A coverage defect this sector exposes, and it is not `D563`'s

**`us_top300.csv` contains exactly TWO Regional Banks — `HBAN` and `FITB`.** The regional-bank complex
is the part of Financials that a curve/deposit-beta story moves first, and the desk's universe reduces
it to a two-name sub-node with `eqflow` −0.299 built from `HBAN` +0.042 and `FITB` −0.640 — **a 0.68
spread across the entire node.**
⇒ **Any "regional banks are X" statement from this desk is a statement about two companies.** This is
the sector face of the same defect `D563` found in energy (`LNG`/`GLNG`/`FLNG` absent) and `P127`
(`TLN`/`NRG` absent): **a top-300-by-cap universe is a large-cap universe, and cap-rank is not the
same as economic coverage.** Registered as **`D579`**'s sibling observation — see §7.

## 4 · Money — `[FINRA]` short-volume z, settled 2026-09-04

| name | short% | base20 | z | 5v5 | read |
|---|--:|--:|--:|--:|---|
| **SPGI** | **82.2%** | 54.3% | 🔴 **+3.00** | **+17.9▲** | ★ **the board's most extreme short-pressure reading this run** — and `SPGI` is the sector's #2 flow name (+0.711) with `exc5` **+0.03 = flat**. Flow says accumulation, the short tape says the opposite, and the price says nothing |
| FITB | 74.1% | 57.6% | +1.39 | +2.4▲ | pressure building on the worse of the two regionals |
| WFC | 42.0% | 35.6% | +0.68 | **+11.9▲** | the fastest-building pressure among the money-centres |
| JPM | 39.7% | 47.9% | 🟢 **−1.21** | −2.2▼ | shorts leaving the largest name |
| BAC · GS · C · HOOD · COIN · HBAN | | | −0.86 · −0.08 · −0.28 · −0.64 · +0.42 · +0.26 | | all 🟡 normal |

⚠ **`SPGI` is the sector's sharpest single-name disagreement and it is left unresolved on purpose.**
Flow +0.711 / OBV 매집 / surge 1.08 against a **z +3.00 with the trend still building**. `D6` grades
OBV **C**; `[FINRA]` short-volume is a **proxy, not an investor-type feed** (the US has none). Two
weak instruments disagreeing is not a finding — it is a **named open question**, and it goes to the
watchlist, not to BET.

## 5 · The macro leg, cited on instruments rather than narrative

| instrument | last | value | read |
|---|---|--:|---|
| `hy_oas` | `[FRED]` 09-03 | **2.65%** | near its 1-year low; **5-session change +2 bp = mid-pack** |
| `ig_oas` | `[FRED]` 09-03 | **0.81%** | +2 bp / 5 sessions |
| `nfci` | `[FRED]` 08-28 | **−0.558** | **six consecutive weekly readings easing** (−0.538 → −0.558) |
| `DGS10` / `DFII10` / `T10YIE` | 09-03 / 09-03 / **09-04** | 4.77 / 2.42 / **2.35** | 5-session move **+0.08 REAL vs +0.04 breakeven** |

⇒ **The curve is selling off on the REAL leg while credit and financial conditions ease.** For banks
that is the *favourable* combination (steeper nominal curve, no credit deterioration) — and it is
**precisely the argument ROTATION declined three runs running as a macro re-argument.** This file does
not overturn that decline; it **converts the argument into `P148`'s branch A/B**, which is the
disposition the rule actually asks for.

⚠ `D3` throughout: the `hy_oas` **level** (2.65, near a 1-year low) and its **change** (+2 bp,
mid-pack) are different objects. `P128` was written on the **change**.

## 6 · Track KPIs and anti-signals

| | observable | current |
|---|---|---|
| **KPI 1** | `IEF` − `SHY` 2-session excess (the `P148` observable) | **+0.0147% = 54.0th pctile** |
| **KPI 2** | Diversified-Banks `exc5` median vs Exchanges/Data `exc5` median | **+1.33 vs −0.77** — the split; under a curve-driven read it widens |
| **KPI 3** | `hy_oas` 5-session change | **+2 bp** — the `P128` observable, currently unreadable |
| **ANTI-SIGNAL 1** | `hy_oas` **≥ 3.10% on a close** ⇒ it is a credit event, not a rate event, and every rate attribution above is void (the clause `S19`/`S41`/`S46` all used) | 2.65% |
| **ANTI-SIGNAL 2** | P&C insurance ceasing to be 5-of-5 🔴 ⇒ the one node-level fact in this file dissolves | 5 of 5 🔴 |
| **ANTI-SIGNAL 3** | an unscheduled Fed action or a US bank failure inside 09-15 → 09-17 ⇒ `P148` VOID | not observed |

## 7 · Findings this file hands upward

1. **`FIN`'s dispersion/sector-move is 50.9× — the board's worst.** The `N` verdict is arithmetically
   right and analytically empty; the sub-nodes, not the sector, are the unit of analysis (`D566`,
   now with a second and much larger instance).
2. 🚨 **`us_top300.csv` holds two Regional Banks.** A universe built on cap rank is not economic
   coverage, and this is the **third distinct place** the same defect has bitten this run
   (gas/LNG absent · `TLN`/`NRG` absent from a live bracket's basket · regional banks reduced to n=2).
   ⇒ registered as **`D579`** — *"state a sub-node's `n` on every sub-node claim; a two-name node is
   two companies, not an industry."*
3. **`SPGI`**: an unresolved two-instrument disagreement (flow +0.711 / OBV 매집 vs `[FINRA]` z
   **+3.00** and building) — **named, not averaged**, and routed to the watchlist. **RULE D6 exempt** — the OBV reading is cited *as one side of a disagreement that is explicitly left unresolved*; nothing rests on it, which is the opposite of an OBV-carried proposition.
4. **`P128`'s successor exists**: `P148` settles the curve question on ETFs, immune to `D427`.

> **No verdict change** (ROTATION holds `FIN N`), **no sizing**, **no buy/sell language** (`P4`).
> ⚠ Written serially and in-context, not as a parallel agent fan-out — declared.
