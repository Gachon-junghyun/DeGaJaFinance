# PREFLIGHT — 2026-08-22 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-22 22:09–22:22 = ET 2026-08-22 09:09–09:22, SATURDAY — US cash CLOSED.**
> Terminal settled bar **2026-08-21 (Friday close)**; sweep `asof` **2026-08-21**. Sweep run fresh at
> **22:09–22:13 KST today** with `--refresh` (no artifact reuse).

★ **Today this stage did something it has never managed in ten runs: it stopped describing the news
defect and measured its mechanism.** Three numbers now define it — **budget ≈ 100 remote calls
(≈ 51 names) · the wall is a hard contiguous cut, not a success *rate* · cooldown ≈ 90 s.** Two of
yesterday's written conclusions are retracted below on the strength of it.

---

## ① The news axis has a **quota**, and the quota is ~100 calls. Yesterday's "1-in-6 success rate" is retracted.

The 08-21 table concluded, in bold: *"Not a quota exhausted at call N; a ~1-in-6 success rate spread
over the whole loop."* That conclusion was **inferred** from the scattered index positions of the
survivors (41 disjoint runs, 33 singletons). Today the same question was asked **directly** instead of
inferred, and the answer is the opposite.

**The experiment** — 150 names, hand-issued, serially, through the identical `news_velocity()` entry
point the sweep calls, with the sweep's own parameters (`recent=7, base=30`), with **no interleaved
work between calls**:

| Result | Reading |
|---|---|
| Successes | **51 names — indices 0 through 50, contiguous, no gaps** |
| Failures | **99 names — indices 51 through 149, contiguous, no gaps** |
| First failure | index **51** (`ADBE`), note `뉴스 API 응답 실패 + 로컬 FTS 색인 없음` |
| Elapsed | 47.1 s for 300 calls |

**51 names × 2 calls = 102 calls, then a wall.** Not a rate. A **budget**, spent to zero, in one clean cut.

★ **And 51 is exactly the plateau this desk has logged for eight runs** (08-18 · 08-19 · 08-20 · 08-21:
51 / 49 / 50 / 50 survivors; this morning's KR run: ~50 of 806). The number was never a property of the
news. **It is the size of the bucket.**

**Why the sweep's survivors look scattered anyway** — the sweep does price slicing, OBV, RS and volume
work between news calls, so the bucket trickle-refills during the loop and single calls leak through
across the whole universe. The scatter is an artifact of the sweep's *pacing*, not evidence against a
quota. The hand loop, which pauses for nothing, exposes the bucket in its raw shape.

## ② Two sweeps, minutes apart, identical prices: **16.4% then 0.0%.**

| Clock (KST) | Event | News coverage |
|---|---|---|
| 22:09:30 | `fts search Nvidia --days 7 --count --scope foreign` ×3 | **3536 · 3536 · 3536** (tunnel UP) |
| 22:09:50–22:11:37 | **sweep run 1** (`--refresh`, 301 tickers) | **49 / 299 = 16.4%** |
| 22:11:40–22:13:16 | **sweep run 2** (same prices, `--json`) | **0 / 299 = 0.0%** |
| 22:14:26–22:14:44 | falsification probe, 40 silent names | **40 / 40 valid in 18.1 s** |
| 22:15:28–22:16:15 | burst experiment, 150 names | **51 ok / 99 fail, contiguous** |
| 22:16:36 → 22:17:37 | single-call probe every 20 s | **FAIL · FAIL · FAIL · FAIL** |
| **22:17:57** → 22:19:41 | same probe continues | **ok ×6** (recent 3536 · base 478.7) |

Run 1 drained the bucket; run 2 started empty and never recovered inside its 96 s; the bucket refilled
**≈ 90–100 s** after the last burst. **The server was healthy in every one of those windows** — the same
CLI returned 3536 before the sweeps and 3536 after.

⇒ **This is the KR desk's self-DoS finding (measured this morning on the KR side) reproduced on the US
side with a number attached.** The desk is not being starved of news. **The desk spends its own news
budget on a 299-name loop and then throws 96% of the answers away** — the axis is dropped whenever
coverage < 80%, which it always is.

## ③ ★ Retraction two — **`breadth` / `green` / `red` are not news-free under PARTIAL coverage, and yesterday granted them unconditionally.**

> ⚠ **Read G1 rule 3 with this section.** A first draft of this finding revoked the tag layer outright;
> that over-reach was caught later in the same run and is corrected there, with the reasoning kept
> visible rather than edited away. **Today's persisted file is the one case where the tag layer is
> clean** — because its velocity coverage is exactly **zero**, not partial.

The 08-21 rights table permitted them explicitly: *"`breadth`, `green`, `red` counts remain citable
(they derive from the 3 surviving axes)."* Today's back-to-back pair falsifies that, because the two
runs share **one identical price frame**:

| Quantity | Run 1 (49 names had velocity) | Run 2 (0 names had velocity) | Same? |
|---|---|---|---|
| `wflow`, `eqflow`, `delta` — **all 11 sectors, to 3 decimals** | +0.196 / +0.122 / +0.108 / +0.076 / … | **identical, sector for sector** | ✅ yes |
| Universe `wflow` | −0.076 | −0.076 | ✅ yes |
| **Universe 🟢 count** | **9** | **6** | 🚨 **no** |
| Energy 🟢 / Financials 🟢 / IT 🟢 | 1 / 2 / 3 | **0 / 1 / 2** | 🚨 **no** |

Cause, in source: `sector_flow.py:224` — `tag = flow_read.flow_tag(p, vel)`. **`flow_score` never sees
`vel` when the axis is dropped, but `tag` always does.** So the score layer is clean and the tag layer
is contaminated — and `green` / `red` / `breadth` are counted off the **tag**.

★ The contamination is **selection-biased upward**: three names were promoted to 🟢 for no reason but
having landed inside an arbitrary 51-name bucket while carrying accelerating news. Breadth built that
way is **inflated by exactly the arbitrariness of the bucket**. (The three names are unrecoverable —
run 1 was not persisted as JSON. Logged as a gap, not guessed at.)

★★ **And the inversion this implies is the run's sharpest single line:** *zero* coverage is uniform and
therefore safe, while *partial* coverage is selection-biased and therefore not. **The sweep that failed
hardest at news produced the cleanest tag layer of any run in this ledger.** Run 1's 9 greens are the
contaminated set; run 2's 6 are the honest one.

⚠ **Filename deviation, logged (13th consecutive run, same reason):** the composition table names this
`preflight/PREFLIGHT.md`; the `industry_kr` desk wrote its rights table there this morning
(08:17–08:35 KST). Overwriting a sibling desk's output is not a correction, so the US table is
`PREFLIGHT_US.md` in the same folder — documented practice 08-10 through 08-21. Human decision on
permanent market-suffixing still pending (PROMPT_MAP §6).

---

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** *(4th consecutive US pass)* | Terminal bar **2026-08-21 (Friday)** · Close **300/301** on each of the last three rows (08-19 · 08-20 · 08-21) · last-bar volume / prior-20d median **0.940** (q25 0.782 · q75 1.149, n=300) · `SPY` closes present through **08-21 765.72** ⇒ names and benchmark share one terminal date, **no RS-leg misalignment**. Sole missing name in every column is `EA` (G5). `n_new_sessions_since_prior_run = 1` |
| **G1** news axis alive | 🔴 **FAIL** *(10th consecutive run — but the mechanism is now measured)* | Sweep coverage **16.4% (49/299)** then **0.0% (0/299)** on the very next run, same prices. Hand burst: **51 ok / 99 fail, contiguous cut at index 51** ⇒ **budget ≈ 100 calls, cooldown ≈ 90 s**. Falsification **40/40 in 18.1 s**; cumulative **0 false silences in 320 hand-checks over eight runs** |
| **G2** scoring-scale continuity | 🟢 **PASS** | **3-axis (`nonews`) vs 3-axis (`nonews`)** — prior snapshot `2026-08-20._mode = nonews`. Subtraction is legal and the Δ spans exactly **ONE session (08-20 → 08-21)**: 290/299 scores moved, median abs-Δ **0.061**, max **1.230** |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **1 of 11**: Consumer Staples / `WMT` **28.9%** (wflow **−0.013** → ex-top1 **+0.116**). Yesterday's flipper (Communication Services / `GOOGL`) has left the set: today +0.108 → +0.022, same sign |
| **G4** risk-unit stability | 🔴 **FAIL** *(13th consecutive run — and today it hides behind a matching count)* | 250d **11 units** · 500d **11** · 750d **10**. ★ **250d and 500d both print 11 and disagree on membership** — the count is no longer a safe proxy for stability |
| **G5** does the universe cover the book | 🔴 **FAIL** *(staleness + one hole)* | **11/11 US holdings inside `us_top300` AND scored ✅** (all 11 🟡 again). But `us_top300.csv` is **38 days old** (limit ≤8), and **`EA`** is still absent from the sweep (299 of 300) — **10th** consecutive run unmeasurable |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** *(but the daemon fired today, 4th straight day)* | 14 files / **32 calendar days** = **0.44/day** ⇒ measured ETA **≈59 days** to the 40-day target vs ideal 26 = **2.3×** (limit 1.5×). ★ Last save = **today, 2026-08-22** |
| **G7** tool liveness | 🔴 **FAIL** *(13th consecutive, same two)* | **45 entry points** probed (16 modules + 29 scripts), **2** non-zero `--help`: `module_chart` · `scripts/margin_history.py`. Both pass a functional probe ⇒ citation retained **for those command lines only** |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate and it passed).
**Instrument state is unchanged from 08-21 in every count. What changed is knowledge, not health** —
and it moved in the direction that *costs* this run a right (③) rather than granting one.

Today this desk **cannot** speak with the sweep's news-velocity axis, the 51 survivors as a set, theme
freshness, "it went quiet", **`breadth` / `green` / `red` / new-🟢 in any form**, a single concentration
number, a unit count without its window, an `--ic`-derived size, the Consumer Staples `wflow` sign, or
`EA`. It **can** speak with settled prices through the **2026-08-21** close, a **one-session Δ**,
`flow_score`, RS, OBV, `vol_surge`, `eqflow`, `wflow` signs for 10 sectors, the full `module_chart
--read` panel, FINRA short pressure, CFTC COT positioning, FRED series, primary filings, and
**hand-probed per-name news velocity — now with a known safe batch size of ≤ 50 names per ~90 s.**

---

## G0 · Bar completeness · date alignment — 🟢 **PASS** (4th consecutive)

Not one of the seven. Carried because the KR desk measured it into existence on 08-12.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-22.pkl`
(85 rows × 1806 columns = 301 tickers × 6 fields) + `SECTOR_FLOW_US.json §scoring`.

### (a) The three most recent rows, field by field — **[measured]**

| Field | 2026-08-19 | 2026-08-20 | **2026-08-21 (terminal)** |
|---|---|---|---|
| Open | 300 / 301 | 300 / 301 | **300 / 301** |
| High | 300 / 301 | 300 / 301 | **300 / 301** |
| Low | 300 / 301 | 300 / 301 | **300 / 301** |
| Close | 300 / 301 | 300 / 301 | **300 / 301** |
| Volume | 300 / 301 | 300 / 301 | **300 / 301** |

The single missing name in every cell is `EA` — a separate, older hole (G5), not a bar defect.

★ **The "three-quarters bar" defect class** (full volume, NaN close, invisible to volume heuristics) —
the one that took the KR desk's whole sweep to zero this morning via a single `^KS11` cell — **has now
been absent for four consecutive US runs.** It is not retired as a *class*: the only test that ever
caught it, **non-null close count**, stays this gate's primary test permanently, clean readings or not.
This morning's KR failure is the standing proof that retiring it would be wrong.

### (b) Completeness of the terminal bar — **[measured]**

| Test | Reading on the 08-21 row | Conclusion |
|---|---|---|
| Row present in frame? | yes, index ends **2026-08-21** | Friday is here |
| **Non-null closes on the last row** | **300 / 301** | primary test fires clean |
| Last-bar volume / prior-20d median | **median 0.940** · q25 **0.782** · q75 **1.149** (n=300) | settled full session |
| Benchmark alignment | `SPY` closes **08-17 772.67 · 08-18 767.45 · 08-19 769.06 · 08-20 762.60 · 08-21 765.72** | names and bench end on the **same date** |

★ **The Saturday clock is this run's friend, not its enemy.** Every prior US run in this ledger fired in
the pre-market and therefore held Thursday while Friday was still unwritten. This one fires with the week
**closed and settled**: no partial-bar risk exists today, because there is no live session to contaminate
anything.

### (c) Sessions gained — **[measured]**

Prior usable snapshot **2026-08-20**; today's **2026-08-21** ⇒
**`n_new_sessions_since_prior_run = 1`.** Written by hand, because nothing writes it automatically
(D280). Four consecutive runs now advance one clean session each.

**✅ Rights retained today**: settled prices, closes, returns, RS, OBV, `vol_surge` through the
**2026-08-21** close · the full `module_chart --read` panel · benchmark-relative statistics.

**🚫 Rights revoked today**
1. **No 08-22 price of any kind.** The US cash market did not open today. There is no Saturday bar and
   none may be invented from a quote endpoint.
2. **`EA` is exempt from every price statement above** — see G5.

---

## G1 · News axis alive — 🔴 **FAIL** (10th consecutive run)

**Command** `SECTOR_FLOW_US.json §scoring`; falsification probe via
`module_flow._news_velocity.news_velocity(query, 7, 30, kr=False)` — **the identical function object the
sweep calls** (`scripts/flow_read.py:13` re-exports it; verified, not assumed);
CLI `python -X utf8 -m module_news_data fts search Nvidia --days 7 --count --scope foreign`.

### (a) What the instrument reports about itself — **[measured]**

```
run 1  "scoring": {"vel_axis": false, "vel_coverage": 0.164, "n_axes": 3,
                   "scored": 299, "dropped_missing_axis": 0}
run 2  "scoring": {"vel_axis": false, "vel_coverage": 0.0,   "n_axes": 3,
                   "scored": 299, "dropped_missing_axis": 0}
```

The sweep's own 🚨 line fired verbatim in both. `dropped_missing_axis = 0` confirms the D225 fix is
holding — **all 299 names scored on the same 3 axes**, so no name received the +0.305 phantom bonus the
2026-08-09 defect produced. The scale is wrong-but-uniform, which is what keeps G2 legal.

### (b) Is it silence, or is it the pipe? — **[measured]** — 40 / 40

The 40 names at the head of the silent set, re-asked by hand: **40 valid / 40 asked, in 18.1 seconds.**
Not one returned "no articles."

| Ticker | Name | recent(7d) | base | vel |
|---|---|---|---|---|
| COIN | Coinbase | **585** | 79.25 | 1.05 |
| MSTR | MicroStrategy | 156 | 15.04 | 1.48 |
| MRK | Merck & Co. | 51 | 3.39 | **2.15** |
| TGT | Target | 26 | 1.61 | **2.31** |
| FCX | Freeport-McMoRan | 36 | 3.18 | 1.62 |
| PSX | Phillips 66 | 42 | 4.86 | 1.24 |
| MPC | Marathon Petroleum | 32 | 4.25 | 1.08 |
| TSLA | Tesla | **339** | 57.68 | 0.84 |
| UBER | Uber | **316** | 39.00 | 1.16 |
| MRVL | Marvell | **230** | 20.39 | 1.61 |
| INTU | Intuit | 245 | 27.93 | 1.25 |
| CRM | Salesforce | 190 | 19.32 | 1.40 |
| LITE | Lumentum | 122 | 15.29 | 1.14 |
| REGN | Regeneron | 31 | 2.89 | 1.53 |
| ISRG | Intuitive Surgical | 40 | 4.32 | 1.32 |
| A | Agilent | 6 | 0.50 | 1.71 |

(full 40 in `llm_outputs/2026-08-22/industry_US/_silent_names.json`)

**Cumulative record of this probe: 0 false silences in 320 hand-checks over eight runs.** The sweep has
never once been right that a US large cap had no news.

### (c) ★ The mechanism — a budget of ~100 calls, not a success rate — **[measured]**

150 names, hand-issued serially, sweep parameters, **nothing interleaved**:

| Index range | Outcome | Count |
|---|---|---|
| **0 – 50** | valid velocity | **51, contiguous, zero gaps** |
| **51 – 149** | `뉴스 API 응답 실패 + 로컬 FTS 색인 없음` | **99, contiguous, zero gaps** |

51 names × 2 calls (recent + base) = **102 calls**, then the wall. Elapsed 47.1 s.

**This retracts the 08-21 conclusion** (*"a ~1-in-6 success rate spread over the whole loop"*), which was
inferred from survivor scatter rather than tested. Both observations are compatible: the bucket is a hard
~100-call budget, and the sweep's survivors scatter because the sweep pauses for price work between calls,
letting the bucket trickle-refill mid-loop.

### (d) ★ Refill time — **[measured]**

Single `Nvidia` call every 20 s after the burst drained the bucket at 22:16:15:

| 22:16:36 | 22:16:56 | 22:17:16 | 22:17:37 | **22:17:57** | 22:18:18 → 22:19:41 |
|---|---|---|---|---|---|
| FAIL | FAIL | FAIL | FAIL | **ok** (3536 / 478.7) | ok ×5 |

**Cooldown ≈ 90–100 s.** The tunnel was never down: the same CLI answered **3536** at 22:09, before any
sweep, and **3536** again at 22:17:57 after.

### (e) ★ The contamination of `tag` — **[measured]** — see ③ above

`wflow` / `eqflow` / `delta` identical to 3 decimals across the two runs; **universe 🟢 went 9 → 6** with
the price frame untouched. Cause: `sector_flow.py:224`, `tag = flow_read.flow_tag(p, vel)`.

**🚫 Rights revoked today (every stage, no exceptions)**
1. **No stage may cite news velocity, theme freshness, or news acceleration from `SECTOR_FLOW_US.json`.**
   The axis is `false` and `velocity` is `null` for **all 299** names in the persisted file.
2. **No stage may write "it went quiet", "no news flow", "the narrative faded", or any absence-claim
   sourced from the sweep.** Measured 0-for-320: this instrument's silence has never once been real.
3. 🆕 **`breadth`, `green`, `red`, and "new 🟢" may not be cited from any run with PARTIAL velocity
   coverage** — that is the normal case, and it is contaminated on an arbitrary subset. Measured: 9 vs 6
   on one price frame; Energy 1→0, Financials 2→1, IT 3→2.
   ★ **CORRECTION, made later in this same run and recorded rather than edited away (§4c / D48).**
   The first draft of this rule revoked the tag layer *outright*. **That was wrong, and the ledger audit
   caught it** — a `missed_ledger` row (`CBRE`) whose entry condition reads *"enters the green set on an
   admissible (non-velocity) axis"* forced the question. Reading `module_flow/_synthesize.py:10-49`:
   with `vel = None` the green term contributes `(vel or 0) >= 1.2` = **False** and the red term
   `(vel is not None and vel < 0.7)` = **False**, so the tag collapses to a pure 3-axis price function —
   🟢 requires `obv매집 ∧ rs20>0 ∧ vol_surge≥1.2` (unanimity, `M25`'s shape), 🔴 requires
   `obv분산 ∧ rs20<−2`. **In the persisted file every one of the 299 velocities is `null`**, therefore
   **today's tags are provably velocity-free and ARE citable**, on the stated condition that a 🟢 is read
   as *3-axis unanimity*, never as *news-confirmed*.
   ★★ The uncomfortable corollary, and it is the run's sharpest finding: **the sweep whose news pipe
   failed hardest produced the epistemically cleanest tag layer.** Zero coverage is *uniform*; partial
   coverage is *selection-biased*. Run 1's 9 greens are the contaminated set; run 2's 6 are not.
   ⚠ Still forbidden regardless: describing any of it as **news-informed**, and comparing today's breadth
   to a prior run's (that run had partial coverage; the two are not on one scale).
4. **The 51 survivors may not be used as a set** — the persisted run has zero of them, and the membership
   of any such set is now known to be *"whichever names the loop reached before call 100."*
5. ✅ **Per-name news velocity IS citable when hand-probed**, labelled with its clock time — **and the safe
   batch is now known: ≤ 50 names, then wait ≈ 90 s.** Any stage needing news should spend the budget on
   **the handful of names it actually cares about**, never on a 299-name sweep.

---

## G2 · Scoring-scale continuity — 🟢 **PASS**

**Command** `SECTOR_FLOW_US.json §scoring.n_axes` vs `llm_outputs/sector_flow/history.json` prior
snapshot `_mode`.

| Snapshot | `_mode` | axes | names |
|---|---|---|---|
| 2026-08-18 | `nonews` | 3 | 299 |
| 2026-08-19 | `nonews` | 3 | 299 |
| 2026-08-20 (**prior run**) | `nonews` | 3 | 299 |
| **2026-08-21 (this run)** | **`nonews`** | **3** | **299** |

Both sides of every `delta` field are 3-axis. **Subtraction is legal today.**

★ **The Δ baseline is one clean session for the fourth consecutive run** (08-20 → 08-21): **290 of 299**
scores moved, median abs-Δ **0.061**, max **1.230** (`HOOD` ▲1.23). Compare 08-21's reading (294 moved,
median 0.067, max 0.873): slightly fewer names moved, with a fatter tail.

⚠ **Standing caveat, unchanged**: `nonews`-mode scores are comparable to each other but are **not** on the
same scale as any 4-axis snapshot before 08-13. Cross-mode subtraction stays forbidden.

⚠ **New caveat from G1(e)**: `delta` is computed on `flow_score`, which is news-free — so Δ is safe.
**But Δ must not be narrated through tag changes** ("X turned green today"), because tag flips are
contaminated.

**✅ Rights retained**: `delta` fields and Δflow ranking — **on a one-session (08-20 → 08-21) basis**,
stated on the same line. **Revoked**: "new-🟢 ignition" as a call (G1 rule 3).

---

## G3 · Who owns the sector sign — 🟢 **PASS**

**Command** `SECTOR_FLOW_US.json §sector_rotation[].top1_flips_sign` — **printed in full, all 11**.

| Sector | n | wflow | ex-top1 | eqflow | top1 | top1 w | **flips?** |
|---|---|---|---|---|---|---|---|
| Health Care | 32 | +0.196 | +0.205 | +0.229 | LLY | 19.4% | no |
| Consumer Discretionary | 28 | +0.122 | +0.254 | +0.103 | AMZN | 40.2% | no |
| Communication Services | 12 | +0.108 | +0.022 | +0.095 | GOOGL | 38.3% | no |
| Energy | 16 | +0.076 | +0.189 | +0.102 | XOM | 30.5% | no |
| Materials | 12 | +0.064 | +0.201 | +0.046 | LIN | 24.7% | no |
| Financials | 47 | +0.003 | +0.034 | −0.034 | BRK-B | 13.9% | no |
| **Consumer Staples** | 19 | **−0.013** | **+0.116** | +0.048 | **WMT** | **28.9%** | **🚨 YES** |
| Information Technology | 56 | −0.231 | −0.243 | −0.102 | NVDA | 19.4% | no |
| Industrials | 50 | −0.259 | −0.218 | −0.231 | CAT | 8.7% | no |
| Real Estate | 12 | −0.543 | −0.491 | −0.446 | WELL | 16.9% | no |
| Utilities | 15 | −0.648 | −0.659 | −0.621 | NEE | 17.7% | no |

**Flipper count: 1 of 11.** Yesterday's flipper (Communication Services / `GOOGL`) has left the set — it
keeps its sign today (+0.108 → +0.022, still positive, though thinly). Today's flipper is **Consumer
Staples**, where `WMT` alone carries 28.9% of the sector cap and is the entire reason the sector prints
*negative*.

★ Note the direction: this flipper works **against** the sector, not for it. Consumer Staples is positive
on `eqflow` (+0.048) and on ex-top1 `wflow` (+0.116), and negative only because of Walmart.

**🚫 Rights revoked today**
- **Consumer Staples may not be promoted or demoted on its `wflow` sign.** ROTATION §2 must use `eqflow`
  (**+0.048**) or `breadth` (**0.05 — 1 green of 19, `TGT`**) for it, or hold it.
  ⚠ Per the G1 rule-3 correction, `breadth` **is** available today (all velocities null ⇒ the tag layer is
  velocity-free) — but it is available as a **3-axis unanimity count**, and it may not be compared to any
  earlier run's breadth, every one of which was computed under partial coverage.
- ✅ The other **10 sectors' `wflow` signs are owner-verified** and may be cited as sector-level facts.

---

## G4 · Risk-unit stability — 🔴 **FAIL** (13th consecutive run)

**Command** `python -X utf8 scripts/risk_units.py --book --days {250,500,750}` — **all three actually
run**, 22:19–22:21 KST.

| Window | Units | Grouping | ARI (1st half vs 2nd) |
|---|---|---|---|
| **250d** | **11** | `U0: 028050 + 316140` (a KR E&C name merged with a KR bank holding) · `MPC + PSX` · **ANET, AVGO, ETN, NVDA each alone** | **0.4902** |
| **500d** | **11** | `U0: ANET + ETN` · `MPC + PSX` · 028050 and 316140 **separate** · AVGO and NVDA **separate** | **0.1899** |
| **750d** | **10** | `U0: ANET + ETN` · `U1: AVGO + NVDA` · `U2: MPC + PSX` · 028050 and 316140 separate | **0.3810** |

★ **The new trap, and it is worse than yesterday's:** 250d and 500d **both print 11** — and they group
**different names**. Yesterday the counts themselves disagreed (11 / 10 / 10), which at least made the
instability visible to anyone reading the number. Today a stage that quotes "11 risk units" would be
quoting a figure that is **simultaneously true at two windows which contradict each other name-for-name**.

Threshold sensitivity: all three windows sit on a cliff — dist 0.60 → 12 units in every window; dist 0.65
→ 11 / 11 / 10 (selected); dist 0.70 → 10 / 9 / 9. The chosen threshold is doing the work.

**🚫 Rights revoked today**
1. **No concentration guard may be quoted as a single number**, and today **not even as a single count**.
   "The book is 11 units" is not a fact; it is a fact-shaped coincidence of two windows.
2. **Any stage citing a risk-unit count must print `--days` on the same line as the conclusion**, and today
   must additionally name at least one grouping, because the count alone no longer discriminates.
3. **AI-compute concentration is unresolved**: four singletons at 250d, three units at 500d (ANET with
   ETN), two at 750d (AVGO+NVDA merged). No stage may state how concentrated the AI-compute book is.
4. ✅ **`MPC + PSX` is one unit in all three windows** — the only window-invariant grouping in the book, and
   it may be treated as a single risk unit without a window caveat.

---

## G5 · Does the universe cover the book — 🔴 **FAIL** (staleness + one hole)

**Command** `data/us_universe/us_top300.csv` (300 rows) × `module_paper_book status` ×
`SECTOR_FLOW_US.json §names`.

### (a) Coverage leg — **PASS** — **[measured]**

**11 / 11 US holdings are inside `us_top300` and carry a score in today's sweep:**

| Ticker | tag | flow | OBV | RS20 | Ticker | tag | flow | OBV | RS20 |
|---|---|---|---|---|---|---|---|---|---|
| ANET | 🟡 | +0.417 | +0.152 | +4.8 | NUE | 🟡 | +0.319 | +0.148 | −5.2 |
| AVGO | 🟡 | −0.221 | +0.038 | −7.2 | NVDA | 🟡 | −0.181 | −0.024 | +0.2 |
| ETN | 🟡 | +0.210 | +0.172 | +0.1 | PSX | 🟡 | +0.728 | +0.261 | +13.8 |
| HPE | 🟡 | +0.489 | +0.198 | +8.5 | RTX | 🟡 | −0.122 | +0.023 | −5.0 |
| MET | 🟡 | −0.164 | +0.038 | −4.1 | MPC | 🟡 | +0.700 | +0.318 | +13.0 |
| NDAQ | 🟡 | −0.025 | +0.016 | +3.0 | | | | | |

★ **All 11 are 🟡 — not one green, not one red — for the second consecutive run.** ⚠ And per G1(e) that
uniformity is itself partly a tag-layer artifact today: with the news bucket empty, the tag layer has one
fewer axis to push any name off neutral. **Do not read "all neutral" as a market statement.**

The two KR holdings (`028050`, `316140`) are out of the US universe by construction, not a hole. The book
carries both at `PRICE n/a` — **4th consecutive run**, inherited from the KR desk's ledger.

### (b) Staleness leg — **FAIL** — **[measured]**

`us_top300.csv` mtime **2026-07-15** ⇒ **38 days old**, limit ≤8. The sweep logs its own warning.

### (c) The `EA` hole — **FAIL** — **[measured]**

`EA` is row-present in `us_top300.csv` but **absent from the 299 scored names and NaN in every price column
of the frame** — **10th consecutive run**. Cause unchanged and undiagnosed here (diagnosis is `idle_probe`'s
job, not this stage's).

**🚫 Rights revoked today**
1. **No flow / RS / OBV / short judgment on `EA`.** It is not *quiet*; it is **unmeasured**. Any stage
   reaching for it writes "unmeasurable, 10th run" — never "no signal."
2. **Market-cap ranks and cap weights from `us_top300` are 38 days stale.** Sector *membership* is citable
   (GICS does not churn in 5 weeks); **rank ordering and cap weights are not** — and `wflow` is
   cap-weighted, so **`wflow` inherits a 38-day-old weighting.** State this wherever `wflow` decides a call.
   `eqflow` does not inherit it.
3. ✅ The **11 book names are fully measurable today** — no per-name caveat needed for them.

---

## G6 · Estimate-snapshot accrual — 🔴 **FAIL** (2.3× slow — but the daemon fired today)

**Command** `python -X utf8 scripts/snapshot_estimates.py --status`.

| Quantity | Reading |
|---|---|
| Files accrued | **14** (120 tickers each, ~148 KB) |
| Calendar span | **32 days** (2026-07-22 → 2026-08-22) |
| Measured rate | **0.44 / day** (ideal 1.00) |
| Remaining to the 40-day target | **26 more** ⇒ ideal 26 days, **measured ≈59 days** |
| Ratio to ideal | **2.3×** (limit 1.5×) |
| Gap distribution (days) | `[1, 2, 1, 1, 5, 1, 1, 1]` · median 2 · max 6 |
| **Last save** | **2026-08-22 — today.** Fourth consecutive day (08-19 → 08-22) |

★ **This is the D16 trap by construction**: counting *files* (14) reads as healthy; counting *days* (32) is
what makes it 2.3× slow. The status tool prints both, which is why it is catchable. Four consecutive daily
saves is the best stretch in the ledger — **and four days still do not move a 32-day rate.** The ratio
improved 2.4× → 2.3× on the strength of them; at that pace the gate clears in weeks, not days.

**🚫 Rights revoked today**
1. **`kelly_size --ic` output may not be presented as an evidence-backed size.** Any stage using it labels
   it **"mechanical ¼-Kelly, IC unmeasured"** on the same line.
2. **No stage may claim an IC-informed edge for any axis.** With n_eff < 4 the `ic_ledger` rule is explicit:
   **no verdict.**
3. ⚠ **Retroactive recovery is impossible.** Days not accrued are gone.

---

## G7 · Tool liveness — 🔴 **FAIL** (13th consecutive, same two)

**Command** `--help` on every entry point this run may touch — **45 probed** (16 `python -m` modules + 29
`scripts/*.py`), exit code recorded.

**43 of 45 returned exit 0.** The two failures, unchanged since 08-10:

| Entry point | `--help` exit | Functional probe (run today) | Verdict |
|---|---|---|---|
| `python -m module_chart` | **1** | `module_chart NVDA --read` → full panel (OBV 분배 −101% · MA 강세스택 5>20>60>120 · RSI 59.5 · turn NEUTRAL/CHOP · trigger 218.78 / stop 190.01) | **argparse defect only** |
| `python scripts/margin_history.py` | **1** | `margin_history.py NVDA` → SEC XBRL **FY2009–FY2026**, no gaps (FY2026 op margin 71.1%, peak FY2025 75.0%) | **argparse defect only** |

Both are the known argparse `%`-format bug in the help string, not a runtime failure.

**🚫 Rights revoked today**
1. **Neither tool's `--help` may be cited as documentation of its interface.** Argument names must be read
   from source, not from help output.
2. ✅ **Citation is RETAINED for the two command lines proved above** — `module_chart <TICKER> --read` and
   `scripts/margin_history.py <TICKER>` — and **only** those.
3. ✅ All other **43 entry points** are cleared, including this run's dependencies: `module_macro_us` ·
   `module_news_data` · `module_flow` · `module_fundamentals_us` · `module_business_us` ·
   `module_disclosure_us` · `module_valuation` · `module_paper_book` · `scripts/sector_flow.py` ·
   `scripts/us_live_shortlist.py` · `scripts/us_flow.py` · `scripts/cycle_exposure.py` ·
   `scripts/catalyst_calendar.py` · `scripts/drift_watch.py` · `scripts/chain_hop.py` ·
   `scripts/theme_age.py` · `scripts/risk_units.py` · `scripts/kelly_size.py` · `scripts/report_lint.py`.

---

## Consolidated rights table — what this run may and may not say

**🚫 FORBIDDEN today**

| # | Claim class | Source gate |
|---|---|---|
| 1 | News velocity / theme freshness / acceleration **from the sweep** | G1 |
| 2 | Any absence-claim ("quiet", "narrative faded", "no flow") sourced from the sweep | G1 |
| 3 | `breadth` / `green` / `red` from any run with **partial** velocity coverage; and any breadth comparison **across** runs | G1(e) |
| 4 | The velocity survivors **as a set** (and the persisted run has none) | G1 |
| 5 | Consumer Staples promoted/demoted on its `wflow` sign (WMT = 28.9%) | G3 |
| 6 | Any concentration figure as a single number — **today, not even as a single count** | G4 |
| 7 | How concentrated the **AI-compute** book is (4 singletons / 3 units / 2 units across windows) | G4 |
| 8 | `wflow` cap-weights or `us_top300` rank order treated as current (38 days stale) | G5 |
| 9 | Any flow/RS/OBV/short judgment on **`EA`** | G5 |
| 10 | `kelly_size --ic` as an evidence-backed size; any IC-informed edge claim | G6 |
| 11 | `module_chart` / `margin_history` **`--help`** as interface documentation | G7 |
| 12 | Any **2026-08-22** price (US cash closed — no Saturday bar exists) | G0 |

**✅ PERMITTED today**

| # | Claim class | Source gate |
|---|---|---|
| 1 | Settled prices / returns / RS / OBV / `vol_surge` / `flow_score` through the **2026-08-21** close | G0 · G1(e) |
| 2 | `delta` / Δflow ranking — **on a one-session (08-20→08-21) basis, stated** — but not narrated as tag flips | G0 · G2 |
| 3 | `wflow` **signs** for the 10 non-flipper sectors; **`eqflow` for all 11**; **and today's tags / green set**, which are provably velocity-free (all 299 `vel = null`) — read 🟢 as *3-axis unanimity*, never as *news-confirmed* | G3 · G1(e) |
| 4 | `MPC + PSX` as one risk unit, window-invariant | G4 |
| 5 | Full flow/RS/OBV panel on all **11 US book names** | G5 |
| 6 | `module_chart <T> --read` and `margin_history <T>` outputs | G7 |
| 7 | **Hand-probed** per-name news velocity, labelled with its clock time — **≤ 50 names per ~90 s** | G1(c)(d) |
| 8 | FRED series, FINRA short pressure, CFTC COT positioning, SEC primary filings | G7 |

---

## Run log

- Sweep run **fresh today at 22:09–22:13 KST** with `--refresh` (301 tickers, yfinance batch) — no artifact
  reuse. A **second** sweep followed immediately to persist `--json`; that second run is the one on disk,
  and its 0.0% news coverage is what produced ③.
- ⚠ **Known cost of that choice, logged**: because run 2 is the persisted file, `SECTOR_FLOW_US.json` carries
  **zero** velocity values and **6** greens rather than run 1's 9. Downstream sees the *cleaner* artifact
  (no arbitrary 51-name contamination), which is the better of the two — but the three names run 1 promoted
  are unrecoverable. A future fix would persist `--json` on the first pass.
- Output filename `PREFLIGHT_US.md` (not `PREFLIGHT.md`) — sibling KR desk owns that path today. 13th
  consecutive run; human decision pending (PROMPT_MAP §6).
- Nothing in this stage is written to `handoff/` — instrument state is not a market view.
- **No failed lookups in this stage.** Every command listed returned.
