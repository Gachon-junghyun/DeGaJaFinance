# MACRO_REPORT — industry_US · 2026-07-17 (Fri)

> Stage 1 / L1·MACRO. Runtime `--market us`, English-pure. Primary data: `module_macro_us` [FRED],
> `us_flow --cot` positioning, `module_news_data` events (`brief --body 2`) + 7-bucket velocity +
> blindspot, tape via `module_flow` / yfinance. Deliverable = the **§4 transmission matrix**
> (ROTATION's input). Zero buy/sell calls.
> Continuity anchor: `llm_outputs/2026-07-15/industry_US/MACRO_REPORT.md`.
> Handoff ledger mode: **not built** — `DEGAJA_REPORT_DIR=llm_outputs module_report_tags show` →
> "ledger absent". Inherited coverage read from the 07-15 artifacts directly. (PROMPT_MAP §6 open
> decision still unlocked.)

---

## §0 Catalyst injection (run-start, from CATALYST_WATCH.json)
| When | Event | Axis | Binary? |
|---|---|---|---|
| **D-0 (today)** | **NFLX earnings** | earnings | ✅ ≤48h → PREMORTEM must bracket both ways |
| Undated / live | **Iran "Strait of Hormuz open" (TACO trigger)** | oil | ✅ open-ended → both-sides bracket |
| D-4 (07-21) | SCHW earnings | financials | ✅ — tests the P5 bank leg |
| D-5 (07-22) | TSLA earnings | earnings/DISC | ✅ |
| D-5 (07-22) | KMI earnings | energy | ✅ |

⚠ **One-way tilt into NFLX or the Hormuz binary = protocol violation.** Both handed to PREMORTEM.

---

## §1 Regime read — primary numbers explicit

### The core wedge this run: **the market flipped the SIGN it puts on AI capex**
TSMC on 07-16 posted a **record profit**, **raised both capex and revenue guidance**, and pledged
**another $100bn** for US fab expansion (on top of $165bn) [BBC · SCMP · Yahoo Finance 07-16].
The chip complex then **sold off**:
- *"Chip Stocks Slide On TSMC **Capex Concerns**"* [Yahoo Finance 07-16]
- *"Chip Stocks Extend Rout as TSMC Results Fall Short of a **High Bar**"* [Bloomberg 07-17]
- *"no single catalyst behind the selloff, but we had TSMC's earnings shortly after"* [Deutsche Bank via FXStreet 07-17]

**Read:** rising AI capex used to be priced as *demand confirmation* (bull the whole chain). It is now
being priced as *margin cost + bubble funding* (bear the chain). The tell that this is a **sign-flip and
not a TSMC-specific miss**: the intended *beneficiaries* of that same capex fell too — **GEV −5.1%**,
**VRT RS60 −12.4%**. A pure TSMC miss would have rotated money *into* the capex recipients, not out.

### It is a ROTATION, not a crash — the breadth tell
| Ticker | 07-10 | 07-16 | 5-session | Read |
|---|---|---|---|---|
| **MU** | 979.30 | **853.20** | **−12.9%** (−5.6% on 07-16 alone) | Epicenter. RS60 was **+84.3%** → RS20 **−16.5%**: a blow-off rolling over |
| **SMH** | 611.03 | 568.92 | **−6.9%** | RS20 −7.7% vs SPY |
| **TSM** | 434.11 | 409.74 | −5.6% | 🔴 distribution on **1.13× volume** — the only surge on the board |
| NVDA | 210.96 | 207.40 | −1.7% | 🟡 holding up better than the complex |
| QQQ | 725.51 | 705.94 | −2.7% | 🔴 distribution |
| **SPY** | 754.95 | 750.72 | **−0.56%** | ← **the tell: the index barely moved** |
| **XLF** | 55.71 | **56.75** | **+1.9%** | 🟢 OBV **accumulation**, RS20 +4.4% |
| **XLE** | 55.08 | **57.02** | **+3.5%** | XOP RS20 +5.8% |
| **CL=F** | 71.41 | **78.69** | **+10.2%** | The Hormuz squeeze **fired** |
| GEV | 1091.57 | 1036.22 | −5.1% | AI-power sold *with* semis |
| LMT | 523.22 | 513.52 | −1.9% | RS60 −17.6%, volume **0.58×** — no interest |
| ^VIX | 15.03 | **17.95** (07-17) | **+19.4%** | Rising, not panicking |

Semis −7% against SPY −0.6% is money **moving between sectors**, not leaving equities. That distinction
is the whole rotation call in §4.

### The primaries [FRED, asof dates explicit — freshness flagged, not assumed]
| Series | Latest | Trend | Read |
|---|---|---|---|
| Fed funds | **3.63%** (07-15) | flat (3.64) | Easing cycle mature, on hold |
| US 10Y | **4.55%** (07-15) | 4.58 prev · 4.48 @06-12 · 4.12 @2025-12-29 | Long end **relieved** from 07-13's 4.62 but structurally +43bp/120d |
| US 2Y | **4.13%** (07-15) | 4.18 prev · 3.45 start | Front end falling faster than the long end |
| **2s10s** | **+42bp** | was **+36bp** in the 07-15 report | **Steepened further** — P1's engine |
| Real 10Y | **2.32%** (07-15) | 2.17 @06-12 · 1.90 start | **+42bp/120d** — real yields still the driver |
| Core CPI idx | 336.065 (**Jun**) | 336.121 prev → **level dipped m/m** | Confirms the cool June print |
| CPI idx | 332.568 (**Jun**) | 333.979 prev → **fell m/m** | Realized disinflation is real |
| Unemployment | 4.2% (**Jun**) | 4.3 → 4.2 | Labor firm, no recession signal |
| DXY | 120.50 (**07-10**) | ⚠ **7 days stale** | Do not treat as current |
| VIX | 15.67 (07-15) | ⚠ **stale** — live ^VIX **17.95** (07-17, +7.3%) | Use the live print, not FRED's |
| M2 | $23,052B (**May**) | expanding | Liquidity tailwind |

⚠ **Freshness discipline:** CPI · Core CPI · Unemployment · M2 are monthly (**June/May data, ~1mo lag**) —
they describe a world before this week's selloff. DXY is 7d stale and FRED's VIX misses today's +7.3%.
The only *current* macro facts here are the daily curve prints and the tape.

**Warsh Fed (carried from 07-15):** velocity **307 hits/7d**, more than double the 145 at which it entered
the term table. His "inflation will be a thing of the past — the AI investment boom is disinflationary"
framing now sits *against* a market repricing that same AI boom as a cost. Noted; not yet a proposition.

---

## §2 Positioning — CFTC COT [us_flow --cot; Tue-close 07-14, 3–4d lag → context, NOT a trigger]
| Instrument | Net spec | Wk Δ | 1Y %ile | Tag |
|---|---|---|---|---|
| **Nasdaq-100** | −8,741 | **+9,502▲** | **4%ile** | 🔴 crowded-SHORT |
| **WTI Crude** | +20,922 | −2,794▼ | **13%ile** | 🔴 crowded-SHORT |
| Nat Gas | −165,307 | +5,496▲ | 16%ile | 🔴 crowded-short |
| **Copper** | +64,272 | −516▼ | **95%ile** | 🟢 crowded-LONG (overheated) |
| S&P 500 | −42,891 | −5,299▼ | 77%ile | 🟡 neutral |
| USD Index | +13,269 | +253▲ | 60%ile | 🟡 |
| Gold / Silver | +194,246 / +28,015 | — | 27% / 45%ile | 🟡 |
| UST 10Y / 2Y | −814,262 / −1,261,008 | — | 26% / 32%ile | 🟡 |
| Russell 2000 | −887 | −963▼ | 62%ile | 🟡 |

### ★ The lesson this run paid for (→ §5 failure class 2)
Two identical signals, opposite outcomes:
- **Nasdaq 4%ile crowded-short** → 07-15 called it "squeeze fuel" and promoted **IT to OW** → QQQ **−2.7%**, SMH **−6.9%**.
- **WTI 13%ile crowded-short** → 07-15 called it squeeze fuel → CL=F **+10.2%**. ✅

The difference is **a catalyst existed for one and not the other**: Hormuz lit the WTI short; Nasdaq had no
igniter, and TSMC's capex print was an active *de*-igniter. The COT tool states this itself
("extreme percentile = contrarian ammunition, not a confirmed direction"). Positioning is **ammunition,
not a trigger** — and both crowded-shorts are *still* loaded (Nasdaq 4%ile, WTI 13%ile).

---

## §3 Narrative velocity — 7-bucket sweep [fts, foreign, 7d, OR-mode + `--syn`, terms as separate argv]
| Rank | Bucket | 7d count | Note |
|---|---|---|---|
| **1** | **Banks / financials** | **3,643** | **New #1** (was 1,581 on 07-15) — earnings week is the loudest story on the tape |
| 2 | Tariff / trade / China | 2,921 | Persistent overhang; see the P6 truce risk below |
| 3 | AI / datacenter / power | 2,312 | Loud but **now being repriced**, not celebrated |
| 4 | Rates / Fed / inflation | 2,246 | Warsh 307 |
| 5 | Oil / energy / Hormuz | 1,840 | War-premium **realized** (+10.2%) |
| 6 | Semis / chips | 1,165 | The selloff's subject |
| 7 | Defense / geopolitics | 771 | Quietest — and the primes are not moving (§4a P4) |

⚠ **Comparability caveat:** the 07-15 run's bucket argv were not recorded verbatim, so cross-run deltas
are **directional only, not exact**. The FIN jump is large enough to survive that caveat; the AI bucket's
apparent 3,413→2,312 drop is **not** trustworthy as a precise number. *(Fix forward: record bucket argv.)*

### Event axis — the day's full denominator [`brief --date 2026-07-17 --scope foreign --body 2`]
**320 articles → 194 clusters → 31 events. head 0 · body 31 · tail 0 · nonmarket 0.**
**Every one of the 31 event lines was read** (tail = 0, so nothing was sampled away). `nb` is null
throughout — market/non-market filtering is domestic-only and this is a foreign scope, so nothing was
silently excluded. The regime-relevant lines, with their outlet counts:
- [3a/2s] *Asian shares sink, with Tokyo down nearly 5% as slumping AI stocks drag world markets lower*
- [3a/2s] *Chip Stock Selloff Deepens in Asia as TSMC Fails to Impress*
- [2a/2s] *Asian stock markets mirror US tech sell-off, Nikkei plunges over 4%*
- [2a/2s] *Micron has turned into "the most important stock in the market." So is it time to worry?*
- [2a/2s] *Investors Can't Shake AI Bubble Fears—But They're Not Dropping Their Favorite Tech Stocks*
- [2a/2s] *Retail Sales Rise For Fifth Straight Month* — consumer resilient (DISC input)
- [4a/2s] *Trump Accuses China of Election Meddling, Threatening Truce* — see P6
- [2a/2s] *TSLA Stock Slips Overnight: Gary Black Says SpaceX Can't Afford Tesla* — 07-22 binary input
- [3a/3s] *Intel's AI-Driven Data Center Growth Set To Power Second Quarter Earnings* — the counter-line

⚠ **The whole regime story sat at 2 outlets.** Head was **empty** (0 events at ≥5 outlets); every line
above lives in the body. At the default `--body 3` this run would have seen **nothing** and reported a
quiet day. `--body 2` is what made this report possible — the L1's warning is confirmed a second time.

### Blindspot pass [19,558-article window, 6,845 random sample, token-0 emergent terms]
- **SpaceX 372** — a **rank jump** with no fixed-set term behind it. The event tape explains it:
  *"Gary Black Says SpaceX Can't Afford Tesla — 'The Math Won't Pass Muster'"* → a funding-structure doubt
  landing **5 days before TSLA earnings (07-22 binary)**. **New term.**
- **Iran 552** — 4th-ranked emergent term, consistent with crude +10.2%. The oil bid is real, not narrative-only.
- **`moratorium` collapsed to 17 hits/7d** (it was 07-15's named AI-power kill-switch). **It never fired** —
  and the AI-power leg fell 5% anyway, for an entirely different reason. → §5 failure class 3.
- **`AI bubble`**: ⚪ECHO, but **accel 1.52×**, 150 hits/90d — an old fear re-accelerating into the selloff.
- **`TSMC`**: 🟡**ACCELERATING**, **accel 2.39×**, 427 hits — the loudest *new* thing on the board.
- **`Hormuz`**: ⚪ECHO, accel 1.15× (was 🔴FADING at 0.39× on 07-15 — see §5 failure class 4).
- **Living term-table additions:** `capex concerns` · `high bar` · `AI bubble` · `SpaceX` · `election meddling`.

---

## §4 ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)
> Wind direction only, one line per GICS sector. Not equal-weight analysis. Proposition IDs in §4a.

| # | GICS Sector | Tilt | Δ vs 07-15 | Driving prop | One-line why |
|---|---|---|---|---|---|
| 1 | **Financials (FIN)** | **OW** | = OW | P1, P5 | 2s10s **+42bp** steepening + Citizens/M&T Q2 beats + **XLF +1.9% while QQQ −2.7%**, OBV accumulating. Loudest bucket (3,643). The one thesis working on both news and tape |
| 2 | **Energy (ENRG)** | **OW** | ↑ from tactical OW | P3 | **CL=F +10.2%/5d realized**; XLE +3.5%, XOP RS20 +5.8%; WTI **still 13%ile** = fuel remains. ⚠ TACO-reversible in a session |
| 3 | **Information Tech (IT)** | **UW** | **↓↓ from OW** | P2 | **The capex sign-flip.** SMH −6.9%, MU −12.9%, TSM distributing on 1.13× volume. The 4%ile short did not save it |
| 4 | **Comm Services (COMM)** | **Neutral→UW** | ↓ from modest OW | P2 | Meta/Alphabet AI-capex now reads as cost, not growth; **NFLX prints today (binary)** |
| 5 | **Industrials (INDU)** | **Neutral** | **↓ from OW** | P2, P4 | Both legs that justified OW have failed: AI-power **GEV −5.1%** (sign-flip) and defense **LMT −1.9%, RS60 −17.6%, vol 0.58×** |
| 6 | **Utilities (UTIL)** | Neutral | = | P1, P2 | AI-power demand story is exactly what's being repriced; mild rate relief offsets. No wind |
| 7 | **Health Care (HLTH)** | Neutral | = | — | No wind; defensive ballast, plausible rotation destination |
| 8 | **Consumer Staples (STPL)** | Neutral | ↑ from UW | P2 | Rotation out of growth gives defensives a bid — but SPY −0.56% says this is **not** risk-off, so no OW |
| 9 | **Consumer Disc (DISC)** | Neutral | = | P1 | **Retail sales up a 5th straight month** [2 outlets] = consumer firm; offset by TSLA 07-22 binary + SpaceX funding doubt |
| 10 | **Materials (MATR)** | **UW** | = UW | P1, P6 | **Copper still 95%ile crowded-long** = overheated; dollar (stale 120.50) a headwind; China-truce risk |
| 11 | **Real Estate (RE)** | **UW** | = UW | P1 | **Real 10Y 2.32%, +42bp/120d** — the structural long end, not the cool CPI, sets this sector's cost |

**Net wind:** out of the AI complex (IT/COMM/INDU-power), into **FIN + ENRG**. The rotation is
*intra-equity*, not a de-risking — SPY −0.56% is the constraint on how far to push a defensive read.

### §4a Falsifiable propositions (both branches mandatory on oscillating variables)

- **P1 — Rates/curve bull-steepener → FIN OW, RE/MATR UW.**
  Evidence: 2s10s **+36bp → +42bp**; 2Y 4.18→4.13 falling faster than 10Y 4.58→4.55; real 10Y 2.32%.
  **Anti-signal:** **oil +10.2% is itself an inflation impulse** — if it feeds breakevens, or the next
  CPI/PPI runs hot, the long end sells off, **real 10Y > 2.50%**, and FIN's steepener gain is swamped by
  duration losses in AFS books. ⚠ **This branch is live, not hypothetical — the trigger has already moved.**
  **Track:** real 10Y (2.32 now), 2s10s (+42bp), next CPI print. **Catalyst:** [blank] — next CPI date not
  in CATALYST_WATCH; do not guess it.

- **P2 — ★ AI capex sign-flip (this run's core, NEW).**
  *The market has inverted the sign on AI capex. TSMC delivered record profit + raised guidance + $100bn
  more US expansion and the complex sold off on "capex concerns" / "a high bar". If capex now reads as
  cost rather than demand, the whole chain de-rates together — which is what the tape shows: SMH −6.9%,
  MU −12.9%, GEV −5.1%, VRT RS60 −12.4% (the capex **recipients** fell with the spender). → UW IT/COMM,
  INDU-power loses its bid.*
  **Anti-signal (mandatory):** NVDA/MSFT/META print and raised capex is **rewarded** (stock up on the
  capex line), **OR** MU holds above its 07-16 close (**853.20**) and SMH RS20 turns positive → then this
  was a TSMC-specific "high bar" event, not a regime change, and the **Nasdaq 4%ile crowded-short becomes
  squeeze fuel after all** (it is still loaded).
  **Track KPI:** MU **853.20** (the line), SMH RS20 (−7.7% now), NVDA's reaction to the next capex headline.
  **Catalyst:** NFLX today · TSLA 07-22 · Intel Q2 (dated [blank] — the *"Intel's AI-Driven Data Center
  Growth Set To Power Q2"* [3a/3s] line is the live counter-thesis).
  ⚠ Oscillating-variable discipline: this is precisely the class §5 says we get wrong one-way. **Both
  branches are stated and the falsifying price is named.**

- **P3 — Oil war-premium (CONTINUED — now realized).**
  *Hormuz × WTI 13%ile crowded-short squeezed: CL=F 71.41 → 78.69 (**+10.2%/5d**), XLE +3.5%. Still
  13%ile → ammunition remains.*
  **Anti (equal weight):** the **TACO trigger** — Iran declares the strait open (undated, live in
  CATALYST_WATCH) → crude gaps down, the crowded short covers into the relief, ENRG round-trips in a
  single session. A one-way tilt here is the exact violation PREMORTEM exists to prevent.
  **Track:** CL=F (78.69), Hormuz transit rate, theme-age (⚪ECHO 1.15×).

- **P4 — Defense structural (RETIRED to watch-only — 3rd consecutive failure).**
  *06-22 and 07-15 both predicted de-rated primes re-rate on Hormuz escalation. Realized with oil **+10.2%**
  and Iran the #4 emergent term: **LMT −1.9%/5d, RS60 −17.6%, OBV distributing, volume 0.58× (no interest)**.*
  → **The war-premium transmits to CRUDE, not to the primes.** The thesis has now been given three runs and
  a near-ideal catalyst, and has not fired. **Demoted out of the matrix as a driver.**
  **Revival condition (falsifiable):** LMT/NOC/GD volume surge **>1.3×** on an appropriations or NATO order.

- **P5 — Bank earnings leg (CONTINUED — compounding).**
  *Citizens Financial Q2 beat on private-bank growth; M&T GAAP EPS **$5.32, beat by $0.66** [SeekingAlpha
  07-15/16]. XLF OBV accumulating, RS20 +4.4%. Velocity #1 (3,643).*
  **Anti:** credit-cost / NIM disappointment in the regionals, or **SCHW misses on 07-21 (binary)** → the
  leg breaks and FIN's OW loses its earnings pillar. **Track:** SCHW 07-21, loan-loss commentary.

- **P6 — China truce risk (NEW — ⚠ NOT yet a proposition: the denominator forbids it).**
  *"Trump Accuses China of Election Meddling, Threatening Truce" [Bloomberg 07-17].* **Denominator:
  `China`+`truce` = 6 hits/3d; `"election meddling"` = **2 hits, 2 outlets** (Bloomberg, BBC).*
  Per P4 (know-before-you-speak), **2 outlets does not support a macro proposition** — it is logged as a
  **watch**, not a driver, and no sector tilt rests on it.
  **Promotion condition:** >20 hits/3d or a Chinese retaliation headline → tariff re-escalation → UW the
  China-exposed complex (IT/semis already UW; MATR, DISC follow).

---

## §5 Self-backtest — scoring the 07-15 propositions at +2d

| 07-15 proposition | Realized by 07-17 | Score |
|---|---|---|
| **P1** bull-steepener → FIN OW, RE/MATR UW | 2s10s +36→**+42bp**; XLF **+1.9%** vs QQQ −2.7%, OBV accumulating | **HIT** |
| **P5** bank earnings leg (GS/JPM crush) | Citizens + M&T Q2 beats; FIN now the #1 velocity bucket | **HIT** |
| **P6** oil war-premium × WTI 13%ile short | **CL=F +10.2%/5d**, XLE +3.5% | **HIT** |
| **P2** dovish Warsh → risk-on, IT/growth re-rate | IT sold off hard: SMH −6.9%, MU −12.9% | **MISS** |
| **P3** AI-power capex intact → INDU/IT/COMM | GEV −5.1%, VRT RS60 −12.4% | **MISS** |
| **P4** defense primes re-rate | LMT −1.9%, RS60 −17.6%, vol 0.58× — with a perfect catalyst | **MISS** (3rd → retired) |
| **IT promoted to OW** (the 07-14 postmortem "correction") | The correction **over-corrected** into the top | **MISS** |

**Running hit-rate: 3 HIT / 4 MISS = 43% (n=7, scored at +2d).**
Prior run's scorecard (07-15 grading 06-22) was 2 HALF / 2 MISS-acknowledged / 1 OPEN — no clean hits.
So: **the rates/banks/oil axis is working (3/3); the AI-complex axis is not (0/3).**

### Recurring failure classes — one carried, three new
1. **(carried, now WORKING)** *One-sided reads of oscillating variables.* P6-oil carried both branches by
   design → it hit. Keep.
2. **★ NEW — extreme positioning treated as a directional trigger.** Nasdaq 4%ile "squeeze fuel" → OW IT
   → −2.7%. WTI 13%ile → +10.2%. Same signal, opposite results; the difference was **a catalyst**.
   **New rule: positioning may only AMPLIFY a proposition that already has its own catalyst. It may never
   BE the proposition.** (§4a P2 obeys this — the sign-flip rests on TSMC's print, not on the 4%ile.)
3. **★ NEW — watching the wrong kill-switch.** 07-15 named `moratorium` as the AI-power anti-signal. The
   leg fell 5% and **moratorium velocity collapsed to 17 hits** — it never fired. The actual killer (the
   capex sign-flip) was **unnamed**. **New rule: an anti-signal must be the mechanism most likely to kill
   the thesis, not the most recently-read headline.**
4. **★ NEW — news velocity ≠ price on supply-shock assets.** 07-15's DRIFT read Hormuz at 🔴FADING
   (accel 0.39×) and inferred *"TACO-down risk rising"*. Crude then went **+10.2%**. A blockade's *price*
   does not need fresh *headlines* — the supply is constrained whether or not editors re-file. **New rule:
   for supply-shock assets, price is the primary and theme-age is the corroborant, never the reverse.**

### §5 DRIFT stamp (append-only — populated by stage 8)

## §5 ADDENDUM — DRIFT (2026-07-17, post-run) · append-only
> **Append-only by rule: nothing above this line was edited.** The original call stays visible next to its
> correction — that asymmetry is the self-backtest's food.

### ⚠ Tooling note (P6): `drift_watch.py` could not run on this client
`scripts/drift_watch.py` opens the server-owned DB **directly** (`line 34 FTS_DB = data/news_fts.db`;
`line 94 sqlite3.connect(FTS_DB)`) with **no `DEGAJA_NEWS_API` branch**. The client's local news DB is
deliberately absent (P6 — API-first; only `news_alert.db-wal/-shm` remain), so it exited at line 76:
*"news_fts.db none"*. **The DRIFT stage's own tool is unusable on the machine the stage runs on.** Filed as
a repo task. **Worked around via the API-routed equivalent** (`burst` **is** in `DB_READ_CMDS` and is
served by `/exec`):
```
python -X utf8 -m module_news_data burst --date 2026-07-17 --scope foreign --top 25
```

### Burst scan result — **no 🚨 regime flip. The report does not lie overnight.**
Denominator: **389 foreign articles**, baseline 30d, market-relevance ≥40%, universe 665 companies, field=title.
**Category ② ("words that never appear normally") returned `(none)` — zero unknown-word emergence.**

| Burst | z | n / outlets | distributing | Body-read verdict |
|---|---|---|---|---|
| **INTUITIVE** | **12.4** ← the run's biggest | 3 / 2 | 0.92 | **Body-read. SUPPORTS the HLTH OW — does not flip it.** ISRG (Intuitive Surgical, Health Care Equipment, $144B) printed Q2 **07-15** (consensus EPS $2.50, **+14.2% Y/Y**) and is **+3.55% on 07-17** while sitting **−35% off its 2025 all-time high** [Yahoo/SeekingAlpha 07-15/17]. Flow: **OBV accumulating, vol_surge 1.45×, delta +0.27** — a beaten-down medtech **being bought**, i.e. money still arriving in HLTH *the day after* the sweep's 07-16 asof. ⚠ **Honest caveat:** ISRG's **RS20 −3.6% / RS60 −19.5%** shows Health Care Equipment holds badly-lagging names — it does **not** contradict DEEP·HLTH's "all 8 sub-industries flow-positive" (ISRG flow_score **+0.327**), but it does temper "broad strength" into "broad *accumulation*, uneven *performance*". |
| NETFLIX | 5.9 | 5 / 3 | 0.86 | **No action — already 🔴RESOLVED and DROPPED** in ALPHA (printed 07-16, disappointed). The burst is post-print coverage of a binary this run already retired. Consistent. |
| AAPL | 4.4 | 3 / **1** | **0.00** | **NOT a real burst — distributing 0.00 = single-outlet echo.** One desk repeating itself is not editors independently judging news. Logged, no action. |
| TSMC | 2.9 | 5 / 3 | 0.96 | **No change — it is already this run's core** (§1 wedge, P2′). A 2.9σ burst on the story the whole report is about is confirmation, not drift. |
| FUTURES / JONES | 2.2 / 2.0 | 4 / 3 | — | Generic market vocabulary. No signal. |

### Kill-switch proximity — the two live ones, restated
1. **P2′ (capital-intensity de-rate):** **MU's line is $853.20 — its actual last print.** This test is live
   *right now*, not hypothetical. Flip → verdict (a), the broad sign-flip. ⚠ Unresolved contradiction
   carried forward: **NVDA short-vol z +1.67 (spike), shorts building** while price holds.
2. **P3/ENRG (crack leg):** the anti-signal is **Russian refining capacity coming back online** — *not*
   Hormuz. DEEP·ENRG verified the driver is **Russian refinery destruction (Afipsky, Syzran) + the diesel
   export ban**, mechanically **independent of the strait**. ⚠ **This corrects §4a P3 as written above**,
   which framed ENRG purely as an oil-war-premium bet: the *durable* part of the ENRG OW is **not** the oil
   premium at all. (Original text left standing above, per append-only.)

### Corrections this stage makes to the report above (stated, not silently patched)
- **§0 listed NFLX as a forward "D-0 binary". It was stale — NFLX printed 07-16.** The catalyst calendar's
  earnings dates are **pattern-estimates**; `next_earnings_date` disagreed on **KMI (07-22 → actually 07-23)**
  and surfaced **UNH (07-16, printed)**, **DHR (07-21)** and **TMO (07-23)** which the calendar carried **not at all**.
- **§4a P4 retired the defense proposition too broadly.** The failed leg is the **platform primes**
  (LMT/NOC/GD); **RTX is a separate leg**, correctly bifurcated on 07-15, held at 9.9%, still 🟡NEUTRAL.
- **§4/§4a's P2 was narrowed to P2′** by PREMORTEM and confirmed by DEEP·SEMI (verdict **(b)**).
- **§2's "✅ no cycle GAP" (via Stage 2) was an artifact** — the rank-2 Energy cycle is an unconfigured stub
  (`min_epicenter_pct = 0.0` → unsatisfiable; `core_pick = None`). **The Energy epicenter GAP is REAL** and
  the book holds **0.0%** of it.

**DRIFT EXIT CHECK:** ✅ drift run (via the API-routed `burst` after `drift_watch.py` proved unusable —
tooling defect filed, not hidden) · ✅ **every flagged item body-read, not counted** (INTUITIVE drilled to
article bodies; AAPL rejected on distributing 0.00) · ✅ **§5 ADDENDUM appended, append-only — no line above was
rewritten** · ✅ **no 🚨 regime flip: the report stands.**

---
**EXIT CHECK:** ✅ catalysts injected (5 binaries, NFLX ≤48h → PREMORTEM) · ✅ events read via `--body 2`
with **tail = 0, all 31 lines read**, denominator 320→194→31 cited · ✅ 7-bucket sweep run with **terms as
separate argv** (every bucket non-zero: 3,643/2,921/2,312/2,246/1,840/1,165/771 — no silent-zero) ·
✅ blindspot pass, `sample[]` + emergent terms read raw, new terms folded into the table · ✅ indicators
(FRED primaries with freshness flags + COT positioning) · ✅ continuity anchor (07-15 MACRO_REPORT) read;
handoff ledger absent — mode stated in the header · ✅ **11-sector transmission matrix** produced ·
✅ self-backtest scored with running hit-rate (3/7) + 3 new failure classes.
**→ proceed to SWEEP.**
