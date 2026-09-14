# SECTOR_DEEP_UTIL — Utilities (UW) · industry_US · 2026-08-20 · **ROTATING slot, FULL FRESH MAP**

> Rotating pick R2, last DEEP **2026-08-16 (3 runs ago)** ⇒ a full fresh map.
> **Mandate from ROTATION §2c and PREMORTEM 2E**: the sector's `eqflow` is the worst on the board
> while its price excess is POSITIVE. **Which instrument is right, and is the four-legged "duration
> complex" one object at all?**
> **Benchmark `SPY`, named inline on every relative number.** Terminal settled bar **2026-08-19**.
> `n_axes = 3`; 🚫 `G1` binds. Cap weights 36 days stale (`G5`). Analytical only — no buy/sell, no
> sizing (P4).

---

## 0 · ★★★ The bottom line, and it is not the one the mandate expected

**The underweight is right and its stated reason is unmeasurable. Utilities has NO distinguishable
rate beta — measured on 120 settled sessions, `XLU` excess vs `SPY` regressed on Δ10y controlling for
Brent gives +0.0277 with t = 0.92. Neither do `XLRE` (t 0.32), `XLP` (t 1.59) or `XLV` (t 1.54). The
ONLY sector with a significant rate beta is `XLE` — at +0.1657, t 5.29, R² 0.575 — and `XLE` is the
desk's OVERWEIGHT, with a POSITIVE sign. The desk has been underweight four sectors for a rate reason
that does not show up in any of them, and overweight the one sector where the rate actually bites.**

**And the flow verdict survives everything.** Unlike every other sector examined this run, **Utilities
has essentially no internal dispersion** — all three nodes are negative and only **1 of 12** names
accumulates. **This is the one sector on the board where the GICS label IS the right unit.**

---

## 1 · Flow — the sector, then the nodes

**Sector**: `wflow` **−0.568** · **`eqflow` −0.545 = LAST of eleven** · `wflow_ex_top1` **−0.578**
(*worse* without `NEE`, so **not** a flipper) · **0🟢 / 8🔴 of 15** · Δ (one session) −0.171 ·
`top1` `NEE` at **17.7%**.

**Sub-node decomposition (equal-weight, `us_top300`, settled 08-19):**

| Node | n | EW flow | rs20 vs `SPY` | rs60 vs `SPY` | OBV 매집 | Names |
|---|---:|---:|---:|---:|---:|---|
| regulated integrated | 9 | **−0.561** | −6.6 | −5.5 | **1 / 9** | `NEE` `SO` `DUK` `AEP` `D` `XEL` `ED` `WEC` `PEG` |
| **IPP / merchant "AI-power"** | 2 | **−0.689** | −10.2 | −10.9 | **0 / 2** | `CEG` `VST` |
| gas / other | 1 | −0.750 | −10.9 | −10.9 | **0 / 1** | `SRE` |

**Spread: 0.189 flow points** — against a sector aggregate of **−0.545**.
⇒ ★ **The dispersion is a THIRD of the sector's own magnitude.** Lens B5's test is whether the spread
*exceeds* the sector move; here it does not, by a wide margin. **The label is the right unit.**
★ **Contrast, measured in this same run**: Information Technology's spread is **1.090 against a −0.197
aggregate (5.5× the sector move, nodes pointing both ways)** and Health Care's is **1.051 against
+0.252 (four nodes agreeing, one dissenting)**. **Three sectors, three completely different
structures — and the desk's instruments produce one number for all three.**

★★ **The AI-power leg is the WORST node in the sector, not a rescue.** `CEG` −0.600 🔴분산 and `VST`
−0.778 🔴분산, **0 of 2 accumulating**, EW rs60 **−10.9**. The "utilities are an AI-datacentre play"
frame — carried in this desk's own files and echoed in this window's body tier (*"Nvidia Chip-Filled
Data Centers Need More Power Than Any Utility Can Promise"*, 3 outlets) — **is being sold harder than
the regulated leg it was supposed to differentiate from.**

---

## 2 · ★★ The contradiction the mandate exists to resolve

| | flow instrument | price instrument |
|---|---|---|
| **Utilities** | `eqflow` **−0.545, LAST of 11**, `ex_top1` −0.578, **0🟢/8🔴**, **1 of 15 accumulating** | `XLU` 5-session excess vs `SPY` **+0.855** (β-adj +0.475, β 0.146) |
| Real Estate | `eqflow` −0.252 (10th), **0🟢/4🔴** | `XLRE` excess **+1.568** (β-adj +1.245) |

**Both duration-labelled underweights rallied while their flow sat at the bottom of the board.**

**Resolution — the flow instrument is the better-supported one here, on three independent grounds:**

1. **The flow reading is UNANIMOUS across nodes and names** (§1): all three nodes negative, 1 of 12
   accumulating, and the sign survives removing the largest name. **A price move with no
   node-level carrier is a re-rating of the index, not of the businesses.**
2. **The price move has an alternative and better-supported cause**, and it is dated: on **2026-08-19**
   Treasury announced a **doubling of long-dated buyback operations** (MACRO §D-1, body-read), long
   yields fell, the dollar hit three-month lows and gold jumped. **`XLU` participated at +0.855pp —
   the WEAKEST of the four "duration" legs**, against `XLV` **+4.742** (a drug trial) and `XLE`
   **+4.622** (the crack). **If this were a duration bid, the purest duration leg would not be last.**
3. **§3's regression says `XLU` has no measurable rate exposure to be bid on.**

⇒ **The UW stands on the flow, and ROTATION was right to DECLINE the promotion** — its only argument
was a price/macro one, and this file confirms that argument does not survive measurement.

---

## 3 · ★★★ The rate beta, measured this run rather than inherited

**Method**: daily excess return vs `SPY` regressed on **Δ`DGS10` in bp**, controlling for **Brent
(`BZ=F`) daily %**, OLS, **120 settled sessions 2026-02-26 → 2026-08-18** (`[FRED]` ends 08-18).
⚠ **`C5`: 120 sessions is a choice**, stated on the same line as the result.

| ETF | β(Δ10y) | t | β(Brent) | t | R² |
|---|---:|---:|---:|---:|---:|
| `XLU` | **+0.0277** | **0.92** | +0.0510 | 1.69 | 0.056 |
| `XLRE` | **+0.0086** | **0.32** | +0.0211 | 0.77 | 0.010 |
| `XLP` | +0.0505 | 1.59 | +0.0171 | 0.54 | 0.039 |
| `XLV` | +0.0462 | 1.54 | −0.0022 | −0.07 | 0.025 |
| **`XLE`** | **+0.1657** | **5.29** | **+0.2315** | **7.37** | **0.575** |
| `XLK` | −0.0649 | −2.21 | +0.0171 | 0.58 | 0.042 |

**Six simultaneous tests ⇒ Bonferroni |t| > ~2.6.** ⇒ **`XLE` is the ONLY sector that clears it, and
its rate beta is POSITIVE.** `XLK` at −2.21 is **suggestive and does not clear**; the four duration
legs are **nowhere near**, with R² of 0.010–0.056.

★ **This independently reproduces the measurement `S102` recorded on 08-19** (a different operator,
one session earlier, window ending 08-18: `XLU` +0.0049 · `XLRE` −0.0072 · `XLP` +0.0224 ·
`XLV` +0.0185 · `XLE` +0.1534). **The magnitudes differ — this run's `XLU` reads +0.0277 against
+0.0049 — and the CONCLUSION is identical: the duration underweights have no measurable rate beta and
the overweight does.** ⚠ **The magnitude instability across two nearly-identical windows is itself
the finding**: an effect that moves 5× between adjacent estimations is not a coefficient anyone should
size on. Reported as **"indistinguishable from zero"** (`C4`), not as "+0.0277".

⇒ **The underweight's STATED mechanism ("real yields are repricing duration") is not measurable in
this sector.** That does not make the underweight wrong — §1 and §2 say it is right — **it makes the
reason wrong**, and a right call held for a wrong reason will be exited for a wrong reason.

---

## 4 · The customers, named (rule A6)

Utilities' customers are **ratepayers and, for the merchant/IPP node, data-centre offtakers**.
**Two disclosed-spend readings, both indirect and both stated as such:**

- **The AI-datacentre offtake story**: the same window's body tier carries *"Big Tech Is on Pace to
  Spend $735 Billion on AI Data Centers in 2026"* (5 outlets) and *"Nvidia Chip-Filled Data Centers
  Need More Power Than Any Utility Can Promise"* (3 outlets). ⇒ **the demand narrative is intact and
  loud** — and the two names most levered to it (`CEG`, `VST`) are **the sector's worst node**
  (§1). **Narrative up, money out. That divergence is the sector's central fact today.**
- **The regulated leg's "customer" is a rate case**, and **no rate-case docket was pulled in this
  run.** ⚠ **Marked `unknown` (`C3`)**, not concluded around.
- ⚠ **No utility in the sector prints inside this window** (`NEE` `SO` `DUK` `AEP` `D` all report in
  late October). **Stated with the date, per the rule.**

---

## 5 · The frame-transfer question, answered

**Frame**: *regulated-return / take-or-pay floors* — the structure this desk trusts on `KMI`'s RPO,
`LNG`'s tolling and, historically, `VST`'s **20-year PPA floor**, and which turned out to save `MU`'s
margin thesis when its 10-Q was finally opened.

**Does it apply here? ✅ CHECKED — and it applies MORE here than anywhere else on the board, which is
exactly why the flow reading is interesting.** A regulated utility's return is **set by a commission**,
which is the strongest revenue floor in the equity market. ⇒ **The negative flow cannot be a
cash-flow-durability judgement**; whatever the market is selling, it is **not** doubting the earnings.
⚠ **And this file did NOT read a single utility filing or rate order to verify the current allowed
ROE at any name.** The frame is applied from structure, not from a document — **stated as an
inference, not a measurement** (`[inferred]`).

⇒ **The open question this leaves, handed forward**: if the earnings are floored and the flow is the
worst on the board, the sale is about **discount rate or opportunity cost**, and §3 has just shown the
discount-rate channel is unmeasurable. **Neither this file nor the desk has a third explanation, and
saying so is the honest end of the analysis.**

---

## 6 · Positioning and short pressure — settled 08-19

`NEE` z **+0.01** (5v5 +0.0·) · `SO` −0.33 (+0.1·) · `DUK` +0.30 (−3.0▼) · `CEG` −0.16 (**−10.1▼**) ·
`VST` −0.55 (−4.4▼) · `D` +0.28 (+5.7▲) · `SRE` −0.29 (**+16.1▲**).
⇒ **Not one crowded-short and not one clean short-exit in the whole sector — every name is 🟡 normal.**
**There is no positioning story here at all**, which is itself informative: the sector is being sold
by longs, not pressed by shorts. ⚠ `D6`: FINRA short-vol includes MM hedging and carries nothing
alone; it is paired with the flow table in §1.
**Implied move `XLU` ±0.9%, expiry 2026-08-21 `D1`, P/C 0.87, skew −15.4** ⇒ a **floor**, and the
negative skew is the only mildly bullish instrument in this file.

---

## 7 · Sub-node dispersion — the explicit lens-B5 ruling

**Spread 0.189 against a sector move of −0.545 ⇒ the spread is ~35% of the sector's magnitude.**
**RULING: the label is the correct unit for Utilities.** Every downstream statement about "UTIL" in
this run may be read as a statement about the sector, without a node caveat — **the only sector
examined today of which that is true.**

---

## 8 · Track-KPIs and anti-signals, as observables

| # | KPI / anti-signal | Threshold | Owner |
|---|---|---|---|
| K1 | **Is the four-legged complex one object?** Cross-sectional **range** of `{XLU,XLRE,XLP,XLV}` exc5 vs `SPY` | `P78`: A ≥ **+4.71** (p85, four objects) · B ≤ **+1.69** (p15, one object) at **08-26** · **now 3.888 = 73.4th %ile** | `P78` |
| K2 | Does the price-vs-flow gap close, and which side moves? | `XLU` exc5 vs `SPY` **+0.855** against `eqflow` **−0.545**; kill the UW if `eqflow` turns positive **and** the node EW rs20 vs `SPY` turns positive (now −6.6) **and** ≥3 of 15 names reach OBV 매집 (now 1 of 15). ⚠ **RULE D6 applied, not exempted — the OBV count is the THIRD leg of a conjunction whose first two legs are `eqflow` and RS; OBV never fires this KPI alone** | this file |
| K3 | The AI-power leg | `CEG`+`VST` EW flow, now **−0.689**; a turn above 0 would re-open the offtake thesis | this file |
| K4 | The rate channel | `P77`: `DGS30` at the first close covering **08-26** — A ≤5.18 · B ≥5.38 · **now 5.28** | `P77` |
| A1 | 🚨 **Anti-signal**: a **rate case or an FERC order** at a top-5 constituent inside the window ⇒ the flow reading is a regulatory event, not a sector judgement. **Not measured this run — `unknown` (`C3`)** | | this file |
| A2 | ⚠ **Correlated-UW flag, PREMORTEM 2E, FIRED**: `UTIL` and `RE` are bottom-two on `eqflow` **and** both rallied on price. **If they are one bet the desk is short one thing twice.** `P78` brackets it; **no fourth bracket was written, deliberately** — that would count one tail twice | | PREMORTEM 2E |
| A3 | ⚠ **`S98` is at VOID** on the FOMC-minutes clause (MACRO §E-0), so **the four-leg sign test may not settle at all.** `P78`'s dispersion test is the surviving instrument for this question | | MACRO §E-0 |

---

## 9 · What this file did NOT establish

- **No rate case, FERC order, or allowed-ROE figure was read.** §5's regulated-floor argument is
  **`[inferred]` from structure**, not measured from a document, and it may not be cited downstream as
  evidence.
- **No third explanation for the flow.** §5 rules out cash-flow durability and §3 rules out the
  discount-rate channel; **the desk does not have a mechanism for why Utilities is the worst-flowing
  sector on the board.** That gap is the honest output of this DEEP, and it is written down rather
  than filled with a story.
- **The IPP/merchant node has n = 2** (`CEG`, `VST`). **`TLN` and `NRG` are outside `us_top300`**, so
  the "AI-power" node is measured on two names — **a thin denominator, stated** (`C4`).
- **No lead/lag claim appears**, so none is inherited as fact (rule A5).
- ⚠ **The 08-19 tape is one session.** §2's cause attribution (Treasury buybacks) rests on a
  body-read of a dated announcement plus a cross-sector ordering, **not** on an event study.
