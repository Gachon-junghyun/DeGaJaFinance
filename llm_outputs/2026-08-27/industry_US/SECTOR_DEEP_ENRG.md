# SECTOR_DEEP_ENRG — Energy · industry_US · 2026-08-27 · **CONTINUOUS TRACK (8th consecutive run) ⇒ DELTA-LED**

> Structure carried by reference to `llm_outputs/2026-08-26/industry_US/SECTOR_DEEP_ENRG.md`.
> This file leads with what changed. Price frame = **equal-weight `us_top300` constituents, excess vs
> `SPY` (named inline), settled closes through 2026-08-26.** Flow = this run's sweep, **asof 2026-08-27,
> a pre-market stub bar** (median volume 4.65% of the prior session) ⇒ **`vol_surge` and the 🟢/🔴 tag
> are not used to carry any claim.** 🚫 G1 FAIL: no freshness/velocity citation.

---

## §0 · ROTATION's mandate, answered in one line

**Mandate**: *Energy's `eqflow` is rank 2 of 11 while its breadth is 0.00 with 0 🟢; and `exc1` is the
best of 11 while `exc5` is the worst of 11. Which is the sector?*

**Answer: neither — the sector label is the wrong unit, and the dispersion proves it.**
**`exc60` runs from +36.43 (Refining & Marketing) to −2.81 (Equipment & Services) — a 39.2pp spread
across five sub-industries, against a sector `exc60` of +10.10.** The dispersion is **~4× the sector
move**. ⇒ **this file states plainly that "Energy" is not the unit of analysis; refining is.**

---

## §1 · The delta since 08-26

### 1a · 🚨 The kill counter RESET for a third time — and this run cannot tell you whether that is real

The registered refiner kill is *"two consecutive negative 5-session crack-rate readings."* Settled
3-2-1 crack 5-session rates, most recent last:

`[+2.355, +0.413, +2.893, −2.862, −1.675, **+2.728**]`

- The 08-26 run recorded the kill as **FIRED** on `−2.862 → −1.675`.
- **The 08-26 settled bar prints +2.728 — the 71.8th percentile of the trailing 252 — and the counter
  resets.** Trailing-252: mean **+0.785**, sd **4.563**, p15 **−2.887**, p50 **+0.463**.
- ⇒ **The kill has now fired and reset twice inside six sessions.** `P80` recorded the first reset on
  08-20; this is the second. **A regime marker whose unconditional base rate is 36.1% and which resets
  within one session of firing is not a usable trigger**, and this file says so for the second time.

### 1b · 🚨🚨 The commodity series is contaminated by a contract roll, ON the night two rows settle on it

**`M981`** (registered at MACRO §C-3, reproduced here because it lands on this sector):

| | 08-25 | 08-26 settled | **08-27 LIVE** | 1-session Δ |
|---|---|---|---|---|
| `CL=F` | 82.36 | 82.23 | 82.49 | **+0.32%** |
| `HO=F` | 4.2438 | 4.2600 | 4.0910 | −3.97% |
| `RB=F` | 3.2529 | 3.3201 | 2.9591 | **−10.87%** |

**Gasoline −10.87% on a day crude is +0.32%.** Leg decomposition of the crack's −12.701 one-session
move: **`RB=F` −10.069 (79.3%)** · `HO=F` −2.342 (18.4%) · **`CL=F` −0.290 (2.3%)**.

**What it does to the two rows settling at tonight's close:**
- **`P96`** (crack 5-session rate; A ≤ −2.887, B ≥ +0.468): **as printed −8.584 = deep inside A**;
  **with `RB=F` held flat at its 08-26 level, +1.485 = inside B.** **The roll alone moves the row
  across the entire C band.**
- **`P83`** ((`HO−RB`)×42 change from the 08-20 settle of 51.131; A ≥ +4.0, B ≤ −4.0): settled 08-26
  **−11.655 = deep inside B**; LIVE 08-27 **−3.578 = C**; with `RB=F` flat, **−18.682 = B**.

🚨 **The roll pushes `P96` toward A ("the margin collapse deepens") and `P83` out of B ("no
capacity-destruction verdict") — opposite directions, one contract change.** Neither row's anti-signal
contains a roll clause. **`P103` (registered this run, settles 09-02) is the roll-free re-read**, by
which date the 08-27 bar is four sessions behind and outside the 5-session window.

### 1c · What the equity did instead — and it disagrees with the commodity
Energy `exc1` **+1.109 = the best single session of the eleven sectors**, on the day the barrel fell
on the Hormuz deal. `exc5` **−1.040 = the worst of eleven.** ⇒ **the tape bought the sector on the day
de-escalation priced.** That is the opposite of a war-premium leg.

---

## §2 · Value chain — five nodes, left → right, with the binding constraint marked

| # | node | n | mcap | `exc1` | `exc5` | `exc20` | `exc60` | `eqflow` | reading |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Oil & Gas E&P** (upstream) | 5 | $352B | −0.45 | −2.12 | −0.98 | +3.01 | −0.144 | **4 of 5 negative on 5d.** The barrel is being sold |
| 2 | **Integrated** (`XOM`, `CVX`) | 2 | $917B | −0.70 | **−2.96** | −2.38 | +5.82 | −0.225 | The sector's `top1` node, and **the weakest on 5d** |
| 3 | **Equipment & Services** (`SLB`, `BKR`) | 2 | $130B | +0.41 | −1.49 | +2.51 | **−2.81** | +0.073 | The only node negative on 60d — capex is not following the price |
| 4 | **Storage & Transportation** (midstream) | 4 | $269B | **+3.51** | +0.19 | +0.77 | +7.81 | +0.071 | **Best single session by a wide margin** — a volume/fee node, not a price node |
| 5 | 🚨 **Refining & Marketing** — **THE BINDING CONSTRAINT** | 3 | $208B | +2.17 | +0.69 | **+11.64** | **+36.43** | **+0.474** | **Zero negative on 5d. Best node on every window ≥20d.** `eqflow` is 2.1× the next node |

**Why refining is the binding constraint and not merely the strongest demand**: the sector's 39.2pp
`exc60` dispersion is almost entirely this node vs the rest, and **the node with the highest 60-day
excess is the node with the lowest capital intensity growth** — Equipment & Services (`exc60` −2.81) is
the node that would move if the answer were *drilling more barrels*. **The market is paying for
throughput capacity, which is the scarce asset, not for reserves.**

**Cross-sector chain marked**: refining margin → **distillate → freight/airlines cost**. The 08-26 head
layer carries *"Soaring Diesel Prices Are Helping Oil Companies and Hurting Consumers"* [6 outlets],
and the airlines sit in **INDU** at `exc20` **−8.78** with `UAL` −8.86 and `DAL` −8.70. **The same
margin appears as a cost on the other side of the board, and it is visible in both places.**

---

## §3 · The three refiners, on the denominator — and `L2` fires hard

| | `MPC` (held) | `PSX` (held) | `VLO` (not held; rejection ledger `H.밸류소진`, recheck 09-04) |
|---|---|---|---|
| `exc60` vs `SPY` | **+39.06** | +33.40 | +36.83 |
| `exc20` | +12.33 | +12.11 | +10.48 |
| OBV | +0.289 매집 | +0.151 매집 | +0.148 매집 |
| `RS20` / `RS60` | +12.3 / +37.3 | +11.7 / +31.8 | +8.8 / +34.5 |

### 🚨 `MPC` read on its denominator — **the peak-margin / low-multiple trap in its purest form on this board**

| metric | value | reading |
|---|---|---|
| Forward P/E | **11.30** | looks cheap |
| Trailing P/E | 12.61 | |
| **Current-quarter EPS, 90-day change** | **+127.0%** (8.59 → 19.49) | |
| **Next-quarter, 90d** | **+91.0%** | |
| **Current-year, 90d** | **+81.9%** (27.61 → 50.23) | |
| **Next-year, 90d** | **+44.4%** (22.31 → 32.20) | |
| 🚨 **Next-year EPS vs current-year** | **32.20 vs 50.23 = −35.9%** | **consensus itself models the cliff** |
| Analyst mean target | **$324.56 vs a price implying −10.8%** | **the mean target is BELOW the price** |
| Ratings (30d) | 4 Strong Buy · 6 Buy · **8 Hold · 1 Sell** | the sell side is not chasing |

⇒ **The 11.30× forward multiple is not cheapness. It is a denominator that consensus has raised 82% in
90 days and already expects to fall 36% next year.** `L2` fires, and it fires with the sell side
agreeing: **the mean price target sits 10.8% below the market price**, which is rare and is the
cleanest single number in this file.
⚠ **Stated with its rule**: this is `L2` plus an estimate-revision table. The revision table is used
**only as a description of where the denominator has been going** — **not** as a leading indicator
(measured 2026-08-09: the effect is an IT loading; ex-IT the Q5−Q1 spread is −1.1pp). `MPC` is not an
IT name, so the confound does not apply, but the axis still carries **no independent predictive
weight** and is not used as one here.

### 🚨 The contract-terms check `L2` requires — **run, and the answer is `unknown` (C3)**

Before asserting *"this margin must mean-revert"*, the rule requires naming the contract terms read
**from the filing**. **Run: `module_disclosure_us MPC --days 60`.** Result: **11 filings — 4 Form 144,
4 Form 4, 2 8-K, 1 10-Q — and the categorised sections for `수주/계약/M&A`, `실적 발표 (Item 2.02)`,
`가이던스/IR (Item 7.01)` and `증자/채무` are ALL EMPTY.** ⇒ **no contract-term disclosure was filed in
the window**, and the 10-Q body was not parsed for pricing terms this run.

⇒ **The contracted share of `MPC`'s throughput is `unknown`, and it is marked `unknown`, not assumed.**
🚫 **Therefore this file does NOT assert that the refining margin must mean-revert.** What it asserts
is narrower and fully supported: **consensus has already modelled a −35.9% next-year decline and the
mean target sits below the price.** That is a statement about expectations, which are measured, rather
than about physics, which is not.
★ **And the frame-transfer question is answered explicitly**: the desk trusts **take-or-pay floors with
contractual ceilings** as a frame — it is the frame that overturned an `L2` call on `MU` in August,
where the 10-Q disclosed binding multi-year volumes with a floor and a ceiling. **Does it apply here?
CHECKED — and the answer is that it CANNOT be checked from the 60-day filing window**, because refining
margin is a **spot spread between two exchange-traded commodities**, not a bilateral contract. There is
no counterparty to write a floor. ⇒ **"Checked, structurally does not apply"** — which is a pass under
the rule, and it also means `MU`'s escape hatch is not available to the refiners.

### The node's customers, named, with their disclosed cost
**Refining's customers are the freight and passenger-transport complex.** Named and read:
**`UAL` (`exc20` −8.86, `RS20` −11.3), `DAL` (−8.70, `RS20` −10.5), `FDX` (`exc20` +3.85), `UPS`
(−3.98), `ODFL` (`exc20` −15.51 — the worst single name in INDU on 20 days).** ⇒ **four of the five
named customers are negative on the 20-day window while the refiners are +10 to +12.**
**This is the margin appearing as a cost, measured on both sides of the same board**, and it is the
strongest corroboration in this file that the refining spread is real economics rather than a quote
artifact — **it is visible in equities that never touch `RB=F`.**
⚠ Print dates for the unread half: `FRO` **08-28** (`S109` armed; outside `us_top300`, `D341`).

---

## §4 · The QoQ rate-of-change series `B1` requires (commodity node)

3-2-1 crack, **settled** closes, 5-session rate — the rate, not the level:

| window ending | rate | percentile of trailing 252 |
|---|---|---|
| ~08-18 | +2.355 | — |
| ~08-19 | +0.413 | — |
| ~08-20 | +2.893 | — |
| 08-24 | **−2.862** | 15.5th |
| 08-25 | **−1.675** | — |
| **08-26** | **+2.728** | **71.8th** |

**Level vs rate, stated as the rule demands**: the crack **level** is **70.373** on the 08-26 settled
close — historically elevated — while the **rate** has crossed zero three times in six sessions.
⇒ **The level says "wide margin"; the rate says "no trend".** `B1` says the rate is the signal, and the
rate currently carries **no** signal — it is oscillating inside ±1σ of its own mean.
🚨 **And before reading this rate as demand**: **the 08-27 bar's rate is 79.3% a `RB=F` contract roll**
(§1b). **A contractual/mechanical ceiling is not producing this — a contract ROLL is**, which is the
same class of question and it is answered: **the rate series is unreadable across 08-26 → 08-27.**

---

## §5 · Chain-hop candidates
🚫 **No `chain-hop` pass was run this run** (carried gap, 2nd consecutive run; the 08-26 run logged the
same). **No body-proximate candidate is therefore proposed**, and none is invented from a headline
co-mention. Stated as a gap, not filled.

---

## §6 · Track KPIs and anti-signals (observables)

| KPI | current | anti-signal — what kills the thesis |
|---|---|---|
| 3-2-1 crack **5-session rate on settled closes** | **+2.728 (71.8th %ile)** | **`P103` branch B at the 09-02 close (≥ +0.468)** ⇒ the whole 08-27 signal was a contract roll |
| Refiner OBV state (3 of 3 매집) | `MPC` +0.289 · `PSX` +0.151 · `VLO` +0.148 | any two of three leaving 매집 on a **settled** bar |
| `MPC` next-year consensus EPS | **32.20 vs 50.23 current-year (−35.9%)** | the next-year figure being revised **down further** while the price holds ⇒ the multiple is re-rating, not the earnings |
| `MPC` mean analyst target vs price | **−10.8% (target below price)** | the target rising above the price ⇒ the sell side capitulates and the trap closes |
| Node dispersion (`exc60` refining − E&S) | **+39.24pp** | compression below ~15pp ⇒ "Energy" becomes a usable unit again and the node call loses its edge |
| Customer-side cost | `UAL` −8.86 / `DAL` −8.70 / `ODFL` −15.51 on `exc20` | these turning **positive** while the crack stays wide ⇒ the cost is being passed through and the margin is no longer scarce |
| Hormuz / sanctions | Hormuz-deal thread **ENDED at its peak (13 outlets)**; tanker-threat thread **REIGNITED (5→3)** | a **dated** reopening statement, or the tanker thread reaching the head layer |

---

## §7 · Resolution verdict on ROTATION's flagged divergence

**Divergence**: `eqflow` rank 2 vs breadth 0.00 / 0 🟢; `exc1` best of 11 vs `exc5` worst of 11.
**Verdict**: 🚨 **BOTH READINGS ARE ARTEFACTS OF AGGREGATION AND THE SECTOR VERDICT SHOULD NOT MOVE ON
EITHER.** The positive `eqflow` and the best-of-board `exc1` come from **midstream (+3.51 `exc1`) and
refining**; the negative `exc5` comes from **integrated (−2.96) and E&P (−2.12)**, which together are
**$1.27tn of the sector's $1.88tn**. ⇒ **`ENRG` is held at `OW` on the refining node alone**, and this
file records that **the OW is a node call wearing a sector label** — a distinction the standing verdict
does not currently carry and should.
⚠ **And the flipper bar applies**: `XOM` at **30.5%** of the bucket makes `wflow −0.091` unusable by
rule; the node table above is equal-weight throughout and therefore admissible.

---

## §8 · Sub-sector dispersion — and the sector label is the wrong unit

**`exc60` range across 5 nodes: +36.43 (Refining) to −2.81 (Equipment & Services) = 39.24pp**, against
a **sector `exc60` of +10.10.** **The dispersion is 3.9× the sector move.**
⇒ ★ **This file states explicitly: for Energy, the GICS sector is the wrong unit of analysis.** Every
downstream reader should carry **"refining"**, not **"Energy"**. The three refiners are 11.1% of the
sector's market cap and produce essentially all of its excess return.

> *(RULE C1 — the benchmark is named: every `exc*` figure in this file is an **equal-weight `us_top300` constituent basket's excess return versus `SPY`**, on settled closes through 2026-08-26, as stated in this file's header and at §2's table head. The dispersion figure is a spread between two such `SPY`-benchmarked numbers.)*


## §9 · What this file did NOT do
- **No 10-Q body parse** for pricing terms; the contracted share is `unknown` (C3), stated above.
- **No `chain-hop` pass** (§5).
- **No `module_industry_map` call** — its corpus is Korean and English seeds return 0 by design.
- **No lead/lag claim is made anywhere in this file**, so none is inherited as fact. The one
  relationship asserted (refining margin ↔ transport cost) is a **contemporaneous cross-section**
  measured this run on the 08-26 settled frame, not a lead/lag.
