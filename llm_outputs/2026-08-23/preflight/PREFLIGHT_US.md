# PREFLIGHT — 2026-08-23 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-23 22:09–22:22 = ET 2026-08-23 09:09–09:22 — SUNDAY, US cash CLOSED
> (and closed Saturday too).** Terminal settled bar **2026-08-21 (Friday close)**; sweep `asof`
> **2026-08-21**. Sweep run fresh at 22:09–22:11 KST with `--refresh` (no artifact reuse), then a
> second time at 22:11–22:13 without refresh.

★ **Two things were measured today that no prior run in this ledger has held.**
> **(1) The six contaminated names are recovered.** Yesterday's §3 logged the tag-layer contamination
> and then wrote *"The three names are unrecoverable — run 1 was not persisted as JSON. Logged as a
> gap, not guessed at."* Today run 1 **was** persisted. The names are named below — and they force a
> **refinement of yesterday's conclusion**: the bias is not upward, it is **outward**.
> **(2) Today's sweep carries zero new price information.** Its 299 scores, 299 tags and 11 sector
> rows are **identical, to the last decimal, to yesterday's persisted file.** Not "similar" — equal.

---

## ① ★ Retraction/refinement — the tag contamination is **bidirectional**, not "selection-biased upward"

Yesterday established the mechanism (`sector_flow.py:224` — `flow_score` never sees `vel` when the
axis is dropped, but `tag = flow_read.flow_tag(p, vel)` always does), and concluded the resulting
breadth was *"selection-biased **upward** … three names were promoted to 🟢 for no reason but having
landed inside an arbitrary 51-name bucket."* That direction was inferred from a single aggregate
(🟢 9 → 6) because the run-1 names were gone.

Today the identical experiment ran with **both runs persisted**. Same price frame, one identical
`asof`, the only difference being which names happened to land inside the news bucket:

| | Run 1 (49 names carried velocity) | Run 2 (0 names did) | Same? |
|---|---|---|---|
| `flow_score`, all 299 names | — | — | ✅ **0 differences** |
| `wflow` / `eqflow` / `delta`, all 11 sectors | — | — | ✅ **0 differences** |
| Universe `wflow` | −0.076 | −0.076 | ✅ |
| Universe 🟢 / 🔴 | **9 / 72** | **6 / 71** | 🚨 no |
| **Tags** | — | — | 🚨 **6 names differ** |

**The six names, and the direction each moved when the news bucket happened to include it:**

| Ticker | Sector | Run 1 (partial coverage) | Run 2 (zero coverage) | Direction |
|---|---|---|---|---|
| `MRVL` | Information Technology | 🟢가속 | 🟡중립 | away from neutral |
| `MA` | Financials | 🟢가속 | 🟡중립 | away from neutral |
| `CVX` | Energy | 🟢가속 | 🟡중립 | away from neutral |
| `MS` | Financials | 🔴분산 | 🟡중립 | away from neutral |
| `JPM` | Financials | 🔴분산 | 🟡중립 | away from neutral |
| `WMT` | Consumer Staples | 🟡중립 | 🔴분산 | **toward** neutral |

★ **Five of six move *away* from neutral; one moves toward it. Three go up, three go down.**
The aggregate 🟢 9→6 that yesterday read as an upward bias is one half of a symmetric effect —
run 1 also carried **one extra 🔴** (72 vs 71). ⇒ **Partial news coverage does not inflate optimism.
It inflates *dispersion*: it manufactures conviction, in whichever direction the news happened to
point, for the arbitrary ~1-in-6 of names that fit inside the bucket.**

Why this matters more than the upward version: an upward bias is correctable by discounting greens.
A **dispersion** bias is not — it corrupts 🟢 and 🔴 symmetrically, so *no* aggregate breadth number
from a partial-coverage run is safe, and no direction of correction exists. It also means the desk's
own instinct ("greens look inflated, read them down") would have been **wrong on JPM and MS**, which
partial coverage marked 🔴 for the same arbitrary reason.

★★ **Yesterday's sharpest line survives and is now strengthened by direct evidence rather than
inference:** *zero* coverage is uniform and therefore safe; *partial* coverage is selection-biased
and therefore not. Today's persisted file is again **run 2** (`vel_coverage = 0.0`), for that reason.
Run 1 is kept beside it as `_sweep_run1.json` so the next run does not have to re-derive this.

Sector rows touched by the contamination (score layer untouched in every case, tag counts only):
Energy (🟢 1→0), Financials (🟢 2→1 · 🔴 10→9), Information Technology (🟢 3→2),
Consumer Staples (🔴 1→2). **Four of eleven sectors would have carried a different breadth reading
purely from bucket membership.**

## ② The sweep produced **no new information at all** — today's file equals yesterday's, element for element

| Quantity | 08-22 persisted | 08-23 persisted | Δ |
|---|---|---|---|
| `asof` | 2026-08-21 | 2026-08-21 | **same bar** |
| `scoring` | `nonews · 3 axes · scored 299 · vel_cov 0.0` | identical | — |
| `flow_score`, 299 names | — | — | **0 differences** |
| `tag`, 299 names | — | — | **0 differences** |
| `wflow`, 11 sectors | — | — | **0 differences** |
| Universe | wflow −0.076 · 🟢6 · 🔴71 | identical | — |

Cause is not a caching bug — it is the calendar. **Friday 08-21 was the last session; Saturday and
Sunday added nothing.** `llm_outputs/sector_flow/history.json` confirms it: the run wrote no new key,
it **overwrote `2026-08-21` in place with the same values**. Tail keys remain
`… 08-18 · 08-19 · 08-20 · 08-21`.

⇒ **`n_new_sessions_since_prior_run = 0`.** The Δflow available today (08-20 → 08-21) is the *same*
Δ yesterday's run already consumed. It may be re-read; it may **not** be presented as movement since
the last run.

⚠ **Filename deviation, logged (14th consecutive run, same reason):** the composition table names this
`preflight/PREFLIGHT.md`; the `industry_kr` desk wrote its rights table there this morning
(08:30 KST). Overwriting a sibling desk's output is not a correction, so the US table is
`PREFLIGHT_US.md` in the same folder — documented practice 08-10 through 08-22. Human decision on
permanent market-suffixing still pending (PROMPT_MAP §6).

---

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** *(5th consecutive US pass)* | Terminal bar **2026-08-21 (Friday)** · Close **300/301** on each of the last four rows (08-18 · 08-19 · 08-20 · 08-21) · last-bar volume / prior-20d median **0.940** (q25 0.782 · q75 1.149, n=300) · `SPY` closes present through **08-21 765.72** ⇒ names and benchmark share one terminal date, **no RS-leg misalignment**. Sole missing name in every column is `EA` (G5). ★ **`n_new_sessions_since_prior_run = 0` — Sunday** |
| **G1** news axis alive | 🔴 **FAIL** *(11th consecutive run)* | Sweep coverage **16.4% (49/299)** then **0.0% (0/299)** on the very next run, same prices — the 08-22 drain reproduced to the decimal. Falsification probe **40/40 valid in a single window, 0 true silences**; cumulative **0 false silences in 360 hand-checks over nine runs** |
| **G2** scoring-scale continuity | 🟡 **PASS (formal) / no subtrahend** | **3-axis (`nonews`) vs 3-axis (`nonews`)** — prior snapshot `2026-08-20._mode = nonews`, and `2026-08-21` was already written yesterday. Subtraction is legal, **but the only Δ that exists (08-20→08-21) is the one yesterday already used.** 0 of 299 scores moved since the prior run |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **1 of 11**: Consumer Staples / `WMT` **28.9% weight** (wflow **−0.013** → ex-top1 **+0.116**). Unchanged from 08-22. Ten sectors print `top1_flips_sign = False` |
| **G4** risk-unit stability | 🔴 **FAIL** *(14th consecutive run; count still hides it)* | 250d **11 units** · 500d **11** · 750d **10**. ★ **250d and 500d both print 11 and disagree on membership** — at 250d the two KR names share `U0` and ANET/ETN are singletons; at 500d that inverts exactly. ARI **0.4902 / 0.1899 / 0.3810** |
| **G5** does the universe cover the book | 🔴 **FAIL** *(staleness + one hole)* | **11/11 US holdings inside `us_top300` AND scored ✅** (all 11 🟡 again). But `us_top300.csv` is **39 days old** (limit ≤8), and **`EA`** is still absent from the sweep (299 of 300) — **11th** consecutive run unmeasurable |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** *(but the daemon fired today, 5th straight day)* | 15 files / **33 calendar days** = **0.45/day** ⇒ measured ETA **≈55 days** to the 40-day target vs ideal 25 = **2.2×** (limit 1.5×). ★ Last save = **today, 2026-08-23** |
| **G7** tool liveness | 🔴 **FAIL** *(14th consecutive, same two)* | **52 entry points** probed (23 modules + 29 scripts), **2** non-zero `--help`: `module_chart` · `scripts/margin_history.py`. Both pass a functional probe ⇒ citation retained **for those command lines only** |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate and it passed).
Identical verdict *pattern* to 08-22 — which is itself the point: **five of these are structural, not
transient, and none of them is being repaired by the passage of days.**

---

## Gate detail

### G0 — bar completeness · date alignment 🟢 PASS (bonus gate · 5th consecutive US pass)
- Price frame `llm_outputs/sector_flow/prices_2026-08-23.pkl`, 85 rows × 301 tickers, downloaded fresh
  with `--refresh` at 22:09 KST.
- Last four sessions **08-18 · 08-19 · 08-20 · 08-21**, each with **300/301 closes present.**
- Benchmark: `SPY` **08-19 769.06 · 08-20 762.60 · 08-21 765.72** — present on the terminal bar, so
  the RS legs (`rs20` / `rs60`) are computed against a benchmark that ends on the **same date** as the
  names. This is the leg that failed catastrophically on the KR side (`^KS11` 08-21 `Close = NaN`
  ⇒ 826 names dropped). **The US side does not have that hole today.**
- Last-bar volume / prior-20d median: median **0.940** (q25 0.782 · q75 1.149, n=300) — a normal,
  complete Friday bar, not a truncated or half-session print.
- Sole missing name in every column: **`EA`** — see G5.
- ★ **`n_new_sessions_since_prior_run = 0`.** Yesterday's run also terminated on 08-21. Two consecutive
  runs now stand on one Friday close.
- 🚫 **Today this gate removes nothing.** But it hands the next stages a constraint that is *not* a
  gate failure and must not be laundered into one: **any sentence of the form "since our last run,
  X moved / turned / accelerated" is false by construction today.** Nothing moved. There was no session.

### G1 — news axis alive 🔴 FAIL (11th consecutive run)
**The drain, reproduced.** Two sweeps, minutes apart, one identical price frame:

| Clock (KST) | Event | News coverage |
|---|---|---|
| 22:09:43–22:09:46 | `fts search Nvidia --days 7 --count --scope foreign` ×3 | **3475 · 3475 · 3475** (tunnel UP) |
| 22:09:50–22:11:37 | **sweep run 1** (`--refresh`, 301 tickers) | **49 / 299 = 16.4%** |
| 22:11:40–22:13:16 | **sweep run 2** (same prices) | **0 / 299 = 0.0%** |
| ≈22:16–22:18 | falsification probe, 40 sweep-silent names, 80 calls | **40 / 40 valid** |

- `SECTOR_FLOW_US.json §scoring` (persisted = run 2): `vel_axis=false` · `vel_coverage=`**0.0** ·
  `n_axes=3` · `scored=`**299** · `dropped_missing_axis=`**0**.
- Both runs tripped the D225 guard, which printed the axis death rather than silently dropping it —
  **the guard works; that is not in question and has not been for eleven runs.**
- **Falsification (actually run, 40 names drawn with a fixed seed from the sweep's own silent set):**
  **40/40 returned real counts, 0 failures, `recent == 0` on none of them.** Velocity median **0.905**
  (min 0.19 `GRMN` · max 2.94 `KEYS`). Samples: `BLK` recent 258 / base 1119 · `IBM` 96 / 568 ·
  `NOW` 80 / 362 · `ADI` 68 / 135 · `COP` 72 / 249.
  ⇒ **Every one of these was recorded as "no velocity" by the sweep minutes earlier.**
- **Cumulative falsification ledger: 360 hand-checks across nine runs, 0 false silences.** The claim
  "the sweep's silence is the pipe, not the news" is no longer an inference; it is the most
  heavily-replicated measurement this desk owns.
- Mechanism inherited from 08-22 (measured there, not re-measured today to avoid re-draining the
  bucket mid-run): **budget ≈ 100 remote calls ≈ 51 names, a hard contiguous cut, cooldown ≈ 90 s.**
  Today's 80-call probe succeeding in full, in one window, after a ~3-minute pause, is **consistent
  with** that budget and does not test its boundary. Cited as inherited, not as re-measured.
- 🚫 **What this run may not do today:**
  1. **Cite the `SECTOR_FLOW` news-velocity axis at all.** Coverage is exactly **0.0%** in the
     persisted file. Not low — zero.
  2. **Call any name or sector "quiet" / "cooling" / "no news" on sweep evidence.** The sweep cannot
     distinguish silence from a spent quota, and 360 hand-checks say it is the quota.
  3. ✅ **Permitted:** direct `fts search` / `brief` / `thread` observation made **outside a sweep
     window**. Today: 3475 (`Nvidia`, d7, foreign) plus the 40-name probe = **43/43 successful direct
     calls.** When cited, write **"direct call outside the sweep window"** on the same line.
  4. **Any sweep re-run in this session invalidates news observations made in that window** — and
     re-runs are pointless today anyway (§2: no new session).

### G2 — scoring-scale continuity 🟡 PASS (formal) / no subtrahend
- Today `n_axes=3` (`vel_axis=false`) / prior snapshot `2026-08-20._mode = nonews`, `2026-08-21._mode
  = nonews` ⇒ **same axis count, subtraction is formally legal.**
- ★ **But there is nothing to subtract.** Against yesterday's persisted file: **0 of 299 scores moved,
  0 of 299 tags moved, 0 of 11 sector `wflow` values moved.** Median abs-Δ is not "small" — it is **0**.
- Five-run snapshot ledger:

  | Run date | `asof` | mode | scored | **`vel_coverage` of the persisted file** | new sessions vs prior run |
  |---|---|---|---:|---:|---:|
  | 08-18 | 08-14 | nonews | 299 | **16.72%** 🚨 partial | — |
  | 08-19 | 08-18 | nonews | 299 | **17.06%** 🚨 partial | 2 |
  | 08-20 | 08-19 | nonews | 299 | **16.39%** 🚨 partial | 1 |
  | 08-21 | 08-20 | nonews | 299 | **16.72%** 🚨 partial | 1 |
  | 08-22 | 08-21 | nonews | 299 | **0.0%** ✅ clean | 1 |
  | **08-23** | **08-21** | nonews | 299 | **0.0%** ✅ clean | **0** |

- ★ **Consequence of §1 that this ledger makes visible for the first time: the four persisted files
  from 08-18 through 08-21 all carry `vel_coverage ≈ 16–17%` — i.e. every one of them has a
  *partial-coverage, dispersion-contaminated tag layer*.** Their `flow_score` and sector `wflow`
  columns are clean (the score layer never sees `vel`), but their 🟢/🔴/`breadth` counts were built
  the same way run 1 built today's. **Only the 08-22 and 08-23 files have a tag layer this desk can
  vouch for.** Any back-reference to breadth in a report dated 08-18…08-21 inherits that defect —
  the correct move is to re-derive breadth from the score column, not to quote the old counts.
- 🚫 **What this run may not do today:** **present any Δflow as change since the last run.** The
  08-20→08-21 Δ is citable as *Friday's move*, and it is the identical Δ yesterday's ROTATION already
  used. Re-labelling it as fresh movement would manufacture a second observation out of one session.

### G3 — who owns the sector sign 🟢 PASS
Full flipper list, all 11 sectors, printed rather than summarised (a silent flipper is exactly how one
company becomes a sector verdict):

| Sector | n | wflow | eqflow | top1 (weight) | wflow ex-top1 | flips sign? |
|---|---:|---:|---:|---|---:|---|
| Health Care | 32 | +0.196 | +0.229 | LLY (19.4%) | +0.205 | no |
| Consumer Discretionary | 28 | +0.122 | +0.103 | AMZN (40.2%) | +0.254 | no |
| Communication Services | 12 | +0.108 | +0.095 | GOOGL (38.3%) | +0.022 | no |
| Energy | 16 | +0.076 | +0.102 | XOM (30.5%) | +0.189 | no |
| Materials | 12 | +0.064 | +0.046 | LIN (24.7%) | +0.201 | no |
| Financials | 47 | +0.003 | −0.034 | BRK-B (13.9%) | +0.034 | no |
| **Consumer Staples** | 19 | **−0.013** | +0.048 | **WMT (28.9%)** | **+0.116** | 🚨 **YES** |
| Information Technology | 56 | −0.231 | −0.102 | NVDA (19.4%) | −0.243 | no |
| Industrials | 50 | −0.259 | −0.231 | CAT (8.7%) | −0.218 | no |
| Real Estate | 12 | −0.543 | −0.446 | WELL (16.9%) | −0.491 | no |
| Utilities | 15 | −0.648 | −0.621 | NEE (17.7%) | −0.659 | no |

- **One flipper of eleven: Consumer Staples.** `WMT` alone carries the sector from **+0.116 to −0.013** —
  a 28.9%-weight single name inverting the sign of a 19-name sector.
- ⚠ Compounding hazard, unique to today: **`WMT` is also one of the six tag-contaminated names (§1)** —
  partial coverage marked it 🔴, zero coverage 🟡. So Consumer Staples is simultaneously the sector
  whose *sign* is owned by one name and the sector whose *breadth* moved with the news bucket.
- 🚫 **What this run may not do today:** **promote or demote Consumer Staples on `wflow`.** ROTATION §2
  must use `eqflow` (+0.048) or `breadth`, and must print `WMT 28.9%` on the same line. The other ten
  sectors carry no flipper restriction.

### G4 — risk-unit stability 🔴 FAIL (14th consecutive run)

| Window | Units | Grouping of the contested names | ARI | within-group resid corr |
|---|---:|---|---:|---:|
| **250d** | **11** | `U0: 028050, 316140` · ANET, ETN, AVGO, NVDA all **singletons** · `U1: MPC, PSX` | 0.4902 | +0.6019 (vs +0.0040 between) |
| **500d** | **11** | `U0: ANET, ETN` · **028050 and 316140 split into singletons** · AVGO, NVDA singletons · `U1: MPC, PSX` | 0.1899 | +0.6111 (vs +0.0217) |
| **750d** | **10** | `U0: ANET, ETN` · **`U1: AVGO, NVDA`** · 028050, 316140 singletons · `U2: MPC, PSX` | 0.3810 | +0.5148 (vs +0.0189) |

- ★ **250d and 500d both print 11 units and mean opposite things.** At 250d the two KR names are one
  risk unit and ANET/ETN are two; at 500d that is exactly inverted. **The count is not a proxy for
  stability, and reporting "11 units" without the window is reporting nothing.**
- Only `MPC, PSX` (energy-refining) is one unit in **all three** windows — the single grouping this
  gate can vouch for.
- Threshold sensitivity (C5): at `dist` 0.40–0.60 **all three windows converge on 12 units.** Only the
  selected 0.65 splits them. The instability is a property of the chosen threshold, not of the data.
- Tool's own S5 warning fires on all three: ARI moves **opposite** to fit — the better the grouping
  looks, the less its membership is reproducible.
- ⚠ Standing structural note: `U0` at 250d mixes **two different book theme labels** (`KR-E&C/plant`,
  `KR-bank-holding`), which `MAX_THEME_PCT` counts as two. At 500d/750d the same warning attaches to
  `ANET + ETN` (`AI-compute-EPICENTER`, `AI-power/electrical`).
- 🚫 **What this run may not do today:** **cite a concentration guard as a single number.** Every
  concentration sentence must carry its `--days` **on the same line as the conclusion**, and must not
  claim the AI-compute names are one unit or two without naming the window that says so.

### G5 — does the universe cover the book 🔴 FAIL (staleness + one hole)
- Book: **11 US holdings + 2 KR.** All 11 US names are in `us_top300.csv` **and** carry a score:
  `ANET +0.417 🟡` · `AVGO −0.221 🟡` · `ETN +0.210 🟡` · `HPE +0.489 🟡` · `MET −0.164 🟡` ·
  `MPC +0.700 🟡` · `NDAQ −0.025 🟡` · `NUE +0.319 🟡` · `NVDA −0.181 🟡` · `PSX +0.728 🟡` ·
  `RTX −0.122 🟡`. **Coverage leg: 0 missing ✅**
- ⚠ **All 11 tag 🟡중립 for the second run running.** With `vel_coverage = 0.0` this is the honest
  output, not a signal — the tag layer has no news input to push any name to an extreme. **"The book
  is all-neutral" is a statement about the instrument today, not about the book.**
- ⚠ **`us_top300.csv` mtime 2026-07-15 — 39 days old** (limit ≤8). Builder warning printed at run
  start: `유니버스 us_top300.csv 39일 경과 — 시총 stale`. A `us_all_v2_candidate.csv` (2026-08-10)
  sits beside it, **unpromoted for 13 days.**
- ⚠ **`EA` absent from the sweep for the 11th consecutive run** — 299 scored of 300 universe rows;
  `EA` has no close on any of the last four bars.
- ⚠ Book-marking defect, **4th consecutive run**: `module_paper_book status` prints **`n/a` for the
  PRICE of both KR holdings** (028050, 316140), with unrealised P&L and stop blank. ★ Total assets
  **17,607,290 KRW** is therefore computed **without marking two positions** — using it as a
  denominator misstates every weight.
- 🚫 **What this run may not do today:**
  1. **No market-cap-weighted claim may rest on the universe's weights** (39-day-old caps).
  2. **No flow / RS / OBV / short verdict on `EA`** — it is **unmeasured**, not quiet.
  3. **No KR-holding P&L, stop, or share-of-book from the book's own numbers**, and **no percentage
     of total assets** while the denominator is unmarked.

### G6 — estimate-snapshot accrual 🔴 FAIL
- `snapshot_estimates.py --status`: **15 files / 33 calendar days** (2026-07-22 → 08-23) = **0.45/day**.
- 25 more days needed to reach the 40-day target: ideal **25 days**, measured **≈55 days** = **2.2×**
  (limit 1.5×). Gaps `[2,1,1,5,1,1,1,1]` · median 2 · max 6.
- ✅ Direction is improving for a 4th run (0.42 → 0.44 → 0.44 → **0.45**) and the daemon has now fired
  **five days straight** (08-19 · 20 · 21 · 22 · 23). It still does not clear the threshold.
- ⚠ Un-backfillable: days not saved are gone permanently.
- 🚫 **What this run may not do today:** **`kelly_size --ic` output may not be reported as a
  measurement-grounded size.** If used, write **"mechanical 1/4"** beside it.

### G7 — tool liveness 🔴 FAIL (14th consecutive, same two)
- **52 entry points probed** — 23 `module_*` packages + 29 `scripts/*.py`. **50 exit 0.**
- **Non-zero (2), both unchanged for fourteen runs:**
  - `module_chart --help` → **exit 1.** Not argparse: the module prints its own usage line
    (`usage: python -m module_text_chart <ticker> [--read]`) and exits non-zero for any unrecognised
    argument, `--help` included. **Functional probe: `python -m module_chart NVDA --days 20` → exit 0,
    wrote `module_chart/output/NVDA_chart.txt`.**
  - `scripts/margin_history.py --help` → **exit 1**, `argparse._expand_help` →
    `ValueError: unsupported format character ')' at index 12`. Help rendering only.
    **Functional probe: `python scripts/margin_history.py NVDA` → exit 0**, FY2009–FY2026 gross margin
    series (max FY2025 75.0% · min FY2009 34.3% · median 56.9%).
- 🚫 **What this run may not do today:** nothing is removed — **but any citation of either tool must
  carry "`--help` is dead; verified by functional output".**
- ⚠ **`--help` remains a weak proxy for liveness, and today shows both failure modes at once:**
  `module_news_data` exits 0 while its data path dies inside every sweep, and `scripts/sector_flow.py`
  exits 0 while producing a file with a zeroed axis. **Exit code 0 is not evidence that a tool measured
  anything.**

---

## Rights removed for this run — one page

1. ★ **No claim of movement since the last run** (G0/G2). **Zero new sessions.** Today's 299 scores,
   299 tags and 11 sector rows are **identical** to 08-22's persisted file. "Turned", "accelerated",
   "rolled over", "since yesterday" are all unavailable. Friday's move (08-20→08-21) is citable **as
   Friday's move**, and must be labelled as the same Δ the prior run already used.
2. **No news-velocity axis citation from the sweep** (G1) — `vel_coverage = 0.0`, exactly zero.
3. **No "quiet / cooling / no news" verdict from sweep silence** (G1) — 40/40 falsified today,
   **360/360 cumulative.**
   ✅ **Exception: direct `fts` / `brief` / `thread` calls outside a sweep window are citable**
   (today 43/43 successful). Write "direct call outside the sweep window" on the same line.
4. **No promotion or demotion of Consumer Staples on `wflow`** (G3) — `WMT` 28.9% flips the sign.
   Use `eqflow` +0.048 or breadth, and print the weight beside it.
5. **No concentration claim as a bare number** (G4) — `--days` must sit on the same line as the
   conclusion. Whether the AI-compute names are one risk unit or two is decided by the window, not
   by the data.
6. **No market-cap-weighted claim resting on universe weights; no flow/RS/OBV/short verdict on `EA`;
   no KR-holding P&L, stop, or share-of-book, and no percent-of-total-assets** (G5).
7. **No `--ic` size reported as measurement-grounded** (G6) — mark it "mechanical 1/4".
8. **`module_chart` and `margin_history` citations carry the "`--help` dead / functionally verified"
   note** (G7).
9. ★ **New, from §1 — no breadth number from a partial-coverage sweep, in either direction.** The
   tag-layer contamination is **bidirectional**: it manufactures 🟢 *and* 🔴 for whichever names land
   in the news bucket. Yesterday's "discount the greens" correction is **retracted** — it would have
   been wrong on `JPM` and `MS`. The only safe tag layer is one built at **zero** coverage, which is
   what today's persisted file is.

### ⚠ The standing fact the next stages inherit
> **The US price instrument is healthy and complete (G0, 5 straight passes) — and it has nothing new
> to say, because there was no session.** The news axis inside the sweep is dead by quota, not by
> silence, for the eleventh consecutive run. So today's live instruments are: **① direct news calls
> outside sweep windows ② the settled Friday 08-21 price frame ③ FRED macro ④ FINRA short-vol /
> CFTC COT positioning ⑤ disclosure & fundamentals ⑥ the inherited carry (`handoff/`).**
> A Sunday run's value is **not** in re-reading Friday's tape. It is in the work that does not need a
> new bar: re-examining the standing view, scoring the open scenarios, and testing what the prior runs
> pre-committed to. Stages that would otherwise reach for Δflow should reach there instead — and say
> so explicitly, rather than dressing a stale Δ as a fresh one.

> ⚠ This document is not written into the carry (`handoff/`) — instrument state is not a market view.
> HANDOVER only reads it.
