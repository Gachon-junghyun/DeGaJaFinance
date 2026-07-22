# L2 · indicators — regime & flow indicators (orchestration)

> Called by L1s. Assembles regime/flow indicators to confirm or refute direction. Composes the below.

## Calls (all `python -X utf8`)
- Macro regime — `python -X utf8 -m module_macro_us --series fed_funds,us_10y,us_2y,real_10y,core_cpi,cpi,unemployment,dxy,vix,m2,hy_oas,ig_oas,breakeven_10y,nfci --days 120 --json`
  ⚠ always `--json` (markdown view has KR headers; each series carries `label_en`); cite `[FRED]`;
  monthly series (CPI/M2) lag ~1 month — flag staleness (e.g. a VIX print that pre-dates an overnight shock).
  *KR desk: no FRED module → cross-read the same-day US MACRO_REPORT §A.*
- US positioning — `python -X utf8 scripts/us_flow.py --cot` (CFTC COT: net-spec, weekly Δ, 1yr %ile —
  ≥80 crowded-long / ≤20 crowded-short; Tue-close +3–4d lag ⇒ context, not trigger)
  and `python -X utf8 scripts/us_flow.py <TICKERS…>` (FINRA daily short-vol z per name;
  z≥+1.5 spike / z≤−1.5 exit — divergence vs narrative = the order-flow tell).
- Name/sector flow tag — `python -X utf8 -m module_flow <tickers…> --bench SPY|^KS11 --json`
  (🟢/🟡/🔴; KR adds `--names` per-investor actuals; `--positioning` is slow — finalists only).
  ⚠ **KR tickers need the `.KS` suffix here.** A bare 6-digit code returns empty rows **without
  erroring** — measured, and read as "no flow signal" on a day flow had actually reversed.
- News velocity — `python -X utf8 -m module_news_data fts search "<theme>" --count` (corroborant, not primary).

## ★ Three axes added 2026-07-22 — use them, they close measured blind spots

**1. Credit & liquidity** (`hy_oas · ig_oas · breakeven_10y · nfci` + `rrp · fed_assets · sofr` on demand).
The catalog had **zero credit spreads** until now. **HY OAS is the single best risk-regime read** and
it is *daily* — fresher than CPI, which lags a month.
⚠ **Measured failure this closed**: on 2026-07-21 the US desk assembled a "credit surprise stack"
(NY Fed application rates at a 10-year high, student-loan defaults, a Dimon quote) **entirely from
narrative** — while HY OAS sat at **2.69%, within 6bp of its 365-day low (2.63%) and 16bp tighter
over 90 days**. The credit market said no stress and nothing in the toolkit could say so.
**Rule**: any proposition about credit stress, risk-off, or financial conditions **cites HY OAS or
NFCI**, or states that it is narrative-only. Also pair `real_10y` with `breakeven_10y` — quoting a
real yield without its breakeven hides whether the move was growth or inflation.

**2. Estimate momentum** (`module_fundamentals_us <TKR>` → §추정치 모멘텀).
`eps_trend` (current / 7 / 30 / 60 / 90 days ago) + `eps_revisions` (up:down counts).
We had valuation as a **snapshot** only; the direction of the denominator was invisible.
⚠ **Why this matters more than it looks**: the lab's only A-grade verified signal is **momentum**
(mom5 LR 0.880, p=0.001, 39,290 obs) and we applied it **only to price**. Earnings-revision momentum
is the same family. *Measured*: MU's +1y EPS estimate went **100.53 → 150.91 in 90 days (+50.1%)**
with **30 upgrades : 0 downgrades** — i.e. the denominator of that "cheap 6.31× forward P/E" had been
racing upward. **Read it next to the valuation table, never alone** (lens L2, peak-margin trap).

**3. Implied move** (`module_flow <TKR> --positioning` → `예상변동 ±x%(만기, D±n)`).
Nearest-expiry ATM straddle = what the market has **already priced** for the move.
⚠ Skew and P/C say *how much people pay for protection*; they do **not** say *how far it is expected
to travel*. **PREMORTEM/SCENARIOS thresholds should come from here rather than being chosen by hand**
— the current `handoff/SCENARIOS.md` brackets were hand-set, which this replaces.
*Measured 2026-07-22*: GOOGL **±7.1%** into that night's print · MU ±4.5% · AMD ±3.6%.
⚠ The straddle is the **total** move to expiry, not the event's isolated contribution — read `D±n`
with it; a 0DTE chain is nearly pure event premium but its OI ratios are noisy.

## ⚠ Grade the signal before you weight it (carry rule D6 of `handoff/RESEARCH.md`)

The tools here print every axis at the same visual weight. **They are not equally measured.**

| Grade | Axis | Use |
|---|---|---|
| **A** | RS20 / RS60 momentum · residual clusters · concave impact · 5-day impact decay · fat tails | Can carry a proposition |
| **B** | KR foreign/institution actuals (`--names`, KIS) · short balance as *liquidity supply* | Confirmation layer — never a standalone system (foreign flow is **non-stationary**: first 18 months IC ≈ 0) |
| **C** | **OBV · 매집/분산 · the 🟢/🟡/🔴 tag that is built from them** | **Corroborant only.** r≈0.49 vs real flow (per name 0.005–0.67) and **no leading power (t=1.00)** once real flow is known |
| **REJECTED** | COT contrarian · VIX contrarian · "short building = bearish" | Do not re-buy — all indistinguishable or reversed |

**Rules that follow from the table**
- A C-grade signal **may never carry a proposition alone**, and **may never override** a disagreeing
  A/B signal. Where KIS actuals exist, they override OBV — never the reverse.
- ⚠ **The 🟢/🟡/🔴 tag is itself partly C-grade.** In `module_flow/_synthesize.py` the conviction gate
  is `obv_state == "매집" OR news_velocity ≥ 1.2` — so on the **US** path (no investor feed) OBV alone
  can unlock 🟢가속 with nothing to override it. Treat a US 🟢 whose only conviction source is OBV as
  **🟡 with a stated disagreement**, and say so in the report. (Fixing the gate itself is open dig
  **D11** — a scoring change needs human approval.)
- **Substitution when tempted to write "OBV accumulating"**: (1) what does RS20/RS60 say (A)?
  (2) for KR, what do KIS actuals say (B)? (3) is the move date-clustered (S1)? Report OBV as
  agreement or disagreement with those, not as the finding.

## ⚠ Reading investor flow — two traps (carry rules A1/B6 of `handoff/RESEARCH.md`)

**1. Check for a second listing venue before reading domestic flow as directional.**
While arbitrage between venues is blocked, a cross-listed name's home-market foreign-flow number is
**mechanically distorted**. Measured: SK hynix (000660) listed ADRs on Nasdaq 2026-07-10 ($26.5B);
the ADR ran to **+50%** over the ordinary line (~25% later) because two-way conversion was closed,
so foreign "selling" in Seoul was substantially venue migration — and US money bought Seoul shares
through EWY instead ($1.1B in a single day). A sibling name with **no** ADR (005930) carried the
clean read.
→ Before citing foreign net-buying as directional, check for an ADR/GDR/dual listing and a
blocked-conversion window. If one exists, mark the flow read **SUSPENDED with the date it clears**
and record it in `handoff/STANDING_VIEW.md`. **Do not retroactively clean the contaminated stretch**
once conversion opens — the old window stays unreadable.

**2. When data looks late, check a second provider before theorizing about the first.**
Measured: KIS, Naver, and KRX (pykrx) returned **identical** investor figures through the same date
and all three stopped there — proving the missing day was unpublished, not one provider lagging.
One source alone cannot distinguish those two cases.

## Output
Regime verdict + per-sector/name flow direction with crowding context.
**The calling L1 uses it to support/refute propositions — never as a standalone buy signal.**
