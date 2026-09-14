# SECTOR_DEEP_ENRG — industry_US · 2026-08-16 · **Continuous track (4th consecutive run)**

> **DELTA-led.** Structure carried by reference to `llm_outputs/2026-08-15/industry_US/SECTOR_DEEP_ENRG.md`.
> Benchmark **`SPY`** named inline (C1). Prices settled **2026-08-14**, `yfinance auto_adjust=False`.
> No sizing (P4).

## §1 · The delta — and it is the largest single-sector move on this board

★ **The refining trio ripped 14–19% in FIVE sessions while the market went nowhere.** This is not
visible in the sweep's RS20 (which reads +9.3 for `MPC`) and the desk had not measured it until now:

| | 08-05 close | **08-14 close** | 5-session | 20-session | 5d excess vs `SPY` |
|---|---|---|---|---|---|
| **`MPC`** *(held)* | 297.75 | **355.42** | **+19.19%** | +13.70% | **+18.79pp** |
| **`PSX`** *(held)* | 202.55 | **233.61** | **+14.57%** | +12.93% | **+14.17pp** |
| **`VLO`** | 302.39 | **341.67** | **+14.54%** | +10.34% | **+14.14pp** |
| `XOM` *(the control)* | 151.63 | 160.10 | +4.61% | +8.65% | +4.22pp |
| `SPY` | 769.79 | 776.34 | **+0.40%** | +4.45% | — |

⇒ **The refiners beat the integrateds by 10–14pp in one week inside one GICS sector** (`W5`: "Energy"
cannot express this). And **`MPC`'s entire 20-day excess, and more, was earned in the last 5 sessions**
— days 6–20 contributed **−9.5pp**. That is the **inverse** of `M149`'s decaying-stock shape: a
concentrated, *fresh* move, which is a live signal and an extension risk at the same time.

## §2 · Thesis confirm-or-crack — the mechanism got dated, primary-adjacent evidence

`P66` / EVENT_ALPHA Card 1. **Five dated strikes on Russian refining in six days**, plus two
consequence prints:

| Date | Item | Outlet |
|---|---|---|
| 08-10 | Ukraine drone strike on a refinery deep inside Russia, **≥13 killed** | `guardian` |
| 08-11 | Drone attack hits a major refinery deep inside Russia | `oilprice` |
| **08-13** | **Gazprom's Salavat refinery, 200,000 bpd, Urals** | `oilprice` + `bloomberg` |
| 08-14 | Blaze at a key Russian oil and fuel terminal | `oilprice` |
| 08-14 | **Russia admits new petrol shortages** | `euronews` |
| 08-12 | **Russia IMPORTS Indian fuel as refinery crisis deepens** — the exporter/importer inversion | `oilprice` |
| 08-13 | **Russia's diesel exports crash to a multiyear low** amid a tight global market | `yahoo_finance` |

⇒ **The bottleneck is a binding physical constraint on refining CAPACITY, not strong crude demand.**
Strong demand is not a bottleneck; **destroyed distillation capacity is.**

## §3 · ⚠⚠ The crack in the thesis — three independent refutations, none of them narrative

This is the section the delta above makes mandatory. **Every one of these is a measurement.**

### 3a · The 19% move has NO volume behind it and carries a bearish divergence
`module_chart MPC --read` (`asof 2026-08-14`):
> **OBV: 중립 (20d slope −3%) — quoted beside the A-grade price axis (RS20 +9.3 vs `SPY`) per RULE D6,
> never alone; the two disagree and that disagreement is the finding** ·
> **다이버전스: 약세 (price higher high · RSI lower high)** ·
> MA 강세스택 5>20>60>120, price above 4/4 · Bollinger **upper band**, expansion 22.0% ·
> **RSI 69.9** · turn verdict **BREAKOUT** · swing-low stop **297.75**

⇒ **A breakout to the upper band with a NEUTRAL OBV and a bearish RSI divergence.** `D6`: OBV is
C-grade, so this does not kill the thesis on its own — **but a +19% five-session move that its own
accumulation series does not confirm is the definition of a move to be sceptical of.**
Corroborating from the sweep: `vol_surge` **`MPC` 1.25 · `PSX` 1.01 · `VLO` 0.84** — the trio moved
14–19% on roughly **normal** volume. ★ And `D270` says why that reads as it does: the whole tape is
thin (median last-bar volume 0.649× the 20-day norm), so a ~1.0 surge in this week means *less* than
usual, not more.

### 3b · Lens `L2` does NOT fire — and that cuts both ways
`scripts/margin_history.py MPC` (SEC XBRL, FY2018–FY2025):

| | value |
|---|---|
| FY2025 gross margin | **10.0%** |
| Own 8-year **median** | **10.5%** |
| Peak FY2022 | 14.5% |
| Trough FY2020 | 5.8% |

⇒ **MPC is at its MEDIAN margin, not its peak** ⇒ the peak-margin/low-multiple trap **does not apply**
(`M670` confirmed on a second pull). ⚠ **But read the other half (C2)**: it also means the current
crack rally is **not yet in the margin series** — FY2025 is the last annual point, and the 3-2-1 crack
sat at the **95.2nd percentile of 250 days** at the 08-14 close. **The denominator has room to rise,
and that is precisely the setup that creates a peak-margin trap one or two quarters later.** Not a
kill; a dated watch.

### 3c · The catalyst calendar is EMPTY where it matters
`module_fundamentals_us MPC`: **next earnings 2026-11-03** — **outside every current window**.
Q2'26 revenue **$51.99B, +53.83% YoY**, **XBRL cross-check 0.0% difference** (`us-gaap:Revenues`), so
the print itself is verified — but there is **no issuer event inside 79 days** to confirm or refute the
crack thesis. ⇒ **This position has to be carried on tape and third-party physical data alone**, which
is exactly the condition under which narrative substitutes for measurement.

### 3d · ★ The named political off-switch, restated because it is the branch that can falsify us
**08-12 — *"Kyiv stops strikes on Russian port after request from JD Vance"*** [`semafor`].
`S92` branch C brackets this and **it is the only branch that breaks `P66`'s stated mechanism**
(PREMORTEM §2b). ⚠ And positioning is on the other side: **`WTI` spec at the 18th percentile SHORT**
(COT Tue 08-11) — the crowd is positioned for de-escalation, so the pain trade on a strike-halt is ours.

## §4 · Value chain — 6 nodes, bottleneck marked

`Crude supply (OPEC+ / Russia / SPR)` → `Seaborne transit (Hormuz · Bab el-Mandeb)` →
**`🔴 DISTILLATION CAPACITY — the binding constraint`** → `Refined product inventories (PADD1/3, ARA, Singapore)` →
`Crack spread (3-2-1; distillate leg leading)` → `Refiner P&L (MPC · PSX · VLO)` → *(cross-sector)*
`Airlines / trucking fuel cost` → `Consumer pump price`.

- **Bottleneck justification**: crude is **not** scarce (`WTI` spec 18th %ile short; *"Oil falls on
  weaker demand outlook and higher US stocks"* 08-13). **Distillation capacity is** — Salavat 200kbpd
  down, Russia importing Indian fuel, Russian diesel exports at a multiyear low.
- **Cross-sector chain flagged**: the pump-price node is now **political** — *"Trump asks Americans to
  accept high pump prices"* (08-15) — which links this chain directly to the **consumer complex** the
  5th DEEP covers, and to the **SPR** constraint (*"Depleted strategic oil reserve nears level that
  raises concerns about damage to caverns"*, `cnbc` 08-15).

## §5 · `D251`, 2nd consecutive run — the sector's leaders are filtered out of its own shortlist

`PSX` (RS60 **+22.3** vs `SPY`) and `VLO` (**+24.3**) are the sector's #2 and #3 on RS60 and are 🟡
**on `vol_surge` 1.01 / 0.84 alone** — OBV 매집 and RS20 positive on both. **The shortlist filter is
removing the two names the 5-session tape just ranked #2 and #3 in the entire universe.** Combined with
§3a this is one fact, not two: **`vol_surge` is the wrong instrument in a thin tape** (`D270`).

## §6 · CYCLE_EXPOSURE — the GAP, read honestly

🚨 Rank-2 cycle epicenter **7.1%** vs an **8.0%** floor ⇒ **−0.898pp**. ⚠ **Identical to the 08-15 run
to three decimals** — the book did not trade and prices did not move, so this is **the same GAP
measured twice**. It is **not** widening and must not be reported as such.
⚠ **And §1 changes how to read it**: the epicenter names ran **14–19% in five sessions**, so a GAP
measured on 08-14 marks is a GAP measured *after* the move.

## §7 · Track KPIs and anti-signals — stated as observables

| Track KPI | Current (08-14) | Kill / anti-signal |
|---|---|---|
| `HO=F` − `CL=F` 20-day return gap | `P62` branch A threshold **+4pp** | gap **≤ 0pp** at the 08-21 settle |
| 3-2-1 crack, **settled weekly mean rate** (lens B1 — the second derivative) | level **95.2nd %ile of 250d** | **two consecutive negative weekly accelerations** |
| Refiner-vs-integrated RS60 spread vs `SPY` | **+29.3 / +22.3 / +24.3 vs −7.3** ≈ a 30–36 point spread | spread **< +10 points** |
| `MPC` OBV 20d slope | **−3% (중립)** — already not confirming | OBV turns **분산** while price holds |
| Dated strikes on Russian refining | **5 in 6 days** | **`S92` branch C**: a US-brokered halt reported by ≥3 independent outlets |
| `MPC` swing-low structural stop reference | **297.75** (the 08-05 base of the rip) | close below it ⇒ the 5-session move is fully retraced |

**🚨 VOID condition** (inherited from `P62`): a **US refinery outage** or a **PADD3 hurricane landfall**
inside the window makes distillate strength a domestic-supply artifact, not a Hormuz/Russia read.

## §8 · Verdict handed forward

**The OW's evidence STRENGTHENED on narrative and on price, and WEAKENED on confirmation quality.**
- ✅ To BET §B: **`MPC`** — the sector's only admissible 🟢 (3-axis producible), FINRA clean-rise
  (short z **−0.71**), the mechanism dated and primary-adjacent.
- ⚠ **With three stated counterweights**: no OBV confirmation on a +19% five-session move; a bearish
  RSI divergence at the upper Bollinger band with RSI 69.9; and **no issuer event until 2026-11-03**.
- ⚠ `PSX` / `VLO` hand forward as **filtered-out leaders** (`D251`), **not** as fresh greens.
- 🚫 **`CVX`'s 🟢 is velocity-produced** (`vol_surge` 0.95) and is **not admissible** as an ignition.
