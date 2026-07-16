# L1 · PULSE — live "what's happening NOW" diagnostic (stage)

> Phase −1 (optional lead). When the book feels like it's crashing ("나락"), do NOT reason from the pipeline's
> lagging data (news up to 60d, EOD marks) — pull **same-day** signals and decide if it's real. Calls L2.
> Output: `PULSE.md`. Trigger: any sharp intraday move, a "왜 이렇게 빠져?" question, or before a nervous decision.

## Why this exists
The research desks run on lagging inputs; a live drawdown needs **today's** data or you misdiagnose it. This stage
answers one question fast: **is this a broad crash, a sector event, an idiosyncratic single-name move, or just noise?**

## L2 called
- [bookkeeping](../L2_modules/bookkeeping.md) — `python -X utf8 -m module_paper_book pulse`: current price +
  **1d / 5d change + stop-distance** for **every book position** (관련 종목 싹), plus market context (SPY/QQQ/VIX).
- [news](../L2_modules/news.md) — **same-day only**: `python -X utf8 -m module_news_data fts search <name/theme>
  --scope foreign --days 1 --snippet` (and `--days 1 --count` for a selloff-term velocity spike). ⚠ `--days 1`
  is the whole point — do not widen the window; a crash diagnosis uses fresh data, not last week's.

## What this stage does
- **Price sweep (모든 관련 종목 현재가):** run `pulse` → rank the book by 1d move; flag any name ≤ −3% and any
  ⛔ stop-hit. Read the market context line (VIX low + SPY flat = no broad panic; VIX spiking = real risk-off).
- **Same-day catalyst (뉴스 DB, 1일내):** for the worst movers and the market, search `--days 1` for the trigger.
  Body-read the top hit — a headline like "IBM plunge triggers software selloff" tells you the move is
  *sector-specific*, not yours.
- **Classify honestly (판단):**
  - **Broad crash** = SPY down hard + VIX spiking + most of the book red → de-risk / respect stops.
  - **Sector event** = one sector red (e.g. software on IBM), your other themes fine → not your problem; hold.
  - **Idiosyncratic** = one name ≤ −3% on its own news (e.g. LNG on nat-gas) → position-level decision only.
  - **Noise** = mixed/flat, VIX calm → the "나락" is perception, not tape. Say so plainly — do not invent a crash.
- ⚠ **Do not fabricate a crash to match anxiety.** If the data says flat, report flat. A missing/failed quote is a
  blank, not a red number. State the data's asof time — it may lag a real-time screen; flag that gap.

## ✅ EXIT CHECK
- [ ] `pulse` run: every book name's 1d/5d + stop-distance + market context (VIX/SPY) read.
- [ ] Same-day (`--days 1`) news catalyst pulled for the worst movers; top hit body-read.
- [ ] Verdict stated: broad crash / sector event / idiosyncratic / noise — with the asof-time caveat.
