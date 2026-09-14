# SECTOR_DEEP_HLTH — Health Care — industry_US — 2026-08-06 (Thu) · ROTATING → **FULL FRESH MAP**

> **asof 2026-08-05 settled.** ⚠⚠ **D74**: the market is open at this clock; every price, RS, OBV,
> `vol_surge` and delta below is read off the **08-05 settle**. The 08-06 partial bar appears exactly
> twice in this file, both times labelled as carrying **no verdict**.
> Flow numbers `[SECTOR_FLOW_US.json, asof 2026-08-05, D74-trimmed]`. Revision books
> `[module_fundamentals_us, pulled 2026-08-06]`. Filings `[module_disclosure_us / EDGAR]`.
> Themes `[module_news_data theme-age --scope foreign]`. Short `[us_flow.py, FINRA Reg SHO 08-05]`.
> Last deep-dived 2026-07-30; that file was read for continuity and is **cited only where this run
> re-measured the same object** — no number is inherited (**A5**).
> **Analysis only. No sizing, no buy/sell, no order language (P4).**

---

## 0 · The one-line answer

🚨 **No — and the failure is worse than "it rests on BMY and IDXX", because the promotion's two stated
carriers are a tautology and an arithmetic accident, and the sector's greens contributed 6.8% of the
number it was promoted on.**

Three measurements, each independent, each fatal to a different leg of ROTATION §2:

**(i) "The ONLY sector whose entire green set is volume-lit" is FALSE, and it is also a tautology.**
`velocity` is populated on **exactly the top 51 names of the 300-name universe by market cap** —
ranks 1…51, nothing else `[own calc on SECTOR_FLOW_US.json, n=300, zero exceptions]`. HLTH's three
greens sit at **universe cap-rank AMGN 66 · BMY 111 · IDXX 254**. **The velocity path did not exist
for any of them.** Every green outside the top-51 is volume-lit *by construction*: of the 28 board
greens, **0 of the 15 non-velocity-covered greens has `vol_surge` < 1.2**, and **all 10 sub-1.2
greens are velocity-covered names**. And the exclusivity claim fails on the run's own file: **four
sectors have an all-volume-lit green set — Consumer Discretionary (3), Health Care (3), Industrials
(5), Real Estate (1)** — with **Industrials carrying more of them than Health Care** `[own calc]`.
⇒ The property ROTATION promoted on is **"HLTH's greens are not mega-caps"**, restated.

**(ii) The Δ +0.328 that ranked #1 of 11 is 48.2% one non-green name.** Cap-weighted delta
decomposition of the 32 names reproduces the reported +0.328 exactly. **LLY alone contributes
+0.1584 = 48.2% of it**, on a 19.4% cap weight — and LLY is **🟡중립, OBV 중립, RS20 −7.1 vs SPY**.
**The top-5 by cap contribute 83.5%. The three greens contribute 6.8%** `[own calc]`.
⇒ **The delta and the greens are two disjoint facts that ROTATION §2 printed in one cell.**

**(iii) The whole thing is the Q2 earnings calendar.** **16 of 32 HLTH names reported Q2 within 7
calendar days of the 08-05 settle** `[yfinance earnings_dates + module_disclosure_us 8-K Item 2.02 +
foreign-feed dating]`, and **those 16 produced 78.2% of the sector's cap-weighted delta on 56.0% of
its cap**. Six reported on **08-04 alone** (MRK · AMGN · GILD · PFE · IDXX · WAT); **LLY reported
08-05, the settle bar itself.** Decisively: **HLTH has exactly 6 names with `vol_surge` ≥ 1.2, and
all 6 reported earnings within the last 7 calendar days — 6/6, no exceptions.** Their OBV states:
**BMY 매집 · AMGN 매집 · IDXX 매집 · LLY 중립 · ALNY 분산 · CI 분산.**
⇒ **In Health Care this week `vol_surge` is not an accumulation instrument, it is an earnings-date
detector — and half of what it detects is people leaving.**

**Does OW− stand on BMY and IDXX alone?** It stands on **BMY alone**, and BMY is a single-name
beat-and-raise dated **2026-07-30**, not a sector state. **IDXX cannot carry it**: revision book
**CQ +0.0% · NQ −0.0% · CY +1.0% · NY +0.7% per 90d**, **RS60 vs SPY exactly 0.0**, price **−24.8%
below its 52-week high**, forward P/E **34.76**, PEG **3.64** `[module_fundamentals_us]`. Under **C4**
IDXX is **INDISTINGUISHABLE**, not supporting evidence.

★ And the desk's own registered anti-signal fired on the promotion day — see **§7**.

---

## 1 · C7's four "against the flow" legs, re-measured on today's data

C7 (`handoff/STANDING_VIEW.md §6`) was carried **INDISTINGUISHABLE (C4)** with a dated re-check of
**2026-08-06**. Its resolving observable — *"a green with `vol_surge` ≥ 1.2 (the volume path), OR any
green from outside the HLTH top-6 by cap"* — **fired on both legs**. Below is what each of C7's four
original "against" legs reads today.

| C7 leg (as registered) | then | **today, measured** | verdict on the leg |
|---|---|---|---|
| **Δ −0.102**, one of only two negative deltas on the board | −0.102 | **+0.328, #1 of 11** `[JSON sector_rotation]` | ⚠ **REVERSED IN SIGN — and the reversal is 48.2% LLY, a non-green name on its earnings day, 83.5% top-5-by-cap, 6.8% the greens** `[own calc]`. **The leg flips; what it flips into is not what ROTATION read** |
| **Revision books flat** (+0.5% to +1.4% CY EPS/90d vs the refiners' +51–71%) | flat | **DISPERSED, not flat — and inverted against the flow.** CY EPS/90d: **BMY +10.3% · UNH +7.9% · MRK −0.1% · JNJ +0.4% · AMGN +0.1% · IDXX +1.0% · TMO +1.0%** `[module_fundamentals_us]` | ⚠⚠ **The leg is REFUTED as stated and REPLACED by a worse finding: the two strongest books in the sector sit on 🟡 names (BMY is the exception), and the single best book — UNH — sits in the sector's WORST flow node** (§2) |
| **Only 3 of 7 sub-nodes carry it** | 3/7 | **exactly 3 of 7 again**: Life-science tools **+0.266** · Large-cap pharma **+0.232** · Med-tech **+0.104** positive; Biotech **−0.051** · Distributors **−0.064** · Providers **−0.270** · Managed care **−0.273** negative `[own calc, cap-weighted within node]` | ✅ **UNCHANGED — the leg SURVIVES verbatim across 5 runs.** ★ This is the only one of the four legs that reads the same number on a second independent date, which under **S1** makes it the sector's **only n=2 fact** |
| **No health-care thread among 145 alive threads** — money without narrative | none | **REFUTED.** `GLP-1` **🟡ACCELERATING, 652 items/90d, 24.3/day over 7d, 2.15x acceleration** · `obesity drug` **🟡ACCELERATING, 147 items, 7.3/day, 3.17x** · `patent cliff` **🟡ACCELERATING, 141, 2.77x** · `Medicare Advantage` **🟡ACCELERATING, 123, 3.27x** · `animal health` **🟡ACCELERATING, 92, 3.3x** `[theme-age --scope foreign]` | ⚠ **REFUTED as a fact, INVERTED as an argument.** The narrative exists and accelerates — **but its named subject is LLY** (*"Eli Lilly Stock Jumps Over 5% as Mounjaro Sales Surge 91%"*, `yahoo_finance` 2026-08-05, full body), and **LLY is 🟡중립, OBV 중립, RS20 −7.1**. **Narrative without the tag, exactly as often as money without the narrative** |

**⚠⚠ Scope discipline — what the resolver DID and did NOT resolve (C4).**

**RESOLVED (and only this):** the C7-era hypothesis that HLTH's flow was a **top-6-by-cap artifact**
is dead. Two of three greens sit at cap-rank 16 and 27, both with `vol_surge` ≥ 1.4 and OBV 매집.
**The flow is not confined to the mega-cap block.** The `revives_if` on the JNJ rejection row is
satisfied on its own terms, on fresh evidence, with the original evidence un-laundered.

**NOT RESOLVED, and none of it may be inherited as resolved:**
1. **Whether Health Care deserves a tilt.** The observable was a test of *artifact vs not-artifact*.
   It says nothing about direction, and this file finds the flow is a **calendar** artifact of a
   different kind than the one C7 tested (§0-iii).
2. **Whether the greens are one object.** They are in three different sub-nodes with three different
   end markets (§2), and the resolver never asked.
3. **Whether the "top-6" definition is fixed.** The 07-30 deep flagged that *"its 'top-6' was never
   defined"* and required a human. **That defect is untouched.** This run used **cap ranking within
   the sector**; under the desk's *named block* (LLY·JNJ·ABBV·MRK·TMO·UNH) AMGN is also outside, so
   the leg fires either way — but the definition is still unfixed, and it is still a human call.
4. ★★★ **Whether the observable measures anything persistent.** On **07-30** the same count read
   **2 (TMO, HCA)**. Today it reads **2 (BMY, IDXX)**. **Zero name overlap.** On today's bar the two
   07-30 resolvers read **TMO 🟡 +0.567** and **HCA 🟡 −0.270**. ⇒ **The observable fires at a stable
   count with a completely different name set each time it is read. That is the signature of session
   noise, not of a standing state.** Under **S1** this is the strongest reason to refuse to promote
   on it.

⇒ **C7's own status**: the *artifact* half is closed; the *belief-vs-money* half is **re-opened on a
new axis** — flow and the revision book now run in **opposite directions at node level** (§2).
**Recommended carry: C7 CLOSED-AND-SUPERSEDED, with the successor contradiction registered on the
node-level inversion.** That is a writeback decision, not this file's to take.

---

## 2 · Sub-node decomposition — ⚠ **W5: the label is the wrong unit, by 7.2×**

All 32 names, GICS sub-industry mapped to the desk's seven nodes. `wflow` = cap-weighted within node,
`eqflow` = equal-weighted, `delta` = cap-weighted day/day `[own calc on SECTOR_FLOW_US.json]`.

| node | n | cap share | **wflow** | eqflow | Δ | 🟢/🔴 | 매집/분산 | med RS20 vs SPY | names |
|---|---|---|---|---|---|---|---|---|---|
| **Life-science tools** | 4 | 7.3% | **+0.266** | +0.279 | +0.144 | 0/0 | 2/1 | **+5.8** | WAT TMO A DHR |
| **Large-cap pharma** | 5 | **40.9%** | +0.232 | **+0.415** | **+0.525** | 1/0 | 4/0 | −1.4 | **BMY** PFE MRK LLY JNJ |
| **Med-tech & devices** | 8 | 14.2% | +0.104 | +0.125 | +0.072 | 1/1 | 5/1 | +1.8 | **IDXX** BDX ABT SYK MDT BSX ISRG EW |
| **Biotech** | 6 | 18.5% | **−0.051** | −0.022 | +0.315 | 1/3 | 2/3 | −6.0 | **AMGN** REGN ABBV ALNY VRTX GILD |
| **Distributors** | 3 | 3.8% | −0.064 | −0.132 | +0.225 | 0/0 | **0/1** | −0.8 | MCK CAH COR |
| **Providers / facilities** | 1 | 1.6% | −0.270 | −0.270 | +0.302 | 0/0 | 0/0 | −3.5 | HCA |
| **Managed care** | 5 | 13.7% | **−0.273** | **−0.328** | +0.155 | 0/1 | **0/1** | **−9.2** | UNH CVS HUM CI ELV |

**Dispersion (B5), stated against the sector's own move:**
**wflow spread = +0.266 … −0.273 = 0.539, against a sector wflow of +0.075 ⇒ 7.2×.**
**eqflow spread = +0.415 … −0.328 = 0.743, against a sector eqflow of +0.055 ⇒ 13.5×.**

⇒ **W5 answered: this is not a sector signal.** The between-node spread is seven to thirteen times
the thing being labelled. Two nodes (managed care, providers) are moving *against* the sector at a
magnitude larger than the sector's entire move.

**And the three greens are three different objects, in three different nodes, on three different
dates:**

| green | node | end market | **the dated event that produced the `vol_surge`** |
|---|---|---|---|
| **BMY** 1.55 | Large-cap pharma | oncology / hematology / immunology, US wholesale channel | **8-K Item 2.02 + 7.01, filed 2026-07-30**; guidance lifted `[EDGAR 0000014272-26-000018]`. ⚠ **`new_green` = FALSE — BMY was already green; it is not part of this run's ignition** |
| **AMGN** 1.27 | Biotech | biologics, biosimilars, rare disease | **8-K Item 2.02, filed 2026-08-04** (results 08-03). Sales +9–10%, adj EPS **$6.29 vs $5.62 est**, FY26 guide **raised to $22.30–23.50 from $21.70–23.10**; stock **+4.57%** `[EDGAR 0000318154-26-000124; Reuters via yahoo_finance, full body, 2026-08-04]` |
| **IDXX** 1.43 | GICS "Health Care Equipment" — ⚠ **mis-filed: this is companion-animal veterinary diagnostics** | vet clinics, water & food-safety testing | **8-K Item 2.02 + 9.01, filed 2026-08-04.** FY26 revenue raised to **$4.70–4.745B**, EPS to **$14.69–14.94**, organic **8.5–9.7%** `[EDGAR 0001104659-26-090033; MarketBeat call transcript via yahoo_finance, full body]` |

**Shared end market between AMGN, BMY and IDXX: none.** A biologics franchise facing LOE, an oncology
franchise facing LOE, and a veterinary point-of-care instrument business whose demand driver is
**US clinical visits, which IDXX itself guided to decline ~1.5% in H2** `[IDXX Q2 call, full body]`.
The only thing they share is **a Q2 print inside a six-session window** — which 16 of the 32 names
share.

★ **The node-level inversion, which is the real finding and is new since C7 was written:**
- **highest-flow node** (life-science tools, wflow +0.266, **0 greens**) — TMO book **CY +1.0%/90d,
  NQ −1.1%, NQ 30d 5↑/11↓** `[module_fundamentals_us]`. **Flow leads, book does not.**
- **lowest-flow node** (managed care, wflow −0.273, medRS20 −9.2) — **UNH book is the best in the
  sector: CY +7.9%/90d, NY +8.1%, 30d CY 21↑/1↓, NY 20↑/0↓, 7d CY 24↑/0↓ and NY 24↑/0↓.**
  ⚠ **C2, both halves**: the same book has **NQ 7d 3↑/18↓** and the CQ 90-day base reads **0.00**
  (a data gap ⇒ CQ/NQ 90d change is **unmeasurable, C3 `unknown`**). **Annual lines strongly up,
  next-quarter sharply down.** Stated as the split it is, not netted.
⇒ **Within Health Care, flow and the revision book are currently anti-correlated at node level.**
**C4: which axis is right here is INDISTINGUISHABLE on this repo's instruments.**

**The C9/M55 population inside this sector — n = 7.** Names with **OBV 매집 ∧ RS20 vs SPY > 0** that
are **not** green, blocked solely by `vol_surge`:
**ABT** (+0.464, RS20 +7.8, RS60 +21.0, d21-60 **+13.2**, `vol_surge` **0.65**) · **TMO** (+0.567,
+10.0, +19.9, **+9.9**, 0.82) · **WAT** (+0.664, +5.4, +8.3, +2.9, 1.19) · **REGN** (+0.656, +12.7,
+3.1, −9.6, 0.98) · **BDX** (+0.600, +10.1, +9.8, −0.3, 0.88) · **PFE** (+0.556, +4.0, −3.9, −7.9,
1.10) · **MDT** (+0.230, +1.6, +8.6, +7.0, 0.72) `[own calc]`.
★ **STANDING_VIEW §6's C7 row carries a standing instruction — *"Watch ABT, which led the sector on
07-24"*.** **Followed**: ABT is in this blocked population with the sector's best d21-60 among
accumulating names (+13.2) and `vol_surge` **0.65** — the lowest of the seven. **It cannot become
green on this instrument no matter what its money does.**

---

## 3 · Players ∪ thematic — the full 32, with primary-filing IR anchors

**Full flow table** `[SECTOR_FLOW_US.json, asof 2026-08-05]`, cap-ranked; `d21-60` = RS60 − RS20 vs
SPY (**M149/M150**); `E` = calendar days from last Q2 print to the 08-05 settle.

| # | tk | node | cap $B | flow | tag | OBV | RS20 | RS60 | d21-60 | v_srg | Δ | E |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | LLY | pharma | 980 | +0.156 | 🟡 | 중립 | **−7.1** | +19.0 | **+26.1** | 1.27 | **+0.817** | **d-0** |
| 2 | JNJ | pharma | 550 | +0.091 | 🟡 | 매집 | −5.5 | +12.0 | +17.5 | 0.88 | +0.199 | d-21 |
| 3 | ABBV | biotech | 382 | −0.201 | 🔴 | 분산 | −5.9 | +17.8 | +23.7 | 0.96 | +0.457 | d-5 |
| 4 | UNH | managed care | 364 | −0.192 | 🟡 | 중립 | −6.3 | +4.3 | +10.6 | 0.69 | +0.382 | d-20 |
| 5 | MRK | pharma | 281 | +0.328 | 🟡 | 매집 | −1.4 | +10.9 | +12.3 | 0.92 | +0.575 | **d-1** |
| 6 | **AMGN** | biotech | 182 | **+0.708** | **🟢** | 매집 | **+7.6** | +18.6 | **+11.0** | **1.27** | +0.586 | **d-1** |
| 7 | TMO | tools | 173 | +0.567 | 🟡 | 매집 | +10.0 | +19.9 | +9.9 | 0.82 | +0.052 | d-13 |
| 8 | ABT | med-tech | 154 | +0.464 | 🟡 | 매집 | +7.8 | +21.0 | +13.2 | 0.65 | +0.010 | d-20 |
| 9 | GILD | biotech | 154 | −0.497 | 🔴 | 분산 | −6.3 | −4.0 | +2.3 | 1.04 | −0.094 | **d-1** |
| 10 | ISRG | med-tech | 144 | −0.492 | 🟡 | 중립 | −12.9 | −21.0 | −8.1 | 0.98 | +0.136 | d-20 |
| 11 | PFE | pharma | 144 | +0.556 | 🟡 | 매집 | +4.0 | −3.9 | −7.9 | 1.10 | +0.100 | **d-1** |
| 12 | CVS | managed care | 125 | −0.335 | 🟡 | 중립 | −8.4 | +5.1 | +13.5 | 1.14 | **−0.379** | d-91 |
| 13 | DHR | tools | 125 | −0.210 | 🟡 | 분산 | +1.4 | +12.3 | +10.9 | 0.87 | +0.182 | d-15 |
| 14 | SYK | med-tech | 118 | +0.306 | 🟡 | 매집 | −0.2 | +13.7 | +13.9 | 1.13 | +0.229 | d-6 |
| 15 | VRTX | biotech | 115 | −0.462 | 🟡 | 중립 | −6.0 | +8.4 | +14.4 | 0.88 | +0.266 | d-2 |
| 16 | **BMY** | pharma | 110 | **+0.943** | **🟢** | 매집 | **+7.3** | +8.9 | +1.6 | **1.55** | −0.013 | d-6 |
| 17 | MDT | med-tech | 102 | +0.230 | 🟡 | 매집 | +1.6 | +8.6 | +7.0 | 0.72 | +0.057 | d-63 |
| 18 | MCK | distributors | 88 | +0.234 | 🟡 | 중립 | +3.9 | +14.8 | +10.9 | 0.99 | +0.216 | d-90 |
| 19 | ELV | managed care | 84 | −0.429 | 🟡 | 중립 | −9.2 | −0.9 | +8.3 | 0.67 | +0.180 | d-21 |
| 20 | HCA | providers | 83 | −0.270 | 🟡 | 중립 | −3.5 | −10.2 | −6.7 | 0.72 | +0.302 | d-12 |
| 21 | CI | managed care | 74 | −0.350 | 🔴 | **분산** | −9.9 | −10.5 | −0.6 | **1.57** | +0.113 | d-6 |
| 22 | BSX | med-tech | 67 | +0.033 | 🟡 | 중립 | +3.3 | −15.8 | −19.1 | 0.94 | −0.274 | d-7 |
| 23 | REGN | biotech | 64 | +0.656 | 🟡 | 매집 | +12.7 | +3.1 | −9.6 | 0.98 | −0.050 | d-6 |
| 24 | COR | distributors | 53 | −0.317 | 🟡 | 분산 | −0.8 | +17.1 | +17.9 | 1.09 | +0.169 | d-91 |
| 25 | CAH | distributors | 52 | −0.312 | 🟡 | 중립 | −2.4 | +25.9 | **+28.3** | 0.91 | +0.298 | d-97 |
| 26 | EW | med-tech | 50 | −0.800 | 🔴 | 분산 | −8.3 | +6.9 | +15.2 | 0.76 | −0.039 | d-13 |
| 27 | **IDXX** | vet dx | 44 | **+0.656** | **🟢** | 매집 | **+2.0** | **0.0** | −2.0 | **1.43** | +0.156 | **d-1** |
| 28 | HUM | managed care | 43 | −0.335 | 🟡 | 중립 | −11.5 | +28.0 | **+39.5** | 1.12 | −0.184 | d-7 |
| 29 | BDX | med-tech | 40 | +0.600 | 🟡 | 매집 | +10.1 | +9.8 | −0.3 | 0.88 | +0.288 | d-90 |
| 30 | ALNY | biotech | 37 | −0.333 | 🔴 | **분산** | **−32.6** | −26.8 | +5.8 | **2.74** | 0.000 | d-6 |
| 31 | A | tools | 36 | +0.097 | 🟡 | 중립 | +6.1 | +17.7 | +11.6 | 0.69 | +0.266 | d-70 |
| 32 | WAT | tools | 35 | +0.664 | 🟡 | 매집 | +5.4 | +8.3 | +2.9 | 1.19 | +0.336 | **d-1** |

**Sector-wide (C1, benchmark inline):** median **RS20 −1.1** / median **RS60 +8.8** vs SPY ·
**RS20 > 0 on 14 of 32, RS60 > 0 on 23 of 32** · OBV **매집 13 / 중립 12 / 분산 7** `[own calc]`.
**XLV vs SPY, settled closes** `[yfinance, auto_adjust, last bar 08-05]`: **60d +10.28pp · 20d
−2.13pp · 10d −0.03pp · 5d −6.78pp.** Sub-ETFs 5d excess: **XPH −3.61 · XBI −2.08 · IHI −4.74.**
⇒ **The sector's outperformance is entirely a days-21-60 object that is rolling over in days 1-20,
and the roll-over is broad (all three sub-ETFs negative over 5d).**

**Momentum geometry, and where the leadership actually sits.** The five largest d21-60 readings are
**HUM +39.5 · CAH +28.3 · LLY +26.1 · ABBV +23.7 · COR +17.9** — **every one of them has RS20 < 0
today.** The three greens read **AMGN +11.0 · BMY +1.6 · IDXX −2.0.** ⇒ **the base was built by names
that are now underperforming, and the greens are the late, shallow part of it.** **D154 guard**: the
"EXHAUSTED" label is unavailable where RS60 ≤ 0, which here excludes only ISRG, GILD, HCA, BSX, PFE.

**IR anchors, primary filings only** `[module_disclosure_us / EDGAR, 90-day window]`:

| name | primary anchor | what it says, and what it does not |
|---|---|---|
| **AMGN** | **8-K Item 2.02, 2026-08-04** (`0000318154-26-000124`) · 10-Q ×1 · **22 Form 4/13G** · **0 M&A/contract filings** | FY26 EPS guide **raised** $21.70–23.10 → **$22.30–23.50**; six growth drivers **+26% y/y ≈ 70% of product sales**; **Repatha +37% to $953M**, **Evenity +38% to $714M**, **Uplizna +90% to $335M** — against **Prolia −32% to $759M on patent expiry**, **Tavneos under an FDA-proposed withdrawal (April) with an EMA revocation recommendation**, **Repatha now competing with Merck's oral Lipfendra**, and **AMG 513 obesity candidate discontinued**. ★ **MariTide Phase-3 read-outs are guided to "next year" — there is no 2026 catalyst in the obesity leg** `[Reuters full body 2026-08-04]` |
| **BMY** | **8-K Item 2.02 + 7.01, 2026-07-30** (`0000014272-26-000018`) · 10-K 2026-02-11 | Guidance lifted. **10-K, verbatim: "our three largest wholesalers … account for approximately 87% of total gross sales of U.S. products for the year ended December 31, 2025."** Single reportable segment. ⚠ **The Barron's body frames the same print as *"declining revenue in its legacy drug portfolio … offset by new products"*** — a mix story, not a demand story `[Barrons via yahoo_finance, 2026-07-30]` |
| **IDXX** | **8-K Item 2.02 + 9.01, 2026-08-04** (`0001104659-26-090033`) | FY26 revenue **$4.70–4.745B** (midpoint = **+$20M operational, −$15M FX**), EPS **$14.69–14.94**, CAG recurring **+9.5–10.7%** of which **~4% is net price**. **5,265 premium instruments placed, 1,602 inVue Dx**; installed base **+11% y/y**; op margin **35% reported**, gross margin **64% (+120bp)**. ⚠⚠ **The company guides US clinical visits to decline ~1.5% in H2** — **volume down, price up ~4%** |
| **JNJ** | no 8-K Item 2.02 in the flow window; last print **2026-07-15** | see **§6** |
| **UNH** | last print **2026-07-16**, next **2026-10-27** | the sector's best revision book sits behind the sector's worst flow node |

**Short pressure** `[us_flow.py, FINRA Reg SHO daily, 2026-08-05]`: **AMGN 46.1% vs base 61.0%,
z −1.59, 5v5 +4.3▲ ⇒ 🟢 short-volume collapse / covering** · **BMY 48.3%, z −0.34, −5.3▼ 🟡 normal** ·
**IDXX 38.6%, z +0.07, +12.5▲ 🟡 normal** · **JNJ 58.8%, z +0.45 🟡 normal** · **LLY 43.5%, z +0.04 🟡**.
⚠ **AMGN's 🟢 is a covering read on an earnings-beat session — mechanically expected, and it is a
US short-*volume* proxy, not an investor-type feed. It does not distinguish covering from
initiation-then-covering (C3).**

**Thematic overlay** `[theme-age --scope foreign, 90d]`: `GLP-1` 🟡ACCELERATING 652/2.15x ·
`obesity drug` 🟡ACCEL 147/3.17x · `patent cliff` 🟡ACCEL 141/2.77x · `Medicare Advantage` 🟡ACCEL
123/3.27x · `animal health` 🟡ACCEL 92/3.3x · `medical cost` ⚪ECHO 125 · `drug pricing` ⚪ECHO 79 ·
`most favored nation` ⚪ECHO 27 · `biotech M&A` ⚪ECHO 7 · **`pharma tariff` 🔴FADING, 11 items,
7d average 0.0/day**.
★ **The two policy themes that would justify a *sector* de-rating (drug pricing, MFN) are ECHO and
the tariff thread is dead; the two accelerating themes (GLP-1, patent cliff) are *name-selective* —
one names LLY, the other names ABBV/BMY/AMGN as victims.** ⇒ **the narrative field is
name-discriminating, which is the opposite of a sector call.**

---

## 4 · Value chain — 7 nodes, with the **BINDING CONSTRAINT** marked

```
① discovery / biotech  →  ② tools & reagents  →  ③ CDMO & manufacture  →  ④ IP owner (pharma)
        AMGN REGN VRTX          TMO DHR A WAT        [unmeasurable here]        LLY JNJ MRK BMY PFE
   →  ⑤ devices & dx  →  ⑥ distribution  →  ⑦ 🚧 PAYER (PBM / MCO / CMS)  →  provider → patient
        ABT SYK MDT BSX EW        MCK COR CAH             UNH ELV CI HUM CVS        HCA
        IDXX (vet — ⚠ different payer entirely: the pet owner, out of pocket)
```

**🚧 BINDING CONSTRAINT = node ⑦, the PAYER.** Marked here on evidence, and marked with the reason
**strong demand is not a bottleneck**: the demand side of this chain has never been the scarce input —
volumes and approvals are abundant, **reimbursement is the rationed resource.** The measurements:

- **Node ⑦ is the sector's worst flow node** (wflow **−0.273**, eqflow **−0.328**, medRS20 **−9.2**,
  **0 매집 across all five names**, one 🔴 with **volume-confirmed distribution — CI `vol_surge`
  1.57, OBV 분산**) **while holding the sector's best revision book (UNH CY +7.9%/90d, 7d 24↑/0↓).**
  A node whose earnings estimates rise while its tape distributes is a node being **re-rated**, not
  a node under demand pressure. **⚠ C2, both halves: UNH's NQ 7d is 3↑/18↓.**
- **`Medicare Advantage` is 🟡ACCELERATING (123 items, 3.27x)** while **`medical cost` is ⚪ECHO** —
  the *policy* thread on this node is live and the *cost-trend* thread is not. **C3: which of the two
  is driving the payer tape is `unknown` on this repo's instruments.**
- **The chain is gated backwards, not forwards.** Every node upstream of ⑦ is flow-positive or
  near-zero; only ⑦ (and the provider node that bills it) is deeply negative. **The money is
  positioned as if the constraint binds at the payer.**

**A6 — name the node's customers and check their disclosed spend or give print dates:**

| node | its customers | disclosed spend / print date |
|---|---|---|
| **④ pharma (BMY, the green)** | **wholesalers** | ✅ **measured, primary**: **BMY 10-K FY2025 — "our three largest wholesalers … approximately 87% of total gross sales of U.S. products."** Those three are **MCK · COR · CAH** ⇒ **node ⑥.** ⚠⚠ **Node ⑥'s flow: wflow −0.064, eqflow −0.132, 0 greens, 0 매집, 1 분산, medRS20 −0.8.** **The customer taking 87% of the green name's US gross sales is not confirming** |
| **② tools (the highest-flow node, 0 greens)** | **pharma & biotech R&D budgets** | ⚠ **the 07-30 deep set this exact test with a date — "MRK's 10-Q lands 2026-08-04." It landed. MRK printed 08-04 and its book reads CY −0.1%/90d, 7d 1↑/2↓, 30d 1↑/2↓** `[module_fundamentals_us]`. **The customer's disclosed trajectory did not turn up.** ★ This is the one A6 test on this chain that was **pre-dated and then actually scored** |
| **⑤ dx — IDXX specifically** | **veterinary clinics**; end payer = **the pet owner, out of pocket** | ✅ **self-disclosed, primary**: **US clinical visits guided ~−1.5% in H2**, offset by **~4% net price** `[IDXX Q2 call full body, 8-K 08-04]`. ⇒ **volume contracting, revenue held by price. `vet clinic` theme is 🟡ACCEL but on 11 items total — D6 low grade, n≈1 outlet class** |
| **① biotech — AMGN** | payers + providers | ⚠ **the disclosed spend is going the wrong way on two named products: Prolia −32% (patent expiry) and Tavneos under FDA-proposed withdrawal.** **0 M&A / contract filings in 90 days** |
| **③ CDMO / manufacture** | — | 🚫 **NOT MEASURED. No name in `us_top300` isolates this node** (the pure-plays are non-US or below the universe). **C3: `unknown`, not "small"** |

⚠ **B2 applied where it bites.** Forward multiples in this sector are **not** valuations here because
**no margin percentile is available in this repo (D15 — a valuation factor has never been measured)**.
Read only with estimate momentum: **MRK fwd P/E 13.34 vs trailing 103.29** — the gap is a charge
artifact and **the CY 2.76 vs NY 9.65 estimate step is itself an artifact of that charge, so MRK's
CY line is not comparable to its peers' (C3, flagged rather than used)**. **IDXX fwd 34.76 / PEG 3.64
against a flat book** and **BMY fwd 9.71 against a +10.3%/90d book** are the two ends. **C5: none of
these multiples vetoes anything, and no measured axis in this file was overruled by one.**

---

## 5 · Chain-hop candidates, each with a flow cross-check

`chain-hop "GLP-1" obesity --days 7 --scope foreign` `[module_news_data]`. Only **body-proximate,
title-absent** rows are candidates by construction; flow cross-check from the same settled file.

| candidate | prox / body | flow cross-check `[08-05 settle]` | read |
|---|---|---|---|
| **MMM** | 6 / 16 | +0.517 🟡 **OBV 매집**, RS20 **+14.4**, RS60 **+22.7**, `vol_surge` **0.73**, Δ −0.061 | ★ **The only textbook chain-hop shape in the list: accumulating, already-leading, volume-quiet, tag-blocked.** ⚠ **But the linkage is spurious — the example article is an Eli Lilly / Novo comparison piece; MMM is co-mentioned, not exposed.** ⇒ **REJECT the linkage, KEEP the flow observation. C4: the name is interesting on flow and unexplained on narrative** |
| **ABBV** | 4 / 8 | −0.201 **🔴 분산**, RS20 −5.9, **RS60 +17.8, d21-60 +23.7**, Δ +0.457, reported **07-31** | ⚠ **Anti-confirming.** A deep base distributing into an earnings delta. **`patent cliff` 🟡ACCEL names this node.** **REJECT** |
| **MRK** | 3 / 9 | +0.328 🟡 **매집**, RS20 −1.4, RS60 +10.9, `vol_surge` 0.92, Δ **+0.575**, printed **08-04** | ⚠ **Split**: OBV agrees, book does not (**CY −0.1%/90d, 7d 1↑/2↓**). ★ Merck's **oral Lipfendra** is the named competitive threat to AMGN's Repatha — **this is the one intra-sector linkage the body text actually establishes**, and it runs **against** the green. **KEEP as a contradiction, not a candidate** |
| **CAH · MCK** | 4/5 · 3/4 | CAH −0.312 🟡 중립, RS60 **+25.9**, d21-60 **+28.3** · MCK +0.234 🟡 중립, RS60 +14.8 | ⚠ **Both are node ⑥ — the customer node from §4 that is *not* confirming.** Deep 60-day bases, **zero accumulation between them.** **C4: INDISTINGUISHABLE** |
| **KO · CCEP · MDLZ · MCD** | 2–3 / 3–12 | KO +0.212 🟡 중립 · CCEP −0.028 🟡 중립 (`vol_surge` 1.26) · MDLZ +0.297 🟡 **매집** RS20 +2.0 · **MCD −0.417 🔴 분산, `vol_surge` 1.21** | The **GLP-1-eats-into-food-volume** leg. ⚠ **It is not one object: MDLZ accumulating, MCD volume-confirmed distributing.** The linkage article is a **WHO ultra-processed-food** piece, not a GLP-1 mechanism piece ⇒ **D6 low grade. C4** |
| **DIS · UBER · C · MS** | 2–5 / 5–12 | DIS +0.403 🟡, `vol_surge` **1.47**, Δ +0.532 · UBER −0.639 🔴 분산 · C −0.260 🟡 · MS +0.387 🟡 매집 | **Co-mention noise** — the example bodies are *"Earnings, PMI and Other Key Things to Watch this Week"* round-ups. **REJECT all four on source grade (D6)** |

**Named-in-title block (not chain-hop, reported for completeness):** **AMGN 6 title / 2 body** —
AMGN **is** inside the GLP-1 thread by name. ⚠ **But its own 8-K removes the 2026 catalyst: AMG 513
discontinued, MariTide Phase-3 read-outs guided to next year.** **JNJ 1 title / 8 body** — the
highest body-proximity in the sector with almost no title presence (see §6).

⇒ **Chain-hop yield this run: zero clean candidates.** The one structurally clean flow shape (MMM)
fails the exposure test; every name that passes the exposure test fails the flow test. **Reported as
a null result rather than padded.**

---

## 6 · The JNJ question — is JNJ a candidate, and on what evidence?

**Answer: NO — and the reason is that the row was *revived*, which restores it to `open`, not to
`supported`. C4 scope discipline applies to the revival exactly as it applies to the resolution.**

**What is true, measured today:**
- **JNJ's revision *breadth* is the best in the sector**: CY **30d 19↑/0↓, 7d 16↑/1↓**; NY 30d 15↑/3↓;
  CQ 30d 5↑/0↓ `[module_fundamentals_us]`. **Nineteen up, zero down over 30 days is the cleanest
  breadth number in this entire file.**
- **⚠ C2, the other half, and it is decisive**: the *levels* barely moved — **CY +0.4%/90d, NY +0.6%,
  CQ −1.5%.** ⇒ **This is consensus *converging*, not consensus *rising*.** Nineteen analysts moved
  toward the same number after the 07-15 print; the number itself is flat. **Breadth without
  magnitude is a post-earnings tightening, and it is not the same object as BMY's +10.3%/90d.**
- **The tape disagrees with the breadth**: **🟡중립, `vol_surge` 0.88, RS20 −5.5 vs SPY**, OBV **매집**,
  RS60 **+12.0**, **d21-60 +17.5** ⇒ **JNJ is the mirror image of AMGN.** AMGN = price-live /
  KPI-dead. **JNJ = KPI-breadth-live / price-dead.** ★ **Both cannot be evidence for the same sector
  verdict, and having both inside one label is the strongest single argument that the label is not
  the unit (W5).**
- **Short**: 58.8% short-volume, **the highest of the five names checked**, z +0.45, 5v5 **+4.3▲**
  `[FINRA Reg SHO 08-05]` — pressure building, not releasing.

**What is untouched, and stays untouched:** the original rejection basis — that HLTH's only green at
the time was a **velocity path at `vol_surge` 0.96**, and that the body identified the driver as a
**$5.5bn talc settlement**, i.e. **a litigation settlement, not accumulation**. **This run re-read
that finding and did not re-open it. It is not laundered by C7's resolver firing, because the
resolver fired on three *other* names.** The name that carried the contradiction is **not** the name
that resolved it — and there is therefore **no evidence path from the resolution to JNJ.**

⇒ **Status: the rejection row is correctly `revived` (the `revives_if` was met verbatim), and JNJ is
correctly NOT a candidate.** The distinction that must survive into the writeback:
**`revived` = eligible to be re-examined. It is not a finding about JNJ.** JNJ's own evidence today
is **INDISTINGUISHABLE (C4)** — a best-in-sector breadth number with no magnitude behind it, against
a tape underperforming SPY by 5.5pp over 20 days.
**Dated re-read:** JNJ's next print is not in this window; the usable observable is **CY EPS level
(not breadth) rising ≥ +1.5% by 2026-09-05** — that would convert convergence into revision.

---

## 7 · Track KPIs and anti-signals — all as dated observables

### 7a · 🚨 The desk's own registered anti-signal FIRED, on the promotion day

**`SECTOR_DEEP_HLTH.md` 2026-07-30 §6 registered, verbatim: *"Second anti-signal: XLV's 5-day excess
vs SPY turning negative while SPY rises ⇒ the outperformance was defensive rotation, not sector
demand — the reading that has been available for four runs and is still not excluded."***

**Measured on the 08-05 settle** `[yfinance, auto_adjust, settled closes only]`:
**SPY 729.46 → 769.79 = +5.53%. XLV 166.24 → 164.16 = −1.25%. Excess = −6.78pp.**
✅ **BOTH conditions met: SPY rose, and XLV's 5-day excess is negative.** Corroborated across the
whole sector: **XPH −3.61 · XBI −2.08 · IHI −4.74** over the same window.

⇒ **The condition the desk itself pre-registered as meaning "this was defensive rotation, not sector
demand" fired on the exact bar the desk used to promote the sector.** It was registered five runs
ago, on a dated file, and **nothing in this run's SWEEP, ROTATION or PREMORTEM read it.**
★ **This is the single most important line in this file.** It is not a new argument invented to
attack the promote — it is **the desk's own frozen falsifier, scored on schedule.**

### 7b · Track KPIs (frozen definitions, carried from 07-30 so the next read is n=3)

| # | KPI | 07-30 | **08-06** | next read |
|---|---|---|---|---|
| **K1** | count of 🟢 from **outside the HLTH top-6 by cap** | **2** (TMO, HCA) | **2** (BMY, IDXX) — ⚠ **zero name overlap; both 07-30 resolvers are now 🟡** | every run. ⚠ **The definitional defect flagged on 07-30 is still unfixed — a human call** |
| **K2** ★new | **name-persistence** of K1: how many of the previous read's names are still 🟢 | — | **0 of 2** | **08-07.** ⇒ K1 measures session noise until K2 ≥ 1 on two consecutive reads |
| **K3** ★new | count of HLTH names with `vol_surge` ≥ 1.2 that did **NOT** report earnings in the prior 7 calendar days | — | **0 of 6** | **08-12** (first clean post-earnings window). ⇒ until K3 > 0, HLTH `vol_surge` is an earnings-date detector |
| **K4** | node-level flow **sign spread** (best minus worst wflow) vs sector wflow | — | **0.539 vs 0.075 = 7.2×** | every run. **Below 2× ⇒ the sector label becomes a defensible unit** |
| **K5** | **BMY** CY EPS estimate level (the promotion's only surviving carrier) | — | **6.95** (was 6.34 seven days ago, +9.6% in 7d) | weekly. ⚠ **NY 6.54 < CY 6.95 and NY breadth 7d 4↑/8↓, 30d 6↑/10↓ — the out-year is being cut while the near book rises** |
| **K6** | **AMGN** 30d CY revision breadth | 3↑/12↓ | **3↑/12↓ (confirmed independently)**; 7d **1↑/1↓** | **08-13.** See 7c-A |

### 7c · Anti-signals — dated observables that would say the promotion was WRONG

**A. 🚨 The primary one, and it is already partly scored.**
**Observable: AMGN's CY consensus fails to rise above the mid-point of its own raised FY26 guidance
by 2026-08-20.** AMGN raised FY26 EPS guidance to **$22.30–23.50 on 2026-08-04** with a **$6.29 vs
$5.62 beat**; consensus CY sits at **22.35 — 5 cents above the raised FLOOR, at the very bottom of
the range — and moved +0.04% in the 7 days spanning the print, on 7d breadth 1↑/1↓.**
⇒ **A beat-and-raise that produced no upward revision in seven days is the anti-signal.** If CY has
not cleared **22.90** (the guidance mid-point) by **08-20**, the "price-live / KPI-dead" reading is
confirmed and AMGN's 🟢 was an event print.
⚠ **Correction owed to the pre-mortem (both directions, C2):** Lens 3's 90-day window **predates the
08-04 raise**, so "worst book in the sample" is measured across a period that ends at a guidance
increase — the label is **backward-looking**. But the 7-day slice that *contains* the print reads
**1↑/1↓**, so the cuts did not continue **and the raise did not land either**. **C4: whether analysts
disbelieve the raise (Prolia −32%, Tavneos withdrawal, Repatha vs Lipfendra) or simply have not
updated is `unknown` (C3) at this clock.** Price corroborates the sceptical read: **$402.65 against a
consensus mean target of $357.03 = −11.3%, with Hold 17 / Sell 2 / Strong-Sell 1 against Buy 10 /
Strong-Buy 4.**

**B. XLV 5-day excess vs SPY stays negative on the 2026-08-07 settle while SPY is flat-to-up.**
Already fired once (7a). **A second consecutive negative read converts it from n≈1 (S1) to a
two-observation fact** and closes the "defensive rotation" alternative in favour of it.

**C. K3 = 0 again on 2026-08-12.** If, in the first week with no HLTH earnings prints, the sector has
**zero** names at `vol_surge` ≥ 1.2, then the entire 08-06 green set was calendar volume.
**This is the cleanest single test in this file** and it costs one week.

**D. IDXX's CY estimate fails to move by 2026-08-20** (currently **14.66**, unchanged for 60 days)
**after a raised revenue and EPS outlook filed 08-04.** Same shape as A, on a name whose guide was
raised **partly by a $20M operational improvement offset by a $15M FX headwind** — i.e. a **$5M net**
midpoint move on a **$4.7bn** revenue base. ⇒ **If a raise that small is what a 1.43 `vol_surge`
green is made of, the green is not about fundamentals.**

**E. The managed-care node's flow stays ≤ −0.20 through 2026-08-13 while UNH's CY estimate holds
≥ 19.50.** That combination sustains the node-level inversion (§2) and means **the sector's money and
the sector's earnings are pointing opposite** — under which no single sector verdict can be right.

**F. Falsifiers of THIS file (stated so it can be scored against, not just used):**
**F1.** If **K3 > 0 on 08-12** — HLTH holds volume-lit greens with no earnings in the window — then
the "calendar artifact" reading in §0-iii is wrong and the flow is a standing state.
**F2.** If **BMY's NY (2027) breadth turns net-up for two consecutive weeks**, the LOE overhang read
is wrong and BMY becomes a genuine two-sided carrier rather than a single print.
**F3.** If **XLV's 20-day excess vs SPY turns positive by 08-13** (today **−2.13pp**), the
"days-21-60 base rolling over" reading in §3 is wrong.

**Dated catalyst calendar (settled facts, no forecast):** **2026-08-07 NFP** · **2026-08-12 CPI** ·
**2026-08-13 PPI** · **AMGN next print 2026-11-04** · **BMY 2026-10-29** · **MRK 2026-10-29** ·
**TMO 2026-10-21** · **UNH 2026-10-27**. ⇒ ⚠⚠ **There is no company-level Health Care catalyst
between now and mid-October.** The Q2 season that produced this entire signal **ended on 08-05.**
**Whatever the flow is, it has no scheduled fuel for ten weeks.**

---

## 8 · Verdict on the promotion

**HLTH N → OW− is NOT SUPPORTED on the evidence this file could measure. It is not refuted into a UW
either — the correct state is the one the desk already had: N.**

**The promotion's two stated carriers, both dissolved:**
1. **"the ONLY sector whose entire green set is volume-lit"** — **false** (four sectors qualify;
   Industrials has more) **and vacuous** (velocity is populated on exactly the universe top-51 by cap;
   all three HLTH greens sit at ranks 66/111/254, so no other path existed). **The statement reduces
   to "HLTH's greens are mid-caps."**
2. **"Δ +0.328, #1 of 11"** — **48.2% LLY** (🟡, OBV 중립, RS20 −7.1, reporting on the settle bar),
   **83.5% top-5-by-cap**, **6.8% the greens**. **78.2% of it comes from the 16 of 32 names that
   printed Q2 in the prior 7 calendar days.**

**And the levels the promotion did not cite: HLTH is 7th of 11 on wflow (+0.075) and 6th of 11 on
eqflow (+0.055).** ⚠⚠ **The same S1 objection ROTATION §3 used to DECLINE Consumer Staples — *"a
rank-2 delta on top of two negative levels is not a verdict"* — applies here as *"a rank-1 delta on
top of rank-7 levels is not a verdict."* The declination was correct; not applying it to Health Care
is the inconsistency.** ★ And the pre-mortem's own procedural point stands unanswered: **Discretionary
out-levels HLTH on both axes (wflow +0.212 vs +0.075; eqflow +0.120 vs +0.055) and was given neither
a promote nor a slot.**

**What genuinely survives, and it is smaller than a sector verdict:**
- **BMY** is the only name in the sector with **both** halves live: **CY +10.3%/90d (+9.6pp in 7 days),
  NQ 30d 12↑/1↓** against **RS20 +7.3, OBV 매집, `vol_surge` 1.55.** ⚠ **With its own crack: the
  out-year is being cut (NY 6.54 < CY 6.95; 7d 4↑/8↓) and 87% of its US gross sales go through a
  three-name customer node that is flow-negative with zero accumulation.**
- **A blocked-by-instrument population of 7** (ABT · TMO · WAT · REGN · BDX · PFE · MDT) carrying
  **OBV 매집 ∧ RS20 > 0** that `vol_surge` gates out — including **ABT, which STANDING_VIEW §6
  explicitly instructed the desk to watch, at `vol_surge` 0.65.**
- **A node-level inversion** (best book in the worst-flow node, weakest book in the best-flow node)
  that is a **real, new, unmeasured-by-C7 contradiction** and is the right successor to C7.

**Recommended disposition of C7 (a writeback decision, stated for the owner, not taken here):**
**close the artifact half — the flow is not a top-6 concentration effect; supersede the
belief-vs-money half with the node-level inversion; and register K2/K3 so that the *next* firing of
C7's observable can be distinguished from noise, which today's firing cannot.**

⚠ **D74 discipline, restated at the close:** the 08-06 partial bar reads **XLV 163.20 / SPY 770.91**.
**It carries no verdict and was used nowhere above.**

---

## ✅ Coverage

flow ✅ (all 32 re-derived from the settled JSON; sector, node and name level) ·
adversarial task (1) ✅ (AMGN removal test run three independent ways) ·
C7 four legs ✅ (all four re-measured; 1 unchanged, 1 sign-reversed, 2 refuted) ·
scope discipline ✅ (resolved / not-resolved stated separately, C4) ·
sub-node decomposition ✅ (7 nodes, dispersion quantified against the sector's own move, B5) ·
players ✅ (32/32) · thematic ✅ (10 themes dated) · IR ✅ (3 primary 8-K Item 2.02 + 1 10-K
customer-concentration anchor, A6) · chain map ✅ (7 nodes, binding constraint marked with evidence) ·
chain-hop ✅ (**null result, reported as null**) · JNJ ✅ · anti-signals ✅ (6, all dated) ·
short ✅ (FINRA proxy, limits stated) · benchmark inline ✅ (SPY, C1)

**NOT measured, reported rather than guessed (C3):**
**③ CDMO/manufacture** — no `us_top300` name isolates it, `unknown` not "small" ·
**margin percentiles** for every multiple quoted — **D15, this repo has never measured a valuation
factor**, so **no multiple vetoed a measured axis (C5)** ·
**UNH's CQ/NQ 90-day revision change** — the 90-day base reads 0.00, a data gap ·
**MRK's CY EPS line** — distorted by a charge, not peer-comparable ·
**investor-type flow** — the US desk has no such feed; FINRA short-volume is a proxy only ·
**whether AMGN's analysts disbelieve the raise or have not yet updated** — indistinguishable at this
clock, and the 08-20 observable in §7c-A exists precisely to settle it.

**No position sizing and no buy/sell language appears anywhere in this file (P4).**
