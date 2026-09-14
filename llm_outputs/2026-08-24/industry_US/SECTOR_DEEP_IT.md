# SECTOR_DEEP_IT — Information Technology · industry_US · 2026-08-24 (Mon) · Stage 8 / L1·DEEP
### 5th slot — **PREMORTEM-PROMOTED** (Lens 1). Narrow, disjoint mandate.

> All flow figures `asof 2026-08-21`; `exc` = excess return vs **`SPY`** (named inline). Option data
> is a **LIVE INTRADAY** read from the chain (spot 08-24 post-open) and is labelled at every use.
> ⚠ Declared deviation, 7th run: in-context serial execution, not a parallel agent fan-out.

## 0 · The mandate, and it is deliberately narrow

PREMORTEM promoted this slot to answer **one** question, disjoint from the other four DEEPs:
*"§0-a — is `NVDA`'s 08-26 print carrying information about the PRINTER or about the MEMORY LAYER?"*
Plus ROTATION's routed question: *"`exc5 −2.655` vs `exc20 +1.992` disagree in sign — what is that?"*

★ **Both answers are the same object. The sector is two businesses with a 19pp gap, and the memory
sub-node sits at the intersection of the board's HIGHEST implied volatility and its WORST realised
participation.**

## 1 · ★★★ The sign split, resolved: software and semis are 19pp apart on 20 sessions (`M876`)

| Sub-node | n | wflow | eqflow | **exc5 vs `SPY`** | **exc20 vs `SPY`** | participation |
|---|---:|---:|---:|---:|---:|---:|
| **Software + IT services** | 19 | **+0.345** | **+0.248** | **+1.86** | ★ **+13.04** | ★ **63.2%** |
| **Semis + semi equipment** | 20 | **−0.341** | **−0.466** | **−4.47** | **−6.13** | 🚨 **5.0%** |
| Hardware / components | 17 | −0.467 | −0.066 | **−5.57** | −0.80 | 23.5% |
| ★ **Memory / storage** (`MU` `WDC` `SNDK` `STX`) | 4 | −0.245 | −0.235 | **−5.04** | −2.56 | 🚨 **0.0%** |
| *Sector as graded* | 56 | −0.231 | −0.102 | −2.65 | +1.99 | 30.4% |

⇒ ★★★ **ROTATION's sign split is an aggregation artifact and nothing else.** Software `exc20`
**+13.04** against semis **−6.13** = a **19.17pp** gap; the sector line `+1.99` is their weighted
average and describes neither. **The decline to demote IT was correct, and now it is correct for a
measured reason rather than a `C5` abstention.**
- Software's leaders are broad and heavy on RS: `PLTR` **exc20 +42.76** · `NOW` +26.44 ·
  `CRM` +24.18 · `ORCL` +23.75 · `MSFT` +22.98 · `SHOP` +18.42 (rs60 +38.0) · `INTU` +17.2 (rs60).
  ⚠ **`ORCL` carries `exc20 +23.75` with `exc60 −25.33`** — a 49pp reversal inside 60 sessions; the
  `DELL` shape (see §4).
- **Semis participation is 1 name in 20.** The tail is uniform: `TXN` −0.806 · `NXPI` −0.800 ·
  `MCHP` −0.789 · `ARM` −0.756 · `AMAT` −0.766 · `ON` −0.719 · `KLAC` −0.699 · `QCOM` −0.691 ·
  `AMD` −0.683 — nine names below −0.68, all OBV 분산 or 중립.

## 2 · ★★★ THE MANDATE'S ANSWER — the options market prices NVDA's print as a MEMORY event (`M874`)

**LIVE INTRADAY, read from the option chain because `module_flow --positioning` broke on this exact
name** (§3). Identical expiry **2026-08-28** for all four:

| Name | Prints in window? | ATM straddle / spot | ATM IV (call / put) | **flow (08-21)** | **participation leg** |
|---|---|---:|---|---:|---|
| **`NVDA`** | ★ **YES — 08-26** | **±6.13%** | 0.692 / 0.617 | −0.181 🟡 중립 | rs20 +0.2, OBV 중립 |
| `MU` | **no** — 09-24 | **±6.52%** | **0.770** / 0.639 | −0.278 🟡 중립 | rs20 +1.4, OBV 중립 |
| `SNDK` | **no** | **±8.41%** | ★ **0.926** / 0.884 | +0.144 🟡 중립 | rs20 +7.5, OBV 중립 |
| `WDC` | **no** | ★ **±11.56%** | **0.880** / 0.708 | **−0.781 🔴** | rs20 **−15.2**, OBV **분산** |

★★★ **Three memory/storage names with NO scheduled event in the window all carry HIGHER ATM implied
volatility than the name that actually prints, and `SNDK` at 0.926 is 1.34× `NVDA`'s 0.692.**
`S117` was registered on a **1.07×** version of this (MU 0.650 vs NVDA 0.606). **Today it is 1.34× and
it is three names, not one.** ⇒ **The mandate is answered: the market prices the information content
of NVDA's print as being about the memory layer.**

🚨 **And the realised tape says the exact opposite — that is the finding, not a footnote.**
**Memory/storage participation is `0.0%` (0 of 4).** The sub-node carrying the board's **highest
implied volatility** carries its **worst realised accumulation**, with `WDC` at `exc20 −15.24`, **rs20 −15.2** and OBV 분산 *(RULE D6 — grade-C, cited beside two price axes, never alone)*. **Highest expected move, lowest evidence of anyone positioning for it.**
⇒ **`S118` (registered today at PREMORTEM, settles 08-28) brackets exactly this**, with a **±6.50pp
relative threshold — outside `NVDA`'s own ±6.13% implied move**, so it can carry information rather
than re-describe what is priced.

**Mechanism, `[measured]` and inherited rather than re-derived** (`M818`): `NVDA` notified customers of
**>15% server price increases with MEMORY COSTS named as the cause** (8 outlets, 08-22/23), alongside
Samsung's up-to-15% foundry increase (08-19). `P90` brackets whether that is **margin expansion or
cost pass-through** and settles on the print.
★ **The two rows are complementary, not redundant, and this file states which is which**: `P90` asks
*what the increase means for NVDA*; `S118` asks *which layer the market gets paid on*. **`S118` can
fire while `P90` fires either way.**

## 3 · 🚨 The instrument that sets thresholds broke on the one name that mattered (`M873`)

`module_flow NVDA --positioning` returned **`예상변동 ±1.3% (만기 2026-08-24, D0) → 안일(연료적음)`** —
it priced **the expiry that expires today**, two days before the print, and rendered the verdict
**"complacent, little fuel."** The correct 08-28 read is **±6.13%, i.e. 4.7× larger.**
⚠ **The same call on `MRVL` picked correctly** (08-28, D4, ±11.2%). **`D315`, 5th run, and this is its
worst instance: silent, intermittent, and it produces a confident wrong adjective on a 🔀binary held in
both books.** All thresholds in this file and in `S118` are read from the chain directly.

## 4 · Value chain, 7 nodes left → right, binding constraint marked

`EDA / IP (`SNPS` `CDNS` `ARM`)` → `wafer equipment (`AMAT` `LRCX` `KLAC` `ASML`)` →
**`memory / storage (`MU` `SNDK` `WDC` `STX`)` ← BINDING** → `logic / accelerator (`NVDA` `AVGO` `AMD`)`
→ `interconnect & optics (`ANET` `LITE` `COHR` `CIEN` `APH`)` → `system / server (`DELL` `HPE`)` →
`hyperscaler demand`

- **Binding constraint = memory**, and it is the issuer's own attribution, not this desk's inference:
  the >15% server price increase names **memory costs** as the cause. **Strong demand is not a
  bottleneck; the memory bill is.**
- ⚠ **`A6` — name the customers and check their disclosed spend.** The hyperscaler node's cash
  position is visibly tightening: **`AMZN` free cash flow went NEGATIVE by $7.6bn** (`brief` 08-23
  head, 25 articles / 5 outlets) and **Alibaba raised $10.2bn in Hong Kong explicitly to fund AI**
  (7→9 outlets). ⇒ **Two independent signs that the buyer side is financing rather than self-funding.**
  **`META`'s and `GOOGL`'s next capex disclosures are the dated measurement** and were not opened here.
- 🚨 **The interconnect/optics node has NO row in `cycle_registry.json`** (`D250`/`M731`, 4th run):
  `LITE` **+0.639 OBV 매집** · `COHR` +0.158 · `CIEN` **−0.380 🔴 rs60 −34.0** · `APH` +0.131.
  ⇒ **exposure is unmeasurable, not zero**, and PREMORTEM Lens 4 escalated it.
- ★ **Node-level exhaustion, flagged with `D6`/`W5` discipline**: `DELL` **exc60 +42.8 with exc20 −2.6
  and OBV 분산**; `HPE` **exc60 +41.65 with exc5 −7.59** (held). **The system node's 60-day numbers are
  historic on both names**, and `S110` (the `HPE`−`DELL` pair test) is the armed row on it.

## 5 · The book's exposure, stated because four of eleven names are here

`NVDA` −0.181 🟡 · `AVGO` −0.221 🟡 (rs60 **−14.7**) · `ANET` +0.417 🟡 매집 (rs60 +20.2) ·
`HPE` +0.489 🟡 매집 (rs60 +41.65).
⚠ **`D329`/`M837` binds and must be quoted with its window**: at `--days` **250/500/750**, `risk_units`
puts **`NVDA` as a singleton in ALL THREE** and **never groups it with `AVGO`**, while `ANET`+`AVGO`
merge at 500d and 750d. ⇒ **the single `AI-compute-EPICENTER` label spans 2–3 measured risk units**,
`label_split_across_units`, **theme cap too tight** — a human call.
★ **The only two AI-compute names with BOTH RS legs positive and OBV 매집 are `ANET` (held) and `MRVL`
(not held, prints 08-27).** `MRVL` reads **🟢가속, news velocity 1.67×, OBV 매집, rs20 +15.5%** on a
**LIVE INTRADAY** pull, with short interest **4.8% of float and BUILDING** into the print — squeeze
fuel on a dated trigger. **It is in the miss ledger (`M.숏리스트탈락`), not handed to BET**, because
it fails the 🟢 gate on `vol_surge` **0.85** alone.

## 6 · Track KPIs and anti-signals (observables, dated)

| KPI | Reading now | Kills the thesis if |
|---|---|---|
| Software − semis `exc20` gap | **19.17pp** | ≤ **5pp** by **2026-09-08** ⇒ the two-business reading dissolves and IT must be graded as one |
| Memory/storage participation | 🚨 **0.0% (0/4)** | ≥ 50% ⇒ the "highest IV, lowest positioning" contradiction resolves toward the options market |
| `SNDK` ÷ `NVDA` ATM IV, same expiry | **1.34×** | ≤ **1.00×** post-print ⇒ `S117`/`M874`'s inference is falsified |
| **`S118`** `EW{MU,SNDK,WDC}` − `NVDA`, 08-26→08-28 | armed | **A ≥ +6.50pp** (memory) / **B ≤ −6.50pp** (NVDA) — both **outside** the ±6.13% implied move |
| Semis participation | **5.0% (1/20)** | ≥ 30% ⇒ the semi tail has turned and the sector's negative half is gone |
| Hyperscaler self-funding | `AMZN` FCF **−$7.6bn`; `BABA` raised $10.2bn | a hyperscaler guides capex **down** ⇒ breaks the volume leg AND the price leg together (`B4`: this is the asymmetric branch) |
| `cycle_registry` optical row | **ABSENT, 4th run** | *(not a market KPI)* — until it exists, optical exposure is **unmeasurable, not zero** |

## 7 · Verdict for BET (analysis only — no sizing, P4)

**IT stays `N`, and the grade is now a deliberate average of two opposite businesses rather than an
abstention.** Any BET sentence about IT must name **which sub-node**; grading software and semis
together is the `W5` error this file exists to prevent.
**Three constraints travel with it:**
1. **The board's highest implied volatility sits on the node with zero participation** (memory/storage).
   `S118` is the bracket; **no name is handed forward from this leg** — a card that arrives D-2 into a
   🔀binary is a timing note, not an entry.
2. **`module_flow --positioning` cannot be trusted for threshold-setting on an event name** (`D315`,
   5th run). Read the chain.
3. **The `AI-compute-EPICENTER` label spans 2–3 measured risk units at `--days` 250/500/750** — every
   concentration sentence carries its window.

---
*Analytical output only. No buy/sell recommendation, no sizing (P4).*
