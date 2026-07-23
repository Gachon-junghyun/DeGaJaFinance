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
- [news](../L2_modules/news.md) — **two event passes, and the domestic one is the bigger half.**
  1. **`--scope domestic`, the PREVIOUS trading day.** This is the single largest source of material
     and it is fully settled by 08:30. ⚠ **Measured 2026-07-23: skipping it cost more than every
     other gap combined.** A 10% random audit of the 539 events knowable at 08:30 (454 domestic
     from 7/22 + 85 overnight foreign) found the 19-item draft covered **essentially none of the
     domestic sample** — and the misses were first-order: 「S&P 삼성전자 등급전망 '긍정적' 상향」,
     「LG디스플레이 상반기 흑자 전환」, 「채권단 여수 1호에 4.4조 상환유예」, 「57년 만의 VLCC
     발주 폭발」, 「中 관영매체 韓 반도체 제조업 공동화 경고」, 「후티 봉쇄에 환율 장중 1,480원대」.
     Ratings actions, earnings turns, restructuring money, an order-cycle turn — all sitting in
     yesterday's domestic pass, none of them reachable from the previous run's *conclusions*.
  2. **`--scope foreign`, the overnight window** — the US session's own event pass.
  ⚠ Do **not** run the domestic pass for **today's** date and read a small number as a quiet
  morning — at 08:30 today's domestic pool is empty by construction, not by news flow. That rule is
  about *today*; it is not a licence to skip *yesterday*, which is where most of the day's knowable
  domestic information lives.
  ⚠ **The previous desk run's output is not a substitute for the previous day's event pass.** The run
  reports what the desk concluded; the event pass reports what happened. A credit-rating outlook
  change appears in the second and never in the first.
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

## Occurrence dating — a WebSearch pass, not an inference
Before anything is ranked, **date each candidate externally**: WebSearch (and WebFetch when the hour
matters) for when the thing happened, then convert to KST. The event pass bins by publish time, so
this step is the only thing standing between the brief and a four-day-old escalation printed as news
— see the public_source unit's Rule 0 for the measured table.
- Record `발생시각(KST)` + `현지시각` + the URL that establishes it, per row.
- **Separate "the event" from "the coverage."** A tariff proposal from 6/3 covered again today is a
  6/3 event with 7/23 coverage; those are different rows, and only one of them is news.
- Rows that survive dating fall into three buckets the ranking stage needs: **간밤 발생**(overnight,
  KST early hours) · **누적/진행 중**(older, still standing) · **오늘 예정**(has not happened yet).
- If external dating fails, the row is still usable — but it must be marked `발생일 미확인` and the
  render stage will say so rather than implying today.

⚠ **Dating also tells you which day's brief an item belongs to.** Measured 2026-07-23: 한국은행 GDP
  (08:00), 삼성바이오로직스 공시, 부동산 대토론회, 무역위 반덤핑 판정 all occurred **during** 7/23 —
  none of them existed at that morning's 08:30 brief. They are 7/24 material. A first draft mixed
  them in and produced a file that could not have been written at the time it claimed.

## What this stage does
- Build `BRIEF_POOL.md`: every candidate fact, one row — `claim · number · origin · url ·
  발생시각(KST) · asof session`.
- **Reach for the origin now, not later.** For every row, record where the fact entered the world
  (the issuing body, the filing, the outlet + how many carried it). A row whose origin box is empty
  is a row that will be dropped downstream — better to find it here than to discover it at render.
- Mark each row's availability: `08:30-OK` / `prior-session-only` / `not-yet-knowable`.
- Do not rank, do not write prose, do not translate. Those are the next two stages' jobs.

## ✅ EXIT CHECK
- [ ] **Every row carries an externally-verified 발생시각 in KST** (with the local time it converts
      from), or is explicitly marked `발생일 미확인`. No date inherited from an article's publish time.
- [ ] Rows bucketed 간밤 발생 / 누적·진행 중 / 오늘 예정 — an item that has not happened yet is
      never in the first bucket.
- [ ] Every row carries an **origin outside this repo** or is explicitly marked `origin: none`.
- [ ] Every row carries an asof **session** (not just a date); mid-session pulls are labelled as such
      and are not passed forward as 08:30 facts.
- [ ] **Both event passes run: domestic on the PREVIOUS trading day, foreign on the overnight
      window** — each including the 1-outlet and non-market boundary sections; counts recorded.
      A brief built without yesterday's domestic pass is a failed stage, not a short one.
- [ ] Denominator stated: how many events were knowable at 08:30 in total, against how many the
      brief will carry. Measured baseline 2026-07-23: **539 knowable** (454 domestic + 85 foreign).
- [ ] Domestic pool emptiness at 08:30 applies to **today only** and is stated as a structural fact,
      never reported as "조용한 아침".
- [ ] Calendar pulled at 10 days, cross-checked against any dated item the prior run already carried.
- [ ] `BRIEF_POOL.md` written. No prose, no ranking, no reader-facing language yet.
