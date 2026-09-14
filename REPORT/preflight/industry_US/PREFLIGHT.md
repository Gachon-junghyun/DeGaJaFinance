# PREFLIGHT — 2026-09-08 (Tue) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is not a report, it is a permissions table** — a FAIL is not "be careful", it is
> **"what this run may not cite today"**.
> Execution KST 2026-09-08 **22:09 clock/weekday · 22:10 news probe pre-sweep (8/8)
> · 22:10 yfinance partial-bar probe · 22:11–22:15 sweep (`--json --refresh`, 300 names, completed)
> · 22:15 news probe post-sweep (0/4) · 22:15 sweep-JSON diff vs 09-07 (11 sectors × 11 fields)
> · 22:15 velocity-wall map through universe rank · 22:16 issuer-concentration rescan
> · 22:16 bar-completeness scan · 22:16–22:19 risk units × 3 windows · 22:19 accrual/universe/book coverage
> · 22:19–22:21 tool `--help` × 53 · 22:21 chart live render × 3 · 22:21 news probe after ~5 min probe-free idle (2/2).**
> **Time-of-run note: the sweep ran at 09:11–09:15 ET — BEFORE the 09:30 ET open.** A direct
> yfinance probe at 22:10 KST returned **no 2026-09-08 row** for NVDA/SPY/AAPL/XOM, so **no
> partial intraday bar entered any calculation.** Last settled US session is **Fri 2026-09-04**
> (Mon 09-07 was Labor Day, NYSE closed).

**Three-line summary**
> (1) FAIL **Fourth consecutive run with zero new price information.** `asof` = **2026-09-04**,
>    identical to the 09-05, 09-06 and 09-07 runs. All **11/11 sectors are identical to the 09-07
>    file on all 11 checked fields** (`wflow`, `eqflow`, `delta`, `breadth`, `n`, `green`, `red`,
>    `top1`, `top1_w`, `wflow_ex_top1`, `top1_flips_sign`). The `delta` column is **still the
>    09-03→09-04 change**, now reported for the fourth time. Unlike the last three runs this is
>    **not** a closed-market artefact — the market opens in 19 minutes; the desk is simply running
>    pre-open, so the freshest possible tape is still Friday's.
> (2) **The news-axis mechanism replicated a fifth time, and the recovery reading now favours the
>    idle-timer hypothesis.** 8/8 alive pre-sweep, **0/4 immediately post-sweep**, **2/2 alive after
>    ~5 minutes of probe-free idleness** (no intermediate polling this run, deliberately — the
>    09-07 run's 20s polling produced 0/5 through t+100s). The wall is exact and contiguous in
>    **universe-rank** order: velocities for ranks **1–52**, `None` for **53–300**, zero gaps.
>    Wall history **49 → 50 → 52 → 52**. Collector liveness independently shown by counts *moving*
>    (NVIDIA 3761→**3892**, 삼성전자 1471→**1442**, Apple 1282→**1297**).
> (3) FAIL **The same four structural FAILs, unmoved and one day older.** Risk units
>    **12 / 11 / 10** across 250/500/750d with re-drawn membership (G4 — numerically identical to
>    09-07, as expected: all three windows still end 09-04); universe file **55 days** stale
>    (G5 freshness leg, bar ≤8); instrumentation accruing at **0.57/day = 1.75× slower than ideal**
>    (G6). Standing permission revocations, not new findings.

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | **PASS — clean, fifth consecutive run** | Fresh cache `prices_2026-09-08.pkl` 301 cols × 86 rows. NaN Close **1/301 on all 14 last sessions** (`EA` only, always; partial-NaN names **0**). `dropped_missing_axis=0`, **scored 299**. asof **2026-09-04** (settled Friday close). **No 09-08 partial bar** — probed directly, absent |
| **G1** | News-axis liveness | **FAIL** (sweep axis) · **direct path LIVE** · mechanism re-confirmed 5th time | `vel_coverage` **17.39%** (52/299, bar 80%). Probe **8/8 pre-sweep · 0/4 immediately post-sweep · 2/2 after ~5 min probe-free idle**. Positional wall by universe rank: live **1–52**, `None` **53–300**, zero gaps |
| **G2** | Scoring-scale continuity | **PASS on scale · FAIL on novelty** (4th consecutive) | `n_axes=3`, `mode=nonews`, `scored=299`, `vel_coverage=0.1739`. Scale identical to 09-07 (`3/nonews/299`), so subtraction is legal. **But `asof` 2026-09-04 == the 09-05, 09-06 AND 09-07 runs' `asof`** = **0 new sessions in four runs**; all 11 sectors identical on every field |
| **G3** | Who owns the sector sign | **PASS** (full 11-row list printed) · guard still blind to the largest case | **1 of 11 flips** by the built-in flag — Cons. Disc./**AMZN** (40.2%), `wflow` −0.255 → ex-top1 **+0.068**. Issuer-level rescan finds a **second, larger** flip the flag misses: **Alphabet = 76.6%** of Comm. Services across **2 share classes**; flag prints `False`; ex-issuer `wflow` **−0.389 → +0.272**, swing **0.661** |
| **G4** | Risk-unit stability | **FAIL** | 250d **12 units** · 500d **11** · 750d **10**; membership re-drawn, not just re-counted. ARI (1st vs 2nd half) **0.3874 / 0.2328 / 0.7937** vs within-group residual fit **+0.8511 / +0.6147 / +0.5183**. All three windows end **2026-09-04** |
| **G5** | Does the universe cover the book | **FAIL** (freshness leg only) | Cover: all **11/11** US holdings present in `us_top300.csv` (300 rows) **and** all 11 scored in the sweep; missing **0**. Freshness: **55 days** (mtime 2026-07-15; bar ≤8) |
| **G6** | Instrumentation accrual rate | **FAIL** | **28 files / 49 calendar days = 0.57/day** ⇒ ETA **~21 days** to the 40-day target vs ideal 12 = **1.75×** (threshold 1.5×). Gaps median 1, max 6. Last save **2026-09-08** (today, 120 names) |
| **G7** | Tool liveness | **PASS with 2 named exceptions** | **51 of 53** `--help` exit 0 (19/20 `-m module_*` + 32/33 `scripts/*.py`). `module_chart --help` **exit=1** *but* live render **3/3** (NVDA/ANET/SPY, populated 7-line read block each), so **chart citation stands**. `scripts/margin_history.py` **exit=1** (help-string format bug; KR-only, unused here) |

⇒ **8 gates: PASS 3 (G0, G3, G7-with-exceptions) · FAIL 5 (G1, G2-novelty, G4, G5, G6).**
Nothing improved and nothing newly broke; the instrument state is a carbon copy of 09-07 with the
staleness counters advanced by one day. That is itself the finding — see the standing implication.

---

## Gate detail

### G0 — Bar completeness: PASS

Fresh `--refresh` pull to `llm_outputs/sector_flow/prices_2026-09-08.pkl`, **301 tickers × 86
sessions** (MultiIndex `Ticker`/`Price`; Close read via `xs('Close', level='Price')`).

| session (last 14: 2026-08-18 → 2026-09-04) | NaN Close / 301 |
|---|---:|
| every one of the 14 | **1** |

- Always-NaN over the last 14: **`['EA']`** — one name, every session.
- **Partial-NaN names: `[]` — zero.** This is the discriminating test: a *vendor hole* appears and
  disappears; a *structurally absent* name never appears. `EA` is the second kind.
- Last index in the frame is **2026-09-04**. `SPY`'s own last non-NaN bar is also **2026-09-04**,
  so the benchmark and the individual names end on the **same session** — the exact misalignment
  that the 2026-09-08 KR run found (positional `iloc[-1]` on two series of different length,
  biasing every `rs20`/`rs60`) **cannot fire here today**. Checked explicitly because of that KR
  finding; this is a same-day cross-market check, not an inherited assumption.
- **Partial-bar probe:** a direct `yfinance` download at 22:10 KST (09:10 ET, pre-open) returned
  rows ending **2026-09-04** for NVDA/SPY/AAPL/XOM — **no 2026-09-08 row exists yet**. So the
  desk is not at risk of the intraday-truncation class today; the risk today is the opposite one
  (stale, see G2).

**Permissions granted (not merely "no problem"):**
- `obv_norm` / `obv_state` / `flow_score` may be cited from the **primary** `SECTOR_FLOW_US.json`.
  No repaired file is produced and none is needed.
- REVOKED: **`EA` may not receive any flow/OBV/RS judgment today** — it is unmeasured, not neutral.
- `asof` is a **settled Friday close**; no partial-bar reasoning is needed and none was applied.

### G1 — News-axis liveness: FAIL on the sweep axis · LIVE on the direct path

**(a) The axis is dead inside the sweep.** `vel_coverage = 17.39%` (52 of 299) against an 80% bar,
so `sector_flow` dropped the velocity axis and scored **every** name on the same 3 axes
(`mode=nonews`). That drop is the correct behaviour — the old implementation dropped the axis
silently for *some* names and inflated the whole book by +0.305.

**(b) The falsification probe says the pipe is alive — and moving.** Eight named probes
immediately **before** the sweep, all live:

| query | today | 09-07 | delta |
|---|--:|--:|--:|
| NVIDIA (`--scope foreign`) | **3886** | — | — |
| Apple (`--scope foreign`) | **1295** | — | — |
| Tesla (`--scope foreign`) | **919** | — | — |
| samsung (`--scope foreign`) | **411** | — | — |
| SK hynix (`--scope foreign`) | **244** | — | — |
| NVIDIA (no scope) | **3892** | 3761 | **+131** |
| Apple (no scope) | **1297** | 1282 | +15 |
| 삼성전자 (no scope) | **1442** | 1471 | −29 |
| SK하이닉스 (no scope) | **952** | 1025 | −73 |

**All alive** (9 rows: 5 scoped probes fired pre-sweep, then 4 no-scope continuity re-probes).
Counts move between runs (7-day window rolling forward plus new ingest), which independently shows
the collector is running, not frozen. Low coverage is **not** "there is no news".

⚠ **Method note recorded so it is not re-derived next run:** the 09-07 file's probe table was run
**without** `--scope foreign`; a `--scope foreign` probe returns a much smaller count for the same
query (samsung **411** vs **1442**). The two are not comparable. Continuity deltas above are taken
from the **no-scope** re-probes only; the `--scope foreign` rows are today's baseline for future runs.

**(c) The sweep knocks the tunnel down. Fifth replication — and the recovery reading changed.**

| probe | today | 09-07 | 09-06 | 09-05 |
|---|---|---|---|---|
| pre-sweep | **8/8 alive** | 6/6 alive | 6/6 alive | 6/6 alive |
| immediately post-sweep ×4 | **0/4** — `URLError(FileNotFoundError)` on the ngrok endpoint | 0/4, same error | 0/4, same error | 0/4, same error |
| recovery clock (20s polling) | **not run — deliberately** | t+20…t+100 all dead (0/5) | t+60/+80/+100 alive | t+60/+80/+100 alive |
| after **probe-free** idleness | **2/2 alive** (~5 min; NVIDIA 3892, Apple 1297) | 2/2 alive (~2 min) | — | — |

The 09-07 run raised a hypothesis it could not separate: either the outage is simply longer under a
heavier burst, or **each failed probe resets the idle timer**, so 20s polling prevents the recovery
it is trying to detect. This run did **not** poll — it left the endpoint alone (the intervening work
was `yfinance` and `--help` calls, no news traffic) and found it **alive**. That is *consistent with*
the idle-timer reading, but it is still **one observation under a different burst size**; it does not
settle the question. A controlled test (fixed burst, then a single probe at a fixed t, varying only
the polling in between) belongs to `idle_probe`, not here.

**(d) The positional wall reproduces exactly, and did not move this run.** Mapped to **universe
rank** (`us_top300.csv` `rank` column, not the flow-sorted output order): velocities exist for ranks
**1,2,…,52** — verified contiguous, **zero gaps** — and are `None` for **every** rank from **53 to
300**. Wall history: **49 → 50 → 52 → 52**. It is a *volume* threshold at ~104 queries (~2 per
name), not a fixed name list; today it landed on the same slot as yesterday.

⚠ **Reading-order caveat, re-confirmed:** the `names` array in `SECTOR_FLOW_US.json` is sorted by
**`flow_score` descending**, not by universe rank. Computing the wall on array index makes it look
scattered and random. It must be mapped through `data/us_universe/us_top300.csv` `rank` to be seen.

**Sector coverage of the 52 measured names** (recomputed today, not carried over — this is the
shape of the bias, stated numerically):

| sector | measured / total | % |
|---|---:|---:|
| Information Technology | 20/56 | 36% |
| Communication Services | 4/12 | 33% |
| Consumer Staples | 5/19 | 26% |
| Financials | 9/47 | 19% |
| Health Care | 5/32 | 16% |
| Energy | 2/16 | 12% |
| Consumer Discretionary | 3/28 | 11% |
| Industrials | 4/50 | 8% |
| **Materials** | **0/12** | **0%** |
| **Utilities** | **0/15** | **0%** |
| **Real Estate** | **0/12** | **0%** |

**Mechanism, on five independent observations:** the sweep issues ~2 queries per name; at ~52
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
  (today: ~5 min of no news traffic was sufficient). `--scope foreign` remains the hard rule for
  every news call in this runtime, `brief` and `thread` included.
- Operational note for whoever fixes this (not this stage's job, P4): throttle/batch **inside
  `sector_flow`**, or add a local FTS fallback — **not** per-request spacing, which was falsified.

### G2 — Scoring-scale continuity: PASS on scale, FAIL on novelty (fourth consecutive)

`scoring = {vel_axis: false, vel_coverage: 0.1739, n_axes: 3, scored: 299, dropped_missing_axis: 0}`.

**Scale leg PASS.** 09-07: `{3 axes, nonews, 299}`. Today: `{3 axes, nonews, 299}`. Identical scale,
so subtracting the two snapshots is arithmetically legal.

**Novelty leg FAIL.** Today's `asof` is **2026-09-04**; so was 09-07's, 09-06's and 09-05's. Saturday,
Sunday, Labor Day — and now a **pre-open run** — mean the feed has had no new session to give for
four runs. Direct comparison of the two `sector_rotation` blocks (11 fields each, diffed
programmatically):

| sector | wflow | eqflow | delta | breadth | n | top1 | top1_w | ex-top1 | flips | identical to 09-07? |
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

**11 of 11 sectors identical on all 11 fields** (`green`/`red` counts also checked and identical).
The `delta` column still resolves against **2026-09-03**, i.e. it is the **Friday-vs-Thursday**
change already reported three times.

**Permissions:**
- GRANTED: Delta-flow **may** be cited on the 3-axis `nonews` scale — the scale is continuous.
- REVOKED: it may **not** be worded as "today's move", "the latest rotation", "flow shifted", or any
  present-tense change language. It is the **09-03 → 09-04** change and must be labelled with those
  two dates. Any stage that reports it as new information fails EXIT.
- REVOKED: no claim that a sector "improved" or "deteriorated" since the last run. Nothing changed
  because nothing was measured that had not already been measured — **three times**.
- REVOKED: no comparison against any snapshot dated **≤ 2026-09-02** without the clean-baseline
  recomputation the 09-04 preflight documented.

### G3 — Who owns the sector sign: PASS (list printed in full), guard's own blind spot flagged

**Flippers by the built-in `top1_flips_sign` flag: 1 of 11 — Consumer Discretionary only.**
(The full 11-row table with `top1`, `top1_w` and `wflow_ex_top1` is printed in G2 above and is not
duplicated here; the flag is the second-from-last column of that table. A zero would still have
been written as "0 of 11".)

**The guard misses the biggest single-issuer sector in the book.** `top1_flips_sign` is computed
per **ticker**, so a company with two listed share classes counts as two independent names.
Issuer-level rescan (share classes merged by issuer name, all 11 sectors, **recomputed today** —
not carried over):

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

| window | units | within-group residual corr | ARI (1st vs 2nd half) | intersection holes >4d |
|---|--:|--:|--:|--:|
| 250d | **12** | +0.8511 | **0.3874** | 2 (max 8d), sample 249 < 250 |
| 500d | **11** | +0.6147 | **0.2328** | 5 (max 8d) |
| 750d | **10** | +0.5183 | **0.7937** | 8 (max 8d) |

Membership is not merely re-counted, it is **re-drawn**:
- `ANET`+`ETN` are **separate** at 250d but **merge into one unit** at 500d and 750d — and at both
  those windows that merged unit **spans two different book theme labels**
  (`AI-compute-EPICENTER` + `AI-power/electrical`); the tool prints its own warning that
  `MAX_THEME_PCT` is counting one risk as two.
- `AVGO`+`NVDA` merge **only** at 750d.
- `MPC`+`PSX` are the one stable pair (merged at all three windows).

Threshold sensitivity shows the 0.65 choice is itself load-bearing: at 250d the count is **12 for
every threshold from 0.40 to 0.65**, then 10/7/7/5; at 500d 12/12/12/**11**/9/7/5/5; at 750d
12/12/12/12/**10**/9/7/5/5. The 250d window also flags 249 < 250 sample and calendar-intersection
holes, so its flattering +0.8511 fit is the **least** trustworthy of the three — high fit with ARI
0.3874 is exactly the fit-vs-stability inversion the tool warns about (S5).

Numerically identical to 09-07, which is the expected result: all three windows still end on the
same 09-04 close. **Sameness here is not stability** — it is the same measurement repeated.

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
- **Freshness leg FAIL:** file mtime **2026-07-15**, i.e. **55 days** against a ≤8-day bar. The
  sweep itself warns that the cap vector is stale.

**Permissions:**
- GRANTED: per-name flow/RS/OBV/short judgments on the 11 holdings — they are measured.
- REVOKED: **market-cap weights, sector cap shares, and `top1_w%` may not be cited as current.**
  Every weighted number in this run — including all `wflow` and the entire `top1_w` / issuer-share
  column in G3 — rests on a **55-day-old cap vector**. Where a weighted and an equal-weighted
  reading disagree, **the equal-weighted one is the citable one today**.
- REVOKED: no claim that a name is "in / out of the top 300" as of today.

### G6 — Instrumentation accrual rate: FAIL

`snapshot_estimates.py --status`: **28 files** spanning **49 calendar days** (2026-07-22 →
2026-09-08) = **0.57 files/day**. 12 more are needed to reach the 40-day target: **12 days ideal,
~21 days at measured rate = 1.75×** the ideal, past the 1.5× threshold. Inter-save gaps
`[1,1,1,1,1,2,1,1]`, median 1, max 6. Last save is **today** (2026-09-08, 120 names) — the daemon is
running; it is the *rate over the whole span* that fails, which is the D16 trap this gate exists to
catch (counting files looks healthy; counting days does not).

**Permissions:**
- REVOKED: **`kelly_size --ic` may not be reported as an evidence-backed size.** If it appears at
  all it must be labelled **"mechanical 1/4"**, with no IC claim attached.
- REVOKED: no statement of the form "we now have enough samples to measure IC".

### G7 — Tool liveness: PASS with 2 named exceptions

**51 of 53** entry points exit 0 (**19 of 20** `-m module_*`, **32 of 33** `scripts/*.py`).

1. **`module_chart --help` exit=1.** The module has no `--help` handler and prints a
   `module_text_chart` usage line instead. **Live render probe: 3/3** — NVDA, ANET and SPY each
   returned a populated 7-line read block (OBV state + 20d slope, divergence, MA stack, Bollinger,
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

## Consolidated permissions table for 2026-09-08 (what the rest of this run may NOT do)

| # | Revoked | Gate |
|---|---|---|
| 1 | Present **Delta-flow as "today's move"** or any present-tense change language — it is the **09-03 → 09-04** change, now restated for the **fourth** run | **G2** |
| 2 | Say a sector **"improved" / "deteriorated" since the last run** — all 11 sectors are numerically identical to the 09-07 file on all 11 fields | **G2** |
| 3 | Cite **news velocity / theme freshness** from `SECTOR_FLOW_US.json` — including the 52 names that carry one, because they are exactly the 52 largest caps | G1 |
| 4 | Say any sector or name is **"quiet"** on news — 247 of 299 were not measured, they were outaged. Absolute for **Utilities / Materials / Real Estate** (0 names measured each) | **G1** |
| 5 | Promote/demote **Consumer Discretionary** or **Communication Services** on `wflow` — both signs are one issuer's; use `eqflow`/breadth and say which on the line | G3 |
| 6 | Quote a **concentration guard as one number** — must carry `--days` on the same line and note 12/11/10 | G4 |
| 7 | Treat **`AI-compute-EPICENTER` and `AI-power/electrical` as two independent themes** without noting that 500d/750d measure them as one unit | G4 |
| 8 | Cite **market-cap weights / sector cap shares / top1_w% / issuer shares** as current — **55-day-old** cap vector; prefer equal-weighted where the two disagree | G5 |
| 9 | Report **`kelly_size --ic`** as an evidence-backed size — label "mechanical 1/4" | G6 |
| 10 | Cite **`scripts/margin_history.py`** output | G7 |
| 11 | Give **`EA`** any flow/OBV/RS verdict — unmeasured, not neutral | G0 |
| 12 | Compare today's Delta-flow against any snapshot **≤ 2026-09-02** without clean-baseline recomputation | G2 |
| 13 | Compute the news wall on the `names` array index — it is **flow_score-sorted**; the wall is only visible in **universe-rank** order | G1 (method) |
| 14 | Compare a `--scope foreign` news count against a no-scope one — the same query returns **411 vs 1442** | G1 (method, new) |

**Granted this run:** primary-file OBV/flow from `SECTOR_FLOW_US.json` (G0) · the 3-axis `nonews`
scale as continuous with 09-07 (G2, scale leg) · 9 of 11 sector `wflow` signs (G3) · per-name
measurement on all 11 US holdings (G5, coverage leg) · `module_chart` reads (G7) · direct
`module_news_data --scope foreign` calls made outside a sweep burst and after a genuine idle gap (G1).

**Standing implication for the rest of the run:** the price tape now carries **four runs' worth of
no new session**, and today that is a *timing* choice rather than a closed market — the desk is
running 19 minutes before the US open, so the freshest possible close is still Friday's and the
09-08 session will not be readable until tomorrow's run. Whatever is genuinely new today must come
from the **non-price instruments**: FRED macro releases (the first US releases since Friday, since
Labor Day suppressed Monday), direct foreign-scope news, disclosures, and the catalyst calendar.
A run that leans on the flow table is restating Friday for the fourth time.

---

> P4 compliance: no market call, no name-level verdict, no sizing appears above. Sector and ticker
> symbols appear only as *instrument identifiers* (who owns a measurement), never as judgments.
> Nothing here is written to `handoff/` — instrument state is not a market view; HANDOVER reads it.
