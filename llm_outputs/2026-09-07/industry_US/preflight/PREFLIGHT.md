# PREFLIGHT — 2026-09-07 (Mon) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is not a report, it is a permissions table** — a FAIL is not "be careful", it is
> **"what this run may not cite today"**.
> Execution KST 2026-09-07 **22:09 clock/weekday · 22:09 news probe pre-sweep (6/6)
> · 22:09–22:10 sweep attempt #1 (aborted, see note) · 22:10–22:11 tool `--help` x51
> · 22:11 news probe post-sweep (0/4) · 22:11–22:13 news recovery clock (5 probes @20s, 0/5)
> · 22:13–22:15 sweep #2 completed (`--json`, cached prices, 300 names)
> · 22:15 bar-completeness scan · 22:15 issuer-concentration rescan
> · 22:15–22:16 risk units x3 windows · 22:16 accrual/universe/book coverage
> · 22:16 chart live render x3 · 22:17 news probe after ~2min probe-free idle (2/2 alive).**
> **Monday 2026-09-07 = US Labor Day. NYSE closed.** Last completed US session is still
> **Fri 2026-09-04**, settled. Every price statement below is about Friday 09-04 or earlier;
> no partial-bar truncation anywhere.

**Three-line summary**
> (1) FAIL **Third consecutive run with zero new price information.** `asof` = **2026-09-04**,
>    identical to both the 09-05 and 09-06 runs. Saturday, Sunday and now the Labor Day holiday
>    gave the feed no new session. All **11/11 sectors are identical to the 09-06 file on all
>    9 checked fields** (`wflow`, `eqflow`, `delta`, `breadth`, `n`, `top1`, `top1_w`,
>    `wflow_ex_top1`, `top1_flips_sign`). The `delta` column is **still the 09-03→09-04 change**,
>    now reported for the third time. **Delta-flow may not be presented as "today's move".**
> (2) **The news-axis mechanism replicated a fourth time; the positional wall moved 50→52 and the
>    recovery clock got worse.** 6/6 alive pre-sweep, **0/4 immediately post-sweep**, and — new —
>    **still 0/5 through t+100s** under 20s-interval probing, where the 09-05 and 09-06 runs both
>    recovered at t+60s. It was alive again (2/2) after roughly two minutes of *probe-free*
>    idleness. Working hypothesis, not a controlled measurement: **failed probes during the outage
>    themselves reset the idle timer.** The wall itself is exact and contiguous in **universe-rank**
>    order: velocities for ranks **1–52**, `None` for **53–300**, zero gaps, zero exceptions
>    (09-06: 1–50; 09-05: 1–49). Collector liveness is independently shown by counts *moving*
>    (NVIDIA 3841→**3761**, samsung 1590→**1471**, Apple 1267→**1282**).
> (3) FAIL **The same four structural FAILs, unmoved.** Risk units **12 / 11 / 10** across
>    250/500/750d with re-drawn membership (G4 — numerically identical to 09-06, as expected: all
>    three windows still end 09-04); universe file **54 days** stale (G5 freshness leg, bar ≤8);
>    instrumentation accruing at **0.56/day = 1.8× slower than ideal** (G6). Standing permission
>    revocations, not new findings.

**Note on sweep attempt #1:** the first sweep was launched detached and was killed at ~150/300
when its parent shell exited, leaving a 0-byte `SECTOR_FLOW_US.json`. It was re-run in the
foreground and completed. The aborted run did download the fresh price cache
(`prices_2026-09-07.pkl`), which sweep #2 reused — so **prices in this run are freshly pulled
today**, not a stale cache. The aborted burst is also what the 22:11 post-sweep probe measured.

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | **PASS — clean, fourth consecutive run** | Fresh cache 301 cols × 86 rows. NaN Close **1/301 on all 14 last sessions** (`EA` only, always; partial-NaN names **0**). `dropped_missing_axis=0`, **scored 299**. asof **2026-09-04** (settled Friday close) |
| **G1** | News-axis liveness | **FAIL** (sweep axis) · **direct path LIVE** · mechanism re-confirmed, recovery worse | `vel_coverage` **17.39%** (52/299, bar 80%). Probe **6/6 pre-sweep · 0/4 immediately post-sweep · 0/5 through t+100s (new) · 2/2 after ~2min probe-free idle**. Positional wall by universe rank: live **1–52**, `None` **53–300**, zero gaps |
| **G2** | Scoring-scale continuity | **PASS on scale · FAIL on novelty** (3rd consecutive) | `n_axes=3`, `mode=nonews`, `scored=299`, `vel_coverage=0.1739`. Scale identical to 09-06 (`3/nonews/299`), so subtraction is legal. **But `asof` 2026-09-04 == the 09-05 AND 09-06 runs' `asof`** = **0 new sessions in three runs**; all 11 sectors identical on every field |
| **G3** | Who owns the sector sign | **PASS** (full 11-row list printed) · guard still blind to the largest case | **1 of 11 flips** by the built-in flag — Cons. Disc./**AMZN** (40.2%), `wflow` −0.255 → ex-top1 **+0.068**. Issuer-level rescan finds a **second, larger** flip the flag misses: **Alphabet = 76.6%** of Comm. Services across **2 share classes**; flag prints `False`; ex-issuer `wflow` **−0.389 → +0.272**, swing **0.661** |
| **G4** | Risk-unit stability | **FAIL** | 250d **12 units** · 500d **11** · 750d **10**; membership re-drawn, not just re-counted. ARI (1st vs 2nd half) **0.3874 / 0.2328 / 0.7937** vs within-group residual fit **+0.8511 / +0.6147 / +0.5183**. All three windows end **2026-09-04** |
| **G5** | Does the universe cover the book | **FAIL** (freshness leg only) | Cover: all **11/11** US holdings present in `us_top300.csv` (300 rows) **and** all 11 scored in the sweep; missing **0**. Freshness: **54 days** (mtime 2026-07-15; bar ≤8) |
| **G6** | Instrumentation accrual rate | **FAIL** | **27 files / 48 calendar days = 0.56/day** ⇒ ETA **~23 days** to the 40-day target vs ideal 13 = **1.8×** (threshold 1.5×). Gaps median 1, max 6. Last save **2026-09-07** (today, 120 names) |
| **G7** | Tool liveness | **PASS with 2 named exceptions** | **49 of 51** `--help` exit 0 (19 `-m module_*` + 32 `scripts/*.py`). `module_chart --help` **exit=1** *but* live render **3/3** (NVDA/ANET/SPY, populated read-block each), so **chart citation stands**. `scripts/margin_history.py` **exit=1** (help-string format bug; KR-only, unused here) |

---

## Gate detail

### G0 — Bar completeness: PASS

Fresh `--refresh` pull to `llm_outputs/sector_flow/prices_2026-09-07.pkl`, **301 tickers × 86
sessions** (MultiIndex `Ticker`/`Price`; Close read via `xs('Close', level='Price')`).

| session (last 14: 2026-08-18 → 2026-09-04) | NaN Close / 301 |
|---|---:|
| every one of the 14 | **1** |

- Always-NaN over the last 14: **`['EA']`** — one name, every session.
- **Partial-NaN names: `[]` — zero.** This is the discriminating test: a *vendor hole* appears and
  disappears; a *structurally absent* name never appears. `EA` is the second kind.
- Last index in the frame is **2026-09-04**, which independently confirms the Labor Day closure —
  the download ran today and returned no 09-07 row.

**Permissions granted (not merely "no problem"):**
- `obv_norm` / `obv_state` / `flow_score` may be cited from the **primary** `SECTOR_FLOW_US.json`.
  No `SECTOR_FLOW_US_REPAIRED.json` is produced and none is needed.
- REVOKED: **`EA` may not receive any flow/OBV/RS judgment today** — it is unmeasured, not neutral.
- `asof` is a **settled Friday close**; no partial-bar reasoning is needed and none was applied.

### G1 — News-axis liveness: FAIL on the sweep axis · LIVE on the direct path

**(a) The axis is dead inside the sweep.** `vel_coverage = 17.39%` (52 of 299) against an 80% bar,
so `sector_flow` dropped the velocity axis and scored **every** name on the same 3 axes
(`mode=nonews`). That drop is the correct behaviour — the old implementation dropped the axis
silently for *some* names and inflated the whole book by +0.305.

**(b) The falsification probe says the pipe is alive — and moving.** Six named probes immediately
**before** the sweep, all live:

| query | today | 09-06 | delta |
|---|--:|--:|--:|
| samsung (삼성전자) | **1471** | 1590 | −119 |
| SK hynix (SK하이닉스) | **1025** | 1157 | −132 |
| NVIDIA | **3761** | 3841 | −80 |
| Nvidia | **3761** | 3841 | −80 |
| Tesla | **826** | 811 | +15 |
| Apple | **1282** | 1267 | +15 |

**6/6 alive.** Counts move between runs (7-day window rolling forward plus new ingest), which
independently shows the collector is running, not frozen. Low coverage is **not** "there is no news".

**(c) The sweep knocks the tunnel down. Fourth replication — and today recovery took longer.**

| probe | today | 09-06 | 09-05 |
|---|---|---|---|
| pre-sweep ×6 | **6/6 alive** | 6/6 alive | 6/6 alive |
| immediately post-sweep ×4 | **0/4** — `URLError(FileNotFoundError)` on the ngrok endpoint | 0/4, same error | 0/4, same error |
| recovery clock (`NVIDIA`, 7d, 20s spacing) | t+20 dead · t+40 dead · **t+60 dead** · t+80 dead · **t+100 dead (0/5)** | t+60/+80/+100 alive (3/3) | t+60/+80/+100 alive |
| after ~2 min of **probe-free** idleness | **2/2 alive** (NVIDIA 3761, Apple 1282) | — | — |

The new observation is the **0/5 recovery clock**. Two readings are consistent with it and this
stage cannot separate them today: either (i) the outage is simply longer under a heavier burst, or
(ii) **each failed probe resets the idle timer**, so polling every 20s prevents the very recovery
it is trying to detect. Reading (ii) is favoured by the fact that the tunnel *was* alive minutes
later once nothing was hitting it. **Logged as a hypothesis, not a measurement** — a controlled
test (one single probe at t+180s, no intermediate polling) belongs to `idle_probe`, not here.

**(d) The positional wall reproduces, and moved by two slots.** Mapped to **universe rank**
(`us_top300.csv` rank column, not the flow-sorted output order): velocities exist for ranks
**1,2,…,52** — verified contiguous, **zero gaps** — and are `None` for **every** rank from **53 to
300**. Wall history: **49 → 50 → 52** across three runs. It is a *volume* threshold at ~104
queries (~2 per name), not a fixed name list.

⚠ **Reading-order caveat recorded so it is not re-derived next run:** the `names` array in
`SECTOR_FLOW_US.json` is sorted by **`flow_score` descending**, not by universe rank. Computing the
wall on array index makes it look scattered and random. It must be mapped through
`data/us_universe/us_top300.csv` `rank` to be seen.

**Sector coverage of the 52 measured names** (this is the shape of the bias, stated numerically):
IT 20/56 (36%) · Comm.Svcs 4/12 (33%) · Staples 5/19 (26%) · Financials 9/47 (19%) · Health Care
5/32 (16%) · Energy 2/16 (12%) · Cons.Disc 3/28 (11%) · Industrials 4/50 (8%) · **Utilities 0/15,
Materials 0/12, Real Estate 0/12 — zero measured names**.

**Mechanism, on four independent observations:** the sweep issues ~2 queries per name; at ~52
names / ~104 queries the tunnel trips; the sweep then fires into a dead endpoint for the remaining
~248 names, and because it never idles long enough the tunnel never recovers inside the run.
Per-request spacing was falsified two runs ago (8/10 at 1.5s == 8/10 at 9s, 40/40 in a 0s burst).
**Cumulative burst volume trips it; only idleness untrips it.**

**Permissions revoked for this run (all stages):**
- **No theme-freshness or news-velocity citation from `SECTOR_FLOW_US.json`.** The 52 names that do
  carry a velocity are exactly the 52 largest caps — a size-selected sample, not a market sample.
- **No "sector X is quiet" / "no news flow on Y" judgment anywhere in this run.** For 247 of 299
  names the desk did not measure silence; it measured its own outage. This is absolute for
  **Utilities, Materials and Real Estate**, where the measured count is **zero**.
- GRANTED: **direct `module_news_data` calls ARE permitted and ARE the required path** for MACRO /
  EVENT_ALPHA / DEEP, provided they are made **outside a sweep burst and after a genuine idle gap**
  (today: ~2 min of no traffic was sufficient; 100s of polled traffic was not). `--scope foreign`
  remains the hard rule.
- Operational note for whoever fixes this (not this stage's job, P4): throttle/batch **inside
  `sector_flow`**, or add a local FTS fallback — **not** per-request spacing, which was falsified.

### G2 — Scoring-scale continuity: PASS on scale, FAIL on novelty (third consecutive)

`scoring = {vel_axis: false, vel_coverage: 0.1739, n_axes: 3, scored: 299, dropped_missing_axis: 0}`.

**Scale leg PASS.** 09-06: `{3 axes, nonews, 299}`. Today: `{3 axes, nonews, 299}`. Identical scale,
so subtracting the two snapshots is arithmetically legal.

**Novelty leg FAIL.** Today's `asof` is **2026-09-04**; so was 09-06's, and so was 09-05's. NYSE was
closed Saturday, Sunday, and Monday (**Labor Day**), so the feed has had no new session to give for
three runs. Direct comparison of the two `sector_rotation` blocks:

| sector | wflow | eqflow | delta | breadth | n | top1 | top1_w | ex-top1 | flips | identical to 09-06? |
|---|--:|--:|--:|--:|--:|---|--:|--:|:--:|:--:|
| Energy | +0.440 | +0.562 | +0.054 | 0.19 | 16 | XOM | 30.5 | +0.621 | False | **yes** |
| Health Care | +0.098 | +0.190 | −0.043 | 0.03 | 32 | LLY | 19.4 | +0.232 | False | **yes** |
| Utilities | +0.071 | +0.050 | −0.037 | 0.00 | 15 | NEE | 17.7 | +0.011 | False | **yes** |
| Materials | −0.025 | −0.107 | −0.037 | 0.08 | 12 | LIN | 24.7 | −0.048 | False | **yes** |
| Information Technology | −0.090 | −0.195 | −0.010 | 0.02 | 56 | NVDA | 19.4 | −0.104 | False | **yes** |
| Real Estate | −0.116 | −0.124 | −0.020 | 0.00 | 12 | WELL | 16.9 | −0.213 | False | **yes** |
| Financials | −0.118 | −0.023 | −0.004 | 0.02 | 47 | BRK-B | 13.9 | −0.061 | False | **yes** |
| Consumer Staples | −0.182 | −0.098 | −0.018 | 0.05 | 19 | WMT | 28.9 | −0.080 | False | **yes** |
| Consumer Discretionary | −0.255 | −0.280 | −0.004 | 0.04 | 28 | AMZN | 40.2 | +0.068 | **True** | **yes** |
| Industrials | −0.379 | −0.354 | +0.082 | 0.04 | 50 | CAT | 8.7 | −0.379 | False | **yes** |
| Communication Services | −0.389 | −0.035 | +0.007 | 0.00 | 12 | GOOGL | 38.3 | −0.294 | False | **yes** |

**11 of 11 sectors identical on all 9 fields.** The `delta` column still resolves against
**2026-09-03**, i.e. it is the **Friday-vs-Thursday** change already reported twice.

**Permissions:**
- GRANTED: Delta-flow **may** be cited on the 3-axis `nonews` scale — the scale is continuous.
- REVOKED: it may **not** be worded as "today's move", "the latest rotation", "flow shifted", or any
  present-tense change language. It is the **09-03 → 09-04** change and must be labelled with those
  two dates. Any stage that reports it as new information fails EXIT.
- REVOKED: no claim that a sector "improved" or "deteriorated" since the last run. Nothing changed
  because nothing was measured that had not already been measured — **twice**.
- REVOKED: no comparison against any snapshot dated **≤ 2026-09-02** without the clean-baseline
  recomputation the 09-04 preflight documented.

### G3 — Who owns the sector sign: PASS (list printed in full), guard's own blind spot flagged

**Flippers by the built-in `top1_flips_sign` flag: 1 of 11 — Consumer Discretionary only.**
(The full 11-row table with `top1`, `top1_w` and `wflow_ex_top1` is printed in G2 above and is not
duplicated here; the flag is the second-from-last column of that table. A zero would still have
been written as "0 of 11".)

**The guard misses the biggest single-issuer sector in the book.** `top1_flips_sign` is computed
per **ticker**, so a company with two listed share classes counts as two independent names.
Issuer-level rescan (share classes merged, all 11 sectors, recomputed today — not carried over):

| sector | issuer | classes | issuer share of sector cap | wflow | wflow ex-issuer | swing | sign flip |
|---|---|--:|--:|--:|--:|--:|:--:|
| **Communication Services** | **Alphabet (GOOGL+GOOG)** | **2** | **76.6%** | −0.389 | **+0.272** | **0.661** | **YES** |
| **Consumer Discretionary** | Amazon | 1 | 40.2% | −0.255 | **+0.068** | 0.323 | **YES** |
| Energy | ExxonMobil | 1 | 30.5% | +0.440 | +0.621 | 0.181 | no |
| Consumer Staples | Walmart | 1 | 28.9% | −0.182 | −0.080 | 0.102 | no |
| Materials | Linde plc | 1 | 24.7% | −0.025 | −0.048 | 0.023 | no |
| Information Technology | Nvidia | 1 | 19.4% | −0.090 | −0.104 | 0.014 | no |
| Health Care | Lilly (Eli) | 1 | 19.4% | +0.098 | +0.232 | 0.135 | no |
| Utilities | NextEra Energy | 1 | 17.7% | +0.071 | +0.011 | 0.061 | no |
| Real Estate | Welltower | 1 | 16.9% | −0.116 | −0.213 | 0.097 | no |
| Financials | Berkshire Hathaway | 1 | 13.9% | −0.118 | −0.061 | 0.057 | no |
| Industrials | Caterpillar | 1 | 8.7% | −0.379 | −0.379 | 0.001 | no |

Comm. Services' negative sign is **one company's**, and the built-in flag prints `False` because it
only sees GOOGL at 38.3%. `eqflow` independently exposes it: **−0.035 equal-weighted vs −0.389
cap-weighted** — the sector is flat once Alphabet stops being three-quarters of it.

**Permissions:**
- REVOKED: **Consumer Discretionary may not be promoted or demoted on its `wflow` bucket** in
  ROTATION §2. Use `eqflow` (−0.280, which agrees with the sign) or breadth, and say which was used
  **on the same line**.
- REVOKED: **Communication Services may not be promoted or demoted on `wflow` either**, despite the
  flag reading `False` — the flag measures the wrong unit. Its `wflow` is an Alphabet quote. Use
  `eqflow` (−0.035) or breadth, and say which was used on the same line.
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
  (`AI-compute-EPICENTER` + `AI-power/electrical`); the tool prints its own warning that
  `MAX_THEME_PCT` is counting one risk as two.
- `AVGO`+`NVDA` merge **only** at 750d.
- `MPC`+`PSX` are the one stable pair (merged at all three windows).

Threshold sensitivity shows the 0.65 choice is itself load-bearing: at 250d the count is **12 for
every threshold from 0.40 to 0.65**, then 10/7/7/5; at 500d 12/12/12/12/**11**/9/7/5/5; at 750d
12/12/12/12/**10**/9/7/5/5. The 250d window also flags 249 < 250 sample and calendar-intersection
holes (2 holes, max 8 days), so its flattering +0.8511 fit is the **least** trustworthy of the
three — high fit with ARI 0.3874 is exactly the fit-vs-stability inversion the tool warns about (S5).

**Permissions:**
- REVOKED: **no concentration guard may be quoted as a single number today.**
- GRANTED with condition: any concentration statement must carry the `--days` window **on the same
  line as the claim**, and must note the count is **12 / 11 / 10** depending on that choice.
- Any `MAX_THEME_PCT` reading that treats `AI-compute-EPICENTER` and `AI-power/electrical` as two
  independent themes is contradicted by the 500d and 750d measurements.

### G5 — Does the universe cover the book: FAIL (freshness leg only)

- **Coverage leg PASS:** all **11** US book holdings — ANET, AVGO, ETN, HPE, MET, MPC, NDAQ, NUE,
  NVDA, PSX, RTX — are present in `data/us_universe/us_top300.csv` (300 rows) **and** all 11 appear
  in the sweep's scored `names` array. **Missing: 0.** (The two KR holdings 028050 / 316140 are out
  of scope for a `--market us` universe by design.)
- **Freshness leg FAIL:** file mtime **2026-07-15**, i.e. **54 days** against a ≤8-day bar. The
  sweep itself warns that the cap vector is stale.

**Permissions:**
- GRANTED: per-name flow/RS/OBV/short judgments on the 11 holdings — they are measured.
- REVOKED: **market-cap weights, sector cap shares, and `top1_w%` may not be cited as current.**
  Every weighted number in this run — including all `wflow` and the entire `top1_w` / issuer-share
  column in G3 — rests on a **54-day-old cap vector**. Where a weighted and an equal-weighted
  reading disagree, **the equal-weighted one is the citable one today**.
- REVOKED: no claim that a name is "in / out of the top 300" as of today.

### G6 — Instrumentation accrual rate: FAIL

`snapshot_estimates.py --status`: **27 files** spanning **48 calendar days** (2026-07-22 →
2026-09-07) = **0.56 files/day**. 13 more are needed to reach the 40-day target: **13 days ideal,
~23 days at measured rate = 1.8×** the ideal, past the 1.5× threshold. Inter-save gaps
`[2,1,1,1,1,1,2,1]`, median 1, max 6. Last save is **today** (2026-09-07, 120 names) — the daemon is
running; it is the *rate over the whole span* that fails, which is the D16 trap this gate exists to
catch (counting files looks healthy; counting days does not).

**Permissions:**
- REVOKED: **`kelly_size --ic` may not be reported as an evidence-backed size.** If it appears at
  all it must be labelled **"mechanical 1/4"**, with no IC claim attached.
- REVOKED: no statement of the form "we now have enough samples to measure IC".

### G7 — Tool liveness: PASS with 2 named exceptions

**49 of 51** entry points exit 0 (19 `-m module_*`, 32 `scripts/*.py`).

1. **`module_chart --help` exit=1.** The module has no `--help` handler and prints a
   `module_text_chart` usage line instead. **Live render probe: 3/3** — NVDA, ANET and SPY each
   returned a populated read block (OBV state + 20d slope, divergence, MA stack, Bollinger,
   RSI/momentum, turn verdict, trigger, swing-low stop). So **`module_chart` output may be cited.**
   The `--help` failure is cosmetic and is recorded here so it is not re-litigated next run.
2. **`scripts/margin_history.py` exit=1** — a formatting bug in its own help string
   (`unsupported format character`). **KR-only tool, not used by this runtime.**
   REVOKED: its output may not be cited today (it is also not wanted today).

Every other tool this run intends to use is live: `module_macro_us`, `module_news_data`,
`module_flow`, `module_disclosure_us`, `module_fundamentals_us`, `module_business_us`,
`module_business`, `module_valuation`, `module_watchlist`, `module_paper_book`,
`module_report_tags`, `module_inflection`, `module_evidence`, `module_epistemics`,
`module_math_check`, `module_industry_map`, `module_KIS`, `module_publish`, `module_order_desk`,
`scripts/sector_flow.py`, `us_live_shortlist`, `us_setup_screener`, `us_flow`, `flow_read`,
`risk_units`, `drift_watch`, `cycle_exposure`, `catalyst_calendar`, `action_bracket`,
`exposure_rule`, `kelly_size`, `report_lint`, `reject_ledger`, `missed_ledger`, `ic_ledger`,
`measure_ic`, `handoff_compact`, `handoff_id_audit`, `leak_scan`, `company_score`,
`axis_inflection`, `axis_window_flow`, `snapshot_estimates`, `yf_snapshot`, `brief_recall`,
`kr_live_shortlist`.

---

## Consolidated permissions table for 2026-09-07 (what the rest of this run may NOT do)

| # | Revoked | Gate |
|---|---|---|
| 1 | Present **Delta-flow as "today's move"** or any present-tense change language — it is the **09-03 → 09-04** change, now restated for the **third** run; Labor Day gave no new session | **G2** |
| 2 | Say a sector **"improved" / "deteriorated" since the last run** — all 11 sectors are numerically identical to the 09-06 file on all 9 fields | **G2** |
| 3 | Cite **news velocity / theme freshness** from `SECTOR_FLOW_US.json` — including the 52 names that carry one, because they are exactly the 52 largest caps | G1 |
| 4 | Say any sector or name is **"quiet"** on news — 247 of 299 were not measured, they were outaged. Absolute for **Utilities / Materials / Real Estate** (0 names measured each) | **G1 (sharpened)** |
| 5 | Promote/demote **Consumer Discretionary** or **Communication Services** on `wflow` — both signs are one issuer's; use `eqflow`/breadth and say which on the line | G3 |
| 6 | Quote a **concentration guard as one number** — must carry `--days` on the same line and note 12/11/10 | G4 |
| 7 | Treat **`AI-compute-EPICENTER` and `AI-power/electrical` as two independent themes** without noting that 500d/750d measure them as one unit | G4 |
| 8 | Cite **market-cap weights / sector cap shares / top1_w% / issuer shares** as current — 54-day-old cap vector; prefer equal-weighted where the two disagree | G5 |
| 9 | Report **`kelly_size --ic`** as an evidence-backed size — label "mechanical 1/4" | G6 |
| 10 | Cite **`scripts/margin_history.py`** output | G7 |
| 11 | Give **`EA`** any flow/OBV/RS verdict — unmeasured, not neutral | G0 |
| 12 | Compare today's Delta-flow against any snapshot **≤ 2026-09-02** without clean-baseline recomputation | G2 |
| 13 | Compute the news wall on the `names` array index — it is **flow_score-sorted**; the wall is only visible in **universe-rank** order | G1 (method) |

**Granted this run:** primary-file OBV/flow from `SECTOR_FLOW_US.json` (G0) · the 3-axis `nonews`
scale as continuous with 09-06 (G2, scale leg) · 9 of 11 sector `wflow` signs (G3) · per-name
measurement on all 11 US holdings (G5, coverage leg) · `module_chart` reads (G7) · direct
`module_news_data --scope foreign` calls made outside a sweep burst and after a genuine idle gap (G1).

**Standing implication for the rest of the run:** the price tape now carries **three runs' worth of
no new session**. Whatever is genuinely new today must come from the **non-price instruments** —
FRED macro releases, direct foreign-scope news, disclosures, and the catalyst calendar. A run that
leans on the flow table is restating Friday for the third time. Note also that US Labor Day means
**no US macro release and no US corporate filing today either**, so the freshest available
non-price material is Friday's and the weekend's.

---

> P4 compliance: no market call, no name-level verdict, no sizing appears above. Sector and ticker
> symbols appear only as *instrument identifiers* (who owns a measurement), never as judgments.
> Nothing here is written to `handoff/` — instrument state is not a market view; HANDOVER reads it.
