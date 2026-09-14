# SECTOR_DEEP_FIN — Financials — industry_US — 2026-07-29 (Wed) · CONTINUOUS-TRACK → **DELTA-LED**

> Continuous slot (5th consecutive run). Structure carried by reference to
> `llm_outputs/2026-07-28/industry_US/SECTOR_DEEP_FIN.md`. All flow/RS **settled 2026-07-28**.
> Benchmark **SPY** inline (C1). Zero buy/sell language (P4).

## 1 · THE DELTA — the breadth claim shrank, and it shrank because BRK-B did

**ROTATION carried Financials as the only sector where breadth exceeds cap-weight and both are
positive: eqflow +0.374 > wflow +0.294, gap +0.080.** Re-decomposed this run **from all 47 rows**
(the re-measurement M173 demanded and the 07-28 run did not perform):

```
ALL 47      wflow +0.294   eqflow +0.374   gap +0.080
ex-BRK-B    wflow +0.339   eqflow +0.382   gap +0.043
```

★ **BRK-B alone is $1,055.7bn = 13.94% of sector cap at a flow score of +0.016, and removing it
halves the breadth gap (+0.080 → +0.043).** ⇒ **46% of "the board's only breadth-led sector" is one
holding company sitting inert at the top of the cap table.** **M173 replicates** (it measured 56% on
07-27) — **the finding is unchanged in kind and smaller in degree.**
⚠ **What survives is real**: ex-BRK the gap is still positive and the cap-weighted flow is *higher*
(+0.339), so the sector is not mega-cap-narrow. **What does not survive is the word "only".**

## 2 · Sub-node decomposition (C5 — the grouping is stated, and it is arbitrary)

| Node | n | wflow | eqflow | 🟢 | Read |
|---|---|---|---|---|---|
| **Payments + insurance** | 15 | **+0.480** | **+0.540** | 1 (CB) | ★ **1.6× the sector's own eqflow. The strongest node for a 4th run** |
| **Banks** | 9 | +0.326 | +0.222 | **0** | ⚠ **wflow > eqflow ⇒ mega-cap-led (JPM +0.578, BAC +0.633 carry it). ZERO greens in nine names** |
| **Capital markets / alt-managers** | 10 | +0.104 | +0.200 | 1 (**BX**) | **GS RS20 +1.3 / RS60 +8.8 vs SPY on flow −0.357 (A-grade first; OBV 분산 only corroborates, D6) · MS RS20 0.0 on −0.145** — the de-rate cohort is intact and GS has deteriorated from −0.071 (07-25) |
| **Exchanges + ratings + other** | 13 | +0.210 | +0.420 | 0 | breadth-led, and see §4 |

⚠ **Two greens in a 47-name sector.** A sector carried at OW− on breadth has **4.3% of its names
tagged 🟢**, and the tag mechanism is the one SWEEP measured broken this run — **30 of the 32 names
that pass `OBV-매집 ∧ RS20>0` are blocked by `vol_surge` alone.** ⇒ **the 🟢 count is not the breadth
evidence; the eqflow number is, and it is 46% one holdco.**

## 3 · ★★ BX — HANDOVER's ranked first-claim, resolved at the flow/valuation level and NOT at the thesis level

**Why it was first-claim**: Financials' **#1 flow score** for a second run, appearing in **no carried
thesis**, with **no 4Phase**, and it was **ranked #1 by the 07-28 run** and left open.

**Measured this run** `[SECTOR_FLOW_US.json asof 07-28 · module_fundamentals_us · module_disclosure_us
· us_flow FINRA 07-28]`:

| Axis | Reading |
|---|---|
| Flow | **🟢가속 +0.783, `new_green`, `vol_surge` 1.21 = a VOLUME path** (not a velocity path — `velocity` is null on 300/300 today) |
| Price (A-grade) | **RS20 +16.6 / RS60 +3.5 vs SPY** — positive on both windows |
| Positioning | FINRA short-vol **z −0.71, 5v5 −0.7▼**, base 20d in-band ⇒ **readable, and neutral-to-covering** |
| Valuation | Trailing P/E 29.08 · **Forward P/E 17.39** · PEG 1.56 · **P/B 11.53** · dividend 3.94% |
| Consensus | mean target **$141.95 = +9.2% upside**; 3 Strong Buy / 9 Buy / 11 Hold / **0 Sell** |
| **Estimate momentum** | ⚠ **current-year +0.9%/90d · next-year −1.1%/90d — a FLAT-to-DECLINING book.** The quarterly 90-day columns read 0.00 = **a data gap, left `unknown` (C3), not read as a collapse** |
| **Filings, 90 days** | 19 total: **2 8-Ks, and NEITHER is an Item 2.02 or a 수주/계약/M&A.** 9 Form 4s, 1 10-Q |

★★ **The differentiator, and it is the reason this name is not the same finding as §5's Industrials
four**: **BX's ignition has NO earnings event under it.** Its two 8-Ks carry no Item 2.02, so the
`new_green` cannot be an 8-K footprint — the **C-B / D51 pattern that explains four of this run's
other greens does not apply here.**

⚠⚠ **And the thesis gap is NOT closed.** **No 4Phase exists, so under the carried rule no thesis may
be built on it**, and the fundamental axis actively cuts the other way: **a flat-to-declining revision
book at 17.4× forward and 11.5× book.** ⇒ **Verdict: the coverage gap is closed at the flow and
valuation level; the thesis gap stands, and BX is handed to BET as a NAMED coverage item with a
stated prohibition, not as a candidate.** ⚠ **P/B 11.5 with a −1.1% next-year revision is exactly the
shape L2 punishes — but L2 needs a margin percentile, and an alternative-asset manager has no
comparable gross-margin series, so this is left `unknown` (C3) rather than asserted.**

## 4 · The exchanges node — its replacement observable moved 0.04pp in a settled session

**The registered replacement observable** (after M135 proved the original RS60 test **BROKEN**, not
passed): equal-weight excess of **{NDAQ, SPGI, ICE, CME, MCO, MSCI, COIN} vs SPY, 2026-07-24 → 08-07.**

**Read on settled closes 07-24 → 07-28: +3.206pp**, against **+3.17pp** at 07-27.
⇒ **one more settled session moved it +0.04pp. Tracking, NOT scored — the window runs to 08-07.**
Per-name excess over the same two sessions: **COIN +5.81 · MSCI +4.93 · ICE +4.49 · NDAQ +3.94 ·
MCO +2.43 · CME +1.58 · SPGI −0.74.**

★ **M137's revenue-engine split (C5) holds on the 20/60-day windows**: **ICE +24.3 / −6.5 ·
NDAQ +24.9 / +1.3 · CME +19.0 / −12.8 · COIN +10.7 / −13.7 are PURE last-20 events**, while
**SPGI +9.8 / +0.9 and MCO +7.0 / +1.8 are the only two positive on both** — the ratings pair again.
⚠ **SPGI is still the node's inversion**: the one name near RS60 ≈ 0 and **the only negative over the
replacement observable's own window (−0.74)**.

## 5 · S23 is the closest it has been, and it moved TOWARD the trigger

`[FRED]` **T10Y2Y +0.34 (07-27), flattened 2bp from +0.36; DGS2 4.31%, inside the registered
4.15–4.45% band.** **S23-B's threshold is ≤ +0.20 by 2026-08-05 ⇒ 0.14pp away, and this print moved
toward it.**
⇒ **The branch that kills NIM without tripping S19 or S9 is live**, and **S19's branch M
("no conclusion changes") remains a false null for this OW** — which is the whole reason S23 was
written. ⚠ **The steepener leg broke on 2026-07-23 (R11) and has not been rebuilt**; the OW stands on
breadth alone, and §1 has just measured that breadth to be 46% one holdco.

**NII, carried, not re-derived (M138)**: **WFC held FY26 NII ~\$50bn and missed at \$12.32bn**, its CFO
naming interest-bearing deposit mix; **JPM RAISED to ~\$105.5bn on markets-related NII.** ⇒ a
bear-flattener hits the spread half WFC just guided flat and **leaves the half belonging to
GS/MS/SCHW/IBKR** — the same names carrying the de-rate.

## 6 · Dispersion (W5)

RS20 vs SPY inside Financials spans **NDAQ +24.9 to GS +1.3 = 23.6pp**, against a sector 5-day move of
**+2.66%**. **The spread exceeds the sector's own move by ~9×** ⇒ **the label is the wrong unit, and
this file says so.** The three internally coherent units, on this run's numbers:
**{payments + insurance} +0.540 eqflow** · **{banks} 0 greens, mega-cap-led** · **{exchanges/ratings}
a last-20 re-rate with a two-name ratings exception.**

**Internal hedge, carried (M147/S26)**: **CB (β 0.125) and TRV (β 0.339)** sit inside this OW and are
on **S26/S41's rips-on-B list** — the only tilt on the board carrying an internal hedge its label
hides. **CB is the sector's only volume-path green** (🟢, `vol_surge` 1.42, RS20 +5.9 / RS60 +8.1);
**TRV is 🟡 at +0.75 with `vol_surge` 1.15 and RS20 +19.7 / RS60 +27.1** — ⚠ and **M150 measured 98.6%
of TRV's 60-day excess in its last 20 sessions**, the R9/AXON geometry, which PREMORTEM Lens 3 re-tagged
**EXTENDED-BUT-LIVE** rather than exhausted.

## 7 · Track KPIs and anti-signals

| # | Observable | Now | Kills / resolves at |
|---|---|---|---|
| 1 | **T10Y2Y with DGS2 alongside (S23)** | **+0.34 / 4.31%** | **≤ +0.20 by 08-05** ⇒ branch B, both remaining legs hit |
| 2 | eqflow − wflow **ex-BRK-B** | **+0.043** | ≤ 0 ⇒ the breadth claim is gone entirely |
| 3 | Exchanges EW excess vs SPY (07-24→08-07) | **+3.21pp** | the registered window closes **08-07**; **4 of 7 do not print inside it** — a defect recorded at registration |
| 4 | **{MA, V, PYPL} RS20 vs SPY (S14)** and the pre-registered **{MA, V}-only** reading | MA +10.6 · V +7.3 | **scored 2026-08-06 exactly as frozen, PYPL contamination included** |
| 5 | **IG OAS with HY OAS alongside (S41, registered this run)** | **0.81% / 2.81%** | IG ≥0.90% by 08-12 ⇒ the AI-credit channel transmitted |
| 6 | GS/MS de-rate | GS **−0.357, OBV 분산** | a positive flow print with RS20 > 0 ⇒ the cohort is over |

**Dated catalysts**: **FOMC 07-29 14:00 ET (S9/S19/S23)** · **V 07-29 AMC** (⚠ **option P/C OI 5.90,
the heaviest put positioning on the board, accounted for by no bracket — logged in the DROPPED table**)
· **MA 07-30** (implied **±3.5%** against S14-num's frozen **±3.9%**, **not re-frozen**; any move
inside ±3.9% is **pre-declared no-information**) · **PCE 07-30 (S15)**.

## ✅ EXIT CHECK
- [x] Continuous-track file **LED with the delta** (the ex-BRK re-decomposition M173 demanded).
- [x] flow → players → primary/filings → sub-node map → bottleneck/KPI/anti-signal present.
- [x] ROTATION's divergence resolved: the breadth claim is **halved by one name** and the surviving
      form is stated.
- [x] **No cheapness claim is made on any name.** BX's forward 17.4× is quoted **next to its
      flat-to-declining revision book**, and its margin percentile is left `unknown` (C3) because an
      alt-manager has no comparable gross-margin series.
- [x] Customers/counterparties: the payments node's customer is the consumer, and **S14's registered
      observable settles it 08-06**; the banks' NII driver is carried with its primary quotes (M138).
- [x] **No lead/lag claim made or inherited.**
- [x] Dispersion stated (**23.6pp RS20 range against a +2.66% sector move**) with the explicit
      statement that the label is the wrong unit.
