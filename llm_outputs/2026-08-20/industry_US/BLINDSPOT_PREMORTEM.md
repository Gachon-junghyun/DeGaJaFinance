# BLINDSPOT_PREMORTEM — industry_US · 2026-08-20 (Thu) · Stage 5 / L1·PREMORTEM ★US-only

> Four adversarial lenses argue **AGAINST this run's own tilt**, before the deep budget is committed.
> Draft tilt under attack: `HLTH OW · ENRG OW · STPL N · COMM N · DISC N · MATR N− · FIN N− ·
> INDU UW− · IT UW · RE UW · UTIL UW`, DEEP = **ENRG · HLTH · IT · UTIL**.
> Settled frame **2026-08-19**. Analytical only — no buy/sell, no sizing (P4).

⚠ **Execution deviation, logged (unattended-run rule).** The stage specifies a **4-agent parallel
fan-out**. This session operates under a standing instruction not to launch subagents, so **the four
lenses were executed sequentially in this context, each against its own fresh measurement** rather
than in parallel. The analytical requirement — four adversarial passes, each returning **named tickers
and dated catalysts** — is met in full; only the concurrency is different. Logged rather than silently
substituted.

⚠ **Implied-move disclosure, and it is a LIMIT not a check.** `module_flow --positioning` returned
**every** straddle at expiry **2026-08-21, `D1`**: `NVDA` ±1.9% · `AVGO` ±2.2% · `XLU` ±0.9% ·
`XLV` ±1.6% · `XLK` ±1.9% · `MPC` ±3.4% · `WMT` ±2.0% · `TGT` ±2.3% · `MRVL` ±5.3% · `COHR` ±6.1%.
A one-day straddle prices one session, so these are a **FLOOR on a multi-session implied move, not an
estimate** ⇒ **no threshold below is claimed to sit outside what is priced.** (`D295` is the standing
dig for exactly this.)

---

## ★ The pre-mortem's headline: the draft tilt survives, and its blind spot is not a sector

**All four lenses agree with the sector verdicts and all four attack the same thing: the desk is
short the label and long the sub-node, repeatedly, and its instruments only measure the label.**
Three independent instances, measured today:

| Label verdict | The sub-node the desk actually holds or that actually carries the money |
|---|---|
| **INDU UW−** (`eqflow` −0.073, 10🔴/50) | **defense** — `RTX` flow +0.617, rs20 **+10.2** / rs60 **+21.3**, OBV 매집 |
| **IT UW** (`eqflow` −0.197, 19🔴/56) | **`MSFT` exc20 +21.18 against exc60 +12.56** and **`CRM` exc20 +23.54 against exc60 +11.31** — two of the sector's largest names are in **20-day reversals whose excess EXCEEDS their own 60-day excess** |
| **COMM N** (`wflow` −0.262) | **9 of 12 names read `wflow` +0.217** ex-Alphabet, ex-`META` |

⇒ **The sector call is right and the sector is the wrong unit** in at least three of eleven buckets.
That is not a verdict change (ROTATION declined all three with numbers, correctly); it is a **DEEP
mandate and a bracket**, and Lens 1 registers the bracket.

---

## Lens 1 · UNDER-COMPUTED LEGS — the strongest bull case for something we did NOT deep-dive

**Method**: every sector without a DEEP slot, screened for (a) a dated catalyst ≤ ~5 trading days and
(b) a flow/price shape the sector aggregate hides. Earnings scan run over the 140 largest
`us_top300` names for the window 2026-08-20 → 2026-08-29.

**Dated catalysts inside the window — the full list, so an absence is legible:**

| Date | Name | Sector | flow | rs20 | rs60 |
|---|---|---|---:|---:|---:|
| 08-20 | `WMT` | Staples | +0.211 | +1.6 | −8.1 |
| 08-20 | `DE` | Industrials | −0.586 | −7.3 | +6.6 |
| 08-24 | `PDD` | Cons. Disc. | +0.492 | +5.0 | −7.7 |
| **08-27** | **`CRM`** | **IT** | **+0.644** | **+23.5** | +11.3 |
| 08-27 | `CRWD` | IT | −0.246 | +4.1 | +18.4 |
| 08-27 | `SNPS` | IT | −0.347 | +3.4 | −26.7 |
| **08-26/27** | **`NVDA`** | IT | −0.253 | −0.3 | −2.1 |
| 08-28 | `MRVL` | IT | +0.378 | +9.6 | +17.7 |

🚨 **A date discrepancy on the desk's most-bracketed binary, found here and not resolved here.**
`catalyst_calendar` and **`S79` · `S81` · `S103` · `P79`** all key `NVDA` to **2026-08-26**;
`yfinance`'s calendar returns **2026-08-27** for the same event. Both are consistent with an
after-the-close print on 08-26, but **the desk has four rows dated against one of the two readings**
and nothing reconciles them. `P79` is safe under either (it settles **08-25, pre-print, by
construction`); `S79` (settle 08-27) and `S103` (settle 08-29) are not obviously safe. **Handed to the
scoring desk as a check, not silently normalised.**

### Leg 1A — **`MSFT` · `CRM`: a 20-day reversal inside the sector we just underweighted** → **WITHIN-RUN-WATCH + bracketed**

The desk's own EXTENDED-vs-EXHAUSTED instrument (share of 60-day excess landing in the last 20
sessions) returns numbers **above 100%** for both — meaning the prior 40 sessions were *negative* and
the entire run is a fresh turn off a losing base:

| | exc20 | exc60 | exc120 | last-20 share | OBV | `vol_surge` |
|---|---:|---:|---:|---:|---|---:|
| **`MSFT`** | **+21.18** | +12.56 | +8.99 | **168.5%** | 매집 | 0.56 |
| **`CRM`** | **+23.54** | +11.31 | −8.25 | **208.1%** | 매집 | 0.96 |

`MSFT` is IT's **3rd-largest name (10.7% of the bucket)** with `flow_score` **+0.422** — inside a
sector whose aggregate is `eqflow` −0.197 with 19 reds. **The bearish IT case is real and it is not
about these two.**
**Verdict: WITHIN-RUN-WATCH, not PROMOTE-TO-DEEP** — IT already holds a DEEP slot (R1), so the leg is
routed **into that slot's mandate** rather than consuming a 5th. ⚠ Stated positively so it cannot be
lost: **DEEP-IT must answer the bull case, not only the AVGO/optical bear case.**
**Bracketed as `S106`** (below).

### Leg 1B — **`CRM` 08-27 is the window's only under-computed *dated* catalyst** → **WITHIN-RUN-WATCH**

`CRM` reports inside the window with rs20 **+23.5**, the highest of any name reporting. It is not held
and not on the shortlist (`vol_surge` 0.96 keeps it 🟡). **Filed to the miss ledger** with an
`enters-if`, so a 208%-shape reversal into its own print is not lost to the funnel.

### Leg 1C — **`T` · `VZ`: the telecom node turned, and the desk's own orphan is in it** → **bracketed**

`T` exc20 **+6.13** against exc60 **−3.70** ⇒ last-20 share **−165.9%**: a **fresh 20-day turn off a
losing base**. ⚠ **RULE D6 applied, not exempted** — OBV is 매집 here, but OBV is a C-grade axis and
**does not carry this leg alone**; the leg rests on the **price decomposition above** (exc20 vs exc60,
both measured against `SPY`) and on the node's **`eqflow` +0.404**, with OBV as the third, weakest
corroborant. **`T` is 9.74% of the real book's invested capital and has had no bracket, no card and no
cycle label for three consecutive runs** — the standing carry says so in those words. **This lens
closes that gap with a falsifiable row: `S107`.**

### Legs examined and NOT promoted, each with its number

| Leg | Why not |
|---|---|
| **Staples / `WMT` 08-20** | The print is **inside this run's clock and outside its settled frame** (`G0`). `S100` already brackets `EW{WMT,TGT}` and settles 08-21. **Bracketing it again would be double-counting one observation** |
| **`DE` 08-20 (Industrials)** | flow **−0.586**, rs20 −7.3, and `DE` is the machinery sub-node `M720` measured as INDU's **worst** leg (−1.45 EW rs60 vs defense +10.47). A bull case cannot be constructed from these numbers |
| **`PDD` 08-24 (DISC)** | flow +0.492 with rs60 **−7.7**; DISC's whole +1.038 excess is **beta** (β 1.178). No sub-node case |
| **`CRWD` · `SNPS` 08-27** | `CRWD` flow −0.246 (its own ledger recheck is 09-02); `SNPS` rs60 **−26.7**. Neither supports a bull case today |
| **Financials** | ★ **The strongest un-slotted mandate on the board** (`M40` inverted: `eqflow` −0.127 now **below** `wflow` −0.009; last DEEP **08-14 = least recent**) — **but it has no dated catalyst in the window**, and this lens promotes on catalysts. **Logged, not promoted** |

**Lens 1 verdict: no 5th DEEP.** Two legs bracketed (`S106`, `S107`), one routed into DEEP-IT's
mandate, one filed to the miss ledger, five declined with numbers.

---

## Lens 2 · REGIME-FLIP / BOTH-SIDES — the against-us branch for every known binary

**Binaries on `CATALYST_WATCH`**: `NVDA` earnings **08-26** (D-6) · July PCE **08-28** (D-8) ·
Iran "Strait of Hormuz open" statement (**undated**, 19th run).
**No binary lands ≤48h from this run**, so the protocol's mandatory-bracket rule does not trigger on a
clock. It triggers on a **gap**, and there is one.

### 2A — 🚨 **July PCE (08-28) has NO bracket anywhere on the board** → **`S104` registered**

MACRO §6 handed it over explicitly. It is the window's only *dated macro* binary and the desk's
§A-1 finding makes it genuinely two-sided: **the entire 60-observation rise in `DGS10` (+0.140) is
real yield (`DFII10` +0.230) against FALLING inflation compensation (`T10YIE` −0.100)**. A PCE print
is the direct test of which leg is doing the work.

**Against-us branch, spelled out**: if PCE reprices **breakeven** rather than real yield, then the
desk's whole *"this is a real-rate/term-premium repricing"* frame — which underwrites the UTIL/RE
underweights and MACRO `P77`/`P78` — is measuring the wrong variable. **What rips**: inflation-levered
names, `XLE` (already OW, so the desk is not hurt) and gold; **what gets hit**: nothing the desk is
long, which is itself the finding — **the desk's OWs are not exposed to the against-us branch**, and
the row is registered anyway because the *frame* is what would break, not the P&L.

### 2B — `NVDA` 08-26: already bracketed three ways, and this lens declines to add a fourth

`S79` (the name) · `S81` (the readthrough, deliberately excluding `NVDA`) · `S103` (the cycle).
**Information-content grading (B4): a fourth row would be redundant** — no branch of a fourth bracket
could change a conclusion that `S79`/`S81`/`S103` do not already own. **Bracket declined and the
reason stated**, per the stage's own rule that a no-information event is not worth bracketing.
⚠ **But two obligations are re-stated because they are unmet**: `D295` requires `S103`'s hand-set
±5.0pp bands to be **re-derived from an 08-26-or-later straddle before the print** — the readable chain
still expires **08-21** — and the 08-26/08-27 date discrepancy (Lens 1) must be reconciled first.

### 2C — 🚨 The against-us branch nobody has bracketed: **`AVGO` displacement** → **`S105` registered**

**This is the lens's most important finding and it concerns a held name.** On 08-19 Google took a
warrant for up to **59m `MRVL` shares (~$12.2bn)** with a chip deal; `MRVL` **+9.85%**, `AVGO`
**−4.61%** the same session (Barron's carries the readthrough in its title). `AVGO` is held in **both**
books, is the **only book name tagged 🔴**, and its standing thesis line still reads *"a separate boat
from memory — hyperscaler capex is their driver."*

**What rips if the against-us branch is right**: `MRVL` (not held), `ALAB`-class custom-silicon
challengers, and the hyperscalers themselves (input cost down). **Which of our positions gets hit**:
`AVGO` directly (7.4% of the IT bucket, held), and **`ANET` indirectly** — same customer, one hop.
**Trigger + invalidation are in `S105`.**

### 2D — Hormuz: **undated for a 19th run**, and the correlated-tail flag

`S8` remains unscoreable (18th consecutive run at HANDOVER's count; a human must `VOID` it or date it —
P5). `S92`/`S95` cover the expiry. ★ **The tail flag that matters here**: EVENT_ALPHA Cards 1 and 7
(Russian refining capacity; Iran economic warfare) **share their entire exposure map — `MPC`, `PSX`,
`VLO`** ⇒ **one risk unit, not two legs**, and **ENRG's continuous DEEP slot rests on both.** If the
Iran thread resolves benignly *and* the Russian refining constraint eases, **the OW loses both its
legs at once.** Registered as a note on `P80`, not as a new row.

### 2E — Correlated-UW check (the 2026-07-15 field note)

**Run and it fires.** `UTIL UW` + `RE UW` are the field note's exact pattern: **both are bottom-two on
`eqflow` (−0.545, −0.252) and BOTH rallied on price** (`XLU` +0.855, `XLRE` +1.568 exc5). If they are
one bet, the desk is short one thing twice and its instruments disagree with the tape on both.
**MACRO `P78` brackets precisely this** (dispersion across the four legs, settle 08-26) and **DEEP-UTIL
(R2) is mandated to resolve it.** No new row — a fourth bracket on the same object would be the
"correlated tail counted twice" error this lens exists to catch.

---

## Lens 3 · MOMENTUM-CONTINUATION — "already ran" is not a verdict; re-tag every runner

**Instrument**: share of the 60-day excess vs `SPY` that landed in the **last 20 sessions**. A low
share means the run is broad-based; a high share means the name *is* the last month. All settled
2026-08-19, paired with the flow instruments so a single axis cannot carry a tag (`D6`).

| Name | exc20 | exc60 | exc120 | last-20 share | OBV · surge | **Re-tag** | Flip condition |
|---|---:|---:|---:|---:|---|---|---|
| **`HPE`** (held) | +7.49 | +38.24 | **+143.37** | **19.6%** | 매집 · 0.84 | ★ **EXTENDED-BUT-LIVE** | last-20 share > 60% **or** OBV → 분산 |
| **`ANET`** (held) | +3.73 | +17.91 | +31.58 | **20.8%** | 매집 · 0.82 | **EXTENDED-BUT-LIVE** | same |
| **`VLO`** | +8.47 | +37.07 | +58.34 | **22.8%** | 매집 · 0.68 | **EXTENDED-BUT-LIVE** | `P80` branch B |
| **`MPC`** (held) | +11.33 | +38.52 | +67.84 | **29.4%** | 매집 · 1.00 | **EXTENDED-BUT-LIVE** | `P80` branch B |
| **`PSX`** (held) | +11.71 | +33.21 | +47.35 | **35.3%** | 매집 · 1.03 | **EXTENDED-BUT-LIVE** | `P80` branch B |
| **`TMO`** | +13.64 | +33.72 | +6.39 | 40.5% | 매집 · 0.64 | **EXTENDED-BUT-LIVE** | exc120 is only +6.39 ⇒ the 60-day run is the whole story; flip if exc20 turns negative |
| **`RTX`** (held) | +10.17 | +21.34 | **−0.07** | 47.7% | 매집 · 0.91 | **EXTENDED-BUT-LIVE**, with a caveat | ⚠ **exc120 is −0.07 = exactly flat**: the defense re-rate is **entirely a 60-day event** on a 120-day base of zero. Flip: rs20 vs `SPY` negative while A&D stays positive (`S97`) |
| **`TGT`** | +12.39 | +23.45 | +26.94 | 52.8% | 매집 · **1.27** | **EXTENDED-BUT-LIVE**, gated | ⚠ Gate is **quality of earnings**, not momentum: **$1.65/share of the beat is a tariff refund** |
| **`MRVL`** | +9.56 | +17.71 | **+187.67** | 54.0% | 매집 · 0.69 | ⚠ **EXTENDED, positioning-flagged** | short **4.8% float and BUILDING**, DTC 1.4 ⇒ part of +9.85% is squeeze. Flip: short-z falls below 0 while price holds ⇒ genuine re-rate |
| **`NUE`** (held) | +2.55 | +4.07 | +30.07 | 62.5% | 매집 · 1.05 | ⚠ **EXHAUSTED-LEANING** | The run is 120-day, the 60-day is +4.07, and it carries **the sheet's only 🔴 FINRA axis** (z +1.99) |
| **`AMGN`** | +17.95 | +27.23 | +5.04 | **65.9%** | 매집 · 0.92 | **MOMENTUM-ONLY, hard-stamp** | exc120 **+5.04** ⇒ two-thirds of the 60-day run is 20 days old on a flat base |
| **`AVGO`** (held) | **−11.55** | **−15.61** | +1.11 | 74.0% | **분산** · 1.00 | 🚨 **EXHAUSTED — and now with a named cause** (`S105`) | Flip: exc20 positive **and** an AI-ASIC revenue raise on its next print |
| **`MRK`** | +16.50 | +21.20 | +16.01 | **77.9%** | 매집 · **1.28** | **MOMENTUM-ONLY, hard-stamp** | The trial result is one day old; flip if exc20 halves while `theme_age "cancer vaccine"` stays >2× |
| **`KKR`** | +12.73 | +14.32 | +6.42 | **88.9%** | 매집 · **1.20** | **MOMENTUM-ONLY, hard-stamp** | Board's highest `flow_score` (+0.778) sits on a 20-day move |
| **`REGN`** | +26.23 | +28.47 | **−2.48** | **92.1%** | 매집 · 0.72 | **MOMENTUM-ONLY, hard-stamp** | exc120 **negative** ⇒ the entire run is 20 sessions old |
| **`MSFT`** | +21.18 | +12.56 | +8.99 | **168.5%** | 매집 · 0.56 | ★ **REVERSAL, not continuation** | see Lens 1A / `S106` |
| **`CRM`** | +23.54 | +11.31 | −8.25 | **208.1%** | 매집 · 0.96 | ★ **REVERSAL, not continuation** | prints 08-27 |
| **`T`** (held) | +6.13 | −3.70 | −20.09 | **−165.9%** | 매집 · 0.46 | ★ **REVERSAL off a losing base** | `S107` |
| **`MU`** | −5.23 | +21.64 | **+113.93** | −24.2% | 중립 · 0.68 | **EXHAUSTED** | the 120-day runner has rolled over on 20 days |
| **`COHR`** · **`LITE`** (real book) | −10.81 / −3.15 | −27.00 / −15.74 | +3.35 / +10.67 | 40.0% / 20.0% | 중립 / 매집 | 🚨 **EXHAUSTED** (`COHR`) · **contested** (`LITE`, OBV still 매집 while price falls) | `S96` settles 08-21 |

★ **The lens's substantive correction to the draft tilt**: the desk's **five best-looking runners on
`flow_score` — `MRK` 77.9% · `KKR` 88.9% · `REGN` 92.1% · `AMGN` 65.9% · `TGT` 52.8% — are all
last-20-concentrated**, while its **held refiners and AI-hardware names (19.6–35.3%) are the broad
ones.** The board's *newest* money is in Health Care and its *oldest* is in Energy and AI-hardware.
**Nothing here changes a sector verdict; it changes which names inside them are extended.**
⚠ `D6`: OBV is a C-grade axis and is never the sole carrier of a tag above — every row pairs it with a
price decomposition.

---

## Lens 4 · CYCLE-EXPOSURE — registry vs coverage vs the REAL book

`../CYCLE_EXPOSURE.md`, real KIS book (read-only), 12 names, `total ≈ $11,075 · invested $6,905`:

| Cycle | rank | epicentre % | floor | any-layer % | held epicentre | GAP |
|---|---:|---:|---:|---:|---|---|
| AI-compute / semiconductors | 1 | **19.78%** | 12.0% | 23.56% | `AVGO` `NVDA` `ANET` | ✅ |
| Energy / oil-refining | 2 | **9.89%** | 8.0% | 9.89% | `MPC` `PSX` | ✅ |
| Missile-defense / rearmament | 3 | 5.89% | **—** | 5.89% | `RTX` | ⚪ **n/a** |

**Verdict: no top-rank cycle GAP.** ✅ And **no 5th DEEP is owed on a GAP**, which is stated because an
absent flag and an unmeasurable one look identical in the artifact.

**Three things the ✅ does not say, all re-confirmed today:**
1. **`M731` — the registry misses 5 of the real book's 12 names** (`LITE` `COHR` `HPE` `T` `NUE`) ⇒
   "any-layer 23.56%" is an **under-count**. Under-counting can only fail to raise a flag, so **the
   verdict is safe and the printed percentage is not.**
2. **Rank-3 has no floor, so it cannot fail.** ⚪ n/a is not a pass. `RTX` at 5.89% would breach an
   8% floor if one existed — and Lens 3 just stamped `RTX`'s exc120 at **−0.07**.
3. **There is still no registry row for optical/interconnect**, which is where **two real-book
   holdings** (`LITE`, `COHR`) live. Their exposure is **unmeasurable, not zero** (`D250`, `S94`
   settles 08-31). Registry maintenance is a **human** item (P5).

★ **The epicentre ✅ and the tape disagree, and the lens says so**: AI-compute exposure is **above its
floor at 19.78%** while `EW{AVGO,ANET,HPE,COHR,LITE}` exc5 sits at the **0.8th percentile of 252
observations**. **The GAP check is a floor on ownership; it is silent on whether owning it is
working** — that is `P79`'s job, and `P79` settles **08-25, one session before the `NVDA` print, by
construction.**

**Cleanest epicentre expressions, named as the lens requires** (analysis, not advice, P4): within
AI-compute the only names carrying **positive rs60 with OBV 매집** are `ANET` (+17.9) and `HPE`
(+38.2); `AVGO` (−15.6, 분산) and `NVDA` (−2.1, 중립) do not. Within Energy the epicentre expressions
are `MPC` (+38.5) and `PSX` (+33.2), both 매집, with `VLO` (+37.1) the un-held equivalent.

---

## §Brackets registered this run — **4 new rows, all two-sided**

★ **ID 3-grep at WRITE time** (`D137`/`D76`): `S104` `S105` `S106` `S107` returned **0 hits** across
`handoff/SCENARIOS*.md` ×3, `handoff/STANDING_VIEW*.md` ×3, `handoff/RESEARCH.md`, and all of
`llm_outputs/2026-08-*/`. Highest existing: **`S103` (US) / `S66-KR` (KR)**.
★ **Every band measured on the estimator's own trailing-252 distribution (`D93`) BEFORE freezing.**
Full text is written to `handoff/SCENARIOS_US.md`; the MASTER INDEX rows go to the `SCENARIOS.md`
spine.

| ID | Question | Observable (frozen) | A | B | C | Settles |
|---|---|---|---|---|---|---|
| **`S104`** | July PCE: does the print move **inflation compensation** or **real yield**? | `T10YIE` change from the 08-27 close to the first `[FRED]` close covering **08-31**, in bp | **≥ +3.0** — breakeven repricing ⇒ **the desk's "it is all real yield" frame is measuring the wrong variable** | **≤ −3.0** — compensation falls again ⇒ the frame survives and strengthens | between | **2026-08-31** |
| **`S105`** | Is Google→`MRVL` a **structural displacement** of a held name? | `[MRVL` 10-session excess vs `SPY]` **−** `[AVGO` 10-session excess vs `SPY]` | **≤ −10.84** (252d p15) — the spread reverses ⇒ **one warrant, one week, no displacement** | **≥ +30.48** (252d p95) — the spread extends ⇒ **displacement, and `AVGO`'s thesis line must be rewritten** | between | **2026-09-03** |
| **`S106`** | Is the IT underweight wrong about its **largest reversal**? | `MSFT` 10-session excess vs `SPY` | **≥ +7.97** (252d p95) — the reversal extends ⇒ **the IT UW is a sub-node call wearing a sector label** | **≤ −9.18** (252d p05) — it rolls over ⇒ the sector call covers it and the 168.5% shape was noise | between | **2026-09-03** |
| **`S107`** | The `T` orphan: is the telecom turn real? | `EW{T, VZ}` 10-session excess vs `SPY` | **≥ +12.24** (252d p95) — the turn extends ⇒ **a 9.74%-of-invested position has a live thesis and the residual really was a LABEL** | **≤ −9.53** (252d p05) — it reverses ⇒ the orphan is an orphan on price too | between | **2026-09-03** |

**Registration state and information grading, disclosed up front rather than at scoring:**

- **`S104`** — state at registration: `T10YIE` **2.300** (08-19). Estimator's own 2-obs change
  distribution: **mean −0.07bp · sd 2.60 · p10 −3.0 · p50 0.0 · p90 +3.0** ⇒ bands are **p10/p90**,
  **A ≈10% · B ≈10% · C ≈80%.** **Information content: HIGH and asymmetric** — branch A would
  invalidate the frame under `P77`, `P78` and two sector underweights; branch B only confirms.
  🚨 **Anti-signal (VOID)**: a **Treasury refunding announcement, a further buyback-size change, or an
  intermeeting Fed action** inside 08-27 → 08-31 ⇒ the move is not the print. ⚠ **Reachability-checked
  and it is LIVE**: Treasury changed buyback sizes on **08-19**, i.e. this exact anti-signal fired
  inside another row's window nine days ago. Registered anyway, with that stated.
- **`S105`** — state at registration: **+25.780 = the 93.7th percentile** of 252 observations
  (mean +3.944, sd 15.753). ⚠⚠ **The spread is ALREADY near branch B. Disclosed at registration, not
  discovered at scoring — branch A is the adversarial ask**, and a scorer must not read a B-fire as a
  surprise. **Information content: HIGH** — branch B forces a rewrite of a held name's thesis;
  branch A retires this run's headline finding. 🚨 **Anti-signal (VOID)**: `MRVL`'s **08-28 earnings
  print falls inside the window** ⇒ ⚠ **this is disclosed as a known contaminant, not a VOID**: the
  row deliberately settles **09-03, after the print**, because a displacement thesis that cannot
  survive the challenger's own guide is not a displacement thesis. **`AVGO` has no print in the
  window** (next 2026-09-04, checked). A **change of control or an M&A announcement at either name**
  ⇒ VOID.
- **`S106`** — state at registration: **−0.551 = the 56.7th percentile** (mean −0.756, sd 6.275) ⇒
  **inside C, essentially at its median.** The 20-day shape is in `exc20`, **not** in `exc10`, which
  is the honest reason the bands are wide. **Information content: MEDIUM** — A changes how the desk
  writes sector calls; C is modal and teaches least. 🚨 **Anti-signal (VOID)**: an `MSFT` acquisition,
  guidance withdrawal, or an antitrust ruling inside the window. `MSFT` has **no earnings print**
  inside it (checked).
- **`S107`** — state at registration: **+7.671 = the 92.9th percentile** (mean −0.722, sd 6.570) ⇒
  ⚠ **already above p85 and approaching branch A. Disclosed.** **Branch B is the adversarial ask.**
  **Information content: HIGH for the book specifically** — this is the first falsifiable statement
  ever registered about a position that is **9.74% of invested capital**, and either branch resolves
  a three-run open residual. 🚨 **Anti-signal (VOID)**: a dividend-policy change, an M&A announcement,
  or a spectrum-auction result at either name inside the window.

---

## §Hand-offs

| To | What |
|---|---|
| **DEEP** | Final set **unchanged: ENRG · HLTH · IT · UTIL. No 5th slot promoted** — Lens 1's legs are routed into DEEP-IT's mandate and into brackets instead. ★ **DEEP-IT's mandate is now two-sided by instruction**: the `AVGO`/optical bear case **and** the `MSFT`/`CRM` reversal bull case. ★ **DEEP-UTIL owns the price-vs-flow contradiction and `P78`/2E's correlated-UW question.** |
| **ALPHA (action bracket)** | `S104` `S105` `S106` `S107` + the standing `D295` obligation on `S103` + the **`NVDA` 08-26 vs 08-27 date reconciliation** |
| **BET** | **No epicentre-starter is owed** — `CYCLE_EXPOSURE` shows no rank≤2 GAP. Lens 3's re-tags travel with the names: five `MOMENTUM-ONLY` hard-stamps (`MRK` `KKR` `REGN` `AMGN` `TGT`), one `EXHAUSTED` held name with a named cause (`AVGO`), one `EXHAUSTED-LEANING` held name with a 🔴 positioning axis (`NUE`) |
| **The book desk** | `AVGO`'s standing thesis line is **inverted, not stale** — flagged in EVENT_ALPHA §Book cross-check and now bracketed (`S105`) |
| **Miss ledger** | `CRM` filed (`Q.확신부족`) with an `enters-if` — the window's only under-computed dated catalyst that did not become a candidate |

---

## ✅ EXIT CHECK — self-audit

- ✅ **4 lenses run, each on its own fresh measurement**, each returning **named tickers and dated
  catalysts** (execution deviation from the parallel fan-out logged at the top, not hidden).
- ✅ **Every bracket names observable + frozen threshold + date and carries BOTH branches.** Four new
  rows, zero one-way. Registered in `handoff/SCENARIOS_US.md` and indexed in the `SCENARIOS.md` spine.
- ✅ **Every magnitude threshold stated against the implied move** — and the disclosure is that **all
  available straddles are `D1` (08-21)**, i.e. a **floor, not an estimate**, so **no threshold is
  claimed to sit outside what is priced.**
- ✅ **Each branch graded by information content before the event** (HIGH ×3, MEDIUM ×1), and **one
  binary was DROPPED with that reason stated**: a fourth `NVDA` bracket, because no branch of it could
  change a conclusion `S79`/`S81`/`S103` do not already own.
- ✅ Every catalyst-bearing leg promoted or logged: 2 bracketed, 1 routed into DEEP-IT, 1 to the miss
  ledger, 5 declined with numbers. **None silently dropped.**
- ✅ Momentum re-tags issued for **21 names** with an explicit flip condition each, and **no tag rests
  on OBV alone** (`D6`).
- ✅ Cycle-GAP read: **none** — with all three caveats (under-count, absent rank-3 floor, missing
  optical row) re-stated rather than inherited silently.
- ✅ **Correlated-UW check run and it FIRED** (UTIL+RE), routed to `P78` and DEEP-UTIL rather than
  double-bracketed. **Correlated-tail flag on ENRG's two cards (`MPC`/`PSX`/`VLO` = one risk unit)
  carried to `P80`.**
- ✅ **DEEP set stated and unchanged: ENRG · HLTH · IT · UTIL (N=4/4, no 5th).**
