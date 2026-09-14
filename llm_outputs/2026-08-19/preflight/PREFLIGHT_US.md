# PREFLIGHT — 2026-08-19 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-19 21:51–21:58 = ET 2026-08-19 08:51–08:58, WEDNESDAY — US cash PRE-MARKET**
> (bell 09:30 ET = 22:30 KST, i.e. *after* this preflight, during the run). Sweep download 21:51 ·
> scoring 21:53 · sweep `asof` **2026-08-18 (Tuesday close)**.
>
> ★ **Two things broke in this desk's favour today, and one broke in a new direction.**
>
> ① **The five-run price freeze is over, and the "three-quarters bar" retired itself.** Yesterday's
> headline defect — a 2026-08-17 daily bar carrying Open/High/Low/Volume for 300 of 301 tickers and a
> **NaN Close for 300 of 301** — is **gone from the feed**. Today's download returns 08-17 with
> **Close 300/300**, and 08-18 settled normally on top of it. The sweep's terminal bar moved
> **08-14 → 08-18**, the first advance in **six runs**, and it advanced by **two sessions at once**.
> ⇒ The provider backfilled. No repair was made on this side; **G0 passes for the first time on the US
> desk.**
>
> ② **The consequence is that today is the first run in six with a genuine Δ** — and it is large:
> **298 of 299 flow scores moved** against the prior snapshot, median |Δ| **0.127**, **44 tag changes**.
> ⚠ But that Δ spans **two sessions (08-17 + 08-18)**, not one, because the prior snapshot in
> `history.json` is dated **2026-08-14**. Any stage writing "today's change" would be wrong by a factor
> of two. This is the single most citation-relevant number in this table.
>
> ③ **G1's cause diverged from this morning's KR diagnosis, measured on the same bridge, the same day.**
> The KR desk closed at 08:29 KST with *"~50-call quota per ~2-min window; the sweep burns it in the
> first 51 tickers; the survivor set is deterministic and mcap-aligned."* On the US side at 21:52 the
> survivor **count** matched almost exactly (**51**, as in KR's 51) but the **shape did not**: KR's
> survivors were **one unbroken run of indices 0–50**; the US survivors are **44 separate runs, longest
> 3, forty of them singletons, spread over indices 16–295**. Same bridge, same day, same call — one
> desk got a clean prefix, the other got interleaved flicker. ⇒ **The count is quota-shaped; the
> placement is not deterministic.** KR's rights-line #3 ("survivors survived because they are the top
> of the market-cap sort") is **market-and-run specific and does not hold here.**
>
> ⚠ **Filename deviation, logged (10th consecutive run, same reason):** the composition table names
> this `preflight/PREFLIGHT.md`, but the `industry_kr` desk wrote its rights table to that path this
> morning (08:17–08:22 KST). Overwriting a sibling desk's output is not a correction, so the US table
> is written as `PREFLIGHT_US.md` in the same folder — documented practice on 08-10 · 08-12 · 08-13 ·
> 08-14 · 08-15 · 08-16 · 08-17 · 08-18. Human decision on permanent market-suffixing still pending
> (PROMPT_MAP §6).

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** *(first US PASS — the 08-17 phantom bar was backfilled upstream)* | 08-17 **Close 300/300** (was 1/301) · 08-18 **Close 300/300** · last-bar volume / prior-20d median **0.938** (q25 0.789 · q75 1.165, n=300) · `SPY` closes present through **08-18** ⇒ names and benchmark share one terminal date, **no RS-leg misalignment**. Frame ends **2026-08-18**, `asof` **2026-08-18** |
| **G1** news axis alive | 🔴 **FAIL** *(7th consecutive run)* | Sweep coverage **17.06% (51/299)**. Falsification: **0/40** at 21:53 · **0/5** CLI at 21:54 · burst probe **15 consecutive failures → 32 consecutive successes** · **40/40** re-probe at 21:57 · CLI **3/3** at 21:58. ★ Failure surfaces at the **TLS layer** (`SSLEOFError: EOF in violation of protocol`), not as an HTTP 429. Cumulative **0 of 200** false-silences across five runs |
| **G2** scoring-scale continuity | 🟢 **PASS** | **3-axis (`nonews`) vs 3-axis (`nonews`)** ⇒ no apples-to-oranges subtraction. ★ **But the Δ baseline is 2026-08-14, so every `delta` field is a TWO-session move.** 298/299 scores moved · median \|Δ\| **0.127** · **44** tag changes. The five-run replay is over |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **3 of 11**: Financials/`BRK-B` **13.9%** · Industrials/`CAT` **8.7%** · Materials/`LIN` **24.7%**. ★ **The set changed for the first time in five runs**: IT/`NVDA` left it, Financials/`BRK-B` entered — because the bar finally moved |
| **G4** risk-unit stability | 🔴 **FAIL** *(10th consecutive run, identical numbers)* | 250d **11 units** · 500d **10** · 750d **10** — 500 and 750 agree, **250 does not** |
| **G5** does the universe cover the book | 🔴 **FAIL** *(staleness + one hole)* | **11/11 US holdings inside `us_top300` AND scored ✅**. But `us_top300.csv` is **35 days old** (limit ≤8), and **`EA`** is still absent from the sweep (299 of 300) — 7th consecutive run unmeasurable |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** *(but the daemon fired today)* | 11 files / **29 calendar days** = 0.38/day ⇒ measured ETA **≈76 days** vs ideal 30 = **2.6×** (limit 1.5×). ★ Last save = **today, 2026-08-19** — the 5-day gap 08-14→08-19 closed |
| **G7** tool liveness | 🔴 **FAIL** *(10th consecutive, same two)* | **50 entry points** probed, **2** non-zero `--help`: `module_chart` · `scripts/margin_history.py`. Both pass a functional probe ⇒ citation retained **for those command lines only** — ★ and unlike yesterday, `module_chart --read` returns **real numbers**, because G0 is clean |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate and it passed).
**This is the best instrument state this desk has recorded. The five remaining failures are all
long-standing and none of them is new.**

Today this desk **cannot** speak with the sweep's news-velocity axis, the 51 survivors as a set, theme
freshness, "it went quiet", `breadth` as a news-independent reading, a single concentration number, an
`--ic`-derived size, or `EA`. It **can** speak — for the first time in six runs — with **settled prices
through the 2026-08-18 close**, a **real two-session Δ**, RS, OBV, `eqflow`, `vol_surge`, the full
`module_chart --read` panel, FINRA short pressure, CFTC COT positioning, FRED series, primary filings,
and **hand-probed per-name news velocity, which measured 40/40 at 21:57 KST.**

---

## G0 · Bar completeness · date alignment — 🟢 **PASS** *(the defect retired itself upstream)*

Not one of the seven. Carried because the KR desk measured it into existence on 08-12. It has never
passed on the US desk before today.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-19.pkl`
(84 rows × 1806 columns = 301 tickers × 6 fields) + `SECTOR_FLOW_US.json §scoring`.

### (a) The two most recent rows, field by field — **[measured]**

| Field | 2026-08-17 today | 2026-08-17 **yesterday** | 2026-08-18 today |
|---|---|---|---|
| Open | 300 / 301 | 300 / 301 | **300 / 301** |
| High | 300 / 301 | 300 / 301 | **300 / 301** |
| Low | 300 / 301 | 300 / 301 | **300 / 301** |
| Volume | 300 / 301 | 300 / 301 | **300 / 301** |
| **Close** | **300 / 301** | **1 / 301** ← the defect | **300 / 301** |

(The one missing name in every column is `EA`, which is a separate hole — see G5.)

★ **The three-quarters bar is gone.** Yesterday this desk documented a new defect class: a bar with
full-session volume (1.78 bn shares) and a NaN close on 300 of 301 names, invisible to every
volume-based completeness heuristic the desk owns. Today the same 08-17 row comes back **complete**.
Nothing on this side was repaired — INSTRUMENT_CHECK does not repair instruments (rule 1), and
yesterday's action was **truncation, not repair**. The provider backfilled the close.

⚠ **What this does and does not license.** It licenses citing 08-17 and 08-18 prices. It does **not**
retire the defect class: a bar that is three-quarters real remains undetectable by volume ratio, and
the only test that fired yesterday — **non-null close count** — is now the gate's primary test, not its
fallback. That change is permanent regardless of today's clean reading.

### (b) Completeness of the terminal bar — **[measured]**

| Test | Reading on the 08-18 row | Conclusion |
|---|---|---|
| Row present in frame? | yes, index ends **2026-08-18** | Tuesday is here |
| **Non-null closes on the last row** | **300 / 301** | ← the primary test, and it fires clean |
| Last-bar volume / prior-20d median | **median 0.938** · q25 **0.789** · q75 **1.165** (n=300) | settled full session |
| Benchmark alignment | `SPY` closes **08-13 777.88 · 08-14 776.34 · 08-17 772.67 · 08-18 767.45** | names and bench end on the **same date** |

★ The last item is the KR desk's failure mode this morning (names 08-18, bench `^KS11` 08-14, RS legs
misaligned, `rs20` median shifting −1.17pp on re-alignment). **It does not occur here** — `SPY` carries
08-18. The gate is checked, not assumed.

### (c) Sessions gained — **[measured]**

The prior usable snapshot was **2026-08-14**. Today's is **2026-08-18**. That is **two new sessions
(08-17, 08-18) in one step**, after five runs of zero. `n_new_sessions_since_prior_run = 2` — which is
exactly the stamp `D280` says nothing writes automatically. It is written here by hand.

**✅ Rights retained today**: settled prices, closes, returns, RS, OBV, `vol_surge` through the
**2026-08-18** close · the full `module_chart --read` panel · benchmark-relative statistics.

**🚫 Rights revoked today**
1. **No 08-19 price of any kind.** The US cash session for 08-19 has not opened at preflight time
   (bell 22:30 KST, after this table). The desk has Tuesday, not Wednesday.
2. **No stage may re-pull prices after 22:30 KST and treat the result as comparable to the sweep** —
   after the bell the feed hands back a live partial bar.
3. **Any Δ must be labelled two-session (08-14 → 08-18)** — see G2.

---

## G1 · News axis alive — 🔴 FAIL *(7th consecutive run — and the shape disagrees with this morning's KR reading)*

**Command**
- `SECTOR_FLOW_US.json §scoring` → `vel_axis false · vel_coverage 0.1706 · n_axes 3 · scored 299 · dropped_missing_axis 0`
- Probe A: `flow_read.news_velocity(q, 7, 30, kr=False)` over **40 names the sweep called silent**
- Probe B (CLI): `module_news_data fts search Nvidia --days 7 --count --scope foreign` ×5
- Probe C (transport): bare `urllib` / `requests` POST to the tunnel, default and unverified SSL context
- Probe D (burst): the identical library call **every 2 s for 121 s**
- Probe E (falsification): **the same 40 silent names, re-run after recovery**

### (a) The probes, in the order they ran — **[measured]**

| Clock (KST) | Path | Calls | Valid | Reading |
|---|---|---|---|---|
| 21:52–21:53 | sweep (library) | 299 | **51** | coverage **17.06%** |
| 21:53:28–21:53:38 | library, 40 silent names | 40 | **0** | every one: `뉴스 API 응답 실패 + 로컬 FTS 색인 없음` |
| ~21:54:0x | **CLI** `fts search Nvidia --count` | 5 | **0** | `URLError(FileNotFoundError(2, 'No such file or directory'))` ×5 |
| ~21:54:2x | bare `urllib` / `requests`, default **and** unverified SSL | 5 | **0** | **`SSLEOFError(8, 'EOF occurred in violation of protocol')`** |
| 21:54:50–21:56:51 | library, same argv, ×47 at 2 s | 47 | **32** | **15 consecutive failures, then 32 unbroken successes** |
| 21:57:24–21:57:42 | **library, the same 40 silent names, re-run** | 40 | **40** | **100% valid in 18.1 s** |
| 21:58:04–21:58:08 | CLI, re-run | 3 | **3** | `3809` three times |

### (b) ★ The failure is at the transport layer, not the query layer — **[measured]**

DNS resolves (`impolite-coherent-props.ngrok-free.dev → 3.114.93.84`). The connection then dies during
the **TLS handshake**: `SSLEOFError(8, 'EOF occurred in violation of protocol')`, identically under
`urllib` with the default context, `urllib` with `_create_unverified_context()`, and `requests`.

⇒ **This is not an HTTP 429.** A quota rejection would return a status line and a body. The remote end
is **closing the socket mid-handshake**. Whatever the mechanism is, it is upstream of any request the
client sends, which is why the argv, the scope flag and the query string are all irrelevant to it.

⚠ The client-side error text is also **misleading** in the CLI path: Windows OpenSSL surfaces the same
socket failure as `URLError(FileNotFoundError(2, 'No such file or directory'))`, which reads like a
missing file and is not one. Anyone diagnosing this from the CLI message alone will look in the wrong
place. Logged as an instrument-legibility defect, not repaired (rule 1).

### (c) ★★ The survivor shape contradicts this morning's KR conclusion — **[measured]**

The `industry_kr` desk closed at 08:29 KST today with a confirmed diagnosis: *~50 calls per ~2-minute
window; the sweep burns the whole bucket in its first 51 tickers; the survivor set is therefore
**deterministic** and **perfectly aligned with the market-cap sort**.* Its evidence was a burst probe
with run structure `[('1', 50), ('0', 90)]` and sweep survivor indices `[0, 1, 2, …, 50]`.

The US sweep, on **the same bridge, the same calendar day**, nine hours later:

| | KR sweep (08:17) | **US sweep (21:52)** |
|---|---|---|
| Survivors | **51** / 827 | **51** / 299 |
| Distinct success runs | **1** | **44** |
| Longest success run | **51** | **3** |
| Singleton successes | **0** | **40** |
| Index span of survivors | **0 – 50** (contiguous prefix) | **16 – 295** (spread over the whole universe) |

**The count agrees almost exactly. The placement does not agree at all.** KR drained a bucket in one
block; the US run collected isolated tokens across the entire sweep. Both landed on **51**.

**Stated positively:** the bridge grants **on the order of 50 successful calls per sweep**, and *where*
those 50 land is **not stable across runs or markets** — it can be a clean prefix or it can be
scattered singletons. The count is the reliable part; the membership is not.

⇒ **KR's rights-line #3 does not transfer.** Its warning was *"the 51 survivors are a market-cap
selection bias"*. Here the survivors span indices 16–295, so they are **not** the largest 51 names —
they are an arbitrary sample. The survivor set is unusable in both markets, but for **different
reasons**, and a desk that imported KR's reason would be defending against the wrong artifact.
(This is the same cross-market import error the protocol's own DEEP-budget note logs as a W1 violation.)

### (d) Recovery — **[measured]**

Probe D caught the transition live: **15 consecutive failures (≈36 s), then 32 consecutive successes
(≈64 s, no break).** The KR desk measured recovery at **77.2 s** this morning. Same class, different
constant. After recovery the bridge stayed open for **32 calls in ~64 s** without locking again — below
the ~50/2min ceiling, so the ceiling was never re-tested.

### (e) The local fallback is structurally absent — **[measured, new]**

Every failure note reads `뉴스 API 응답 실패 + **로컬 FTS 색인 없음**`. Direct measurement of why:

| File | Size |
|---|---|
| `data/news_alert.db` | **0 bytes** |
| `data/news_fts.db` | **0 bytes** |
| `data/news_fts_kr.db` | **0 bytes** |

⇒ There is **no local fallback at all** — not a stale one, an empty one. Under P6 the news DBs are
server-owned and the client reads them over the API by design, so this is **the documented
architecture, not a defect**. But it means the news axis has **exactly one point of failure and zero
degraded mode**: when the tunnel drops handshakes, coverage is not reduced, it is zero. Repair
direction (rate-limit/backoff in the sweep · a client-side FTS index · a batch endpoint) is **code, and
therefore a human-approval item** (rule 1).

### (f) The cumulative falsification record

| Run | Names re-probed | Genuinely quiet |
|---|---|---|
| 08-15 · 08-16 · 08-17 | 120 | **0** |
| 08-18 | 40 | **0** |
| **08-19 (today)** | **40** | **0** |
| **Total** | **200** | **0** |

⇒ **Not once in 200 hand-probes has the sweep's "silence" been real.** Today's re-probe returned a live
spread, not a wall of zeros: `TGT` 2.30 · `LITE` 2.14 · `BX` 1.84 · `APO` 1.66 · `KKR` 1.56 · `CRM` 1.49
· `PSX` 1.47 · `PWR` 1.40 · `ACN` 1.37 · `ANET` 1.30 · `HPE` 1.30 (measured 21:57:24–21:57:42 KST).

### (g) ✅ The 08-09 inflation guard held again

51 of 299 names had a 4th axis available — the exact condition that produced the **+0.305 average score
inflation** on 08-09. Output reads `vel_axis: false · n_axes: 3 · scored 299 · dropped_missing_axis 0`:
**the 51 surviving velocities were discarded from scoring and all 299 names were scored on the same 3
axes.** The inflation path stayed closed.

**✅ Rights retained today**: hand-probed per-name velocity **taken at a stated clock time and marked as
such** (40 names at 21:57 KST) · article counts from the CLI path (`Nvidia` 7d = **3809**, 21:58 KST).

**🚫 Rights revoked today**
1. **The sweep's `velocity` field may not be cited by any stage**, nor may the 51 "survivors" be treated
   as a set with meaning — today they are an **arbitrary sample**, not a mcap-ordered one.
2. **No theme-freshness or "this went quiet / this is heating up" claim from the sweep** (SWEEP ·
   ROTATION · EVENT_ALPHA · DEEP).
3. **`breadth` may not be read as a news-independent statistic** — `tag = flow_tag(price, velocity)`
   bypasses the axis-drop guard (`D261`/`M701`, measured a fourth time).
4. **"No news found" may not be written anywhere today.** The correct sentence is *"not counted."*
5. **Any hand probe must carry its clock time on the same line**, and a failed probe is written as a
   failure, never as a zero.

---

## G2 · Scoring-scale continuity — 🟢 PASS *(and today the gate's own weakness is what matters)*

**Command** `SECTOR_FLOW_US.json §scoring.n_axes` vs the prior snapshot's `_mode` in
`llm_outputs/sector_flow/history.json`.

| | Today | Prior snapshot |
|---|---|---|
| `n_axes` / `_mode` | **3 (`nonews`)** | **3 (`nonews`)** |
| `vel_axis` | false | false |
| snapshot key | **2026-08-18** | **2026-08-14** |

Same axis count ⇒ no apples-to-oranges subtraction. The gate passes on its own condition.

### ★ The number every downstream stage must carry: **the Δ is two sessions wide**

`history.json` holds `2026-08-14` and, as of this run, `2026-08-18`. **There is no 08-17 entry** — the
08-18 desk run wrote its truncated frame back onto the 08-14 key. So the `delta` field in every name
and every sector row is **08-18 minus 08-14 = two trading sessions (08-17 and 08-18 combined)**.

| Measurement vs the 2026-08-14 snapshot | Count |
|---|---|
| `flow_score` **byte-identical** | **1 / 299** |
| `flow_score` **moved** | **298 / 299** · median \|Δ\| **0.127** |
| **tag changes** | **44** |
| Largest moves | `DHR` −0.812→+0.333 (**+1.145**) · `TRGP` −0.814→+0.252 (**+1.066**) · `MU` +0.220→−0.541 (**−0.761**) · `COHR` +0.987→+0.254 (**−0.733**) · `INTC` +0.115→−0.608 (**−0.723**) |

⇒ **The frozen board is unfrozen.** For five runs this line read "294/299 identical". Today it reads
the opposite. That is the expected consequence of gaining two settled sessions, and it is the reason
the rest of this run has something to say.

**🚫 Rights revoked today**
1. **No Δ may be described as "today's change" or "one-day".** Every Δ in this run is
   **08-14 → 08-18, two sessions.** A stage that writes "moved today" is wrong by a factor of two.
2. **No name may be promoted or demoted on a `flow_score` gap ≤0.01** — inside the measured
   provider-revision noise (08-18's measurement: 130 of 300 settled volumes revised, median 0.077%).

---

## G3 · Who owns the sector sign — 🟢 PASS

**Command** `SECTOR_FLOW_US.json §sector_rotation[].top1_flips_sign` — full list printed, per the EXIT CHECK.

| Sector | top1 | weight | `wflow` | `wflow_ex_top1` | flips sign |
|---|---|---|---|---|---|
| Energy | XOM | 30.5% | +0.354 | +0.347 | no |
| Health Care | LLY | 19.4% | +0.114 | +0.149 | no |
| Consumer Staples | WMT | 28.9% | +0.083 | +0.027 | no |
| **Financials** | **BRK-B** | **13.9%** | **+0.028** | **−0.015** | 🚩 **YES** |
| **Industrials** | **CAT** | **8.7%** | **−0.028** | **+0.032** | 🚩 **YES** |
| **Materials** | **LIN** | **24.7%** | **−0.117** | **+0.060** | 🚩 **YES** |
| Information Technology | NVDA | 19.4% | −0.195 | −0.268 | no |
| Real Estate | WELL | 16.9% | −0.296 | −0.213 | no |
| Consumer Discretionary | AMZN | 40.2% | −0.379 | −0.336 | no |
| Utilities | NEE | 17.7% | −0.397 | −0.424 | no |
| Communication Services | GOOGL | 38.3% | −0.439 | −0.432 | no |

**3 of 11 flip.** ★ **The set changed for the first time in five runs**: `NVDA`/IT **left** the flipper
set (IT is now −0.195 weighted and −0.268 ex-top1 — same sign, so the sector print no longer depends on
one name), and `BRK-B`/Financials **entered** it. `CAT` remains the most fragile: an **8.7%** weight
inverting a −0.028 print means the Industrials sign is essentially a coin resting on one company.

⚠ The four identical readings of 08-15/16/17/18 were **one observation**, as logged. Today is a genuine
**second** observation.

**🚫 Revoked in ROTATION §2**: no promotion or demotion of **Financials · Industrials · Materials** on
the weighted `wflow` bucket. Use `eqflow` / `breadth` (⚠ `breadth` is itself news-contaminated, G1) or
hold. Sector market-cap weights are **35 days stale** (G5) and this table inherits that.

---

## G4 · Risk-unit stability — 🔴 FAIL *(10th consecutive run, identical numbers)*

**Command** `scripts/risk_units.py --book --days {250,500,750}` — all three windows actually run.

| Window | Units | Grouping | In-group residual corr | Stability ARI |
|---|---|---|---|---|
| **250d** | **11** | splits `ANET`↔`ETN` and `AVGO`↔`NVDA`; **merges** `028050`+`316140` (two different theme labels in one unit) | +0.6062 | 0.4902 |
| **500d** | **10** | `ANET`+`ETN` = U0 · `AVGO`+`NVDA` = U1 · KR names separate | +0.5249 | 0.1899 |
| **750d** | **10** | identical grouping to 500d | +0.5141 | 0.3810 |

500d and 750d agree; **250d does not**. Book = 13 names (11 US · 2 KR).
⚠ The tool's own threshold-sensitivity table shows unit counts of **12 → 4** across `dist` 0.40–0.85 on
the same data, and its ARI line warns that fit and stability move in opposite directions. The unit
count is a **choice**, not a measurement.

**🚫 Revoked in SIZE · BET**: no concentration statement using a single unit count. Any concentration
sentence must carry the `--days` window **on the same line** as the conclusion.

---

## G5 · Does the universe cover the book — 🔴 FAIL *(staleness + one hole)*

**Command** book from `module_paper_book status`; universe `data/us_universe/us_top300.csv`;
scored set from today's sweep.

| Check | Reading |
|---|---|
| US holdings inside `us_top300` | **11 / 11 ✅** (`ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX`) |
| US holdings actually **scored** in today's sweep | **11 / 11 ✅** |
| `us_top300.csv` age | **35 days** (built 2026-07-15; limit ≤8) — **[FAIL]** |
| Universe rows vs sweep names | 300 vs **299** — **`EA` absent** (7th consecutive run) |
| Sweep names not in universe | **0** |

`EA` carries **0 non-null fields on every row of the 84-row frame** — it is not a stale bar, it is an
empty column. Its failure mode is unchanged from 08-18.

**🚫 Revoked**: no flow / RS / OBV / short judgement on **`EA`** — the correct sentence is *"not
measurable,"* not *"no signal."* Any market-cap-derived weighting (including every sector weight in G3)
is **35 days stale**.

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL *(but the gap closed today)*

**Command** `scripts/snapshot_estimates.py --status`.

| Item | Reading |
|---|---|
| Files / calendar days | **11 / 29** ⇒ **0.38 per day** |
| Measured ETA to 40 samples | **≈76 days** vs ideal 30 ⇒ **2.6×** (limit 1.5×) |
| Gaps (days) | `[4, 6, 3, 1, 2, 1, 1, 5]` · median 3 · max 6 |
| Last save | **2026-08-19 — today** |

★ The daemon **did** fire today, closing the 5-day gap that yesterday's table flagged (08-14 → 08-19).
The rate is still 2.6× slower than ideal, so the gate fails on its own condition, but the trend line
this run is toward the daemon being alive, not dead.
⚠ Not recoverable retroactively — a day not saved is gone.

**🚫 Revoked in SIZE**: no `kelly_size --ic` output may be presented as an evidence-based size. If a
size appears at all it must be labelled **"mechanical ¼"**.

---

## G7 · Tool liveness — 🔴 FAIL *(10th consecutive, same two)*

**Command** `--help` on every module entry point (`module_*/__main__.py`) and every non-underscore
script in `scripts/` — **50 entry points**, exit code checked.

| Entry point | `--help` | Functional probe | Citation right |
|---|---|---|---|
| `module_chart` | ❌ non-zero (usage text names `module_text_chart`; `read` parsed as a ticker) | `module_chart NVDA --read` → OBV distribution (20d slope −68%) · MA bull stack, price above 3/4 · **Bollinger width 21.5%** · **RSI 77.4** · **mom20d +3.6%** · swing stop 190.01 | **RETAINED for `<TK> --read` only** — ★ and today the **full panel is citable**: G0 is clean, so RSI / Bollinger / momentum / MA-position are real numbers, not the NaNs of 08-18 |
| `scripts/margin_history.py` | ❌ `ValueError: unsupported format character ')' at index 12` in argparse help interpolation | `margin_history.py MPC` prints FY2018–2025 gross margins (peak FY2022 14.5% · trough FY2020 5.8% · median 10.5%) | **RETAINED for the bare `<TK>` command line only** |
| other **48** | ✅ exit 0 | — | retained |

Both defects are in **help-string rendering**, not in the functions — the same diagnosis as the previous
nine runs, still unrepaired (repair is a human-approval item, rule 1).

---

## Carry to HANDOVER

1. **The price freeze is over. The terminal bar is 2026-08-18 and it advanced by two sessions at once.**
   Every Δ in this run is **08-14 → 08-18**, and must be labelled two-session. Nothing may be dated
   08-19 — the US session has not opened at preflight time.
2. **The three-quarters bar was fixed upstream, not here.** The defect class stays on the board: the
   only test that detects it is **non-null close count**, which is now this gate's primary test.
3. **G1's mechanism is at the TLS layer, and its survivor shape is not stable across desks.** KR
   measured a contiguous prefix and concluded mcap selection bias; US measured 44 scattered runs with
   40 singletons on the same day and the same bridge. **Both got exactly 51 survivors.** The count is
   quota-shaped; the membership is arbitrary. **Do not import the KR reason.**
4. **There is no local news fallback — the three news DBs are 0 bytes.** By P6 this is the architecture,
   not a defect, but it means the news axis has one point of failure and no degraded mode.
5. **News-axis silence remains 0-for-200 real.**
6. **The flipper set changed for the first time in five runs** — `NVDA` out, `BRK-B` in, `CAT` still the
   fragile one. Today is the second real observation of this table, not the sixth.
7. **PASS 3 / FAIL 5 is the best instrument state recorded on this desk**, and all five failures are
   long-standing (G4 · G5 · G6 · G7 · G1), none new.

---

## ⚠ APPEND-ONLY CORRECTION — G5 audited the WRONG BOOK (found 22:40 KST by PREMORTEM Lens 4, verified independently)

**The G5 section above is left exactly as written.** This block records what refuted it, per the §4c
rule that verification arriving after the assertion is a finding and does not get edited away.

**What G5 did**: it read the book from `module_paper_book status` — the **paper** book — and reported
*"11/11 US holdings inside `us_top300` AND scored."*

**What the desk's own `cycle_exposure.py` reads**: `module_KIS.fetch_overseas_balance()` — the **real
KIS account**. Independently re-fetched at **22:40 KST (09:40 ET, post-bell, LIVE intraday marks —
labelled as such and used below only for MEMBERSHIP, never for price)**:

| | list | n |
|---|---|---|
| **Real KIS book** | `AVGO LITE NVDA ANET COHR ETN HPE MPC NUE PSX RTX T` | **12** |
| Paper book (what G5 checked) | `ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX` | 11 |
| **In real, NOT in paper** | **`COHR` · `LITE` · `T`** | 3 |
| **In paper, NOT in real** | `MET` · `NDAQ` | 2 |

Balances also differ: real `total_asset_krw` **15,565,108** / `krw_deposit` **4,827,207** / USD cash
**550.86**, against the paper book's ₩17,805,044 total and ₩4,938,207 cash. **They are two different
objects and the run treated them as one.**

**Re-run of the G5 test against the REAL book**: **12 / 12 inside `us_top300` AND scored — 0 missing.**
⇒ **The VERDICT survives; the EVIDENCE did not.** G5's staleness FAIL (35-day universe) and the `EA`
hole are unaffected.

★ **Three consequences that do change what this run knows:**
1. **`LITE` is the real book's #2 position by value** (**$848.01 = 12.01% of the $7,059.28 invested**,
   behind `NVDA` 15.59%) — and it was **never universe-checked**, because G5 was looking at a list it
   is not on. `COHR` adds 4.27%, so **optical/interconnect is 16.28% of invested**, larger than the
   registered rank-2 Energy epicenter (`PSX`+`MPC` = 15.45%) and larger than defense (`RTX` 9.60%).
2. **`T` (AT&T) is 9.59% of invested and maps to no cycle in the registry** — and it sits in
   **Communication Services, the sector this run holds UW and just assigned as Rotating-2 DEEP.** Its
   own flow is **+0.383 🟡, OBV 매집 +0.291, RS20 +9.3 vs `SPY`** (settled 08-18): the book's single
   COMM holding is accumulating inside the sector the desk is underweight.
3. **Two holdings carry the board's worst two-session deltas**: `AVGO` **−0.488 (worst of 299)** and
   `COHR` **−0.733**. Neither was visible as a *holding* to any gate this run.

**🚫 Additional right revoked, retroactively, for the rest of this run**: no stage may describe "the
book" without naming which book. **`CYCLE_EXPOSURE`, `SIZE` and `BET` read the real KIS account;
`G5` and `HANDOVER §0`/`§3` read the paper book.** Registered as dig **`D288`** — *G5 must read the
same book the exposure gate reads, or print both and diff them.*
