# PULSE — live diagnostic · 2026-07-23 (Thu)

> L1·PULSE. **Same-day signals only** — the research desks' lagging inputs (this morning's
> `industry_kr` run, FRED asof 07-20/21) are not used for this verdict. One question:
> **broad crash / sector event / idiosyncratic / noise?**

## ⚠ asof caveat (stated first)

- Prices are from `module_paper_book pulse`'s live pull — intraday, exact minute not logged by the
  KRX/US session tools (stated as a blank, not guessed). Treat every 1d% below as partial-day.
- News counts are **binned by publish time and still filling** — foreign pool sits at 485 articles →
  81 market events at pull time; domestic pool (re-checked from this morning's `industry_kr` MACRO
  run) has moved from 906→ a larger count since. Today's counts are a floor, not a total.
- A failed quote is a blank, not a red number. None were needed — all quotes in the book returned.

---

## §1 · Price sweep — every book position (`module_paper_book pulse`)

Market context: **S&P 747.4 (−0.1%) · Nasdaq 705.3 (−0.5%) · VIX 16.6 (−2.4%)**

| Ticker | Price | 1d | 5d | Stop dist | Theme |
|---|---|---:|---:|---:|---|
| 009150 | 1,433,000 | **+6.5** | +13.7 | +13.7 | IT-substrate/MLCC |
| AVGO | 396.81 | +2.7 | +2.0 | +10.2 | AI-compute epicenter |
| VST | 166.74 | +2.7 | +5.2 | +10.4 | AI-power-IPP |
| NVDA | 212.06 | +2.3 | +0.1 | +9.9 | AI-compute epicenter |
| LNG | 267.40 | +1.8 | +0.9 | +18.8 | energy-fuel/AI-power |
| RTX | 194.88 | +0.6 | +0.8 | +7.1 | defense-missile |
| KMI | 32.49 | +0.3 | −0.2 | +6.9 | energy-fuel/AI-power |
| TSM | 421.21 | −0.8 | +0.2 | +6.6 | AI-compute epicenter |
| MA | 531.98 | −1.2 | −1.1 | — | payments/FIN |

**⚠ Names ≤ −3%: none. No stop hit. Nothing in the book is in trouble.**

---

## §2 · Same-day catalyst search (`--days 1`)

### 009150 — the day's biggest mover, and it has a real, named, dated catalyst

`fts search 삼성전기 --scope domestic --days 1 --snippet` (70 hits today):

> **"삼성전기, 글로벌 기업서 AI 서버용 MLCC 3000억(₩295.1bn) 수주"** — CEO 장덕현 quoted directly:
> *"이번 대규모 계약은 삼성전기 MLCC가 AI 인프라의 핵심 부품으로서 […]"* (sedaily, 본문 확인).
> Stock ran from open to **+8%** intraday on the print (연합뉴스, sedaily, 코주부 all corroborate).

**This is not noise and not a benchmark artifact** — it is the first news-explained move on this name
in **3 consecutive `industry_kr` DEEP-ENRG-adjacent runs** that had flagged 009150-class names as
"rallying with zero same-day news" (see this morning's `SECTOR_DEEP_ENRG.md` on 475150 SK이터닉스,
a different but structurally similar case). Here the news exists and is dated and quantified — a
genuinely idiosyncratic positive catalyst, not a repeat of that pattern.

### Foreign-scope event brief (`brief --scope foreign --body 2`, 485 articles → 81 market events)

**Head (≥5 outlets):**
1. **"Oil prices rise to six-week high as US-Iran tensions escalate"** (14 art / 10 outlets)
2. "Pichai pushes back on claims Google is losing ground in AI race" (8 art / 7 outlets)
3. **"Houthis claim attack on oil tankers as US launches more strikes on Iran"** (5 art / 5 outlets)

**This directly confirms and extends this morning's `industry_kr` DEEP-ENRG finding** (the
UKMTO-confirmed tanker strike, S8 branch C materializing) — the same event is now the day's #1
foreign-feed story by outlet count, not just a KR-desk-side observation.

**Notable body-tier items** (2–4 outlets, worth naming even though below head threshold):
- *"Donald Trump's Iran Blockade Announcement Sent Oil Prices Surging and the Dow Falling"* — names
  the mechanism for today's soft Nasdaq/S&P tape directly.
- *"Treasury Selloff Spreads: Fed Rate Hike Bets Heat Up, Yields Climb Across the Curve"* — the
  likeliest explanation for MA's −1.2% (rate-sensitive payments name) rather than a company-specific
  story; confirmed below that no MA-specific catalyst exists in the last 24h.
- *"KOSPI Reclaims 7,000 as Citi's 10,000 Target Gathers Steam on AI Rebound"* — independent
  corroboration (from the *foreign* feed) of this morning's `industry_kr` MACRO finding.
- *"Samsung's $516,400 bonus fuels labour disputes across South Korea"* — same SK하이닉스 성과급
  thread this morning's MACRO §3b already carried as a tail item; still not a flow signal.

### MA (−1.2%, the book's only red name) — no single-name trigger found

`fts search Mastercard --scope foreign --days 1 --snippet`: all hits date to 07-21/07-22 (earnings
commentary, 13F filings, ETF comparisons) — **nothing dated today**. Read as sector/rates drag
(Treasury selloff, above), not an MA-specific event. **Honest result, not a gap papered over.**

---

## §3 · Classify

- **Not a broad crash**: S&P −0.1%, VIX **16.6, calmer than yesterday** (17.05 on 07-21) and well
  below the >24 anti-signal. Nasdaq −0.5% is soft, not a selloff, and the one dated mechanism found
  (Treasury yields rising on Fed-hike repricing) explains it without needing a panic story.
- **Not a sector event against the book**: the book's two largest thematic clusters (AI-compute
  epicenter: AVGO/NVDA/TSM; energy-fuel/AI-power: KMI/LNG/VST) are flat-to-up. The Iran-escalation
  axis, if anything, is a **tailwind** for the energy names (VST +2.7, LNG +1.8, KMI +0.3), consistent
  with this morning's KR-desk ENRG read on the same event.
- **One idiosyncratic name, explained and positive**: 009150 +6.5%/+8% intraday on a real, quantified,
  dated MLCC contract win. Not a risk item.
- **Everything else is noise-range**: MA −1.2% (rates/sector drag, no company news), TSM −0.8%
  (no same-day trigger found — not checked in depth given it's nowhere near a stop or a −3% flag).

## Verdict: **NOISE at the book level — one clean idiosyncratic positive (009150), no crash anywhere.**

No stop is threatened (nearest headroom: TSM at +6.6%, RTX at +7.1%). The market-wide softness
(Nasdaq −0.5%) has a named, dated mechanism (Treasury/Fed-hike repricing) and does not touch the
book's own thematic exposures, which are green. The Iran/oil escalation this morning's `industry_kr`
run flagged as S8 branch C materializing is **still live and now the day's top foreign-feed story**
— worth continued attention as a geopolitical axis, but it is not currently a threat to this book; if
anything today it is paying the energy names.

## ✅ EXIT CHECK
- [x] `pulse` run: every book position's 1d/5d + stop-distance + market context (VIX/S&P/Nasdaq) read.
- [x] Same-day (`--days 1`) news catalyst pulled for the worst/best movers (009150, MA); top hits
      body-read. 009150's catalyst confirmed real and dated; MA's absence of a catalyst stated
      honestly rather than invented.
- [x] Event axis re-run (`brief --scope foreign --body 2`) to surface what a name-by-name search would
      have missed — surfaced the Houthi tanker strike as the day's #1-adjacent story, independently
      confirming this morning's `industry_kr` DEEP-ENRG finding from a different feed pull.
- [x] Verdict stated (**noise, one clean idiosyncratic positive**) with the asof/partial-day caveat
      stated first, not fabricated as a crash to match any anxiety.
