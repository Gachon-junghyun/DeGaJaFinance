# SECTOR_DEEP_INDU — Industrials — industry_US — 2026-08-05 (Wed) · CONTINUOUS, newly-promoted leg

> Last covered 2026-08-02: that file found ETN had **no base** (rs60 −2.2) and excluded it from
> breadth. Three sessions later ROTATION promoted INDU **N → OW−** on breadth carried by
> **ETN·EMR·AME·PWR** — same names, still no base, now the majority of the promote. **Delta**: the
> prior file's ETN skepticism was right and is now the mandate for the whole cluster. Flow/RS
> **`asof 2026-08-04 settled`**. Benchmark **SPY** inline (C1). Zero buy/sell, zero sizing (P4).

---

## §0 · One-line answer

**Both readings are live: on the price test alone this is indistinguishable from an ignition's first
20 days, but the money that would separate the two is bid only at the switchgear/automation node
(ETN·EMR·AME) and absent at the turbine node (GEV) and the data-centre-integration node (VRT) — so
the desk should read this as a repair confirming unevenly, not a chain-wide ignition, with PWR on
neither side cleanly.**

## §1 · The segment test, reproduced independently

`yfinance`, `auto_adjust=False`, one source, benchmark **SPY** inline, closes trimmed to
**≤ 2026-08-04** (US market is open now; last common bar for every name below is 2026-08-04, verified).
`Segment_21_60 = (close[-21]/close[-61]-1) − (SPY[-21]/SPY[-61]-1)`, points.

| Ticker | RS20 vs SPY | RS60 vs SPY | **segment 21–60** | Note |
|---|---|---|---|---|
| EMR | +12.0 | +7.1 | **−4.5** | matches PREMORTEM Lens 3 exactly |
| ETN | +9.2 | +6.0 | **−3.1** | matches |
| AME | +6.5 | +2.8 | **−3.5** | matches |
| PWR | +2.4 | −13.1 | **−14.7** | matches, worst of the four |
| ROK | −8.2 | −6.2 | **+2.3** | 🟡 laggard, only positive prior-40 base in the node |
| VRT | −14.8 | −26.0 | **−12.3** | negative on both windows — a decline, not a repair |
| GEV | −8.6 | −8.0 | **+0.8** | flat prior-40, still declining now |
| TRI | +17.1 | +11.5 | **−5.0** | INDU's other new-ish green, same repair shape |
| Defense median (RTX·GD·LMT·NOC·LHX) | — | — | **+2.3** | real base, wide dispersion (+11.4 to −4.1) |
| Rails median (UNP·NSC·CSX) | — | — | **+4.7** | real base, tight |

The independent pull reproduces the JSON's RS20/RS60 to one decimal on all seven shared names —
the price source is validated a second time, by a second method. Defense and rails carry a genuine
prior-40 base; **the electrical/automation cluster and PWR do not** — every carrier plus TRI has a
negative segment. VRT and GEV are negative-to-flat on *both* windows, a different shape again: not
repairing, just not turning.

## §2 · Repair vs. ignition — argued both ways

**For ignition**: a real regime change rarely arrives with a clean prior base — it arrives *because*
the prior 40 sessions reset positioning, so RS20 sharply positive with RS60 modest and segment
negative is the expected shape of a genuine turn's opening days, not a disqualifier. OBV accumulation
(13/13 axes lit, SWEEP §2) and 1.33–1.56× volume surges on all four carriers read as new money
entering names the tape had left for dead. Demanding a positive prior-40 base before calling it real
asks the data to prove the turn already happened before it is allowed to start.

**For repair**: the segment test exists to separate base-building turns from bounces inside a
still-declining trend, and this desk's own prior file used it to correctly disqualify ETN three days
before ROTATION counted it as breadth anyway. The differentiator is not the four carriers' own shape
but what the rest of the chain does on the same date. A cycle ignition should pull adjacent nodes
together; instead §4 shows the turbine node (GEV) and integration node (VRT) still distributing,
carrying the worst RS60/RS20 in the basket, on the same catalyst window (EVENT_ALPHA Card 6).

**Verdict: do not call this an ignition on today's data.** The segment test alone is genuinely
ambiguous — both readings above are honest — but the cross-node split in §4 is not: three names
accumulating and two distributing on the same theme, same date, is a repair concentrated in one
sub-node, not a cycle bidding its whole chain. **S62 (settles 2026-08-07) is the instrument built to
resolve this, not this file**; its reading today (+14.51pp, past the 85th percentile) sits closer to
"one crowded rotation" than "one cycle."

## §3 · Value chain and the binding constraint

generation (**GEV** turbines) → transmission/grid (**PWR**; GEV Electrification also sells HVDC) →
switchgear & distribution (**ETN**: breakers, switchgear) → power management/automation (**EMR**,
**ROK**; instrumentation via **AME**) → data-centre integration/UPS/cooling (**VRT**, AME's thermal
leg) → compute load (NVDA/AVGO, held, not INDU).

**Primary anchors, `module_business_us --json`:**
- **GEV** FY2025 10-K (filed 2026-01-29): *"Customer lead-times have increased as a result of demand
  outstripping supply… we are making investments to expand our capacity"* — stated for **Grid
  Solutions** (HVDC, substations, power transformers, switchgear). `[measured, primary]`. The
  grid/switchgear node, not generation or compute.
- **ETN** FY2025 10-K (filed 2026-02-26): $27.4bn revenue, 22% of Electrical sales to "six large
  customers" (class disclosed, not named — A6 partially unmet). Its three 2025–26 acquisitions all buy
  capacity at the same two nodes: **Resilient** (solid-state transformers), **Fibrebond** (modular
  power for "hyperscale data center customers" — the closest this filing comes to naming the buyer),
  **Boyd Thermal** (liquid cooling, "chip to the grid"). `[measured, primary]`.

**Binding constraint: switchgear/transformer manufacturing capacity, not demand.** Both filings flag
the same node — grid/distribution hardware — as lead-time-constrained and under active capacity
investment; neither names generation or compute as the limiter. Demand language ("growth cycle,"
"electrification") is universal across both filings; capacity-*add* activity concentrates specifically
at the switchgear/distribution and cooling nodes — that concentration is the evidence.

## §4 · Why the chain splits

Electrical Components & Equipment (n=5): **ETN** fs +0.978 🟢, **EMR** +0.867 🟢, **AME** +0.788 🟢 —
all OBV 매집, RS20 +6.5 to +12.0. **ROK** 🟡 fs +0.183, RS20 −8.2, FINRA z −0.26. **VRT** 🟡 fs
+0.019, RS20 −14.8/RS60 −26.0, vol_surge **1.87** (sector's 3rd-highest) carrying **no accumulation**
(OBV 중립, FINRA z −0.09). Heavy Electrical Equipment (n=1): **GEV** 🔴 fs −0.681, RS20 −8.6, OBV
분산, FINRA z −0.71. Construction & Engineering: **PWR** 🟢 but RS60 −13.1; peers FER/FIX/EME all
RS60 −10.4 to −17.0, none 🟢.

The split tracks §3's chain almost exactly: **ETN/EMR/AME sit at the switchgear-distribution/
automation node §3's own filings identify as capacity-constrained.** Where new orders get priced up
is where the equity gets bid. **GEV (one node upstream) and VRT (one node downstream) are both
distributing** — a real but narrow effect (the bottleneck is rewarded, not the chain), consistent
with §2's repair verdict: a broad ignition should pull generation and integration into the same bid,
and it has not.

## §5 · Chain-hop — under-named beneficiaries, flow cross-checked

`chain-hop "data center power" --scope foreign --days 7` (46 articles): one body-proximate,
headline-absent candidate, **GS** (2 proximity mentions, 0 titles, tied to a Bloom Energy piece).
Cross-check (`scripts/us_flow.py`): GS flow −0.377 🔴분산, RS20 −2.2, OBV 분산, FINRA z −0.49 —
**fails; money is leaving GS the same date the theme names it. Not handed to BET.**
`chain-hop "switchgear"` (10 articles): only non-headline candidate is **MSFT** — already the most
headline-crowded name in this run and not "under-named"; declined without a flow check that would
only confirm the obvious.
`chain-hop "data center cooling"` (30 articles): **zero** non-headline candidates. **Swept, found
nothing that clears the bar — a negative result, stated as one.**

## §6 · Track KPIs + anti-signals, dated

- **S62** (settles **2026-08-07**): median RS20{EMR,ETN,AME,PWR} − XLU RS20, currently **+14.51pp**.
  A ≤ **−5.9pp** (one bet, not two) · B ≥ **+7.4pp** (survives, incl. CEG 08-06/VST 08-07). This
  file's §2 verdict falsifier — watch, don't pre-empt.
- ETN/EMR/AME segment 21-60 turning net positive on a settled close by **2026-08-19** ⇒ repair
  upgrades toward confirmed continuation.
- **Anti-signal**: two of {ETN,EMR,AME} turning OBV 분산 ⇒ collapses to "one earnings-day pop,"
  matching the 08-02 file's ETN call.
- **Anti-signal**: GEV or VRT posting settled RS20 > 0 with OBV 매집 together (D6, both legs) by
  **2026-08-12** ⇒ the chain is bid broadly and §4's narrow-bottleneck read is wrong.
- PWR RS60 crossing above 0 ⇒ EVENT_ALPHA's `enters-if` clears; recheck **2026-08-19**.
- GEV's stated capacity expansion (§3): no dated disclosure exists yet for when added
  transformer/switchgear capacity comes online — open item, not invented.

---

*asof 2026-08-05 · flow/RS settled 2026-08-04 · segment test reproduced independently, matches
PREMORTEM Lens 3 to one decimal on all seven shared names · verdict: repair confirming at one node,
not a chain-wide ignition · S62 (08-07) is the frozen falsifier · chain-hop swept three theme terms,
one candidate (GS) failed cross-check, one (MSFT) declined as already-crowded, one term returned
nothing. Analysis only, zero buy/sell, zero sizing (P4).*
