# BET_SHEET — industry_US — 2026-08-07 (Fri) · ONE file, per-sector sections

> Flow/price `asof 2026-08-06 settled` (D74-trimmed), bench **SPY** inline on every relative number.
> **Zero buy/sell language, zero position sizing (P4).** §B freshness tags are filled by ALPHA (stage 9).
> Numbers sourced from `SECTOR_FLOW_US.json` · `module_fundamentals_us` · `us_flow.py` · `module_chart --read`
> · the four `SECTOR_DEEP_*.md` files · `US_LIVE_SHORTLIST.json` · `us_setup_screener.py`.

## ⛔ 0 · What this sheet must say before any name — **the DEEP stage corrected the run FOUR times, and one correction deleted a sector verdict**

| # | Correction | Consequence for this sheet |
|---|---|---|
| **1** | 🚨🚨 **`EA` is a DELISTED security** — Electronic Arts closed a **$55bn Saudi-led go-private on 2026-08-04/05** (`[EDGAR Form 25-NSE + 8-K 2.01/5.01, 08-04]` · `[AP 08-05]` · `[guardian body]` · `[prnewswire, Oak-Eagle AcquireCo]` · `[nasdaq 08-01, replaced in the S&P 500 by Ferguson]`), with **Open=High=Low=Close=209.70 on two consecutive ZERO-volume bars** after a 48,713,698-share settlement print, so its A-grade axes are degenerate too (**RS20 +0.8 / RS60 −0.5 vs SPY are a frozen price against a moving benchmark**) | **EA carries NO section and NO row.** Its 🟢가속 / `vol_surge` 3.78 / OBV 매집 +0.758 / `new_green` are all artifacts of one bar. **The COMM UW→UW− delta is WITHDRAWN** (`SECTOR_ROTATION.md` §5) and **`S68-ANNEX` voids that bracket's leg (i) by construction** |
| **2** | ★★ **DEEP-ENRG rejected BKR** — the run's only chain-hop candidate — as **D10 boilerplate** (549 articles re-scanned; its one proximity hit traces to the Hormuz-transit article **R46** already disqualified; its real driver is the Chart Industries integration) | **BKR is dropped from §A and filed to the rejection ledger.** EVENT_ALPHA Card 1 handed it forward; **DEEP killed it. The funnel worked** |
| **3** | ★★★ **DEEP-INDU inverted the electricals ranking on primary filings**: "data center" mentions **PWR 16 > ETN 6 ≫ AME 1 > EMR 0** — **the exact inverse of the flow-tag ranking** | **EMR's 🟢 (the board's #3 flow score) describes a process-automation name.** §C flags it |
| **4** | ★★★ **DEEP-FIN replaced the desk's rate mechanism with FRESH primaries** — it pulled **JPM, BAC and GS Q2-2026 10-Qs (filed 08-06, 07-31, 08-03 — all under a week old)**, superseding the FY2025 filings **M425** rested on. **All three now attribute NII growth primarily to BALANCE-SHEET VOLUME**, and **GS's mechanism FLIPPED** from *"NII rose because rates fell"* (FY2025) to volume-driven with expense also rising | ⇒ **a BULL steepener threatens the VOLUME leg via growth deceleration — which is what all three now cite as the driver.** This is a **better** mechanism than M425's cost-of-funds framing and it **strengthens `S66` branch A** |

⚠ **And one instrument trap that would have manufactured a false contradiction on this sheet (`D208`, new).**
**`module_flow` and `module_chart --read` both print an axis called "OBV" with near-identical verdict
vocabulary from DIFFERENT statistics**, and for **MPC** they disagree in sign:

| | `module_flow/_price_flow.py:28–32` | `module_chart/_metadata.py:125–131` |
|---|---|---|
| series | **cumulative** `sign(Δclose)×volume` | a **rolling-window SUM** of signed volume |
| statistic | `(OBV_t − OBV_{t−21}) / Σvolume₂₀` — normalized by **traded volume** | `(obv_now − obv_ref) / max|obv|` — normalized by the **OBV series' own range**, and *labelled* "20d기울기" though it is not a slope |
| MPC's verdict | **매집** (`obv_norm` **+0.244** settled, **+0.199** incl. live) | **분배 ("−26%")** |

⇒ **Both are internally correct; citing one against the other is the error.** **Independently recomputed
with the sweep's own formula, MPC is 매집 on settled AND live bars — the sweep is right.** ⚠ **PSX flips
중립 → 매집 only when the live bar is included, so its settled state is 중립.** **Every OBV figure on this
sheet is the settled `module_flow` one.**

---

# §ENRG · Energy — matrix **N+** → ROTATION **OW−** (continuous slot)

**Sector**: n=16 · wflow **+0.426** · eqflow **+0.209** · breadth 0.120 · **Δ +0.196** · 2🟢/2🔴 ⇒ **rank 1
on BOTH axes.** ★ **And it is the ONLY DEEP sector whose flow, revision and theme axes all point the same
way**: `refining margin` **🟡ACCELERATING 3.06× on n=174**, `distillate exports` **🟡ACCELERATING 25.71× on n=7 (⚠ S5 — a ratio on seven articles is not a trend)**, `diesel shortage` 🟡 2.45× — against `data center power` ⚪ECHO **1.01×**,
`defense spending` ⚪ECHO **0.81× (decelerating)** and `bank net interest margin` **🔴FADING, 7-day
average ZERO**.

## §A · Numbers (`module_fundamentals_us`, today)

| | fwd P/E | trail P/E | P/B | CQ est, 90d | CY est, 90d | CY breadth 30d | mean target upside |
|---|---|---|---|---|---|---|---|
| **PSX** | **10.17×** | 11.56 | 2.85 | **+72.3%** | +60.4% | **13↑ / 2↓** | **+5.8%** |
| **MPC** | 10.54× | 10.10 | 4.35 | **+130.4%** | +84.2% | **13↑ / 0↓** | **+8.1%** |
| **VLO** | 10.62× | 12.28 | 3.66 | **+77.3%** | +49.0% | **13↑ / 2↓** | **+5.2%** |

⚠⚠ **L2 / B2 executed and it produces a NEGATIVE, not a cheapness claim.** `margin_history.py` returns
blank on all three (**M233**) ⇒ **margin percentile `unknown` (C3)**, so **no name here is called cheap.**
And **the estimate surge is already arbitraged**: current-quarter consensus up **72–130% in 90 days**
against **mean-target upside of only +5.2% to +8.1%.** ⇒ **consensus chasing, by L2's own rule.**
★ **DEEP-ENRG adds the second-derivative half**: **FY26 consensus rose 18–28% in ONE WEEK** (MPC 39.08→**49.80** · VLO 35.41→**41.66** · PSX 21.02→**25.52**), **reversing the "first weekly cut" the 08-06
run flagged as week 1 of a flip condition.** ⇒ **the rate is re-accelerating, not decaying (B1).**
⚠ **R8 re-argued, not smuggled**: PSX **10.17× < MPC 10.54× < VLO 10.62×** today **reverses** the 07-22
ordering (MPC 8.8 < VLO 9.4 < PSX 10.8) that retracted R8. **The ordering inverted in 16 days** ⇒
*"cheapest large refiner"* has a ~16-day half-life and **should not sit in the cycle registry's
`core_pick_why`, where it still does.**

## §B · Thesis + freshness *(ALPHA fills the tag)*

**The distillate bottleneck's earning geography is the US Gulf export terminal, and the volume is
measured**: US distillate exports at a **record 1.88m b/d (+98k WoW)** with inventories **−3.47m bbl** and
stockpiles at their **lowest seasonal level since 1996**, cargoes clearing to NW Europe — `[ING/Patterson
& Manthey off the EIA release, fxstreet body]` + `[oilprice/ZeroHedge body, Goldman's Dart & Struyven]`.
⚠ **D5: the "since 1996" leg is ONE source counted twice; ING's 1.88m b/d is the independent leg.**
⚠⚠ **C2, the other half — and it is geography, not contradiction**: **Fujairah middle distillate rose
10% to a FOUR-MONTH HIGH** the same week `[hellenicshipping/FOIZ/Platts bodies]`. ⇒ **the bottleneck is
REGIONAL, and `HO=F` is NY Harbour — the contract for the basin the exports are draining.**

**Name-level W4/A6, resolved by DEEP-ENRG on primary evidence:**
- **VLO** — **books the rent on its own management's attribution** (Q2 call: capture-rate gain tied
  explicitly to distillate/jet export demand for Gulf Coast barrels; **jet yield 7% → 12% y/y**).
- **MPC** — **the largest named Gulf-Coast export-capable capacity** (Galveston Bay **631 kbpd** +
  Garyville **617 kbpd** = **1,248 kbpd**) and **the only one committing NEW capex to it** (a 90 kbpd
  distillate hydrotreater, YE2027).
- **PSX** — ⚠ **its own segment disclosure, the most granular of the three, shows its Gulf Coast unit's
  Q2 beat was the SMALLEST of its beating segments (+8.2%)** ⇒ **PSX's numbers do not support the rent
  claim this quarter.** (Its **Atlantic Basin/Europe** margin was the only regional MISS, **$14.44 vs
  $19.77 est, −27%** — the shortage geography earning least, which is what "rent accrues to the
  exporter" predicts.)

## §C · Flow / positioning

| | tag | flow | RS20 / RS60 | `vol_surge` | OBV (settled) | Δ | FINRA z | implied move |
|---|---|---|---|---|---|---|---|---|
| **VLO** | 🟡 | +0.574 | **+5.5 / +18.2** | 1.02 | **매집** (+0.190) | +0.223 | −0.83 | ±1.8% (D0, **uninformative**) |
| **MPC** | 🟡 | +0.453 | +3.4 / +14.6 | 0.96 | **매집** (+0.244) | +0.031 | +1.30 | **±7.1% (D14, expiry 08-21 — the only real-horizon straddle in the sector)** |
| **PSX** | 🟡 | +0.416 | +6.0 / +13.2 | 1.13 | **중립** (+0.045) | +0.078 | −0.83 | ±2.1% (D0) |
| **COP** | 🟡 | +0.569 | +5.8 / −2.9 | 0.99 | 매집 | **+0.338** | — | — |
| **OXY** | 🟡 | +0.315 | +4.9 / −2.3 | 1.02 | 중립 | **+0.734 (sector's largest)** | — | — |
| **EOG** | 🟡 | +0.336 | −0.2 / −1.8 | 1.02 | **매집** (+0.183) | **+0.517** | — | — |
| *XOM* | 🟢 | +0.688 | **+10.4 / −0.5** | **0.85** | 매집 | +0.119 | 0.17, **5v5 +11.4▲ = board's largest short BUILD** | ±1.4% (D0) |
| *CVX* | 🟢 | +0.711 | +6.5 / −1.5 | 1.02 | 매집 | +0.131 | −0.48 | ±1.4% (D0) |

⚠⚠ **The two 🟢 are the crowded layer by the desk's own read** — both **velocity-lit** (`vol_surge` 0.85 /
1.02) with **RS60 ≈ 0**, i.e. all of their move is 20-day, while **the money and the 60-day base sit in
the 🟡 refiners.** **D6: the tag axis is pointing at the two names §B says do NOT book the rent.**
★ **EOG is the ONE screener setup that intersects the flow sweep**: `us_setup_screener --sector Energy`
put it in the leader-pullback basket (RSI 42.1, px/200 +8%, ~2% off its 50DMA) **and** it carries
**positive flow, OBV 매집 and Δ +0.517.** ⚠ **But `module_chart --read` gives it a BEARISH divergence
(price high↑ / RSI high↓) and a `PULLBACK-TO-SUPPORT` verdict** — recorded against it, not hidden.

## §D · Competition / peers
Refining is the node; the integrateds (XOM/CVX) are a different business with a different driver — and
**R39 killed *"XOM is 0% refining"***, so **the Energy label's refining share is `unknown` (C3)**, not zero.
⚠ **W5, measured**: **XLE exc5 −4.98 · XOP −8.09 · OIH +0.70** = an **8.8pp spread inside one label**; and
**refining beats integrated on both independent axes** (RS60 MPC +14.6 / VLO +18.2 / PSX +13.2 vs XOM
−0.5 / CVX −1.5; CY revision breadth 13↑/0–2↓ vs **XOM 4↑/12↓** per M427). ⇒ **"Energy" is the wrong unit.**

## §E · Refutation + dated catalyst
- ⚠⚠ **P4⁗'s anti-signal is HALF-FIRED**: dist−gas **compressed once** (40.211 → **39.627**). **A SECOND
  consecutive settled compression withdraws the leg — TONIGHT decides it.**
- ⚠ **08-06's own registered break condition technically FIRED**: RS60 declined a 2nd consecutive session
  on all three (MPC 17.2→14.6 · VLO 21.1→18.2 · PSX 13.7→13.2). **But RS20 recovered on the same session**
  (+2.8→+3.4 · +3.6→+5.5 · +4.6→+6.0). **The 60-day leg erodes while the 20-day leg stabilises** — and
  **`S67` tracks the RS20 median, the newer window, not the one that breached.**
- **`S67` → 2026-08-13**: median RS20 vs SPY of {MPC, VLO, PSX}, registration **+5.488**, **A ≤ −2.20
  falsifies today's promotion · B ≥ +13.56 · C between.** **`S55` → 08-11. `S64` → 08-13.**
- **Kill line**: HY OAS ≥ 3.10 (S26) hands the sector to the credit branch, not to this thesis.

---

# §FIN · Financials — matrix **OW** → ROTATION **OW−** (continuous slot)

**Sector**: n=47 · wflow **+0.241 (rank 2, was rank 1)** · eqflow **+0.125** · breadth **0.130** ·
**Δ −0.076** · 6🟢/8🔴. ⚠ **DEEP-FIN's verdict: "arithmetically survivable but with ZERO margin left."**

## §A · Numbers — the un-owned leg is the interesting one

| | CY est, 90d | CY breadth 30d | CY breadth 7d | flow tag |
|---|---|---|---|---|
| ★★ **GS** | **+19.2%** | 🚨 **19↑ / 0↓** | 🚨 **19↑ / 0↓** | **🔴분산**, flow −0.167, RS20 **−4.5** / RS60 +5.3, Δ −0.262 |
| **JPM** | +8.2% | 8↑ / 0↓ | 7↑ / 0↓ | 🟢 (velocity-only, `vol_surge` **0.68**) |
| ⚠ **WFC** | +4.6% | 17↑ / 1↓ | — but **next-quarter 7↑ / 10↓ (30d) and 1↑ / 3↓ (7d), estimate −0.7%/90d** | 🟡 — **OUT of the green set**, RS20 **−1.5**, Δ −0.185 |

⚠ **margin percentile is not a meaningful axis for banks** (no comparable gross-margin series) ⇒
**`unknown` (C3)** and **no cheapness claim is made on any name here.**

## §B · Thesis + freshness *(ALPHA fills)*
★★★ **The mechanism is now primary-sourced from filings under a week old, and it changes what a
steepener means.** DEEP-FIN pulled **JPM (08-06), BAC (07-31) and GS (08-03) Q2-2026 10-Qs** — superseding
the FY2025 filings **M425** used. **All three now attribute NII growth primarily to balance-sheet VOLUME**;
JPM and BAC still name lower rates as a headwind; **GS's stated mechanism FLIPPED from "NII rose because
interest expense fell on lower rates" to volume-driven with expense also rising.** ⇒ **a BULL steepener
attacks the volume leg through growth deceleration — the leg all three now cite** — which is a different
and better-founded threat than the cost-of-funds framing, and it is why **`S66`** exists.
⚠⚠ **And the sector's own narrative axis is dead**: `bank net interest margin` reads **🔴FADING with a
7-day average of ZERO on n=4.** **The NIM story is not what the market is discussing.**

## §C · Flow / positioning
**Greens**: **MET** +0.769 (RS20 +7.4 / RS60 +24.2, `vol_surge` 1.23, **volume-confirmed**) · **MA** +0.702
(+7.8/+11.7, **velocity-only 0.90**) · **PRU** +0.697 (+3.4/+16.2, 1.40, volume-confirmed) · **BRK-B**
+0.554 (+3.6/+5.4, **velocity-only 0.86**, ⚠ **reports Q2 2026-08-09 — INSIDE S65's window**) · **BAC**
+0.520 (+4.1/+20.7, **velocity-only 0.74**) · **JPM** +0.492 (+4.0/+14.8, **velocity-only 0.68**).
⇒ **three of six greens are velocity-only.** **XLF exc5 −2.20 / exc20 +1.85 · KRE exc5 −2.85.**
⚠ **28 of 300 universe tickers return 0 on the FINRA pull regardless of coverage (M152)** and that list
includes **C · GS · ICE · MA · MET · AIG · ALL · CB** ⇒ **a zero there is uninformative, not clean.**
★ **DEEP-FIN pulled GS's short-vol z fresh (the mandate flagged it un-pulled): +0.91, no divergence.**
★ **`module_chart --read GS`: `BASING (unconfirmed turn)`, RSI 48.1, price above 3 of 4 MAs** — **a third
axis that sits with the revision book and against the 🔴 tag.**

## §D · Competition / peers — W5
Sub-node spread: money-centres (JPM +4.0 / BAC +4.1) · insurers (**MET +7.4 / PRU +3.4, both with RS60
+16 to +24**) · payments (MA +7.8) · **brokers (GS −4.5, 🔴)** · regionals (**KRE exc5 −2.85**, HBAN −4.5).
⇒ **insurers carry the sector's best 60-day base while the broker with the best revision book carries its
worst tag.**

## §E · Refutation + dated catalyst
- **`S65` → 08-11**: median RS20 vs SPY {JPM, BAC, WFC, BRK-B}, **+3.805 = branch C** (A ≤ +0.34 · B ≥
  +6.81). ★ **WFC's exit does NOT move it** — DEEP-FIN recomputed the median ex-WFC at **+4.0 vs +3.805
  with it, both deep in C.** ★ **And the "BRK-B is dragging" companion note is numerically dead: ex-BRK-B
  reads +3.97 vs +3.805, a 0.17pp gap** (it was +5.219 vs +3.405 at registration) ⇒ **the 08-06 within-run
  correction that it was an n=4 estimator artifact is confirmed on fresh data.**
- **`S51` → 08-10** (2s10s at tonight's settle) — ⚠⚠ **branch A cannot be read as confirmation** (its own
  bull-steepener caveat); **`S66`** owns that leg. **`S69` → 08-13** (MET's tag vs its falling estimates).
  **`S63` → 08-13.** **BRK-B prints 08-09, inside S65's window.**
- **Kill line**: derived 2s10s **≤ +0.20** (currently **+0.45**, buffer 25bp — and the 3-print flattening
  trend **reversed** on its 4th print). Credit overlay: **HY OAS ≥ 2.90** (currently 2.75, **15bp**, and
  **it has not printed since the payroll data ⇒ `unknown`, C3**).

---

# §INDU · Industrials — **OW− held** (rotating slot, recency-starved fallback)

**Sector**: n=50 · wflow +0.088 · **eqflow +0.110 > wflow ⇒ breadth-led** · breadth 0.120 · Δ −0.038 ·
6🟢/11🔴. **XLI exc5 −0.05 / exc20 −0.23 — the flattest sector of 11 on BOTH windows, second run running.**

## §A/§B · **DEEP-INDU's verdict: defence, not electricals** — and the primary filings invert the tape

| Name | "data center" mentions in its 10-K | CY est 90d | CQ breadth 30d | flow tag | RS20 / RS60 |
|---|---|---|---|---|---|
| **PWR** | **16 — deepest disclosure** | ★ **+19.3%** | 2↑ / 1↓ | 🟡 | 🚨 **−2.3 / −18.5** |
| **ETN** | 6 | +1.4% | ⚠ 3↑ / 4↓ | 🟢 +0.789 | +8.2 / +3.0 |
| **AME** | 1 | +2.2% | 2↑ / 1↓ | 🟢 +0.726 | +5.7 / +4.3 |
| **EMR** | 🚨 **0** | +0.7% | 🚨 **0↑ / 2↓** | 🟢 **+0.950 (board's #3)** | +11.6 / +8.6 |

⇒ ★★★ **The disclosure ranking is the exact INVERSE of the flow-tag ranking.** **EMR's 🟢 describes a
process-automation name** (M436: its power language is *"Final Control … power end markets"* = process
valves); **PWR is the only name where the filing, an acquisition trail (CEI) and the estimate book all
agree — and it is the one price abandoned.**
⚠⚠ **And the narrative axis agrees with the filings, not the tape**: `data center power` reads **⚪ECHO at
1.01× on n=420 — flat, not accelerating.**

**Defence — EVENT_ALPHA Card 5's substitution risk is REFUTED at the primary level.** DEEP-INDU pulled
RTX/LMT/GD/NOC 10-Ks and ran a 60-day DSCA/FMS search **that came back empty**: FMS is
government-to-government and **already booked** (**LMT backlog $193.6bn, +9.9% y/y**), FMS-to-any-single-
country is **low-single to low-double-digit revenue share (GD ~1.9%, RTX 8%)**, and **RTX's own 10-K
carries the precedent that China's Taiwan-FMS sanctions did not reverse booked backlog.** ⇒ **Card 5 is
downgraded to a narrative-only leg.** ⚠ **But the theme axis is decelerating: `defense spending` ⚪ECHO
0.81× on n=308**, and **`module_chart --read RTX` reads RSI 83.1, momentum20d +12.7%, price above 4 of 4
MAs, Bollinger expanding 22.6% = extended.**

## §C · Flow / positioning
**RTX** 🟡 +0.606, **RS20 +12.1 / RS60 +21.0 vs SPY (A-grade, both positive)** with OBV **매집 (+0.442, the strongest of the primes) AGREEING rather than carrying it (D6)**, **Δ +0.410**, z +0.59
(5v5 +5.2▲) · **LMT** 🟡 +0.594, +10.2/+9.8, 매집, z +0.31 (5v5 +6.7▲) · **NOC** 🟡 +0.344, +4.4/−0.4, 매집,
Δ +0.233 · **GD** 🟡 +0.297, +1.0/+8.5, 매집 · **LHX** 🟡 +0.406, −2.4/−8.2, 매집.
⇒ **Five primes, five 🟡, five OBV 매집, ZERO 🟢** — a uniform accumulation signature the tag filter cannot
show ROTATION. ★★ **AME (z −2.03, 5v5 −2.2▼) is the ONLY 🟢 short-collapse on the entire FINRA pull**, and
it is an S62 leg. ⚠ **margin percentile is `unknown` (C3) for RTX/NOC/GD/LHX** — `margin_history.py`
returns a **stale pre-2020 window** for all four (a measured tool gap, not a guess); **computable only for
EMR/ETN/AME/PWR/LMT.**

## §D/§E · Refutation + dated catalyst
- **`S62` settles TONIGHT** at **+13.045** (INDU median +6.925 − XLU −6.12). ⚠⚠ **`D206`: branch A needs
  XLU's RS20 to move 18.96pp relative in ONE session against a ±0.5% straddle ⇒ arithmetically
  unreachable. Tonight's near-certain branch-B print is NOT confirmation the bracket earned.** ★ **And
  DEEP-INDU adds the decisive structural point: S62's basket contains ZERO defence names, so it cannot
  adjudicate the electricals-vs-defence question however it settles.** *(S62 independently reproduced at
  +13.043 vs the handed +13.045 — D5 ✅.)*
- ⚠ **VST · PPL · EMA · AQN · OKLO all printed PRE-MARKET today** and XLU is one of S62's two legs —
  `[nasdaq 08-06 pre-market list]`. **`CATALYST_WATCH.json` carried only VST, and with no BMO/AMC field.**
- ⚠⚠ **M437 binds and must not be re-argued**: **UNP FY2025 surcharge revenue −$218M vs fuel expense
  −$84M = −$134M NET NEGATIVE; NSC −$134M vs −$55M = −$79M net.** ⇒ **crude weakness is NOT an Industrials
  tailwind.** **`S54` → 08-10 · `S64` → 08-13.**
- **W5**: ★ **DAL RS60 +25.2 and UAL +29.7 against negative-to-flat flow** (−0.063 / −0.369) — the sector's
  largest RS60/flow divergence, un-owned by any thesis.

---

# §COMM · Communication Services — **UW** *(the UW− notch was WITHDRAWN at DEEP — see §0)*

**No candidate is advanced from this sector.** The section exists because the slot produced the run's
most consequential correction, and because it leaves ONE inherited item.

**Sector, corrected**: n=13 as measured, but **12 are live.** ex-EA: eqflow **+0.0893 (−34.5%)** · wflow
+0.0548 · **1🟢** · breadth **0.083, 6th of 11** (as cited: 0.150, 2nd). **XLC exc5 +0.69 / exc20 −1.64.**

★ **The assignment DEEP-COMM was sent to settle, answered**: **positive revision books DO exist in this
sector — and only in telecom.** **TMUS current-year breadth 15↑ / 3↓ (30d), next-quarter +5.7%/90d** ·
**VZ 10↑ / 2↓** — against **DIS 1↑ / 7↓ (30d), CQ −4.1% / NQ −2.9% over 90d.**
⇒ **the promotion named the wrong two names.** ⚠ **T (+10.4) · VZ (+9.0) · CMCSA (+5.6) all carry positive
RS20 and (T, CMCSA) OBV 매집 — but all three are 🟡, not 🟢, and ALL THREE carry NEGATIVE RS60** (−8.6 /
−4.5 / −3.4). ⇒ **a candidate node for a future run, explicitly NOT a basis for a verdict today.**
⚠ **GOOGL/GOOG's apparent +44.7% / +44.5% CY revision jump was tagged `unknown` (C3) as a likely
base-effect** rather than carried — recorded so it is not quoted next run as a finding.
★ **DIS is the sector's strongest chart** — `module_chart --read`: **OBV 누적 +128% slope, `CONFIRMED-TURN`,
RSI 70.0, upper band, price above 4/4 MAs** — **against its 1↑/7↓ revision book.** ⇒ **two price/flow axes
positive vs one fundamental axis negative**, which is exactly why **`S68` leg (ii) is the scoreable one.**
★ **Meta's legal observable was BUILT from primary evidence and it cuts against the tail story**: **Meta's
own 10-Q already discloses the AG's $62.85bn ask, making the $942M judgment ≈1.5% of it**, and options
positioning (**P/C 0.65, call-heavy, skew −2.0**) shows the market is not pricing it as structural.
⚠ **C2, the other half**: `teen safety` reads **🔴FADING (7-day average 0.0, n=10)** while the doctrine
term **`public nuisance` reads 🟡ACCELERATING 8.57× on n=45** — **the two framings of one event disagree,
and the accelerating one is the legal doctrine.** **Chain-hop returned a NULL result (boilerplate, D10).**
**Alphabet's personnel leg is tagged `[unverified]` (A5): no 8-K exists for the reshuffle.**

---

# §X · Cross-sector LIVE shortlist — included or dropped with a reason

`US_LIVE_SHORTLIST.json` (mcap ≥ $10B ∧ 🟢가속 ∧ flow desc top-15). **Names outside the four DEEP
sectors, with a verdict each — none is advanced without one:**

| Name | flow · RS20/RS60 · surge · OBV | FINRA | Verdict |
|---|---|---|---|
| **SHOP** | +1.000 · **+17.5 / +39.8** · 2.09 · 매집 | −0.12 △ | **CARRIED as a watch.** Board's #1 flow score, both legs positive. ⚠ **Lens 3: margin at its series LOW (0th percentile, 48.1%) against a 101× trailing P/E — a margin-vs-multiple conflict, not a peak-margin trap.** IT sector, no DEEP slot |
| **PLTR** | +0.955 · +18.6 / +9.9 · 1.73 · 매집 | −0.34 △ | **CARRIED as a watch.** ⚠ **d21-60 is NEGATIVE (−7.4): all of RS60 is the last 20 sessions.** Margin **88th percentile** |
| **BMY** | +0.900 · +8.5 / +11.3 · 1.42 · 매집 | **−0.78 ✅ clean rise** | ★ **CARRIED — the ONLY dual-axis-strong name in Health Care** (NQ revision breadth 12↑/1↓), and the one Lens 1 named as a standalone watch rather than a sector case |
| **PH** | +0.828 `new_green` · +10.5 / +18.4 · 1.29 · 매집 | **−1.34 ✅** | **CARRIED with a stamped caveat**: **margin 94th percentile at a record high**, estimates flat (+0.3%), **CY breadth 3↑/5↓** ⇒ **L2 says the margin has no room left and the flow flip is not confirmed by revisions** |
| **MSFT** | +0.808 · **+27.8** / +17.2 · **1.14 velocity-only** · 매집 | **+1.68 ⚡crowded-short** | **CARRIED, hard-stop stamped.** Board's highest RS20 **but near-term breadth is net-down (CQ 1↑/4↓)**, d21-60 **−8.5**, and ⚡ is turn-conditional squeeze fuel, **never a standalone** |
| **IDXX** | +0.731 · +3.4 / +6.9 · 1.46 · 매집 | **+1.51 ⚡** | ⛔ **DROPPED — revisions are outright NEGATIVE** (CQ −2.0% / NQ −2.1%) against a positive RS. Ledger row filed |
| **TRI** | +0.933 · +10.5 / +8.3 · 1.48 · 매집 | −0.21 △ | ⛔ **DROPPED — coverage without belief for a 2nd run.** Measured flow rows, **no 4Phase, no thesis anywhere** ⇒ no thesis may be built on it. Ledger row filed |
| **MA** | +0.702 · +7.8 / +11.7 · **0.90 velocity-only** · 매집 | **−0.76 ✅** | **CARRIED inside §FIN.** ⚠ **MA is on the M152 `_US_STOP` list** ⇒ a FINRA zero would be uninformative; the −0.76 here is a real read |
| **DIS · EA** | — | — | **§COMM. EA is DELISTED (§0). DIS carries no candidate status while its revision book is 1↑/7↓** |
| **WAT · MRK · AMGN** | HLTH greens | — | ⛔ **NOT advanced.** ROTATION's HLTH promotion was declined on the sector's **own registered anti-signal firing a 2nd consecutive run** (SPY +3.62% / XLV +0.57% / excess −3.05pp), **MRK's green is velocity-only (0.91)**, and **AMGN's CY breadth is 3↑/12↓ with its 90d column reading 0.00 ⇒ `unknown` (C3)** |
| **ANET** | +0.635 · +1.9 / **+37.0** · 1.40 · 매집 | — | ★ **CARRIED as the cleanest instrumented rank-1 epicenter expression** (Lens 4). **d21-60 +33.7 with RS20 still positive ⇒ a genuine pause, not the M429/PSX artifact.** Revisions 0-down every horizon, CQ +18.0% |
| **APH** *(new, never named by this desk)* | +2.9 / **+35.3** | — | ★ **CARRIED as a watch** — Lens 3's find: an AI-datacenter connector adjacent to ANET, **0-down revisions at every horizon (n up to 9)**, d21-60 +30.8 **with RS20 positive** ⇒ a real base rise. ⚠ **margin 90th percentile** |

## §X-2 · Setup-screener candidates — and a structural finding about the instrument
`us_setup_screener.py` returned **13 setups across the four DEEP sectors** (ENRG 6 · FIN 5 · INDU 2 ·
**COMM ZERO of 13 names**). ⚠⚠ **Eleven of the thirteen carry a NEGATIVE flow score and five are 🔴분산.**
⇒ **that is structural, not a coincidence**: the leader-pullback basket selects on **RSI < 45 and 50DMA
proximity**, which mechanically prefers names whose recent relative strength is negative. **A name that
appears ONLY in the screener and nowhere in the flow sweep is a mean-reversion candidate, not a flow
candidate, and this sheet says which of the two it is.**
★ **The single intersection is EOG** (§ENRG §C). ★ **And COMM producing ZERO setups is a third
independent axis against the withdrawn promotion**, after the revision books and the EA correction.

---

# §Z · Epicenter-starter module — **no cycle GAP, so no starter is required**

`cycle_exposure.py`: **rank 1 AI-compute epicenter 23.67% vs a 12.0% floor** (AVGO · NVDA · ANET · TSM) ·
**rank 2 Energy/refining 10.06% vs 8.0%** (MPC · PSX) ⇒ ✅ **no GAP, so the tape-independent core-starter
clause does not fire.**
⚠⚠ **But 8.67pp of the book cannot be graded at all**: **TSM $417.51 of the $2,562 rank-1 epicenter total
(16.3%)** and **LNG $525** are outside `us_top300`. **Ex-TSM the rank-1 epicenter still clears the floor at
~19.7%, so the ✅ survives — but the 11.6pp margin overstates the measurable part by about a third.**
★ **And the rank-1 epicenter is cleanly split by phase (M149, computed this run)**: the seven names with
positive RS60 (**AMD · MU · ASML · AMAT · LRCX · KLAC · MRVL**) **all have a NEGATIVE last-20 leg** = a
decaying stock of past excess, while **the three the book HOLDS (NVDA · AVGO · ANET) are the ONLY three
with a POSITIVE last-20 leg.** ⇒ **the 6-of-10 🔴분산 flip is the decay of an old run the book is not in.**
🚨 **Structural gap carried, not fixed: 11 of the desk's 27 greens are in NO cycle at all** — EMR · AME ·
TRI · PH · BA · MET · SHOP · PLTR · DIS · NUE · STLD (+ BKR). **EMR and AME are two of the four legs of a
bracket settling tonight.** **Registry edits are human-gated (P5).**

---

# §L · Ledger rows filed by this stage

**Rejections** (`reject_ledger.py add`, each with a reason class, a `--revives-if` and a `--recheck-date`):
**BKR** `K.본문반증` · **IDXX** `H.밸류소진` · **TRI** `B.모멘텀only`.
**Missed** (`missed_ledger.py add`, each with an `--enters-if`): **TMUS** `Q.확신부족` (the sector's best
revision book, no flow carrier) · **APH** `U.발굴부재` (never named by this desk).
⚠ **EA is filed to NEITHER ledger** — a delisted security is not a rejection or a miss, it is a
**universe-integrity defect**, and it is recorded as `S68-ANNEX` plus a dig instead.

**Sizing**: **none.** ⚠ **The exposure state carried by HANDOVER (`방어`, target 55%, band gap +0.5pp) is
the KR contest book's rule on `069500.KS` and is explicitly NOT a US sizing input (W1)** — so this sheet
supplies candidates without a target to fill, and says so rather than implying one.

---

# §B-ALPHA · Freshness gate — appended by stage 9 (ALPHA). Append-only; nothing above is rewritten.

> `theme_age` deterministic novelty run FIRST (token-0), then positioning, then a targeted live check.
> **🟢LIVE / 🟡PARTIAL (residual + a dated re-check) / 🔴RESOLVED (dropped AND ledgered).**
> ⚠ **Every 🟡 carries a re-check date, and every tag follows the NAME, not its sector's turn in the
> rotation** — the measured failure this rule exists for cost the desk **+12.3% over five sessions on an
> untracked 🟡** (006360, 07-20).

## ★★★ B-0 · The gate itself is mis-calibrated, and this run has the cleanest possible proof (F1, 9th run)

**Not one theme on the board reaches 🟢FRESH.** The gate, read at source
(`module_news_data/_theme_age.py:62`), is `v = "FRESH" if (age <= 14 and not censored) else "ACCELERATING"`
— i.e. **an AGE filter, plus a censoring flag.**

| theme | verdict | age | accel | n |
|---|---|---|---|---|
| **`polysilicon tariff`** | 🟡ACCELERATING | **17** | **25.71×** | 7 |
| `distillate exports` | 🟡 | 29 | **25.71×** | 7 |
| `yen intervention` | 🟡 | ≥90 | **13.19×** | **193** |
| `public nuisance` | 🟡 | ≥90 | 8.57× | 45 |
| `refining margin` | 🟡 | 70 | 3.06× | **174** |
| `Section 232` | 🟡 | 70 | 2.76× | 108 |
| `diesel shortage` | 🟡 | 23 | 2.45× | 11 |
| `windfall tax` | 🟡 | 45 | **2.38× (was 9.05× on 08-06, n unchanged at 29 ⇒ ZERO new articles)** | 29 |
| `video game` · `AI capex` · `data center power` · `defense spending` · `steel prices` · `copper` · `Strait of Hormuz` | ⚪ECHO | 76–≥90 | **0.81× – 1.98×** | 41–6,394 |
| `teen safety` · `bank net interest margin` · `export drain` | 🔴FADING | 65–78 | **0.0×, 7-day avg ZERO** | 4–10 |
| `Hormuz coordinates` | ⚫SILENT | — | — | **0** |

⇒ ★★★ **`polysilicon tariff` carries the board's joint-highest acceleration and fails the gate by THREE
DAYS of age.** **That is a calibration property, not an empty universe** — which is exactly what F1 says,
and it is the sharpest instance the desk has recorded. ⚠ **The gate change is NOT made here (P4);** it is
a scoring change and needs a human.
⚠ **S5 binds hard on the top of that table**: the two 25.71× readings are **n=7**. **A ratio on seven
articles is not a trend, and neither is quoted as one.**

## B-1 · Tags

| Name | Tag | Evidence label + date | Residual / why |
|---|---|---|---|
| **VLO** | **🟡PARTIAL** | flow 🟡 +0.574 · RS20 **+5.5** / RS60 **+18.2** vs SPY · OBV 매집 (+0.190 settled) · Δ +0.223 · `asof 2026-08-06 settled`; theme `refining margin` **🟡 3.06× on n=174**; management's own export attribution `[Q2 call]` | **Residual: it is 🟡 and not 🟢 because `vol_surge` 1.02 blocks the tag, and L2 is UNRUNNABLE (`margin_history` blank, M233) so no cheapness claim exists.** ⚠ **And the estimate surge is arbitraged — mean-target upside +5.2%.** **Re-check 2026-08-13 (`S67`'s settle)** |
| **MPC** | **🟡PARTIAL** | flow 🟡 +0.453 · +3.4 / +14.6 · OBV 매집 (+0.244, verified independently) · z **+1.30** · **±7.1% implied to 08-21 — the only real-horizon straddle in the sector** | **Residual: largest named Gulf-Coast capacity + the only new capex, but its OWN capture number is not the one management attributed to exports (VLO's is).** **Re-check 2026-08-13** |
| **PSX** | **🟡PARTIAL** | flow 🟡 +0.416 · +6.0 / +13.2 · **OBV 중립 (+0.045 settled — it only flips 매집 if the live bar is included)** · Δ +0.078 | ⚠ **Its own segment disclosure says its Gulf Coast beat was the SMALLEST of its beating segments** ⇒ the rent claim is not supported for PSX this quarter. **Re-check 2026-08-13** |
| **EOG** | **🟡PARTIAL** | flow 🟡 +0.336 · **Δ +0.517** · OBV 매집 (+0.183) · RS20 −0.2 / RS60 −1.8 · **the ONLY setup-screener hit that intersects the flow sweep** | ⚠ **`module_chart --read` gives it a BEARISH divergence (price high↑ / RSI high↓) and `PULLBACK-TO-SUPPORT`** — the residual is the divergence. **Re-check 2026-08-14** |
| **XOM · CVX** | **🔴RESOLVED as the sector expression** *(NOT as businesses)* | both 🟢가속 but **velocity-lit** (`vol_surge` 0.85 / 1.02) with **RS60 ≈ 0** (−0.5 / −1.5); XOM's **FINRA 5v5 +11.4▲ is the board's largest short BUILD**; `Strait of Hormuz` ⚪ECHO **1.98×, age ≥90** | **The move is 20-day and the narrative is old and loud. Dropped from the bettable list as the Energy expression** — the money and the 60-day base are in the 🟡 refiners. ⚠ **NOT ledgered as a rejection: XOM is a HELD-adjacent name and CVX is a sector control; this is a tag on the EXPRESSION, not a verdict on the businesses (C4)** |
| **GS** | **🟡PARTIAL** — the run's sharpest single disagreement | **CY revision breadth 19↑ / 0↓ at BOTH 7 and 30 days, CY +19.2%/90d** (the sector's best) vs **🔴분산, flow −0.167, RS20 −4.5, Δ −0.262, OBV −0.134 (verified)**; `module_chart --read`: **`BASING`, RSI 48.1, price above 3/4 MAs**; **freshly-pulled FINRA z +0.91 = no divergence** | ⚠⚠ **A genuine flow/fundamental split, NOT an artifact — declared unresolved for a 5th consecutive run.** **Two of three axes (revisions, chart) say basing; one (flow tag) says distribution.** **Re-check 2026-08-14** |
| **MET** | 🔴**RESOLVED — dropped** | 🟢가속 +0.769, RS20 +7.4 / RS60 +24.2, `vol_surge` 1.23 — **against FY and next-year estimates −0.7%/90d and revision breadth net-down on 3 of 4 horizons**; d21-60 **+15.2** vs RS20 +7.4 ⇒ old money | **Dropped and BRACKETED rather than ledgered: `S69` (→08-13) is the frozen falsifier**, so the name is tracked by a bracket instead of a rejection row. **The bracket IS the re-check** |
| **BRK-B** | **🟡PARTIAL** | 🟢 +0.554, +3.6/+5.4, **velocity-only 0.86** | ⚠⚠ **Reports Q2 2026-08-09 — INSIDE `S65`'s window (settles 08-11).** ⇒ **S65's scorer must not read a BRK-B earnings gap as breadth.** **Re-check 2026-08-11** |
| **JPM · BAC** | **🟡PARTIAL** | 🟢 but **velocity-only** (0.68 / 0.74); RS60 **+14.8 / +20.7** is the real leg; Q2-2026 10-Qs (08-06 / 07-31) attribute NII growth to **balance-sheet VOLUME** | **Residual: the mechanism is volume, so `S66` branch A (a growth scare) is the live threat, not a flattener.** **Re-check 2026-08-10 (`S51`) / 08-11 (`S65`)** |
| **WFC** | 🔴**RESOLVED — dropped** | out of the green set (🟡, RS20 **−1.5**, Δ −0.185) **AND** the only negative revision book among S65's legs (**NQ 7↑/10↓ 30d, 1↑/3↓ 7d, −0.7%/90d**) | **Two independent axes agree.** ⚠ **Not ledgered as a new rejection — it is INSIDE `S65`'s frozen basket, so removing it from the sheet while the bracket still measures it would double-count.** **The bracket is the record** |
| **RTX** | **🟡PARTIAL, momentum-only + hard-stop stamped** | **RS20 +12.1 / RS60 +21.0 (A-grade, both positive)**, OBV 매집 +0.442 agreeing, **Δ +0.410**; primary filings refute the substitution risk (**LMT backlog $193.6bn +9.9% y/y**; FMS share GD ~1.9% / RTX 8%; a 60-day DSCA search returned EMPTY) | 🚨 **Residual is a POSITIONING one: `module_chart --read` gives RSI 83.1, momentum20d +12.7%, price above 4/4 MAs, Bollinger expanding 22.6% = EXTENDED** — and **`defense spending` reads ⚪ECHO 0.81×, DECELERATING.** ⇒ **hard-stop stamped.** ⚠ **margin percentile `unknown` (C3) — `margin_history` returns a stale pre-2020 window for RTX/NOC/GD/LHX.** **Re-check 2026-08-14** |
| **EMR** | 🔴**RESOLVED as an AI-power expression** | flow +0.950 (board's #3) but its **10-K carries ZERO "data center" mentions**, CY +0.7%/90d, **CQ breadth 0↑/2↓** | ⚠ **NOT ledgered as a rejection and this is deliberate (C4): EMR is not refuted as a business — it is refuted as the AI-power node the flow tag implies.** **The tag is on the THESIS.** `data center power` ⚪ECHO **1.01×** corroborates. **Re-check 2026-08-14** |
| **ETN** | **🟡PARTIAL** | 🟢 +0.789, +8.2/+3.0, **6 "data center" mentions and named hyperscale customers by acquisition**; ✅ low-short/short-cover on the shortlist | **Residual: CQ revision breadth 3↑/4↓ (30d) with CY only +1.4%** ⇒ the disclosure is real and the estimates have not followed. **Re-check 2026-08-14** |
| **AME** | **🟡PARTIAL** | 🟢 +0.726, +5.7/+4.3, **z −2.03 = the ONLY 🟢 short-collapse on the entire FINRA pull**, ✅ clean rise | **Residual: only ONE "data center" mention in its 10-K** ⇒ the best B-grade corroborant in the basket sits on the thinnest disclosure. **Re-check 2026-08-14** |
| **PWR** | **🟡PARTIAL — the inverted one** | **16 "data center" mentions (deepest of the four), CY +19.3%/90d (the only real revision acceleration)** | 🚨 **Residual is the price: RS20 −2.3 / RS60 −18.5 vs SPY, 🟡, and it DRAGS S62's median.** ⇒ **filing, acquisition trail and estimates all agree; the tape does not.** **Re-check 2026-08-14** |
| **ANET** | **🟡PARTIAL** | 🟢 +0.635, **RS20 +1.9 / RS60 +37.0**, `vol_surge` 1.40, OBV 매집; **d21-60 +33.7 with RS20 still POSITIVE ⇒ a genuine pause, not the M429/PSX artifact**; revisions **0-down every horizon, CQ +18.0%**; margin 43rd pctile | **Residual: IT holds no DEEP slot, so no sector file owns it this run.** ★ **The cleanest instrumented rank-1 epicenter expression.** **Re-check 2026-08-12 (`S13`)** |
| **APH** | **🟡PARTIAL — new, never named by this desk** | **+2.9 / +35.3**, d21-60 **+30.8 with RS20 positive**, **0-down revisions at every horizon (n up to 9)**, CQ +14.3% | ⚠ **margin 90th percentile (L2 caution)** and **no sector file owns the connector node.** **Filed to the missed ledger (`U.발굴부재`, `--recheck-date 2026-08-21`)** so it cannot vanish |
| **BMY** | **🟡PARTIAL** | 🟢 +0.900, +8.5/+11.3, 1.42, **✅ z −0.78 clean rise**, **NQ revision breadth 12↑/1↓** | **Residual: HLTH's SECTOR promotion was declined on the sector's own anti-signal firing a 2nd run — BMY is a standalone watch, explicitly NOT a sector case (C4).** **Re-check 2026-08-14** |
| **PH** | **🟡PARTIAL, hard-stop stamped** | 🟢 `new_green` +0.828, +10.5/+18.4, ✅ z −1.34 | 🚨 **margin 94th percentile AT a record high, estimates flat (+0.3%), CY breadth 3↑/5↓** ⇒ **L2: no margin room, and the flow flip is unconfirmed by revisions.** **Re-check 2026-08-14** |
| **MSFT** | **🟡PARTIAL, ⚡ + hard-stop stamped** | board's highest RS20 **+27.8**, velocity-only 1.14, **z +1.68 ⚡crowded-short** | **Residual: near-term breadth net-down (CQ 1↑/4↓) and d21-60 −8.5** ⇒ all of RS60 is the last 20 sessions. ⚡ **is turn-conditional squeeze fuel, NEVER a standalone.** **Re-check 2026-08-14** |
| **SHOP · PLTR** | **🟡PARTIAL** | SHOP +17.5/+39.8 (both legs positive, RS20 faster); PLTR +18.6/+9.9 (**d21-60 −7.4 ⇒ all of RS60 is the last 20**) | **SHOP's residual is a margin-vs-multiple conflict (margin at its SERIES LOW, 48.1%, against a 101× trailing P/E — NOT a peak-margin trap, the opposite one).** PLTR's is a 88th-percentile margin. **Re-check 2026-08-14** |
| **NUE · STLD** | **🟡PARTIAL** | NUE +20.1/+13.3 **(above its own trailing-252 85th percentile of +12.95)**, OBV 매집, **NQ +57.0% / CQ +41.8% / 90d**; STLD +15.5/+6.9, NQ +28.8%; **both blocked from 🟢 by `vol_surge` alone (1.01 / 0.88) — the M422/C9 gate, and D6 says a C-grade metric may not veto a disagreeing A-grade one** | ⚠⚠ **Residual is the second derivative (L1): NUE's 7-day breadth is NEGATIVE on three of four horizons (NQ 0↑/1↓, CY 0↑/1↓)** ⇒ **a DECELERATING revision surge.** ⚠ **NUE closed 272.00 against a 272.50 52-week high with margin percentile `unknown`** and `steel prices` reads ⚪ECHO 1.14×. **MATR holds no DEEP slot (5th-run deferral). Re-check 2026-08-13 (`S57`)** |
| **CRWD · PANW · FTNT · DDOG** | 🔴**RESOLVED — the carve-out is NOT renewed blanket** | all four retag **EXHAUSTED**: **PANW (+4.0/+64.3, d21-60 +56.7) and CRWD (+2.3/+49.0, +44.7) have POSITIVE RS20 ⇒ base rise real, recent leg flat**; **FTNT (−4.5/+34.7) and DDOG (−17.0/+9.4) are PSX-pattern (d21-60 inflated by the RS20 collapse, M429)** | ⚠ **NOT ledgered as four new rejections** — the carve-out is a *standing exemption*, and what changes is that it now needs **per-name re-justification.** **Flip conditions, dated: PANW/CRWD → LIVE if RS20 clears +8 while d21-60 holds · FTNT → LIVE if RS20 reclaims positive within two weeks while its 0-down breadth holds · DDOG → only on RS20 above 0. Re-check 2026-08-21** |
| **IDXX · TRI** | 🔴**RESOLVED — dropped AND ledgered** | IDXX: revisions CQ −2.0% / NQ −2.1% against a positive RS, z +1.51 ⚡. TRI: board's #4 flow with **no 4Phase and no thesis anywhere, 2nd run** | ✅ **`reject_ledger.py add` filed with class + `--revives-if` + `--recheck-date`** (IDXX `H.밸류소진` → 08-28 · TRI `B.모멘텀only` → 08-21) |
| **BKR** | 🔴**RESOLVED — dropped AND ledgered** | DEEP-ENRG: **D10 boilerplate**; 549 articles re-scanned, its one proximity hit is the Hormuz-transit article **R46** disqualified; real driver = the Chart Industries integration; RS60 −6.8 | ✅ **`reject_ledger` `K.본문반증`, `--recheck-date 2026-08-21`.** ★ **EVENT_ALPHA promoted it and DEEP killed it — the funnel worked in one run** |
| **DIS** | 🔴**RESOLVED as a COMM carrier** | ★ **strongest chart in the run** (OBV 누적 **+128% slope**, **`CONFIRMED-TURN`**, RSI 70.0, upper band, above 4/4 MAs) with **RS20 +6.6 (A-grade) agreeing** — **against CY revision breadth 1↑/7↓ and CQ −4.1%/90d** | **Dropped as the sector's carrier because the sector verdict was WITHDRAWN (EA delisted), not because DIS failed.** ⚠ **NOT ledgered: `S68` leg (ii) IS the frozen falsifier on DIS's revision breadth and it is the only scoreable leg left.** **The bracket is the re-check (08-13)** |
| **EA** | 🚨 **NO TAG — DELISTED, and this is deliberately not a 🔴** | went private **2026-08-04/05** ($55bn, Form 25-NSE + 8-K 2.01/5.01); Open=High=Low=Close=209.70 on two ZERO-volume bars | ⛔ **A delisted security is neither a rejection nor a miss. It is a universe-integrity defect** and it is recorded as **`S68-ANNEX`** + a dig. **Filing it to a ledger would corrupt both ledgers' benchmarks** |
| **TMUS · VZ** | **🟡PARTIAL — the only positive revision books in COMM** | **TMUS CY breadth 15↑/3↓ (30d), NQ +5.7%/90d** · **VZ 10↑/2↓**; RS20 **−3.1 / +9.0** | ⚠ **Neither is a flow carrier (TMUS flow −0.236, 🟡) and BOTH carry negative RS60.** **TMUS filed to the missed ledger (`Q.확신부족`, → 08-21)** so the sector's best book is not lost when COMM rotates out |

**Counts: 🟢LIVE 0 · 🟡PARTIAL 19 · 🔴RESOLVED 9 (3 ledgered as rejections, 2 filed to the missed ledger,
4 tagged on the EXPRESSION or held inside a live bracket rather than ledgered).**
⚠ **🟢LIVE = 0 for a 9th consecutive run, and §B-0 shows why it is the GATE and not the board.**

**Momentum-only / positioning stamps**: **RTX** (RSI 83.1, extended, decelerating theme) · **MSFT** (⚡
crowded-short, breadth net-down) · **PH** (94th-pctile margin at a record high) · **NUE** (RS20 above its
own 85th percentile, revision surge decelerating). **All four carry "hard-stop required."**
⚠ **D6 applied throughout**: no tag above rests on OBV alone; where OBV appears it is stated as agreeing
or disagreeing with the A-grade RS and revision axes, never as the finding.
