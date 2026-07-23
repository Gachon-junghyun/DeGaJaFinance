# L1 · BRIEF_GATHER — what is knowable at 08:30 (stage)

> Stage 1 of `morning_brief`. Assemble the candidate facts for a **pre-open** brief, each with the
> timestamp it actually carries. Calls L2. Output: `BRIEF_POOL.md` under
> `llm_outputs/{date}/morning_brief/`. Adds no research — it only collects what already exists.

## The availability rule (the whole point of this stage)
The brief goes out at **08:30 KST — KRX is not open.** A number that cannot exist at 08:30 must not
appear as if it does. Measured failure (2026-07-23 draft): a flow line pulled at **10:20 KST** —
mid-session — was written into an 08:30 brief. At 08:30 that figure did not exist in any form.

| Available at 08:30 | Not available |
|---|---|
| Prior KR session: close, index, per-investor net-buy, short balance | **Today's** KR price / flow / index — nothing has traded |
| Overnight US session close + what moved it | Today's KR closing anything |
| FX, crude — quoted continuously | Today's domestic news at any useful volume (the pool is nearly empty until mid-morning) |
| Overnight foreign news (= the US session's own coverage) | Any figure from a mid-session pull |
| Today's calendar, and any filing published before 08:00 | |

⚠ **Label the session, not the date.** "전 거래일 종가 기준" is a fact; "어제" is ambiguous across a
holiday or a Monday. If the prior session is not the previous calendar day, say which day it was.

## L2 called
- [report_read](../L2_modules/report_read.md) — the **previous** desk run's finished output. This is
  the analytical substance of the brief; the morning stage never re-derives it. Read the prior
  `llm_outputs/{prev date}/industry_{KR|US}/` set. ⚠ Take the *facts and their origins*, not the
  desk's verdicts — a brief reports what happened, not what we concluded.
- [news](../L2_modules/news.md) — **`--scope foreign`, prior/overnight date**: the US session's own
  event pass. This is the one news axis that is genuinely full at 08:30, because the overnight window
  has already closed. ⚠ Do **not** run the domestic event pass for today's date and read a small
  number as a quiet morning — at 08:30 the domestic pool is empty by construction, not by news flow.
  ⚠ Read the recovery sections, not only head/body: the domestic prints that a brief most needs
  (FX fixings, rate/bond lines, single-outlet regulator releases) live in the 1-outlet tier and in
  the non-market boundary band. Measured 2026-07-23: 「5대은행 예·적금 금리 3%대 인상」, 「30년물
  미국채 5%」 and a domestic anti-dumping ruling were all invisible until those sections existed.
- [schedule](../L2_modules/schedule.md) — today's and this week's dated events. ⚠ Pull the **10-day**
  window, not the 5-day default: measured 2026-07-23, the 5-day pull missed four separate 07-29
  events including a domestic structural one (financial-holdco governance reform) sitting on a
  continuously-covered sector.
- [bookkeeping](../L2_modules/bookkeeping.md) — prior-session marks for any name the brief names, so
  a price claim is a quote and not a memory. ⚠ Read-only here; this stage books nothing.

## What this stage does
- Build `BRIEF_POOL.md`: every candidate fact, one row — `claim · number · origin · asof session`.
- **Reach for the origin now, not later.** For every row, record where the fact entered the world
  (the issuing body, the filing, the outlet + how many carried it). A row whose origin box is empty
  is a row that will be dropped downstream — better to find it here than to discover it at render.
- Mark each row's availability: `08:30-OK` / `prior-session-only` / `not-yet-knowable`.
- Do not rank, do not write prose, do not translate. Those are the next two stages' jobs.

## ✅ EXIT CHECK
- [ ] Every row carries an **origin outside this repo** or is explicitly marked `origin: none`.
- [ ] Every row carries an asof **session** (not just a date); mid-session pulls are labelled as such
      and are not passed forward as 08:30 facts.
- [ ] Foreign event pass run on the overnight window, **including the 1-outlet and non-market
      boundary sections**; their counts recorded.
- [ ] Domestic pool emptiness at 08:30 is stated as a structural fact, never reported as "조용한 아침".
- [ ] Calendar pulled at 10 days, cross-checked against any dated item the prior run already carried.
- [ ] `BRIEF_POOL.md` written. No prose, no ranking, no reader-facing language yet.
