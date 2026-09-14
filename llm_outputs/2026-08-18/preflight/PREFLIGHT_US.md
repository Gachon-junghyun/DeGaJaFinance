# PREFLIGHT — 2026-08-18 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-18 22:10–22:40 = ET 2026-08-18 09:10–09:40, TUESDAY — US cash PRE-MARKET**
> (bell 09:30 ET = 22:30 KST, i.e. *during* this run). First sweep download 22:12 · scoring 22:14 ·
> second sweep (after mitigation) 22:29 · sweep `asof` **2026-08-14** (Friday close).
>
> ★ **The headline today is a defect this desk has never seen in either market: a bar that is
> three-quarters real.** yfinance minted a **2026-08-17 daily bar carrying Open, High, Low and Volume
> for 300 of 301 tickers — and a NaN Close for 300 of 301.** Volume on that row is full-session
> magnitude (1.78 bn shares vs 1.76 bn on 08-14), so every completeness heuristic this desk owns —
> *"is the last bar's volume a plausible fraction of the 20-day average?"* — reads **0.73 and says
> the bar is settled.** The gate that would have caught it in KR (G0's volume ratio) **passes on this
> bar.** What failed instead was the scoring: `rs20` needs a close, the close was NaN, and
> **the sweep scored 0 of 299 names.**
>
> ★★ **The failure was loud, and that is the only reason this run is not silently wrong.** The 12
> defects that created this protocol on 08-09 all *returned plausible numbers*. This one returned an
> empty `SECTOR_FLOW_US.json` (327 bytes, `sector_rotation: []`, `names: []`) — the D225-KR fix
> ("a name with a missing axis gets no score, it does not quietly fall to 3 axes") converted a
> data-feed defect into a visible outage instead of a rank shuffle. **The guard did its job.**
>
> ⚠ **Filename deviation, logged (9th consecutive run, same reason):** the composition table names
> this `preflight/PREFLIGHT.md`, but the `industry_kr` desk wrote its rights table to that path this
> morning (09:25 KST). Overwriting a sibling desk's output is not a correction, so the US table is
> written as `PREFLIGHT_US.md` in the same folder — documented practice on 08-10 · 08-12 · 08-13 ·
> 08-14 · 08-15 · 08-16 · 08-17. Human decision on permanent market-suffixing still pending (PROMPT_MAP §6).

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🔴 **FAIL** *(first US failure in 6 runs — and a new defect class)* | **08-17 bar has OHL+V for 300/301 names and a NaN Close for 300/301** (`MNST` alone carries a close). Volume is full-session (**0.73** × 20d median) so the volume heuristic **passes on a broken bar**. Sweep #1 scored **0 / 299**. Reproduced at source with a bare 3-ticker `yf.download` ⇒ **upstream feed, not our cache** |
| **G1** news axis alive | 🔴 **FAIL** *(6th run)* — but the cause was caught **in the act** today | Sweep coverage **16.72% (50/299)**. Falsification probe at 22:2x: **0/40 valid**. Repeat probe, same argv, every 2 s for 92 s: **0/41, one unbroken run of failures.** Then CLI **5/5** and the same library call **40/40 valid in 18.4 s** — **ZERO genuinely quiet.** Cumulative **0 of 160** false-silence across four runs |
| **G2** scoring-scale continuity | 🟢 **PASS** *(literally)* | **3-axis (`nonews`) vs 3-axis (`nonews`)** ⇒ no apples-to-oranges subtraction. ★ **New measurement: same `asof` is not the same data** — 294/299 `flow_score` identical to yesterday, **5 moved**, because **130 of 300 names had their settled 08-14 *volume* revised** between downloads (median **0.077%**, max **0.77%**). Closes: **zero** revised bars |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **3 of 11**: IT/`NVDA` **19.4%** · Industrials/`CAT` **8.7%** · Materials/`LIN` **24.7%**. Same set and same numbers as 08-15 · 08-16 · 08-17 — **same terminal bar**, not a confirmed structure |
| **G4** risk-unit stability | 🔴 **FAIL** *(9th consecutive run, identical numbers)* | 250d **11 units** · 500d **10** · 750d **10** — 500 and 750 agree, **250 does not** (it splits `ANET`+`ETN` and `AVGO`+`NVDA`, and merges the two KR names) |
| **G5** does the universe cover the book | 🔴 **FAIL** *(staleness + one hole)* | **11/11 US holdings inside `us_top300` AND scored ✅**. But `us_top300.csv` is **34 days old** (limit ≤8), and **`EA` has now vanished from the sweep output entirely** (299 of 300 names) — 6th consecutive run unmeasurable |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** | 10 files / **24 calendar days** = 0.42/day ⇒ measured ETA **≈72 days** vs ideal 30 = **2.4×** (limit 1.5×). Last save **08-14, 4 days ago** |
| **G7** tool liveness | 🔴 **FAIL** *(9th consecutive, same two)* | **50 entry points** probed, **2** non-zero `--help`: `module_chart` · `scripts/margin_history.py`. Both pass a functional probe ⇒ citation retained **for those command lines only** — ★ except `module_chart --read`, whose numbers are contaminated by G0 today (see blast radius) |

**PASS 2 / FAIL 6** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate).
**The headline count is worse than the last three runs, and for once the reason is not the clock —
it is the data feed itself.**

Today this desk **cannot** speak with any 08-17 price, the sweep's news-velocity axis, the 50
survivors, theme freshness, "it went quiet", `breadth` as a news-independent reading, a single
concentration number, an `--ic`-derived size, `module_chart`'s RSI / Bollinger / momentum / MA-position
fields, or **any Δ described as "today's change"**. It **can** speak with settled prices through the
**08-14** close, RS, OBV, `eqflow`, `vol_surge`, FINRA short pressure, CFTC COT positioning, FRED
series, primary filings, and **hand-probed per-name news velocity — which measured 40/40 today.**

---

## G0 · Bar completeness · date alignment — 🔴 FAIL *(new defect class: the three-quarters bar)*

Not one of the seven. Carried because the KR desk measured it into existence on 08-12. It has failed
there repeatedly on **intraday stubs**; today it fails here on something else entirely.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-18.pkl`
(83 rows × 1806 columns = 301 tickers × 6 fields) + `SECTOR_FLOW_US.json §scoring` +
independent reproduction with a bare `yf.download`.

### (a) The 08-17 row, field by field — **[measured]**

| Field on 2026-08-17 | Non-null | of |
|---|---|---|
| Open | **300** | 301 |
| High | **300** | 301 |
| Low | **300** | 301 |
| Volume | **300** | 301 |
| **Close** | **1** | 301 |
| **Adj Close** | **1** | 301 |

The single name carrying a close is **`MNST` = 45.52**. Every other name — including the benchmark
`SPY` — has `Open 776.18 · Volume 33,285,717 · Close NaN`.

### (b) Why every completeness heuristic this desk owns passes on it — **[measured]**

| Test | Reading on the 08-17 row | What it concludes |
|---|---|---|
| Row present in frame? | yes, index ends 08-17 | "we have Monday" |
| Last-bar volume / prior-20d median | **0.730** (q25 0.591 · q75 0.892, n=300) | "settled full session" |
| Total universe volume | **1,782,317,677** vs 08-14's 1,756,362,200 | "settled full session" |
| Non-null closes on the last row | **1 / 301** | ← **the only test that fires** |

★ This is the lesson. The KR desk's stub bars are detected by **volume** (median 0.044 at open+26min).
**This bar's volume is real** — the session happened, the tape printed, and only the close field is
absent. A volume-based completeness gate is **structurally blind** to it.

### (c) It is upstream, not our cache — **[measured]**

A bare, dependency-free reproduction outside the pipeline: a 3-ticker `yf.download` over `period=1mo`
returns **NaN Close on 08-17 for SPY, NVDA and AAPL alike**, and a single-ticker `SPY` download returns
that bar with **Open 776.179993 · Volume 33,285,717 · Close NaN**.

⇒ The defect arrives from the provider. Nothing in `batch_prices`, the pickle cache, or `slice_frame`
created it. **[measured]**

### (d) What it did to the run — the guard converted a silent shuffle into a visible outage

Sweep #1 (22:12): `price_axes()` requires `obv_norm`, `rs20`, `vol_surge`. `obv_norm` and `vol_surge`
survived (they lean on volume); **`rs20` and `rs60` went NaN for every name because `last` was NaN**.
The resulting `scoring` block read `vel_axis false · vel_coverage 0.1706 · n_axes 3 · scored 0 ·
dropped_missing_axis 299`, with `universe.n = 0`, `sector_rotation: []` and `names: []`.

★ **Read this against the protocol's own origin.** On 2026-08-09 the same class of hole produced a
**+0.305 average score inflation** and a reordered sector table, and *no output line showed it*. Today
the D225-KR rule ("run-level axis set; a name missing an axis gets **no score**, it does not slide to a
3-axis average") turned the identical hole into a **327-byte empty file**. The desk lost a day of sweep
signal and lost **zero** ability to tell that it had. **That is the fix working as designed.**

### (e) Mitigation applied, and exactly what it is — *(logged, not hidden)*

INSTRUMENT_CHECK does not repair instruments (rule 1). What was done is **truncation, not repair**:
rows whose Close is non-null for ≤50% of tickers were dropped from the cached frame, so the frame ends
at the last **fully-closed** session. The raw download is preserved at
`llm_outputs/sector_flow/prices_2026-08-18.RAW_phantom0817.pkl` for audit.

| | Sweep #1 (raw frame) | Sweep #2 (truncated frame) |
|---|---|---|
| Rows | 83, ends **08-17** | 82, ends **08-14** |
| `asof` | 2026-08-17 | **2026-08-14** |
| Scored | **0** / 299 | **299** / 299 |
| Universe `wflow` | — | **−0.132** (green 11 · red 60) |

★ **The consequence is that today's sweep is anchored to the same Friday close as yesterday's run.**
This desk has now had **five consecutive runs** whose terminal bar is **2026-08-14**.

### (f) Blast radius — the phantom bar contaminates a second instrument — **[measured]**

`module_chart <TK> --read` pulls its own yfinance data and therefore inherits the NaN close. On both
`NVDA` and `XOM` it prints `볼린저: 확장 nan%`, `RSI: nan`, `모멘텀20d +nan%`, and
`MA정렬: … 가격 0/4 MA 위` — the last of which is not a bearish reading but a **NaN comparison**.
OBV, divergence and the swing-low stop still compute (volume/low-based). Any stage quoting `--read`
today must quote **only** those fields.

**✅ Rights retained today**: settled prices, RS, OBV, `vol_surge` through the **2026-08-14** close ·
OBV / divergence / swing-stop from `module_chart --read` · the fact that a full 08-17 session occurred
(volume is real).

**🚫 Rights revoked today**
1. **No 08-17 price, close, or return may be cited by any stage** — the desk does not have Monday's close.
2. **No "as of today/Monday" framing of the sweep.** The sweep's terminal bar is **2026-08-14 (Friday)**,
   for the fifth consecutive run.
3. **No Δflow described as "today's change"** — see G2; this is the 5th replay of one interval.
4. **`module_chart --read` RSI · Bollinger · momentum · MA-position may not be cited** (NaN, not a reading).
5. **No stage may re-pull prices later in this run and treat the result as comparable** — the bell rings
   at 22:30 KST, mid-run, after which a live partial bar is what the feed will hand back.

---

## G1 · News axis alive — 🔴 FAIL *(6th run — and today the outage was caught mid-collapse and mid-recovery)*

**Command**
- `SECTOR_FLOW_US.json §scoring` → `vel_axis false · vel_coverage 0.1672 · n_axes 3`
- Falsification probe A: `flow_read.news_velocity(q, 7, 30, kr=False)` over **40 names the sweep called silent**
- Falsification probe B (**new today**): the *identical* library call, **every 2 s for 92 s**
- Falsification probe C: the CLI path, `module_news_data fts search Nvidia --days 7 --count`, ×5
- Falsification probe D: `exec_remote(base, argv)` with the exact argv `_count_remote` builds

### (a) The four probes, in the order they ran — **[measured]**

| Clock (KST) | Path | Calls | Valid | Reading |
|---|---|---|---|---|
| 22:12–22:14 | sweep (library) | 299 | **50** | coverage **16.72%** |
| ~22:22 | library, 40 silent names | 40 | **0** | every one: `뉴스 API 응답 실패 + 로컬 FTS 색인 없음` |
| 22:23–22:25 | library, same argv ×41 | 41 | **0** | **one unbroken run of 41 failures over 92 s** |
| ~22:26 | **CLI**, `fts search Nvidia --days 7 --count` | 5 | **5** | `3773` five times |
| ~22:27 | `exec_remote`, `_count_remote`'s exact argv | 3 | **3** | `3866` (with `--mode or`), `1329`, `1329` |
| ~22:28 | **library, the same 40 silent names, re-run** | 40 | **40** | **100% valid in 18.4 s** |

### (b) What that sequence rules in and out

- **Not the argv.** Probe D ran the byte-exact argv `_count_remote` builds (`--mode or`, `--scope
  foreign`) and it returned **3866**. The library's query construction is sound.
- **Not "the news is quiet."** The 40 names the sweep scored as silent came back **40/40 measurable**
  minutes later: `COHR` 2.37 · `BX` 2.07 · `APO` 1.93 · `LITE` 1.92 · `MPC` 1.88 · `KKR` 1.77 ·
  `PSX` 1.50 · `NEM` 1.09 · `EMR` 1.04 · `ISRG` 0.64 · `WAB` 0.19 — a live spread, not a wall of zeros.
- **It is a contiguous outage window of the remote path**, ≥3 minutes long, that opened before the sweep
  and closed after it. Failures and successes arrive **in blocks, not at random** — which is exactly the
  shape the KR desk measured independently this morning (29 consecutive failures → 13 consecutive
  successes, 13/42 = 31.0%). **Two desks, two markets, one calendar day, same signature.**

### (c) The cumulative falsification record

| Run | Names re-probed | Genuinely quiet |
|---|---|---|
| 08-15 · 08-16 · 08-17 | 120 | **0** |
| **08-18 (today)** | **40** | **0** |
| **Total** | **160** | **0** |

⇒ **Not once in 160 hand-probes has the sweep's "silence" been real.** The sweep's velocity coverage
measures *the tunnel's uptime during a two-minute window*, and nothing about the news.

### (d) The survivor set is a clock artifact, re-confirmed

`RTX` carried `velocity 1.18` in yesterday's sweep, is **`None`** in today's, and probed **valid** in
today's re-run. The survivor set is **not monotone and not informative** — membership records which
names happened to be queried while the tunnel was open.

**✅ Rights retained today**: hand-probed per-name velocity **taken at a stated clock time** and marked
as such (40 names measured at ~22:28 KST) · article counts from the CLI path.

**🚫 Rights revoked today**
1. **The sweep's `velocity` field may not be cited by any stage**, nor may the 50 "survivors" be treated
   as a set with meaning.
2. **No theme-freshness or "this went quiet / this is heating up" claim from the sweep** (SWEEP ·
   ROTATION · EVENT_ALPHA · DEEP).
3. **`breadth` may not be read as a news-independent statistic** — carried from 08-17's measurement that
   `tag = flow_tag(price, velocity)` bypasses the axis-drop guard; today's tag deltas (`ORCL`, `MRVL`
   🟡→🟢) moved on **identical price data**, confirming it a second time.
4. **"No news found" may not be written anywhere today.** The correct sentence is *"not counted."*

---

## G2 · Scoring-scale continuity — 🟢 PASS *(literally — and the literal reading is now measurably too weak)*

**Command** `SECTOR_FLOW_US.json §scoring.n_axes` vs the prior snapshot's `_mode`.

| | Today | 08-17 |
|---|---|---|
| `n_axes` / `_mode` | **3 (`nonews`)** | 3 (`nonews`) |
| `vel_axis` | false | false |
| `asof` | **2026-08-14** | **2026-08-14** |

Same axis count ⇒ no apples-to-oranges subtraction. The gate passes on its own condition.

### ★ New measurement — **identical `asof` does not mean identical data**

| Comparison, today vs 08-17 | Count |
|---|---|
| `flow_score` **byte-identical** | **294 / 299** |
| `flow_score` **moved** | **5** — `COHR` 0.990→0.987 · `MU` 0.213→0.220 · `GOOG` −0.441→−0.443 · `APP` −0.589→−0.583 · `UPS` −0.739→−0.733 |
| **Close** values revised on any shared bar | **0 names** |
| **Volume** values revised on the 08-14 bar | **130 of 300 names** — median **0.077%**, max **0.771%** (`NVDA`: 176,900 shares) |

⇒ The provider **revises settled volume after the fact**. OBV and `vol_surge` both eat volume, so a
"frozen" universe still breathes at the third decimal. The magnitude is small — **max score movement
0.007, no tag changed on price grounds** — but the desk should stop saying *"the scores are identical
because the bar is the same."* They are identical **because nobody revised those names.**

**🚫 Rights revoked today**
1. **No Δflow may be described as "today's change".** Today is the **5th consecutive run** whose terminal
   bar is 2026-08-14; any Δ against yesterday is a **replay of one interval**, not a day's movement.
2. **No name may be promoted or demoted on a `flow_score` gap ≤0.01** — that is inside the measured
   revision noise.

---

## G3 · Who owns the sector sign — 🟢 PASS

**Command** `SECTOR_FLOW_US.json §sector_rotation[].top1_flips_sign` — full list printed, per the EXIT CHECK.

| Sector | top1 | weight | `wflow` | `wflow_ex_top1` | flips sign |
|---|---|---|---|---|---|
| Energy | XOM | 30.5% | +0.217 | +0.205 | no |
| **Information Technology** | **NVDA** | **19.4%** | **+0.023** | **−0.081** | 🚩 **YES** |
| Financials | BRK-B | 13.9% | −0.031 | −0.079 | no |
| **Industrials** | **CAT** | **8.7%** | **−0.047** | **+0.006** | 🚩 **YES** |
| Health Care | LLY | 19.4% | −0.115 | −0.031 | no |
| **Materials** | **LIN** | **24.7%** | **−0.169** | **+0.033** | 🚩 **YES** |
| Consumer Staples | WMT | 28.9% | −0.242 | −0.249 | no |
| Real Estate | WELL | 16.9% | −0.280 | −0.208 | no |
| Consumer Discretionary | AMZN | 40.2% | −0.378 | −0.369 | no |
| Communication Services | GOOGL | 38.3% | −0.436 | −0.414 | no |
| Utilities | NEE | 17.7% | −0.445 | −0.395 | no |

**3 of 11 flip.** ⚠ Identical set and identical numbers to 08-15, 08-16 and 08-17 — because it is
**the same terminal bar four times over**. Four identical readings of one Friday are **one observation**,
not four. `CAT` is the fragile one: an **8.7%** weight is enough to invert a −0.047 sector print.

**🚫 Revoked in ROTATION §2**: no promotion or demotion of IT · Industrials · Materials on the
weighted `wflow` bucket. Use `eqflow` / `breadth` (⚠ breadth itself is news-contaminated, G1) or hold.

---

## G4 · Risk-unit stability — 🔴 FAIL *(9th consecutive run, identical numbers)*

**Command** `scripts/risk_units.py --book --days {250,500,750}` — all three windows actually run.

| Window | Units | Where it disagrees |
|---|---|---|
| **250d** | **11** | splits `ANET`↔`ETN` and `AVGO`↔`NVDA`; **merges** `028050`+`316140` (two different theme labels in one unit) |
| **500d** | **10** | `ANET`+`ETN` = U0 · `AVGO`+`NVDA` = U1 · KR names separate |
| **750d** | **10** | identical grouping to 500d |

500d and 750d agree; **250d does not**. Book = 13 names (11 US · 2 KR).

**🚫 Revoked in SIZE · BET**: no concentration statement using a single unit count. Any concentration
sentence must carry the `--days` window **on the same line** as the conclusion.

---

## G5 · Does the universe cover the book — 🔴 FAIL *(staleness + one hole)*

| Check | Reading |
|---|---|
| US holdings inside `us_top300` | **11 / 11 ✅** (`MPC PSX ANET AVGO ETN HPE MET NDAQ NUE NVDA RTX`) |
| US holdings actually **scored** in today's sweep | **11 / 11 ✅** |
| `us_top300.csv` age | **34 days** (built 2026-07-15; limit ≤8) — **[FAIL]** |
| Universe rows vs sweep names | 300 vs **299** — **`EA` absent** |

★ `EA`'s failure mode **changed**: for five runs it appeared in the output with a null last bar; today
it is **gone from `names` entirely**. Same underlying hole, less visible than before.

**🚫 Revoked**: no flow / RS / OBV / short judgement on **`EA`** — the correct sentence is *"not
measurable,"* not *"no signal."* Any market-cap-derived weighting is **34 days stale**; sector weights
in the table above inherit that staleness.

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL

**Command** `scripts/snapshot_estimates.py --status`.

| Item | Reading |
|---|---|
| Files / calendar days | **10 / 24** ⇒ **0.42 per day** |
| Measured ETA to 40 samples | **≈72 days** vs ideal 30 ⇒ **2.4×** (limit 1.5×) |
| Gaps (days) | `[3, 4, 6, 3, 1, 2, 1, 1]` · median 2 · max 6 |
| Last save | **2026-08-14 — 4 days ago** |

⚠ Not recoverable retroactively — a day not saved is gone.

**🚫 Revoked in SIZE**: no `kelly_size --ic` output may be presented as an evidence-based size. If a
size appears at all it must be labelled **"mechanical ¼"**.

---

## G7 · Tool liveness — 🔴 FAIL *(9th consecutive run, same two)*

**Command** `--help` on every module entry point (`module_*/__main__.py`) and every non-underscore
script in `scripts/` — **50 entry points**, exit code checked.

| Entry point | `--help` | Functional probe | Citation right |
|---|---|---|---|
| `module_chart` | ❌ non-zero (usage text names `module_text_chart`; `read` is parsed as a ticker) | `module_chart NVDA --read` runs | **RETAINED for `<TK> --read` only** — ★ but see G0(f): RSI / Bollinger / momentum / MA-position are **NaN today** |
| `scripts/margin_history.py` | ❌ `ValueError: unsupported format character ')' at index 12` in argparse help interpolation | `margin_history.py MPC` prints FY2020–2025 margins | **RETAINED for the bare `<TK>` command line only** |
| other **48** | ✅ exit 0 | — | retained |

Both defects are in **help-string rendering**, not in the functions — the same diagnosis as the previous
eight runs, still unrepaired (repair is a human-approval item, rule 1).

---

## Carry to HANDOVER

1. **The sweep is anchored to 2026-08-14 for the fifth consecutive run.** Nothing in this run may be
   dated Monday or Tuesday.
2. **A new instrument-defect class is on the board: the three-quarters bar** (OHL+V present, Close
   absent, full-session volume). Every completeness heuristic the desk owns is volume-based and
   **passes on it**. The only test that fired was non-null close count.
3. **The D225-KR axis guard converted that defect into a visible outage instead of a silent
   re-ranking.** This is the first time the protocol's central fix has been observed paying out on a
   defect it was not designed for.
4. **News-axis silence remains 0-for-160 real.** The outage is a contiguous block in the remote path;
   both desks measured the same block signature on the same day.
5. **Four "identical" flipper tables are one observation**, not four.
