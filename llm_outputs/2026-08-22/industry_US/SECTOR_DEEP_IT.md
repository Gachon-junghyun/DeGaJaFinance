# SECTOR_DEEP_IT — Information Technology (UW) · industry_US · 2026-08-22 (Sat) · **PREMORTEM-PROMOTED 5th slot**

> Promoted by LENS 1: the desk carries a **UW** into the board's largest binary (`NVDA` **08-26**),
> from the **12th percentile of 252**, while **holding four names in the sector**.
> Flow `asof` **2026-08-21** settled; `exc5` vs **`SPY` (−1.368%)** named inline (`C1`).
> **No sizing, no buy/sell language (P4).**

## 0 · The mandate PREMORTEM set

> *"The UW is priced, not building — and there is a dated binary in four days."*

**★★★ Answer: the price is worse than the flow, the flow is worse than the balance sheet, and the
sector's largest dated commitment of the week is in a layer the book does not own.**

## 1 · The three facts that make the UW an under-computed leg

| Axis | Reading | Rank |
|---|---|---|
| `exc5` vs `SPY` | **−2.158** | **11 of 11 — worst** |
| `eqflow` | **−0.102** | **8 of 11 — mid** |
| **`eqflow` − `wflow`** | **+0.129** | **widest positive gap on the board** |
| `SMH` `exc5` | **−3.293 = 12th %ile of 252** (mean +1.063, sd 3.740) | — |
| `NVDA` `exc5` | **−3.269 = 21st %ile of 252** | — |
| `Nasdaq-100` spec | **4th %ile**, **+30,838 WoW** (the week's largest covering flow) | `[COT 08-18]` |

⇒ **The sector's weakness is concentrated in its largest names, not in its breadth.** ⚠ **The COT line
is positioning — context, NOT a trigger (`D6`)** — and it is 4 days stale.
★ **The tape's own attribution, 08-21, 3 outlets: *"Chip Stocks Didn't Fall on Chip News This Week."***
Which is what `MACRO §0` predicts: this was a **rates** week, not a semis week.

## 2 · The sector is FOUR businesses and only one of them is broken

```
── SOFTWARE (accumulating) ──────────   ── ANALOG / LEGACY SEMI (broken) ──────
CRM  +0.639 obv+0.344 rs20 +24.2        TXN  −0.806 🔴 obv−0.341 rs60 −18.8
NOW  +0.544 obv+0.509 rs20 +26.4        NXPI −0.800 🔴 obv−0.353 rs60 −33.5
INTU +0.561 obv+0.458 rs20 +20.2        MCHP −0.789 🔴 obv−0.276 rs60 −23.5
PLTR +0.511 obv+0.190 rs20 +42.8        WDC  −0.781 🔴 obv−0.156 rs60 −15.4

── AI-COMPUTE (the book's four) ─────   ── OPTICAL (price ≠ fundamentals) ────
HPE  +0.489 obv+0.198 rs60 +41.6        LITE +0.639 obv+0.174 d **+0.236**
ANET +0.417 obv+0.152 rs60 +20.2        (COHR/CIEN sit in this node too)
NVDA −0.181 obv−0.024 rs60  −1.0
AVGO −0.221 obv+0.038 rs60 −14.7
```

- **Software is the sector's strength and it is unambiguous**: `NOW` `obv_norm` **+0.509** and `INTU`
  **+0.458** are the two highest in the sector; `PLTR` `rs20` **+42.8** is the highest of all 299
  names; `CRM` +24.2. **None is 🟢** — all four blocked by `vol_surge` (0.95 / 0.81 / 0.72 / 0.95).
- **Analog/legacy is where the −0.806 to −0.781 reds live**, all four with distributing OBV **and**
  deeply negative `rs60`. ⇒ **the "IT UW" is really an analog-and-storage UW plus a mega-cap de-rate.**
- **The book's four**: `HPE` `rs60` **+41.6** (but `S87` fired **A — EXHAUSTED** on `EW{DELL,HPE}`
  −8.076, so the *run* leg is scored dead while the *price* leg is still high — DEEP does not
  re-argue it); `ANET` improved most in the book (**delta +0.384**) **but carries this run's only
  🔴 short axis** (§4); `NVDA` and `AVGO` both flat-to-negative.
- **Optical**: `LITE` +0.639 with **delta +0.236** and `obv_norm` +0.174 accumulating, `COHR` +0.158
  (delta +0.207), `CIEN` −0.380 (delta **+0.274**). **All three deltas strongly positive off deeply
  negative bases**, while `S86` **and** `S96` both settled **branch B** this morning and `Fabrinet`
  guided *"AI optical demand fueling years of growth"* (5 outlets, 08-21). 🚨 **`cycle_registry.json`
  still has no optical row for a 10th run (`D250`/`M731`) ⇒ exposure here is unmeasurable, not zero.**

## 3 · ★★ Value chain — and the layer where the week's money was actually committed

```
①EDA/IP ─►②foundry ─►③COMPUTE ─►④interconnect ─►⑤SYSTEMS ─►⑥POWER ─►⑦offtake/financing
           (TSM not     NVDA −0.181   LITE +0.639    HPE +0.489   GEV −0.741🔴  OpenAI (private)
            in universe) AVGO −0.221   COHR +0.158    ANET +0.417  CEG −0.625🔴  ORCL +0.444
                         MRVL +0.583   CIEN −0.380🔴  DELL         VRT −0.539    ★ NVDA guarantees
                         ★ book owns 4                             ETN +0.210     up to **$105bn**
                                                                   [BINDING NODE]
```

**★★★ The binding constraint moved to ⑥ this week, and the book has no measured exposure there.**
- `yahoo_finance` **08-18**, quoted: **"Nvidia will guarantee up to $105 billion for OpenAI's Ohio
  [data-centre leases]"**; 08-17 *"Nvidia confirmed Monday it will provide a **financial guarantee**"*
  alongside Huang's *"Could Generate $600 Billion in Revenue"*; 08-16 the tape's own metaphor —
  *"Nvidia is becoming the **'Federal Reserve of AI'**"*; **08-21 *"Nvidia in Talks to Invest in
  Data-Center Power Developer Cloverleaf Infrastructure."***
- **Every power-layer name is 🔴 or deeply negative**: `GEV` −0.741, `CEG` −0.625, `VRT` −0.539,
  `NEE` −0.600 🔴, `VST` −0.689 🔴. **The guarantor itself is flat** (`NVDA` −0.181, obv −0.024).
- ⚠ **`ETN` is the book's only electrical name and `M778` says it is an `XLI` position** (β +1.402,
  t +6.12 vs β`XLK` +0.620) ⇒ **it may not be counted as node-⑥ exposure.**
- ⇒ **`PREMORTEM §5`'s third attack is confirmed here: the AI-compute cycle ✅ is carried at the
  COMPUTE layer while the week's committed capital went to POWER, and the desk cannot measure whether
  it owns that layer.** This is a **measurement gap**, not a sizing conclusion (P4).

### `chain-hop` — the one candidate that survives the flow cross-check

`module_news_data chain-hop "data center power" --days 7 --scope foreign` returned **3 body-proximate,
title-unnamed candidates**: `ORCL` (proximity 3 / body 16) · `NEE` (3/4) · `CEG` (3/8). Example
article: *"Micron's AI Boom Is a Utility Story Too. Here's the Power Angle Wall Street Isn't Pricing."*

**Flow cross-check applied before any name may reach BET (the stage rule):**

| Candidate | flow | `obv_norm` | rs20 | rs60 | Verdict |
|---|---|---|---|---|---|
| **`ORCL`** | +0.444 | **+0.380 accumulating** | **+23.8** | **−25.3** | ✅ **passes** — *"OBV accumulating, RS not yet up"* is the exact shape the tool defines as chain-hop alpha |
| `NEE` | −0.600 🔴 | **−0.205 distributing** | −10.5 | −6.6 | ❌ fails |
| `CEG` | −0.625 🔴 | **−0.268 distributing** | −4.2 | −7.5 | ❌ fails |

⇒ **One candidate admitted to BET §B as a chain-hop name: `ORCL`.** ⚠ It is already carried as a
cross-sector orphan in `STANDING_VIEW`, so this is a **re-anchoring**, not a discovery — and its
`vol_surge` is **0.60**, the lowest in the admitted set, so it will never be 🟢 under the current gate.

## 4 · 🚨 The one new red flag on a held name

**`ANET` FINRA short-volume z = +1.82 🔴 (short% 51.9 vs base 42.2, 5v5 +3.9▲)** — settled 08-21.
**It is the only 🔴 in this run's 25-name short probe**, and it lands on the book name that *improved
most* on flow this run (delta +0.384, flow +0.033 → +0.417).
⇒ **Flow improving and short pressure spiking on the same settled bar is a divergence, and it is the
kind news cannot see** — precisely what the L2's short-z cross-check exists for. **Recorded as an
observable, with no directional claim (P4).**

**The counter-readings in the same probe**: `AVGO` **z −2.53 🟢** (deeper covering than the −1.60 the
08-21 packet recorded), `NVDA` **z +0.41 🟡** (normal), `MRVL` −0.65 🟡, `HPE` +0.20 🟡 with
**5v5 −14.8▼ — the largest downward short-trend in the probe set**.

## 5 · Lens `B2` — the peak-margin / low-multiple trap, applied where it belongs

⚠ **This lens is NOT applied to `NVDA` here.** `margin_history NVDA` (settled, run this stage) gives
**FY2009–FY2026, 19 years**, with **FY2026 operating margin 71.1%** against a peak of **75.0% (FY2025)**
and a median of 56.9%. **The margin is ~4pp off its own peak and the peak was last year** ⇒ the
denominator is *already rolling*, which is a different situation from `MU`'s 100th-percentile print.
🚫 **And the revision-momentum axis may not be used as a leading indicator here**: `measure_ic`'s
control arm showed the effect is an **Information-Technology loading**, not a revision axis
(**+0.074 / −0.064** on ex-IT 120 names, Q5−Q1 **+9.4pp → −1.1pp**). **`NVDA` is exactly the confound.**

## 6 · Track-KPIs and anti-signals

| KPI | Today | What kills the UW |
|---|---|---|
| **`S113`** (registered this run) | `SMH` exc5 **−3.293 = 12th %ile**; window **08-25 → 09-01** | **branch A ≥ +4.461pp** ⇒ the complex re-rates through the print and the UW was wrong at the 12th percentile. ⚠ branch B (≤ −2.627) is **pre-declared LOW-INFORMATION** — the state is already below it |
| `S103` | `NVDA` 08-26, **hand-set ±5.0pp bands, NOT re-frozen** (`D242`) | 🚫 **`D295` unmet for a 3rd run and the reason is now measured**: `--positioning NVDA` returns **±1.6%, expiry 08-24, D2 — before the event** (`D315`) |
| `P79` | AI-compute EW exc5 **−5.609**, settles **08-25** | **moved +1.57pp AWAY from branch B (≤ −7.72)** in one session — the flush thesis is losing, not winning |
| `S94` | `EW{COHR,LITE}` exc5 **−7.412**, settles **08-31** | already inside **branch B**; branch A additionally needs `vol_surge` ≥ 1.0 on both and **`LITE` is 0.95** ⇒ A currently fails on the volume conjunction |
| `ANET` short axis | **z +1.82 🔴, 5v5 +3.9▲** | a move above **+2.5** with flow still improving = a genuine divergence to escalate |
| Node ⑥ | `GEV` −0.741 · `CEG` −0.625 · `VRT` −0.539 all 🔴 | `EW{GEV,CEG,VRT}` exc5 vs `SPY` **≥ 0** by 09-02 ⇒ the $105bn commitment starts being priced (EVENT_ALPHA CARD 2's branch) |

## 7 · The mandate, answered in one line

**The UW is priced at the mega-cap layer and is not supported at the breadth layer** — `eqflow`
(rank 8) is a full three ranks better than price (rank 11), software carries the sector's two highest
`obv_norm` readings, and the sector enters an 08-26 binary from the **12th percentile** with
`Nasdaq-100` spec at the **4th**. ⇒ **UW is carried into the print because no notch below it exists to
express a change and `S113` now brackets it both ways — but the honest statement is that this is the
board's most likely wrong verdict, and the row that would convict it is registered.**
🚨 **And the sector's real gap is not the verdict: it is that the week's largest dated capital
commitment ($105bn, 8-GW) landed on a chain layer whose every measurable name is 🔴 and where the book
has no measured exposure.**
