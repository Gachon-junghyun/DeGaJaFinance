# SECTOR_DEEP_IT — Information Technology (UW−) · industry_US · 2026-08-23 (Sun) · Stage 8 / L1·DEEP
### ★ PREMORTEM-promoted 5th slot — **NARROW mandate, deliberately disjoint from the 08-22 IT file**

> ⚠ **Why this file is narrow.** IT was deep-dived **yesterday** on an **identical price frame**
> (`n_new_sessions_since_prior_run = 0`), so a full re-map would reprint the 08-22 file under a new
> date. PREMORTEM promoted the slot on a **question that file does not answer**, and this file answers
> only that question. The 08-22 map is carried by reference.

## 0 · ★★★ The mandate

*"Does the book's 16.52% 'AI-compute epicenter' contain **two** businesses — **sells the accelerator**
(`NVDA`, `ANET`) versus **co-designs someone else's** (`AVGO`) — and did 2026-08-19 move them apart?"*

## 1 · ★★★ `M837` — The answer is YES, and it is the rare `G4`-ROBUST result: it holds in all three windows

`scripts/risk_units.py NVDA ANET AVGO MRVL HPE MU AMD` at `--days` **250 / 500 / 750**
(residual correlation after a market factor; `dist 0.65` selected, `C5` sensitivity printed by the tool):

| Window | Measured units | `NVDA` | `AVGO` | `ANET` | `MRVL` |
|---|---|---|---|---|---|
| **250d** | **5** — `U0: AMD, MU` · `U1: HPE, MRVL` · `U2: ANET` · `U3: AVGO` · `U4: NVDA` | **singleton** | **singleton** | singleton | with `HPE` |
| **500d** | **5** — `U0: AMD, MU` · **`U1: ANET, AVGO`** · `U2: HPE` · `U3: MRVL` · `U4: NVDA` | **singleton** | **with `ANET`** | with `AVGO` | singleton |
| **750d** | **6** — **`U0: ANET, AVGO`** · `U1: AMD` · `U2: HPE` · `U3: MRVL` · `U4: MU` · `U5: NVDA` | **singleton** | **with `ANET`** | with `AVGO` | singleton |

★★★ **`NVDA` is a singleton in EVERY window. `AVGO` never groups with `NVDA` in ANY window.**
⚠ **This matters because `G4` has failed for 14 consecutive runs precisely because groupings flip with
the window.** This finding is **invariant across all three**, which makes it one of exactly two
groupings this desk can currently vouch for (the other is `MPC` + `PSX` on the book set).
⚠ **What is NOT invariant, stated plainly**: whether `AVGO` is alone (250d) or paired with `ANET`
(500d, 750d), and whether `MRVL` pairs with `HPE` (250d) or stands alone (500d, 750d). **Per `G4`,
every count above carries its `--days` on the same line as its conclusion.**

### The consequence for the book's own guard — `M838`

The book labels **`NVDA`, `ANET`, `AVGO`** with a single theme string, **`AI-compute-EPICENTER`**, and
`cycle_exposure.py` reports them as **one cycle at 16.52%** of the book.
**The measurement says that label spans 2–3 distinct risk units in every window.**
⇒ This is the **`label_split_across_units`** flag from L2·risk_model — *"market says many units, labels
say one ⇒ **the cap is too TIGHT**."* The theme cap is currently treating a genuinely 2–3-unit
position as a single concentrated one.
⚠ **P4 — this is a measurement handed to a human, not a sizing action.** No size is recommended, and
the run does not alter the label.

## 2 · ★★★ Did 2026-08-19 move them apart? — measured

| | `NVDA` | `ANET` | `AVGO` | `MRVL` |
|---|---:|---:|---:|---:|
| `flow_score` | −0.181 | **+0.417** | **−0.221** | **+0.583** |
| `obv_state` | 중립 −0.024 | **매집 +0.152** | 중립 +0.038 | **매집 +0.183** |
| rs20 vs `SPY` | +0.2 | +4.8 | **−7.2** | **+18.4** |
| **rs60 vs `SPY`** | **−1.0** | **+20.2** | **−14.7** | **+17.3** |
| `vol_surge` | 0.75 | 0.82 | 1.00 | 0.85 |
| one-session `delta` | +0.018 | **+0.384** (book's largest) | +0.176 | +0.044 |
| **FINRA short z (08-21)** | +0.41 △ | **+1.82 🔴 surge**, 5v5 **+3.9▲** | **−2.53 🟢 covering**, 5v5 −6.0▼ | — |

★★ **`AVGO` ↔ `MRVL` rs60 spread = 32.0pp. `AVGO` ↔ `ANET` rs60 spread = 34.9pp.**
⇒ **The three names the book calls one thing are 35 percentage points apart over 60 sessions.**
The 08-19 event (Alphabet dual-sourcing custom silicon to `MRVL`, with a **$12.2bn / 59m-share
warrant that does not fully vest until Google buys $120bn of chips** — `yahoo_finance` 08-20, 08-21)
sits exactly on the seam the correlation measurement finds.

⚠ **Two flow readings that cut against the obvious story, recorded because they do:**
1. **`ANET` carries the only 🔴 short-surge on the book** — FINRA z **+1.82** with the 5v5 trend
   **+3.9▲**. **New shorts arrived INTO the book's largest positive flow delta.** A rising name with
   rising short pressure is not a clean rise.
2. **`AVGO`'s shorts are COVERING into the decline** — z **−2.53**, 5v5 −6.0▼, against rs60 −14.7.
   **This is the third instance of the `M804` shape in this single run** (after `RTX` z −2.15 into a
   −0.304 delta, and `LHX` on 08-21). **Shorts covering into decline is not a bottom signal; it is
   the removal of one class of future buyer.**

## 3 · The three dated binaries inside this one sector — with their implied moves

| Name | Print | Implied move (first expiry spanning it) | ATM IV | Calendar status |
|---|---|---:|---:|---|
| `NVDA` (held) | **08-26** | **±6.11%** (08-28 straddle $13.12 / spot 214.72) | 0.606 / 0.588 | ✅ on `catalyst_calendar`, corroborated to two bodies |
| **`MRVL`** | **08-27** | **±11.31%** (08-28 straddle $26.80 / spot 237.04) | **1.122 / 1.096** — highest on the board | 🚨 **ABSENT from `catalyst_calendar`** |
| `AVGO` (held) | **09-02/03** | **±9.51%** (09-04 straddle $35.05 / spot 368.45) | 0.643 / 0.618 | on calendar as 09-02; `yfinance` says 09-03 — **one-day ambiguity, flagged not resolved** |
| *(control)* `MU` — **no print until 09-24** | — | ±6.61% (08-28) | **0.650 / 0.643** | — |

★★★ **`MU` carries a HIGHER ATM IV than `NVDA` on the identical 08-28 expiry (0.650 vs 0.606) while
having no print.** ⇒ **The options market prices the information in `NVDA`'s print as being about
MEMORY.** Registered as `S117`. **This is the sector's single most useful cross-check and it comes
from price, not narrative.**

## 4 · What this file is NOT re-deriving

The 08-22 `SECTOR_DEEP_IT.md` owns the sector's node map, the UW− justification, and the
under-computed-leg argument. **Nothing in it has changed**, because nothing in the price frame has:
`eqflow` −0.102, `exc5` −2.158 (rank 11 of 11), 🟢2 : 🔴15, participation **30.4%** (17 of 56) — all
identical. ⚠ And `SECTOR_DEEP_SEMI.md`, which covers the AI-compute epicenter proper, is **39 days
old** and is the sector's standing coverage gap.

## 5 · Track KPIs and anti-signals

| KPI / anti-signal | Current | What resolves it |
|---|---|---|
| **`AVGO` ↔ `MRVL` rs60 spread** | **32.0pp** | `S116` settles the direction on **08-28** (A ≥ +12.0pp / B ≤ −12.0pp on the 1-session spread) |
| **`NVDA` gross-margin guide** | — | `P90` (A: guided GM ≤ reported and reported ≤ +50bp vs prior; B: guided ≥ +100bp), **08-26** |
| **`MU` − `NVDA` 1-session excess** | — | `S117`, **08-27** (A ≥ +3.0pp = the information was memory) |
| `ANET` short pressure | z **+1.82**, 5v5 +3.9▲ | z above **+2.5** with rs20 turning negative would flip its EXTENDED-BUT-LIVE tag |
| Risk-unit stability | `NVDA` singleton in **3 of 3** windows | a window in which `NVDA` and `AVGO` merge would overturn `M837` |
| ⚠ Registry gap | **The custom-silicon / merchant-ASIC layer has NO row in `cycle_registry.json`** | Human fix; until then the book's 16.52% "epicenter" conflates two businesses |

## 6 · Verdict on the mandate

**Yes — the "AI-compute epicenter" label contains at least two distinct risk units, `NVDA` is separate
from `AVGO` in every measurement window, and the 08-19 Alphabet–`MRVL` event landed exactly on that
seam.** The three names the label groups are **35 percentage points apart on rs60**.
⇒ **Three consequences, all handed forward rather than acted on (P4):**
1. **The theme cap is too tight on this book** (`M838`, `label_split_across_units`) — a human call.
2. **`AVGO`'s standing thesis line still has no customer in it** (`W4`), and the customer is the
   event. `S116` is the falsifier and it settles **08-28**.
3. **`cycle_registry.json` needs a custom-silicon row**, or the desk cannot distinguish "sells the
   accelerator" from "co-designs someone else's" — which is precisely the distinction that moved.
