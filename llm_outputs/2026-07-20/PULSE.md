# PULSE — live diagnostic · 2026-07-20 (Mon)

> L1·PULSE. Same-day signals only; the research desks' lagging inputs (news ≤60d, EOD marks) are
> **not** used for this verdict. One question: **broad crash / sector event / idiosyncratic / noise?**

## ⚠ asof caveat (stated first, per the stage rule)
- Run **2026-07-20 pre-open KST**. The last completed US session is **Friday 07-17** — the market-context
  line and all USD prices are that close (or a futures print), **not live**.
- `fts --days 1 --scope foreign` returned articles dated **07-16 and 07-19**, i.e. the foreign feed has
  **no 07-20 content yet** (weekend + Monday pre-open). **A fresh same-day catalyst could not be sourced.**
  The catalyst below is therefore the *most recent* one, not today's. Flagged rather than papered over.
- These prices **may lag a real-time screen.** Do not treat as live quotes.

## §1 Price sweep — every book position
**시장맥락: S&P500 743.3 (−1.0%) · Nasdaq 695.3 (−1.5%) · VIX 18.8 (+12.2%)**

| TKR | Price | 1d% | 5d% | stop% | Theme |
|---|---|---|---|---|---|
| 009150 삼성전기 | 1,314,000 | **+2.9** | **−12.0** | +4.3 | IT-substrate/MLCC |
| VST | 155.44 | +1.9 | −1.6 | +2.9 | AI-power-IPP |
| LNG | 262.60 | +1.4 | +0.5 | +16.7 | energy-fuel/AI-power |
| RTX | 193.51 | −0.4 | −0.9 | +6.3 | defense-missile |
| KMI | 32.30 | −0.7 | −0.3 | +6.2 | energy-fuel/AI-power |
| AVGO | 370.83 | −1.0 | **−7.5** | +3.0 | AI-compute-EPICENTER |
| MA | 543.60 | −1.4 | +3.9 | — | payments/FIN |
| NVDA | 202.81 | −2.2 | +0.0 | +5.1 | AI-compute-EPICENTER |
| **TSM** | 398.37 | **−2.8** | **−8.8** | **+0.9** | AI-compute-EPICENTER |

- **당일 −3% 이하: 없음.** ⛔ **스탑 히트: 없음.** TSM is closest to its stop at **+0.9%**.
- **VIX 18.8 (+12.2%)** — the one genuinely elevated reading. Compare the FRED print of **16.73 (07-16)**:
  broad hedging demand has risen, this is **not** a calm tape.

## §2 Same-day catalyst
`fts search TSMC semiconductor selloff --scope foreign --days 1` → 287 hits, newest dated 07-19:
> **"Markets sink on global selloff in chip stocks"** — *"A global selloff in chip stocks dragged markets down Thursday"* [semafor, 07-16]
> **"Lattice Semiconductor, AMD, and Qualcomm Shares Are Falling"** — *"…wide selloff that began with **ASML** the day before. **TSMC** shares fell…"* [yahoo_finance, 07-16]

Velocity (`--days 1 --count`, foreign): `volatility` **295** · `AI capex` **89** · `selloff` **48**.

**Read:** the chip drawdown started ~**07-15/16 with ASML** and has run a week — TSM **−8.8% / 5d**,
AVGO **−7.5% / 5d**. This is **not a new shock today**; it is day ~4 of a running semis de-rating,
and it lines up with the AI-capex-doubt cluster the 07-20 KR MACRO logged (Oracle 52wk low + credit cut
toward junk, IBM −25%, Apple memory fix, 키미 K3, Gemini delayed).

## §3 ★ VERDICT: **SECTOR EVENT (AI-compute), not a broad crash — with a rising-hedging caveat**

The red is **concentrated by theme, not spread across the book**:
- **AI-compute-EPICENTER is the whole drawdown** — TSM −2.8, NVDA −2.2, AVGO −1.0 (and −8.8 / +0.0 / −7.5 on 5d).
- **Every non-AI-compute theme is flat-to-up** — LNG +1.4, VST +1.9, MA −1.4, RTX −0.4, KMI −0.7.
- **No book name is ≤ −3% and no stop is hit.** By the stage's own rule this is *not* a broad crash.

**Caveat that stops this being a clean "hold" read:** **VIX +12.2% to 18.8** is a real move, and
**VST +1.9% sits inside the same AI-power thesis that MACRO's M-03 kill-switch just fired on.** VST is
up today while its narrative axis is under attack — a divergence to watch, not to act on here.

**★ Resolves an open item from today's `real_alpha_kr` run on 009150.** That agent left today's move
unresolved across three conflicting sources (pulse +2.6% / KIS 1,345,000 / news 시간외 **−7.75%**).
PULSE now reads **삼성전기 +2.9% at 1,314,000** — **the −7.75% 시간외 print was not today's move.**
The name is **UP** today, bouncing off a −12.0% five-day drawdown. The forensic verdict
(REAL-but-PRICED, catalysts land 2027+) is unaffected; only the intraday confusion is cleared.

**Not fabricating a crash:** the book is **not** 나락. Two names green, no stop hit, no name ≤ −3%.

## ✅ EXIT CHECK
- [x] `pulse` run — all 9 book names' 1d/5d/stop-distance + market context (VIX/SPY/Nasdaq) read.
- [x] Same-day news pulled for the worst movers (`--days 1 --scope foreign`); top hit body-read
      (ASML-led chip selloff). ⚠ **Feed had no 07-20 content — stated, not assumed away.**
- [x] Verdict stated — **sector event (AI-compute)** — with the asof-time caveat up front.
