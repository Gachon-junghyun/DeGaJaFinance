# PREFLIGHT — 2026-08-10 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run time KST 2026-08-10 (US market closed; Mon 08-10 KST = pre-open Mon US) · sweep data **asof 2026-08-07** (last US close, Friday).
>
> ⚠ **Filename deviation, logged:** the composition table names this `preflight/PREFLIGHT.md`, but
> `PREFLIGHT.md` in this folder is **today's KR run's** rights table (written 08:26 KST). Overwriting a
> sibling desk's output is not a correction, so this US table is written as `PREFLIGHT_US.md` in the same
> folder. Human decision pending on whether the path should be market-suffixed permanently.

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| G1 news axis alive | 🔴 **FAIL** | Coverage **16.0% then 0.0%** on two runs 12 min apart — while the direct probe returns **3,321** Nvidia hits/7d. Not silence: **a flapping pipe** |
| G2 scoring-scale continuity | 🔴 **FAIL** | Mode guard held (3-axis vs 3-axis) but the matched baseline is a **5-ticker scratch snapshot from 2026-07-20** — Δ is being printed against an 18-day-old, 1.7%-complete run |
| G3 who owns the sector sign | 🟢 **PASS** | Flipper list printed — **1 of 11** sectors (Materials / LIN) |
| G4 risk-unit stability | 🔴 **FAIL** | 250d **8 units** vs 500d/750d **7 units** — NVDA membership splits by window |
| G5 does the universe cover the book | 🔴 **FAIL** | **2 of 8** US holdings outside `us_top300` (**LNG · TSM**, 11th consecutive run) + universe **26 days** old (limit ≤8) |
| G6 estimate-snapshot accrual | 🔴 **FAIL** | Measured ETA **94 days** vs ideal 33 = **2.85×** |
| G7 tool liveness | 🟡 **FAIL→probed** | 31 entry points, **30 exit 0**; `module_chart` exits 1 on `--help` but its functional probe is clean |

**PASS 1 / FAIL 6.** Today this desk cannot speak in **news velocity · Δflow · "new 🟢" · single-number
concentration · `--ic`-grounded size · flow reads on LNG/TSM**.

---

## G1 · News axis alive — 🔴 FAIL

**Command**
- `SECTOR_FLOW_US.json §scoring` → `{"vel_axis": false, "vel_coverage": 0.0, "n_axes": 3, "scored": 299, "dropped_missing_axis": 1}`
- Falsification probe, actually executed: `python -X utf8 -m module_news_data fts search <q> --days 7 --count --scope foreign`

**Numbers**

| Item | Value |
|---|---|
| velocity measured — sweep run A (08:47 KST) | **48 / 300 = 16.0%** (threshold 80%) |
| velocity measured — sweep run B (09:01 KST, same prices, cached) | **0 / 300 = 0.0%** |
| Axis decision | velocity axis **excluded** → all names scored on **3 axes** |
| Names unscored (axis missing) | 1 (excluded from aggregation) |
| Probe `Nvidia` 7d `--scope foreign` | **3,321** |
| Probe `tariff` 7d | **1,439** |
| Probe `Federal Reserve` 7d | **1,119** |
| Probe `natural gas` 7d | **731** |
| Probe `Broadcom` 7d | **306** |
| News path | NEWS API `https://impolite-coherent-props.ngrok-free.dev` — responds |

**★ This is the point of the gate.** Writing "16% coverage means US names have no news" fails EXIT.
The probe answers that the same universe of names is **sitting in the pool in the thousands**. The
sweep's velocity lookup returned `None` for 252–300 names, and that is **not "no articles" — it is
"not counted."**
New this run, sharper than the KR table's version of the same defect: **two sweeps of the same
tickers on the same cached prices, twelve minutes apart, measured 16.0% and then 0.0%.** A pipe that
returns a different coverage each call while the pool is unchanged is **non-deterministic**, which
settles the ambiguity — the fault is in the sweep's velocity call path (remote hop / rate limit /
timeout), not in collection, indexing, or the API.

**Second-order contamination, measured.** The flapping does not stop at the dropped axis — the
`flow_read` authoritative **tag** still consults news. Same day, same prices, two runs:

| | run A | run B (this run's JSON) |
|---|---|---|
| 🟢 accelerating | **23** | **15** |
| 🔴 distributing | 77 | 76 |

**8 names moved out of the 🟢 bucket with zero price change.** The 🟢 bucket is therefore not a stable
object today.

**🚫 Rights revoked today**
1. **No citation of news velocity (`vel`)** — every stage (SWEEP · EVENT_ALPHA · ROTATION · DEEP · BET).
2. **No "this theme is fresh / this theme has gone cold" call.** The freshness axis does not exist today.
3. **No "it's quiet" as evidence.** Today's silence is the instrument's, not the market's.
4. `flow_score` is cited **as a 3-axis score**, and that fact goes **on the same line** as the conclusion.
5. **No 🟢/🔴 headcount, breadth, or bucket-membership claim treated as stable to ±8 names** — quote it
   with the run it came from.

*Repair is not this stage's job (rule 1) → `idle_probe` or a human-approved item.*

---

## G2 · Scoring-scale continuity — 🔴 FAIL

**Command** `§scoring.n_axes` vs `llm_outputs/sector_flow/history.json` previous same-mode snapshot.

Full US history ledger (18 snapshots):

| snapshot | `_mode` | tickers stored |
|---|---|---|
| 2026-07-14 … 07-17 | news | 300 each |
| **2026-07-20** | **nonews** | **5** |
| 2026-07-21 … 08-06 (13 snapshots) | news | 300 each |
| **2026-08-07 (this run)** | **nonews** | **299** |

`prev_snapshot()` correctly refuses cross-mode subtraction — so it skipped all thirteen 300-name
`news` snapshots and matched **2026-07-20**, the only other `nonews` entry, which holds **5 tickers**
(`AAPL·GOOG·GOOGL·MSFT·NVDA` — the residue of a `--tickers` scratch run that got persisted into the
shared history file).

Consequence, measured in this run's own output:
- **names carrying a Δ: 5 of 299** (1.7%). The remaining 294 are `null`.
- **sectors carrying a Δ: 2 of 11** — Information Technology `▼0.134`, Communication Services `▲0.31`.
  Both are driven entirely by those five megacaps.
- The printed line `Δ상승: NVDA ▲0.95, GOOG ▲0.34, GOOGL ▲0.30, MSFT ▲0.16, AAPL ▼0.63` reads as
  day-over-day. It is **18 calendar days** over, against a 1.7%-complete baseline.
- The `신규🟢 (first acceleration today)` list from run A — PLTR, SHOP, EMR, TRI, PH, BMY, COHR, DIS,
  AMGN, AME, WAT, EA — is **an artifact**: against a 5-name baseline, every other name is trivially "new."

The mode guard did its job; what is missing is a **recency + completeness guard on the matched
snapshot**. Nothing in the output says the baseline was 18 days old and 5 names wide — the numbers
came out looking ordinary. That is this preflight's founding failure class, reproduced.

**🚫 Rights revoked today**
1. **No Δflow citation at all** (SWEEP · ROTATION), including the two sector Δs that printed.
2. **No "new 🟢 / first acceleration today"** anywhere. That list is baseline-artifact.
3. ROTATION speaks in **levels only** — wflow · eqflow · breadth. **Not in change.**
4. Any promotion/demotion argued from "IT flow deteriorated / Comm improved" is **void today**.

---

## G3 · Who owns the sector sign — 🟢 PASS

**Command** `§sector_rotation[].top1_flips_sign` — does a list print (0 is a valid list).

**1 of 11 sectors** flips sign when its largest name is removed. Recorded in full:

| Sector | wflow | ex-top1 | top1 | n |
|---|---|---|---|---|
| Materials | **−0.038** | **+0.173** | LIN (Linde, 24.7% of sector cap) | 12 |

All other ten sectors keep their sign ex-top1. For the record, the ex-top1 values that move most in
magnitude without flipping: Consumer Discretionary (−0.033 → **−0.273**, AMZN), Energy (+0.286 →
+0.151, XOM), Industrials (+0.041 → +0.105, CAT), IT (−0.008 → −0.110, NVDA).

Gate **PASSES** (the list printed). Its content still binds ROTATION:
**Materials may not be promoted or demoted on wflow today** — use eqflow (+0.040) / breadth (0/12) or hold.
Note the two readings disagree in sign, which is the whole point of the gate.

*Caveat carried from G5: `top1_weight` is computed off a 26-day-old market-cap column.*

---

## G4 · Risk-unit stability — 🔴 FAIL

**Command** `python -X utf8 scripts/risk_units.py --book --days {250,500,750}` — **all three actually run.**

| --days | trading days after align | units | within-group residual corr | ARI (first half vs second) |
|---|---|---|---|---|
| 250 | 249 | **8** | +0.4345 | 0.6565 |
| 500 | 499 | **7** | +0.4464 | 0.5424 |
| 750 | 749 | **7** | +0.4389 | 1.0 |

**The split is at exactly one name — `NVDA`:**
- 250d: `U0 = {AVGO, TSM}` · `U5 = {NVDA}` (**separate**)
- 500d · 750d: `U0 = {AVGO, NVDA, TSM}` (**merged**)

The other six units (`{KMI,LNG}` · `{009150}` · `{096770}` · `{MA}` · `{RTX}` · `{VST}`) are identical
across all three windows. ⇒ grouping **disagrees** → FAIL. The tool itself warned at 250d that the
sample (249 days) is shorter than requested and that *short samples invent structure (S5)*, and ARI
swings 0.54 → 1.0 across windows. Threshold sensitivity also shows the choice is near a boundary:
at 250d, `dist 0.75` collapses 8 units → 7.

**🚫 Rights revoked today**
1. **No single-number concentration guard** (SIZE · BET).
2. Whenever concentration is stated, the `--days` used goes **on the same line** as the conclusion.
3. **Whether `AVGO/NVDA/TSM` is one unit or two is decided by the window** — neither may be asserted today.

*Side observation (not a verdict): the tool warned each window that the benchmark is `SPY` while the two
KR positions are KRW local returns, so a common FX factor may be injected.*

---

## G5 · Does the universe cover the book — 🔴 FAIL

**Command** builder invariant recomputed (`data/us_universe/us_top300.csv` × `module_paper_book status`).

| Item | Value |
|---|---|
| Book positions | 10 (US 8 · KR 2) |
| **US holdings outside `us_top300`** | **2 🚨 `LNG` · `TSM`** — logged, not fixed, for **11 consecutive runs** |
| US holdings outside `us_all_v2_candidate.csv` (1,522 names, built today 00:53) | **0** — the fix exists, it is just not the file the sweep reads |
| `us_top300.csv` age | **26 days** (mtime 2026-07-15; limit **≤8**) → 🔴 |
| Sweep scale | 300 requested / **299 scored** (1 dropped, axis missing) |
| KR holdings in `kr_all` | 2/2 ✅ (out of scope for this desk) |

The sweep logged it itself on line 1: `[warn] 유니버스 us_top300.csv 26일 경과 — 시총 stale.`

Worth stating precisely, because it changes what kind of failure this is: a **1,522-name candidate
universe containing both LNG and TSM was rebuilt today at 00:53**. The book's blind spot is no longer
a data gap — it is a **wiring gap** between `us_all_v2_candidate.csv` and what `sector_flow --market us`
loads. (Naming it is this stage's job; changing the wiring is not — rule 1.)

**🚫 Rights revoked today**
1. **No flow / RS / OBV / short-pressure verdict on `LNG` or `TSM`** (SWEEP · BET · DEEP). Where they
   come up, the line reads **"not measured,"** never "no signal."
2. **wflow may not be described as "current market cap"** — the weights are 26 days old, and so is
   every `top1_weight` in G3.
3. The one unscored name may not be characterized at all.

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL

**Command** `python -X utf8 scripts/snapshot_estimates.py --status`

| Item | Value |
|---|---|
| Accrued | **7 files / 20 calendar days** (2026-07-22 → 2026-08-10), 120 names each |
| Measured rate | **0.35 files/day** (ideal 1.0) |
| To the 40-day target | ideal **33 days** vs measured **≈94 days** = **2.85×** (limit 1.5×) |
| Gaps (days) | [2, 3, 4, 6, 3, 1] · median 3 · max 6 |

The tool printed its own trap warning: *"counted as 'number of files' this instrument looks healthy (D16)."*
Not recoverable retroactively — days not accrued are gone.

**🚫 Rights revoked today**
1. **`kelly_size --ic` output may not be reported as a grounded size** (SIZE).
2. Any size written today is labeled **"mechanical 1/4"**. Calling it IC-based fails EXIT.

---

## G7 · Tool liveness — 🟡 FAIL on 1 of 31, probed back

**Command** `--help` on every entry point this run will use; exit code checked.

**exit 0 — 30 entry points**
`sector_flow.py` · `us_live_shortlist.py` · `us_flow.py` · `flow_read.py` · `cycle_exposure.py` ·
`catalyst_calendar.py` · `drift_watch.py` · `action_bracket.py` · `exposure_rule.py` · `risk_units.py` ·
`kelly_size.py` · `report_lint.py` · `missed_ledger.py` · `reject_ledger.py` · `us_setup_screener.py` ·
`axis_window_flow.py` · `axis_inflection.py` · `snapshot_estimates.py` · `module_macro_us` ·
`module_news_data` · `module_paper_book` · `module_watchlist` · `module_report_tags` ·
`module_business_us` · `module_disclosure_us` · `module_fundamentals_us` · `module_valuation` ·
`module_flow` · `module_industry_map` · `module_epistemics`

**exit 1 — 1 entry point**

| Tool | Why `--help` failed | Functional probe (rule 3: don't manufacture UNKNOWN — measure) |
|---|---|---|
| `module_chart` | **CLI does not implement `--help`** — prints `usage: python -m module_text_chart <ticker> [--read]` then exits 1 | `module_chart NVDA --read` → **exit 0, clean**: OBV accumulating (20d slope +46%), no divergence, MA mixed/price above 4 of 4, Bollinger expanding 16.7% at upper band, RSI 65.6, turn verdict CONFIRMED-TURN, stop 190.01 |

**🚫 / ✅ Rights**
- By the gate's letter, `module_chart` output would be uncitable. **Under rule 3 the functional probe
  was actually run and returned clean output ⇒ citation right retained**, but the warrant is the probe
  above, not `--help`. Cite it that way.
- The right holds **only for this command form** (`<ticker> --read`). No other argument was measured.
- ⚠ A dead `--help` means a human cannot discover the tool. Repair is out of scope (rule 1).

Not measured this run (not on the US path): `margin_history.py` (KR fundamentals), `module_KIS`,
`module_disclosure`, `module_fundamentals_kr`, `module_business`, `kr_live_shortlist.py`.

---

## What this table binds in today's run (handed to HANDOVER)

| Stage | May not be used today |
|---|---|
| SWEEP | news velocity · "new 🟢" · Δflow · stale market cap described as "current" · LNG/TSM flow tags · 🟢 headcount as stable |
| EVENT_ALPHA | "theme is cooling / fresh" · velocity-based forward cards · thread-age arguments |
| ROTATION | Δ-based promotion/demotion (incl. the 2 sector Δs that printed) · Materials wflow as a promote/demote reason |
| PREMORTEM | "the news went quiet on X" as evidence of anything |
| DEEP | news velocity · "it's quiet" · any estimate-revision leg leaning on `--ic` |
| BET / SIZE | single-number concentration · `--ic`-grounded size (→ "mechanical 1/4") · LNG/TSM flow verdicts |

**What remains, stated positively.** This desk today may speak with: **3-axis flow levels** (OBV
accumulation · RS20 · volume surge), **eqflow · breadth · ex-top1 decomposition**, **FRED macro
series** (`module_macro_us`, untouched by any gate), **FINRA short-volume and CFTC COT positioning
percentiles**, **primary filings and fundamentals** (`module_disclosure_us` · `module_fundamentals_us` ·
`module_business_us`), **chart structure via the probed `module_chart <ticker> --read` form**, and
**the news pool by direct query** — the `fts search --scope foreign` path is alive and answered every
probe; it is only the sweep's per-name velocity hop that is dead.
**Speak with price, positioning, and primary sources. Do not speak with velocity or with Δ.**

*Instrument state is not a market view — this document is not written into `handoff/` (HANDOVER only reads it).*
