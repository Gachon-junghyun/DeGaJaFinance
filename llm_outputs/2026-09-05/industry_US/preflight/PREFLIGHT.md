# PREFLIGHT — 2026-09-05 (Sat) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is not a report, it is a permissions table** — a FAIL is not "be careful", it is
> **"what this run may not cite today"**.
> Execution KST 2026-09-05 **22:09 clock/weekday · 22:09 news probe pre-sweep (6/6)
> · 22:10–22:11 sweep (`--json --refresh`, 301 names) · 22:11–22:12 tool `--help` ×44
> · 22:12–22:14 risk units ×3 windows · 22:12 universe/book/accrual · 22:14 chart live ×3
> · 22:15 news probe post-sweep (0/4) · 22:15–22:17 news recovery-clock probe (6 tries @20s)
> · 22:17 bar-completeness scan · 22:18 sector-sign ownership scan.**
> **Saturday — NYSE is closed and was closed for the whole preflight.** Last completed US session
> **Fri 2026-09-04**, which is settled and fully written. ⇒ Every price statement below is about
> **Friday 09-04 or earlier**, and unlike the last four runs there is **no partial-session
> truncation problem** — the tape is closed, not mid-formation.

★ **Three-line summary**
> ① ✅ **The bar tape is the cleanest it has been in three weeks and it STAYED clean.** The 08-28
>    vendor hole that healed on 09-04 has not regressed: today's fresh 4-month cache carries
>    **exactly 1 NaN Close out of 301 on every one of the last 14 sessions**, and that one name is
>    the same one every session (`EA` — structurally absent, not a hole). `dropped_missing_axis=0`,
>    **299 scored**. ⇒ **No `_REPAIRED.json` is produced and none is needed. OBV/flow may be cited
>    from the PRIMARY file.**
> ② ★ **The news-axis diagnosis is now MECHANISTIC, and it is self-inflicted.** Yesterday's run
>    established the signature is *positional* (a hard cutoff at 50 names inside the sweep's own
>    ~600-query run) and not spacing. Today reproduces the positional wall **exactly** — velocities
>    exist for universe positions **0–48 and nothing at 49 or beyond** — and then closes the loop:
>    the same probe that returned **6/6 before the sweep** returns **0/4 immediately after**, stays
>    dead at t+20s and t+40s, and comes back **alive at t+60s, t+80s, t+100s (3/3, identical count
>    4102)**. ⇒ The sweep's own burst trips the news tunnel at ~49 names / ~98 queries and then keeps
>    hammering a tunnel that needs ~60 idle seconds to recover, so the remaining 250 names can never
>    score. **The pipe is not down; this desk knocks it down.** The failure is the measurement's,
>    not the market's.
> ③ 🔴 **Three structural FAILs are unchanged and are now chronic, not incidents.** Risk units
>    **12 / 11 / 10** across 250/500/750d with differing membership (G4); universe file **52 days
>    stale** (G5 freshness leg, bar ≤8); instrumentation accruing at **0.56/day = 1.8× slower than
>    ideal** (G6). None of the three moved today. They are logged as standing permission
>    revocations, not as new findings.

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | ✅ **PASS — clean, and holding** | Fresh cache 301 cols × 86 rows. NaN Close **1/301 on all 14 last sessions** (`EA` only, always). 08-28 row NaN **1/301** (was 258/301 two runs ago). `dropped_missing_axis=0`, **scored 299**. asof **2026-09-04** (settled Friday close) |
| **G1** | News-axis liveness | 🔴 **FAIL** (sweep axis) · ✅ **direct path LIVE** · ★ mechanism identified | `vel_coverage` **16.39%** (49/299, bar 80%). Probe **6/6 pre-sweep · 0/4 immediately post-sweep · dead t+0/+20/+40s · alive t+60/+80/+100s (3/3)**. Positional wall: velocities at universe positions **0–48**, `None` at **49–299**, zero exceptions |
| **G2** | Scoring-scale continuity | ✅ **PASS** | `n_axes=3`, `mode=nonews`, `scored=299`. `prev` resolves to **2026-09-03** (`nonews`, 298) ⇒ genuine **one-session** Δ. **Both sides computed off healed caches** (the 09-04 run already stored a post-heal 09-03) ⇒ no baseline contamination this run, unlike 09-04's measured 0.1078 mean skew |
| **G3** | Who owns the sector sign | ✅ **PASS** (full list printed) · ⚠ guard blind to the largest case | **1 of 11 flips** — Cons. Disc./**AMZN** (40.2%), `wflow` −0.255 → ex-top1 **+0.068**. ★ Alphabet is **76.6%** of Comm. Services across **two share classes**; `top1_flips_sign` prints **False** (it sees only GOOGL at 38.3%); ex-both-classes `wflow` **−0.389 → +0.272**, swing **0.661** |
| **G4** | Risk-unit stability | 🔴 **FAIL** | 250d **12 units** · 500d **11** · 750d **10**; membership differs. ARI **0.3874 / 0.2328 / 0.7937** vs within-group residual fit **+0.8511 / +0.6147 / +0.5183**. All three windows end **2026-09-04** |
| **G5** | Does the universe cover the book | 🔴 **FAIL** (freshness leg) | Cover ✅ **11/11** US holdings present in `us_top300.csv` (300 rows), missing **0**. Freshness ❌ **52 days** (mtime 2026-07-15; bar ≤8) |
| **G6** | Instrumentation accrual rate | 🔴 **FAIL** | **25 files / 45 calendar days = 0.56/day** ⇒ ETA **~27 days** to the 40-day target vs ideal 15 = **1.8×** (threshold 1.5×). Gap median 1, max 6. Last save 2026-09-04 (1 day ago) |
| **G7** | Tool liveness | 🟡 **PASS with 2 named exceptions** | **42 of 44** `--help` exit 0. `module_chart --help` **exit=1** *but* live render **3/3** (NVDA·ANET·SPY, full `CHART_READ` block present) ⇒ **chart citation stands**. `scripts/margin_history.py` **exit=1** (`ValueError: unsupported format character ')'`; KR-only, unused in this runtime) |

---

## Gate detail

### G0 — Bar completeness ✅ PASS

Fresh `--refresh` pull, `prices_2026-09-05.pkl`, 301 tickers × 86 sessions.

| session | NaN Close / 301 |
|---|---:|
| 2026-08-18 … 2026-09-04 (14 sessions) | **1** on every single one |

The one NaN is **`EA` on all 14 sessions** — a name that is structurally absent from the feed, not
a hole that appears and disappears. Contrast: two runs ago the 2026-08-28 row alone carried
**258/301** NaN. That hole healed on the 09-04 run and **has not regressed**.

⇒ **Permissions granted (not merely "no problem"):**
- ✅ `obv_norm` / `obv_state` / `flow_score` may be cited from the **primary** `SECTOR_FLOW_US.json`.
  No `SECTOR_FLOW_US_REPAIRED.json` exists for this run and none is required.
- ✅ 08-28 closes/volumes may be cited plainly, no "5m-proxy" label, for 300 of 301.
- 🚫 **`EA` may not receive any flow/OBV/RS judgment today** — it is unmeasured, not neutral.
- ✅ `asof` is a **settled Friday close**. Unlike the 09-01→09-04 runs, no partial-bar truncation
  reasoning is needed and none was applied.

### G1 — News-axis liveness 🔴 FAIL on the sweep axis · ✅ LIVE on the direct path

**(a) The axis is dead inside the sweep.** `vel_coverage = 16.39%` (49 of 299) against an 80% bar,
so `sector_flow` dropped the velocity axis and scored **every** name on the same 3 axes
(`mode=nonews`). That drop is correct behaviour — the old implementation silently dropped the axis
for *some* names and inflated the whole book by +0.305.

**(b) The falsification probe says the pipe is alive.** Six named probes immediately **before** the
sweep: **6/6** (`삼성전자` 1565 · `SK하이닉스` 1165 · `NVIDIA` 4102 · `Nvidia` 4102 · `Tesla` 822 ·
`Apple` 1299). So low coverage is **not** "there is no news".

**(c) ★ The new measurement: the sweep knocks the tunnel down, and it recovers on a ~60s clock.**

| probe | result |
|---|---|
| pre-sweep ×6 | **6/6 alive** |
| immediately post-sweep ×4 | **0/4** — `URLError(FileNotFoundError)` on the ngrok endpoint |
| recovery clock, same query (`NVIDIA`, 7d) | t+0s ❌ · t+20s ❌ · t+40s ❌ · **t+60s ✅ 4102** · t+80s ✅ 4102 · t+100s ✅ 4102 |

**(d) The positional wall reproduces exactly.** Velocities exist for universe positions
**0,1,2,…,48** — a contiguous run — and are `None` for **every** position from **49 to 299**.
Zero exceptions in either direction.

⇒ **Mechanism, stated plainly:** the sweep issues ~2 queries per name; at ~49 names / ~98 queries
the tunnel trips; the sweep then continues firing into a dead endpoint for the remaining 250 names,
and because it never idles for 60 seconds the tunnel never recovers inside the run. Yesterday's
run proved spacing was not the variable (8/10 at 1.5s == 8/10 at 9s, 40/40 in a 0s burst); today
supplies the missing half — **cumulative burst volume trips it, and only idleness untrips it.**

⇒ **Permissions revoked for this run (all stages):**
- 🚫 **No theme-freshness or news-velocity citation from `SECTOR_FLOW_US.json`.** The 49 names that
  do carry a velocity are **positions 0–48 = the largest 49 caps**, which is a size-selected
  sample, not a market sample — quoting even those 49 would smuggle a mega-cap bias in.
- 🚫 **No "sector X is quiet" / "no news flow on Y" judgment anywhere in this run.** For 250 of 299
  names the desk did not measure silence; it measured its own outage.
- ✅ **Direct `module_news_data` calls ARE permitted and ARE the required path** for MACRO /
  EVENT_ALPHA / DEEP, provided they are made **outside a sweep burst**. `--scope foreign` remains
  the hard rule.
- ⚠ Operational note for whoever fixes this (not this stage's job, P4): the fix is throttling or
  batching inside `sector_flow`, **not** per-request spacing — spacing was falsified yesterday.

### G2 — Scoring-scale continuity ✅ PASS

`scoring = {vel_axis: false, vel_coverage: 0.1639, n_axes: 3, scored: 299, dropped_missing_axis: 0}`.

History resolution: today's `asof` is **2026-09-04**; `prev_snapshot` walks back to the most recent
key with the **same `_mode`** and lands on **2026-09-03** (`nonews`, 298 names). So the Δ column is a
**one-session** difference on an **identical 3-axis scale** — the subtraction is legal.

Additionally, and unlike the 09-04 run, **the baseline itself is clean**: the 09-03 snapshot stored
by yesterday's run was computed off the already-healed cache, so there is no holed-minus-healed
asymmetry. Yesterday that asymmetry measured mean |Δ| **0.1078** / max **0.5570** / 19 sign flips and
had to be repaired inside the preflight. **Today it is structurally absent** (both sides post-heal),
so no baseline repair was performed and none is claimed.

⇒ ✅ **Δflow may be cited this run**, as a one-session change, labelled `nonews` 3-axis.
⇒ 🚫 It may **not** be compared against any snapshot dated **2026-09-02 or earlier** without the
   clean-baseline recomputation that the 09-04 preflight documented.

### G3 — Who owns the sector sign ✅ PASS (list printed) · ⚠ the guard's own blind spot

**Full 11-sector flipper list (printed in full, per EXIT CHECK — "0 would still be written as 0"):**

| sector | n | wflow | eqflow | top1 | top1 w% | wflow ex-top1 | flips? |
|---|--:|--:|--:|---|--:|--:|:--:|
| Energy | 16 | +0.440 | +0.562 | XOM | 30.5 | +0.621 | False |
| Health Care | 32 | +0.098 | +0.190 | LLY | 19.4 | +0.232 | False |
| Utilities | 15 | +0.071 | +0.050 | NEE | 17.7 | +0.011 | False |
| Materials | 12 | −0.025 | −0.107 | LIN | 24.7 | −0.048 | False |
| Information Technology | 56 | −0.090 | −0.195 | NVDA | 19.4 | −0.104 | False |
| Real Estate | 12 | −0.116 | −0.124 | WELL | 16.9 | −0.213 | False |
| Financials | 47 | −0.118 | −0.023 | BRK-B | 13.9 | −0.061 | False |
| Consumer Staples | 19 | −0.182 | −0.098 | WMT | 28.9 | −0.080 | False |
| **Consumer Discretionary** | 28 | **−0.255** | −0.280 | **AMZN** | **40.2** | **+0.068** | **True** |
| Industrials | 50 | −0.379 | −0.354 | CAT | 8.7 | −0.379 | False |
| Communication Services | 12 | −0.389 | −0.035 | GOOGL | 38.3 | −0.294 | False |

**★ The guard misses the biggest single-issuer sector in the book.** `top1_flips_sign` is computed
per **ticker**, so a company listed under two share classes is counted as two independent names.
Issuer-level concentration scan:

| sector | issuer | issuer share of sector cap | wflow | wflow ex-issuer | swing |
|---|---|--:|--:|--:|--:|
| **Communication Services** | **Alphabet (GOOGL+GOOG)** | **76.6%** | −0.389 | **+0.272** | **0.661** |
| Consumer Discretionary | Amazon | 40.2% | −0.255 | +0.068 | 0.323 |
| Energy | ExxonMobil | 30.5% | +0.440 | +0.621 | 0.181 |

Comm. Services' negative sign is **one company's**, and the flag prints `False`. (Note `eqflow`
−0.035 vs `wflow` −0.389 independently exposes this: equal-weighted the sector is flat.)

⇒ **Permissions:**
- 🚫 **Consumer Discretionary may not be promoted or demoted on its `wflow` bucket** in ROTATION §2.
  Use `eqflow` (−0.280, which agrees) or breadth, or hold.
- 🚫 **Communication Services may not be promoted or demoted on `wflow` either**, despite the flag
  reading `False` — the flag is measuring the wrong unit. Its `wflow` is an Alphabet quote.
  Use `eqflow` (−0.035) or breadth, and say which was used on the same line.
- ✅ The other 9 sectors' `wflow` signs survive a top-1 removal and may be cited as sector-level.

### G4 — Risk-unit stability 🔴 FAIL

Same book (11 US + 2 KR names), same bench (SPY), same 0.65 distance threshold, three windows all
ending **2026-09-04**:

| window | units | within-group residual corr | between | ARI (1st half vs 2nd) |
|---|--:|--:|--:|--:|
| 250d (249 trading days actual) | **12** | +0.8511 | +0.0107 | **0.3874** |
| 500d | **11** | +0.6147 | +0.0215 | **0.2328** |
| 750d | **10** | +0.5183 | +0.0184 | **0.7937** |

Membership is not merely re-counted, it is re-drawn: `ANET`+`ETN` merge into one unit at 500d and
750d but are separate at 250d; `AVGO`+`NVDA` merge only at 750d. And at 500/750d the merged
`ANET`+`ETN` unit **spans two different book theme labels**, i.e. `MAX_THEME_PCT` is counting one
risk as two. The 250d window also flags 249 < 250 sample and calendar-intersection holes (max 8
days), so its flattering +0.8511 fit is the least trustworthy of the three, not the most.

⇒ **Permissions:**
- 🚫 **No concentration guard may be quoted as a single number today.**
- ✅ Any concentration statement must carry the `--days` window **on the same line as the claim**,
  and must note that the count is 12/11/10 depending on that choice.

### G5 — Does the universe cover the book 🔴 FAIL (freshness leg only)

- **Coverage leg ✅:** all **11** US book holdings — ANET, AVGO, ETN, HPE, MET, MPC, NDAQ, NUE,
  NVDA, PSX, RTX — are present in `data/us_universe/us_top300.csv` (300 rows). **Missing: 0.**
  (The two KR holdings 028050 / 316140 are out of scope for a `--market us` universe by design.)
- **Freshness leg ❌:** file mtime **2026-07-15**, i.e. **52 days** old against a ≤8-day bar. The
  sweep itself warns on this (`universe 52 days stale`).

⇒ **Permissions:**
- ✅ Per-name flow/RS/OBV/short judgments on the 11 holdings are permitted — they are measured.
- 🚫 **Market-cap weights, sector cap shares, and `top1_w%` may not be cited as current.** Every
  weighted number in this run (including all of G3's `wflow` and the `top1_w` column) rests on a
  **52-day-old cap vector**. Where a weighted and an equal-weighted reading disagree, the
  equal-weighted one is the citable one today.
- 🚫 No claim that a name is "in / out of the top 300" as of today.

### G6 — Instrumentation accrual rate 🔴 FAIL

`snapshot_estimates.py --status`: **25 files** spanning **45 calendar days** (2026-07-22 →
2026-09-04) ⇒ **0.56 files/day**. 15 more needed to reach the 40-day target: **15 days ideal,
~27 days at measured rate = 1.8×** the ideal, past the 1.5× threshold. Inter-save gaps: median 1,
max 6. Last save 1 day ago (2026-09-04, 120 names).

⇒ **Permissions:**
- 🚫 **`kelly_size --ic` may not be reported as an evidence-backed size.** If it appears at all it
  must be labelled **"mechanical 1/4"**, with no IC claim attached.
- 🚫 No statement of the form "we now have enough samples to measure IC".

### G7 — Tool liveness 🟡 PASS with 2 named exceptions

**42 of 44** entry points exit 0 (19 `-m module_*`, 25 `scripts/*.py`).

1. **`module_chart --help` exit=1.** The module has no `--help` handler and prints a `module_text_chart`
   usage line instead. **Live render probe: 3/3** — NVDA, ANET, SPY each wrote a chart file with a
   populated `CHART_READ` block (OBV state, divergence, MA stack, Bollinger, turn verdict, trigger,
   swing-low stop). ⇒ **`module_chart` output may be cited.** The `--help` failure is cosmetic and is
   recorded so it is not re-litigated next run.
2. **`scripts/margin_history.py` exit=1** — `ValueError: unsupported format character ')' (0x29) at
   index 12`, a formatting bug in its own help string. **KR-only tool, not used by this runtime.**
   ⇒ 🚫 Its output may not be cited today (it is also not wanted today).

⇒ Every other tool this run intends to use is live: `module_macro_us`, `module_news_data`,
`module_flow`, `module_disclosure_us`, `module_fundamentals_us`, `module_business_us`,
`module_valuation`, `module_watchlist`, `module_paper_book`, `module_report_tags`,
`module_inflection`, `module_evidence`, `module_epistemics`, `module_math_check`,
`scripts/sector_flow.py`, `us_live_shortlist`, `us_setup_screener`, `us_flow`, `flow_read`,
`risk_units`, `drift_watch`, `cycle_exposure`, `catalyst_calendar`, `action_bracket`,
`exposure_rule`, `kelly_size`, `report_lint`, `reject_ledger`, `missed_ledger`, `ic_ledger`,
`measure_ic`, `handoff_compact`, `handoff_id_audit`, `leak_scan`, `company_score`,
`axis_inflection`, `axis_window_flow`, `snapshot_estimates`.

---

## Consolidated permissions table for 2026-09-05 (what the rest of this run may NOT do)

| # | Revoked |
|---|---|
| 1 | Cite **news velocity / theme freshness** from `SECTOR_FLOW_US.json` (G1) — including the 49 names that do carry one, because they are the 49 largest caps, a size-selected sample |
| 2 | Say any sector or name is **"quiet"** on news (G1) — 250 of 299 were not measured |
| 3 | Promote/demote **Consumer Discretionary** or **Communication Services** on `wflow` (G3) — both signs are one issuer's; use `eqflow`/breadth and say so on the line |
| 4 | Quote a **concentration guard as one number** (G4) — must carry `--days` on the same line, and note 12/11/10 |
| 5 | Cite **market-cap weights / sector cap shares / top1_w%** as current (G5) — 52-day-old cap vector; prefer equal-weighted where the two disagree |
| 6 | Report **`kelly_size --ic`** as an evidence-backed size (G6) — label "mechanical 1/4" |
| 7 | Cite **`scripts/margin_history.py`** output (G7) |
| 8 | Give **`EA`** any flow/OBV/RS verdict (G0) — unmeasured, not neutral |
| 9 | Compare today's Δflow against any snapshot **≤ 2026-09-02** without clean-baseline recomputation (G2) |

**Granted this run:** primary-file OBV/flow (G0) · one-session Δflow on the 3-axis `nonews` scale
(G2) · 9 of 11 sector `wflow` signs (G3) · per-name measurement on all 11 US holdings (G5) ·
`module_chart` reads (G7) · direct `module_news_data --scope foreign` calls made outside a sweep
burst (G1).

---

> P4 compliance: no market call, no name-level verdict, no sizing appears above. Sector and ticker
> symbols appear only as *instrument identifiers* (who owns a measurement), never as judgments.
> Nothing here is written to `handoff/` — instrument state is not a market view; HANDOVER reads it.
