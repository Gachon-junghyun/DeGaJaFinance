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
  🚨 **A `--days 1` window has the least tolerance for a dead pipe of any stage here.** The news
  search rides a tunnel that intermittently drops, and an empty result is indistinguishable from a
  quiet day (measured 2026-08-09). ⇒ On a PULSE run, **probe a known-loud name first**; if it comes
  back empty, report **"뉴스축 판정 불가"** rather than "촉매 없음". Calling a crash uncatalysed on a
  dead feed is the exact failure P4 forbids — and this stage's whole job is a same-day diagnosis.
  - **Then ask what the tape says you missed**: `brief --date <today>` (run `embed sync` first, ~2s).
    You searched the names you already suspect; the event view surfaces the one you didn't. On the
    measured crash day the term search would have chased `영업이익` while 8 outlets ran the
    circuit-breaker. ⚠ Partial by construction — today's articles are still arriving, and the day is
    binned by **publish** time, so a mid-session `brief` is a floor, not a full count. Say so.
  - **If a trigger event IS found, date it**: `thread --days 7` (~17s) tells you whether this is
    day 1 of a fresh shock or day 5 of a saga the market has already priced — the classification
    below (broad/sector/idio/noise) reads differently at day 1 vs day 5. Optional when seconds
    matter; mandatory before acting on the diagnosis.

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
