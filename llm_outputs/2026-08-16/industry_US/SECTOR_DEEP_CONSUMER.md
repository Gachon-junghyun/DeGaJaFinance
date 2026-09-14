# SECTOR_DEEP_CONSUMER — industry_US · 2026-08-16 · **5th slot, PREMORTEM-PROMOTED**

> ★ **Not a ROTATION pick.** PREMORTEM Lens 1 promoted this over ROTATION's own decline, and the L1
> requires the promoted leg to get a DEEP rather than a note. Object = **DISC ∪ STPL as ONE unit**,
> because the split that matters crosses both labels.
> Benchmark **`SPY`** named inline (C1). Settled **2026-08-14**. No sizing (P4).

## §1 · Why this leg was promoted, and what ROTATION's decline got wrong

ROTATION held DISC at N− because **Δ is +0.038, positive** — a demote needs a negative delta.
⚠ **But Δ is a FROZEN number this run**: zero sessions settled, so Δ is byte-identical to the one that
blocked the demote yesterday. *"The delta blocks it"* is, today, **a statement about the calendar**.
Meanwhile:
1. **Three dated prints land inside five sessions** — `HD` ~08-19, `WMT` ~08-20, `TGT` ~08-20 — and
   🚨 **`catalyst_calendar --days 5` carried ZERO of them** (`[EARNINGS] (none in window)`).
2. **`WMT`'s straddle is genuinely event-priced**: implied **±5.0%, expiry 2026-08-21 (D5)** — it
   **covers** its print. Contrast `NVDA`, whose ±1.5% straddle expires **nine days before** its event
   (`M47`, PREMORTEM §6).
3. **`STPL` is the board's longest-uncovered sector (08-10 = 6 runs)** and ROTATION declined it a slot
   on the grounds that its mandate was empty. **This file is the counter-argument.**
4. A dated macro driver already printed: *"US retail sales post first decline in nine months in July"*
   [`yahoo_finance` 08-14] and *"'Nobody escaped': Walmart, Bank of America, TransUnion raise major red
   flag over US consumers"* [08-14].

## §2 · ★★★ The finding — the GICS labels are the wrong object, measurably, in BOTH directions

Settled closes, excess vs **`SPY`**, `yfinance auto_adjust=False`:

| Name | GICS label | exc5 | exc20 | exc60 | Flow `asof 08-14` |
|---|---|---|---|---|---|
| **`ABNB`** | Consumer **Discretionary** | +2.966 | **+21.639** | **+34.525** | **🟢가속** · OBV 매집 · surge **1.55** · FINRA **clean-rise z −0.94** |
| **`TGT`** | Consumer **Staples** | **+2.795** | **+6.213** | **+15.601** | 🟡 · **OBV 매집** · RS20 +6.2 |
| `WMT` | Consumer **Staples** | +2.659 | −3.545 | **−19.913** | 🟡 · OBV **중립** · RS60 −19.9 |
| `AMZN` | Consumer **Discretionary** | **−4.708** | +1.791 | −4.531 | 🟡 · OBV **분산** · 40.2% of `XLY` cap |
| `COST` | Consumer **Staples** | +1.003 | −2.296 | **−17.981** | **🔴분산** · OBV 분산 |
| **`HD`** | Consumer **Discretionary** | **−5.111** | −4.449 | +6.235 | **🔴분산** · OBV 분산 |
| `XLY` (the DISC ETF) | — | **−1.783** *(worst of eleven)* | −2.056 | −3.052 | — |
| `XLP` (the STPL ETF) | — | +0.741 | −3.390 | −5.807 | — |

**`W5` fires on BOTH labels at once, which is the promotion's whole justification:**
- **Inside Staples**: `TGT` (**+6.213 exc20 / +15.601 exc60 vs `SPY`** — the A-grade price axis — with
  the C-grade OBV 매집 quoted beside it per **RULE D6**, never alone) against `COST` (**−2.296 /
  −17.981 vs `SPY`**, OBV 분산) — a **35.6pp** spread on 60 days between two mass retailers in one label.
- **Inside Discretionary**: `ABNB` (**+34.525** on 60 days, the best in the exposure set) against `HD`
  (**🔴분산**, exc5 **−5.111**, the worst 5-day in the complex) — a **28.3pp** 60-day spread.
- ⚠ **And the labels do not even sort the split**: the two accumulating names (`TGT`, `ABNB`) sit in
  **different** labels, as do the two dispersing ones (`COST`, `HD`).

⇒ **The real axis is not goods-vs-services and not staples-vs-discretionary.** On this data it is
**"names taking share / with a fresh operating story" vs "incumbents"**, and neither GICS label
expresses it. **A sector-level verdict on DISC or STPL is measuring the wrong object.** This is exactly
what **`S93`** was registered to settle (PREMORTEM §5).

## §3 · The macro driver, with both halves (C2)

- **08-14** *"US retail sales post first decline in nine months in July"* — the **sequential** half.
- ⚠ **The other half was NOT found in the corpus**: no YoY figure and no control-group (ex-auto,
  ex-gas) breakdown appears in any body this run pulled. ⇒ **The print is quoted as a
  first-decline-in-nine-months event and NOT as a level claim** (C2 satisfied by declaring the gap,
  not by inventing the number).
- **Counter-evidence on the same axis, and it is not buried**: `recession` term velocity **1.07×** and
  `layoffs` **0.83×** — **neither is elevated**, and both sit inside a 7-day window contaminated by the
  weekend collapse (736 → 269 → 112 events). ⇒ **There is no narrative surge behind the consumer
  story.** The print is dated; the narrative is not accelerating.
- ★ **A second, cross-sector driver the desk had not connected**: *"Trump asks Americans to accept
  **high pump prices** as Iran standoff drags on"* [`seekingalpha` 08-15]. The ENRG DEEP's chain ends at
  the **pump-price node**, and that node is this sector's input cost. **The desk's #1 OW (Energy) and
  its consumer read are the same trade viewed from two ends of one chain** — if the refining thesis is
  right, the consumer squeeze is its consequence.

## §4 · Value chain — 7 nodes, bottleneck marked

`Household real income (wages − CPI − pump price)` → **`🔴 DISCRETIONARY WALLET SHARE — the binding constraint`** →
`Trip / experience spend (ABNB)` ∥ `Big-ticket goods (HD)` ∥ `Everyday basket (WMT · TGT · COST)` →
`Retailer gross margin & mix` → `Inventory / markdown cadence` → `Guidance (the 08-19/08-20 prints)`
*(cross-sector input)* ← `Refined-product price (ENRG chain terminus)`.

- **Bottleneck justification**: supply is not constrained anywhere in this chain. **Wallet share is** —
  and the July retail print plus a politically-endorsed high pump price are two dated squeezes on the
  same node. ⚠ **`[inferred]` — no issuer filing was pulled this run**; the three prints are the test.
- ★ **Why `ABNB` sits on the right side of the bottleneck while `HD` sits on the wrong side is a
  falsifiable claim, not a story**: if wallet share is the constraint, experience spend and big-ticket
  goods compete directly. **`S93` branch B tests exactly that** (`ABNB` − `HD` 5-session excess spread
  vs `SPY` **> +5pp**).

## §5 · What this DEEP did NOT do — stated rather than implied

- **No `module_business_us` / `module_disclosure_us` pull** on any name. Inventory position, comp
  trajectory and margin guidance are **`unknown`** (C3), not "neutral".
- **No chain-hop run** — the L2 offers it and it was not used. Any un-named beneficiary in this chain
  is **unsearched**, and that is a gap, not an absence.
- ⚠ **These omissions are the cost of promoting a 5th slot into an already-committed budget**, and they
  are logged so the next run inherits the debt rather than re-discovering it.

## §6 · Track KPIs and anti-signals

| Track KPI | Current (08-14) | Kill / anti-signal |
|---|---|---|
| **`S93` cross-sectional sign test** | `TGT` +, `WMT` −(20d), `HD` − | **branch A** (all three negative on 5d excess vs `SPY` at the 08-21 settle) ⇒ one factor, "the consumer is rolling" |
| **`ABNB` − `HD` 5-session excess spread vs `SPY`** | +2.966 − (−5.111) = **+8.077pp** | falls **< 0** ⇒ the wallet-share bottleneck claim fails |
| `TGT` − `COST` 60-day excess spread vs `SPY` | **+33.6pp** | converges **< +10pp** ⇒ the intra-Staples split is not a unit |
| `XLY` exc5 vs `SPY` | **−1.783, worst of eleven** | turns positive ⇒ the UW-side wind is gone |
| DISC Δ | **+0.038 (positive)** — the number that blocked the demote | turns negative ⇒ ROTATION's stated blocker clears |
| `WMT` implied move | **±5.0% (expiry 08-21, D5)** — event-priced | a move **inside** ±5.0% is **pre-declared no-information** |

**🚨 VOID**: a **tariff announcement affecting consumer goods** inside the window ⇒ `S93` is void; the
prints would be reacting to policy, not to the consumer.

## §7 · Verdict handed forward

**No sector verdict is proposed, and that is the finding.** DISC (N−) and STPL (UW−) are **held**, and
this DEEP's conclusion is that **both labels are the wrong object** — the measured split runs across
them, not along them.
- ✅ **To BET §B: `ABNB`** — the one name in this complex the money confirms: **🟢가속, 3-axis
  producible** (OBV 매집 ∧ RS20 +21.6 ∧ `vol_surge` **1.55**), **FINRA clean-rise (short z −0.94)**,
  **exc60 +34.525 vs `SPY`** and **exc20 +21.639** with **exc5 still positive (+2.966)** — i.e. **not**
  `M149`'s decaying-stock shape. Re-tagged **EXTENDED-BUT-LIVE** by PREMORTEM Lens 3.
- ⚠ **`TGT` is handed forward as a WATCH, not a candidate**: OBV 매집 and a 15.6pp 60-day excess vs
  `SPY`, but it is **🟡 with no `vol_surge` leg**, and **it reports inside the window** — a candidate
  that reports in 3 sessions is a coin-flip, not a thesis.
- 🚫 **`HD` and `COST` are not filed to the rejection ledger**: both are **🔴분산 with a dated print
  inside 5 sessions**, so a rejection now would be scored against an event the desk deliberately chose
  to wait for. **Deferred to the post-print run**, and named here so the deferral is visible rather
  than silent.
- 🚨 **Instrument debt named**: `catalyst_calendar` carried **zero** of the three prints this DEEP is
  built around.
