# MACRO_REPORT — industry_US · 2026-08-31 (Mon) · Stage 3 / L1·MACRO

> Run clock **KST 22:09–23:0x = ET 09:09–10:0x, Monday, PRE-OPEN → the open crossed mid-stage.**
> Last **completed** US session: **Fri 2026-08-28**. Every price statement below is about 08-28 or
> earlier unless it is explicitly quarantined as a pre-open indication.
> `--scope foreign` on every news call. IDs from `module_evidence next-id`
> (`P118`–`P120` · `M1133`–`M1144` · `D431`–`D433`; highest before this run `P117` · `M1132`
> issued this run in HANDOVER · `D430` issued this run in HANDOVER) — **not hand-grepped**.

---

## §0 · Rights removed before any number below is read

Inherited from `preflight/PREFLIGHT.md` (this run) and re-stated because they bind this stage:

1. 🚫 **The primary `SECTOR_FLOW_US.json` is empty** (`scored=0`, 2nd consecutive run). Every flow
   number below comes from **`SECTOR_FLOW_US_REPAIRED.json`** and carries the label `repaired sweep`.
2. 🚫 **No `wflow`-based promotion or demotion of IT, Energy or Consumer Discretionary** — one name
   owns each sign (NVDA 19.4% · XOM 30.5% · AMZN 40.2%).
3. 🚫 **No news-velocity or theme-freshness figure sourced from the sweep** (15.72% coverage).
   Direct queries only, labelled `direct query, outside the sweep window`.
4. 🚫 **No 08-28 close from the daily endpoint, the book, `status` or `pulse`** — those print 08-27.
   The 08-28 tape is available only as a **5m proxy (err ≤0.05%)**.
5. 🚫 **No claim about the 08-31 session.** It had not opened when this stage's data was pulled, and
   §A-6's pre-open numbers are quarantined, not cited.
6. 🚫 **No US chart shape verdict** (`module_chart` 0/3).

---

## §A · Instruments

### A-0 · ★★ The macro axis produced **no new data today**; the news axis produced a regime event

This has to be said first, because it determines what this report can honestly be.

| channel | newest observation | new since the 08-30 run? |
|---|---|---|
| FRED H.15 (`DGS2/5/10/30`, `DFF`) | **2026-08-27** | **no** |
| FRED credit (`hy_oas`, `ig_oas`) | **2026-08-27** | **no** |
| `VIXCLS` | **2026-08-27** | **no** |
| `DTWEXBGS` | **2026-08-21** (**10 days**) | **no** |
| `DCOILBRENTEU` | **2026-08-25** (**6 days**) | **no** |
| CFTC COT | week to **2026-08-25** | **no** (next print Fri 09-04) |
| Equity daily closes | **2026-08-27** settled / 08-28 by proxy | **no** |
| **Foreign news** | **2026-08-31, 1,944 articles / 344 market events** | ★ **YES — and it carries a military escalation** |

⇒ **Every `[FRED]` number in this report is identical to the 08-30 run's.** Re-deriving the same
propositions from the same numbers in fresher-sounding language would be the failure this desk logs
as re-discovery. **The new information in this run is entirely in §B**, and §C's propositions are
written against it.

### A-1 · FRED primaries `[FRED]` — each with its own staleness

| series | asof | value | 365d %ile | note |
|---|---|---:|---:|---|
| `DFF` fed funds | 08-27 | **3.63** | **9.0** | the Fed has cut 70 bp over the year (4.33 → 3.63) |
| `DGS2` | 08-27 | **4.20** | **91.2** | `P115`'s observable (A ≥4.32 / B ≤4.12) |
| `DGS5` | 08-27 | 4.38 | 94.1 | |
| `DGS10` | 08-27 | **4.67** | **93.0** | |
| `DGS30` | 08-27 | **5.19** | **93.4** | `S120` needs this **and** `T10YIE` on 08-28 |
| `DFII10` real 10y | 08-27 | **2.34** | **89.0** | |
| `T10YIE` breakeven | **08-28** | **2.31** | **45.6** | ★ the only H.15-family series carrying 08-28 |
| `VIXCLS` | 08-27 | 14.51 | 3.9 | |
| `BAMLH0A0HYM2` HY OAS | 08-27 | **2.63** | **0.0** | at its 365-day **low** (range 2.63–3.46) |
| `BAMLC0A0CM` IG OAS | 08-27 | 0.79 | 45.3 | `S111` A ≥0.85 / B ≤0.77 |
| `NFCI` | **08-21** | −0.566 | **0.0** | weekly; at its own low |
| `DTWEXBGS` | **08-21** | 118.06 | 8.2 | **10 days stale — `D333`, 13th reproduction** |
| `SOFR` | 08-28 | 3.65 | 34.8 | |
| `RRPONTSYD` | 08-28 | 0.175 | 3.7 | |
| `SP500` | **08-28** | **7,711.76** | — | ★ carries 08-28 (see A-2) |
| `NASDAQCOM` | **08-28** | **26,402.42** | — | ★ carries 08-28 |
| CPI / core CPI / U-3 / M2 | **2026-07** (monthly, ~1-month lag) | 332.813 / 336.789 / 4.1% / 23,218 | — | July CPI **+3.30% YoY / +0.07% MoM**, core **+2.47% YoY / +0.22% MoM** ⇒ headline runs **83 bp above core** (`C2`: both halves quoted) |

**Curve, `[FRED]` 08-27**: 2s10s **+0.47 = 20.5th %ile** · 10s30s **+0.52 = 16.5th** · 5s30s
**+0.81 = 14.7th** · **10y − fed funds +1.04 = 93.0th**. ⇒ a **level/term-premium repricing against
policy**, not a steepening — the shape is flat at the long end and wide against the policy rate.
`real_10y` **2.34 (89th)** is quoted with `breakeven_10y` **2.31 (45.6th)**: the level is a **real**
phenomenon, not an inflation-expectation one.

★ **`M1133` [measured] — FRED's staleness is per-series, not per-release, and the desk has been
assuming otherwise.** On one pull at 22:2x KST: `SP500` and `NASDAQCOM` carry **08-28**; `T10YIE`
carries **08-28**; `DGS10`/`DGS30`/`DFII10` stop at **08-27**; `DCOILBRENTEU` stops at **08-25**.
`T10YIE` is arithmetically `DGS10 − DFII10`, so **a derived series is published for a date on which
neither of its constituents is** — the upstream values exist. ⇒ **a row requiring two FRED series on
one date can be blocked indefinitely by whichever leg publishes slowest**, which is exactly `S120`'s
state for a second run. Registered as **`D431`**.

### A-2 · Credit — the axis this stage must cite, and it still refuses the stress story

`hy_oas` **2.63 = the 0.0th percentile of its year** (i.e. its own 365-day low) · `ig_oas` 0.79
(45.3rd) · `NFCI` **−0.566 = 0.0th** (also its own low, 08-21). **VIX 14.51 = 3.9th.**

⇒ **Any "rates are breaking something" sentence in this run is `narrative-only` and is labelled so.**
Four separate funding/risk instruments sit at or within 4 percentiles of their **easiest** readings of
the year, on the same date the 10y sits at the 93rd and the real 10y at the 89th. **That joint state
is `P116`'s registered object and it is unchanged today** — no new credit observation exists.

⚠ **This is the third consecutive run in which the equity tape and the news flow tell a tightening
story while the credit instruments refuse it.** Recorded as a standing disagreement, not resolved.

### A-3 · Positioning — `us_flow --cot`, CFTC speculative net, 1-year percentile

**Unchanged from the 08-30 run** (same Tuesday-08-25 print; next release Fri 09-04). Context, not a
trigger — 3–4 day lag by construction.

| instrument | net spec | wk Δ | 1y %ile | read |
|---|---:|---:|---:|---|
| **Copper** | +85,266 | +5,518▲ | **100** | 🟢 crowded long |
| Gold | +243,334 | +21,145▲ | 66 | neutral — **not** to be netted with copper |
| S&P 500 e-mini | −67,994 | **−57,434▼** | 65 | neutral level, extreme weekly change |
| Nasdaq-100 | +11,127 | **+23,193▲** | 59 | ★ moved **opposite** to the S&P leg in one week |
| Russell 2000 | −16,118 | −412▼ | **15** | 🔴 crowded short |
| Nat Gas | −197,932 | +5,571▲ | **2** | 🔴 crowded short |
| UST 10Y | −838,975 | +107,986▲ | 22 | near crowded-short |
| UST 2Y | −861,296 | +66,041▲ | 72 | |
| USD Index | +18,682 | −397▼ | 74 | |
| WTI | +31,099 | +1,935▲ | 43 | ⚠ **43rd percentile — the war premium is NOT a crowded speculative long** |

★ **`M1134` [measured] — the single most useful positioning line for today's event is WTI at the
43rd percentile.** The Iran escalation (§B-1) lands on speculative oil positioning that is **mid-range,
not crowded**. That is the opposite of the copper setup (`C24`), and it means an oil move today has
**room** rather than fuel-exhaustion — stated as *context*, explicitly not as a direction (P4).

**FINRA daily short-volume `z` (08-28 file), book + two watch names:**

| ticker | short% | 20d base | z | 5v5 | read |
|---|---:|---:|---:|---:|---|
| **SLB** | 72.5% | 46.7% | **+2.40** | **+9.0▲** | 🔴 **short-vol spike, the board's extreme** |
| ANET | 55.4% | 45.8% | +1.31 | **+11.0▲** | pressure building on a held name |
| MET | 57.7% | 43.7% | +0.98 | −17.1▼ | |
| NVDA | 39.9% | 36.5% | +0.88 | +2.0▲ | |
| RTX | 48.3% | 41.7% | +0.75 | +1.5▲ | |
| PSX | 56.5% | 50.9% | +0.63 | −4.4▼ | |
| AVGO | 36.8% | 34.5% | +0.26 | −5.7▼ | |
| NUE | 47.4% | 47.5% | −0.01 | −4.4▼ | |
| LLY | 45.6% | 42.6% | +0.54 | −2.7▼ | |
| HPE | 30.8% | 47.0% | −1.44 | −3.7▼ | |
| **MPC** | 45.5% | 56.6% | **−1.85** | +6.8▲ | 🟢 short covering |
| **ETN** | 40.9% | 56.0% | **−1.98** | +8.0▲ | 🟢 short covering |
| **NDAQ** | 16.8% | 44.2% | **−2.37** | −18.2▼ | 🟢 |
| **XOM** | 17.0% | 47.9% | **−3.71** | −14.8▼ | 🟢 the board's extreme covering |

★ **`M1135` [measured] — `XOM` short volume collapsed to 17.0% against a 47.9% 20-day base (z −3.71)
on 08-28, the session before the US resumed strikes on Iran.** `XOM` is also the name that **owns
Energy's negative sign** in the repaired sweep (30.5% of the bucket; ex-`XOM` the sector is **+0.074**
vs a headline **−0.097**). ⚠ **This is a conjunction, not a causal claim** — FINRA short volume
includes market-maker hedging and is not directional on its own (`D6`-class caution).

### A-4 · The tape, settled 2026-08-28 (**5m-proxy close, err ≤0.05%**)

Repaired sweep, asof **08-28**, 299/299 scored, 3-axis (`nonews`), **Δ vs the 08-27 snapshot**
(299/299 common names, same mode):

| sector | wflow | **Δ vs 08-27** | eqflow | 🟢/n | red | top-1 | ex-top1 | sign flips? |
|---|---:|---:|---:|---:|---:|---|---:|---|
| **Materials** | **+0.225** | **+0.197** | +0.164 | 0/12 | 0 | LIN 24.7% | +0.233 | no |
| Information Technology | +0.033 | +0.025 | −0.034 | 3/56 | 13 | NVDA 19.4% | **−0.016** | **🚨 yes** |
| Health Care | +0.021 | +0.047 | **+0.135** | 1/32 | 2 | LLY 19.4% | **+0.095** | no |
| Financials | −0.072 | **+0.073** | −0.089 | 0/47 | 5 | BRK-B 13.9% | −0.020 | no |
| Energy | −0.097 | −0.046 | **+0.005** | 0/16 | 3 | XOM 30.5% | **+0.074** | **🚨 yes** |
| Consumer Discretionary | −0.262 | −0.126 | −0.247 | 0/28 | 12 | AMZN 40.2% | **+0.056** | **🚨 yes** |
| Consumer Staples | −0.264 | +0.080 | −0.187 | 0/19 | 4 | WMT 28.9% | −0.130 | no |
| Industrials | −0.317 | −0.129 | −0.291 | 0/50 | 17 | CAT 8.7% | −0.291 | no |
| Real Estate | −0.338 | +0.078 | −0.333 | 0/12 | 4 | WELL 16.9% | −0.415 | no |
| Communication Services | −0.422 | −0.162 | **+0.080** | 0/12 | 3 | GOOGL 38.3% | −0.338 | no |
| **Utilities** | **−0.549** | −0.025 | −0.524 | 0/15 | 10 | NEE 17.7% | −0.525 | no |

**Universe**: cap-weighted flow **−0.136** · **4 green / 73 red of 299** · breadth **1.3%**.
Greens: `CRM` +1.000 · `A` +0.906 · `MSTR` +0.883 · `INTU` +0.850.
Δ movers (**repaired sweep, 08-27 → 08-28, 3-axis nonews**): up `CTVA` +0.77 · `AAPL` +0.69 ·
`LYV` +0.63 · `CBRE` +0.52 · `SYK`/`MLM`/`ADM` +0.47; down `FTNT` −0.59 · `PYPL` −0.55 ·
`MPWR` −0.48 · `KLAC` −0.45 · `CIEN` −0.42 · `JBL` −0.40 · **`ETN` −0.39** (held).

**08-28 index/sector proxy tape** (last 5m bar vs 08-27 official close): risk-off **NVDA −4.58% ·
HPE −3.90% · ETN −3.21% · ANET −2.87% · XLK −1.55% · XLU −1.09% · XLI −0.95% · AVGO −0.77%** against
risk-on **PSX +1.76% · MPC +1.47% · XLC +1.41% · XLY +1.15% · XLE +0.59%**, with **SPY −0.22%**.
Cross-provider (`D5`): FRED `SP500` **−0.2487%** vs `SPY` proxy **−0.2231%** — **2.6 bp apart**.

### A-5 · ★★ `M1136` — the Brent front-month **rolled on 08-31**, and two ARMED rows are keyed to it

Measured, `yfinance`, `auto_adjust=False`:

| date | `BZ=F` | `CL=F` | **Brent − WTI** |
|---|---:|---:|---:|
| 2026-08-25 | 88.58 | 82.36 | 6.22 |
| 2026-08-26 | 87.84 | 82.23 | 5.61 |
| 2026-08-27 | 89.70 | 83.53 | 6.17 |
| **2026-08-28** | **89.31** | **83.40** | **5.91** |
| **2026-08-31 (live, pre-open)** | **88.26** | **85.65** | **2.61** |

The spread moved **−3.30 in one session** against a 60-day range of **2.40 → 8.50** (mean 5.09).
A physical Brent–WTI relationship does not move that far in a session while WTI rises 2.7% on a
military escalation; **the signature is a front-month contract roll in `BZ=F`**, and the 60-day
minimum of 2.40 shows the same artifact at the prior roll.

⇒ 🚨 **`P107` (branch B: `BZ=F` settled close ≥ 96.00 through 09-08) and `P117` (A ≤85.00 / B ≥95.00
through 09-18) are both keyed to `BZ=F`, and their thresholds were set against the *previous*
contract.** A −3.3 level shift is **~48% of `P117`'s entire lower band** (88.10 → 85.00 = 3.10),
so **branch A has moved materially closer for a reason that is not price.**
- 🚫 **Neither row is re-frozen** (`D242`) — no threshold is improvised and no source is substituted.
- ⚠ **The cross-provider tie-break `P117` registered cannot be run today**: `DCOILBRENTEU` `[FRED]`
  ends **2026-08-25**, six days back (A-1). The leg that was designed to arbitrate is itself stale.
- ⇒ **`D432` registered**: *a row whose observable is a **front-month futures contract** names the
  roll convention at registration, or uses a roll-immune series (`DCOILBRENTEU`/`DCOILWTICO` spot).*
  This is `D413`'s sibling — that one was about two providers disagreeing about one barrel; this one
  is about **one provider's series meaning a different barrel from one day to the next.**
- ★ This is why `P118` below is registered on **`DCOILWTICO` `[FRED]` spot**, not on a future.

### A-6 · 🚫 QUARANTINE — pre-open indications, **not citable, recorded so the absence is not silent**

Pulled at ET 09:1x, i.e. before/at the open. These rows are **not settled closes**, the 08-28 row is
**missing entirely** for every ETF below (the ghost), and `PREFLIGHT` bars any 08-31 tape claim.
They appear here **only** so that a later run can see they were looked at, and **no proposition,
matrix line or verdict in this report uses them**:

`XLE` 64.03 · `XLU` 41.92 · `XLRE` 43.99 · `SMH` 555.66 · `RSP` 219.64 · `SPY` 766.06 · `^VIX` 15.30 ·
`^TNX` 4.746 · `DX-Y.NYB` 99.543 · `JPY=X` 159.83 · `HG=F` 6.72 · `GC=F` 4,492.2 · `NG=F` 2.905.
⚠ This is the **`D401`/`M1045` shape** — a live intraday print wearing a settled-date label. It is
labelled here rather than absorbed.

---

## §B · Narrative — events, trajectories, buckets, blind spot

### B-1 · Events — `brief --date 2026-08-31 --body 2 --scope foreign`, `embed sync` run first

**Denominator, stated**: **1,944 articles → 717 clusters → 344 market events (2+ outlets)** ·
head (≥5 outlets) **33** · body (2–4) **311** · **tail 0** · `single_source` **15 shown of 373**
(`min_nb` 10.0 ⇒ **358 withheld**) · `excluded_nonmarket` **0 of 0** · `subevents_recovered` **59** ·
`excluded_not_news` **{} (empty — no correction to subtract today)**.
⚠ **`tail = 0` is not the coverage claim**: **358 single-source clusters were not shown**, so no
"nothing happened in bucket X" sentence is made anywhere in this report.

★★ **`M1137` [measured] — the day's #1 event is a military escalation inside the Strait of Hormuz,
and it reverses the state the 08-30 run measured.**

| event | outlets / articles |
|---|---:|
| **"Oil rises as US, Iran resume military attacks"** | **16 / 28** |
| "Iran war live: IRGC attacks US bases in Jordan after US bombs **Larak Island**" | 9 / 14 |
| "Oil: geopolitical support and **Venezuela deal risk** – BNY" | 10 / 10 |
| "Bessent and G20 finance ministers" (subevent: *"Bessent calls on G20 to curb China trade imbalances"*) | 10 / 14 |
| "AI-driven cyber risk is top concern for global financial stability: Watchdog" (Bailey at G20) | 9 / 14 |
| **"10 Terrifying Words From Fed Chair Kevin Warsh at Jackson Hole Have Spooked Wall Street"** (subevent: *"Warsh's speech sends hike chances higher, may put Fed 'at odds' with Treasury"*) | 7 / 13 |
| "Toyota and Honda may get stuck with the bill for Trump's Canada tariffs" | 7 / 12 |
| **"John Ternus to lead Apple into the age of AI"** (subevent: *"John Ternus becomes Apple CEO"*) | 6 / 16 |
| "Dollar near two-week high as Warsh boosts rate-hike bets; **yen slips past 160**" | 5 / 7 |
| **"Eli Lilly buying Merida Biosciences for up to $2.875 billion"** | 5 / 8 |
| "Stock Market Today: Oil Climbs on Fresh Mideast Flare-Up — WSJ" | 5 / 6 |
| "Veteran analyst predicts Fed rate hike after Warsh's hawkish shift" | 5 / 5 |

**Body layer (2–4 outlets), the lines that carry sector transmission** — this is the tier the L2 spec
insists on, and today it is where the mechanism sits:
- *"Stock market today: Dow, S&P 500, Nasdaq **futures fall** as US strikes Iran, **rate-hike bets
  jump**"* [4] · *"Update: US Equity Futures Slightly Lower Pre-Bell as US, Iran Resume Hostilities"* [4]
- *"**QatarEnergy extends LNG cancellations into November** as Hormuz disruption drags on"* [4]
- *"**Goldman Sachs Sees Diesel Refining Margins Soaring to $63 a Barrel**"* [4] ← the refiners' leg
- *"**Asian Refiners Turn to Argentina** as Iran War Disrupts Oil Supply"* [3, subevent]
- *"Brent: **Hormuz tensions keep prices supported above $90** – ING"* [2]
- *"**Bond markets face fresh selling as oil prices jump**, stocks cautious"* [4] ·
  *"Stocks cautious on US-Iran escalation, **bond yields hit multi-year highs**"* [3] ·
  *"U.S. Treasury Yields Fall but **10-Year German Bund Yield Hits 15-Year High**"* [2]
- *"**The U.S. Struck Iran Again On Sunday: A September Rate Hike Is Now The Base Case**"* [2] ·
  *"US Stock Market: **Warsh signals Fed may need to raise rates** if inflation remains elevated"* [2]
- *"**Yen Breaks 160 Per Dollar Again as Traders Brace for Fresh Japan Intervention**"* [2] ·
  *"Japan July industrial output growth cools, bolstering **dovish BoJ** view and weighing on yen"* [3]
- *"**Nikkei Falls 2.2%, Dragged by Chip Stocks**"* [2] · *"Asian stocks drop on hawkish Warsh tone,
  oil gains"* [3]
- *"**Gold Extends Losses On Fed Rate Hike Expectations**"* [2] · *"Gold prices drop ₹9,500/10g in 4
  days… as US Fed rate hike bets increase"* [2]
- *"**SLB To Acquire Kelvion For $3.4 Bln To Expand Data Center Business**"* [2] ← an **Energy** name
  buying into **AI-power cooling**
- *"**Aon To Buy USI Insurance Services From KKR In $17 Bln Deal**"* [2] ← Financials/brokers
- *"**AI Chips Update — Optical Transceivers Propel AI Data Center Growth**"* [4] ← `D250`'s subject
- *"SK Hynix Weighs **Japan Memory Fab Partnership** to Supply AI Boom"* [4] ·
  *"Huawei and Apple bend to a tougher market as **memory crunch bites**"* [3]
- *"**Steel Hits 2½-Month Highs**"* [2] ← `NUE` is held · *"COPX: The Copper Shortage Trade Has One
  Major Weakness"* [2] ← `C24`
- *"US Stock Market: **Jobs data, Broadcom results to test stock rally** near record highs"* [2] —
  the two dated binaries the desk already brackets (`S126`/`P114`, `S132`/`S127`)
- *"Fire breaks out after unidentified explosions at **oil refinery in Baghdad**"* [2]

⚠ **What this layer does NOT contain**: any credit-stress item. The credit axis is **absent from the
narrative as well as flat in the data** — stated as a measured absence against a **344-event**
denominator, not as "quiet" (`G1` bars the latter and this is not that claim).

### B-2 · Trajectories — `thread --days 7 --scope foreign`

**Per-day denominator first** (the L2's own instruction): 08-25 **832** · 08-26 **832** · 08-27 **854**
· 08-28 **736** · 08-29 **307** · 08-30 **273** · 08-31 **344**. ⇒ **the weekend is a real ~2.5×
thinner tape, not a dark one** (`R110`) — so `FADING` tags on any thread whose mass sits mid-week are
**window-shape artifacts** and the curve is quoted instead of the tag.
**Population**: 4,178 day-events → 3,200 threads (520 multi-day, **121 alive**, 2,680 one-day of which
214 new today). Tags among the alive: **BUILDING 14 · REIGNITED 16 · FADING 0-in-top / many in tail ·
ENDED 399 (cumulative)**.

| thread | curve (08-25 → 08-31) | tag | reading |
|---|---|---|---|
| **"US forces strike two Iranian launchers on Iran's Larak…"** | **5→5→5→15→6→21→9** | FADING | 🚨 **the tag is wrong for the question being asked.** 21 outlets on 08-30 against a **273-article** day is the highest outlet-share of the week; 9 on 08-31 sits **beside** a *separate* 16-outlet cluster the same day (B-1) |
| **"Iran, Oman Agree to Temporary Strait of Hormuz Deal"** | 9→13→3→3, peak 13 | **ENDED** | ★ **the de-escalation thread ENDED on 08-28** and strikes resumed 08-30. A clean dated state change |
| "Qatar Extends LNG Force Majeure as Hormuz Traffic Remains…" | 11 outlets 08-28 | alive | extended **into November** today (B-1) |
| "Key Takeaways From Fed Chairman Warsh's Jackson Hole Speech" | 4→7→13→21→5→2→**7** | FADING | re-accelerates into today |
| "Warsh says Fed has 'work to do' if above-target inflation…" | 8→11→8→18→11→2→2 | FADING | |
| "Dollar jumps after Warsh comments, set for weekly gain" | 4→3→3→5→3 | REIGNITED | |
| "Canada set to announce retaliatory tariffs against US" | 29→15→9→5→4→4→**7** | FADING | re-accelerates; `S129` (09-09) and `S123` own this |
| "As Ukraine hits Russia's refineries, Russia targets Ukraine…" | 15→13→15→14→11→13→**9** | FADING | **the most persistent thread of the week** — the second refining-supply leg |
| **"Nvidia agrees to acquire Hugging Face for $12.9B"** | 15→2, peak 15 | **ENDED** | 🚨 **staleness flag on an ARMED row**: `S130` settles **09-10** on this event and its attention thread is already dead |
| "Nvidia tops earnings estimates, guides to $108bn" | 6→18→2, peak 18 | **ENDED** | |
| "SK Hynix to start AI chip volume production in Indiana" | 6→5→4 | REIGNITED | |
| "Aon nears $17bn deal to buy insurance broker USI" | 8→2 | FADING | **confirmed as a signed deal today** (B-1) — the thread faded *into* the event |
| "Analysis — Bessent, Warsh diverge on who should set the…" | 5→5→2 | REIGNITED | the policy-conflict leg of `P115` |

★ **`M1138` [measured] — `thread`'s tag disagreed with `brief`'s ranking on the run's single largest
event, and the disagreement is structural.** The Iran/Hormuz story is **#1 in `brief`** (16 outlets)
and tagged **FADING** in `thread`, because the linkage split it across ≥3 threads (Larak strikes /
Iran diplomacy / Hormuz deal-ENDED) and each fragment's curve is read separately.
⇒ **`D433` registered**: *when `brief`'s head layer ranks an event top-3 and no `thread` carries it
with a rising curve, check whether the linkage fragmented it before recording a `FADING`/`ENDED`
verdict on that subject.* ⚠ **This does not retract `M1106`** (three instruments agreeing Hormuz was
decaying as of 08-30) — that measured a real state, and **the state then changed by an event**. The
appended point is that the instruments would not have told us it changed.

### B-3 · Term sweep — with the same-day column `D411` asked for

Terms passed as **separate argv**, `--scope foreign`, direct queries outside the sweep window.
**No dark-day correction is applied** — `R110` withdrew it; the remote index was current throughout.

| term | **1d** | 7d | 30d | vel (7d/30d) | **1d ÷ 7d-avg** |
|---|---:|---:|---:|---:|---:|
| **Larak** | **91** | 92 | 100 | **3.94** | **6.92** 🚨 |
| **Warsh** | 300 | 1,474 | 2,373 | **2.66** | **1.42** |
| Jackson Hole | — | 1,306 | 1,485 | **3.77** | — |
| force majeure | 11 | 21 | 76 | 1.18 | **3.67** |
| **rate hike** | 196 | 860 | 3,247 | 1.14 | **1.60** |
| tariff | 330 | 1,993 | 6,601 | 1.29 | 1.16 |
| **Hormuz** | **201** | 1,081 | 5,138 | **0.90** | **1.30** |
| diesel | 46 | 255 | 1,115 | 0.98 | 1.26 |
| refining margin | 8 | 45 | 190 | 1.02 | 1.24 |
| inflation | — | 3,168 | 11,490 | 1.18 | — |
| recession | — | 325 | 1,248 | 1.12 | — |
| credit spread | — | 84 | 328 | 1.10 | — |
| layoffs | — | 116 | 524 | 0.95 | — |
| payrolls | — | 229 | 1,354 | 0.72 | — |

★★ **`M1139` [measured] — `D411`'s prescription changes the reading, and this is the run that proves
it.** The 7d/30d column says **Hormuz 0.90 = decaying**; the same-day column says Hormuz printed
**201 articles, 1.30× its own 7-day average**, and the escalation's proper noun — **`Larak`** — printed
**91 of its 100 thirty-day articles TODAY** (1d ÷ 7d-avg = **6.92**). **`theme_age` independently
returns Hormuz `0.83× ⚪ECHO`** and **Iran `0.94× ⚪ECHO`**, i.e. two of three instruments say
"decaying" while the event is the day's largest.
⇒ **The 7-day-over-90-day family of instruments is structurally blind to a one-day binary on an old
theme.** It is not broken — it measures the **stock** of attention. **The desk needs the flow column
to see an event, and until today it did not have one.** The same-day column is adopted from here on.
⚠ `theme_age` verdicts today, for the record: **Warsh 🟡ACCELERATING 3.27×** (the only accelerator) ·
optical ⚪ECHO **1.35×** · tariff 1.28× · rate hike 1.07× · memory 1.05× · data center 1.03× ·
copper 0.98× · Iran 0.94× · Hormuz 0.83× · refining margin 0.85×. **`age ≥ 90` on every term ⇒ the
🟢FRESH gate is arithmetically unreachable on this board** (`F1`, and it is arithmetic, not instrument —
`M1107` established that on a verified pipe).

### B-4 · Blind-spot pass — `blindspot --days 7 --scope foreign`

Top zero-token emerging terms (title frequency in the pool the fixed set never sees):
**Trump 935 · Iran 837 · China 835 · Bitcoin 677 · Fed 664 · Warsh 602 · Billion 575 · Wall/Street
498/508 · Oil 487 · Dollar 459 · Canada 425 · Energy 399 · Japan 391 · Meta 360 · Jackson 356 ·
Hole 350 · Bank 362 · Dividend 365.**

⇒ **The blind-spot pass, the event pass and the term sweep now agree on the same two clusters** —
**Iran/Oil** and **Warsh/Jackson Hole**. That is a convergence, not three independent confirmations,
and is recorded as such (`D5`-hygiene: three views of one corpus are one source).
**New terms folded into the living table this run: `Larak` · `Strait of Hormuz` · `refining margin` ·
`diesel crack` · `yen intervention` · `optical transceiver`.**
Random sample read raw (8 rows): Druckenmiller/Revolution Medicines, Kirby (marine transport),
Anthropic physical-world standard, The9 Q2, AUD/Iran sanctions, Social Security, US Open, Michael
Burry halving his NVDA call hedge. **No single-name rank-jump ⇒ nothing promoted from the sample.**
⚠ `Dollar` at 459 with **`DTWEXBGS` 10 days stale** is `D333` arriving from a second direction for the
second consecutive run.

---

## §C · Propositions — falsifiable, both branches, mandatory anti-signal

> **ID 3-grep at write time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`:
> `P118`–`P120` · `M1133`–`M1139` · `D431`–`D433` → **0 hits**. Issued by `module_evidence next-id`.
> ⚠ **All three rows are keyed to observables the 08-28 ghost bar and the `BZ=F` roll do not touch.**
> Every relative-performance number names its benchmark inline (`C1`).

### `P118` — ★★★ The war premium came back. Is it in the **barrel** or only in the **crack**?

**Claim to falsify**: *the 08-30/31 escalation re-prices crude itself, not merely refined product* —
i.e. this is a supply-of-oil event, not a supply-of-refining event.

**Anchors.** `[news]` B-1: **"Oil rises as US, Iran resume military attacks" [16 outlets / 28
articles]**, **"IRGC attacks US bases in Jordan after US bombs Larak Island" [9/14]**, *"QatarEnergy
extends LNG cancellations **into November**"* [4], *"Asian Refiners Turn to **Argentina** as Iran War
Disrupts Oil Supply"* [3], *"Brent: Hormuz tensions keep prices supported **above $90**"* [2],
**"Goldman Sachs Sees Diesel Refining Margins Soaring to $63 a Barrel" [4]**.
`[measured]` term sweep: **`Larak` 91 of 100 thirty-day articles printed today** (B-3).
`[measured]` COT: **WTI spec net at the 43rd percentile — the war premium is not a crowded long** (A-3).
**Thread**: the de-escalation thread (*"Iran, Oman Agree to Temporary Strait of Hormuz Deal"*, peak 13
outlets) is **ENDED** as of 08-28; the strike thread carried **21 outlets on a 273-article day** (B-2).

**Frozen observable**: **`DCOILWTICO` `[FRED]` — spot WTI, roll-immune** — **first observation
covering 2026-09-11 or later**, against its **2026-08-25 value of 83.90**.

| branch | threshold | meaning |
|---|---|---|
| **A (the barrel repriced)** | `DCOILWTICO` **≥ 91.00** | +8.5% ⇒ crude carries the event; Energy is an **oil** call, `XLE` leads on the barrel, and the desk's `N` on Energy is too low |
| **B (only the crack repriced)** | `DCOILWTICO` **≤ 82.00** | −2.3% ⇒ crude gave it back while diesel margins held ⇒ the move is **downstream**, refiners (`MPC`/`PSX`, held) are the expression and integrated majors are not |
| **C** | between | disclosed as the modal outcome |

- **Band derivation, stated (`C5`)**: `DCOILWTICO`'s own realised range 08-14→08-25 is **83.90–89.75**
  (7.0% wide). A is **+8.5%** (just outside the month's high), B is **−2.3%** (just below the month's
  low). ⚠ **Asymmetric and disclosed**: the series sits at the bottom of its own month, so the room
  below is mechanically thinner than the room above.
- ⚠ **Why not `BZ=F`**: **the Brent front month rolled on 08-31** (`M1136`, A-5) and a −3.30
  Brent–WTI spread shift is a contract change, not a price. `P107`/`P117` stay ARMED on their own
  `BZ=F` thresholds (`D242`) and this row is the **roll-immune** companion, registered as a
  deliberate near-duplicate, not discovered as one.
- ⚠ **Anti-signal (AMBIGUOUS)**: **a Venezuela supply event.** *"Trump Says Venezuelan Oil Will Refill
  U.S. Strategic Petroleum Reserve"* [3] and *"Oil: geopolitical support and **Venezuela deal risk**"*
  [10] both printed today. **Base rate checked and NOT remote — this is `P117`'s registered VOID
  condition already advancing** (`M1108`). ⚠ Second anti-signal: an **OPEC+ quota decision** in the
  window. ⚠ Third: `DCOILWTICO` is **6 days stale on its Brent sibling** — if the 09-11 bar has not
  published at the next run, this row is **DEFERRED and named, not `EXPIRED`** (`D333` clause,
  written in at registration).
- **Information content (`L3`)**: **HIGH on B.** B separates the barrel from the crack — the exact
  separation `R89`/`P83` bar the desk from *asserting*, which is why it must be **measured** instead.
  A is the direction the news is already travelling and is worth less.
- ⚠ **Non-redundancy (`D343`)**: `P107` (BZ=F ≥96 through 09-08) and `P112`/`P117` observe **Brent
  futures**. This observes **spot WTI** on a later window. If Brent-futures rows and this row fire
  different branches, **the disagreement is `D432`'s evidence**, not a contradiction to resolve.

### `P119` — ★★★ Yen through 160: the transmission leg nothing in this desk brackets

**Claim to falsify**: *the yen breaking 160 is a **dollar/rate-differential** event that resolves with
the US front end, not an independent shock requiring intervention.*

**Anchors.** `[news]` B-1: *"Dollar near two-week high as Warsh boosts rate-hike bets; **yen slips
past 160**"* [5/7], **"Yen Breaks 160 Per Dollar Again as Traders Brace for Fresh Japan
Intervention"** [2], *"Japan July industrial output growth cools, bolstering **dovish BoJ** view and
weighing on yen"* [3], *"Yen might be on its way to ¥164 to the dollar"* [2], **"Nikkei Falls 2.2%,
Dragged by Chip Stocks"** [2]. **Thread**: *"Tokyo bought the Japanese Yen a range, not a trend"*
(REIGNITED 5→5→2→4→3) and *"Dollar jumps after Warsh comments"* (REIGNITED 4→3→3→5→3).
`[FRED]` `DGS2` **4.20 = 91.2nd %ile** (08-27) as the US leg. ⚠ **`DTWEXBGS` is 10 days stale
(`D333`), so the dollar leg cannot be anchored on FRED** — this row therefore uses the cross rate.

**Frozen observable**: **`JPY=X` (USD/JPY) daily settled close, `yfinance`, `auto_adjust=False`, any
settled bar 2026-09-01 → 2026-09-18**, against the **08-28 settled close of 159.32**.
⚠ **FX has no front-month roll** — `M1136`'s defect cannot touch this observable, and that is why it
was chosen over a Nikkei future.

| branch | threshold | meaning |
|---|---|---|
| **A (rate-differential, unresolved)** | `JPY=X` **≥ 164.00** on any settled bar | +2.9% ⇒ the differential dominates and Tokyo's range-defence fails ⇒ Japanese chip/exporter weakness (`Nikkei −2.2%`) is a **funding** story that reaches `SMH` and the desk's IT names |
| **B (intervention or reversal)** | `JPY=X` **≤ 156.00** on any settled bar | −2.1% ⇒ MoF acted or the US front end retraced ⇒ the yen leg is **not** an independent risk and `P115`-B gains a second, independent confirmation |
| **C** | neither touched by 09-18 | contested range persists — the "range, not a trend" thread wins |

- **Band derivation, stated (`C5`)**: 20-day realised range 158.9–159.9 is only **0.6%** wide, so a
  symmetric band on realised vol would fire on noise. Bands are set at the **levels the narrative
  itself names** — 164 is quoted in a headline, 156 is the round level below the 20-day base — and are
  **2.9% / 2.1%** away, i.e. ~4–5× the realised range in both directions (`D216`: reachable both ways).
- ⚠ **Anti-signal (AMBIGUOUS)**: **a BoJ policy meeting or an announced MoF intervention inside the
  window** makes branch B an administrative outcome rather than a market one. ⚠ Base rate checked and
  **NOT remote** — the intervention story is already in the headline layer.
- **Information content**: **HIGH on A.** The desk holds four AI-compute names and has **no row at all**
  on the funding channel that moved Japanese chip stocks 2.2% overnight. B is the branch that would
  retire the leg.
- ⚠ **Non-redundancy (`D343`)**: no existing row observes FX. `P115` observes `DGS2`; this observes the
  cross rate the same policy expectation is being expressed in. If `P115` fires A and this fires B,
  **that pair is the finding** (the US front end held while the yen did not follow).

### `P120` — ★★ The credit axis has now been silent for three runs against a 344-event denominator

**Claim to falsify**: *credit's refusal to confirm the tightening story is **information**, not lag* —
i.e. HY OAS at its 365-day low is a live reading of a funding-easy economy, and it will not converge
toward the equity/rates story even after an oil shock and a hawkish repricing.

**Anchors `[FRED]`**: `hy_oas` **2.63 = 0.0th %ile** · `ig_oas` 0.79 (45.3rd) · `NFCI` **−0.566 =
0.0th** · `VIX` 14.51 (3.9th), all 08-27 (08-21 for `NFCI`), against `DGS10` **93rd** and `DFII10`
**89th**. `[news]` **a measured absence**: in **344 market events** and a 311-line body layer, **zero**
credit-stress items; the nearest are *"US debt burden raises longer-term risks as borrowing costs…"*
[3] and *"Private Credit Investors Prefer Being Trapped Than Tak…"* [4→2, FADING] — neither is a spread
event. **Thread**: **no credit thread among the 121 alive** — stated as an absence against a named
denominator, not as "quiet".

**Frozen observable**: **`BAMLC0A0CM` (IG OAS) `[FRED]`, first observation covering 2026-09-25 or
later**, against **0.79** (08-27).
⚠ **Deliberately IG, not HY** — `P108` (09-11) and `P116` (09-18) already own HY OAS on two windows.
This row observes the **investment-grade** leg, which is the one sitting mid-range (45th %ile) and
therefore the one with room to move in **either** direction; HY is pinned at its own low and its
downside branch is mechanically near-impossible (the `S61` failure this desk has logged).

| branch | threshold | meaning |
|---|---|---|
| **A (credit is information)** | `ig_oas` **≤ 0.76** | a new low in the IG leg after an oil shock + a hawkish repricing ⇒ the funding channel genuinely is not transmitting, and every "duration is breaking `UTIL`/`RE`" line stays **narrative-only** |
| **B (credit was lagging)** | `ig_oas` **≥ 0.88** | +9 bp ⇒ IG confirms the rates story; the `UTIL`/`RE`/`INDU` underweights get a funding cause and `S135`'s three-UW spread should compress toward "one bet" |
| **C** | between | disclosed as the modal outcome |

- **Band derivation, stated (`C5`)**: 365-day range **0.73–0.94**; current 0.79 sits at the 45.3rd
  percentile. A is **−3 bp** (0.76, above the yearly low of 0.73 so it is reachable), B is **+9 bp**
  (0.88, below the yearly high of 0.94 so it is also reachable). **Symmetric in reachability, not in
  basis points**, and that is the point of choosing IG over HY.
- ⚠ **Anti-signal (AMBIGUOUS)**: an **index-composition change in `BAMLC0A0CM`**, or a **single large
  IG downgrade/fallen-angel event**, moves the level without a macro repricing.
- ⚠ **`D431` clause, written in at registration**: `BAMLC0A0CM` is currently **3 business days in
  arrears** and its release does not travel with `T10YIE`. **If the 09-25 bar has not published at the
  next run after that date, this row is DEFERRED and named, not `EXPIRED`.**
- **Information content**: **HIGH on B**, because B is the first funding-side confirmation of a story
  the equity tape has now told alone for **three** runs; **MEDIUM on A**, which continues an extreme.
- ⚠ **Non-redundancy (`D343`)**: `P108` = HY, 09-11. `P116` = HY, 09-18. `S111` = IG, first close
  covering 08-28 (**still blocked**, A-1). This is IG on **09-25**, a fourth window, and it is
  registered **because `S111` has been unreadable for two runs** — if `S111` becomes readable before
  09-25, the two are scored independently and any disagreement is recorded, not reconciled.

---

## §D · ★ SECTOR TRANSMISSION MATRIX — wind direction only (ROTATION's input)

> **Each line names the axes it actually stands on.** Where the repaired sweep is the source it says
> `repaired sweep`; where a sector's sign is owned by one name (`G3`) the line says so and **does not
> propose a promotion or demotion on that axis**. No line uses §A-6's quarantined pre-open numbers.

| GICS sector | wind | driving proposition | axes this line stands on |
|---|---|---|---|
| **Energy** | **OW ↑** (up from the carried `N`) | **`P118`** | `[news]` **16-outlet escalation + Larak 91/100 same-day** (B-1/B-3) · `[measured]` **WTI COT 43rd %ile = room, not crowding** · ⚠ 🚫 **not on `wflow`** — `XOM` (30.5%) owns the sector's negative sign and ex-`XOM` it is **+0.074** (`G3`). ⚠ **`R89`/`P83` bar any margin-vs-barrel separation claim; `P118` is the row that measures it instead** |
| **Utilities** | **UW ↓ (strongest UW)** | `P115` · `P120` | `repaired sweep` **wflow −0.549, eqflow −0.524, 10 reds of 15, worst of eleven**, and **no flipper problem** (`NEE` 17.7%, ex-top1 −0.525 — the weakness is broad). `[FRED]` real 10y **89th %ile**. ⚠ **the funding leg is `narrative-only` until `P120` scores** |
| **Real Estate** | **UW** | `P115` · `P120` | `repaired sweep` **−0.338**, ex-top1 **−0.415** (worse without `WELL` ⇒ broad). ⚠ Δ **+0.078**, i.e. improving off a deep base — recorded, not acted on |
| **Industrials** | **UW** | `P115` · `S126` | `repaired sweep` **−0.317**, **17 reds of 50 — the largest red count on the board**, ex-top1 −0.291 (`CAT` only 8.7% ⇒ genuinely broad). Δ **−0.129**, still deteriorating |
| **Consumer Discretionary** | **UW, held under protest** | `P115` | `repaired sweep` −0.262 with **12 reds of 28** — ⚠ **but `AMZN` (40.2%) owns the sign and ex-`AMZN` the sector is +0.056** (`G3`) ⇒ 🚫 **no demotion may be argued on `wflow` this run.** The UW is carried on **breadth** (12/28 red) and is stated as such |
| **Information Technology** | **N, and the N is doing work** | `P119` · `S124` | `repaired sweep` **+0.033 but eqflow −0.034 and 13 reds of 56** ⇒ cap-weight positive, equal-weight negative. ⚠ `NVDA` (19.4%) owns the sign; ex-`NVDA` **−0.016** (`G3`) ⇒ 🚫 no promotion on `wflow`. `[news]` **Nikkei −2.2% on chips**, **memory crunch**, **optical transceivers** — three live legs, one of which (`P119`) is a funding channel the desk has never bracketed |
| **Communication Services** | **OW− (down from `OW`)** | — | `repaired sweep` **wflow −0.422 but eqflow +0.080** — the negative is **`GOOGL`+`GOOG` ≈85% of bucket cap, both 🔴분산**, so `eqflow` is the honest read and it is positive. Δ **−0.162** is the worst delta on the board. `[news]` **Apple CEO transition (6/16)** sits in IT but reprices the same platform complex. ⇒ **downgraded one notch on Δ, not on level** |
| **Health Care** | **OW** | — | `repaired sweep` +0.021 headline but **eqflow +0.135 and ex-`LLY` +0.095** ⇒ ★ **`D424` shape**: the top-1 is a **drag**, and the sector is materially stronger underneath. Only **1 green in 32** but only **2 reds**. `[news]` **`LLY` buying Merida Biosciences (5/8)** and new Taltz/Zepbound Phase 3b data — the drag name is the one doing deals |
| **Materials** | **OW** | — | `repaired sweep` **rank 1, +0.225, Δ +0.197 (the largest positive delta on the board), zero reds in 12**, ex-top1 +0.233 ⇒ broad. `[news]` *"Steel Hits 2½-Month Highs"*. ⚠ **`C24` unresolved and reproduced**: copper COT **100th %ile** against a rank-1 flow. **Not resolved by picking a side** |
| **Financials** | **OW−** | `P120` | `repaired sweep` −0.072 with **Δ +0.073**, ex-top1 −0.020, **0 greens in 47**. `[news]` **Aon/USI $17bn (2)** — consolidation, not credit. ⚠ **`P115`-A would help this sector and `P120`-B would hurt it**; the two are registered on different observables precisely so the sector is not talked into one story |
| **Consumer Staples** | **N** | — | `repaired sweep` −0.264 but **Δ +0.080**; ex-`WMT` −0.130 (better without it). `[news]` *"Companies Plow Tariff Refunds Into Price Cuts"* [3] — a margin-vs-volume item, direction unresolved |

**Wind summary**: **OW** = Energy(↑), Health Care, Materials · **OW−** = Financials, Comm. Services(↓)
· **N** = IT, Consumer Staples · **UW** = Utilities(strongest), Real Estate, Industrials, Consumer
Discretionary.
⚠ **The only verdict this stage MOVED is Energy `N → OW`**, and it moved on **`[news]` + positioning**,
with the flow axis explicitly excluded because `XOM` owns its sign. **Comm. Services `OW → OW−`** moved
on **Δ**, not level. Everything else is carried.

---

## §E · Self-backtest — this desk's own hit rate

### E-1 · Live rows — status, every deferral named

| id | window | status this run |
|---|---|---|
| `P115` | `DGS2` at first close covering 09-04 | **ARMED**, not due |
| `P116` | HY OAS at first close covering 09-18 | **ARMED**, not due |
| `P117` | `BZ=F` 08-31 → 09-18 | **ARMED**. 🚨 **contaminated by the roll (`M1136`) — disclosed, thresholds NOT changed** |
| `P107` | `BZ=F` ≥96.00 through 09-08 | **ARMED**. Same contamination. ⚠ On **FRED spot Brent** the 96.00 line was touched 08-21 at **96.92**; on `BZ=F` it was not — `D413`, unchanged |
| `P108` · `P111` · `P112` · `P114` · `P116` | 09-11 / 09-14 / 09-11 / 09-04+ / 09-18 | **ARMED**, not due |
| `P67` · `P86` · `P97` | `[FRED]`-blocked | **ARMED**, pre-settle reads disclosed in `HANDOVER §2c`, **not scored** |
| `S111` · `S120` | need the 08-28 `[FRED]` close | **ARMED**, blocked a 2nd run (A-1) |
| `S92` `S94` `S103` `S104` `S112` `S124` `S131` | settle 08-31 | **NOT DUE** — the session had not closed at run time (`M1127`) |
| `S130` | 09-10, `NVDA`/Hugging Face | **ARMED** ⚠ **staleness flag raised**: its attention thread is **ENDED** (peak 15 outlets, dead by 08-28) — B-2 |
| `S8` | undated | ⛔ **33rd consecutive run unscoreable**; needs a human `VOID` or a date (P5) |

**Scored this run: 0.** Composition: **7 not-due-by-clock · 5 `[FRED]`-blocked · 1 unscoreable · 0
silent skips** (`D430`'s prescription, executed in the run that registered it).

### E-2 · Running hit-rate and the pattern in the misses

The desk's own recorded pattern is carried unchanged and it is the reason nothing above was
pre-scored: **"a pre-settle read is not a weak version of a verdict; on this desk's record it has been
an inverted one"** — `S101` (registered −0.677, pre-settle **+1.616**, final **−0.744**), `P78`
(pre-settle above A, final **B**), `P96` (live **−8.584** deep in A, settled **+4.874** = **B**).
**Three for three inverted.** ⇒ every disclosed pre-settle number in `HANDOVER §2c` and §E-1 above is
labelled as **not a score**, and none is inherited as a verdict.

### E-3 · 🚨 What this stage asserted and then refuted, in the same run (`§4c` / `D48`)

**Nothing was retracted this run** — but one thing was **caught before it was written**, and the
catch is the reportable part:

★ **`M1140` [measured].** The first read of `BZ=F` 08-31 vs 08-28 was **−1.14% while `CL=F` was
+2.75%**, and the natural sentence — *"Brent fell despite the escalation"* — was **one keystroke from
this report**. Checking the **spread** instead of the level killed it: Brent−WTI moved **5.91 → 2.61**
against a 60-day range of 2.40–8.50, which no physical relationship does in a session. **The
escalation reading survives (`CL=F` +2.75%); the Brent sentence does not exist.**
⇒ This is `D419`'s discipline (re-derive from the artifact) applied by the author to **their own**
first draft, and it is written down because a run that only shows its surviving claims has hidden its
own error rate.

### E-4 · The one carried claim this run degrades

**`M1106`/`M1107` (08-30): "three instruments, one answer — Hormuz is decaying" — SURVIVES as a
measurement and is DEGRADED as a guide.** Today's same-day column (`M1139`) and the event pass
(`M1137`) show the three agreeing instruments are all **stock-of-attention** measures over 7–90 day
windows, and **all three still say "decaying" on the day the strait's escalation is the #1 story with
16 outlets.** ⇒ **Not retracted** — appended (`D48`). The correction is to the **inference**, not the
number: *"three instruments agree"* was three views of one window, and the desk now carries a flow
column so this cannot recur silently.

---

## ✅ EXIT CHECK

- [x] **Catalysts injected** — `catalyst_calendar --days 12` (extended past the `--days 5` default
      because ARMED rows sit on 09-04/09-08/09-11, per the L2's own instruction): **5 binaries** —
      MSCI review **D-0**, `AVGO` **D-2**, NFP **D-4**, PPI **D-10**, CPI **D-11**, plus the undated
      Hormuz trigger. **All five already carry both-sides brackets** (`HANDOVER §8`).
- [x] **Narrative read** — events (`brief --body 2`, `embed sync` run first per `R110`), trajectories
      (`thread --days 7`), 7-bucket term sweep, blind-spot pass. **Indicators read** — FRED primaries
      + COT positioning + FINRA short-vol. **Daily anchor** = the 08-30 `MACRO_REPORT.md` read in
      full (its `P115`–`P117` carried in §E-1, its `M1106`/`M1107` re-examined in §E-4).
- [x] **`--body 2` used; tail = 0.**
- [x] **`tail = 0` is NOT treated as the coverage claim** — `single_source` **15 shown / 373 total ⇒
      358 withheld** (`min_nb` 10.0); `excluded_nonmarket` **0 / 0**; `subevents_recovered` **59**.
      **No "quiet bucket" claim is made anywhere in this report**, and the one absence that *is*
      claimed (credit, `P120`) is stated against the **344-event** denominator and the **121 alive
      threads**, with the two nearest non-qualifying items quoted.
- [x] **Denominator is the corrected one** — `excluded_not_news` is **empty `{}` today**, so
      **1,944 articles** needs no subtraction. Stated rather than assumed.
- [x] **Trajectories read** — every proposition names its thread's tag **and** curve, or states "no
      thread" explicitly (`P120` does: **no credit thread among 121 alive**). ★ **An ENDED thread
      under an ARMED row is flagged**: `S130`. ★ The per-day denominator was read **first** and used
      to reject a `FADING` tag as a window artifact (B-2, `M1138`).
- [x] **No bucket's low count is trusted** — `force majeure` (21/76) and `refining margin` (45/190)
      are read **only** through their same-day ratios (3.67× / 1.24×), never as "quiet".
- [x] **Both halves of every headline print** — July CPI quoted **+3.30% YoY and +0.07% MoM**, core
      **+2.47% YoY and +0.22% MoM**, like-for-like monthly windows.
- [x] **Every relative-performance number names its benchmark inline** (`vs SPY` on every excess
      figure; `Brent − WTI` named as a spread). **No statistical result carried across markets** —
      `M1132`'s `vol_surge` result is `market=kr` and is explicitly **not** applied here (`W1`).
- [x] **Credit axis read and cited** — `hy_oas` **2.63 (0.0th)** + `nfci` **−0.566 (0.0th)**; every
      tightening sentence in §D is labelled `narrative-only` where credit does not support it.
- [x] **`real_10y` quoted with `breakeven_10y`** — 2.34 (89th) with 2.31 (45.6th).
- [x] **Linter** — `python -X utf8 scripts/report_lint.py llm_outputs/2026-08-31/industry_US/MACRO_REPORT.md`
      → **0 findings** on C1 / C2 / S6 / D6, no exemptions claimed. ⚠ It checks **form only**; a clean
      run is not a correct report, and the substantive risks in this one are named in §A-5 (the roll)
      and §E-4 (the degraded inference), not in the linter's scope.
- [x] **Transmission matrix produced** — all 11 sectors, one line each, each naming its axes.
- [x] **MACRO_REPORT.md written** with primary numbers explicit; self-backtest appended; new
      blind-spot terms folded into the living table (**`Larak` · `Strait of Hormuz` · `refining
      margin` · `diesel crack` · `yen intervention` · `optical transceiver`**).

---
> Next: `run_protocol.py industry_us --next` → **SWEEP** (Stage 4).
> ⚠ SWEEP inherits: the primary sweep is empty; `SECTOR_FLOW_US_REPAIRED.json` is the citable object;
> Energy moved `N → OW` on `[news]`+positioning with the flow axis excluded (`G3`).

---

# §5 · ADDENDUM — DRIFT WATCH (Stage 11, post-run) · appended 2026-08-31, never clobbered

> `drift_watch.py --report MACRO_REPORT.md` — completion stamp **2026-08-31T22:40 KST**, window
> **0.6h**. ⚠ **`D422` binds this window**: the anchor is the report's completion time, so this watch
> covers **36 minutes**, not the session. The report's own subject — the 08-30/31 escalation — sits
> **outside** the watched window by construction. **Named, not worked around.**
> ⚠ **Nothing below is a score.** Every registered row stays ARMED on its frozen threshold (`D242`).

## 4 burst candidates ≥3.0×, all body-read (not merely counted)

| term set | post-completion | vs normal |
|---|---:|---:|
| **`strikes on Iran`** | 5 | **20.6×** |
| `downgrade` | 7 | 8.3× |
| **`rate hike`** | 14 | **4.7×** |
| `default` | 4 | 3.2× |

`downgrade` and `default` are **false positives on body-read** — their triggering articles are
*"Tyler Technologies boosts 2030 goals"*, *"S&P Global's remaining divisions post spin-out"*,
*"Broadcom introduces VMware Private AI Cloud"*. **Term-match, not event.** Dismissed with the reason.

## 🚨 The drift that matters — and it points AGAINST this report's own principal claim

Body-read of the `strikes on Iran` / `rate hike` bursts (all 2026-08-31, foreign):

- **`oilprice`: *"Iran Says Supertanker Hit by Mines in Strait of Hormuz"*** · **`upi`: *"IRGC says
  ship struck 2 sea mines after U.S. declared Hormuz cleared"*** · **`guardian`: *"…supertanker hits
  mines and catches fire — Middle East crisis live"*** · `fxstreet`: *"WTI rises to near $84.50 as
  IRGC claims supertanker struck by mines in Hormuz"*.
  ⇒ **a PHYSICAL TRANSIT event, not only strikes.** §A's node 3 (the chokepoint) escalates from
  "military exchange" to **"mines in the water and a hull on fire"**, and the `Strait of Hormuz`
  same-day count is **188**, `supertanker` **11**, `mines` **186**.
- **`yahoo_finance`: *"Chevron and Exxon Mobil Rise 3% as U.S. Strikes on Iran Push WTI Crude Oil to
  $86"*** · `oilprice`: *"Asia Steps In to Fill Diesel Supply Gap in Africa as **Middle East Exports
  Crash**"* · `oilprice`: *"China's LNG Imports Set to Drop 18% in August as Prices Soar"*.
- `fxstreet`: *"Dow Jones futures slip as traders adopt caution amid higher oil prices"* ·
  *"Why the Tech Stocks Rally is Under Threat From Surging Rate-Hike Odds"*.

### 🚨 The report's chain-position claim is being contradicted in the session that followed it

§D promoted Energy `N → OW` and `SECTOR_ROTATION §2` + `SECTOR_DEEP_ENRG` argued the escalation's
beneficiary is the **chain's midpoint** (services + refining), because the money had left E&P
**before** the strikes. **Measured live at ET 10:18 (≈48 minutes into the 08-31 session):**

| leg | names | live move vs the 08-28 settle |
|---|---|---|
| **E&P / integrated** | `XOM` **+2.15%** · `FANG` **+2.01%** · `EOG` **+1.65%** · `CVX` +1.06% | **EW{XOM,EOG,FANG} = +1.94%** |
| **services / refining** | `SLB` **+3.18%** · `COP` +2.20% · `VLO` +0.96% · `PSX` +0.78% · `MPC` +0.38% | **EW{SLB,MPC,PSX,VLO,COP} = +1.50%** |
| benchmark | `SPY` **−0.47%** | — |

⇒ **`S136`'s spread reads ≈ −0.44pp intraday, i.e. toward branch B — the branch that says THIS RUN'S
HEADLINE FLOW FINDING IS WRONG.**
🚫 **This is explicitly NOT a score.** `S136`'s observable is a **5-session sum from the first settled
close after 09-01 through 09-08**, and the number above is **48 minutes of an unsettled bar**.
★ **And the desk's own record is the reason to distrust it in either direction: pre-settle reads have
been INVERTED three-for-three** (`S101` registered −0.677 / pre-settle **+1.616** / final −0.744;
`P78` pre-settle above A / final **B**; `P96` live **−8.584** deep in A / settled **+4.874** = **B**).
**The pre-settle number is disclosed so the next run inherits it together with this warning.**
⚠ `SLB` is nonetheless the single best of the nine (+3.18%) — **which is exactly the ambiguity
`EVENT_ALPHA` card 8 pre-registered**: a barrel move lifts an oilfield-services name for a reason that
is not its data-centre thesis.

### ⚠ A headline number this addendum REFUSES to propagate

`zerohedge` (title-only, no body): ***"Oil Tops $91, US Diesel Crack Near $100 As US-Iran Strikes
Resume, Tehran Claims Supertanker Mined In Hormuz."***
**Checked against the tape rather than repeated**: at ET 10:18 `CL=F` reads **85.59** and `BZ=F`
**88.38**; `fxstreet`'s own sequence through the session is **$83.50 → $84.50 → $85.50**, and
`yahoo_finance` says **$86**. **No source I can measure puts crude at $91.**
⇒ 🚫 **The "$91" and the "$100 diesel crack" are NOT carried into any proposition, matrix line or
verdict.** They are recorded here as an unverified headline so a later run can settle them, per the
rule that a load-bearing number needs a receipt and not a headline.
⚠ **`P118`'s branch A is `DCOILWTICO` ≥ 91.00 at the first `[FRED]` observation covering 09-11** —
had the $91 been taken at face value, this addendum would have been one keystroke from reading a
title-only headline as a branch touch on a row registered eight hours earlier. **It is not.**

## ★ A recovery path I hypothesised this stage and then REFUTED with a wider sample (`D48`)

`fast_info.previousClose` returned **769.35** for `SPY` against the 5m proxy's **769.38** — a
**0.004%** match — which suggested a **third, simpler recovery path** for the 08-28 ghost close.
**Widened to the same 24-name validation set, it fails:**

| | value |
|---|---:|
| mean abs error vs the 5m proxy | **0.394%** |
| max abs error | 🚨 **3.208%** (`XLU`: 44.08 vs 42.71) |
| names above 0.05% | **17 of 24** |
| second-worst | `XLB` **1.712%** · `MET` **1.461%** |

⇒ **It is right on the most liquid names (`NDAQ` 0.000% · `NUE` 0.002% · `SPY` 0.004% · `XLV` 0.003%)
and wrong by up to 3.2% elsewhere** — the classic shape of a value that is sometimes adjusted or
stale. 🚫 **Not adopted. The 5m proxy (0.018% mean / 0.045% max) remains the only validated path.**
★ **Written down rather than deleted**: the first observation (`SPY` at 0.004%) would have been a
perfectly convincing single-name proof, and **the only thing that killed it was widening n from 1 to
24.** ⇒ **`D439` registered**: *a recovery path is validated on the full n=24 set before it is called
a path — a single liquid name will agree with almost anything.*

## What this addendum changes, and what it does not

- **Changes**: §A's node-3 characterisation is upgraded from *"military exchange"* to
  **"physical transit disruption — mines, a struck hull, and `Strait of Hormuz` at 188 same-day
  articles."** The `EVENT_ALPHA` card-1 direction read (supply destroyed on two legs) is
  **strengthened**, not weakened.
- **Does not change**: **no threshold, no branch, no sector verdict.** `S136`, `P118`, `P107`, `P112`,
  `P117` all stay **ARMED on their frozen thresholds**. Energy stays **`OW`**. `INDU` stays **`UW−`**.
- **Leaves standing, deliberately**: this report's chain-position claim **and** the live number that
  points against it, side by side. **That asymmetry is the self-backtest's food** — a run that only
  showed its surviving claims would have hidden its own error rate, and the next run inherits both.
