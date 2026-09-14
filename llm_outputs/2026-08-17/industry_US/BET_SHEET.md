# BET_SHEET — industry_US · 2026-08-17 · Stage 9/11 (L1·BET)

> ONE file, per-sector sections. Downstream desks glob this exact filename — never split it.
> **Analytical only. Zero buy/sell recommendation. Sizing language is influence-illustration (P4).**

## 0 · Reading rules that bind every number below

| Rule | Applied |
|---|---|
| **Price vintage is split and labelled** | Flow / RS / OBV / `vol_surge` / short-z = **settled 2026-08-14**. Valuation multiples and `price` = **live intraday, pulled 22:5x KST = 09:5x ET**. **The two are never compared to each other** (PREFLIGHT G0) |
| **`flow_score` is a 3-axis score** | coverage 17.06% ⇒ the news axis is dropped. Stated on the same line as every conclusion drawn from it |
| **Green counts are the ADMISSIBLE count** | 5 of 9 (`SWEEP_READ §2`). `CVX` `CSCO` `BAC` `MA` are green on velocity alone and are marked 🚫 throughout |
| **Concentration** | ⚠ **No single-number concentration guard** (PREFLIGHT G4, 8th run). Any unit statement carries its `--days`: at **250d** `AVGO`/`NVDA` and `ANET`/`ETN` are **separate**; at **500d and 750d** both pairs **merge** |
| **Sizing** | ⚠ `kelly_size --ic` is **not** evidence-backed this run (G6, ETA 2.4× the limit) ⇒ any size is **"mechanical ¼"** and none is computed here |
| **Date-clustering** | `MPC`/`PSX`/`VLO` moved in the **same five sessions on the same driver** ⇒ **n≈1, not n=3.** "Three names confirm it" is unavailable |

---

## §A · Numbers — the candidate set, cross-checked

Live prices 22:5x KST. Blanks are blanks.

| Name | Sector | px (live) | fwd P/E | trail P/E | PEG | P/S | P/B | mcap | tgt median | **px vs target** |
|---|---|---|---|---|---|---|---|---|---|---|
| `MPC` | ENRG | 361.84 | **11.24** | 12.56 | 1.76 | **0.69** | 5.37 | $101.6B | 322.00 | 🚨 **+12.4%** |
| `PSX` | ENRG | 237.89 | **11.32** | 13.58 | 1.35 | **0.62** | 3.01 | $95.4B | 220.00 | 🚨 **+8.1%** |
| `VLO` | ENRG | 346.98 | 12.27 | 14.46 | **4.08** | 0.75 | 4.32 | $99.9B | 323.00 | 🚨 **+7.4%** |
| `COHR` | IT | 344.69 | 24.73 | 83.87 | **0.92** | 9.47 | 6.19 | $67.4B | 420.00 | **−17.9%** |
| `LITE` | IT | 953.58 | 28.88 | *(blank — no trailing EPS)* | **0.63** | **28.03** | **22.99** | $84.5B | 1121.00 | **−14.9%** |
| `KKR` | FIN | 110.29 | **14.93** | 35.12 | **0.59** | 3.94 | 3.51 | $101.9B | 126.00 | **−12.5%** |
| `ABNB` | DISC | 182.14 | 29.67 | 41.58 | 1.97 | 8.29 | 13.78 | $109.1B | 175.00 | +4.1% |
| `TGT` | STPL | 153.78 | 17.02 | 20.31 | 2.87 | 0.66 | 4.26 | $69.8B | 146.50 | +5.0% |

★★ **The pattern §A exists to surface: the five names with the strongest recent price action are all
ABOVE consensus target median, and the three with the weakest are all 12–18% BELOW it.**
`MPC` +12.4% · `PSX` +8.1% · `VLO` +7.4% · `TGT` +5.0% · `ABNB` +4.1% **vs** `COHR` −17.9% ·
`LITE` −14.9% · `KKR` −12.5%. ⚠ **This is not a valuation verdict** — sell-side targets lag price by
construction and a target median is a **crowd-consensus artifact, not a measurement** (C5-adjacent).
It is reported because it inverts exactly with the flow ranking, and that inversion is information.

**XBRL cross-checks, with the failures stated as failures:**
- `MPC` quarterly revenue steps **$34.20B (2026-03-31) → $51.99B (2026-06-30) = +52%**; `PSX` shows the
  same shape (**$32.54B → $51.00B**). 🚨 **Two refiners posting an identical +52%-class QoQ step is a
  period-tagging signature, not an operating event** — almost certainly a 6-month cumulative filed
  against a quarterly tag. ⇒ **Marked `unknown` (C3). No growth figure is derived from it.**
- `LITE` XBRL quarterly revenue **ends 2025-03-29** ⇒ its **P/S 28.03 and P/B 22.99 cannot be
  cross-checked against a filing.** Reported from yfinance only, and labelled.
- `VLO` `quarterly_revenue_xbrl` is **empty**. ⇒ blank stays blank.
- `LITE` has **no trailing P/E** (no trailing EPS) ⇒ blank, not zero.

---

## §B · Thesis and freshness *(ALPHA-filled, 2026-08-17)*

⚠ **Freshness authority.** PREFLIGHT **G1 FAILED** (sweep coverage 17.06%), so the **sweep's** velocity
axis may not be cited. `theme_age` is **conditionally permitted where a value actually returned, with
its probe time** — and **19 of 19 probes answered** this run (22:30:56–22:31:20 and 23:05:20 KST).
🚫 **An empty or low reading is never read as "cooled"** (measured: 0 of 120 "silent" names were quiet).

| Name | Thesis, one line | Theme (probe 23:05 KST) | **Freshness** |
|---|---|---|---|
| `MPC` | **Refining-capacity destruction, not a crude trade** — 08-11→08-14 finally supplied the control: refiner EW rs60 **+25.30** vs integrated EW **−5.40** = a **30.70pp** spread inside one GICS sector while **Brent fell 0.44%** | `refining` ⚪ECHO **1.31×**, age ≥90 | 🟡 **PARTIAL** — residual: **does the barrel ever pay?** Re-check **2026-08-21** (`S95`/`P70`/`S88` all settle) |
| `PSX` | Same node, same driver. rs60 **+22.3**, OBV accumulating, blocked from its own shortlist by `vol_surge` **1.01** alone (`D251`, 3rd run) | `refining` ⚪ECHO 1.31× | 🟡 **PARTIAL** — residual: `vol_surge` ≥1.2 with OBV still accumulating. Re-check **08-21** |
| `VLO` | Same node. rs60 **+24.3**, `vol_surge` **0.84**. ⚠ PEG **4.08** is the worst of the three by a wide margin | `refining` ⚪ECHO 1.31× | 🟡 **PARTIAL** — residual: the PEG gap must close or the name is the node's worst expression. Re-check **08-21** |
| `COHR` | **The interconnect bottleneck is physical** — AI hit the copper wall, so the link layer must go optical regardless of demand elsewhere. Board's **#1 `flow_score` (+0.99)** and **#1 `vol_surge` (1.67)** | **`optical` ⚪ECHO 1.74× — the highest accel of 19 terms probed**, age ≥90 | 🟡 **PARTIAL** — residual: **reclaim 332.48 with `vol_surge` ≥1.0**; rs60 is **−13.7**. Re-check **08-21** (`S96`) |
| `LITE` | Same node, **held its move where `COHR` round-tripped** — rs20 **+21.9** vs +12.9, rs5 **+3.6** vs **−14.5** | `optical` ⚪ECHO 1.74× | 🟡 **PARTIAL** — residual: rs60 must turn positive (now −1.8) so the move is a trend, not a print reaction. Re-check **08-21** (`S96`) |
| `KKR` | `M669`'s **relocated Financials breadth node** — the sector's only admissible 🟢, confirmed on a 4th date. **PEG 0.59, the cheapest growth-adjusted multiple on the sheet** | `alternative asset` ⚪ECHO **1.39×**, age ≥90 | 🟡 **PARTIAL** — residual: the **±10.8% implied move with no scheduled print** is unexplained (`unknown`, C3). Re-check **08-19** (`S78`) |
| `ABNB` | The one name in the consumer complex the money confirms; **EXTENDED-BUT-LIVE** (rs20 +21.6 **and** rs60 +34.5, move **not** concentrated in 5 days) | ★ **`travel booking` 🟡ACCELERATING — 2.2×**, the accel gate CLEARED | 🟡 **PARTIAL, and the strongest on the sheet** — residual: Lens-3 flip (rs20 negative while rs60 positive). Re-check **08-21** (`S93`) |
| `TGT` | STPL's #1 `flow_score` (+0.503, ~2× the #2) with the sector's best rs60 — against a grocery node at **−21.1** EW | ★ **`retail earnings` 🟡ACCELERATING — 30.0×**, age **82d** ⚠ base **61 articles** ⇒ a small denominator; the ratio is fragile | 🟡 **PARTIAL** — residual: **its own print ~08-20**, against a **±6.7%** implied move (4.5× its 1.48% daily sigma) and a **put-heavy** book. Re-check **08-20** |

### 🚨 §B-1 · `F1` closed a second time — and this run locates the failing leg exactly

**🟢LIVE fired ZERO times again — a 9th consecutive US run — and this is now measured, not inferred.**
The pipe answered **19 of 19** probes. The gate requires **age ≤14d AND accel ≥2×**. Today:

| Leg | Result |
|---|---|
| **Acceleration ≥2×** | ✅ **CLEARED TWICE** — `travel booking` **2.2×** and `retail earnings` **30.0×** |
| **Age ≤14 days** | 🚫 **FAILED ON EVERY ONE OF 19 TERMS.** 17 read **">=90"**, the two accelerating ones read ≥90 and **82** |

⇒ ★ **The binding constraint is the AGE leg, not the acceleration leg** — and `theme_age` **caps its own
age readout at ">=90"**, so for any theme older than 90 days 🟢FRESH is **structurally unreachable
regardless of how fast it accelerates.** The 08-16 run closed `F1` as *"a gate property, not a pipe
artifact"*; this run narrows it to **which half of the gate**, using two terms that actually cleared the
other half. **A US desk trading multi-quarter industrial cycles will never see a ≤14-day theme age.**
🚫 **Consequence: no bet on this sheet may be marked 🔴RESOLVED on a freshness reading**, because the
instrument cannot issue the only tag that would contrast with it.

🚨 **Correction carried from `SECTOR_DEEP_STPL §0`, not edited away.** Earlier stages of this run
described `TGT` as **"🟢가속"**. **On the admissible instrument it is 🟡중립** (`vol_surge` 1.01,
velocity `None` in the sweep). The 🟢 came from a standalone `module_flow` probe that *did* get
velocity (2.38×) — the same code, the same closes, one extra input. **The 🟢 claim is withdrawn here
too.** What survives is the `flow_score` rank, which uses no news.

---

## §C · Flow and positioning cross-read

Flow/RS/OBV/short-z = **settled 08-14**. Implied moves = live, expiry **2026-08-21 (D4)**.

| Name | flow | OBV | rs20 | rs60 | surge | tag | 3-axis? | FINRA short-z | positioning |
|---|---|---|---|---|---|---|---|---|---|
| `COHR` | **+0.990** | 매집 | +12.9 | **−13.7** | **1.67** | 🟢 | ✅ | −0.17 △ | not pulled |
| `KKR` | +0.939 | 매집 | +8.5 | +16.9 | 1.49 | 🟢 | ✅ | **+1.62 ⚡crowded-short** | ±10.8% (08-16 pull), **no scheduled print** ⇒ `unknown` (C3) |
| `ABNB` | +0.881 | 매집 | **+21.6** | **+34.5** | 1.55 | 🟢 | ✅ | **−0.94 ✅clean rise** | not pulled |
| `LITE` | +0.817 | 매집 | **+21.9** | −1.8 | 1.27 | 🟢 | ✅ | +0.38 △ | not pulled |
| `MPC` | +0.806 | 매집 | +9.3 | **+29.3** | 1.25 | 🟢 | ✅ | **−0.71 ✅clean rise** | **±4.3%**, P/C 0.81, skew **+38.9** |
| `PSX` | +0.628 | 매집 | +8.5 | +22.3 | 1.01 | 🟡 | — | — | — |
| `TGT` | +0.503 | 매집 | +6.2 | +15.6 | 1.01 | 🟡 | — | — | **±6.7%**, **P/C 1.74 put-heavy**, skew +37.5 · **reports ~08-20** |
| `VLO` | +0.490 | 매집 | +5.9 | +24.3 | 0.84 | 🟡 | — | — | **±3.9%**, P/C 0.65, skew +7.3 |
| 🚫 `CVX` | +0.401 | 매집 | +2.3 | −4.4 | 0.95 | 🟢 | **NO** | −0.38 △ | — |
| 🚫 `CSCO` | +0.274 | 매집 | **−4.7** | — | 1.37 | 🟢 | **NO** | +0.67 △ | — |
| 🚫 `BAC` | +0.217 | 매집 | +0.8 | — | 0.73 | 🟢 | **NO** | +0.68 △ | — |
| 🚫 `MA` | +0.085 | 매집 | +0.3 | — | 0.73 | 🟢 | **NO** | +0.41 △ | — |

★ **The four 🚫 rows are the sheet's most important negative finding.** All four are 🟢 in the sweep,
none can be produced by `OBV+ ∧ RS20>0 ∧ vol_surge≥1.2`, and all four carry a velocity value.
`CSCO` is 🟢 on **rs20 −4.7 — negative — for a fourth consecutive run.**
⚠ **`MA` entered the shortlist today and `NFLX` left it, both on a ~0.06 move in an article-count ratio
with zero price change.** Candidate generation is non-deterministic under a 17%-coverage bridge.

⚠ **`TGT`'s ±6.7% implied move is 4.5× its own 1.48% daily sigma**, with a put-heavy book, against
accumulating OBV. **Flow and positioning disagree and the print settles it in ~3 sessions.**

---

## §D · Competition and peers

| Node | Inside | Outside / unmeasurable |
|---|---|---|
| **US refining** | `MPC` `PSX` `VLO` — one measured risk unit (`MPC`+`PSX` merge at **all three** `--days` windows, the only pair the instrument agrees on) | — |
| **Integrated / upstream** | `XOM` −7.3 · `CVX` −4.4 · `COP` −4.5 (rs60) — the peer set that **owns the barrel and lags** | — |
| **Optical transceiver** | `COHR` `LITE` | 🚨 **`FN` (Fabrinet) is NOT in `us_top300`** — the node's third name has **no flow, RS, OBV or short reading on this desk** (`D274`) |
| **Optical components** | `APH` (headline-0 chain-hop, short-z **−2.14**) · `CIEN` (short-z −1.72) · `GLW` (rs60 −11.4, **not part of this move**) | — |
| **Switch / fabric** | `ANET` *(held)* rs60 **+34.6** | — |
| **Alt-asset managers** | `KKR` fwd **14.93× on PEG 0.59** | — |
| **Mass retail** | `TGT` +15.6 vs `WMT` −19.9 · `COST` −18.0 · `KR` −25.5 (rs60) | — |

⚠ **`COHR` vs `LITE` are 18.1pp apart on 5 days and the desk carried them as ONE node for two runs.**
They are **not** one node — and today's data widens it: rs5 **−14.46** vs **+3.64**.

---

## §E · Refutation and dated catalyst — one per name

| Name | What kills it | Dated |
|---|---|---|
| `MPC` | `BZ=F` ≤ **86.50** at settle (de-escalation) **or** `EW{MPC,PSX,VLO}` excess ≤ −2.0pp while Brent ≥ +2.0% ⇒ it *was* a crude trade | **08-21** (`S95`, `P70`, `S88`) |
| `PSX` | same, plus its own **−3.2% 0q estimate revision** — the first negative in the series (`M708`) | **08-21** |
| `VLO` | same. ⚠ **PEG 4.08** means the market is paying most for the least growth-adjusted of the three | **08-21** |
| `COHR` | `EW{COHR,LITE}` 5-session excess ≤ **−5.0pp** ⇒ the 20-day move was print-reaction volume. ⚠ **Already below its 332.48 ignition trigger and rs60 −13.7** | **08-21** (`S96`) |
| `LITE` | same bracket. ⚠ **P/S 28.03 · P/B 22.99, un-cross-checkable** (XBRL ends 2025-03) | **08-21** (`S96`) |
| `KKR` | `S78`'s frozen thresholds. ⚠ A **±10.8% implied move with no scheduled print** is unexplained ⇒ `unknown` | **08-19** (`S78`) |
| `ABNB` | Lens 3 flip: **rs20 turns negative while rs60 stays positive** | **08-21** (`S93`) |
| `TGT` | Its own print: 1-session excess ≤ **−6.7%** ⇒ the options book was right and the OBV was noise | **~08-20** |

---

## §F · Epicenter-starter module — the cycle GAP, with its counter-argument attached

`CYCLE_EXPOSURE`: **rank-2 Energy / oil-refining epicenter 7.13% vs an 8.0% floor = 🚨 GAP −0.868pp**,
flagged on the day the 60-day US–Iran MoU expired. Held epicenter: `MPC`, `PSX`. Rank-1 AI-compute
clears (**16.57%** vs 12.0%). Rank-3 missile-defense has **no floor set ⇒ ⚪n/a by construction**.

**The stage's rule**: a 🔴/crowded tape gates ADD **timing**; it never justifies a sub-floor core. Here
the core is not zero — it is **0.87pp under**, the mildest form of this flag on record.
⚠⚠ **The counter-argument travels on the same line, per PREMORTEM Lens 4a**: the three refiners are
**one date-clustered ~3z observation**, the equity complex has priced a premium **the barrel has not**
(Brent −0.44% through the escalation), and all three names trade **above** consensus target median.
**Closing a 0.87pp gap into that is the "buy the confirmation" shape `M707` warns about.**
⇒ **Reported as a GAP. No action, no size, no recommendation (P4).**

🚨 **And the registry's own blind spot binds this section**: there is **no row for
optical/interconnect**, so exposure to the cycle owning the sheet's **#1 `flow_score`** is
**unmeasurable, not zero** (`D250`, `S94` settles 08-31).

---

## §G · Names set aside, and names never reached — both ledgers written

| Ledger | Name | Class | Condition |
|---|---|---|---|
| `reject_ledger` | **`HD`** | `D.약한손` *(intended `A.OBV분배`; **that class does not exist in the CLI enum** — see `EVENT_ALPHA §3`)* | revives-if OBV accumulating **and** rs20 > 0 after the print · **08-25** |
| `missed_ledger` | **`APH`** | `Q.확신부족` | enters-if pullback with OBV accumulating **and** `vol_surge` ≥ 1.2 · **08-25** |
| `missed_ledger` | **`NOC`** | `M.숏리스트탈락` | enters-if `vol_surge` ≥ 1.2 with OBV accumulating · **08-25** |
| `missed_ledger` | **`CIEN`** | `M.숏리스트탈락` | enters-if `vol_surge` ≥ 1.2 with OBV turning to accumulating · **08-25** |

★ **The re-file rule applied, not just cited**: `CVX` `CSCO` `BAC` `MA` are **NOT** rejected. Their flow
gate is ambiguous rather than failed — they are green on an axis the desk cannot cite and unmeasurable
on the axis it can. **A name whose instrument is broken is not a name whose money left.** They stay on
the sheet marked 🚫 with the reason, which is the honest state.
★ Likewise `COHR` is **not** rejected despite rs60 −13.7: its OBV is accumulating, so a rejection would
be filed against a still-rising accumulation axis — the exact error the 475150 precedent cost **+41.2pp**
and **+26.9pp**.

## ✅ EXIT CHECK

- [x] **Every DEEP sector has a section** — ENRG (§A–§F, `MPC`/`PSX`/`VLO`) · IT (`COHR`/`LITE`) ·
      STPL (`TGT`) · HLTH (**explicitly empty — 0 of 32 names clear the volume gate; the absence is
      diagnosed as a `vol_surge` artifact, not treated as evidence**) · INDU (**explicitly empty — 0
      admissible greens; `NOC` filed to `missed_ledger` rather than dropped**).
- [x] **Cross-sector LIVE shortlist names included or explicitly dropped**: `KKR` `ABNB` included;
      `CVX` `CSCO` `BAC` `MA` carried with a 🚫 and the reason (inadmissible green), **not** dropped.
- [x] **Numbers cross-checked; blanks are blanks** — three XBRL failures are stated as failures
      (`MPC`/`PSX` period-tagging signature marked `unknown`, `LITE` XBRL stale to 2025-03, `VLO` empty)
      and **no figure is derived from any of them**.
- [x] **Flow/positioning cross-read present per candidate**; `BET_SHEET.md` written as ONE file.
- [x] **Every set-aside name is in a ledger with a class and a revival/entry condition** (§G).
- [x] **No name removed on narrative grounds while its measured flow still passed** — `COHR`, and the
      four 🚫 names, are explicitly retained with their reasons.
- [x] **No sizing computed.** `--ic` is not evidence-backed this run (G6); any size would be
      **"mechanical ¼"** and none is written. Concentration statements carry their `--days` (§0).
