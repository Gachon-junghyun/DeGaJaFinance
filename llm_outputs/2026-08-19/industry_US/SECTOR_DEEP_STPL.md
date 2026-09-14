# SECTOR_DEEP_STPL — Consumer Staples (UW− → UW) · industry_US · 2026-08-19 · **PREMORTEM-PROMOTED 5th slot**

> **Benchmark for every relative figure in this file: `SPY`.** It is also named inline on each one.
> Flow numbers are `SECTOR_FLOW_US.json`, `asof` **2026-08-18**, 3 axes, `velocity` field **revoked (G1)**.
> Terminal settled bar **2026-08-18** — there are no 08-19 settled prices and every sweep Δ is **TWO
> sessions (08-14 → 08-18), not one (G2)**. Sector cap weights **35 days stale (G5)**.
> Last full DEEP on this sector: **2026-08-17** — this file leads with the delta, not a re-map.
> Analytical only — **zero buy/sell, zero sizing (P4)**.

---

## 0 · 🚨 The clock, before any number — this file is being written while the tape is live

`PREFLIGHT_US.md` fixed the run clock at **KST 21:51–21:58 = ET 08:51–08:58, pre-market**, and set the
binding: **"No stage may re-pull prices after 22:30 KST and treat the result as comparable to the sweep."**
This stage began at **22:52 KST (09:52 ET)** — **22 minutes after the bell**. Every module this mandate
names (`module_fundamentals_us`, `module_flow --positioning`, `module_chart --read`) re-pulls prices as a
side effect. **It re-pulled them. That is a rule breach by construction, and the response is quarantine,
not silence**: all post-22:30 KST readings are confined to **§8** and **no judgement in §1–§7 rests on one.**

**Two primary-source facts about where the two prints stand, from EDGAR, which is not a price feed:**

| issuer | scheduled | EDGAR state at 23:00 KST | consequence for this file |
|---|---|---|---|
| **`TGT`** | **2026-08-19 (today)** | **8-K Item 2.02 "Results of Operations", filed date 2026-08-19** — [accession 0000027419-26-000034] | **The print is on the wire.** This file has **not** read it, does **not** know its contents, and asserts nothing about them |
| **`WMT`** | **2026-08-20** | **No Item 2.02 in 90 days** — the most recent is **2026-05-21** | **The print is genuinely ahead.** Everything below about `WMT` is pre-event |

⚠ **This is the honest statement of position and it is deliberately awkward.** The mandate says *"you are
writing before `TGT` reports"*; EDGAR says the 8-K exists. **Both are true of different objects** — the
*analysis* is pre-print (built on the 08-18 settled tape and on filings dated 08-14 and earlier), the
*calendar* is not. Nothing here is written as if the quarter were known, and §9's KPIs are all dated and
falsifiable **after** this file closes.

---

## 1 · Delta since the 08-17 DEEP — what actually changed in two settled sessions

The 08-17 file mapped all 19 names on `asof 2026-08-14`. Same 19 names, `asof 2026-08-18`:

| | `TGT` 08-14 | `TGT` 08-18 | `WMT` 08-14 | `WMT` 08-18 |
|---|---|---|---|---|
| `flow_score` | +0.503 (#1) | **+0.713 (#1)** | −0.226 (#9) | **+0.220 (#4)** |
| OBV state / `obv_norm` | 매집 +0.115 | 매집 **+0.177** | flat +0.015 | 매집 **+0.115** |
| **RS20 vs `SPY`** | **+6.2** | **+7.5** | **−3.5** | **+1.8** |
| **RS60 vs `SPY`** | **+15.6** | **+17.5** | **−19.9** | **−8.4** |
| `vol_surge` | 1.01 | 1.12 | 0.80 | 0.83 |
| tag | 🟡중립 | 🟡중립 | 🟡중립 | 🟢가속 **(new-🟢)** |

*(OBV is a grade-C axis and never carries a row alone — RS20 and RS60 vs `SPY` are on every line above,
and the volume axis is on the next one.)*

Sector aggregate moved `wflow` **−0.242 → +0.083**, `eqflow` **−0.213 → −0.020**, greens **0 → 1**, reds
**5 → 3**, and `delta` **+0.325 = the largest two-session improvement on the 11-sector board**. Verified
against the JSON: cap-weighted `wflow` recomputes to **+0.0826**, cap-weighted Δ to **+0.3251**, equal-
weighted `eqflow` to **−0.0197**. **Every figure ROTATION §2b used reproduces exactly.** The dispute below
is not about arithmetic.

⚠ **One item from the 08-17 file is corrected by the new tape rather than carried.** That file recorded
`TGT` `vol_surge` **1.01** and a `module_flow` standalone probe reading **0.79** on the same closes. Today
the sweep reads **1.12** and the sector maximum is **1.62**. The 08-17 instrument-conflict finding stands as
history; the number it disputed has moved and is restated here rather than quoted forward.

---

## 2 · ★★★ THE MANDATE — was `UW− → UW` made on the right reasoning?

> **VERDICT: the direction is defensible, the reasoning is wrong, and it is wrong on THREE counts —
> one that PREMORTEM found, and two that are measured here for the first time. The third one is the
> serious one, because it is not about Staples: it puts the same question on the other promotion this
> run made on the same rule.**

### 2a · Count 1 — `TGT` is under-computed, not "mega-cap-narrow" *(PREMORTEM Lens 1 — independently reproduced)*

ROTATION §2b promoted on `wflow +0.083 ≫ eqflow −0.020` and labelled that **"mega-cap-narrow"**.
The delta decomposition, recomputed from `mcap` in the JSON:

| name | cap weight | own Δ | contribution to the sector's **+0.325** | share |
|---|---|---|---|---|
| **`WMT`** | **28.88%** | **+0.446** | **+0.1288** | **39.6%** |
| `COST` | 13.07% | +0.361 | +0.0472 | 14.5% |
| `PM` | 8.61% | +0.511 | +0.0440 | 13.5% |
| `PG` | 10.85% | +0.360 | +0.0390 | 12.0% |
| `PEP` | 6.01% | +0.391 | +0.0235 | 7.2% |
| … | | | | |
| **`TGT`** | **1.84%** | **+0.210** | **+0.0039** | **1.2%** |

**Confirmed to the third decimal.** `TGT` carries the sector's **best `flow_score` (+0.713)**, the sector's
**best RS20 vs `SPY` (+7.5)** and the sector's **best RS60 vs `SPY` (+17.5)** at a **1.8%** cap weight, so
it moves the cap-weighted instrument by **+0.004**. **Every instrument this run read — `wflow`, `XLP`, the
β-adjusted `XLP` excess vs `SPY` — is cap-weighted, and in all of them `TGT` is invisible.** That is
under-computation. "Mega-cap-narrow" describes what the *instrument* can see, not what the sector is doing.

### 2b · Count 2 — level and change were conflated: the Δ is the board's BROADEST, not its narrowest

**"Mega-cap-narrow" was derived from a LEVEL comparison (`wflow` vs `eqflow`) and applied to a decision
made on a CHANGE.** The correct narrow/broad test for a change is the **equal-weighted delta**, which
nothing in this run computed. It is computed here, for all 11 sectors:

| sector | `wflow` | `eqflow` | **cap-wtd Δ** | **EQUAL-wtd Δ** | names improving |
|---|---|---|---|---|---|
| **Consumer Staples** | +0.083 | −0.020 | **+0.325** | **+0.1935** | **16 / 19 = 84%** |
| Energy | +0.354 | +0.295 | +0.137 | +0.1931 | 14 / 16 = 88% |
| Health Care | +0.114 | +0.163 | +0.228 | +0.136 | 20 / 32 = 62% |
| Utilities | −0.397 | −0.376 | +0.049 | +0.057 | 12 / 15 |
| Financials | +0.028 | −0.087 | +0.060 | +0.039 | 30 / 47 |
| Information Technology | −0.195 | −0.135 | −0.218 | −0.179 | 17 / 56 = 30% |

⇒ **Consumer Staples has the highest equal-weighted two-session Δ on the board (+0.1935) with 16 of 19
names improving.** On the only instrument that can answer the question ROTATION asked, the improvement is
**the broadest on the board**, not the narrowest. The `wflow ≫ eqflow` gap is a statement about the
sector's *level* — the median staples name is still a negative-`flow_score` name — and that was
transplanted onto a sentence about the *change*. **Two different objects, one label.**

### 2c · ★★★ Count 3 — and it cuts against §2b too: **77–80% of the improvement is calendar, not money**

**Nineteen names improving together over two sessions is exactly what a shared window artifact looks
like.** `flow_score` is `mean[ clip(obv/0.16), clip(rs20/8.0), clip((vol_surge−1)/0.6) ]`, and `rs20` is a
**rolling 20-session excess vs `SPY`**. Advancing `asof` by two sessions **adds two days to the front and
drops two days off the back**. Decomposing every staples name's ΔRS20 into *earned* (08-14 → 08-18,
measured vs `SPY`) and *roll-off* (the two dropped days, measured vs `SPY`):

| name | RS20 @08-14 | RS20 @08-18 | ΔRS20 | **earned** vs `SPY` | **roll-off** |
|---|---|---|---|---|---|
| **`WMT`** | −3.54 | +1.80 | **+5.34** | **+1.08** | **+4.26 (80%)** |
| **`TGT`** | +6.21 | +7.55 | **+1.34** | **−0.15** | **+1.48 (111%)** |
| `CL` | −5.55 | −1.50 | +4.05 | +0.61 | +3.44 |
| `PM` | −5.79 | −2.79 | +3.00 | −0.31 | +3.31 |
| `KDP` | −2.73 | −0.64 | +2.09 | −0.92 | +3.01 |
| `COST` | −2.30 | +0.90 | +3.19 | +1.17 | +2.02 |
| `KR` | −8.07 | −5.05 | +3.01 | +0.53 | +2.49 |
| **sector EW, all 19** | — | — | **+2.48** | **+0.57** | **+1.91 = 77%** |

**`TGT` LOST 0.15pp to `SPY` over the two sessions the promotion was made on.** 100%+ of its RS20
improvement is two bad days falling out of the back of the window. `WMT` — the run's new-🟢 and 39.6% of
the sector Δ — earned **+1.08pp** of a **+5.34pp** RS20 move.

**Converted into the units the promotion was actually made in** — recomputed per name through the same
`clip(rs20/8.0)/3` transform the scorer uses, so `MNST`'s pinned axis contributes zero: the RS20 axis
supplies **+0.1344 = 41% of the cap-weighted +0.3251**, and **the roll-off portion of it is +0.1022, i.e.
31% of the sector's headline delta is the calendar.** ⚠ **That is a FLOOR, not a ceiling** — `obv_norm` and `vol_surge` are rolling-window
statistics too and were **not** decomposed here, so the true calendar share is **≥31%** and this file does
not claim to know how much more.

★★ **And it is not a Staples problem. It is a board problem, and it re-ranks today's two promotions:**

| sector | EW ΔRS20 | **earned** vs `SPY` | roll-off | roll-off share |
|---|---|---|---|---|
| **Energy** | +3.28 | **+3.75** | **−0.47** | **−14% — the only sector that EARNED it** |
| **Health Care** *(promoted N → N+ today)* | +2.96 | +1.55 | +1.41 | **48%** |
| **Consumer Staples** *(promoted UW− → UW today)* | +2.40 | **+0.48** | +1.92 | **80%** |
| Financials | +1.32 | +0.11 | +1.21 | 92% |
| Communication Services · Real Estate · Materials · Industrials · Cons. Discretionary | +1.04 … +0.51 | **all negative** | +0.99 … +1.45 | **>100%** — RS20 rose while the sector lost ground to `SPY` |

⚠ **Reconciliation, stated rather than smoothed**: the cross-sector pass above runs on each sector's
**data-complete** names (Staples 18 of 19 — `MNST` drops out of that pass on a window gap), which is why
its Staples row reads **80%** against the 19-name table's **77%**. **Both are printed; neither is chosen.**

⇒ **On 08-14 → 08-18 the 20-session window dropped two days on which most of the market lagged `SPY`.
Nine of eleven sectors received a free RS20 improvement from the calendar; six of them improved while
actually losing ground to `SPY`.** The Δ-rule read that as money moving.
⇒ **Of the two promotions made today on that rule, Staples' is the weaker: 77–80% roll-off against Health
Care's 48%.** And **Energy — held, not promoted — is the one sector whose flow improvement was genuinely
earned**, on an axis nothing in this run computed.
⚠ **Honest limit (`C4`/`S3`)**: this is one 20-session window, one two-session advance, 299 names. It is a
**construction** finding about `rs20`, not a statistical claim about flow, and it does **not** touch the
`flow_score` **LEVEL** — `TGT`'s **+7.55** RS20 vs `SPY` and **+17.54** RS60 vs `SPY` were independently
recomputed from settled closes to 08-18 and are real 20- and 60-session facts.

### 2d · The case AGAINST the promotion — and the β objection is **window-dependent and it reverses**

MACRO's binding: *"no sector may be moved on a RAW excess return alone"*, evidenced by `XLP` raw excess
**+0.852 vs `SPY`** flipping to **−0.592** once β (−0.08, 252d) is removed. ROTATION §2b carried this as
the unresolved price disagreement. **Measured across all four windows in play, β-adjusted excess vs `SPY`
= raw − β×`SPY`, β from 252 daily settled returns to 08-18:**

| window | `SPY` | **`XLP` β-adj** | `TGT` β-adj | `WMT` β-adj | EW{`TGT`,`WMT`} β-adj |
|---|---|---|---|---|---|
| **3-session 08-13→08-18** *(MACRO / `S98` / `S80`)* | **−1.341%** | **−0.592** | −1.338 | −0.581 | −0.960 |
| **2-session 08-14→08-18** *(the sweep Δ window)* | **−1.145%** | **−0.681** | −0.774 | −0.173 | −0.473 |
| **20-session** *(the window `rs20` reads)* | **+2.562%** | **+2.006** | **+8.944** | **+4.609** | **+6.777** |
| **60-session** *(the window `rs60` reads)* | **+3.330%** | **+1.343** | **+19.357** | −4.733 | **+7.312** |

🚨 **`XLP`'s β-adjusted excess vs `SPY` is negative on the two windows where `SPY` FELL and positive on the
two windows where `SPY` ROSE.** The β correction's sign is the sign of the market move — that is what
β-adjustment *does* — so **"the flow axis and the risk-adjusted price axis disagree" is, in large part,
a WINDOW disagreement, not an instrument disagreement.** MACRO's −0.592 is a 3-session number; the
`flow_score` it is being weighed against reads a 20-session window with the opposite `SPY` sign.
⇒ **The two axes were never measured on the same days.** Once they are, on the 20-session window they
**agree**: `XLP` β-adj **+2.006 vs `SPY`**, `TGT` β-adj **+8.944 vs `SPY`** — *higher* than its raw excess
of +7.548, because stripping β **helps** a positive-β name that outperformed a rising `SPY`.

★ **And `TGT` is not a low-β defensive.** Measured β vs `SPY`, 252 daily settled returns to 08-18:
**`TGT` +0.455 · `WMT` −0.098 · `COST` −0.140 · `XLP` −0.077 · `KR` −0.666.** `TGT` is **the highest-β name
in the big-box node and the only positive-β name of the four** — so *"Staples outperformed because it is
low-β in a down tape"* is the one explanation that **cannot** be applied to the name carrying the sector's
flow rank. ⚠ Three instruments give three betas for `TGT` — `module_fundamentals_us` (yfinance `.info`,
5-year monthly) reads **0.97**, this file's 252-day daily reads **0.455**, a 60-day daily reads **−0.075**.
**`C5`: the β window is a choice and it is on the same line as the conclusion.**

🚨 **Correction to `S100` as registered today.** Its branch A rests on *"basket β vs `SPY` = **0.09**"*.
Measured here on 252 daily settled returns to 08-18, **EW{`TGT`,`WMT`} β = +0.178** — roughly double; on
60 daily returns it is **−0.262**. **The registered number does not reproduce.** ⚠ **The thresholds do not
need to move and are not moved here**: `S100` voids on `|SPY| > 2.5%`, so inside the live band a β of
0.178 can contribute at most **0.178 × 2.5 = ±0.445pp** against a **±6.5pp** threshold — **≤6.8% of the
bar**. **`S100`'s "β-free" claim survives at the corrected β; the number quoted for it does not.**

### 2e · ✅ What the mandate answers

**Right verdict, wrong reasoning, and the third count is the one that should propagate.**

1. **The one-notch move is defensible** and no re-vote is proposed here (P4 — this stage does not carry a
   verdict). The sector genuinely holds the board's best equal-weighted Δ, and `TGT` genuinely holds a
   **+7.5 RS20 and +17.5 RS60 vs `SPY`** with OBV accumulating (`obv_norm` +0.177).
2. **"Mega-cap-narrow" is a false description**, twice over: it hides the sector's best name behind a 1.8%
   weight (§2a), and it is a level statement doing a change statement's job (§2b).
3. **★ The instrument the promotion was made on was, this run, ≥31% measuring the calendar** (§2c) — and
   the same instrument made the Health Care promotion (48% roll-off) and was withheld from Energy (the
   only sector that earned it). **This is a rule-level finding, not a Staples finding, and it belongs
   upstream.**
4. **The β objection does not settle it either way** — it changes sign with the window (§2d), so neither
   `S80` tonight nor `S98` tomorrow can adjudicate the flow axis using a 5-session raw sign. That is
   `P74`'s point, and this file supplies the four-window table it lacked.

---

## 3 · Sub-sector dispersion — the sector label is the wrong unit, and by a factor of 5–16×

Five nodes, equal-weighted within node, cap share of the sector's **$3,228.5bn** (weights **35 days stale**):

| node | n | cap % | EW flow | EW Δ | **EW RS20 vs `SPY`** | **EW RS60 vs `SPY`** | EW `vol_surge` | OBV 매집 |
|---|---|---|---|---|---|---|---|---|
| **Big-box / discount / club** (`TGT` `WMT` `COST`) | 3 | **43.8** | **+0.271** | **+0.339** | **+3.4** | −0.9 | 0.86 | 2/3 |
| Food & beverage (`KO` `PEP` `MNST` `KDP` `CCEP` `HSY` `MDLZ` `ADM`) | 8 | 26.6 | +0.073 | +0.167 | −5.8 | −5.3 | 0.84 | 6/8 |
| Household & personal (`PG` `CL` `KMB` `KVUE`) | 4 | 15.2 | −0.019 | +0.172 | −3.5 | **+1.2** | 0.81 | 3/4 |
| Tobacco (`PM` `MO`) | 2 | 12.2 | −0.342 | +0.267 | −8.0 | −9.4 | 1.04 | 0/2 |
| Grocery / food distribution (`KR` `SYY`) | 2 | 2.2 | **−0.505** | +0.052 | −3.4 | −8.1 | 0.71 | 0/2 |

*(RS20 and RS60 are both benchmarked to `SPY`; OBV is grade-C and is the last column, never the first.)*

**The arithmetic that decides the unit question:**
- Node `flow_score` spread **0.776** vs a sector `wflow` of **+0.083** ⇒ **9.4×**.
- Node RS60 spread vs `SPY` **10.5pp** vs `XLP`'s own 60-session excess of **−2.24pp vs `SPY`** ⇒ **4.7×**.
- Name extremes: **`TGT` +17.5 vs `KR` −19.3 = 36.8pp** against that same −2.24pp sector move ⇒ **16.4×**.

⇒ **The internal spread exceeds the sector move by between 5 and 16 times. "Consumer Staples" is the wrong
unit and the UW/UW− is a node call wearing a GICS label.** ★ **But the node it is a call on has changed
since 08-17.** That file found big-box **collapsing** (`WMT` −19.9, `COST` −18.0 RS60 vs `SPY`) and named
the sector *"a food-retail call wearing a staples label."* Two sessions later the big-box node is the
sector's **best** node on flow (+0.271), on Δ (+0.339) and on RS20 vs `SPY` (+3.4), and **grocery/
distribution is the worst (−0.505)**. Part of that is real (`WMT` earned +1.08pp vs `SPY`), and part is
§2c's roll-off — **but the 08-17 framing that grocery and big-box are one falling node no longer holds:
`TGT` +7.5 and `KR` −5.1 RS20 vs `SPY` sit inside the same three-name retail complex.**

⚠ **The 08-17 "household is the defensive node" reading is now contradicted on the 20-session axis**:
household EW RS20 is **−3.5 vs `SPY`** while its RS60 is **+1.2 vs `SPY`**. **The node that was leading on
the long window is lagging on the short one.** Stated, not resolved — it is one window each way.

---

## 4 · The volume gate — 6 of 19 pass accumulation, 0 clear 1.2, and the sector max of 1.62 belongs to a collapse

`SWEEP_READ §3`: **6 of 19** Staples names pass `OBV 매집 ∧ RS20 > 0 vs SPY` — verified: **`TGT` `KO` `HSY`
`WMT` `MDLZ` `PEP`** — and **0 of those 6** clear `vol_surge ≥ 1.2`, while the **sector maximum is 1.62**.
SWEEP concluded from that that *"volume does exist there, so its absence is a per-name gate failure rather
than a sector-wide one"*, contrasting Energy's max 1.06 and Health Care's 1.00.

🚨 **The 1.62 has an owner and it changes the conclusion. It is `MNST` — the only name in the sector at or
above 1.2 — and it carries RS20 −52.9 and RS60 −48.8 vs `SPY`.**

| | `MNST` |
|---|---|
| `vol_surge` | **1.62 — rank 1 of 19, the sector's entire "volume exists" claim** |
| RS20 / RS60 vs `SPY` | **−52.9 / −48.8** |
| `flow_score` · Δ | +0.173 · **+0.433** |
| OBV state | 매집 +0.083 — *the weakest accumulation of the 11 accumulating names, and it sits under those RS figures* |
| FINRA daily short-volume ratio, **08-18 settled** | **51.6% vs its own 20-day base 37.6%, z +1.43** |

⇒ **The sector's open volume gate is opened by short-side and event volume on a −52.9pp RS20 name vs
`SPY`, not by accumulation.** Restating SWEEP's finding precisely: **Staples' 1.62 is not evidence that the
sector's accumulators could clear the gate if they had the volume — it is evidence that this sector's
volume went somewhere else.** Energy's 1.06 and Health Care's 1.00 mean *"no name had the volume"*;
Staples' 1.62 means *"one name had it and it was the one being liquidated."* **Those are different facts
and they do not license the same inference.** The six accumulators max out at `TGT`'s **1.12** — closer to
Energy's ceiling than to their own sector's.

**FINRA daily short-volume, all settled 2026-08-18** (`us_flow.py`), read against the short-**interest**
stock from `module_flow --positioning`, because **`D289` established these are different objects**:

| name | short **volume** ratio (z vs own 20d) | 5v5 trend | short **interest** % float | verdict on the pair |
|---|---|---|---|---|
| `TGT` | 37.6% (**z −0.85**, below own base) | **+6.4▲** | 3.7%, **covering**, DTC 4.3 | consistent — low and covering |
| `WMT` | 37.8% (z −0.27) | **+11.3▲ — the group's largest** | 1.6%, covering, DTC 3.2 | consistent, but pressure **building into 08-20** |
| `COST` | 42.2% (z +0.36) | +1.1▲ | 1.7%, **building**, DTC 3.3 | consistent |
| **`KR`** | **63.3% (z +1.56) — 🔴 the sector's only extreme** | +1.2▲ | 4.2%, **covering**, DTC 3.4 | 🚨 **the two measures point opposite ways — `D289` exactly**: heavy intraday short *volume* against a *shrinking* short *stock* |
| `PG` | 16.3% (**z −1.66**) 🟢 | +2.2▲ | — | pressure leaving |
| `MNST` | 51.6% (z +1.43) | +3.2▲ | — | matches the 1.62 `vol_surge` |

⚠ **The module's own caveat is load-bearing**: FINRA daily short volume is *"공매도체결/총체결, 40~45% is
normal, market-maker hedging included"* — it is a **pressure proxy, not a directional bet**, and `KR`'s
divergence may be same-day-covered flow rather than new positioning. **Recorded unresolved, per `D289`.**

---

## 5 · The two issuers side by side — every multiple carried with its own margin percentile and revision direction

**P4: this section states no direction, no candidacy and no size.**

| | **`TGT`** | **`WMT`** |
|---|---|---|
| Settled close 08-18 | $152.48 | $115.20 |
| Trailing / **forward P/E** | 20.99 / **17.73** | 40.86 / **35.50** |
| PEG · P/S · P/B | 2.83 · 0.68 · 4.44 | 4.39 · 1.28 · 9.83 |
| **Gross margin, latest FY** | **27.9% (FY2026)** | **24.2% (FY2026)** |
| 🚨 **Percentile in its OWN 19-year history** | **13.2nd** *(SEC XBRL FY2008–FY2026; max 32.6% FY2010, min 24.6% FY2023, median 29.7%)* | **23.7th** *(max 25.5% FY2010, min 23.5% FY2023, median 24.7%)* |
| **Estimate-revision trend** *(direction description only — **NEVER** a leading indicator)* | **rising** — current-quarter consensus 2.24 → 2.34 over 90 days; 30-day breadth **9↑ / 0↓** on the current year | **falling** — current-year consensus 2.92 → 2.90 over 90 days; 30-day breadth **0↑ / 8↓** on the current year, **1↑ / 7↓** on next year |
| Consensus target (mean) vs 08-18 close | $144.40 — **below** the settled close | $137.93 — above |
| Analyst mix (30d) | 2 SB / 9 B / **23 H** / 0 S / 3 SS | 9 SB / 27 B / 6 H / 1 S / 0 SS |
| Latest reported revenue | **$25.44bn, +6.70% YoY**, sequential **−16.5% QoQ** vs the $30.45bn Jan quarter *(fiscal-Q4 seasonality — the sequential is a calendar fact, not a deterioration)* | **$177.75bn, +7.33% YoY**, sequential **−6.8% QoQ** vs the $190.66bn Jan quarter *(same seasonality)* |
| Short interest | 3.7% float, covering, DTC 4.3 | 1.6% float, covering, DTC 3.2 |
| 🚨 **Options posture into the print** | **P/C 1.74 · skew +41.1 · implied ±7.8% (D2, at registration)** — deep downside fear | **P/C 0.67 · skew +0.6 · implied ±5.3% (D2)** — **call-heavy and flat-skewed** |

★★ **The finding this table exists for: the two names printing 24 hours apart are opposites on every axis
that is not the sector label.**

- **`TGT`**: the cheapest forward multiple in the pair, at the **13.2nd percentile of its own 19-year gross
  margin**, with estimates **rising** and a **put-heavy, +41-skew** option book. `module_fundamentals_us`
  attaches the standard warning — *"a low forward P/E with estimates revising up may be a peak-margin trap"*
  — and **here the percentile answers it directly: 13.2nd is a near-trough margin, not a peak.** The
  company's own 10-K MD&A names the drivers of the 28.2% → 27.9% decline: *"higher markdown rates and
  purchase order cancellation costs, partially offset by growth in advertising and other revenues; changes
  in category sales mix; and lower inventory shrink."* ⇒ **the multiple is low against a depressed margin
  base**, which is a different object from a low multiple against a peak one. **Which of the two it is
  cannot be settled from here and is not settled here.**
- **`WMT`**: **2× the forward multiple** at the 23.7th margin percentile, with estimates **falling** on a
  **0↑/8↓** 30-day breadth, going into a print its option market prices as **unremarkable** (P/C 0.67,
  skew +0.6). **`WMT` is the run's new-🟢, 39.6% of the sector Δ, and the leg of `S100` whose own options
  market is not pricing an event.**
- ⇒ **`S100` equal-weights a fear-priced name and a complacency-priced name.** Its ±6.5pp thresholds were
  set at the EW implied move (**≈±6.55%**), which is correct construction — but **the basket is not one
  signal**, and a branch-A or branch-B fire will not say which leg produced it. **Recorded as a
  construction note for the settling desk; the thresholds are frozen and are not touched here.**

**Structure, `module_chart --read`, full panel** ⚠ **the panel's last bar is the LIVE 08-19 bar, so RSI and
20-day momentum below are contaminated by an unsettled session and are cited for shape only:**
`TGT` — OBV 누적, 20d slope +97%, no divergence, bull stack 5>20>60>120, price above 4/4 MAs, band expansion
18.2%, **CONFIRMED-TURN**, swing low 133.46 · alongside RS20 **+7.5** and RS60 **+17.5 vs `SPY`**.
`WMT` — OBV 누적 +40%, no divergence, **mixed** MA alignment, 3/4 MAs, CONFIRMED-TURN · RS20 **+1.8** and
RS60 **−8.4 vs `SPY`**. `COST` — OBV 누적 +35% but **bearish divergence**, coiling 5.0% · RS20 **+0.9**,
RS60 **−11.8 vs `SPY`**. `KR` — OBV 중립 −11%, **bear stack**, NEUTRAL/CHOP · RS20 −5.1, RS60 −19.3 vs `SPY`.

---

## 6 · Frame transfer — is there a take-or-pay / RPO / regulated-return analogue in staples retail?

**Answer: the analogue the question expects — supplier rebates and vendor allowances — is NOT one. It is
the structural inverse. The real analogue is membership fee income, and only one of these two issuers
discloses it.**

**(a) Vendor income is anti-lock-in.** `TGT` 10-K (FY ended 2026-01-31), verbatim from the filing:
*"We receive various forms of consideration from our vendors (vendor income), principally earned as a
result of volume rebates, promotions, certain advertising activities, and markdown allowances. Vendor
income is recorded as a reduction of cost of sales… Vendor income earned **can vary based on a number of
factors, including purchase volumes, sales volumes, and our pricing and promotion strategies.**"*

| property | take-or-pay / RPO / regulated return | **retail vendor income** |
|---|---|---|
| pays if volume does **not** happen | **yes** — that is the whole point | **no** — it is volume-contingent by its own definition |
| contracted term / backlog | disclosed, dated | **none disclosed** |
| minimum floor | yes | **none disclosed** |
| separately quantified | yes (RPO is a disclosed balance) | **no — buried inside cost of sales** |
| cyclical behaviour | **damps** the downside | **amplifies** — falls exactly when sales fall |

⇒ **Vendor allowances are a pro-cyclical margin amplifier that an outside analyst cannot size**, because
the reduction runs through COGS with no separate line. **A desk that transfers the take-or-pay frame here
gets the sign backwards.**

**(b) Private label transfers risk TOWARD the retailer, not away.** `TGT`: *"Approximately thirty percent
of our Merchandise Sales come from our owned and exclusive brands."* As **importer of record** on those
goods it is *"responsible for customs compliance, including… payment of all applicable duties and fees"*,
and its duty-refund route (**first sale claims**) has *"processing and payment cycles that extend beyond
one year"* — a **>1-year working-capital drag**. `WMT` discloses the same model (Great Value, Equate,
bettergoods, etc.). **Private label raises gross margin and simultaneously absorbs tariff, inventory and
duty-timing risk that a national-brand pass-through would have left with the vendor.** That is the
opposite of a regulated return.

**(c) The genuine analogue: membership fee income — prepaid, annual, ratable, separately disclosed.**
`WMT` FY2026 10-K, consolidated: net sales **$706,413m**, **membership and other income $6,750m**, total
revenues **$713,163m**, operating income **$29,825m** ⇒ **the fee line equals 22.6% of consolidated
operating income.** By segment:

| `WMT` segment FY2026 | net sales | **membership & other income** | operating income | fee line ÷ segment op income |
|---|---|---|---|---|
| Walmart U.S. | $482,975m | $2,624m | $25,158m | 10.4% |
| International | $130,423m | $1,565m | $5,103m | 30.7% |
| **Sam's Club U.S.** | $93,015m | **$2,525m** | **$2,442m** | 🚨 **103.4% — the fee line EXCEEDS the segment's entire operating income** |

The filing states it plainly: *"As a membership-only club, membership income is a significant component of
the segment's operating income,"* at **$50 Club / $110 Plus** annual fees. **That is the take-or-pay
analogue: paid in advance, recurring, and independent of whether the member shops that quarter.**
⚠ **Sizing caveat the filing forces**: the line is defined as *"membership fees **and other items such as
rental and tenant income, recycling income, gift card breakage income**"* — **the pure fee share is not
decomposed in the 10-K**, so 22.6% and 103.4% are upper bounds on the fee-only figure, not the figure.

**(d) The asymmetry the sector label hides.** `TGT` **has** a paid membership (**Target Circle 360**) — but
its 10-K names *"membership fees"* only inside a prose list of *"other sources"* alongside Roundel
(advertising services to vendors), Target Circle Card profit-sharing and the Target Plus marketplace, and
**discloses no quantified line for any of them.** ⇒ **Of the two big-box names printing inside 24 hours,
one carries a disclosed, quantified, prepaid annuity worth up to 22.6% of group operating income, and the
other's equivalent is unmeasurable from the outside.** **`S100` equal-weights them.**

---

## 7 · Who is the node's customer, and what does their disclosed spend say?

**For retail the customer is the consumer**, so the question becomes: what does this desk actually
*measure* about consumer spend? **The honest answer is: nothing directly.**

| disclosed proxy the desk holds | latest observation | staleness at 2026-08-19 | what it measures |
|---|---|---|---|
| `M2` (`M2SL`) | **23,155.2 (June)** | **~2.5 months** | a **stock of money**, not spending |
| `CPI` (`CPIAUCSL`) | **332.813 (July)** | ~1.5 months | a **price level**, not volume |
| `U-3` (`UNRATE`) | **4.1% (July)** | ~1.5 months | a **labour count**, not outlays |
| `Core CPI` (`CPILFESL`) | **absent — FRED 502**, retry succeeded upstream at 336.789 (July) | ~1.5 months | price level |

🚨 **The desk's FRED specification contains no consumer-spending series at all** — no retail sales, no
PCE, no real disposable income, no personal saving rate. **All three usable proxies are monthly, all three
are stale by six weeks or more, and not one of them is a measure of what a consumer spent.** For a DEEP on
a node whose entire revenue line is consumer transactions, **that is the gap, and it is stated rather than
papered over with a rate series.**

**What is left is the issuers' own disclosure — and it is a quarter old:**

| node member | latest **reported** period | revenue | YoY | sequential |
|---|---|---|---|---|
| `TGT` | quarter ended **2026-04-30** | $25.44bn | **+6.70%** | −16.5% QoQ *(fiscal-Q4→Q1 seasonality)* |
| `WMT` | quarter ended **2026-04-30** | $177.75bn | **+7.33%** | −6.8% QoQ *(same seasonality)* |

⇒ **The most current measurement of this node's customer spend is ~3.5 months old, and the two prints
landing today and tomorrow are precisely its refresh.** That — not the rate curve, not `XLP`'s β — is why
the PREMORTEM promotion of this slot was correct as a *scheduling* decision even where its reasoning about
`wflow` needed the corrections in §2. **The sector's single missing input arrives on a known date.**

⚠ **Lead/lag discipline.** No lead/lag relationship between these macro proxies and staples retail
performance was measured this run. **Any such claim is `[unverified]` and none is made here.** The only
lead/lag statements in this file that carry measurements are §2c's roll-off decomposition and §2d's β
table, both computed on settled closes to 08-18.

**One dated, primary-source fact from inside the sweep's own Δ window, and it is not a price:** on
**2026-08-14** `TGT` filed an 8-K (Items 1.01 / 1.02 / 2.03) entering a **$4.0bn unsecured five-year
revolving credit facility** expiring **2031-08-14**, upsizable by a further **$1.0bn**, and terminating the
prior **$3.0bn** facility that *"was scheduled to expire on October 18, 2028."* ⇒ **a bank syndicate
re-underwrote a 33% larger commitment more than two years early, five days before the print.**
⚠ **This is a dated fact, not a forecast.** Revolver renewals are routine corporate finance, the filing
discloses no drawn balance, and **this file makes no claim that it predicts anything about the quarter.**
It is recorded for two reasons: it sits inside the 08-14 → 08-18 Δ window and is therefore a candidate
contributor to `TGT`'s `vol_surge` moving 1.01 → 1.12; and it is **not** a guidance or M&A event, so
**it does not trip `S100`'s anti-signal** — which matters because `S100` was registered today and its
window (08-18 → 08-21) begins after it in any case.

---

## 8 · 🚨 LIVE-TAPE QUARANTINE — post-22:30 KST observations, inadmissible, recorded for the settling desk

**None of the following supports any conclusion in §1–§7.** Each carries its clock time on its own line,
per the hand-probe rule. The terminal settled bar is **2026-08-18** and stays that way.

| clock (KST) | instrument | reading | why it is quarantined |
|---|---|---|---|
| **22:52** | `module_fundamentals_us` live quote | `TGT` **$160.35** · `WMT` **$116.46** | **08-19 unsettled** |
| **22:56** | `module_flow TGT --positioning` | 🟢가속 · news velocity **2.82×** · RS20 +13.3 / RS60 +24.5 vs `SPY` · `vol_surge` 1.02 · **implied ±4.4% (D2)** · P/C 1.74 · skew +41.1 | RS figures include an unsettled bar; the **implied move has collapsed from the ±7.8% `S100` registered** — a mechanical post-event IV move that carries **no directional content** |
| **22:57** | `module_flow WMT --positioning` | 🟢가속 · velocity **1.70×** · **implied ±5.0% (D2)**, ≈ the ±5.3% registered ⇒ **`WMT`'s event risk is intact** · P/C **0.67** · skew **+0.6** | same |
| **23:03** | yfinance last bar (08-19, partial) | `TGT` 160.34 (**+5.16%** on 08-18) · `WMT` 116.58 (+1.20%) · `SPY` 769.42 (+0.257%) · `XLP` 87.04 (+1.71%) | **an incomplete intraday bar is not a close** — the desk's standing rule |
| **23:03** | ⚠ implied `S100` state | EW{`TGT`,`WMT`} raw **+3.18%** minus `SPY` **+0.257%** = **+2.92pp**, vs branch A ≥ **+6.5pp** | 🚫 **NOT a score.** `S100`'s observable is **08-18 settled close → 08-21 settled close**. This is one partial session of three and **may not be read as tracking** |
| **23:1x** | `module_news_data fts search --scope foreign --days 3 --count` | `Walmart` **195** · `Target` **2558** | 🚨 **`Target` is a common English noun** — the count is polysemy-contaminated and **may not be used as a velocity or attention figure** |
| 21:57 *(retained, pre-bell)* | PREFLIGHT hand-probe | **`TGT` velocity 2.30 — the highest of the 40 hand-re-probed names** | ✅ **admissible**: the retained hand-probe path, cited with its clock time |

⚠ **`vol_surge` note against §4**: the 22:56 KST live read puts `TGT` at **1.02**, below the 1.12 the
settled sweep carries. **A mid-session volume ratio is not comparable to a settled one** and §4's gate
arithmetic uses the settled 1.12 throughout.

---

## 9 · Dated, falsifiable KPIs — every forward statement in this file, as a testable row

**Rule S6: each row below is a `[label]`-free, dated observable measured on settled closes vs a named
benchmark. None is a signal, none carries direction, none is sized.**

| # | KPI | Threshold | Settles |
|---|---|---|---|
| 1 | **The roll-off finding, forward-tested.** EW ΔRS20 vs `SPY` across all 11 sectors on the next two-session `asof` advance, decomposed into earned vs roll-off, identical method to §2c | **Roll-off share ≥ 50% of EW ΔRS20 in ≥ 6 of 11 sectors** ⇒ §2c is a recurring property of the Δ-rule, not a one-window accident · **≤ 3 of 11** ⇒ this run was idiosyncratic and §2c does **not** generalise | **first run with a new `asof`** |
| 2 | **Does the `flow_score` LEVEL survive when the calendar stops helping?** `TGT` `flow_score` at the next `asof` | **≥ +0.60 with earned RS20 vs `SPY` ≥ 0 over the advance** ⇒ the level is money · **< +0.40** ⇒ the level was carried by the same window effect as the Δ | next `asof` |
| 3 | **`S100` (registered today, frozen, not touched here).** EW{`TGT`,`WMT`} 08-18→08-21 settled excess vs `SPY` | **A ≥ +6.5pp · B ≤ −6.5pp · C between**. ⚠ this file adds only that **the basket's β is +0.178, not the registered 0.09** (§2d), and that **A/B cannot attribute to a leg** (§5) | **2026-08-21** |
| 4 | **Is the sector label still the wrong unit?** Node RS60 spread vs `SPY` (§3) against `XLP`'s own 60-session excess vs `SPY` | **spread ≥ 3× the sector move** ⇒ §3 holds · **< 1.5×** ⇒ the nodes have converged and the GICS label has become adequate | 08-26 |
| 5 | **Is `MNST` the sector's volume, or is the volume spreading?** Count of Staples names with `vol_surge ≥ 1.2` **and** RS20 > 0 vs `SPY` | **≥ 1** ⇒ the gate opened on an accumulator and §4's reading is superseded · **0 with `MNST` still the max** ⇒ §4 holds | 08-26 |
| 6 | **The customer-spend gap (§7).** Whether a consumer-spending series (retail sales / PCE / real disposable income / saving rate) is added to the desk's FRED specification | **added** ⇒ gap closed · **absent** ⇒ the next staples DEEP inherits the same blind node and must say so | 08-26 |
| 🚨 | **Anti-signal for KPIs 1–2** | An `asof` advance of **more than 5 sessions** (the roll-off decomposition is defined for a short advance and becomes a different statistic over a long one) ⇒ **VOID** | — |
| 🚨 | **Anti-signal for KPI 4** | A GICS reclassification moving any of the 19 names between sectors, or an index add/delete inside the window ⇒ the node table is not comparable ⇒ **VOID** | — |

---

## ✅ Verdict for BET — analytical, no direction, no size (P4)

1. **`UW− → UW`: right direction, wrong reasoning, three counts.** `TGT` is invisible at 1.8% cap weight
   in every instrument the run read (§2a); "mega-cap-narrow" is a **level** statement applied to a
   **change** decision, and on the change the sector is the board's **broadest** (EW Δ **+0.1935**, 16/19
   improving, §2b); and **≥31% of the +0.325 headline Δ is 20-session base roll-off, not money** (§2c).
2. **★ §2c is the finding that should leave this file.** It is not about Staples. On 08-14 → 08-18 **nine
   of eleven sectors received a free RS20 improvement from the calendar, six of them while losing ground
   to `SPY`.** Both of today's promotions ride that instrument — **Health Care at 48% roll-off, Staples at
   77–80%** — and **Energy, which was held, is the only sector that earned its improvement (+3.75 earned,
   −0.47 roll-off vs `SPY`)**. **The Δ-rule needs an earned/roll-off split before the next promotion.**
3. **The β objection does not settle the disagreement in either direction.** `XLP`'s β-adjusted excess vs
   `SPY` is **−0.592 / −0.681 on the two windows where `SPY` fell** and **+2.006 / +1.343 on the two where
   it rose** (§2d). Flow and risk-adjusted price were never measured on the same days. And **`TGT` is the
   node's only positive-β name (+0.455, 252d vs `SPY`)**, so the defensive-β explanation is the one that
   cannot be applied to the name carrying the sector's rank.
4. **`S100` correction, thresholds untouched**: the registered basket β of **0.09** does not reproduce —
   **+0.178** on 252 daily settled returns to 08-18. **The row's β-free claim survives** (β can reach at
   most ±0.445pp of a ±6.5pp bar inside the non-VOID band); **the number quoted for it does not.**
5. **The sector label is the wrong unit by 5–16×** (§3), and the node it is a call on **inverted since
   08-17**: big-box is now the sector's best node and grocery/distribution its worst.
6. **Frame transfer answered (§6)**: vendor allowances are the **inverse** of take-or-pay — volume-
   contingent, un-sized, buried in COGS, pro-cyclical. **Membership fee income is the real analogue**, and
   **`WMT` discloses it (up to 22.6% of group operating income; Sam's Club U.S. at 103.4% of segment
   operating income) while `TGT` does not quantify its equivalent at all.** `S100` equal-weights the two.
7. **The node's customer is not measured by this desk** (§7): `M2` June, `CPI` July, `U-3` 4.1% July, and
   **no spending series in the specification at all**. The only real measure of this node's customer spend
   is issuer-disclosed revenue, ~3.5 months old — **and the two prints are its refresh.**
8. **Written under quarantine (§0, §8).** The stage ran 22 minutes after the bell, the modules re-pulled
   live prices, `TGT`'s Item 2.02 8-K is on EDGAR and `WMT`'s is not. **Every live reading is fenced into
   §8, no conclusion rests on one, and the print itself has not been read.**
