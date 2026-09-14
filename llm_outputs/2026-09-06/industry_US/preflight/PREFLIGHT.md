# PREFLIGHT — 2026-09-06 (Sun) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is not a report, it is a permissions table** — a FAIL is not "be careful", it is
> **"what this run may not cite today"**.
> Execution KST 2026-09-06 **22:09 clock/weekday · 22:09 news probe pre-sweep (6/6)
> · 22:10–22:16 sweep (`--json --refresh`, 301 names) · 22:11 tool `--help` x47
> · 22:12 accrual/universe/book coverage · 22:13–22:16 risk units x3 windows
> · 22:16 news probe post-sweep (0/4) · 22:16–22:19 news recovery-clock probe (5 tries @20s)
> · 22:17 bar-completeness scan · 22:17 positional-wall scan · 22:18 issuer-concentration scan
> · 22:18 chart live render x3.**
> **Sunday — NYSE closed all weekend.** Last completed US session **Fri 2026-09-04**, settled.
> Every price statement below is about **Friday 09-04 or earlier**; no partial-bar truncation.

**Three-line summary**
> (1) FAIL **The single most important instrument fact today: this sweep contains ZERO new market
>    information.** Today's `asof` is **2026-09-04** — *identical to the 09-05 run's* `asof`. The
>    weekend gave the feed no new session, so today's sector table is **identical** to yesterday's
>    on every field checked (11/11 sectors: `wflow`, `eqflow`, `delta`, `breadth`, `n`, `top1`,
>    `top1_w`, `wflow_ex_top1`, `top1_flips_sign` all the same). The `delta` column is **still the
>    09-03 to 09-04 change** the 09-05 run already cited. Therefore **Delta-flow may not be
>    presented as "today's move" — it is a restatement of a change already reported once.** This is
>    a new G2 finding, not a carry-over.
> (2) **The news-axis mechanism replicated a third time, and tightened.** 6/6 alive pre-sweep,
>    **0/4 immediately post-sweep**, dead at t+20s and t+40s, **alive at t+60s / t+80s / t+100s
>    (3/3, identical count 3841 all three times)**. The positional wall is again exact and
>    contiguous: velocities at universe positions **0–49, `None` at 50–298, zero gaps, zero
>    exceptions** (yesterday 0–48). The wall sits at **~49–50 names ~ ~100 queries**; the recovery
>    clock is **~60s of idleness**; both reproduced on independent runs. **The pipe is not down;
>    this desk knocks it down.** Independent evidence the collector is alive: pre-sweep counts
>    *moved* vs yesterday (samsung 1565 to **1590**, NVIDIA 4102 to **3841** as the 7d window
>    rolls) — a frozen pipe would return frozen counts.
> (3) FAIL **The same three structural FAILs, unmoved and now measurably chronic.** Risk units
>    **12 / 11 / 10** across 250/500/750d with re-drawn membership (G4 — numerically identical to
>    yesterday, as expected: all three windows end on the same 09-04); universe file **53 days**
>    stale (G5 freshness leg, bar <=8); instrumentation accruing at **0.55/day = 1.8x slower than
>    ideal** (G6). Logged as standing permission revocations, not new findings.

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | **PASS — clean, third consecutive run** | Fresh cache 301 cols x 86 rows. NaN Close **1/301 on all 14 last sessions** (`EA` only, always; partial-NaN names **0**). `dropped_missing_axis=0`, **scored 299**. asof **2026-09-04** (settled Friday close) |
| **G1** | News-axis liveness | **FAIL** (sweep axis) · **direct path LIVE** · mechanism re-confirmed | `vel_coverage` **16.72%** (50/299, bar 80%). Probe **6/6 pre-sweep · 0/4 immediately post-sweep · dead t+20/+40s · alive t+60/+80/+100s (3/3, identical 3841)**. Positional wall: velocities at positions **0–49**, `None` at **50–298**, zero gaps, zero exceptions |
| **G2** | Scoring-scale continuity | **PASS on scale · FAIL on novelty** (new) | `n_axes=3`, `mode=nonews`, `scored=299`, `vel_coverage=0.1672`. Scale identical to 09-05 (`3/nonews/299`), so subtraction is legal. **But `asof` 2026-09-04 == the 09-05 run's `asof`** = **0 new sessions**; all 11 sectors identical on every field. Delta is the **09-03 to 09-04** change, already reported |
| **G3** | Who owns the sector sign | **PASS** (full 11-row list printed) · guard still blind to the largest case | **1 of 11 flips** by the built-in flag — Cons. Disc./**AMZN** (40.2%), `wflow` -0.255 to ex-top1 **+0.068**. Issuer-level rescan finds a **second, larger** flip the flag misses: **Alphabet = 76.6%** of Comm. Services across **2 share classes**; flag prints `False`; ex-issuer `wflow` **-0.389 to +0.272**, swing **0.661** |
| **G4** | Risk-unit stability | **FAIL** | 250d **12 units** · 500d **11** · 750d **10**; membership re-drawn, not just re-counted. ARI (1st vs 2nd half) **0.3874 / 0.2328 / 0.7937** vs within-group residual fit **+0.8511 / +0.6147 / +0.5183**. All three windows end **2026-09-04** |
| **G5** | Does the universe cover the book | **FAIL** (freshness leg only) | Cover: all **11/11** US holdings present in `us_top300.csv` (301 lines = header + 300), missing **0**. Freshness: **53 days** (mtime 2026-07-15; bar <=8) |
| **G6** | Instrumentation accrual rate | **FAIL** | **26 files / 47 calendar days = 0.55/day** = ETA **~25 days** to the 40-day target vs ideal 14 = **1.8x** (threshold 1.5x). Gaps median 1, max 6. Last save **2026-09-06** (today, 120 names) |
| **G7** | Tool liveness | **PASS with 2 named exceptions** | **45 of 47** `--help` exit 0. `module_chart --help` **exit=1** *but* live render **3/3** (NVDA/ANET/SPY, populated `CHART_READ` block each), so **chart citation stands**. `scripts/margin_history.py` **exit=1** (help-string format bug; KR-only, unused here) |

---

## Gate detail

### G0 — Bar completeness: PASS

Fresh `--refresh` pull to `llm_outputs/sector_flow/prices_2026-09-06.pkl`, **301 tickers x 86
sessions** (MultiIndex `Ticker`/`Price`; Close read via `xs('Close', level='Price')`).

| session (last 14) | NaN Close / 301 |
|---|---:|
| 2026-08-18 ... 2026-09-04 | **1** on every single one |

- Always-NaN over the last 14: **`['EA']`** — one name, every session.
- **Partial-NaN names (NaN on some sessions but not all): `[]` — zero.** This is the discriminating
  test: a *vendor hole* appears and disappears; a *structurally absent* name never appears. `EA`
  is the second kind. Contrast three runs ago, when the 2026-08-28 row alone carried **258/301**.

**Permissions granted (not merely "no problem"):**
- `obv_norm` / `obv_state` / `flow_score` may be cited from the **primary** `SECTOR_FLOW_US.json`.
  No `SECTOR_FLOW_US_REPAIRED.json` is produced and none is needed.
- 08-28 closes/volumes may be cited plainly, no "5m-proxy" label, for 300 of 301.
- REVOKED: **`EA` may not receive any flow/OBV/RS judgment today** — it is unmeasured, not neutral.
- `asof` is a **settled Friday close**; no partial-bar reasoning is needed and none was applied.

### G1 — News-axis liveness: FAIL on the sweep axis · LIVE on the direct path

**(a) The axis is dead inside the sweep.** `vel_coverage = 16.72%` (50 of 299) against an 80% bar,
so `sector_flow` dropped the velocity axis and scored **every** name on the same 3 axes
(`mode=nonews`). That drop is the correct behaviour — the old implementation dropped the axis
silently for *some* names and inflated the whole book by +0.305.

**(b) The falsification probe says the pipe is alive — and moving.** Six named probes immediately
**before** the sweep, all live:

| query | today | 09-05 | delta |
|---|--:|--:|--:|
| samsung (삼성전자) | **1590** | 1565 | +25 |
| SK hynix (SK하이닉스) | **1157** | 1165 | -8 |
| NVIDIA | **3841** | 4102 | -261 |
| Nvidia | **3841** | 4102 | -261 |
| Tesla | **811** | 822 | -11 |
| Apple | **1267** | 1299 | -32 |

**6/6 alive.** The counts *move* between runs (7-day window rolling forward, plus new ingest),
which independently shows the collector is running, not frozen. So low coverage is **not**
"there is no news".

**(c) The sweep knocks the tunnel down; ~60s of idleness brings it back. Third replication.**

| probe | today | 09-05 |
|---|---|---|
| pre-sweep x6 | **6/6 alive** | 6/6 alive |
| immediately post-sweep x4 | **0/4** — `URLError(FileNotFoundError)` on the ngrok endpoint | 0/4, same error |
| recovery clock (`NVIDIA`, 7d) | t+20s dead · t+40s dead · **t+60s alive 3841** · **t+80s alive 3841** · **t+100s alive 3841** | t+0 dead · t+20 dead · t+40 dead · t+60 alive · t+80 alive · t+100 alive |

**(d) The positional wall reproduces, and it moved by exactly one slot.** Velocities exist for
universe positions **0,1,...,49** — verified contiguous, **zero gaps inside the run** — and are
`None` for **every** position from **50 to 298**. First name past the wall: position 50 = `RTX`
(`velocity=None`); positions 48/49 (`WDC` 0.42, `WFC` 0.92) are the last two live ones.
Yesterday the wall sat at 0–48. **49 to 50 across two runs**: the wall is a *volume* threshold at
~100 queries (about 2 per name), not a fixed name list.

**Mechanism, stated plainly and now on three independent observations:** the sweep issues ~2
queries per name; at ~49–50 names / ~100 queries the tunnel trips; the sweep then keeps firing into
a dead endpoint for the remaining ~250 names, and because it never idles 60 seconds the tunnel
never recovers inside the run. Spacing was falsified two runs ago (8/10 at 1.5s == 8/10 at 9s,
40/40 in a 0s burst). **Cumulative burst volume trips it; only idleness untrips it.**

**Permissions revoked for this run (all stages):**
- **No theme-freshness or news-velocity citation from `SECTOR_FLOW_US.json`.** The 50 names that
  do carry a velocity are **positions 0–49 = the 50 largest caps**, a size-selected sample, not a
  market sample — quoting even those 50 smuggles in a mega-cap bias.
- **No "sector X is quiet" / "no news flow on Y" judgment anywhere in this run.** For 249 of 299
  names the desk did not measure silence; it measured its own outage.
- GRANTED: **direct `module_news_data` calls ARE permitted and ARE the required path** for MACRO /
  EVENT_ALPHA / DEEP, provided they are made **outside a sweep burst and >=60s after one**.
  `--scope foreign` remains the hard rule.
- Operational note for whoever fixes this (not this stage's job, P4): the fix is
  throttling/batching **inside `sector_flow`**, or a local FTS fallback — **not** per-request
  spacing, which was falsified.

### G2 — Scoring-scale continuity: PASS on scale, FAIL on novelty (new finding)

`scoring = {vel_axis: false, vel_coverage: 0.1672, n_axes: 3, scored: 299, dropped_missing_axis: 0}`.

**Scale leg PASS.** Yesterday: `{3 axes, nonews, 299}`. Today: `{3 axes, nonews, 299}`. Identical
scale, so subtracting the two snapshots is arithmetically legal — unlike the mixed-axis cases this
gate exists to catch.

**Novelty leg FAIL — and this is the finding of the day.** Today's `asof` is **2026-09-04**. The
09-05 run's `asof` was **also 2026-09-04**. NYSE was closed Saturday and Sunday, so the feed had no
new session to give. Direct comparison of the two `sector_rotation` blocks:

| sector | wflow (today / 09-05) | eqflow (today / 09-05) | delta (today / 09-05) | identical? |
|---|---|---|---|:--:|
| Energy | +0.440 / +0.440 | +0.562 / +0.562 | +0.054 / +0.054 | yes |
| Health Care | +0.098 / +0.098 | +0.190 / +0.190 | -0.043 / -0.043 | yes |
| Utilities | +0.071 / +0.071 | +0.050 / +0.050 | -0.037 / -0.037 | yes |
| Materials | -0.025 / -0.025 | -0.107 / -0.107 | -0.037 / -0.037 | yes |
| Information Technology | -0.090 / -0.090 | -0.195 / -0.195 | -0.010 / -0.010 | yes |
| Real Estate | -0.116 / -0.116 | -0.124 / -0.124 | -0.020 / -0.020 | yes |
| Financials | -0.118 / -0.118 | -0.023 / -0.023 | -0.004 / -0.004 | yes |
| Consumer Staples | -0.182 / -0.182 | -0.098 / -0.098 | -0.018 / -0.018 | yes |
| Consumer Discretionary | -0.255 / -0.255 | -0.280 / -0.280 | -0.004 / -0.004 | yes |
| Industrials | -0.379 / -0.379 | -0.354 / -0.354 | +0.082 / +0.082 | yes |
| Communication Services | -0.389 / -0.389 | -0.035 / -0.035 | +0.007 / +0.007 | yes |

**11 of 11 sectors identical on every field.** The sweep's `history.json` last key is 2026-09-04
(today's run overwrote yesterday's same-dated key); the `delta` column therefore still resolves
against **2026-09-03**, i.e. it is the **Friday-vs-Thursday** change the 09-05 run already reported.

**Permissions:**
- GRANTED: Delta-flow **may** be cited on the 3-axis `nonews` scale — the scale is continuous.
- REVOKED: it may **not** be worded as "today's move", "the latest rotation", "flow shifted", or any
  present-tense change language. It is the **09-03 to 09-04** change and must be labelled with those
  two dates. Any stage that reports it as new information fails EXIT.
- REVOKED: no claim that a sector "improved" or "deteriorated" since the last run. Nothing changed
  because nothing was measured that had not already been measured.
- REVOKED: no comparison against any snapshot dated **<= 2026-09-02** without the clean-baseline
  recomputation the 09-04 preflight documented.

### G3 — Who owns the sector sign: PASS (list printed in full), guard's own blind spot flagged

**Full 11-sector flipper list (printed in full per EXIT CHECK — a 0 would still be written as 0):**

| sector | n | wflow | eqflow | breadth | delta | top1 | top1 w% | wflow ex-top1 | flips? |
|---|--:|--:|--:|--:|--:|---|--:|--:|:--:|
| Energy | 16 | +0.440 | +0.562 | 0.19 | +0.054 | XOM | 30.5 | +0.621 | False |
| Health Care | 32 | +0.098 | +0.190 | 0.03 | -0.043 | LLY | 19.4 | +0.232 | False |
| Utilities | 15 | +0.071 | +0.050 | 0.00 | -0.037 | NEE | 17.7 | +0.011 | False |
| Materials | 12 | -0.025 | -0.107 | 0.08 | -0.037 | LIN | 24.7 | -0.048 | False |
| Information Technology | 56 | -0.090 | -0.195 | 0.02 | -0.010 | NVDA | 19.4 | -0.104 | False |
| Real Estate | 12 | -0.116 | -0.124 | 0.00 | -0.020 | WELL | 16.9 | -0.213 | False |
| Financials | 47 | -0.118 | -0.023 | 0.02 | -0.004 | BRK-B | 13.9 | -0.061 | False |
| Consumer Staples | 19 | -0.182 | -0.098 | 0.05 | -0.018 | WMT | 28.9 | -0.080 | False |
| **Consumer Discretionary** | 28 | **-0.255** | -0.280 | 0.04 | -0.004 | **AMZN** | **40.2** | **+0.068** | **True** |
| Industrials | 50 | -0.379 | -0.354 | 0.04 | +0.082 | CAT | 8.7 | -0.379 | False |
| Communication Services | 12 | -0.389 | -0.035 | 0.00 | +0.007 | GOOGL | 38.3 | -0.294 | False |

**Flippers by the built-in flag: 1 of 11 — Consumer Discretionary only.**

**The guard misses the biggest single-issuer sector in the book.** `top1_flips_sign` is computed
per **ticker**, so a company with two listed share classes counts as two independent names.
Issuer-level rescan (share classes merged, all 11 sectors):

| sector | issuer | classes | issuer share of sector cap | wflow | wflow ex-issuer | swing | sign flip |
|---|---|--:|--:|--:|--:|--:|:--:|
| **Communication Services** | **Alphabet (GOOGL+GOOG)** | **2** | **76.6%** | -0.389 | **+0.272** | **0.661** | **YES** |
| **Consumer Discretionary** | Amazon | 1 | 40.2% | -0.255 | **+0.068** | 0.323 | **YES** |
| Energy | ExxonMobil | 1 | 30.5% | +0.440 | +0.621 | 0.181 | no |
| Consumer Staples | Walmart | 1 | 28.9% | -0.182 | -0.080 | 0.102 | no |
| Materials | Linde plc | 1 | 24.7% | -0.025 | -0.048 | 0.023 | no |
| Information Technology | Nvidia | 1 | 19.4% | -0.090 | -0.104 | 0.014 | no |
| Health Care | Lilly (Eli) | 1 | 19.4% | +0.098 | +0.232 | 0.135 | no |
| Utilities | NextEra Energy | 1 | 17.7% | +0.071 | +0.011 | 0.061 | no |
| Real Estate | Welltower | 1 | 16.9% | -0.116 | -0.213 | 0.097 | no |
| Financials | Berkshire Hathaway | 1 | 13.9% | -0.118 | -0.061 | 0.057 | no |
| Industrials | Caterpillar | 1 | 8.7% | -0.379 | -0.379 | 0.001 | no |

Comm. Services' negative sign is **one company's**, and the built-in flag prints `False` because it
only sees GOOGL at 38.3%. `eqflow` independently exposes it: **-0.035 equal-weighted vs -0.389
cap-weighted** — the sector is flat once Alphabet stops being three-quarters of it.

**Permissions:**
- REVOKED: **Consumer Discretionary may not be promoted or demoted on its `wflow` bucket** in
  ROTATION section 2. Use `eqflow` (-0.280, which agrees with the sign) or breadth, and say which
  was used **on the same line**.
- REVOKED: **Communication Services may not be promoted or demoted on `wflow` either**, despite the
  flag reading `False` — the flag measures the wrong unit. Its `wflow` is an Alphabet quote. Use
  `eqflow` (-0.035) or breadth, and say which was used on the same line.
- GRANTED: the other 9 sectors' `wflow` signs survive top-1 removal and may be cited as
  sector-level.

### G4 — Risk-unit stability: FAIL

Same book (11 US + 2 KR names), same bench (SPY), same 0.65 distance threshold, three windows all
ending **2026-09-04**:

| window | actual trading days | units | within-group residual corr | between | ARI (1st vs 2nd half) |
|---|--:|--:|--:|--:|--:|
| 250d | 249 | **12** | +0.8511 | +0.0107 | **0.3874** |
| 500d | 499 | **11** | +0.6147 | +0.0215 | **0.2328** |
| 750d | 749 | **10** | +0.5183 | +0.0184 | **0.7937** |

Membership is not merely re-counted, it is **re-drawn**:
- `ANET`+`ETN` are **separate** at 250d but **merge into one unit** at 500d and 750d — and at both
  those windows that merged unit **spans two different book theme labels**
  (`AI-compute-EPICENTER` + `AI-power/electrical`), i.e. `MAX_THEME_PCT` is counting one risk as two.
- `AVGO`+`NVDA` merge **only** at 750d.
- `MPC`+`PSX` are the one stable pair (merged at all three windows).

Threshold sensitivity shows the 0.65 choice is itself load-bearing: at 250d the unit count is
**12 for every threshold from 0.40 to 0.65** and then falls to 10/7/7/5; at 500d the same sweep
gives 12/12/12/12/11/9/7/5/5. The 250d window also flags 249 < 250 sample and calendar-intersection
holes (2 holes, max 8 days), so its flattering +0.8511 fit is the **least** trustworthy of the
three, not the most — high fit with ARI 0.3874 is exactly the fit-vs-stability inversion the tool
warns about (S5).

**Permissions:**
- REVOKED: **no concentration guard may be quoted as a single number today.**
- GRANTED with condition: any concentration statement must carry the `--days` window **on the same
  line as the claim**, and must note the count is **12 / 11 / 10** depending on that choice.
- Any `MAX_THEME_PCT` reading that treats `AI-compute-EPICENTER` and `AI-power/electrical` as two
  independent themes is contradicted by the 500d and 750d measurements.

### G5 — Does the universe cover the book: FAIL (freshness leg only)

- **Coverage leg PASS:** all **11** US book holdings — ANET, AVGO, ETN, HPE, MET, MPC, NDAQ, NUE,
  NVDA, PSX, RTX — are present in `data/us_universe/us_top300.csv` (301 lines = header + 300).
  **Missing: 0.** (The two KR holdings 028050 / 316140 are out of scope for a `--market us`
  universe by design.)
- **Freshness leg FAIL:** file mtime **2026-07-15**, i.e. **53 days** against a <=8-day bar. The
  sweep itself warns: `유니버스 us_top300.csv 53일 경과 — 시총 stale`.

**Permissions:**
- GRANTED: per-name flow/RS/OBV/short judgments on the 11 holdings — they are measured.
- REVOKED: **market-cap weights, sector cap shares, and `top1_w%` may not be cited as current.**
  Every weighted number in this run — including all of G3's `wflow` and the entire `top1_w` /
  issuer-share column — rests on a **53-day-old cap vector**. Where a weighted and an
  equal-weighted reading disagree, **the equal-weighted one is the citable one today**.
- REVOKED: no claim that a name is "in / out of the top 300" as of today.

### G6 — Instrumentation accrual rate: FAIL

`snapshot_estimates.py --status`: **26 files** spanning **47 calendar days** (2026-07-22 to
2026-09-06) = **0.55 files/day**. 14 more are needed to reach the 40-day target: **14 days ideal,
~25 days at measured rate = 1.8x** the ideal, past the 1.5x threshold. Inter-save gaps
`[2,2,1,1,1,1,1,2]`, median 1, max 6. Last save is **today** (2026-09-06, 120 names) — so the
daemon is running; it is the *rate over the whole span* that fails, which is the D16 trap this
gate exists to catch (counting files looks healthy; counting days does not).

**Permissions:**
- REVOKED: **`kelly_size --ic` may not be reported as an evidence-backed size.** If it appears at
  all it must be labelled **"mechanical 1/4"**, with no IC claim attached.
- REVOKED: no statement of the form "we now have enough samples to measure IC".

### G7 — Tool liveness: PASS with 2 named exceptions

**45 of 47** entry points exit 0 (19 `-m module_*`, 28 `scripts/*.py`).

1. **`module_chart --help` exit=1.** The module has no `--help` handler and prints a
   `module_text_chart` usage line instead. **Live render probe: 3/3** — NVDA, ANET, SPY each wrote
   a chart file with a populated `CHART_READ` block (OBV state + 20d slope, divergence, MA stack,
   Bollinger, RSI/momentum, turn verdict, trigger, swing-low stop).
   So **`module_chart` output may be cited.** The `--help` failure is cosmetic and is recorded here
   so it is not re-litigated next run.
2. **`scripts/margin_history.py` exit=1** — `ValueError: unsupported format character ')'`, a
   formatting bug in its own help string. **KR-only tool, not used by this runtime.**
   REVOKED: its output may not be cited today (it is also not wanted today).

Every other tool this run intends to use is live: `module_macro_us`, `module_news_data`,
`module_flow`, `module_disclosure_us`, `module_fundamentals_us`, `module_business_us`,
`module_valuation`, `module_watchlist`, `module_paper_book`, `module_report_tags`,
`module_inflection`, `module_evidence`, `module_epistemics`, `module_math_check`,
`module_industry_map`, `module_KIS`, `module_publish`, `module_order_desk`,
`scripts/sector_flow.py`, `us_live_shortlist`, `us_setup_screener`, `us_flow`, `flow_read`,
`risk_units`, `drift_watch`, `cycle_exposure`, `catalyst_calendar`, `action_bracket`,
`exposure_rule`, `kelly_size`, `report_lint`, `reject_ledger`, `missed_ledger`, `ic_ledger`,
`measure_ic`, `handoff_compact`, `handoff_id_audit`, `leak_scan`, `company_score`,
`axis_inflection`, `axis_window_flow`, `snapshot_estimates`, `yf_snapshot`, `brief_recall`,
`kr_live_shortlist`.

---

## Consolidated permissions table for 2026-09-06 (what the rest of this run may NOT do)

| # | Revoked | Gate |
|---|---|---|
| 1 | Present **Delta-flow as "today's move"** or any present-tense change language — it is the **09-03 to 09-04** change, already reported by the 09-05 run; today's sweep read the same settled session | **G2 (new)** |
| 2 | Say a sector **"improved" / "deteriorated" since the last run** — all 11 sectors are numerically identical to the 09-05 file | **G2 (new)** |
| 3 | Cite **news velocity / theme freshness** from `SECTOR_FLOW_US.json` — including the 50 names that carry one, because they are the 50 largest caps, a size-selected sample | G1 |
| 4 | Say any sector or name is **"quiet"** on news — 249 of 299 were not measured, they were outaged | G1 |
| 5 | Promote/demote **Consumer Discretionary** or **Communication Services** on `wflow` — both signs are one issuer's; use `eqflow`/breadth and say which on the line | G3 |
| 6 | Quote a **concentration guard as one number** — must carry `--days` on the same line and note 12/11/10 | G4 |
| 7 | Treat **`AI-compute-EPICENTER` and `AI-power/electrical` as two independent themes** without noting that 500d/750d measure them as one unit | G4 |
| 8 | Cite **market-cap weights / sector cap shares / top1_w% / issuer shares** as current — 53-day-old cap vector; prefer equal-weighted where the two disagree | G5 |
| 9 | Report **`kelly_size --ic`** as an evidence-backed size — label "mechanical 1/4" | G6 |
| 10 | Cite **`scripts/margin_history.py`** output | G7 |
| 11 | Give **`EA`** any flow/OBV/RS verdict — unmeasured, not neutral | G0 |
| 12 | Compare today's Delta-flow against any snapshot **<= 2026-09-02** without clean-baseline recomputation | G2 |

**Granted this run:** primary-file OBV/flow from `SECTOR_FLOW_US.json` (G0) · the 3-axis `nonews`
scale as continuous with 09-05 (G2, scale leg) · 9 of 11 sector `wflow` signs (G3) · per-name
measurement on all 11 US holdings (G5, coverage leg) · `module_chart` reads (G7) · direct
`module_news_data --scope foreign` calls made outside a sweep burst and >=60s after one (G1).

**Standing implication for the rest of the run:** because the price tape carries no new session,
**whatever is genuinely new today must come from the non-price instruments** — FRED macro releases,
direct foreign-scope news, disclosures, and the catalyst calendar. A run that leans on the flow
table will be restating Friday.

---

> P4 compliance: no market call, no name-level verdict, no sizing appears above. Sector and ticker
> symbols appear only as *instrument identifiers* (who owns a measurement), never as judgments.
> Nothing here is written to `handoff/` — instrument state is not a market view; HANDOVER reads it.
