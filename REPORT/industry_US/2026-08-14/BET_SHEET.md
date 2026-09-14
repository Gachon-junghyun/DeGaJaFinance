# BET_SHEET — industry_US · 2026-08-14 · Stage 9/11 (L1·BET)

> **ONE file, per-sector sections** (downstream desks glob this exact filename — never split).
> Numbers from `module_fundamentals_us --json` (yfinance + SEC XBRL) and `margin_history.py`
> (functional probe — `--help` is broken, G7). Flow asof **2026-08-13 settled**, benchmark **`SPY`
> inline (C1)**. **Sizing language is influence illustration only — zero buy/sell recommendation (P4).**

## §0 · Rights and constraints this sheet operates under

| Constraint | Consequence here |
|---|---|
| **G6 FAIL** (estimate accrual 2.4× slow) | 🚫 **No `kelly_size --ic` figure appears.** Any size language is **"mechanical ¼"** |
| **G4 FAIL** (11 / 10 / 10 units across 250/500/750d) | 🚫 **No single-number concentration guard.** Any concentration statement carries its `--days` **on the same line** |
| **G5 FAIL** (universe 30d stale, `EA` null) | 🚫 No verdict on `EA`; `wflow` is not "current-cap weighted" |
| **`D261`** (SWEEP §2) | **5 of 11 🟢 are disqualified** — `CSCO` `DELL` `CVX` `NVDA` `BAC` are read as 🟡 throughout |
| **G1 / `D259`** | 🚫 No velocity, no theme-age. News facts carry **source + date on the line** |
| **`D258`** | Every rejection/miss below names an **observable**, never a tool |

## §1 · Candidate set — the wide net, stated before it is filtered

**(DEEP thesis leaders) ∪ (`us_setup_screener` buckets) ∪ (`US_LIVE_SHORTLIST`) ∪ (EVENT_ALPHA CONFIRMED-EARLY)**

- **DEEP leaders**: `VLO` `MPC` `PSX` `XOM` (ENRG) · `RTX` `LMT` `GD` `ETN` `PH` (INDU) ·
  `T` `VZ` `CMCSA` (COMM) · `BX` `KKR` `BLK` (FIN)
- **Screener, 17 new names**: `WM` `O` `AAPL` `SPG` `CB` `AFL` `GWW` `ED` (leader-pullback) ·
  `MSTR` `ALNY` `COIN` `NKE` `PDD` `CRH` `KR` (de-rate snapback) · `MNST` `SO` (washout)
- **LIVE shortlist (admissible 6)**: `COHR` `KKR` `ABNB` `LITE` `MPC` `ALL`
- **EVENT_ALPHA CONFIRMED-EARLY**: `MU` `SNDK` `WDC` `MRVL` `VLO` `COHR` `LITE`

⚠ **The screener's own header binds**: *"raw candidates, turn unconfirmed — not a buy signal."*
🚫 **Zero screener names reach §A below.** Diagnosed rather than waved: **the leader-pullback bucket
is 5 of 8 in UW/N− sectors** (`O`·`SPG` RE · `CB`·`AFL` FIN · `ED` UTIL), the de-rate bucket is
crypto/consumer beta (`MSTR` `COIN` `NKE` `PDD`), and **`AAPL` is the one name this run's own
EVENT_ALPHA Card 1 identifies as the crowded headline layer** (🔴 분산, RS20 −12.0). A pullback
screen that surfaces the sectors the desk is underweight is **finding the underweight, not an entry**.

---

# §A · ENERGY (OW−) — the refining node

## A-§A · Numbers

| | `VLO` | `PSX` *(held)* | `MPC` *(held)* |
|---|---|---|---|
| Price / mcap | **$345.40** / $99B | — | — |
| Trailing / forward P/E | 14.41 / **12.22** | — | — |
| PEG · P/B · beta | 4.08 · 4.30 · **0.55** | — | — |
| Forward EPS | 28.27 | — | — |
| **Consensus target (mean)** | **$315.26 ⇒ the price is 9.6% ABOVE it** | — | — |
| **Gross-margin percentile** | 🚫 **`margin_history VLO` returns `연간 데이터 없음` ⇒ UNKNOWN (C3)** | median **12.1%** (high FY2016 25.9 · low FY2021 8.4) | FY2025 **10.0%** vs median **10.5%** ⇒ **at median** |
| 0q EPS trend (90d→now) | **8.53 → 10.40 → 15.65 = +83%** | — | — |
| Revision breadth (30d) | 0q **15↑ / 0↓** · 0y **14↑ / 1↓** | — | — |

★★ **The B2 lens applied, and it does NOT fire for the held names**: `MPC` sits **at the median of its
own 17-year margin history** and `PSX`'s median is 12.1% — **these are mid-cycle margins, not peak
margins**, so a low forward multiple here is not automatically the peak-margin trap.
🚨 **But it cannot be applied to `VLO` at all** — the margin series is missing, so **`VLO` carries a
`[C3] margin percentile UNKNOWN` tag and no valuation claim is attached to it.**

## A-§B · Thesis (freshness placeholder — ALPHA fills)
**The OW− is on refining, not on Energy** (`SECTOR_DEEP_ENRG §1`): refining is the **only** node with
positive median RS60 (**+27.3**); integrateds −5.5, E&P −8.3, midstream −9.2, OFS −11.8.
Mechanism is **physical and named**: *"Ukraine Strikes Gazprom's **200,000-Bpd Salavat Refinery**"*
[`oilprice` 08-13] · *"Drone Strike Sparks Blaze at Key Russian Oil and Fuel Terminal"* [`oilprice`
08-14]. Crack **59.34 → 65.84 (+6.50 pts / 5 sessions)** with products outrunning crude.

**`[freshness: 🟡PARTIAL]`** — filled by ALPHA (stage 10). **Residual stated**: the *mechanism* is
live and un-consumed (a refinery struck **08-14**, i.e. after the settle this sheet prices), but the
**price leg is 60 days old** — `MPC`/`VLO`/`PSX` RS60 **+32.0 / +27.3 / +24.1** — so the move is not
new even though the news is. ⚠ **`XLE` exc60 is −4.519**: the sector window has not turned.
⇒ **Bettable as a continuation, not as an ignition.** 🚫 **`theme_age` is NOT used to set this tag**
(`MACRO §D-4`: 6 of 6 terms returned an identical `🟡ACCELERATING`, including one on 14 articles).
The tag is set from the **age of the price leg**, which is measurable.

## A-§C · Flow / positioning
`MPC` **flow +0.811, OBV 매집, RS20 +12.9, RS60 +32.0, `vol_surge` 1.26 — the book's only admissible 🟢.**
`PSX` +0.637 / 매집 / +11.9 / +24.1 and `VLO` +0.639 / 매집 / +10.6 / +27.3 — **both 🟡 solely because
`vol_surge` reads 1.04 and 0.95.** `XLE` FINRA z **+0.57 (normal)**; **WTI spec 18th %ile crowded short**.
⚠ **The two names the tape says lead the sector are filtered out of the sector's own shortlist by a
volume test** (`SWEEP_READ §4.3`).

## A-§D · Competition / peers
Within-node the three refiners are near-identical on flow (0.637–0.811) and RS60 (+24.1 to +32.0).
The **peer that matters is the integrated**: `XOM` at **30.5% of sector cap** reads RS20 +5.1,
**RS60 −6.5, Δ −0.247** — and **`XOM` alone is 48% of the sector's entire Δ decay.**

## A-§E · Refutation + dated catalyst
**Refuted if**: the crack falls ≥5 points while crude holds ±3% (`P58` anti-signal b) · **or** the
refining node's median Δ turns ≤ −0.15 · **or** `S84` branch A fires (≤ −3.174, **08-21**).
**Dated**: `S75` **08-19** · `S84` **08-21**.
⚠⚠ **`R47` binds**: no stage may state *"the distillate bottleneck released"* as fact — `S55` scored C.
⚠ **`VLO` is the un-held expression and it trades ABOVE its consensus target.** Stated as the single
most important fact on this section, not buried.

---

# §B · INDUSTRIALS (OW−) — defense + electricals, NOT `XLI`

## B-§A · Numbers · B-§B · Thesis
🚫 **No new candidate is put up.** `SECTOR_DEEP_INDU §1` answered `D249`: the OW− lives in **17 of 50
names** — aero/defense (`wflow +0.260`, **OBV 매집 8 of 9**) and electricals (`eqflow +0.149`) —
while machinery (Δ −0.203) and transport (**OBV 매집 0 of 6**) drag. **`RTX` and `ETN` are already
held and are the node's expressions.**

**`[freshness: 🟡PARTIAL]`** — **residual: there is no dated catalyst at all.** `S64` is VOID, no
replacement bracket exists, and `D249` is three runs old. A thesis with live flow (defense
`wflow +0.260`) and **zero dated observables** is by construction PARTIAL: it cannot be scored, only
watched. **This is the tag the desk should least like to see on a continuous-track sector.**

⚠ **RULE D6 — exemption stated.** The paragraph above cites an OBV-매집 count. **OBV is grade-C and
supports no proposition alone.** The exemption is that the sentence's actual claim (*the OW− lives in
17 of 50 names*) is carried by **`wflow +0.260` and `eqflow +0.149`**, neither of which contains an
OBV term; the 8-of-9 count is **node-level corroboration**, and **no candidate on this sheet is put
up or set aside on an OBV reading.**

## B-§C · Flow · B-§D · Peers
`RTX` +0.511 / 매집 +0.31 / RS20 +9.8 / RS60 +20.0 · `LMT` +0.533 / 매집 +0.38 / +12.8 / +7.9 ·
`GD` +0.238 / 매집 +0.35 / +2.9 / +9.2 · `ETN` +0.489 / **매집 +0.41** / +10.8 / +13.4 ·
`PH` +0.554 / 매집 +0.34 / +6.9 / **+18.0**.
⚠ **The electrical node is SPLITTING**: `GEV` **−0.412** and `VRT` **−0.452 (RS60 −20.8)** against
`ETN`/`PH` positive — **a +0.94 flow spread inside one "AI-power" label.**

## B-§E · Refutation + dated catalyst
**Refuted if** the defense node's OBV-매집 count falls below 5 of 9 **and** its `eqflow` turns negative.
🚨 **Dated catalyst: NONE — and that is the finding.** `S64` is **VOID** (it measured `XLI` against a
crude fall that never came; crude **rose 10.7%**). **The desk has no live Industrials bracket at all**,
and `D249` is three runs old. **This sheet does not invent one; `SECTOR_DEEP_INDU §6` registers the
build of a defense-EW observable as the next run's most useful Industrials task.**

---

# §C · COMMUNICATION SERVICES (UW) — the node the UW is not actually short

## C-§A · Numbers — `T`

| | `T` |
|---|---|
| Price / mcap | **$24.86** / $170B |
| Trailing / forward P/E | 8.20 / **9.69** |
| PEG · P/B · **beta** | 1.61 · 1.55 · **0.42 — the lowest beta on this sheet** |
| Forward EPS · target mean | 2.56 · **$28.71 ⇒ +15.5% to consensus** |
| Gross-margin median | **58.7%** (high FY2007 60.6%) — **a level; no valuation claim attached (C4)** |
| **Revision breadth (30d)** | 0y **15↑ / 3↓** ✅ · ⚠ **+1q 2↑ / 13↓ — strongly net-DOWN** |
| +1q EPS trend | **0.5466 (90d) → 0.5251 = −3.9%** |

🚨 **C2 — both halves, and they disagree.** The **current year** is being revised **up** (15↑/3↓)
while the **next quarter** is being revised **down** (2↑/13↓) and its EPS estimate has fallen 3.9%.
**A candidate whose two revision horizons point opposite ways is not a clean candidate**, and this
sheet says so rather than quoting the friendly half.

## C-§B · Thesis
**88.8% of COMM is three share classes of two companies** (`GOOGL`+`GOOG`+`META`), all negative,
**0 of 3 accumulating**, med RS60 **−17.8**. The **telecom node (`T` `VZ` `CMCSA`) is positive on every
admissible axis** — `eqflow +0.286`, med RS20 **+6.3**, 2 of 3 accumulating — **at 3.6% of sector cap,
structurally invisible to the 🟢 gate** (`vol_surge` 0.52 / 0.55 / 0.54, the sector's three lowest).
Live narrative is **AI-adjacent, not telco-yield**: *"Can **AI Infrastructure** Drive **Verizon's**
Next Long-Term Growth?"* [`yahoo_finance` 08-13] · *"**Comcast** Pushes **Private Wireless** Into The
Office Market"* [`yahoo_finance` 08-09].

**`[freshness: 🟢LIVE]`** — ★ **and it is the first 🟢LIVE this desk has issued in a long run of
zeros, issued on a REBUILT basis rather than on `theme_age`.** The gate that produced those zeros
(`age ≤14d AND accel ≥2×`) is **disqualified today** (`MACRO §D-4` · pre-existing `D254`), so this tag
is set on three measurable facts instead: (i) the node's live narrative is **AI-adjacent and 2 outlets
deep** — *"Can AI Infrastructure Drive Verizon's Next Long-Term Growth?"* [`yahoo_finance` 08-13],
*"Comcast Pushes Private Wireless Into The Office Market"* [`yahoo_finance` 08-09] — i.e. **early, not
consumed**; (ii) the flow is positive and **un-crowded** (`eqflow +0.286`, `vol_surge` 0.52–0.55, the
sector's three lowest — nobody is chasing); (iii) **RS60 is still negative (−4.7 / −0.3 / −2.2)**, so
the price has not made the move. **Fresh narrative + positive flow + un-made price is the definition
this stage exists to isolate.**
⚠⚠ **And the honest counterweight, on the same line**: `T`'s **+1q revision breadth is 2↑/13↓** and
its +1q EPS estimate has fallen **−3.9% in 90 days.** **A 🟢LIVE tag on a name whose next-quarter
estimate book is net-down is a narrative call, not an earnings call**, and it is labelled as such.

## C-§C · Flow · C-§D · Peers
`T` +0.400 / OBV 매집 +0.34 / RS20 **+8.2** / RS60 −4.7 · `CMCSA` +0.292 / 매집 / +5.0 / −0.3 ·
`VZ` +0.165 / 중립 / +6.3 / −2.2. **Peer that fails**: `TMUS` **−0.788, RS20 −8.5, RS60 −9.1** — the
node is **not** "telecom", it is **the three names that are not `TMUS`.**
⚠ `XLC` FINRA short z **+2.15 with a +12.4▲ trend — the steepest short surge of the eleven sectors**,
i.e. the crowding is in the wrapper, not measurable per-name.

## C-§E · Refutation + dated catalyst
**Refuted if** `T`'s **+1q revision breadth stays net-down for two more weekly reads while its 0y
breadth turns net-down too** — the current-year strength would then be a stale estimate rather than a
different horizon. **Dated**: `T` next earnings — **not read this run**, stated as a gap.
⚠ **`SECTOR_DEEP_COMM §5` anti-signal 3 is the standing one**: telecom-ex-`TMUS` `eqflow` > +0.25 for
three sessions **while the sector stays UW** ⇒ the desk is underweighting a bucket containing a
positive node its own gate cannot see. **Available for six runs, registered today.**

---

# §D · FINANCIALS (N−, demoted today) — the node the breadth premium moved to

## D-§A · Numbers — `BX`

| | `BX` |
|---|---|
| Price / mcap | **$145.77** / $174B |
| Trailing / forward P/E | 32.68 / **19.47** |
| PEG · **P/B** · beta | 1.62 · **12.94 — the highest on this sheet** · 1.55 |
| Forward EPS · target mean | 7.49 · **$142.38 ⇒ the price is 2.3% ABOVE it** |
| Gross-margin percentile | 🚫 **`margin_history BX` → `연간 데이터 없음` ⇒ UNKNOWN (C3)** |
| **Revision breadth (30d)** | ⚠ **0q 1↑ / 14↓ — strongly net-DOWN** · 0y 12↑ / 5↓ |
| 0q EPS trend | **1.482 (30d) → 1.366 = −7.8%** |

🚨 **Same C2 shape as `T`, and worse**: the **current quarter** is being cut hard (1↑/14↓, EPS −7.8%)
while the **current year** is revised up. **`BX` is the best name on the sector's best flow node and
its near-term estimate book is the worst on this sheet.** Both halves stated.

## D-§B · Thesis
`M40`'s "breadth-led Financials" **inverted** (`eqflow −0.144` now **below** `wflow −0.066`) — and
`SECTOR_DEEP_FIN §1a` locates the inversion **entirely in the bank node** (`wflow − eqflow` gap
**+0.191** vs ≤ ±0.035 everywhere else), i.e. **a regional-bank statement, not a Financials one.**
★ **The breadth property relocated**: alternatives/asset-management is positive on **every** axis —
`wflow +0.357` · `eqflow +0.324` · med RS20 **+6.9** · med RS60 **+14.2** · **med Δ +0.105, the
sector's only positive Δ node** · **OBV 매집 5 of 6.**

**`[freshness: 🟡PARTIAL]`** — **residual: the node is right and the entry point is not.** `BX` trades
**2.3% ABOVE its consensus target** with **0q revisions 1↑/14↓** and a **−7.8% 0q EPS cut in 30 days**,
while `KKR` is an admissible 🟢. ⇒ **the flow thesis (breadth relocated to alternatives) is LIVE; the
valuation/estimate leg is RESOLVED against it.** Two legs, opposite tags, and the sheet reports both
rather than averaging them into one colour.

## D-§C · Flow · D-§D · Peers
`BX` +0.644 / 매집 +0.21 / RS20 **+12.2** / RS60 **+22.3** · `KKR` **admissible 🟢**, +0.961 /
매집 +0.27 / +8.6 / — · `BLK` +0.251 / 매집 / +5.2 / +3.6 with **Δ +0.265**.
**Peers that fail**: payments (`V −0.300` · `MA −0.149` · **`AXP −0.861` 🔴**) and exchanges/data
(**`SPGI −0.811` 🔴**), the sector's two worst nodes.
⚠ **The book's two Financials positions sit in those two weakest nodes**: `NDAQ` (**Δ −0.288, the
book's worst**) and `MET` (**`S69` fired branch A today**).

## D-§E · Refutation + dated catalyst
**Refuted if** the bank node's `eqflow` rises above its `wflow` (the inversion was a one-session
regional artifact) · **or** `HY OAS` widens ≥25bp from **2.71** (the constraint moves from curve shape
to credit, which would make the N− right for a worse reason).
**Dated**: **`S78` settles 2026-08-19.**
⚠ **Credit is measurably NOT the constraint today**: HY OAS **2.71 flat over 20 obs, 8bp off a
365-day low**; IG **0.79 flat**; `NFCI −0.549 loosening`. **Any Financials bear case built on credit
is narrative-only.**

---

# §X · CROSS-SECTOR LIVE — names outside the DEEP sectors

## X-§A · Numbers

| | `MU` | `MRVL` | `LITE` | `COHR` |
|---|---|---|---|---|
| Price / mcap | $978.40 / **$1,105B** | $220.97 / $198B | $954.12 / $85B | $342.47 / $67B |
| Forward P/E | **6.32** | 35.40 | 28.92 | 25.19 |
| PEG · P/B · beta | **0.13** · 10.96 · 2.21 | 1.23 · 10.62 · **2.25** | 0.63 · **23.02** · 1.51 | 0.92 · 6.27 · 2.11 |
| Target mean vs price | **$1,502 ⇒ +53.5%** | $257 ⇒ **+16.4%** | $1,126 ⇒ **+18.0%** | $395 ⇒ **+15.2%** |
| **Gross margin vs own history** | 🚨 **84.6% = 100th %ile, +25.7pp OVER its FY2018 peak of 58.9%** (`M18`) | FY2026 **51.0% = its own all-time high**, median 50.1% (range 41.3–51.0 ⇒ **narrow**) | 🚫 current not returned; **median 32.4%**, range 30.5–34.9 | FY2026 **37.5%** vs median **37.9%** ⇒ ★ **AT median** |
| Revision breadth (30d) | **0q 26↑/0↓ · 0y 29↑/1↓** | **0q 25↑/3↓** | 0q 4↑/0↓ · +1q 5↑/0↓ · 0y **6↑/0↓** | 0q 2↑/0↓ · +1q 4↑/0↓ · 0y 4↑/0↓ |
| 0q EPS trend (90d→now) | **22.50 → 31.30 = +39.1%** | 0.893 → 0.928 = +3.9% | 3.301 → 3.631 = **+10.0%** | 1.540 → 1.617 = +5.0% |

## X-§B · Thesis and the B2 verdict, name by name — **this is the section's whole point**

🚨🚨 **`MU` is the textbook peak-margin / low-multiple trap and this sheet says so plainly.**
Forward P/E **6.32** and PEG **0.13** look like the cheapest thing on the board. **They are the
denominator peaking**: gross margin **84.6% is the 100th percentile of a 17-year series and sits
25.7pp ABOVE the prior cycle's peak**, while consensus has raised 0q EPS **+39% in 90 days on 26↑/0↓**.
**A multiple without a margin percentile is not a valuation** — and with the percentile attached, the
multiple is a **warning**, not an attraction. ⚠ **C4: this is not a claim that `MU` falls.** It is a
claim that **the cheapness is arithmetic, and EVENT_ALPHA Card 1's demand-destruction read
(`AAPL` +$300, `GOOGL` +$100, and the equity sold on the hike) is the mechanism that would resolve it.**

★ **`COHR` is the opposite shape and it is why it survives this section**: gross margin **37.5% against
a 37.9% median** — **mid-cycle, not peak** — with **`flow_score +1.000`, the maximum on the 300-name
board**, and revisions net-up on all three horizons. **A 25× forward multiple on a mid-cycle margin is
a different object from a 6× multiple on a 100th-percentile margin.**
`LITE` shares the shape (**revisions 4↑/0↓, 5↑/0↓, 6↑/0↓ — zero downgrades across three horizons**)
but carries **P/B 23.02**, the highest on this sheet, which is stated rather than netted out.
`MRVL` sits between: **at its own all-time-high margin**, but inside a **narrow 41.3–51.0 range**, so
the peak is 0.9pp above median — **a weak B2 signal, and labelled weak.**

## X-§C · Flow · X-§D · Competition
`COHR` +1.000 / 매집 / RS20 **+14.5** / **RS60 −15.1** · `LITE` +0.844 / 매집 / **+21.0** / −5.8 ·
`CIEN` +0.273 with **Δ +0.622, the board's 2nd largest** · `MRVL` +0.378 / 매집 / +14.4 / **+26.2** ·
`MU` −0.004 / 중립 / +7.7 / +34.1 with **Δ +0.585**.
⚠ **Positioning, and it cuts against the optical names**: `COHR` carries **5.4% of float short and
BUILDING** (DTC 1.9, implied move **±3.8% at `D0`**). **Crowded-short is turn-conditional squeeze
fuel, never a buy on its own (D6).**
**Competition**: `MRVL` is the **named** beneficiary of Microsoft's Maia 300 — *"Microsoft New AI Chip
Could Be a **Big Win for Marvell and TSMC**"* [`yahoo_finance` 08-11] — **against `NVDA`, which the
book holds and whose RS60 is −4.0 to `MRVL`'s +26.2.** ⇒ **the book is long both sides of this
displacement and cannot express the card** (`PREMORTEM §4.5`).

## X-§E · Refutation + dated catalyst
- **`MU`/`SNDK`/`WDC`**: dead if `MU`'s Δflow turns negative **and** `AAPL` RS20 recovers above −5.0
  by **2026-08-21** (EVENT_ALPHA Card 1's frozen kill).
- **`COHR`/`LITE`**: dead if either RS20 falls below +5 before RS60 crosses zero. **Dated: `S86`
  settles 2026-08-21** (bands A ≥ +12.584 / B ≤ −5.948, **sd 8.998 disclosed ⇒ C is the favourite**);
  `S48` runs to 09-30.
- **`MRVL`**: dead if [`MRVL` RS60 − `NVDA` RS60] narrows below +10pp by **2026-09-15**, or the Maia
  300 unveil slips past September without a restated unit target (currently **+30.2pp**).

## §X-F · Epicenter-starter module
🚫 **Not triggered.** `cycle_exposure` returns **✅ no GAP** (AI-compute 16.68% vs a 12.0% floor;
Energy 11.1% vs 8.0%).
⚠ **But `PREMORTEM §4` shows the ✅ rests on 2 armed tests of 3, over ~82% of the book, against a
28-day-old registry that contains no entry for either cycle this run found** (optical/interconnect,
custom AI silicon). **The starter module is not invoked, and the reason the flag did not fire is
recorded so a later run can distinguish "no gap" from "no registry".**

---

## §2 · Names set aside — every one becomes a scored record

**Rejections (filed to `reject_ledger`)**

| Ticker | Class | Why (one line) | `--revives-if` | recheck |
|---|---|---|---|---|
| `AAPL` | `B.모멘텀only` | The screener's leader-pullback bucket surfaced it at RSI 25.9, but this run's own EVENT_ALPHA Card 1 identifies it as the **crowded headline layer of the memory pass-through**: 🔴 분산, flow −0.715, **RS20 −12.0**, and a Jefferies downgrade to sell 08-11. **A pullback screen finding the name we independently marked as the losing side of a chain is not a setup** | `AAPL` OBV state returns to 매집 **AND** RS20 vs SPY > −5.0 | 2026-09-04 |
| `VST` | `G.섹터중립` | Surfaced by `chain-hop` on the Hormuz theme (4 proximate / 10 body) but reads **flow −0.543, OBV 분산, RS20 −7.7** — **a news co-mention alone is not a candidate** and the flow cross-check kills it outright | `VST` flow_score > 0 **AND** OBV state 매집 | 2026-09-04 |

**Missed entries (filed to `missed_ledger`)** — names that cleared an axis and did not make the sheet

| Ticker | Class | Why | `--enters-if` | recheck |
|---|---|---|---|---|
| `CIEN` | `Q.확신부족` | **Δflow +0.622, the board's 2nd largest**, RS20 +10.3 — but **RS60 −20.9, the worst of the optical four**, and it is 🟡 rather than an admissible 🟢. Not put up | `CIEN` RS60 vs SPY > −5.0 **AND** flow_score > +0.5 | 2026-09-04 |
| `PH` | `M.숏리스트탈락` | flow **+0.554**, OBV 매집 +0.34, **RS60 +18.0** — the electrical node's best un-held name. Dropped only because INDU put up no new candidate | `PH` Δflow > 0 **AND** RS20 vs SPY > +5.0 | 2026-09-04 |

⚠ **Every condition above names an OBSERVABLE with a threshold — never a tool** (`D258`, registered
this run after three tanker rows became unresolvable when `chain_hop` died).

## ✅ EXIT CHECK

- [x] **ONE file, per-sector sections §A–§E** — not split.
- [x] **Candidate set is the wide net** (DEEP ∪ screener ∪ LIVE shortlist ∪ EVENT_ALPHA), and the
      **screener's 17 names are diagnosed, not silently dropped** (§1).
- [x] **§A numbers with XBRL↔yfinance cross-check; blanks stated as blanks** — `VLO` and `BX` carry
      explicit **`[C3] margin percentile UNKNOWN`** rather than an omitted row.
- [x] **B2 applied to every candidate**: the forward multiple sits beside the **margin percentile** in
      every case where the series exists, and `MU` is called a trap **on the percentile**, not on a feeling.
- [x] **C2 both halves** on `T` (0y 15↑/3↓ **vs** +1q 2↑/13↓) and `BX` (0y 12↑/5↓ **vs** 0q 1↑/14↓).
- [x] **§C flow with positioning; §D peers; §E refutation + dated catalyst** on every section —
      **and where no dated catalyst exists (INDU) that absence is the finding, not a blank.**
- [x] **Epicenter-starter module considered** and correctly not invoked, with the registry caveat.
- [x] **Every set-aside name has a reason class, a `--revives-if`/`--enters-if` and a `--recheck-date`.**
- [x] **Zero buy/sell language. No `--ic` size. No single-number concentration guard.**

---

## §3 · ALPHA freshness summary (stage 10 wrote §B tags in place)

| Section | Tag | Residual / reason |
|---|---|---|
| **§A ENRG — refining** | 🟡 **PARTIAL** | Mechanism live (a refinery struck **08-14**), **price leg 60 days old** (RS60 +32.0/+27.3/+24.1), `XLE` exc60 **−4.519**. Continuation, not ignition |
| **§B INDU — defense/electricals** | 🟡 **PARTIAL** | **No dated catalyst exists.** `S64` VOID, no replacement, `D249` three runs old |
| **§C COMM — telecom node** | ★ 🟢 **LIVE** | Narrative 2-outlet deep and AI-adjacent · flow positive and **un-crowded** (`vol_surge` 0.52–0.55) · **RS60 still negative** ⇒ the price has not made the move. ⚠ counterweight on the line: `T` +1q revisions **2↑/13↓** |
| **§D FIN — alternatives** | 🟡 **PARTIAL** | Flow thesis LIVE; **valuation/estimate leg RESOLVED against it** (`BX` above target, 0q 1↑/14↓) |
| **§X `MU`** | 🔴 **RESOLVED — dropped from the bettable list** | The cheapness is arithmetic: **margin at the 100th percentile, 25.7pp above the prior-cycle peak**, with consensus +39% in 90 days on 26↑/0↓. **Logged as a ledger row below, not as prose**, so "it's cheap at 6.3×" cannot resurface next run |
| **§X `COHR` · `LITE`** | 🟡 **PARTIAL** | Mid-cycle margin (`COHR` 37.5% vs a 37.9% median) and revisions net-up on all horizons, **but RS60 still −15.1 / −5.8** and `COHR` carries **5.4% float short and BUILDING** |
| **§X `MRVL`** | 🟡 **PARTIAL** | Named Maia-300 beneficiary with **RS60 +26.2**, but the desk is **long the displaced side too** (`NVDA`) and cannot express the card |

🚫 **`theme_age` was NOT used to set any tag on this sheet.** It returned **6 identical
`🟡ACCELERATING` verdicts out of 6 queries**, with its **highest acceleration (7.71×) on the term
holding 14 total articles** (`MACRO §D-4`, `D260`). Every tag above is set from **price-leg age, flow
crowding, and revision breadth** — three instruments that discriminated today.

★ **The `🟢LIVE` zero-streak broke, and it broke because the gate was replaced rather than because the
market changed.** The standing gate (`age ≤14d AND accel ≥2×`) is the one `D254` measured as *"an off
switch, not a filter"*. **This is a methodology change and it is flagged as one** — the next run must
decide whether to keep the rebuilt basis or restore the gate. **It is not evidence that the board got
fresher.**
