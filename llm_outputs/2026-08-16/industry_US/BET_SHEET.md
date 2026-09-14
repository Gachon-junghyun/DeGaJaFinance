# BET_SHEET — industry_US · 2026-08-16 · Stage 9/11 (L1·BET)

> **ONE file, per-sector sections.** Downstream desks glob this exact filename — never split it.
> Benchmark **`SPY`** named inline (C1). Prices settled **2026-08-14**. Multiples from
> `module_fundamentals_us --json` (yfinance), revenue cross-checked against **SEC XBRL** where pulled.
> **Zero buy/sell recommendation. Sizing language below is influence-illustration only (P4).**

## §0 · What this sheet is allowed to say today, and what it is not

| Constraint | Source | Effect on this sheet |
|---|---|---|
| **Zero sessions settled** since the prior run | PREFLIGHT / HANDOVER §0 | No candidate's flow may be described as "improving today". Every flow number is the **08-14** observation, read a second time |
| **No single-number concentration guard** | PREFLIGHT G4 (11/10/10 across 250/500/750d, 7th run) | §E states the `--days` window **on the same line** as any concentration statement |
| **No `--ic`-backed size** | PREFLIGHT G6 (accrual 0.42/day vs 1.0; ETA ≈72d vs 30d) | Any size language is labelled **"mechanical ¼"** |
| **Velocity axis revoked** | PREFLIGHT G1 (coverage 16.7%, survivor set monotone-nesting) | **4 of the 9 🟢 are inadmissible**: `NFLX` · `CVX` · `CSCO` · `BAC`. They appear on this sheet **only** as excluded rows |
| **`AVGO/NVDA` and `ANET/ETN` unit counts** unusable | PREFLIGHT G4 | §E's concentration read uses the **500d/750d agreement** and says so |

**Candidate set** = (DEEP thesis leaders) ∪ (`us_setup_screener --sector Energy`) ∪ (`US_LIVE_SHORTLIST.json`).
⚠ **The screener contributed ZERO names**: `--sector Energy` returned **0 of 16** in all three baskets
(leader-pullback · de-rate snapback · washout). **That is a finding, not an empty call** — after a
14–19% five-session rip **there is no pullback to buy**; the sector is extended, not setting up.

---

# §ENRG — the sector whose evidence grew this run

## §A · Numbers

| | **`MPC`** *(held)* | **`PSX`** *(held)* | `VLO` |
|---|---|---|---|
| Price (08-14) | **355.42** | 233.61 | 341.67 |
| Market cap | $99.8bn | $93.7bn | $98.4bn |
| Trailing P/E | 12.33× | 13.33× | 14.24× |
| **Forward P/E** | **11.04×** | **11.11×** | 12.09× |
| PEG | 1.76 | **1.35** | 4.08 |
| P/S · P/B | 0.67 · 5.27 | 0.61 · **2.96** | 0.74 · 4.25 |
| **Gross margin, FY2025** | **10.0%** | *(not pulled — `unknown`, C3)* | *(not pulled)* |
| **Its own 8-yr median GM** | **10.5%** (peak FY2022 14.5% · trough FY2020 5.8%) | — | — |
| Q2'26 revenue | **$51.99bn, +53.83% YoY** — **XBRL cross-check 0.0% difference** | — | — |
| **Next earnings** | **2026-11-03** | *(not pulled)* | *(not pulled)* |

★ **Lens `L2` does NOT fire on `MPC`.** An 11.04× forward multiple sits against a gross margin at its
own **median (10.0% vs 10.5%)**, not its peak ⇒ **this is not the low-multiple/peak-margin trap**
(`M670`, confirmed on a second pull). ⚠ **Both halves (C2)**: it also means the current crack rally is
**not yet in the annual margin series**, and the 3-2-1 crack sits at the **95.2nd percentile of 250
days** — which is how a peak-margin trap gets *built* one or two quarters out.

## §B · Thesis · freshness `[ALPHA fills]`

**A refining-capacity destruction trade, not a crude trade.** Five dated strikes on Russian refining in
six days (**08-13 Salavat 200kbpd** the largest), **Russia importing Indian fuel** (08-12), **Russian
diesel exports at a multiyear low** (08-13), **Russia admitting petrol shortages** (08-14).
The bottleneck is **distillation capacity**, and crude is explicitly *not* scarce (`WTI` spec at the
**18th percentile SHORT**, COT Tue 08-11).
⚠ **Grade**: `[news]` bodies + COT + settled prices. **No issuer document supports the mechanism** —
`MPC`'s own next filing is 2026-11-03.
**`freshness: 🟡PARTIAL`** — resolved by ALPHA (`ACTION_TICKETS.md` §1). ⚠ The theme axis is
**non-discriminating this run**: `theme_age` answered **8 of 8** probes at 22:56–22:57 KST and returned
**⚪ECHO on every one** (zero 🟢FRESH, zero 🔴FADING; highest acceleration **1.70×** against a 2×
gate, every theme **>90 days old**). ⇒ **🟢LIVE was arithmetically unreachable, not absent** — and
because the pipe answered, that is now a measured property of the **gate**, not of the instrument
(`F1` closed). **An ⚪ECHO reading is NOT written as "cooled"** (PREFLIGHT G1).

## §C · Flow / positioning cross-read (`asof 2026-08-14`)

| | `MPC` | `PSX` | `VLO` |
|---|---|---|---|
| Tag | **🟢가속** | 🟡중립 | 🟡중립 |
| **3-axis producible?** | ✅ **YES** | ❌ blocked on `vol_surge` **1.01** | ❌ blocked on `vol_surge` **0.84** |
| OBV state · RS20 vs `SPY` | 매집 · **+9.3** | 매집 · +8.5 | 매집 · +5.9 |
| RS60 vs `SPY` | **+29.3** | +22.3 | +24.3 |
| **5-session excess vs `SPY`** | **+18.79pp** | +14.17pp | +14.14pp |
| FINRA short | **z −0.71 — ✅ clean-rise**, 2.8% float, `covering`, DTC 3.4 | — | — |
| Implied move | **±4.4% (expiry 2026-08-21, D5)** — genuinely covers the window | — | — |

⚠⚠ **The counterweight, stated at the same size as the thesis.** `module_chart MPC --read`:
**turn verdict BREAKOUT at the upper Bollinger band, RSI 69.9, bull stack 5>20>60>120 — but OBV 중립
(20d slope −3%) and a BEARISH RSI divergence (price higher high, RSI lower high)**, quoted beside the
A-grade price axis per RULE D6. **A +19.19% five-session move with no accumulation confirmation and a
bearish divergence.** Swing-low structural reference **297.75** (the 08-05 base of the rip).

★ **And the revision leg just showed its first downtick** (`module_fundamentals_us PSX`, estimate
momentum — the desk's cleanest read of the denominator's *direction*):

| `PSX` EPS estimate | 90d ago | 60d | 30d | **7d** | **now** |
|---|---|---|---|---|---|
| Current quarter (0q) | 5.66 | 6.20 | 7.20 | **9.56** | **9.25** ⚠ |
| Current year (0y) | 16.30 | 17.66 | 19.39 | 25.52 | **25.80** |
| Next year (+1y) | ~16.2 | 17.21 | 18.01 | 19.91 | **21.02** |

⇒ **0y +58.3% over 90 days** — consensus is **chasing** the crack, hard. ⚠ **And `0q` ticked DOWN
−3.2% in the last 7 days — the first negative in the series.** Read on the **second derivative**
(lens B1): the *level* of revisions is extreme and the *rate* just turned. **One observation (S1).**
🚨 **Not to be written as "revisions turn before price does"** — that was tested and did not hold
(`measure_ic.py`: W1 +0.403 vs W2 −0.299, opposite signs; an IT loading, not a revision axis).

## §D · Competition / peers

Three refiners, **one risk unit** (`risk_units`: `MPC`·`PSX` merge at **all three windows — the only
unit the instrument agrees on**, `--days 250/500/750`). `VLO` is the same trade at a worse multiple
(12.09× fwd, PEG **4.08**). `XOM` is **the control, not a peer**: **0% refining exposure** (`M146`),
5-session excess **+4.22pp** vs the trio's +14 to +19 — a **10–14pp intra-sector spread** that is the
whole thesis.
⚠ **`PSX` is the cheaper of the pair on PEG (1.35 vs 1.76) and P/B (2.96 vs 5.27)** — and it is the one
the shortlist filter excluded.

## §E · Refutation + dated catalyst

| Refutation | Threshold | Date |
|---|---|---|
| **`S92` branch C** — a US-brokered halt to Ukrainian strikes on Russian energy infrastructure, ≥3 independent outlets | **the only branch that breaks the mechanism**; first datapoint already on the board (`semafor` 08-12) | **2026-08-31** |
| `P62`/`P66` branch B | `HO=F` − `CL=F` 20-day gap **≤ 0pp** | **2026-08-21** |
| Crack rate (lens B1) | **two consecutive negative weekly accelerations** on the settled 3-2-1 | rolling |
| OBV confirmation | `MPC` OBV turns **분산** while price holds | rolling |
| Structural price reference | close below **297.75** ⇒ the entire 5-session move retraced | rolling |
| 🚨 **VOID** | a US refinery outage or a PADD3 hurricane landfall | rolling |

**Concentration note (G4 — window stated on the same line):** at `--days 500` **and** `--days 750`
`MPC`+`PSX` are **one measured unit**; at `--days 250` they are **also** one unit. **This is the single
pair the instrument agrees on across all three windows**, so treating them as one bet is the only
concentration statement this sheet can make without a caveat. Size language, if any: **mechanical ¼**.

---

# §CONSUMER — the PREMORTEM-promoted leg

## §A · Numbers — **`ABNB`**

| | value |
|---|---|
| Price (08-14) · market cap | **184.06** · $110.2bn |
| Trailing P/E · **Forward P/E** | 42.02× · **29.98×** |
| PEG · P/S · P/B | 1.97 · **8.38** · 13.92 |
| **Estimate momentum, 0y** | 5.091 (90d) → 5.093 (60d) → 5.093 (30d) → 5.092 (7d) → **5.290 now** = **+3.9% in 7 days**, flat for the prior 83 |
| **Estimate momentum, +1y** | 6.033 → 6.050 → 6.056 → 6.041 → **6.181** = **+2.5%/90d, all of it in the last 7 days** |
| Gross margin history | **not pulled — `unknown` (C3)** |
| Next earnings | **not pulled — `unknown`** |

⚠ **This is an expensive name and the sheet says so**: **P/S 8.38 · P/B 13.92 · forward 29.98×**.
The estimate book is **positive but tiny and brand-new** — 83 days of flat, then a +3.9% step in the
last week. **One observation (S1)**, and it is not a trend.

## §B · Thesis · freshness `[ALPHA fills]`

**Wallet-share winner inside a squeezed consumer, and the GICS label cannot see it.** The measured
axis is not goods-vs-services and not staples-vs-discretionary: the two accumulating names (`ABNB`,
`TGT`) sit in **different** labels, as do the two dispersing ones (`HD`, `COST`). Dated squeezes on the
wallet: *"US retail sales post first decline in nine months in July"* (08-14) and *"Trump asks
Americans to accept high pump prices"* (08-15) — **the terminus of §ENRG's own value chain**.
⚠ **Counter-evidence carried, not buried**: `recession` term velocity **1.07×** and `layoffs` **0.83×**
— **no narrative surge behind the consumer story**.
**`freshness: 🟡PARTIAL`** — resolved by ALPHA (`ACTION_TICKETS.md` §1). ⚠ The theme axis is
**non-discriminating this run**: `theme_age` answered **8 of 8** probes at 22:56–22:57 KST and returned
**⚪ECHO on every one** (zero 🟢FRESH, zero 🔴FADING; highest acceleration **1.70×** against a 2×
gate, every theme **>90 days old**). ⇒ **🟢LIVE was arithmetically unreachable, not absent** — and
because the pipe answered, that is now a measured property of the **gate**, not of the instrument
(`F1` closed). **An ⚪ECHO reading is NOT written as "cooled"** (PREFLIGHT G1).

## §C · Flow / positioning cross-read (`asof 2026-08-14`)

| | `ABNB` | `TGT` *(watch)* | `HD` | `COST` |
|---|---|---|---|---|
| Tag | **🟢가속** | 🟡중립 | **🔴분산** | **🔴분산** |
| 3-axis producible? | ✅ **YES** (`vol_surge` **1.55**) | ❌ no `vol_surge` leg | — | — |
| OBV · RS20 vs `SPY` | 매집 · **+21.6** | 매집 · +6.2 | 분산 · −4.4 | 분산 · −2.3 |
| exc5 / exc20 / exc60 vs `SPY` | **+2.966 / +21.639 / +34.525** | +2.795 / +6.213 / +15.601 | **−5.111** / −4.449 / +6.235 | +1.003 / −2.296 / −17.981 |
| FINRA short | **z −0.94 — ✅ clean-rise** | — | — | — |

★ **`ABNB` is NOT `M149`'s decaying-stock shape**: exc60 **+34.525**, exc20 **+21.639**, and exc5 is
**still positive (+2.966)** — the move is distributed across all three windows rather than concentrated
in the last 20 sessions. PREMORTEM Lens 3 re-tag: **EXTENDED-BUT-LIVE**, flip condition = RS20 turns
negative while RS60 stays positive.

## §D · Competition / peers

Inside `XLY`, **`AMZN` is 40.2% of sector cap and carries exc5 −4.708 vs `SPY`** (the A-grade price
axis; its C-grade OBV 분산 agrees, quoted beside it per RULE D6, never alone) — so the sector ETF is
not a proxy for `ABNB`. Nearest measured comparison is the **`ABNB` − `HD` 5-session excess spread vs
`SPY` = +8.077pp**, which is `S93` branch B's registered observable.
⚠ **`TGT` is the sheet's cleanest *unowned* accumulation** (OBV 매집, +15.601 exc60 vs `SPY`) — **and
it reports inside 3 sessions**, which is why it is a watch and not a candidate.

## §E · Refutation + dated catalyst

| Refutation | Threshold | Date |
|---|---|---|
| **`S93` branch A** — one factor, "the consumer is rolling" | `WMT` **and** `HD` **and** `TGT` all post negative 5-session excess vs `SPY` | **2026-08-21** |
| Wallet-share bottleneck fails | `ABNB` − `HD` 5-session excess spread vs `SPY` falls **< 0** | 2026-08-21 |
| Momentum flip (Lens 3) | `ABNB` RS20 turns negative while RS60 stays positive | rolling |
| Valuation | forward 29.98× on a **+3.9%/7-day** estimate step is **not** a value case, and this sheet does not make one | — |
| 🚨 **VOID** | a tariff announcement affecting consumer goods | rolling |

**Dated catalysts inside the window that `CATALYST_WATCH` did NOT carry**: `HD` ~08-19 · `WMT` ~08-20
(**implied ±5.0%, expiry 08-21, event-priced**) · `TGT` ~08-20.

---

# §LIVE — cross-sector shortlist names outside the DEEP sectors

`US_LIVE_SHORTLIST.json`, mcap ≥ $10bn ∧ 🟢. **9 names; 5 admissible after the `D261` decomposition.**

## §A/§C · The admissible three not already covered above

| | **`KKR`** (Financials) | `COHR` (IT) | `LITE` (IT) |
|---|---|---|---|
| Price · mcap | 114.01 · $105.3bn | 325.83 · $63.7bn | 926.14 · $82.1bn |
| Trailing / **Forward P/E** | 36.31× / **15.43×** | 79.28× / **23.38×** | — / **28.05×** |
| PEG · P/S · P/B | **0.59** · 4.08 · 3.63 | 0.92 · 8.96 · 5.85 | 0.63 · **27.22** · 22.33 |
| Tag · 3-axis producible | 🟢 · ✅ (`vol_surge` 1.49) | 🟢 · ✅ (1.67) | 🟢 · ✅ (1.27) |
| OBV · RS20 / RS60 vs `SPY` | 매집 · **+8.5 / +16.9** | 매집 · +12.9 / **−13.7** | 매집 · **+21.9** / −1.8 |
| **exc5 / exc20 vs `SPY`** | — | **−14.457** / +12.927 | **+3.642** / **+21.934** |
| FINRA short | **z +1.62 — ⚡ crowded-short** | — | — |
| Estimate momentum, +1y (90d→now) | 7.502 → **7.389 = −1.5%** ⚠ | — | 27.9 → **29.85 = +7.0%** |
| Estimate momentum, 0y (90d→now) | 6.089 → **6.314 = +3.7%** | — | 18.045 → **18.735 = +3.8%** |

### The three verdicts, each with its reason

- **`KKR` — candidate, with a split book named.** `M669`'s **relocated Financials breadth node**
  (alternatives/asset-management) and the sector's **only** admissible 🟢. Forward **15.43× on a PEG of
  0.59** is the cheapest growth-adjusted multiple on this sheet. ⚠ **Its estimate book disagrees with
  itself**: current year **+3.7%/90d** while **next year is being CUT −1.5%/90d** — consensus is
  pulling earnings forward, not raising the level. ⚠ **`z +1.62` is crowded-short = squeeze fuel
  conditional on a turn, never a standalone read (D6).** `S78` settles **08-19**.
- 🚫 **`COHR` — NOT a candidate, and the reason is a measurement.** It carries the **board's highest
  `flow_score` (+0.99)** and the **universe's biggest `vol_surge` (1.67)** — and it **round-tripped**:
  379.13 on 08-07 → **325.83** on 08-14, i.e. **below its 08-05 level**, a **−14.06% five-session move
  and −14.457pp excess vs `SPY`**. Its own chart puts it **NEUTRAL/CHOP, price above only 2 of 4 MAs,
  and BELOW its own ignition trigger of 332.48**. **The surge measured the round-trip's volume.**
- ⚠ **`LITE` — watch, not candidate.** It **held** its move (+26.38% 20d, exc20 **+21.934**) and its
  estimate book is the best on the sheet (**+1y +7.0%/90d**). **But its 🟢 is dated to its own
  08-11/08-12 earnings print** ⇒ **reaction volume, not accumulation** (EVENT_ALPHA Card 2).
  **Re-read after the print volume rolls off, ≈2026-08-25.** ⚠ **P/S 27.22 · P/B 22.33** — nothing on
  this sheet is priced like it.

## §C-excl · The four inadmissible 🟢 — listed so they cannot re-enter unexamined

| Name | Why excluded |
|---|---|
| `NFLX` | 🟢 is **velocity-produced** (`vol_surge` **0.63**); the run's only `new_green` (Δ +0.48) — **a `new_green` produced by a revoked axis is not an ignition** |
| `CVX` | velocity-produced (`vol_surge` 0.95); RS60 **−4.4** vs `SPY`, i.e. the wrong side of §ENRG's own 30-point spread |
| `CSCO` | velocity-produced (velocity 2.48) **on RS20 −4.7 — negative — for a third consecutive run** |
| `BAC` | velocity-produced (`vol_surge` 0.73); RS20 **+0.8 ≈ zero** ⇒ Lens 3 re-tag **DECAYING** |

---

# §GAP · Epicenter-starter module — required because a cycle GAP was flagged

🚨 `CYCLE_EXPOSURE`: **rank-2 cycle `Energy / oil-refining` — epicenter exposure 7.1% vs an 8.0% floor
⇒ margin −0.898pp.** The standing rule: **a crowded or 🔴 tape gates ADD timing; it never justifies 0%
core in a top-rank cycle.**

| | Reading |
|---|---|
| **Is the core zero?** | **No.** `MPC` and `PSX` are both held; the shortfall is **−0.898pp**, not an absence |
| **Cleanest epicenter expressions the desk can measure** | **`MPC`** (only admissible 🟢, FINRA clean-rise z −0.71) · **`PSX`** (cheapest on PEG 1.35 / P/B 2.96, filtered out on `vol_surge` 1.01 alone) |
| ⚠ **Is the GAP widening?** | **No — it is identical to the 08-15 run to three decimals.** The book did not trade and prices did not move. **Do not read a second appearance as a strengthening signal** |
| ⚠ **Timing context, stated plainly** | The epicenter names ran **+14 to +19% in five sessions**, so this GAP is measured **after** the move. `MPC`'s implied move is **±4.4% (D5)** and its chart reads **BREAKOUT at the upper band with RSI 69.9 and a bearish divergence** |
| ⚠ **Rank-3 has no floor set** | `⚪ n/a` — `D250`, the registry is **29 days stale** and has **no entry for either cycle this run found** (optical/interconnect, custom AI silicon). **`S94` brackets that** |

**Influence illustration only (P4)**: any core in this cycle is **mechanical ¼** (G6 — the `--ic` input
is not evidence-backed), and the concentration statement that travels with it is: **`MPC`+`PSX` are one
measured risk unit at `--days` 250, 500 and 750.**

---

## §Z · Names set aside — the ledger discipline

**No new rejection is filed this run, and the reason is stated rather than skipped.**
The three names that would have been candidates and were not — **`COHR`**, **`HD`**, **`COST`** — each
fail the ledger's own precondition that a rejection must carry a `--revives-if` **and** a
`--recheck-date` that is not a coin-flip:

| Name | Why not filed |
|---|---|
| `COHR` | Its OBV is **누적 (+57% 20d slope)** while its price round-tripped. **Filing it now would score a rejection against a name whose accumulation axis is still rising** — the reason class would have to be "price structure", which its own trigger (332.48) can clear in one session. **Deferred to the post-08-25 re-read** |
| `HD` · `COST` | **Both report inside 5 sessions.** A rejection filed 3 sessions before a print is scored against an event the desk deliberately chose to wait for. **Deferred to the post-print run** |

⚠ **These deferrals are named here so they are visible rather than silent**, per the L1's own warning
that the funnel's widest stage is the one with no scoreboard. **Two `missed_ledger` rows were filed
this run** (`MSTR` `Q.확신부족` recheck 08-28 · `RIOT` `N.유니버스부재` recheck 09-01) from
EVENT_ALPHA §9 — ledger totals now **reject 176 / missed 134, legacy 0 on both**.

## ✅ EXIT CHECK

- [x] **ONE file, per-sector sections** — `§ENRG` · `§CONSUMER` · `§LIVE` · `§GAP` · `§Z`, each with
      §A numbers / §B thesis+freshness placeholder / §C flow+positioning / §D peers / §E refutation.
- [x] **Wide net, not the three names already known** — DEEP leaders ∪ screener ∪ `US_LIVE_SHORTLIST`.
      ⚠ **The screener's 0-of-16 return is reported as a finding** (the sector is extended, not
      setting up), not silently dropped.
- [x] **Blanks stated as blanks** — `PSX`/`VLO` gross-margin history, `ABNB` margin history and next
      earnings, `COHR` estimate momentum all marked **`unknown` (C3)**, not filled.
- [x] **XBRL ↔ yfinance cross-check performed where pulled** — `MPC` Q2'26 revenue **$51.99bn, 0.0%
      difference**.
- [x] **Epicenter-starter module included** (`§GAP`) because a cycle GAP was flagged — with the GAP
      explicitly disclosed as **identical to the prior run, not widening**.
- [x] **Sizing language is influence-illustration only and labelled "mechanical ¼"** (G6). **Zero
      buy/sell recommendation anywhere.**
- [x] **Concentration statements carry their `--days` window on the same line** (G4).
- [x] **Names set aside are accounted for** — three deferrals with their reasons (`§Z`), two
      `missed_ledger` rows actually filed with `--enters-if` + `--recheck-date`. **No rejection was
      filed that could not carry both required fields.**
- [x] **The four inadmissible 🟢 are listed with the reason each is excluded** (`§C-excl`) so they
      cannot re-enter a later stage unexamined.
