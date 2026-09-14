# ACTION_BRACKET — 2026-08-21  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,305,485원 · fx 1380 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** NVDA earnings (D-5, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*

---

# ADDENDUM — hand-written brackets and freshness tags (`industry_US` ALPHA, 2026-08-21)

> Appended by the ALPHA stage. **Analytical only — zero buy/sell language, no order is implied (P4).**
> Settled bar **2026-08-20**. `module_flow --positioning` and `theme_age` pulls are **`[live 08-21]`,
> US session OPEN** (this stage ran 23:5x KST = 10:5x ET) and are labelled at every use.

## 1 · 🚨 `D294` reproduces for a THIRD run, and today it cost more than usual

The script's own output, verbatim:

> **Nearest binary:** NVDA earnings (D-5, axis=earnings) — both-sides armed below.
> _No tickets — no cycle GAP and no dated binary in window._

**The header names a binary and the body says there is none, in nine lines of each other.**
`branch_map.json → axes.earnings` holds placeholder prose, `_first_clean()` rejects it, the ticket
list empties, and the empty-list message fires under a header naming the binary. **A single-name
earnings binary can never produce a ticket.**

★ **And today the defect compounds with `D18`/`D288-KR`.** The window's **D-0** binary — **Kevin
Warsh's Jackson Hole debut, TODAY** — is **absent from `catalyst_calendar` entirely**, so the bracket
tool could not have emitted a ticket for it even with a working `earnings` axis. **Two instruments
failed in series on the single most dated event of the week.**
⇒ **Everything below is hand-written, and that is the cost being recorded.**

## 2 · Ticket state, stated plainly

**`CYCLE_EXPOSURE` GAP: none** (AI-compute epicenter 19.8% vs a 12.0% floor · Energy/refining 9.78%
vs 8.0% · missile-defense 5.73% with **no floor set**). ⇒ **no epicenter-starter ticket is due**, and
that is a measured null rather than an empty file.
⚠ Two caveats travel with the null: the **optical/interconnect cycle has no registry row** (`D250`),
so "any-layer 23.57%" is a floor; and **a floor of zero cannot fail**, which makes the rank-3 ⚪ a
`D122` zero-information gate (human item, P5).

## 3 · Hand-written both-sides brackets for every binary the tool could not emit

**All four are pre-registered rows written earlier today, restated here as the bracket record.**
**Thresholds are frozen; none is set from an implied move — see §5 for why that check returned unusable.**

| Binary | Date | Row | Against-us branch | With-us branch |
|---|---|---|---|---|
| **Warsh · Jackson Hole** | **2026-08-21, D-0** | `P82` (rate) · **`S108`** (equity) | `S108` A: `EW{XLU,XLRE,XLP}` 3-session excess vs `SPY` **>= +1.68pp** by 08-25 — the three underweights rip together | `S108` B: **<= -1.76pp** |
| `NVDA` earnings | 2026-08-26, D-5 | `S79` · `S81` · `S103` | see rows | see rows |
| July PCE | 2026-08-28, D-7 | `S104` | see row | see row |
| **`FRO` earnings** | **2026-08-31, D-10** | **`S109`** | B: `FRO` 5-session excess vs `SPY` **<= -4.62pp** by 09-02 — the freight leg is NOT paid and `M45` replicates | A: **>= +8.04pp** |
| Hormuz "open" statement | **undated, 20th run** | `S74`/`S84`/`S92`/`S95` | — | — |

🚨 **`D295` — UNMET for a second consecutive run, and now it is this stage's own failure.** `S103`
(`NVDA` 08-26) carries **hand-set +/-5.0pp bands** because the readable option chain expired 08-21.
**That chain has now rolled**, so the re-derivation became possible today and **this stage did not
perform it**: the `--positioning` pulls this run all returned **D0 expiries** (see §5), i.e. the
*old* chain on its last day, not the 08-28 one. **Recorded as unmet rather than deferred silently.**
**It is the 08-22 run's first ALPHA job.**

## 4 · `BET_SHEET §B` freshness tags — issued on the HAND-PROBED path only

🚨 **`PREFLIGHT G1` FAILED (9th consecutive run): the sweep's news axis is dead at 16.72% coverage.**
The stage rule is that **ALPHA may not issue a freshness verdict when G1 fails** — so the falsification
probe was run first and it passed decisively: **the same 40 names the sweep marked silent returned
40/40 valid in 18.8 s**, and the CLI returned **3523 three times** for `Nvidia --days 7 --count
--scope foreign`, **including once before the sweep ran**. ⇒ **the pipe is alive and the sweep's loop
is the broken part.** Every tag below is issued on the **hand-probed CLI path** and on **no sweep
velocity number**, and each carries its clock time.

| Bet | Tag | Evidence (settled 08-20 unless marked) | Residual / re-check |
|---|---|---|---|
| **`MPC` (held)** | 🟡 **PARTIAL** | flow +0.700 · rs20 +11.4 · **rs60 +42.8** · OBV 매집 · `vol_surge` 1.06 · FINRA **-0.52**. `M149` share 26.6% with days 21-60 **+31.4** ⇒ EXTENDED-BUT-LIVE. ⚠ `[live 08-21]` chart: **BEARISH DIVERGENCE**, RSI 76.9 | **Residual: `P70`'s control leg FAILED (`BZ=F` 5d +7.71% vs a <=+2.0% control).** Re-check **2026-08-27** at `P83`'s settle |
| **`PSX` (held)** | 🟡 **PARTIAL, downgraded within the tag** | flow +0.733 · rs60 +36.4 · OBV 매집. 🚨 **TWO independent axes against it**: FINRA **z +1.95, 5v5 +13.5▲** and the only negative 7-day estimate revision of the three refiners (**9.56 -> 9.25, -3.2%**) | **Residual: the B-grade axis disagrees with the C-grade one (`D6`).** Re-check **2026-08-27** |
| **`VLO`** | 🔴 **RESOLVED — dropped from the bettable list** | fwd P/E 11.36 with next-year estimates **+58.4%/90d**, price at the 52-week high and **+11.0% above** the consensus mean | **Logged as a ledger row, not prose**: `reject_ledger` `H.밸류소진`, `--revives-if` written, re-check **2026-09-04** |
| **`MRK`** | 🟡 **PARTIAL** | flow **+0.894 (board #2)** · rs60 +22.8 · OBV 매집 · **`vol_surge` 1.41**. `theme_age "cancer vaccine"` **ACCELERATING 25.71x on n=103** (clears the `T24` floor). Driver dated **2026-08-19** (mRNA Phase 3) | **Residual: price is +4.8% ABOVE its consensus mean and next-year estimates are flat (+0.2%/90d, 5up/4down).** Re-check **2026-09-04** — the same date as its open `missed_ledger` row |
| **`CBRE`** | 🟡 **PARTIAL — the sheet's cleanest positive** | Sector's best flow **+0.528** · rs60 +15.4 · OBV 매집 · FINRA **1.7% float covering, DTC 2.7** · **PEG 1.02**, forward P/E 16.84, **+19.4% to the consensus mean**, price **12.3% below** its 52-week high | **Residual: next-quarter estimates -2.9%/90d (2up/6down) and beta 1.19.** Re-check **2026-09-04** |
| **`MRVL`** | 🟡 **PARTIAL** | rs20 +16.6 · rs60 +18.9 · OBV 매집 · Δ +0.161; the **named winner** of the Google custom-silicon socket `AVGO` (held) lost. ⚠ its green is **velocity-derived** (`vol_surge` 0.77) and is **not** cited as a tag | **Residual: no 4Phase exists; short 4.8% of float and BUILDING** `[live 08-21]`. Re-check at **`S105`, 2026-09-03** |
| **`NEM`** | 🟡 **PARTIAL, with an exhaustion stamp** | flow +0.628 · rs20 **+31.4** · OBV 매집. 🚨 **`M149`: 246.4% of the 60-day excess is the last 20 sessions and days 21-60 are NEGATIVE (-18.68)** | **Residual: `S89` settles TONIGHT already inside branch B, and its anti-signal is 2.1pp from firing.** Re-check **2026-08-22** |
| **`DLR`** | 🔴 **RESOLVED — dropped** | three axes, no agreement; Bollinger coiling 6.3%; `S90` inside C | **Ledger row**: `reject_ledger` `A.flow미도착`, re-check **2026-09-04** |
| **`MSTR` + `COIN`** | 🟡 **PARTIAL — one unit, not two** | both new-🟢 with OBV 매집, **but both carry NEGATIVE rs60 (-31.3 / -5.9)** and `COIN` is **crowded-short z +2.20** | **Residual: a reversal off a losing base is confirmed only when both rs60 cross zero.** Re-check **2026-09-04** |
| **`ETN` (held)** | 🟡 **PARTIAL** | flow -0.075 · OBV 매집 (sweep) vs **분배 -40%** `[live 08-21 chart]` — **neither picked**. **Joint loading beta_XLI +1.402 : beta_XLK +0.620 (60 obs, both t>5)** | **Residual: `S99` settles tonight and its branch labels do not contain the answer.** Re-check **2026-08-22** |
| **`RTX` (held)** | 🟡 **PARTIAL, downgraded within the tag** | rs60 +17.0 but rs20 **-1.8** and **Δ -0.435 = the largest single-session deterioration among the book's 11**. `M149` share **-10.6%** ⇒ 🚨 **ROLLING OVER** | **Residual: customer measurement unmet for 204 days (`W4`).** Re-check **2026-09-04** |
| **`AXON`** | ⚪ **NO TAG ISSUED — filed as a MISS, not a 🔴** | **exc60 +57.82 = the board's best**, in a sector deep-dived today, with **zero** desk artifacts | `missed_ledger` `U.발굴부재` with an `--enters-if`, re-check **2026-09-04** |
| **`ECL`** | ⚪ **NO TAG ISSUED — filed as a MISS** | the **+0.51 specialty-chemicals node** in a sector with **zero** greens | `missed_ledger` `U.발굴부재`, re-check **2026-09-04** |

★ **🟢LIVE count this run: ZERO — for the 10th consecutive US run — and the reason is arithmetic,
not the instrument, and this run can say so with a probe rather than an assumption.**
`theme_age` returned **one 🟢FRESH theme on the board** (`Treasury buybacks`, age **2**, n **135**,
7d average 19.3 — up from age 1 / n 64 yesterday). **A theme can be FRESH; a NAME-level 🟢LIVE still
requires the conjunction (age <= 14d AND accel >= 2x) to hold for the bet's own theme**, and the
themes this desk's bets ride are **>= 90 days old**: `Strait of Hormuz` **8,022 articles, 0.84x
DECELERATING** · `AI capex` 1,125, 0.67x · `crack spread` 165, 1.48x · `memory shortage` 553, 1.51x ·
`rate hike` 6,094, 0.97x. ⇒ **`R83`'s rewritten mechanism is confirmed for a second run: the readout
is not capped, the conjunction is unmet, and a desk trading multi-quarter industrial cycles will keep
reading zero.** ⚠ **`refinery outage` (n=27) is below the `T24` floor and its 0.58x is NOT quoted as
a reading** — it is used only as a reachability check on `P83`'s anti-signal.

★★ **And the one theme that IS fresh points at a macro row, not a name**: `Treasury buybacks` 🟢FRESH
is the object of `P77` (settles 08-26) and half the object of `P81` (08-28). **The freshest thing on
this desk's board is not something it can own — it is something it must bracket**, and both brackets
exist.

## 5 · The implied-move check was performed and returned UNUSABLE — stated, not skipped

`module_flow --positioning`, `[live 08-21]`, nine names:

| Name | short % float | trend | DTC | P/C | IV skew | implied move | expiry |
|---|---:|---|---:|---:|---:|---|---|
| `MPC` | 2.8% | covering | 3.4 | 1.10 | **+64.6** | +/-1.8% | **2026-08-21, D0** |
| `PSX` | 2.1% | covering | 2.9 | **1.73** | +43.1 | +/-2.1% | **D0** |
| `MRVL` | **4.8%** | **building** | 1.4 | 1.39 | +14.6 | +/-3.2% | **D0** |
| `CBRE` | 1.7% | covering | 2.7 | **0.31** | +12.3 | +/-1.3% | **D0** |
| `MRK` | 1.1% | covering | 3.2 | 0.69 | +36.5 | +/-1.6% | **D0** |
| `HPE` | 5.6% | covering | 3.7 | 0.84 | -3.4 | +/-2.7% | **D0** |
| `DELL` | 4.4% | building | 2.0 | 0.74 | **+40.1** | +/-1.8% | **D0** |
| `FRO` | **6.1%** | **building** | **4.1** | 0.56 | +18.5 | +/-3.1% | **D0** |
| `NEM` | 2.0% | covering | 2.5 | 0.65 | +27.6 | +/-2.0% | **D0** |

🚨 **All nine straddles expire 2026-08-21 = D0.** They price today's session and **cover none of the
events bracketed in §3** (`FRO`'s print is 08-31; `S110` settles 09-03; `NVDA` prints 08-26).
⇒ **Taking a threshold from them would fabricate one — the `M47` defect by name.** Every threshold
registered today is `D93` distribution-based, and **this table is reported for its POSITIONING columns
only** (short interest, DTC, P/C, skew), never for its implied move.
★ **What the positioning columns do say, and it is usable**: `FRO` **6.1% of float and BUILDING at
DTC 4.1** is the reason `S109` has two reachable branches; `MPC`'s **IV skew +64.6** and `PSX`'s
**P/C 1.73** are the highest downside-fear readings on the sheet **on the two names the desk holds**;
and `CBRE`'s **P/C 0.31 with 1.7% float covering** is the most complacent reading — **which is a
caution on the sheet's cleanest positive, not a confirmation of it.**

## 6 · Two obligations recorded as UNMET

1. **`D295`** — `S103`'s `NVDA` bands are still hand-set (+/-5.0pp). The chain has rolled and the
   re-derivation was possible today. **Not done. Second consecutive run. It is the 08-22 ALPHA's
   first job.**
2. **Targeted live WebSearch per bet** — the stage calls for a per-bet "has the catalyst already
   fired / is this street consensus" check via live search. **This run substituted the news corpus
   (`fts` + `theme_age` + the 4,991-article `brief`) and did NOT run live web search.** For `MRK` and
   the refiners the corpus is same-day and adequate; **for `CBRE` and `AXON`, both of which have no
   thread at all, the substitution is weaker and is named as such.**
