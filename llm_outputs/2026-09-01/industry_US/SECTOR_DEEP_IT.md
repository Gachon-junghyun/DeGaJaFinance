# SECTOR_DEEP_IT — Information Technology · industry_US · 2026-09-01 (Tue) · Stage 8 / L1·DEEP
### ★ PREMORTEM-PROMOTED 5th SLOT — narrow, disjoint mandate

> Flow: `SECTOR_FLOW_US_REPAIRED.json`, 3-axis `nonews`, **asof 2026-08-31**. Benchmark `SPY` inline (`C1`).
> Prices tagged **[live]** are partial bars.

## 0 · Mandate (from PREMORTEM Lens 1 — deliberately disjoint from ROTATION's four)
> *`S124` fired **A at 41 of 56** while `eqflow` reads **−0.014** with 3🟢 against 9🔴.
> **Price and participation disagree inside one sector. Which of the two is describing the money —
> and does the answer survive the `AVGO` print?** Resolve on the NAME level, not the bucket.*

---

## ★ 1 · The two instruments do not disagree. Decomposing the axis shows why.

**`M1208` [measured] — `flow_score` is `(OBV + RS20 + SURGE)/3`, and IT's negative sign comes from
ONE of the three.** Mean clipped axis values across the sector's 56 scored names:

| sector | n | axis **OBV** | axis **RS20** | axis **SURGE** | `eqflow` |
|---|---:|---:|---:|---:|---:|
| **Information Technology** | 56 | **+0.168** | **+0.142** | **−0.353** | **−0.014** |

★ **Both direction axes are POSITIVE. The volume axis alone drags the sector below zero.**
`(+0.168 + 0.142 − 0.353)/3 = −0.014` — the printed number, reproduced from its parts.

⇒ **`S124` (a return measurement) and `eqflow` (a 3-axis composite) are not in conflict.** They agree
on direction and disagree only because one of them also prices **participation**, and participation is
falling.

## 2 · And it is not an IT phenomenon — it is the whole board

**`M1209` [measured] — the universe's negative flow is a VOLUME reading, not a direction reading.**

| | universe mean, 299 names |
|---|---:|
| axis **OBV** | **+0.034** |
| axis **RS20** | **−0.079** |
| axis **SURGE** | ★ **−0.326** |
| names with `vol_surge ≥ 1.0` | ★ **41 of 299** |
| **median `vol_surge`** | ★ **0.77** |

Two of the three axes sit within 0.08 of zero; the third is **−0.326**. ⇒ **"the board is red"
(`wflow` −0.156, 6🟢 / 84🔴) is, arithmetically, "market-wide volume is contracting into the end of
August."** Every sector's surge axis is negative — the only one near zero is **Energy (−0.086)**,
which is precisely the sector this run confirmed on every other measure.

⚠ **And the desk's own scoreboard says this axis has the wrong sign.** `ic_ledger score`:
`vol_surge` **h=1, n_eff 41.0, mean IC −0.0417, t(NW) −3.51 — the only cell that passes Bonferroni**,
and its sign is **negative**, i.e. high surge has predicted *lower* forward returns.
🚫 **This run does NOT act on that.** The ledger is `market=kr`; flipping a US reading on a KR
measurement is the `W1` violation the repo keeps logging (`D428`, unmet). **The observation is carried;
the gate is untouched.** ⇒ **`D460`**: *when a composite score's sign is carried by a single axis,
the run states which axis and what that axis's own measured IC sign is, before the score is used as
evidence.*

## 3 · Name level — where price and participation actually part company

`exc5` = 5-session excess vs `SPY`, settled closes, 08-24 → 08-31 (`SPY` **+0.47%**).
**Sign agreement between `exc5` and `flow_score`: 35 of 56 (62.5%).**

**Group means, and this is the resolution in two numbers:**

| group | n | mean `vol_surge` | mean `obv_norm` |
|---|---:|---:|---:|
| `exc5` > 0 | **41** | **0.822** | **+0.094** |
| `exc5` ≤ 0 | 15 | 0.718 | −0.027 |

★ **Both groups are below 1.0 on volume.** The winners did not attract volume; they **shed less** of
it. OBV separates the groups cleanly (+0.094 vs −0.027) — so **accumulation did discriminate**, and
**surge did not**.

### 3a. The 18 names where price rose and participation fell — the mandate's real content
| ticker | `exc5` | flow | OBV | surge | `rs60` vs `SPY` | node |
|---|---:|---:|---:|---:|---:|---|
| `CDNS` | **+6.77** | −0.007 | +0.012 | 0.98 | −19.0 | EDA |
| `DELL` | +4.80 | −0.119 | −0.098 | 0.77 | +6.7 | Hardware |
| **`DDOG`** | +4.52 | **−0.631 🔴** | −0.087 | 0.79 | −4.0 | Software |
| **`APP`** | +4.04 | **−0.806 🔴** | −0.288 | 0.75 | **−45.5** | Software |
| `STX` | +3.78 | −0.056 | +0.104 | 0.63 | −11.9 | Storage |
| `KEYS` | +3.41 | −0.231 | −0.083 | 0.97 | −7.3 | Instruments |
| **`WDC`** | +3.02 | **−0.861 🔴** | −0.166 | 0.65 | **−23.0** | Storage |
| ★ **`AVGO`** (held) | **+2.76** | **−0.616 🔴** | −0.133 | 0.90 | **−12.9** | Semis |
| `AMD` | +2.59 | −0.287 | +0.051 | 0.60 | −11.3 | Semis |
| `ON` | +2.53 | −0.394 | +0.091 | 0.55 | −45.1 | Semis |
| `CIEN` | +2.45 | −0.413 | −0.020 | 0.58 | −29.8 | Optical |
| `GLW` · `APH` · `TEL` · `IBM` · `NXPI` · `COHR` · `TXN` | +1.72 … +0.29 | all negative | mixed | 0.47–0.83 | −8 to −36 | components / semis |

### 3b. The 3 names where participation rose and price fell — the mirror, and it is thin
| ticker | `exc5` | flow | OBV | surge | `rs60` |
|---|---:|---:|---:|---:|---:|
| `SHOP` | −2.09 | **+0.472** | **+0.456** | 0.65 | **+25.7** |
| **`INTU`** | −3.34 | **+0.831 🟢** | +0.148 | **1.34** | +17.7 |
| **`MRVL`** | **−8.16** | +0.367 | −0.013 | **1.11** | **−34.4** |

★ **`M1210` [measured] — `MRVL` is the sharpest single name in the sector.** It is **the worst
5-session performer among the 56** (`exc5` −8.16) with `rs60` **−34.4 vs `SPY`**, and yet it is one of
only **two IT names with `vol_surge` above 1.1** and its `rs20` is **+8.0**. **Volume is arriving into
the deepest-discounted large-cap semi in the sector, four sessions before `AVGO` prints.**
⚠ This is a **description of two axes moving apart**, not a recommendation (P4), and `MRVL` is **not**
handed to BET — its OBV is **−0.013**, i.e. flat, so the "conviction" leg the 🟢 gate requires is absent.

## 4 · Does the answer survive the `AVGO` print? — the second half of the mandate

**`AVGO` is the test case for §3a in one name**: `exc5` **+2.76** (price up) with flow **−0.616 🔴**
and OBV −0.133 (participation down), `rs60` **−12.9 vs `SPY`**, **and it is held.**

**Fundamentals say the de-rating is NOT an estimate cut** (`module_fundamentals_us`):

| | `AVGO` | `MU` (for contrast) |
|---|---|---|
| Trailing / **Forward P/E** | 60.65 / **18.59** | 21.27 / **6.06** |
| PEG | 0.42 | **0.14** |
| **estimate momentum, 90-day change** | current-qtr **+1.6%** · current-yr **+2.7%** · next-yr **+6.0%** | current-qtr **+38.1%** · current-yr **+25.9%** · next-yr **+50.9%** |
| target mean vs price | $525.97 = **+44.5%** | $1,513.41 = **+61.0%** |
| recommendations (30d) | **8 SB / 37 B / 4 H / 0 S** | 9 SB / 34 B / 4 H / 0 S |

★ **`M1211` [measured] — `AVGO` and `MU` are the same forward-multiple story with opposite
denominators.** `MU`'s estimates have been revised **+50.9% in ninety days** (the peak-margin /
low-multiple trap shape, lens **B2**) while **`AVGO`'s have barely moved (+2.7% current-year)** — so
`AVGO`'s `rs60` −12.9 is a **multiple de-rating against a flat denominator**, not a downgrade cycle.
⚠ **The margin percentile for both is `unknown` (`C3`)** — no US gross-margin history is wired
(`scripts/margin_history.py` exits 1, PREFLIGHT G7) ⇒ **neither is called cheap in this file.**

**Priced move**: `module_flow AVGO --positioning` reads **±9.6% (expiry 2026-09-02, D1)**, options
**P/C 1.73**, IV skew **−3.3**, short **1.2% of float, covering, DTC 3.0** ⚠ **live partial bar**.
⇒ `S132`'s ±9.00pp threshold now sits **inside** the priced move and is pre-declared no-information
(`M1197`); **`S138` was registered at ±11.00pp, outside it.**

**Answer to the second half**: **the print cannot settle §1–§3, because the mandate is a
participation question and one earnings reaction is a price event.** What it *can* settle is the
`AVGO`-specific leg, and **`S138` is the row that does it.** ⇒ **`S140` (registered this run, settles
09-08) is the row that actually re-tests the breadth**, using `S124`'s identical construction.

## 5 · Contract terms and the frame-transfer question — answered
> *Does the take-or-pay / floor-ceiling frame the desk trusts on `KMI`, `LNG` and `MU` apply here?*

**Checked, and it splits the sector — and the split is the reason §4's two names diverge.**
- **`MU`: YES, and it is on record.** `R111` (retracted 08-30) established from the **FY26Q3 10-Q**
  that strategic customer agreements are **take-or-pay with binding multi-year volumes, a ceiling at
  ~the 2Q CY2026 market price, and a floor for the term**, with management stating that at *floor*
  pricing gross margin runs above any prior cycle's peak. ⇒ ⚠ **the contract-price QoQ deceleration
  (+90~95% → +58~63% → +13~18%) must NOT be read as demand weakening — it is arithmetic hitting a
  cap.** The desk's rule is explicit: *check for a band before reading a second derivative as a demand
  signal.* **Checked; the band exists.**
- **`AVGO`: `unknown` (`C3`).** ⚠ **`module_disclosure_us AVGO` was NOT called this run** — the
  filing budget went to `SLB`. **The contracted share of `AVGO`'s custom-ASIC revenue is not read**,
  so **no "the margin must mean-revert" claim is made about `AVGO` anywhere in this file.** Named as
  the single most valuable unopened document for the next run, four days before the print.
- **The rest of IT: NO.** Software (`CDNS`, `DDOG`, `APP`) is subscription-recurring, which is a
  *retention* structure, not a price floor; hardware and components are spot.

★ **Transferable point**: the desk's own `M-` record notes that 21 files applied take-or-pay to
midstream/LNG/utilities and **zero** applied it to memory until `R111`. **The same asymmetry now
exists one layer over**: the frame has been applied to `MU` and **not once to the custom-silicon
node** whose largest name prints in ≤48h.

## 6 · Customers named, and their disclosed spend (rule A6)
- **`AVGO`'s** customers are the hyperscalers. Their disclosed spend is arriving as **contracted
  capacity, and the unit has become the gigawatt**: Anthropic's **$35bn** Lambda contract (BUILDING
  4→4), *"Sundar Pichai says Alphabet can't build AI capacity fast enough, and Anthropic has secured
  **5 gigawatts** of it"* [09-01]. ⇒ **the demand side is corroborated and dated.**
- ⚠ **And the counter-evidence, same window, same sourcing standard**: *"Analysis — Texas' halt on
  powering data centers reflects US reckoning over **'ghost' demand**"* [reuters via yahoo_finance +
  cna, 09-01], with *"AI Power Demand Is Exploding, But How Much Actually Gets Built"* [13 outlets].
  ⇒ **the buyers' announced spend and the buyers' ability to energize it are diverging**, and the
  equity tape sides with the second (every AI-power name 🟡 or 🔴 — PREMORTEM Lens 4).
- **`MU`'s** customer statement arrived from an unusual direction this window: **Tim Cook's last
  warning as Apple CEO was that memory-chip shortages "won't improve any time soon"** [nasdaq ·
  yahoo_finance · fool, 09-01; thread BUILDING 7→…→21]. ★ **A buyer saying the input is scarce is a
  better corroborator of a supplier thesis than the supplier saying it.**

## 7 · Dispersion (lens B5) and the sub-node map
`flow_score` spans **`CRM` +1.000 to `AMAT` −0.889 = 1.889 inside one sector** against an `eqflow` of
−0.014. **The label is the wrong unit — for the fifth sector in a row this run.**

`design/EDA` → `foundry & equipment` → **`memory`** → `logic/custom ASIC` → `interconnect & optical`
→ `systems/hardware` → `software & platforms`

| node | tone | evidence |
|---|---|---|
| **Software** | ★ **the only strong node** | `CRM` **+1.000 🟢** (OBV +0.326, `vol_surge` **1.90 — highest on the board**), `INTU` +0.831 🟢, `NOW` +0.661, `PANW`/`CRWD` `rs60` +35.5/+27.2 |
| **Memory** | **splitting** | `MU` +0.270 (Δ +0.255) and `SNDK` +0.481 (Δ +0.343) accumulating vs **`WDC` −0.861 🔴** (`rs60` −23.0) — see EVENT_ALPHA Card 1 |
| **Equipment** | ★ **the weakest node on the whole board** | `AMAT` **−0.889** (the universe's worst), `KLAC` −0.556, `LRCX` −0.195 |
| **Logic / custom ASIC** | de-rated, estimates flat | `AVGO` −0.616 🔴, `MRVL` +0.367 (volume arriving), `NVDA` +0.246 (OBV **−0.098** with `vol_surge` **1.39** — the crowded-layer shape) |
| **Interconnect / optical** | **diverging** | `LITE` +0.533 (OBV **+0.284 매집**) vs `COHR` −0.188 (**Δ −0.805, the universe's worst**) — `S137` settles 09-09 on the *average* of these two |
| **Hardware** | mixed | `DELL` −0.119 (Δ −0.463), `HPE` −0.054 (held, Δ −0.493), `STX` −0.056 |

**chain-hop** (`chain-hop "optical transceiver" --days 7 --scope foreign`): body-proximate candidates
**`MRVL`** (3 prox / 3 body) and **`LITE`** (2/2), from *"AI Chips Update — Optical Transceivers Propel
AI Data Center Growth"* and *"AI-Driven Optical Transceiver Investment Surges…"*. ⚠ `AAPL` also
surfaced but from a **China-IPO article** — **rejected as a co-mention, not a chain relationship.**
⇒ **two admissible candidates, and both are already inside the sector** (no new name reaches BET from
this hop; `MRVL`'s OBV is flat and it fails the conviction leg).

## 8 · Track KPIs and anti-signals
| KPI | now | what settles it |
|---|---|---|
| ★ **IT positive-`exc5` count** | **41 of 56** (p85 = 39) | **`S140`, settles 2026-09-08**: A ≥ 39 / B ≤ 20 |
| **universe median `vol_surge`** | **0.77**, 41 of 299 ≥ 1.0 | a return above 1.0 median ⇒ the board's red turns without a single price changing |
| IT axis decomposition | OBV **+0.168** · RS20 **+0.142** · SURGE **−0.353** | **OBV turning negative** ⇒ the disagreement becomes a real one |
| `AVGO` 1-session excess post-print | — | **`S138`, ±11.00pp**, outside the ±9.6% priced move |
| `MRVL` `vol_surge` / OBV | **1.11 / −0.013** | OBV turning 매집 ⇒ the §3b divergence becomes a conviction signal |
| `MU` Δ | **+0.255** | a turn negative kills EVENT_ALPHA Card 1's supplier leg |

**Anti-signals that would kill this file's reading**: (i) OBV going negative sector-wide while price
breadth holds — that would make the participation objection real rather than volumetric; (ii) a GICS
reclassification (also `S140`'s VOID clause); (iii) evidence that `vol_surge` is mis-computed rather
than merely low — **not** checked this run, and named as an open question given `M1209`.

## 9 · Handed forward
- **To BET (CONFIRMED-EARLY, unsized)**: **`MU`**, **`SNDK`** (EVENT_ALPHA Card 1's supplier leg),
  **`LITE`** (single name, not an optical basket). ⚠ **`CRM` and `INTU` are the sector's two 🟢 names
  and are handed as shortlist rows, with `CRM`'s `vol_surge` 1.90 flagged as a top-risk reading.**
  **`MRVL` is explicitly NOT handed** (OBV flat = no conviction leg).
- **Held-name read**: **`AVGO`** — de-rated on a **flat** estimate line, `exc5` **+2.76** with flow
  **−0.616 🔴**; prints in ≤48h; `S138` is the informative row and `S132` is not. **No sizing** (P4).
- ★ **To the next ROTATION — the mandate's answer**: *neither instrument is wrong.* **IT is positive
  on both direction axes and negative only on volume, and so is the whole board.** ⇒ **`IT N` was not
  refuted by `S124`, and it was not confirmed by `eqflow` either** — the two were measuring different
  things and the desk spent three runs treating that as a contradiction. **`S140` settles the part
  that is actually testable.**
- **To the desk (`D460`)**: *state which axis carries a composite's sign, and that axis's own measured
  IC sign, before using the composite as evidence.*
