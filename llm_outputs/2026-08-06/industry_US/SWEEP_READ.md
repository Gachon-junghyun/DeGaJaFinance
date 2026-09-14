# SWEEP_READ — industry_US · 2026-08-06 · **asof 2026-08-05 settled**

> The numbers live in `SECTOR_FLOW_US.json`, `US_LIVE_SHORTLIST.json`, `CYCLE_EXPOSURE.json`.
> This file holds only what those cannot say. No sector-ranking table and no per-name table is
> reprinted here (the 2026-07-21 measurement: 100% of tickers / 97% of numbers were restatement).

## 0 · Universe headline — three numbers

**n = 300 · Energy wflow +0.230 (rank 3) vs Financials +0.317 (rank 1) · 🟢 28 / 🔴 74.**

---

## 1 · ⚠⚠ D74 fired mid-stage, was QUANTIFIED, and the contamination changed the RANKING

**HANDOVER §0 pre-committed that this run would cross 09:30 ET and that SWEEP must re-check and
report which side of the open its cache was built on. It crossed at 09:30 and the first sweep
returned `asof 2026-08-06`.**

**Contamination, measured `[own calc on the untrimmed cache, n=300]`**: the 08-06 bar carries a
**median 2.61%** of the prior full session's volume (mean 3.90%, p90 8.20%) — a **six-minute** bar.
Cache trimmed to the 08-05 settled close; sweep re-run; `asof 2026-08-05`.

**What the six-minute bar did to the output — this is the finding, not the incident:**

| | contaminated | **trimmed (used)** |
|---|---|---|
| **#1 sector by wflow** | **Energy** +0.316 | **Financials** +0.317 |
| Information Technology **eqflow** | **−0.201** | **+0.001** — a **0.202 swing and a sign flip** on the breadth axis of the board's largest sector (n=56) |
| IT red count | 23 | **17** |
| Energy red count | 1 | **5** |
| wflow **sign flips** | — | **four sectors**: Materials (−0.048 → +0.071) · Real Estate (−0.042 → +0.022) · Consumer Staples (+0.084 → −0.013) · and Energy/Financials swapping rank 1 |
| 🟢 total | 20 | **28** |

⇒ **A bar carrying 2.6% of a session's volume reversed the sign of four sectors' mega-cap flow and
inverted the board's top rank.** This is **M171 replicated with a cleaner measurement** and it is the
strongest version of the D126 experiment the desk has run: **the price input barely moved and the
verdict moved everywhere.**

### 🚨 1a · And it wrote itself into the baseline — M171's exact failure mode, caught and reversed

The contaminated run **stored its snapshot in `llm_outputs/sector_flow/history.json` under a
`2026-08-06` key** (verified: NVDA 0.636 there vs **0.595** on the settled bar). **`history.json` is
the baseline every future `new_green` diffs against**, so tomorrow's ignition set would have been
diffed against a six-minute bar.

**Action taken**: backed up to `history.json.contaminated_0806.bak`, **the `2026-08-06` key deleted**.
The `2026-08-05` key holds the trimmed values and is correct. ⚠ **The re-run did NOT self-heal** — it
wrote under its own `asof` (08-05) and left the contaminated key orphaned. **That is a code defect,
not an operator error: a re-run cannot clean up after a prior run of the same day.** Registered as a
dig (ID at writeback). ★ Precedent: `history.json.contaminated.bak` from 2026-07-28 — **third
occurrence.**

---

## 2 · ★★★ The green tag decomposed — the interim D161 rule executed, and it inverts today's headline

> HANDOVER §9 made this binding: *no stage cites a 🟢 tag without decomposing which axis lit it.*
> This is the first US run to actually run the decomposition. **It should have been run every run.**

**Of 28 greens: 18 lit by the VOLUME path (`vol_surge` ≥ 1.2) · 13 by the VELOCITY path · 3 by both
· and 10 by VELOCITY ONLY, with `vol_surge` BELOW 1.2.**

**The velocity-only ten, with their `vol_surge`:**
**XOM 0.85 · CVX 0.99 · JPM 0.72 · BAC 0.74 · WFC 0.83 · BRK-B 0.85 · MA 1.03 · NVDA 0.92 ·
AVGO 0.77 · CSCO 0.89.**

★★★ **Read that list against the sector ranking and the sweep's headline reverses:**
- **Financials is rank 1 with 5 greens — and JPM · BAC · WFC · BRK-B · MA are ALL velocity-only.**
  ⇒ **the "breadth-led Financials ignition" is a NEWS-COUNT ignition, not a money ignition.**
- **Energy's only two greens are XOM and CVX — both velocity-only, both with `vol_surge` under 1.0.**
  ⇒ **the sector MACRO carries at OW− has zero volume-confirmed ignitions.**

⚠⚠ **And the coverage is asymmetric by construction: `velocity` is populated on only 51 of 300
names.** A green on a velocity-covered name and a green on one of the other 249 **are not the same
object**, because only the first can be lit without volume. **M25 measured the opposite state (vel
`None` on all 300); the axis has since come partly online and 10 of 28 greens now exist only because
of it.** This is not a bug being reported — it is a **grading instrument whose meaning changed under
the desk without the desk re-reading it.**

⚠ **W1 guard, stated**: this does **not** import the KR `vol_surge` sign result. It decomposes the
tag, which is what the interim rule asks for. The US IC ledger reads `vol_surge` **+0.0267, t +1.36,
`구분 불가`** — **no sign, either way.**

### 2a · The C9/M55 mechanism, reproduced on the US board at n = 80

**80 of 300 names carry OBV 매집 ∧ RS20 vs SPY > 0 and are NOT green.** The gate that blocks them is
`vol_surge` — the same arithmetic C9 documents for KR and M25/M38 for the US. **Carried, not
resolved** (a behavioural change to a live shared module needs a human, D37).

---

## 3 · Cross-checks against the MACRO transmission matrix — where the money agrees and where it does not

| MACRO row | Money says | Verdict |
|---|---|---|
| **Energy OW−** | wflow **+0.230 (rank 3)** but **eqflow −0.055** and **5 reds of 16** | ⚠⚠ **CONTRADICTS the breadth half.** Mega-cap-narrow with negative breadth, and **both greens are velocity-only (§2)**. ★ The refiners the OW actually rests on — **MPC · VLO · PSX** — are all **🟡, all OBV 매집 except PSX (중립), all RS60 +13.7 to +21.1**. **The money is in the refining leg and the TAG is on the integrated leg.** Precisely the 2026-07-2x pattern where a 🟢-filter artifact hid the refiners |
| **Financials OW−** | **rank 1 on both axes** (wflow +0.317, eqflow **+0.190**), 5 greens, and **5 of 18 new-🟢 are banks** (JPM, BAC, WFC, BRK-B, PRU) | ⚠ **CONFIRMS on the surface and DISSOLVES on decomposition.** Four of those five are velocity-only. ⚠ **M173 also binds: BRK-B is 13.94% of sector cap.** ⇒ **the confirmation is weaker than the rank suggests**, and P13‴'s flattening points the other way |
| **IT Neutral** | wflow **+0.246**, eqflow **+0.001**, **7 greens vs 17 reds** | ★★ **CONFIRMS the neutrality-as-work reading.** The widest internal split on the board: **SHOP +1.00 · PLTR +0.97 · MSFT +0.95 · ANET +0.78** against **CDNS −0.77 · IBM −0.85 · CIEN −0.86.** ⇒ **C8's shape, measured: one label, opposite verdicts** |
| **Utilities UW** | wflow **−0.398**, eqflow **−0.392**, **0 greens, 12 reds of 15** | ★★ **CONFIRMS unanimously** — worst on every axis, the only sector where wflow and eqflow agree deeply negative. ⚠ Note **VST −0.315, SO −0.338, DUK −0.367 all 🔴 with `vol_surge` 1.24–1.39** — **the distribution IS volume-confirmed**, which the ignition side of the board is not |
| **Materials UW−** | wflow **+0.071** but **eqflow +0.167 (3rd-best on the board)** with **0 greens, breadth 0.00** | ⚠⚠ **CONTRADICTS, and it is S36/S57's exact divergence still running.** S36 scored **FIRED-B** on price (XLB exc5 −3.79) **while the flow breadth is positive** — ⇒ **the two axes have now disagreed for three straight weeks and the bracket that closed did not settle it.** ★ **NUE +0.672 / STLD +0.600 (both OBV 매집, RS20 +17.9 / +13.0)** are the carriers; **steel, not chemicals** |
| **Health Care N** | **3 greens, ALL volume-confirmed** (AMGN 1.27 · BMY 1.55 · IDXX 1.43), all OBV 매집, all RS20 > 0 | ★★★ **C7's registered resolver FIRED — see §5** |
| **Comm Services UW** | wflow +0.084, eqflow +0.094, **0 greens** (down from 1 on the contaminated read), 2 reds | **CONFIRMS**, and P28's GOOGL event is not yet in the flow numbers |
| **Staples UW** | **the only sector with wflow AND eqflow both negative outside UTIL/RE** (−0.013 / −0.085) — **but delta +0.236, the highest on the board** | ⚠ **Ambiguous.** Negative levels, strongest positive *change*. **Diagnosed, not called**: one sector's delta on one day is n≈1 |
| **Industrials OW−** | wflow +0.126, **eqflow +0.179 > wflow** ⇒ **breadth-led, not mega-cap-led** | ★ **CONFIRMS, and it is the only OW− where breadth exceeds concentration.** ⚠⚠ **Three of the four names in S62's basket — EMR (+0.92) · ETN (+0.88) · AME (+0.78) — sit in the shortlist's top ten, and S62 settles TOMORROW** |
| **Real Estate UW** | wflow +0.022 / eqflow +0.038, 1 green (**IRM**, ⚡crowded-short) | **Neutral-to-mild-positive flow against a UW.** ⚠ **R7 binds: do not re-argue RE as a duration expression** |

---

## 4 · Shortlist composition — the absences, each diagnosed

The 15-name shortlist (mcap ≥ $10B, 🟢 only, top-15 by flow) contains **IT ×4 · Industrials ×4 ·
Health Care ×2 · Financials ×2 · Discretionary ×2 · Real Estate ×1**.

**Five sectors produced ZERO names, and they are not the same kind of zero:**

| Absent sector | Diagnosis |
|---|---|
| **Energy** | ⚠ **NOT a true absence — a FLOW-RANK artifact.** Energy has 2 greens (XOM +0.569, CVX +0.580) and they simply rank below the 15th-place cutoff (PRU +0.69). **The absence is a top-N truncation, not evidence.** ★ And the more informative fact is one level down: **the refiners are 🟡, so even lifting the cutoff would not surface them** — the same 🟢-filter artifact the desk measured in July |
| **Utilities** | ✅ **A TRUE absence and the strongest signal in this section.** 0 greens of 15, wflow and eqflow both ≈ −0.4, 12 reds. **Nothing was filtered out because nothing was there** |
| **Materials** | ⚠ **Filter artifact with a live contradiction behind it.** 0 greens **but eqflow +0.167**, and **NUE/STLD carry OBV 매집 with RS20 +17.9/+13.0 while tagged 🟡.** ⇒ **exactly the §2a n=80 population.** The shortlist cannot see this sector by construction |
| **Consumer Staples** | ✅ **A true absence** — 0 greens, negative on both axes. But see §3's delta caveat |
| **Comm Services** | ✅ **A true absence**, 0 greens of 13, and **the sector's largest name fell 4.03% on a leadership exodus the day this bar settled (P28)** |

**Short-pressure verdicts (US has no investor-type feed — FINRA z proxy only):**
✅ clean-rise (low short / covering): **AME · GRMN · AMGN** · ⚡ crowded-short (turn-conditional
squeeze fuel, **not** a buy read): **IRM** · everything else △ normal.
⚠ **GRMN is on this list for a third run while carrying the desk's "#1 flow, no thesis anywhere"
coverage gap AND two rejections.** ★ **PLTR ranks #2 on flow (+0.967) with news velocity 2.65 — and
`Palantir` was independently the blind-spot pass's top name-level emergent term (269 mentions).**
**Two unrelated instruments surfaced the same name on the same day, and the desk has no thesis on
it.** Handed to EVENT_ALPHA.

---

## 5 · ★★★ C7 was registered "re-check 2026-08-06". The date arrived and its own resolver fired.

**C7's registered resolving observable** (from `STANDING_VIEW.md §6`, and reproduced verbatim in the
JNJ rejection row's `revives_if`): *"a green with `vol_surge` ≥ 1.2 (volume path), **or** any green
from outside the HLTH top-6 by cap."*

**Measured on the settled bar: BOTH legs.** Health Care's three greens are **AMGN (cap-rank 6,
`vol_surge` 1.27) · BMY (cap-rank 16, 1.55) · IDXX (cap-rank 27, 1.43)** — all three clear the volume
path, and **two are outside the top-6 by cap**. All three also carry OBV 매집 and RS20 vs SPY of
+7.6 / +7.3 / +2.0.

⇒ **The JNJ rejection row is resolved `revived`** (both legs, on fresh evidence, original evidence
un-laundered). ⇒ **C7's "money without narrative" reading is answered on the axis C7 itself
nominated**: the HLTH flow is **not** a top-6 litigation artifact — it has **mid-cap breadth with
volume confirmation.**

⚠⚠ **Scope, stated precisely (C4)**: what resolved is **whether the flow is an artifact**, not
whether Health Care deserves a tilt. **JNJ itself still reads 🟡중립, `vol_surge` 0.88, RS20 −5.5** —
the name that carried the original contradiction is *not* the name that resolved it. **ROTATION owns
whether this changes the HLTH row; SWEEP only reports that the resolver fired.**
★ **This is the one clean instance this run of the rule "resolve a carried contradiction with a
measurement, or leave it alone."**

---

## 6 · Cycle exposure — ✅ no GAP, and one registry observation worth a stage's attention

`cycle_exposure --json` → **no top-rank cycle GAP.** Rank-1 **AI-compute** epicenter **19.97%**
(need ≥12%, held AVGO/NVDA/TSM); rank-2 **Energy / oil-refining** epicenter **12.15%** (need ≥8%,
held **MPC, PSX**). Rank-3 rearmament has no threshold set (⚪ n/a).

⚠⚠ **The registry's rank-2 cycle is now literally named *"Hormuz + Russia crack"* — the registry
already encodes MACRO §0-b's object, and the desk's reports have not been.** Recorded.

🚨 **And a reconciliation item for ROTATION/BET**: the held Energy epicenter is **MPC and PSX**.
**XOM is not in the book.** **S31 — scored `AMBIGUOUS` this morning — is written throughout as a
bracket on *"the only Energy name the book holds"*, and that has not been true since the XLE exit
window.** The bracket's *observable* is unaffected (a frozen number is a frozen number); its *stated
meaning* is stale. **Named, not silently corrected** — same treatment R39 got.

⚠ Book context only, and it is **not** a US sizing input: total ≈ **$10,855**, invested **$7,591**.
**No sizing, no buy/sell language (P4).**
