# BET_SHEET — industry_US · 2026-08-23 (Sun) · Stage 9 / L1·BET

> **ONE file, per-sector sections.** Downstream desks glob this exact filename.
> **P4 — zero buy/sell recommendation. Sizing language below is influence-illustration only.**
> ⚠ **`n_new_sessions_since_prior_run = 0`.** Every flow/price figure is the **2026-08-21** settle and
> is identical to the 08-22 sheet. **Nothing in this file is a "move".**
> DEEP set: **ENRG · HLTH · DISC · UTIL · IT** (IT = PREMORTEM-promoted 5th).

---

## §0 · The three things this sheet exists to hand forward, and one of them is a refusal

1. **`EVENT_ALPHA` handed BET nothing, and this sheet does not backfill.** No card reached
   CONFIRMED-EARLY on **both** the story and money axes. The candidate sections below are therefore
   built from the **screener ∪ shortlist ∪ DEEP** union, not from a promoted thesis — and where a
   section has no candidate, it says so instead of finding one.
2. ★★★ **A gate finding that governs every 🟢 on this sheet.** **94 of 299 names clear `OBV 매집 ∧
   rs20 > 0`; 6 clear 🟢; 88 are blocked and 100% of them on `vol_surge` alone.** That axis is measured
   at **t(NW) −3.86 (h=1) / −3.38 (h=5)**, past Bonferroni, **negative** — in a `market=kr` ledger,
   so **`W1` bars this desk from acting on it** (`D310`, open 2 runs). ⇒ **Every 🟢 cited below carries
   the sentence: *selected partly on `vol_surge`, an axis measured negative in the KR ledger.***
3. ★★ **`M835` (DEEP-HLTH): `breadth` in `SECTOR_FLOW.json` is the 🟢 rate, not participation**
   (`sector_flow.py:342`, `greens / len(names)`). **No section below uses `breadth` as a participation
   claim**; each quotes true participation `(OBV 매집 ∧ rs20>0)/n` instead.

⚠ **Thesis-confirmation gate**: `REPORT/COMPANY_SCOREBOARD.md` is dated **2026-08-21** and is a
**KR-universe** batch (`028050`, `042700`, …). **No US candidate below has a scoreboard row**, so the
confirm-don't-re-derive path is unavailable and every §A is derived here. Stated rather than assumed.

---

## §I · ENERGY (OW) — the sheet's most consequential section, and it contains no new name

### §I-A · Numbers
Held: `MPC`, `PSX`. Non-held sector names clearing two of three axes: `COP`, `VLO`, `XOM`(no).

| | flow | OBV | rs20 | rs60 | surge | FINRA z (08-21) |
|---|---:|---|---:|---:|---:|---:|
| `PSX` **held** | +0.728 | 매집 +0.261 | +13.8 | +37.0 | 1.11 | +0.13 (5v5 **+8.4▲**) |
| `MPC` **held** | +0.700 | 매집 +0.318 | +13.0 | +44.0 | 1.06 | −0.07 (5v5 −6.4▼) |
| `COP` | +0.694 | 매집 +0.259 | +8.5 | +15.1 | 1.05 | — |
| `VLO` | +0.506 | 매집 +0.254 | +11.7 | +43.1 | 0.71 | — |
| `XOM` (`top1`, 30.5%) | **−0.183** | **분산 −0.101** | +1.6 | +9.6 | 0.93 | −1.02 |

**From the primary source, this run** (`M833`, MPC 10-Q filed 2026-08-04):
**R&M margin per barrel Q2 2026 $36.33 vs Q2 2025 $17.58 (+106.7%)**; 6M **$27.24 vs $15.57
(+74.9%)**; **crude capacity utilization 94% vs 97%**; net throughput **2,944 vs 3,060 mbpd (−3.8%)**.

### §I-B · Thesis + freshness placeholder *(ALPHA fills the tag)*
Refining-capacity constraint expressed through product cracks. ⚠ **The issuer disagrees about the
mechanism** (`M832`): MPC attributes the margin to *"global crude oil supply disruptions as a result of
increasing regional conflicts."* **Shape confirmed, mechanism contested — carried, not resolved.**

### §I-C · Flow / positioning cross-read
`eqflow` **+0.102 (rank 2 of 11)**, participation **37.5% (6/16)**, `exc5` **+4.162 (rank 2)**.
🚨 **The sector returns ZERO shortlist names and that is a FILTER ARTIFACT, not evidence** — `PSX`
1.11 / `MPC` 1.06 / `COP` 1.05 all fail the surge gate alone. **WTI spec 36th %ile** — uncrowded.
⚠ `delta` **−0.093**, second-most negative of eleven: price leads, flow does not confirm.

### §I-D · Competition / peers
`XOM` at 30.5% weight is **dispersing on three agreeing axes, with OBV as the third rather than the claim (`RULE D6`)**: `flow_score` **−0.183**, one-session `delta` **−0.200** (the sector's worst), and OBV **분산 −0.101** — while the sector's `eqflow` is
positive. **The Energy OW is the refiners, not the majors** — and `top1_flips_sign` is **false**
(`wflow` +0.076 → ex-`XOM` **+0.189**), so removing the largest name *strengthens* the sector.

### §I-E · Refutation + dated catalyst
🚨 **`M831` — the refutation is contractual and it is now measured.** MPC's 10-Q contains **zero**
`take-or-pay`, **zero** fixed-fee refining-margin structure, and **zero** long-term contracts. The only
long-term structure runs the **wrong way**: minimum-volume commitments to MPLX that *"will negatively
impact segment adjusted EBITDA in periods when throughput or sales are lower or refineries are idled."*
⇒ **Micron's contracts floor revenue; Marathon's floor cost.** The `L2` peak-margin lens has **no
escape hatch here**, and `P70`'s MISS is explained rather than merely recorded.
**Dated catalysts**: `P89` settles **08-28** (A: `BZ=F` ≥ 93.00 ∧ distillate crack ≥ 98.0 · B: `BZ=F`
≤ 88.00 **or** crack ≤ 90.0) · `P83` **08-27** · `FRO` print **08-28**.
**No new name advanced. No sizing.**

---

## §II · HEALTH CARE (OW) — the widest candidate set on the sheet, and the gate excludes all but one

### §II-A · Numbers (the six the screener and the axes jointly surface)

| | flow | OBV | rs20 | rs60 | surge | fwd P/E | price vs consensus mean target |
|---|---:|---|---:|---:|---:|---:|---|
| **`MRK`** 🟢 | **+0.978** | 매집 +0.370 | +12.8 | +24.8 | **1.56** | **15.99** | **$152.55 vs $147.77 = −3.1% (ABOVE target)** |
| `REGN` | +0.550 | **매집 +0.656** | **+23.5** | +30.8 | 0.79 | — | — |
| `BDX` | +0.589 | 매집 +0.437 | **+19.2** | +28.4 | 0.86 | — | — |
| `A` | +0.711 | 매집 +0.186 | +11.1 | **+35.2** | 1.08 | — | — |
| `TMO` | +0.568 | 매집 +0.339 | +7.1 | **+35.9** | 0.89 | — | — |
| `ABT` | +0.528 | 매집 +0.461 | +9.6 | **+34.1** | 0.75 | — | — |
| *screener* `CAH` (leader pullback, RSI 41.6) · `ISRG` (de-rate snapback, RSI 51.9) | −0.252 · +0.539 | 중립 · 매집 | −3.0 · +8.6 | +12.8 · **−11.5** | 0.70 · 0.77 | — | — |

### §II-B · Thesis + freshness placeholder
Pharma/devices/tools accumulation, **broad**: **19 of 32 names (59.4%) carry `OBV 매집 ∧ rs20 > 0`** —
the second-highest participation on the board. `eqflow` **+0.229 (rank 1)** > `wflow` +0.196.

### §II-C · Flow / positioning cross-read
🚨 **18 of the 19 participating names fail 🟢 on `vol_surge` alone** (median surge **0.85** vs gate 1.20).
`MRK` is the sole 🟢 — and it is the one name in the group whose **consensus target sits BELOW spot**.
⇒ **The gate selected the one name the sell side thinks is fully valued and excluded five carrying
rs60 of +28 to +36.** Stated as the gate's behaviour, not as a valuation view.

### §II-D · Competition / peers — the sector is TWO businesses (`W5`)
**Pharma + devices + tools (17 names): all `flow_score` > 0, all rs20 > 0, all OBV 매집 — no exception.**
**Managed care + distribution (7 names): `CVS` −0.783 🔴 · `UNH` −0.719 🔴 · `CI` −0.651 · `MCK` −0.403 ·
`HUM` −0.349 · `CAH` −0.252 · `COR` −0.206 — all `flow_score` < 0, zero OBV 매집.**
⇒ **An OW on "Health Care" is an OW on pharma/devices and an implicit UW on managed care.** The desk
holds neither. ⚠ `LLY` (19.4%) and `JNJ` (10.9%) rank **22nd and 21st of 32** on flow.

### §II-E · Refutation + dated catalyst
**Kills the OW**: `eqflow` rank falls below 4 · participation below 40% · any 4 of the 17 leave 매집 ·
a third and fourth managed-care name turns 🔴 (the drag stops being one node).
⚠ **Duration**: this is the desk's longest-duration OW against `DGS30` at the **96.4th %ile** —
`S112` (Jackson Hole, **08-31**) branch B is its macro falsifier.
**No name advanced.** ⚠ `CAH` and `ISRG` are screener raw candidates, **turn unconfirmed**, and `ISRG`
carries rs60 **−11.5**. Both filed to the miss ledger rather than carded.

---

## §III · CONSUMER DISCRETIONARY (N+) — a real node, a mega-cap drag, and no falsifier

### §III-A · Numbers

| Node | Names | flow | OBV | rs20 | rs60 |
|---|---|---|---|---|---|
| **Travel / delivery / marketplace — the base** | `DASH` +0.717 · `ABNB` +0.700 · `BKNG` +0.494 · `MELI` +0.370 | all **매집** (`DASH` **+0.595**, sector high) | +25.6 / **+29.1** / +14.5 / +3.1 | **+39.8 / +39.8 / +22.5 / +11.3** |
| **The two mega-caps — the drag** | `AMZN` **40.2% wt** −0.076 · `TSLA` **23.0% wt** +0.600 | `AMZN` **분산 −0.110** · `TSLA` 매집 | +7.8 / +12.3 | **−6.9 / −19.6** |
| *screener new* (6) | `RCL` −0.075 · `AMZN` −0.076 · `ROST` +0.396 · `NKE` −0.299 🔴 · `AZO` −0.280 · `TJX` −0.333 🔴 | mixed | — | — |

### §III-B · Thesis + freshness placeholder
`exc20` **+4.244 = rank 1 of 11** against `exc60` **−4.938 = rank 10**. **The 20-day leadership sits on
a 60-day base in one node; the 60-day deficit is two mega-caps at 63.2% combined weight.**

### §III-C · Flow / positioning cross-read
Participation **39.3% (11/28)** — *not* the 0.000 that `breadth` prints (`M835`). `eqflow` **+0.103
(rank 2)**. ★ **`top1_flips_sign` false because removing `AMZN` takes `wflow` +0.122 → +0.254** —
**the 40.2% name is a drag, not a driver.**
⚠ **Three of the sector's four highest volume surges are in apparel/off-price and two are 🔴**:
`TJX` 1.64 🔴분산 · `ROST` 1.61 🟡매집 · `LOW` 1.30 🟡중립 · `NKE` 1.22 🔴분산. **The clearest single
demonstration on this sheet that `vol_surge` carries no sign.**

### §III-D · Competition / peers
Node 2 **splits**: asset-light platforms accumulate (`ABNB` +0.700, `BKNG` +0.494) while asset-heavy
hotels/cruise disperse (`MAR` **−0.750 🔴**, `HLT` **−0.479 🔴**, `CCL` −0.491). **1.45 of flow spread
inside one node** (`W5`).

### §III-E · Refutation + dated catalyst
🚨 **The sector has NO live pre-registered falsifier** — `S91` was VOIDed 08-22 on a `D300-KR` anti-signal.
**The board's best 20-day excess and worst DEEP recency (~8 runs) has nothing testing it.**
**Kills the N+**: any 2 of `{ABNB, DASH, BKNG, MELI}` leave 매집 · `AMZN` leg down (it alone can take
the sector negative) · participation below 25%.
**Dated**: `P92` settles **08-28** (`XLI` ≤ −2.50pp **or** `XLB` ≤ −1.00pp = the tariff prices).
⚠ The **50% US–Canada tariff took effect 08-22**, *after* this flow frame.
**No name advanced.**

---

## §IV · UTILITIES (UW) — the sheet's cleanest negative, and a 62% consensus gap on top of it

### §IV-A · Numbers

| | flow | OBV | rs20 | rs60 | surge | fwd P/E | price vs consensus mean target |
|---|---:|---|---:|---:|---:|---:|---|
| `PCG` | **+0.231** | **매집 +0.255** | −5.0 | **+4.4** | 1.19 | — | — |
| `ED` | −0.115 | 매집 +0.081 | −9.5 | −3.6 | 1.09 | — | — |
| **`VST`** | **−0.689** | **분산 −0.340** | **−20.3** (sector worst) | −17.0 | 0.96 | **13.14** | **$136.21 vs $220.56 = +61.9% "upside"** |
| `CEG` (9.6% wt) | −0.625 | 분산 −0.268 | −4.2 | −7.5 | 0.79 | — | — |
| `NEE` (17.7% wt) | −0.600 | 분산 −0.205 | −10.5 | −6.6 | 1.12 | — | — |
| *screener washout* | `D` · `SO` · `PEG` · `AEP` (RSI < 28, near 52w low) | all 분산 | −10.0 to −14.4 | — | — | — |

### §IV-B · Thesis + freshness placeholder
**The UW is confirmed against the news, not with it.** A named **38-gigawatt** AI power gap (Morgan
Stanley, 08-20) and `NVDA`'s **$105bn** OpenAI lease guarantee sit against **0% participation**.

### §IV-C · Flow / positioning cross-read
**Participation 0.0% — 0 of 15.** `eqflow` **−0.621** (worst of 11), `exc20` **−11.230** (last by 5.7pp),
**13 of 15 분산**, **0 of 15 with rs20 > 0**. ⚠ **The only sector where `breadth` and participation
agree** (`M835`).

### §IV-D · Competition / peers — the ordering is the finding (`M836`)
**The two names not dispersing (`PCG`, `ED`) have the LEAST AI-load exposure** (wildfire-liability
recovery; NY regulated distribution). **The two purest AI-power expressions (`CEG` 9.6%, `VST` 5.4%)
are among the worst.** ⚠ Cross-sector, the equipment node is where the only accumulation on the whole
chain sits: `ETN` **+0.210 매집** (held, rs20 +0.1) and `EMR` **+0.268 매집** (rs20 +2.7) — while
`GEV` −0.741 🔴 and `TT` −0.812 🔴 disperse (each also `flow_score` ≤ −0.74 and rs20 ≤ −9.3;
`RULE D6`). ⚠ **`M778` assigns `ETN`'s move to `XLI` (β +1.402, t +6.12)** — the book's "AI-power"
label is not measurably an AI-power exposure.

### §IV-E · Refutation + dated catalyst
🚨 **`VST`: forward P/E 13.14 with a consensus mean target of $220.56 against a $136.21 price — a
+61.9% implied upside — in the sector with zero participation and the worst rs20 on its own board.**
**Consensus and the tape are 62 points apart on one name.** *(Recorded as the sheet's largest
sell-side-vs-tape divergence. **No view is taken on which is right** — P4.)*
**Kills the UW** (EVENT_ALPHA Card 6's registered horizon, **2026-09-03**): 3 of
`{GEV, VST, CEG, NEE, TT}` reach OBV 매집 **and** `flow_score` > −0.20.
**Discriminating KPI registered, not bracketed**: the **`CEG` − `NEE` 20-session excess** (today
**+6.3pp**) — a rate-driven de-rate keeps them together inside ±8pp; a "the load never reaches listed
utilities" outcome takes `CEG` to **≤ −8pp**.
**No name advanced.**

---

## §V · INFORMATION TECHNOLOGY (UW−, PREMORTEM-promoted) — one held-name event, three dated binaries

### §V-A · Numbers

| | flow | OBV | rs20 | rs60 | surge | fwd P/E | FINRA z |
|---|---:|---|---:|---:|---:|---:|---:|
| `NVDA` **held** | −0.181 | 중립 −0.024 | +0.2 | −1.0 | 0.75 | — | +0.41 △ |
| `ANET` **held** | **+0.417** | 매집 +0.152 | +4.8 | **+20.2** | 0.82 | — | **+1.82 🔴 surge**, 5v5 +3.9▲ |
| `AVGO` **held** | **−0.221** | 중립 +0.038 | **−7.2** | **−14.7** | 1.00 | — | **−2.53 🟢 covering**, 5v5 −6.0▼ |
| `HPE` **held** | +0.489 | 매집 +0.198 | +8.5 | **+41.6** | 0.68 | — | +0.20 |
| `MRVL` *(not held)* | **+0.583** | 매집 +0.183 | **+18.4** | **+17.3** | 0.85 | **37.95** | — |
| `MSTR` 🟢 · `MSI` 🟢 | +1.000 · +0.806 | 매집 | +26.5 · +11.4 | **−24.7** · +11.9 | 1.61 · 1.25 | — | `MSTR` −1.23 🟢 |

### §V-B · Thesis + freshness placeholder
🚨 **The book's `AI-compute-EPICENTER` label covers 2–3 distinct measured risk units** (`M837`):
`NVDA` is a **singleton in all three windows (250/500/750d)** and **never groups with `AVGO`**;
`ANET`+`AVGO` merge at 500d and 750d. **This is one of only two `G4`-robust groupings the desk owns.**

### §V-C · Flow / positioning cross-read
Participation **30.4% (17/56)**, `eqflow` −0.102, `exc5` **−2.158 (rank 11 of 11)**, 🟢2 : 🔴15.
**Implied moves, from the option chain** (`module_flow --positioning` returns the wrong expiry —
`D315`, 4th run): `NVDA` **±6.11%** (08-28, IV 0.606) · `MRVL` **±11.31%** (08-28, IV **1.122**) ·
`AVGO` **±9.51%** (09-04, IV 0.643) · **`MU` ±6.61% at IV 0.650 with no print until 09-24.**
★★ **`MU`'s IV exceeds the reporting company's on the same expiry** — registered as `S117`.

### §V-D · Competition / peers — the held-name event
**Alphabet dual-sourced custom silicon to `MRVL` on 2026-08-19**, with a **$12.2bn / 59m-share warrant
that does not fully vest until Google buys $120bn of chips** (`yahoo_finance` 08-20, 08-21).
**`AVGO` ↔ `MRVL` rs60 spread 32.0pp; `AVGO` ↔ `ANET` 34.9pp.** ⚠ **`AVGO`'s standing thesis line has
carried no customer for the life of the position** (`W4`) — and the customer is the event.
⚠ `MRVL` fwd P/E **37.95** vs price $237.04 and consensus mean target $263.94 (**+11.3%**) — the only
name on this sheet whose consensus target is meaningfully above spot, and it is **LATE-MONEY** (the
32pp spread is already realised). **Filed to the miss ledger 08-23, not carded.**

### §V-E · Refutation + dated catalyst
- **`P90`** (**08-26**): A = guided GM ≤ reported **and** reported ≤ +50bp vs prior (**cost
  pass-through**) · B = guided GM ≥ +100bp (**pricing power — the card's premise is wrong**).
- **`S115`** (**08-27**): `NVDA` 1-session return ≥ +7.0% / ≤ −7.0%, **outside** the ±6.11% implied.
- **`S116`** (**08-28**): `MRVL` − `AVGO` 1-session spread ≥ +12.0pp / ≤ −12.0pp.
- **`S117`** (**08-27**): `MU` − `NVDA` ≥ +3.0pp / ≤ −3.0pp.
- ⚠ `ANET`: **the only 🔴 short-surge on the book** — new shorts into the book's largest positive delta.
  Flip condition: z above **+2.5** with rs20 turning negative.
- 🚨 **`SECTOR_DEEP_SEMI.md` is 39 days old** and covers where 4 of 11 book names live.
**No name advanced.**

---

## §VI · Cross-sector LIVE_SHORTLIST names (outside the DEEP sectors)

`US_LIVE_SHORTLIST.json`, 6 names, `mcap ≥ $10B` ∧ 🟢. **Two are in DEEP sectors** (`MRK` §II,
`MSI`/`MSTR` §V). The rest:

| | sector | flow | OBV | rs20 | rs60 | surge | short verdict | fwd P/E · target |
|---|---|---:|---|---:|---:|---:|---|---|
| `COIN` | Financials | **+1.000** | 매집 +0.289 | +14.2 | +5.3 | 1.68 | △ normal (z +0.81) | — |
| `MSTR` | Info Tech | **+1.000** | 매집 +0.361 | **+26.5** | **−24.7** | 1.61 | ✅ **low-short / covering — the only "clean rise"** | — |
| `TGT` | Cons. Staples | +0.950 | 매집 +0.289 | +17.3 | +26.9 | 1.51 | △ (z +1.22, 5v5 −4.2▼) | **17.41** · $165.44 vs **$161.62 = −2.3% (ABOVE target)** |
| `ECL` | Materials | +0.606 | 매집 +0.174 | +1.2 | — | 1.40 | △ (z −0.07) | — |

🚨 **`COIN` and `MSTR` are ONE risk unit in two GICS labels** (bitcoin beta). **A third of the entire
green set is one factor**, and the sole "clean rise" verdict lands on the **most** factor-concentrated
name — whose rs20 (+26.5) and rs60 (−24.7) disagree by **51.2pp**.
⚠ **`TGT` is in the sector whose verdict is BLOCKED** (`WMT` at 28.9% owns the sign, `R82`+G3), so it
cannot inherit a sector call. `TGT` +0.950 🟢 vs `WMT` −0.333 🔴 = **17.1pp** intra-sector (`W5`), and
`WMT`'s weakness has a **named dated cause**: *"Walmart shares tumble as sales growth slows"*, **peak
19 outlets 08-19→08-22**.
★ **Three of the four names with a consensus target here or in §II trade ABOVE it** (`MRK` −3.1%,
`TGT` −2.3%; and `VLO` −10.4% on 08-22). **The names the gate selects are the ones consensus has
already caught up to.**

---

## §VII · Cycle-exposure / epicenter-starter module

`cycle_exposure.py`: **AI-compute epicenter 16.52% (need ≥12.0) ✅ · Energy/refining 9.84% (need ≥8.0)
✅ · Missile-defense 3.79% ⚪ (no threshold).** **No top-rank cycle GAP** ⇒ **no epicenter-starter is
required and none is written.**

🚨 **Two cycles cannot be measured at all, and that is not the same as zero:**
1. **Optical / interconnect** — no registry row (`D250`/`M731`). `LITE` +0.639 (blocked on surge 0.95),
   `COHR` +0.158, `CIEN` −0.380 🔴 rs60 −34.0.
2. ★ **Custom-silicon / merchant-ASIC — no registry row either** (new this run, `M838`). The book's
   16.52% "epicenter" conflates *sells the accelerator* (`NVDA`, `ANET`) with *co-designs someone
   else's* (`AVGO`), and 08-19 moved them apart. **`label_split_across_units` ⇒ the theme cap is
   currently TOO TIGHT on this book — a human call, stated not acted on (P4).**

---

## §VIII · Ledger writes — every name set aside leaves a record

**Rejections filed this run: 0.** No name was examined and set aside with a stated reason on its own
merits; the names below were **surfaced and not carded**, which is a *miss*, not a rejection, and the
boundary is machine-enforced (`missed_ledger add` refuses a ticker×date already in the rejection ledger).

**Misses filed at EVENT_ALPHA (5)**: `MU` · `SNDK` · `LRCX` · `STX` (`Q.확신부족`, recheck **09-03**)
and `MRVL` (`R.타이밍대기`, recheck **09-19**).

**Misses filed at BET (this section, 6)** — screener/shortlist names that reached this sheet and did
not become candidates:

| Ticker | class | why, in one line | enters-if | recheck |
|---|---|---|---|---|
| `REGN` | `Q.확신부족` | Sector's 2nd-highest OBV (+0.656) with rs20 +23.5 / rs60 +30.8, blocked from 🟢 by `vol_surge` 0.79 alone | `vol_surge ≥ 1.2` with OBV 매집 and rs20 > 0 maintained, **or** the US desk accrues its own `ic_ledger` and `vol_surge` clears | 2026-09-19 |
| `ABT` | `Q.확신부족` | rs60 **+34.1**, OBV +0.461, blocked on surge 0.75 alone | same | 2026-09-19 |
| `CAH` | `U.발굴부재` | Screener leader-pullback (RSI 41.6) but sits in the **managed-care/distribution node that is the sector's entire drag** — flow −0.252, zero 매집 in that node | flow_score > 0 **and** OBV turns 매집 | 2026-09-19 |
| `ISRG` | `Q.확신부족` | Screener de-rate snapback, OBV 매집 +0.294, but **rs60 −11.5** — the only participating HLTH name with a negative 60-day | rs60 vs `SPY` > 0 with OBV 매집 maintained | 2026-09-19 |
| `VST` | `S.테마회피` | **Consensus target +61.9% above spot at fwd P/E 13.14** while carrying the sector's worst rs20 (−20.3) and OBV 분산 −0.340. Story-vs-tape at maximum width; left out on the tape | OBV turns 매집 **and** flow_score > −0.20 (Card 6's own kill condition) | 2026-09-03 |
| `COP` | `M.숏리스트탈락` | OBV 매집 +0.259, rs20 +8.5, rs60 +15.1 — **fails 🟢 on `vol_surge` 1.05 alone**, i.e. excluded by the axis measured negative in the KR ledger | `vol_surge ≥ 1.2` maintained with the other two axes, **or** a US `ic_ledger` measurement on `vol_surge` | 2026-09-19 |

⚠ **Sign hygiene**: the miss ledger's `excess > 0` means *missing it cost us*, inverted vs the
rejection ledger. **The two are never summed.**
★ **`T25` carried**: no structural rejection is made this run, so the loss-asymmetry number is not
invoked. **When one is made, it must be re-printed beside it.**

---

## ✅ EXIT CHECK

- [x] **ONE file, per-sector sections §I–§V plus cross-sector §VI** — not split.
- [x] **Candidate set is the wide union** (DEEP thesis names ∪ `us_setup_screener --sector` ×4 ∪
      `US_LIVE_SHORTLIST`), and the cross-sector shortlist names have their own section.
- [x] **Every candidate has §A numbers / §B thesis+freshness placeholder / §C flow / §D peers /
      §E refutation + dated catalyst.** Blanks are stated as blanks (no fabricated multiples).
- [x] **Thesis-confirmation gate honoured**: `COMPANY_SCOREBOARD.md` checked — **KR universe, no US
      row exists** ⇒ confirm-don't-re-derive unavailable, stated rather than assumed.
- [x] **Cycle GAP**: none on the three registered cycles ⇒ **no epicenter-starter written**; two
      unregistered cycles named as **unmeasurable, not zero**.
- [x] **Every name set aside is a scored record** — 6 miss rows filed here with class, `--enters-if`
      and `--recheck-date`; 5 filed at EVENT_ALPHA. **0 rejections**, with the boundary stated.
- [x] **Sizing language is influence-illustration only. Zero buy/sell recommendation (P4).**
- [x] **Linter run on this stage's own output** — `report_lint.py BET_SHEET.md` → **0 findings** after one `D6` fix (an `XOM` OBV citation now carries `flow_score` and `delta` beside it). ⚠ Form only; the linter does not check that the six miss rows were the right six.


---

# §B FRESHNESS TAGS — appended by Stage 10 / L1·ALPHA, 2026-08-23

> ALPHA fills the `§B` freshness placeholders left by BET. Tags follow the **name**, not the sector's
> turn in the rotation, and are carried into the next run's inheritance packet.

## §B-0 · 🚨 The G1 question, answered before any tag is issued

The stage's own rule: *"when G1 FAILs, ALPHA may not issue a freshness verdict at all"* — and **G1
FAILED for the 11th consecutive run** (sweep `vel_coverage` 0.0).

**A freshness verdict IS issued today, and here is the entitlement it rests on.** `PREFLIGHT_US.md`
grants one exception explicitly: **direct `fts` / `theme-age` / `brief` / `thread` calls made OUTSIDE a
sweep window are citable.** Every `theme-age` call below was made after 22:16 KST, i.e. more than
three minutes after the last sweep ended at 22:13, and the pipe was falsification-probed in the same
window: **40 of 40 sweep-silent names returned real counts, 0 true silences** (cumulative **360/360**
over nine runs). Each theme query below also returned a **non-zero base** (138 to 3,887 articles).
⇒ **These are direct observations, not sweep output, and each is stamped as such.**

## §B-1 · ★★★ `F1` is RESOLVED on the US side — and the resolution is that the gate WORKS

The standing `F1` line reads: *"🟢LIVE fired 0 times in 8 consecutive runs because it required a FRESH
theme age the board structurally could not produce — **a gate that never fires looks identical to a
universe with nothing in it**."*

**Today the gate fired.** In the same session, on the same instrument, `theme-age --scope foreign`
returned:

| Theme | Verdict | Age | Velocity | Base |
|---|---|---:|---:|---:|
| **`Treasury buyback`** | 🟢 **FRESH** | **4 days** | — | 178 |
| `Jackson Hole` | 🟡 **ACCELERATING** | ≥90 | **10.67×** | 190 |

⇒ **The instrument produces 🟢FRESH when a theme is genuinely new, and 🟡ACCELERATING at 10.67× when
one re-ignites.** ⇒ **`F1`'s ambiguity is closed for the US desk: the gate is not broken, and the
zero on equity theses is ARITHMETIC.** *(⚠ Scope: this resolves the US instance. The KR count —
**18 consecutive runs** — is a separate measurement in a separate market; `W1`.)*

## §B-2 · The tags

All `theme-age … --scope foreign`, direct calls outside a sweep window, 2026-08-23:

| §  | Thesis | Theme probed | Verdict | Age · velocity · base | **TAG** | Residual / re-check |
|---|---|---|---|---|---|---|
| §I | Refining-capacity constraint | `refining margin` | ⚪ECHO | 4.7 · **0.69×** · 249 | 🟡 **PARTIAL** | ⚪ECHO demands stronger live evidence, and it got it — **from a filing, not from news**: `M831` (no contractual margin floor; a cost floor instead) and `M833` ($36.33/bbl vs $17.58 with utilization 94% vs 97%). **Residual: the FY2025 10-K Item 1A, still unopened.** Re-check **2026-08-28** (`P89`) |
| §II | Pharma/devices accumulation | `pharmaceutical` | ⚪ECHO | 72.6 · 0.90× · **3,887** | 🟡 **PARTIAL** | Broadest participation evidence on the board (**59.4%**), oldest possible theme. **Residual: 18 of 19 participants are gate-blocked on `vol_surge`.** Re-check **2026-08-31** (`S112` rate leg) |
| §II | Managed-care drag | `managed care` | ⚪ECHO | 2.3 · 0.76× · 138 | 🔴 **RESOLVED — as a SHORT-side observation the desk does not express** | The node is uniformly negative (7 of 7 `flow_score` < 0, zero 매집) and the desk holds none of it. **Not a bettable long; logged so "UNH is cheap" cannot resurface.** ⚠ **No rejection row filed** — no name was examined on its merits and set aside; these were never candidates |
| §III | Travel/delivery node | *(no single theme term; node-level)* | — | — | 🟡 **PARTIAL** | Base is real (**rs60 +22.5 to +39.8, all 매집**) but **the sector has NO live falsifier** — `S91` VOIDed 08-22. **Residual: register one.** Re-check **2026-08-28** (`P92`) |
| §IV | AI-power demand | `data center power` | ⚪ECHO | 11.0 · **1.10×** · 601 | 🔴 **RESOLVED — story alive, money absent** | **0 of 15 participation.** ⚠ **`RESOLVED` here is a MONEY verdict on the expression, not a story verdict**: the thread is BUILDING with a named **38-GW** number, so per the stage rule it is **re-filed with a dated re-check, not dropped**. Re-check **2026-09-03** (Card 6 kill condition) |
| §V | Memory cost pass-through | `memory prices` | ⚪ECHO | 15.6 · 0.75× · 914 | 🟡 **PARTIAL** | ⚠ **The ECHO tag and the event disagree, and the disagreement is dated**: the theme term is old, but the *specific* story is **8 outlets, 4 days old, still spreading on 08-23**. **`theme-age` measures the TERM, not the EVENT.** Residual: the 08-26 print. Re-check **2026-08-26** (`P90`) |
| §V | Custom-silicon share shift | `custom silicon` | ⚪ECHO | 15.4 · **1.15×** · 802 | 🟡 **PARTIAL** | The only ECHO theme with velocity **above 1.0** among the equity theses. **Residual: `S116` settles it 08-28.** ⚠ **Momentum-only flag on `MRVL`** — rs20 +18.4 with OBV 매집 agreeing, so **not** a tape trade; but it is **LATE-MONEY** (32.0pp spread realised) and stays a miss-ledger row, not a candidate |
| §VI | Bitcoin-beta greens (`COIN`, `MSTR`) | — | — | — | 🟡 **PARTIAL, momentum-only stamp** | **rs20 +26.5 vs rs60 −24.7 on `MSTR` — the two horizons disagree by 51.2pp.** Two names, **one risk unit**, a third of the entire green set. **Hard stop required if acted on.** ⚠ `D6`: the accumulation read is **C-grade (OBV only)** — the disagreement **downgrades to 🟡 and is reported**, it does not by itself convert the bet into a tape trade |

**Tally: 🟢LIVE 0 · 🟡PARTIAL 6 · 🔴RESOLVED 2.**
⚠ **Both 🔴s are logged, and neither produced a rejection-ledger row**, because neither was a name
examined and set aside on its merits — one is a node the desk does not express (managed care) and one
is a **money verdict on an expression whose story is still building** (AI-power), which the stage rule
requires be **re-filed with a date rather than dropped**. **The boundary is stated, not assumed.**

## §B-3 · `D295` DISCHARGED — the obligation that had crossed three HANDOVERs

The 08-21, 08-22 packets and this run's HANDOVER all carried: *"`S103`'s `NVDA` bands are hand-set;
`D295` obliges a re-derivation from the straddle before the print."* **Fourth run, print in three days.**

**Discharged this run.** `module_flow NVDA --positioning` returns **`예상변동 ±1.6% (만기 2026-08-24,
D1)`** — an expiry that **does not span the 08-26 print** (`D315`, 4th run). The bands were therefore
taken **directly from the option chain**:

| | expiry NOT spanning the print | **first expiry spanning it** | implied | ATM IV |
|---|---|---|---:|---:|
| `NVDA` | 08-24 ±1.61% (IV 0.280) | **08-28** K=215, straddle **$13.12** | **±6.11%** | 0.606 / 0.588 |

⇒ **`S103`'s ±5.0pp sits INSIDE ±6.11% and is pre-declared NO-INFORMATION.** Per `D242` it is **not
re-banded** and still settles as registered; **`S115`** is the successor, written outside the implied
move. **The pre-commitment is met and the counter stops at four.**

## §B-4 · What ALPHA could not do

- **No US `ic_ledger`** ⇒ `--ic`-derived sizes remain **"mechanical 1/4"** (G6 FAIL: 0.45 files/day,
  2.2× slower than the threshold). `D310` open for a 2nd run.
- **`ACTION_TICKETS.md` was hand-built** — `action_bracket.py` printed *"Nearest binary: NVDA (D-3)"*
  and *"no dated binary in window"* in consecutive lines (**`D294`, 5th reproduction**) on a window
  holding five binaries.
- **Share counts omitted from the tickets by design**, per this run's `Analytical output only` mandate.
  **Logged as a deviation from documented practice.**
