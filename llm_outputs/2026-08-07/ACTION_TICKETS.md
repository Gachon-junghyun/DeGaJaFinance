# ACTION_TICKETS — industry_US — 2026-08-07 (Fri) · **written BY HAND; the script's output is superseded**

> Pre-committed conditional tickets. **Analytical artifact only — DRY-RUN, no order is sent, and a human
> executes separately via `module_kis --order … --execute`. Zero buy/sell recommendation (P4).**
> ⚠ **No cycle GAP fired** (rank 1 epicenter **23.67% vs a 12.0% floor**; rank 2 **10.06% vs 8.0%**), so
> **the tape-independent core-starter clause does NOT apply this run.**

## 🚨 0 · Why this file was written by hand — `scripts/action_bracket.py` armed a conditional on an event that had ALREADY RESOLVED

The script ran cleanly at **10:2x ET** and produced:

> **Nearest binary:** July Employment / NFP (D-0) — both-sides armed below.
> `BRACKET::A_soft` **IF … prints toward soft** → NVDA · `BRACKET::B_strong` **IF … prints toward strong** → XLE

**Three defects, and the first one is a one-line fix because the data is already in the file:**

1. 🚨 **NFP printed at 08:30 ET — roughly two hours BEFORE the script ran.** And
   `llm_outputs/2026-08-07/CATALYST_WATCH.json` **already carries the field the fix needs**:
   `{"date": "2026-08-07", **"time_et": "08:30"**, "event": "July Employment / NFP", …, "days_until": 0}`.
   ⇒ **`action_bracket.py` reads `days_until == 0` and never compares `time_et` against the run clock**, so
   on any morning-print day it arms a "conditional" whose condition is already known. **The answer is
   known: the print came in SOFT (−23,000 vs +83,000 consensus)** ⇒ **branch A_soft is the RESOLVED side
   and the ticket is a description, not a pre-commitment — D122's class** (a condition already true at
   registration cannot discriminate).
2. 🚨 **The soft/strong → asset mapping is hard-coded to a CUT-cycle Fed.** *"soft ⇒ buy NVDA / strong ⇒
   buy XLE"* encodes a reaction function in which a strong print is pro-cyclical. **This Fed is debating a
   HIKE** — it held **3.50–3.75% on 07-29 with THREE hike dissents**, CME September **hike** odds fell
   **67% → 56%**, and Gov. Cook said on 08-05 she would back a hike absent inflation improvement. ⇒ **in a
   hike-risk regime a STRONG print is hawkish and a SOFT print is dovish, so the mapping is arguably
   inverted.** **Not changed here — a scoring change is human-gated (P5).**
3. ⚠ **The prices and the FX are LIVE and inconsistent with the run's other instrument (D74 / D5).** The
   script quoted **NVDA ≈ $222.315** against the **08-06 settled close of 218.99**, and **fx 1419** against
   **`cycle_exposure.py`'s 1380** minutes earlier. **Every size it printed is illustrative off an
   unsettled bar.**

⇒ **New dig `D207`, with both halves.** ★ **And a fourth, which is what caused a separate error in this
run's PREMORTEM**: **the `[EARNINGS]` block carries NO BMO/AMC field at all** —
`{"date": "2026-08-07", "event": "VST earnings", "ticker": "VST", …}` has no `time_et`. **That ambiguity is
exactly what let PREMORTEM Lens 2 assert VST reported AMC when it reported PRE-MARKET**
(`BLINDSPOT_PREMORTEM.md` §1). **A bracket that settles on a close cannot be scored without knowing which
side of that close its catalyst lands on.**

⚠ **D155/D188 did NOT reproduce**: the script's output was internally consistent this run, because the
call was made at **23:2x KST — before the run crossed local midnight.** Recorded as a null result, not as
a fix.

---

## 1 · The binary that already fired — recorded as RESOLVED, not armed

| | |
|---|---|
| **Event** | **July Employment Situation, 2026-08-07 08:30 ET** `[bls✓]` |
| **Observable (both halves, C2)** | payrolls **−23,000** vs **+83,000** consensus `[cnbc body]`; **unemployment 4.1%, DOWN from 4.2%** `[bloomberg · wsj · marketwatch · investing_en]`; **prior two months revised −74,000** `[guardian body]` |
| **Direction in THIS regime** | **DOVISH** — hike odds fall, front end rallies ⇒ a **BULL** steepener |
| **State** | ✅ **RESOLVED. No conditional is armed on it.** The forward question it created is **frozen as `S66`** (below), not as a ticket |

## 2 · The forward bracket that carries it — **`S66`**, registered at PREMORTEM, four exhaustive branches

**Frozen observable**: `ΔDGS2` = `DGS2`(first settled close covering 08-07) − **4.18** **and**
`ΔHY OAS` = `BAMLH0A0HYM2`(same) − **2.75**, both `[FRED]`, anchored on the **08-05** print.
**Settles at the first FRED close covering 08-07 — expect 2026-08-10** (FRED daily series run ~1–2
business days behind).

| Branch | Threshold | If it fires |
|---|---|---|
| **A — full growth-scare** | `ΔDGS2` ≤ **−0.15** AND `ΔHY OAS` ≥ **+0.15** | **FIN loses the mechanism · ENRG loses it · INDU loses cyclical support — and UTIL UW / RE UW are wrong-footed by a duration bid.** Rips FOR the UWs: NEE −5.1/−14.8 · SO −4.6/−4.2 · DUK −3.3/−4.8 · D −6.1/+2.8 · PLD −3.8/−7.4 · WELL −0.6/+5.9 · AMT +1.5/−7.5 (RS20/RS60 vs SPY) |
| **A′ — PARTIAL** | exactly ONE leg clears its own tail: `ΔDGS2` ≤ −0.12 **xor** `ΔHY OAS` ≥ +0.14 | **The firing leg is named and the verdict is graded partial** |
| **B — with us** | `ΔDGS2` > **−0.05** AND `ΔHY OAS` < **+0.08** | **`S51` branch A's *"NIM thesis intact"* reading becomes usable without its own caveat firing** |
| **C** | anything else | No conclusion changes |

**Thresholds measured, like-for-like, on a 2-session horizon**: `DGS2` n=613, sd 0.0742, **≤ −0.15 fires in
2.12%**, p05 −0.12 · `hy_oas` n=645, sd 0.1050, **≥ +0.15 fires in 4.34%**, p95 +0.14. ⚠ **A is a sub-1%
conjunction and is pre-declared as such — which is why A′ exists.**
⚠ **HY OAS has NOT printed since the payroll data** ⇒ which branch is live is **`unknown` (C3), not
benign.** **It is the single most informative number the desk is missing tonight.**

## 3 · Binaries still ahead — what is armed and what deliberately is not

| When | Event | Owner | Ticket? |
|---|---|---|---|
| **tonight, 16:00 ET** | **`S62` settles** — `(median RS20 {EMR,ETN,AME,PWR}) − (XLU RS20)`, at **+13.045** | S62 | ⛔ **No ticket. `D206`: branch A needs an 18.96pp one-session relative move in XLU against a ±0.5% straddle ⇒ arithmetically unreachable. Tonight's near-certain branch-B print is NOT confirmation the bracket earned**, and **S62's basket contains ZERO defence names**, so it cannot adjudicate the electricals-vs-defence question either way |
| **today, pre-market (already printed)** | **VST · PPL · EMA · AQN · OKLO** `[nasdaq 08-06 pre-market list]` · **TTWO** | — | ⛔ **No ticket — they have already printed.** ⚠ **The calendar carried only VST, and with no BMO/AMC field.** XLU is one of S62's two legs and **TTWO printed in EA's gaming node** |
| **2026-08-09** | **BRK-B Q2** | — | ⚠ **No ticket, but flagged: it lands INSIDE `S65`'s window (settles 08-11)** ⇒ **S65's scorer must not read a BRK-B earnings gap as breadth** |
| **2026-08-10** | `S51` · `S54` settle | S51 / S54 | ⛔ Already bracketed |
| **2026-08-11** | `S5` · `S55` · `S56` · `S58` · `S60` · **`S65`** settle | those rows | ⛔ Already bracketed |
| **2026-08-12 08:30 ET** | ★ **July CPI** `[bls✓]` | **S63 · S26 · S41 · S57 · S13 · S24 · S42 · S59 · S61** | ⛔ **No new ticket — every transmission channel is already owned** (real rate, credit, duration composite, materials). A standalone row was declined on 08-02 for the same reason and the reason still holds |
| **2026-08-13 08:30 ET** | **July PPI** `[bls✓]` | — | ⛔ **DROPPED with an L3 reason**: this repo has **no wired producer-margin pass-through observable** for MATR/INDU, and PPI's settle date sits **inside `S63`'s and `S64`'s existing windows** ⇒ whatever it moves is already captured. **Bracket spent elsewhere** |
| **2026-08-13** | `S64` · `S67` · `S68` · `S69` settle | those rows | ⛔ Already bracketed |
| **undated** | Iran *"Strait of Hormuz open"* statement | **S8 · S52 · S55** | ⛔ **Fully owned.** ⚠ **`S8` is on its 6th consecutive un-scoreable carry and needs a human `VOID` or re-registration (P5)** |
| **today ~15:30 ET** | **CFTC COT publication** — *not in the calendar; added by hand* | — | ⚠ **No ticket, but it is the one instrument refresh this run needs**: the file has been **byte-identical stale for SIX reads**, so **no positioning percentile was citable today, Copper's 96th included.** **DRIFT re-checks if it reaches 15:30 ET** |

## 4 · Epicenter-starter — **not triggered**

✅ **No rank≤2 cycle GAP**, so no tape-independent core-starter is required this run.
⚠⚠ **But the ✅ is measured on an instrument that cannot see 8.67pp of the book**: **TSM ($417.51 of the
$2,562 rank-1 epicenter total = 16.3%)** and **LNG ($525)** sit outside `us_top300`. **Ex-TSM the rank-1
epicenter still clears the floor at ~19.7% vs 12.0%, so the verdict survives — the 11.6pp margin
overstates the measurable part by about a third.** **9th consecutive run; the universe change is
human-gated.**
🚨 **And two registry defects mean a floor could not bind even if set**: **`cycle_exposure.py` computes
`gap = (cyc["rank"] <= 2) and (…)`, so a rank-3 floor is INERT by construction (`D189-a`, verified at
source)**, and **`SMH` — an ETF — sits inside rank-1's `epicenter` member list**, dormant only because it
is not held (`D189-d`). ⚠ **11 of the desk's 27 greens are in NO cycle at all** — EMR · AME · TRI · PH ·
BA · MET · SHOP · PLTR · DIS · NUE · STLD (+BKR) — **and EMR and AME are two of the four legs of the
bracket settling tonight.**

## 5 · What a human should look at first

1. **`S8`** — a 6th un-scoreable carry on the event that has driven the tape for a week. **`VOID` it or
   re-register it.**
2. **`data/us_universe/us_top300.csv` is 23 days stale and still lists a DELISTED security (EA).** The
   sweep's freshness guard **fired and was not read**, and it tests **stale market caps** rather than
   **constituent liveness** — so it cannot catch this class. **A rebuild plus a liveness assertion.**
3. **`D207`** (this file §0) — one line in `action_bracket.py` to compare `time_et` to the run clock, plus
   a BMO/AMC field on `[EARNINGS]` entries.
4. **`D187`** — `drift_watch.py` is still unrunnable remotely for a 2nd run. **Verified at source: the
   client's `DB_READ_CMDS` holds 9 entries including `drift`; the server's allow-list holds the same 8
   minus `drift`.** ⇒ **this is a DEPLOYMENT LAG (a `git pull` + API restart on the server PC), not a
   code-design fault** — a materially cheaper fix than the 08-06 characterisation implied.
5. **`handoff/` now reads 1,043+ KB against a 250 KB budget** — 5th run naming it, and after the D165
   truncation it is a **safety** item. **`handoff_compact.py` is non-destructive and nobody runs it.**

*Analytical/scheduling artifact — zero buy/sell advice. No order is sent by this desk.*
