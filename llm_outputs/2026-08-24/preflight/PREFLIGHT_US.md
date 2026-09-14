# PREFLIGHT — 2026-08-24 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-24 22:10–22:30 = ET 2026-08-24 09:10–09:30 — MONDAY PRE-MARKET, US cash
> not yet open.** Terminal settled bar **2026-08-21 (Friday close)**; sweep `asof` **2026-08-21**.
> Sweep run fresh at 22:11 KST with `--refresh` (new price download, `prices_2026-08-24.pkl`),
> then a second time at 22:13 without refresh.

★ **Today's run produced one measurement that overturns the framing this ledger has carried since
08-22, and one that repeats a state no prior pair of runs had held.**
> **(1) The news bucket is not arbitrary — it is the top-49 by market capitalisation, exactly.**
> Universe positions **0–48**, a perfectly contiguous block from rank 1, and it is the **identical
> 49 names as yesterday (49/49 overlap, 0 differences).** Those 49 names are **16.4% of the universe
> by count but 69.0% of it by market cap.** Yesterday's phrase *"an arbitrary ~1-in-6 bucket"* is
> **retracted** — the contamination is deterministic and it lands on the cohort that owns
> **two-thirds of the weight.**
> **(2) The third consecutive persisted file is element-identical.** 08-22 = 08-23 = 08-24, to the
> last decimal, across 299 scores, 299 tags and 11 sector rows. `n_new_sessions_since_prior_run = 0`
> for the **second** run running.

---

## ① ★ Retraction — the contaminated bucket is **deterministic and mega-cap**, not "arbitrary"

Yesterday established the mechanism (`sector_flow.py:224` — `flow_score` never sees `vel` when the
axis is dropped, but `tag = flow_read.flow_tag(p, vel)` always does) and correctly identified the
effect as **bidirectional dispersion** rather than upward bias. That conclusion stands. What does
**not** stand is the description of *which* names get contaminated. Yesterday wrote:
*"three names were promoted to 🟢 for no reason but having landed inside an **arbitrary** 51-name
bucket"* — and the standing note inherited the budget mechanism (≈100 remote calls ≈51 names,
"a hard contiguous cut") **as inference, never as a direct positional measurement.**

Today the positions were measured directly against `data/us_universe/us_top300.csv` row order
(which is `rank` ascending = market cap descending):

| Question | Measurement |
|---|---|
| How many names carried `velocity` in run 1? | **49 of 299** |
| Their positions in universe (market-cap) order | **`[0, 1, 2, … 48]`** — contiguous, from rank 1 |
| Is it the top-49 block? | ✅ **True**, exactly |
| Same 49 names as yesterday's run 1? | ✅ **49 / 49 overlap · 0 today-only · 0 yesterday-only** |
| Share of universe **by count** | **16.4%** |
| Share of universe **by market cap** | ★ **69.0%** |

⇒ **The budget mechanism is now confirmed by position, not inferred from a count.** The sweep walks
the universe in market-cap order, spends its ≈100 remote calls on the first ~50 names, and every
name from rank 50 down gets `velocity = None`. This is reproducible to the name across days.

★ **Why the correction matters more than the original finding.** "An arbitrary 1-in-6 of names"
invites the reading that the damage is scattered thin and averages out across a sector. It does the
opposite. The contaminated cohort **is** the mega-cap cohort — the same names that G3 shows own the
sector signs. A tag flip on `WMT` moves **28.9%** of Consumer Staples; a tag flip on the 250th name
would move ~0.3% of anything, and the 250th name is precisely the one that **can never be
contaminated**, because it never gets a news call at all.

**The six names that changed tag between run 1 (partial) and run 2 (zero), with their weight inside
their own sector:**

| Ticker | Sector | Sector weight | Run 1 (49 names had velocity) | Run 2 (0 did) | Direction |
|---|---|---:|---|---|---|
| `CVX` | Energy | **18.4%** | 🟢가속 | 🟡중립 | away from neutral (up) |
| `JPM` | Financials | **11.5%** | 🔴분산 | 🟡중립 | away from neutral (down) |
| `MA` | Financials | 5.7% | 🟢가속 | 🟡중립 | away from neutral (up) |
| `ORCL` | Information Technology | 2.0% | 🟢가속 | 🟡중립 | away from neutral (up) |
| `MRVL` | Information Technology | 1.0% | 🟢가속 | 🟡중립 | away from neutral (up) |
| `WMT` | Consumer Staples | **28.9%** | 🟡중립 | 🔴분산 | **toward** an extreme under *zero* coverage |

- **Five of six moved away from neutral under partial coverage; `WMT` moved the other way.**
  The bidirectional finding from 08-23 replicates: partial coverage manufactured **4 extra 🟢**
  (universe 🟢 10 vs 6) *and* **1 extra 🔴** (`JPM`), while suppressing one (`WMT`). Universe 🔴 is
  **71 in both runs** — the reds net out exactly, as they did yesterday.
- ★ **Five of these six names are the same six as yesterday** (`CVX` `JPM` `MA` `MRVL` `WMT`
  unchanged; `MS` → `ORCL` is the sole substitution). Combined with the 49/49 bucket identity, this
  says the contamination is not noise that a second run would wash out — **it is a stable, repeatable
  defect that reproduces the same names on consecutive days.**

Sector rows touched (score layer untouched in every case — tag counts only):
Energy (🟢 1→0) · Financials (🟢 2→1 · 🔴 10→9) · Information Technology (🟢 4→2) ·
Consumer Staples (🔴 1→2). **Four of eleven sectors would have carried a different breadth reading
purely from bucket membership — and, per §1, "bucket membership" now means "is a mega-cap".**

Today's persisted file is again **run 2** (`vel_coverage = 0.0`), for the reason established 08-22
and unchanged: *zero* coverage is uniform and therefore safe; *partial* coverage is
selection-biased — and now measurably biased toward the heaviest names — and therefore not.
Run 1 is kept beside it as `_sweep_run1.json`.

## ② The sweep again produced no new information — third consecutive identical file

| Quantity | 08-22 persisted | 08-23 persisted | **08-24 persisted** | Δ |
|---|---|---|---|---|
| `asof` | 2026-08-21 | 2026-08-21 | **2026-08-21** | **same bar, three runs** |
| `scoring` | `nonews · 3 axes · 299 · vel_cov 0.0` | identical | identical | — |
| `flow_score`, 299 names | — | — | — | **0 differences vs 08-23** |
| `tag`, 299 names | — | — | — | **0 differences** |
| `wflow`, 11 sectors | — | — | — | **0 differences** |
| Universe | wflow −0.076 · 🟢6 · 🔴71 | identical | identical | — |

Cause is the calendar again, one step further along than yesterday. Yesterday was Sunday. **Today is
Monday 09:10 ET — twenty minutes before the opening bell.** Friday 08-21 is still the last settled
session. `llm_outputs/sector_flow/history.json` confirms it: tail keys remain
`… 08-18 · 08-19 · 08-20 · 08-21`; the run wrote no new key and overwrote `2026-08-21` in place with
identical values.

⇒ **`n_new_sessions_since_prior_run = 0`, for the second consecutive run.** The Δflow available today
(08-20 → 08-21) is the same Δ that both the 08-23 and 08-22 runs already consumed. It may be re-read;
it may **not** be presented as movement since the last run.

⚠ **Timing note that the next stages must carry:** unlike Sunday, the market **will** open during
this desk's working window. Any price fact in this run is a **Friday** fact, and if a stage runs past
09:30 ET it must not blend a live quote into a frame whose `asof` is 08-21 (the D-class error this
repo logs as "intraday bar read as a close").

⚠ **Filename deviation, logged (15th consecutive run):** the composition table names this
`preflight/PREFLIGHT.md`. Today the `industry_kr` desk **did not** write one (its 08-24 output folder
exists, no `preflight/`), so the sibling-collision reason that produced the deviation on 08-10…08-23
is **absent today** — the name is kept anyway, per the unattended rule of defaulting to the most
recent documented practice, and to keep the fifteen-run ledger greppable under one filename. Human
decision on permanent market-suffixing still pending (PROMPT_MAP §6).

---

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** *(6th consecutive US pass)* | Terminal bar **2026-08-21 (Friday)** · Close **300/301** on each of the last four rows (08-18 · 08-19 · 08-20 · 08-21) · last-bar volume / prior-20d median **0.940** (q25 0.782 · q75 1.149, n=300) · `SPY` closes present through **08-21 765.72** ⇒ names and benchmark share one terminal date, **no RS-leg misalignment**. Sole missing name in every column is `EA` (G5). ★ **`n_new_sessions_since_prior_run = 0` — Monday pre-market** |
| **G1** news axis alive | 🔴 **FAIL** *(12th consecutive run)* | Sweep coverage **16.4% (49/299)** then **0.0% (0/299)** on the very next run, same prices — the drain reproduced to the decimal for the third day. Falsification probe **40/40 valid calls, 0 failures, 0 false silences**; cumulative **400 hand-checks over ten runs, 0 false silences**. ★ The 49 that *do* get counted are the **top-49 by market cap = 69.0% of universe weight** |
| **G2** scoring-scale continuity | 🟡 **PASS (formal) / no subtrahend** | **3-axis (`nonews`) vs 3-axis (`nonews`)** — prior snapshots `2026-08-20._mode` and `2026-08-21._mode` both `nonews`. Subtraction is formally legal, **but the only Δ that exists (08-20→08-21) has now been consumed by two prior runs.** 0 of 299 scores moved |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **1 of 11**: Consumer Staples / `WMT` **28.9% weight** (wflow **−0.013** → ex-top1 **+0.116**). Unchanged from 08-22 and 08-23. Ten sectors print `top1_flips_sign = False` |
| **G4** risk-unit stability | 🔴 **FAIL** *(15th consecutive run; the count still hides it)* | 250d **11 units** · 500d **11** · 750d **10**. ★ **250d and 500d both print 11 and disagree on membership** — at 250d the two KR names share `U0` and ANET/ETN are singletons; at 500d that inverts exactly. ARI **0.4902 / 0.1899 / 0.3810** |
| **G5** does the universe cover the book | 🔴 **FAIL** *(staleness + one hole)* | **11/11 US holdings inside `us_top300` AND scored ✅** (all 11 🟡 for a third run). But `us_top300.csv` is **40 days old** (limit ≤8), and **`EA`** is still absent from the sweep (299 of 300) — **12th** consecutive run unmeasurable |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** *(but the daemon fired today, 6th straight day)* | 16 files / **34 calendar days** = **0.47/day** ⇒ measured ETA **≈51 days** to the 40-day target vs ideal 24 = **2.1×** (limit 1.5×). ★ Last save = **today, 2026-08-24** |
| **G7** tool liveness | 🔴 **FAIL** *(15th consecutive, same two)* | **52 entry points** probed (23 modules + 29 scripts), **2** non-zero `--help`: `module_chart` · `scripts/margin_history.py`. Both pass a functional probe ⇒ citation retained **for those command lines only** |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate and it passed).
Identical verdict *pattern* to 08-22 and 08-23 — three days, no repair. **These five are structural.**

---

## Gate detail

### G0 — bar completeness · date alignment 🟢 PASS (bonus gate · 6th consecutive US pass)
- Price frame `llm_outputs/sector_flow/prices_2026-08-24.pkl`, **85 rows × 301 tickers**, downloaded
  fresh with `--refresh` at 22:11 KST (a genuinely new download, not a cache hit — the 08-23 pkl was
  not reused).
- Last four sessions **08-18 · 08-19 · 08-20 · 08-21**, each with **300/301 closes present.**
- Benchmark: `SPY` **08-18 767.45 · 08-19 769.06 · 08-20 762.60 · 08-21 765.72** — present on the
  terminal bar, so the RS legs (`rs20` / `rs60`) are computed against a benchmark ending on the
  **same date** as the names. This is the leg that failed catastrophically on the KR side
  (`^KS11` 08-21 `Close = NaN` ⇒ 826 names dropped). **The US side does not have that hole today.**
- Last-bar volume / prior-20d median: median **0.940** (q25 0.782 · q75 1.149, n=300) — a normal,
  complete Friday bar. Identical to yesterday's figure, because it is the identical bar.
- Sole missing name in every column: **`EA`** — see G5.
- ★ **`n_new_sessions_since_prior_run = 0` for the second run running.** Three consecutive runs
  (08-22 · 08-23 · 08-24) now stand on one Friday close.
- 🚫 **This gate removes nothing** — but it hands the next stages a constraint that must not be
  laundered into a market observation: **any sentence of the form "since our last run, X moved /
  turned / accelerated" is false by construction today.** There was no session.
- ⚠ **New constraint vs yesterday:** the US open lands at **09:30 ET, inside this run's window.**
  A quote pulled after the bell is not part of this frame. If a later stage cites one, it must be
  labelled a **live intraday print**, never merged into an `asof = 2026-08-21` reading.

### G1 — news axis alive 🔴 FAIL (12th consecutive run)
**The drain, reproduced for a third day, and this time located.**

| Clock (KST) | Event | News coverage |
|---|---|---|
| 22:10:0x ×3 | `fts search Nvidia --days 7 --count --scope foreign` | **3704 · 3704 · 3704** (tunnel UP; 08-23 read 3475 ⇒ **+229 new foreign articles**, the collector is alive and moving) |
| 22:10 | `fts search 삼성전자 --days 7 --count` (the guard's own suggested probe) | **1537** |
| 22:11–22:13 | **sweep run 1** (`--refresh`, 301 tickers) | **49 / 299 = 16.4%** |
| 22:13–22:15 | **sweep run 2** (same prices) | **0 / 299 = 0.0%** |
| ≈22:20–22:24 | falsification probe, 40 run-1-silent names, 80 calls | **40 / 40 valid** |

- `SECTOR_FLOW_US.json §scoring` (persisted = run 2): `vel_axis=false` · `vel_coverage=`**0.0** ·
  `n_axes=3` · `scored=`**299** · `dropped_missing_axis=`**0**.
- Both runs tripped the D225 guard, which printed the axis death rather than silently dropping it.
  **The guard works; that has not been in question for twelve runs.**
- ★ **The bucket is now positionally identified (§1): universe ranks 0–48, contiguous from the top,
  identical names two days running, 69.0% of universe market cap.** The inherited claim
  ("budget ≈100 remote calls ≈51 names, hard contiguous cut") is **confirmed by direct measurement**
  and is no longer cited as inherited.
- **Falsification (actually run; 40 names drawn with fixed seed 20260824 from run 1's own 250-name
  silent set):** **40/40 returned real counts, 0 failures.** Exactly **one** name — `TRV`
  (recent 0 / base 5) — is a genuine 7-day quiet, and even there the pipe answered with a real zero
  rather than a `None`. Velocity median **1.180** (min `TRV` 0.00 · max `PDD` 4.69).
  Samples: `NDAQ` 13/12835 · `AXP` 68/513 · `STX` 124/439 · `COHR` 50/245 · `MDT` 30/143 ·
  `A` 10/27 · `LIN` 1/26 · `CSX` 1/15.
  ⇒ **Every one of these was recorded as "no velocity" by the sweep minutes earlier.**
- **Cumulative falsification ledger: 400 hand-checks across ten runs, 0 false silences.** The claim
  "the sweep's silence is the pipe, not the news" is the most heavily-replicated measurement this
  desk owns.
- 🚫 **What this run may not do today:**
  1. **Cite the `SECTOR_FLOW` news-velocity axis at all.** Coverage is exactly **0.0%** in the
     persisted file. Not low — zero.
  2. **Call any name or sector "quiet" / "cooling" / "no news" on sweep evidence.** The sweep cannot
     distinguish silence from a spent quota, and 400 hand-checks say it is the quota.
  3. ✅ **Permitted:** direct `fts search` / `brief` / `thread` observation made **outside a sweep
     window**. Today: 4 tunnel probes + the 40-name probe = **44/44 successful direct calls.**
     When cited, write **"direct call outside the sweep window"** on the same line.
  4. **Any sweep re-run in this session invalidates news observations made in that window** — and a
     re-run is pointless today anyway (§2: no new session).
  5. ★ **New:** **do not describe the news-coverage defect as random or self-cancelling.** It is
     deterministic and mega-cap-selective. Any stage that wants a breadth number must take it from
     the **score** column, which never sees `vel`.

### G2 — scoring-scale continuity 🟡 PASS (formal) / no subtrahend
- Today `n_axes=3` (`vel_axis=false`) / prior snapshots `2026-08-20._mode = nonews` and
  `2026-08-21._mode = nonews` ⇒ **same axis count, subtraction is formally legal.**
- ★ **But there is nothing to subtract.** Against yesterday's persisted file: **0 of 299 scores moved,
  0 of 299 tags moved, 0 of 11 sector `wflow` values moved.** Median abs-Δ is not "small" — it is **0**.
- Seven-run snapshot ledger:

  | Run date | `asof` | mode | scored | **`vel_coverage` of the persisted file** | new sessions vs prior run |
  |---|---|---|---:|---:|---:|
  | 08-18 | 08-14 | nonews | 299 | **16.72%** 🚨 partial | — |
  | 08-19 | 08-18 | nonews | 299 | **17.06%** 🚨 partial | 2 |
  | 08-20 | 08-19 | nonews | 299 | **16.39%** 🚨 partial | 1 |
  | 08-21 | 08-20 | nonews | 299 | **16.72%** 🚨 partial | 1 |
  | 08-22 | 08-21 | nonews | 299 | **0.0%** ✅ clean | 1 |
  | 08-23 | 08-21 | nonews | 299 | **0.0%** ✅ clean | 0 |
  | **08-24** | **08-21** | nonews | 299 | **0.0%** ✅ clean | **0** |

- ★ **§1 sharpens the consequence already logged here.** The four persisted files from 08-18 through
  08-21 carry `vel_coverage ≈ 16–17%` — a partial-coverage tag layer. Yesterday's note said their
  breadth counts were built "the same way run 1 built today's". Today adds *which names*: the
  contamination in those four files sat on **the top-49 mega-caps**, i.e. **69% of the weight**, not
  on a scattered sixth of the list. Their `flow_score` and sector `wflow` columns remain clean (the
  score layer never sees `vel`). **Only the 08-22, 08-23 and 08-24 files have a tag layer this desk
  can vouch for.** Correct move for any back-reference: re-derive breadth from the score column,
  never quote the old counts.
- 🚫 **What this run may not do today:** **present any Δflow as change since the last run.** The
  08-20→08-21 Δ is citable as *Friday's move*, and it is the identical Δ the last **two** runs
  already used. Re-labelling it as fresh movement would manufacture a third observation from one
  session.

### G3 — who owns the sector sign 🟢 PASS
Full flipper list, all 11 sectors, printed rather than summarised (a silent flipper is exactly how one
company becomes a sector verdict):

| Sector | n | wflow | eqflow | breadth | top1 (weight) | wflow ex-top1 | flips sign? |
|---|---:|---:|---:|---:|---|---:|---|
| Health Care | 32 | +0.196 | +0.229 | +0.03 | LLY (19.4%) | +0.205 | no |
| Consumer Discretionary | 28 | +0.122 | +0.103 | +0.00 | AMZN (40.2%) | +0.254 | no |
| Communication Services | 12 | +0.108 | +0.095 | +0.00 | GOOGL (38.3%) | +0.022 | no |
| Energy | 16 | +0.076 | +0.102 | +0.00 | XOM (30.5%) | +0.189 | no |
| Materials | 12 | +0.064 | +0.046 | +0.08 | LIN (24.7%) | +0.201 | no |
| Financials | 47 | +0.003 | −0.034 | +0.02 | BRK-B (13.9%) | +0.034 | no |
| **Consumer Staples** | 19 | **−0.013** | +0.048 | +0.05 | **WMT (28.9%)** | **+0.116** | 🚨 **YES** |
| Information Technology | 56 | −0.231 | −0.102 | +0.04 | NVDA (19.4%) | −0.243 | no |
| Industrials | 50 | −0.259 | −0.231 | +0.00 | CAT (8.7%) | −0.218 | no |
| Real Estate | 12 | −0.543 | −0.446 | +0.00 | WELL (16.9%) | −0.491 | no |
| Utilities | 15 | −0.648 | −0.621 | +0.00 | NEE (17.7%) | −0.659 | no |

- **One flipper of eleven: Consumer Staples.** `WMT` alone carries the sector from **+0.116 to −0.013** —
  a 28.9%-weight single name inverting the sign of a 19-name sector. Third consecutive run.
- ⚠ Compounding hazard, and §1 makes it structural rather than coincidental: **`WMT` is also one of
  the six tag-contaminated names.** It is contaminated *because* it is a mega-cap, and it is the
  flipper *because* it is a mega-cap. **The two defects share a cause.** The same reasoning attaches
  to `CVX` (18.4% of Energy) and `JPM` (11.5% of Financials) — both contaminated, both heavy, though
  neither flips its sector's sign today.
- 🚫 **What this run may not do today:** **promote or demote Consumer Staples on `wflow`.** ROTATION §2
  must use `eqflow` (+0.048) or `breadth` (+0.05), and must print `WMT 28.9%` on the same line. The
  other ten sectors carry no flipper restriction.

### G4 — risk-unit stability 🔴 FAIL (15th consecutive run)

| Window | Units | Grouping of the contested names | ARI | within-group resid corr |
|---|---:|---|---:|---:|
| **250d** | **11** | `U0: 028050, 316140` · ANET, ETN, AVGO, NVDA all **singletons** · `U1: MPC, PSX` | 0.4902 | +0.6019 (vs +0.0040 between) |
| **500d** | **11** | `U0: ANET, ETN` · **028050 and 316140 split into singletons** · AVGO, NVDA singletons · `U1: MPC, PSX` | 0.1899 | +0.6111 (vs +0.0217) |
| **750d** | **10** | `U0: ANET, ETN` · **`U1: AVGO, NVDA`** · 028050, 316140 singletons · `U2: MPC, PSX` | 0.3810 | +0.5148 (vs +0.0189) |

- All three windows terminate on the same bar (**2026-08-21**), so the instability below is a
  property of window *length*, not of a moving endpoint.
- ★ **250d and 500d both print 11 units and mean opposite things.** At 250d the two KR names are one
  risk unit and ANET/ETN are two; at 500d that is exactly inverted. **The count is not a proxy for
  stability, and reporting "11 units" without the window is reporting nothing.**
- Only `MPC, PSX` (energy-refining) is one unit in **all three** windows — the single grouping this
  gate can vouch for.
- Threshold sensitivity (C5): at `dist` 0.40–0.60 **all three windows converge on 12 units.** Only the
  selected 0.65 splits them. The instability is a property of the chosen threshold, not of the data.
- Tool's own S5 warning fires on all three: ARI moves **opposite** to fit — the better the grouping
  looks, the less its membership is reproducible. The 250d run additionally warns **n = 249 < 250**
  ("a short sample invents structure").
- ⚠ Standing structural note: `U0` at 250d mixes **two different book theme labels**
  (`KR-E&C/plant`, `KR-bank-holding`), which `MAX_THEME_PCT` counts as two. At 500d/750d the same
  warning attaches to `ANET + ETN` (`AI-compute-EPICENTER`, `AI-power/electrical`).
- 🚫 **What this run may not do today:** **cite a concentration guard as a single number.** Every
  concentration sentence must carry its `--days` **on the same line as the conclusion**, and must not
  claim the AI-compute names are one unit or two without naming the window that says so.

### G5 — does the universe cover the book 🔴 FAIL (staleness + one hole)
- Book: **11 US holdings + 2 KR.** All 11 US names are in `us_top300.csv` **and** carry a score:
  `ANET +0.417 🟡` · `AVGO −0.221 🟡` · `ETN +0.210 🟡` · `HPE +0.489 🟡` · `MET −0.164 🟡` ·
  `MPC +0.700 🟡` · `NDAQ −0.025 🟡` · `NUE +0.319 🟡` · `NVDA −0.181 🟡` · `PSX +0.728 🟡` ·
  `RTX −0.122 🟡`. **Coverage leg: 0 missing ✅**
- ⚠ **All 11 tag 🟡중립 for the third run running.** With `vel_coverage = 0.0` this is the honest
  output, not a signal — the tag layer has no news input to push any name to an extreme.
  **"The book is all-neutral" is a statement about the instrument today, not about the book.**
  ★ Note the interaction with §1: **9 of the 11 holdings sit below universe rank 49**, so even on a
  partial-coverage run most of the book would be tagged from three axes regardless. `NVDA` and
  `AVGO` are the exceptions — they are inside the news bucket, and their tags are therefore the two
  in the book that a partial run could have moved.
- ⚠ **`us_top300.csv` mtime 2026-07-15 — 40 days old** (limit ≤8). Builder warning printed at both
  sweep starts: `유니버스 us_top300.csv 40일 경과 — 시총 stale`. A `us_all_v2_candidate.csv`
  (2026-08-10) sits beside it, **unpromoted for 14 days.**
  ★ This staleness now compounds with §1: the **rank order of the universe file decides who gets a
  news call.** A 40-day-old cap ranking is not just a weighting error — it silently determines the
  membership of the contaminated bucket.
- ⚠ **`EA` absent from the sweep for the 12th consecutive run** — 299 scored of 300 universe rows;
  `EA` has no close on any of the last four bars.
- ⚠ Book-marking defect, **5th consecutive run**: `module_paper_book status` prints **`n/a` for the
  PRICE of both KR holdings** (028050, 316140), with unrealised P&L and stop blank. ★ Total assets
  **17,607,290 KRW** is therefore computed **without marking two positions** — using it as a
  denominator misstates every weight. (Unchanged to the won from 08-23, which is itself a symptom:
  the two unmarked positions cannot move the total.)
- ⚠ **Every stop column is blank (`—`) on all 13 rows**, US names included — 5th consecutive run.
- 🚫 **What this run may not do today:**
  1. **No market-cap-weighted claim may rest on the universe's weights** (40-day-old caps).
  2. **No flow / RS / OBV / short verdict on `EA`** — it is **unmeasured**, not quiet.
  3. **No KR-holding P&L, stop, or share-of-book from the book's own numbers**, and **no percentage
     of total assets** while the denominator is unmarked.

### G6 — estimate-snapshot accrual 🔴 FAIL
- `snapshot_estimates.py --status`: **16 files / 34 calendar days** (2026-07-22 → 08-24) = **0.47/day**.
- 24 more days needed to reach the 40-day target: ideal **24 days**, measured **≈51 days** = **2.1×**
  (limit 1.5×). Gaps `[1,1,5,1,1,1,1,1]` · median 1 · max 6.
- ✅ Direction is improving for a 5th run (0.42 → 0.44 → 0.44 → 0.45 → **0.47**) and the daemon has
  now fired **six days straight** (08-19 · 20 · 21 · 22 · 23 · 24). It still does not clear the
  threshold, and the ratio is dominated by the un-repairable early gaps, not by current behaviour.
- ⚠ Un-backfillable: days not saved are gone permanently.
- 🚫 **What this run may not do today:** **`kelly_size --ic` output may not be reported as a
  measurement-grounded size.** If used, write **"mechanical 1/4"** beside it.

### G7 — tool liveness 🔴 FAIL (15th consecutive, same two)
- **52 entry points probed** — 23 `module_*` packages + 29 `scripts/*.py`. **50 exit 0.**
- **Non-zero (2), both unchanged for fifteen runs:**
  - `module_chart --help` → **exit 1.** Not argparse: the module prints its own usage line
    (`usage: python -m module_text_chart <ticker> [--read]`) and exits non-zero for any unrecognised
    argument, `--help` included. **Functional probe: `python -m module_chart NVDA --days 20` → exit 0,
    wrote `module_chart/output/NVDA_chart.txt` (7,708 bytes, 22:15 KST).**
  - `scripts/margin_history.py --help` → **exit 1**, `argparse._expand_help` →
    `ValueError: unsupported format character ')' at index 12`. Help rendering only.
    **Functional probe: `python scripts/margin_history.py NVDA` → exit 0**, FY2009–FY2026 gross margin
    series (max FY2025 75.0% · min FY2009 34.3% · median 56.9% · FY2026 71.1%).
- 🚫 **What this run may not do today:** nothing is removed — **but any citation of either tool must
  carry "`--help` is dead; verified by functional output".**
- ⚠ **`--help` remains a weak proxy for liveness, and today shows both failure modes at once:**
  `module_news_data` exits 0 while its data path dies inside every sweep, and `scripts/sector_flow.py`
  exits 0 while producing a file with a zeroed axis. **Exit code 0 is not evidence that a tool measured
  anything.**

---

## Rights removed for this run — one page

1. ★ **No claim of movement since the last run** (G0/G2). **Zero new sessions, second run running.**
   Today's 299 scores, 299 tags and 11 sector rows are **identical** to both 08-23's and 08-22's
   persisted files. "Turned", "accelerated", "rolled over", "since yesterday" are unavailable.
   Friday's move (08-20→08-21) is citable **as Friday's move**, labelled as the same Δ two prior runs
   already used.
2. ★ **No blending of a live Monday quote into the 08-21 frame** (G0). The bell rings at 09:30 ET,
   inside this run's window. A post-open quote is a **live intraday print** and must be labelled one.
3. **No news-velocity axis citation from the sweep** (G1) — `vel_coverage = 0.0`, exactly zero.
4. **No "quiet / cooling / no news" verdict from sweep silence** (G1) — 40/40 falsified today,
   **400/400 cumulative over ten runs.**
   ✅ **Exception: direct `fts` / `brief` / `thread` calls outside a sweep window are citable**
   (today 44/44 successful). Write "direct call outside the sweep window" on the same line.
5. ★ **New — no description of the news defect as random, scattered, or self-cancelling** (G1/§1).
   The bucket is **universe ranks 0–48, contiguous, identical across days, 69.0% of market cap.**
   Breadth must come from the **score** column, which never sees `vel`.
6. **No promotion or demotion of Consumer Staples on `wflow`** (G3) — `WMT` 28.9% flips the sign.
   Use `eqflow` +0.048 or breadth +0.05, and print the weight beside it.
7. **No concentration claim as a bare number** (G4) — `--days` must sit on the same line as the
   conclusion. Whether the AI-compute names are one risk unit or two is decided by the window, not
   by the data.
8. **No market-cap-weighted claim resting on universe weights; no flow/RS/OBV/short verdict on `EA`;
   no KR-holding P&L, stop, or share-of-book, and no percent-of-total-assets** (G5).
9. **No `--ic` size reported as measurement-grounded** (G6) — mark it "mechanical 1/4".
10. **`module_chart` and `margin_history` citations carry the "`--help` dead / functionally verified"
    note** (G7).

## Retractions issued by this run

| Retracted | Source | Replaced by |
|---|---|---|
| *"an **arbitrary** 51-name bucket"* / *"the arbitrary ~1-in-6 of names that fit inside the bucket"* | PREFLIGHT 08-22, 08-23 §1 | **Universe ranks 0–48, contiguous from rank 1, identical names on consecutive days, 16.4% by count but 69.0% by market cap.** The bucket is deterministic and mega-cap-selective |
| *"budget ≈ 100 remote calls ≈ 51 names, a hard contiguous cut"* — cited as **inherited, not re-measured** (08-23 G1) | PREFLIGHT 08-22 → 08-23 | Same claim, now **directly measured by position** (49 names, positions 0–48). Promoted from inherited to measured |

**Standing and *not* retracted:** the bidirectionality finding of 08-23 (partial coverage inflates
dispersion, not optimism) replicates today — 4 manufactured 🟢, 1 manufactured 🔴, 1 suppressed 🔴,
universe 🔴 unchanged at 71 in both runs.

---

*Instrument check only. No market call, no name call, no sizing (P4). Written before HANDOVER.*
