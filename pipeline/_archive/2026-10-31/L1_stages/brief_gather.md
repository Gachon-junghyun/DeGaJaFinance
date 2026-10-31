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
     ★ **Run it to find the handful of overnight facts a KR reader needs, and let each one qualify by
     having been printed domestically** (trigger **W6**). The domestic print is the qualifier because
     it does three jobs in one move: it proves the fact reached this reader's market, it dates the
     event in this reader's timezone, and it carries figures the English wires drop — measured
     2026-07-24, 국내 매체가 두바이유 90달러선과 원·엔 900원선을 실었고 영문 와이어는 둘 다 없었다.
     **Record the pass-through count as a number** (measured 2026-07-24: **5 of 810 = 0.6%**), so the
     next run can see at a glance whether the frame stayed domestic.
     ⚠ **Size-order this pass and the brief becomes a foreign brief automatically.** The overnight
     pool is **larger every day by construction** — 2026-07-24: **810 foreign market events off 5,576
     articles vs 357 domestic off 3,093**. That is a 2.3× event ratio with no editorial meaning in it.
     **Let the domestic pass set the spine first; then this pass fills the overnight gaps.**
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
  ★ **Open the 1-outlet tier with `--singles-nb` until the market-relevant rows surface, and record
  how many you recovered from it.** Measured 2026-07-25: the default view showed ~20 single-outlet
  rows and the run stopped there, cutting the day to 12 items; lowering `--singles-nb` exposed **215**
  single-outlet rows, and inside them sat first-order material the head/body never carried —
  「HMM 중장기 투자 8조원 증액」, 「조선3사 미국 1,500억달러 조선동맹」, 「오포 등 中제조사, 삼성전자
  3Q 반도체 가격 인상안 보이콧」, 「삼성·SK하이닉스 레버리지 규제」, 「환율 1,470원대」. A brief that
  stops at the default single-outlet view is reading a fraction of the tier where the day's real
  transmission lives.
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

⚠⚠ **This pass is the one most likely to be skipped, and skipping it is what publishes wrong facts.**
  Measured 2026-07-25: the run built the whole brief from the clustered event passes and **ran no
  dating pass at all**. Two errors shipped that the pass would have caught in one WebSearch each:
  (a) the EU–Google tariff threat was dated "주말 새벽" when it was a **07-24 (US Friday) Truth Social
  post**; (b) the overnight US line read *"다우 +360"* — a number that appeared in no settle, against
  the actual **Dow +235.60 / Nasdaq −0.6%**. **Run the pass before ranking, every time — it is not the
  optional polish, it is the fact-check.** A brief whose numbers were never externally checked is a
  draft, not a brief.

## Primary-source-module rule — hard numbers come from our modules, not from the news
News clusters carry the *event*; the *number* comes from the primary-source module that owns it.
This is the standing instruction (user, 2026-07-25: "숫자·계약·주가는 우리 모듈 쓰자"):

| Number type | Pull from | Not from |
|---|---|---|
| **국내 주가 · 등락률 · 투자자별 순매수** | `module_KIS` (KRX·KIS 시세/수급) | a news headline's "5% 급등" |
| **국내 수주·공급계약·투자·실적 금액** | `module_disclosure` (DART 원문 rcpNo — `--category contract`/`earnings`) | a paraphrased deal size |
| **국내 멀티플·목표주가·컨센서스** | `module_valuation` | a broker-note headline |
| **해외(US) 실적·매출·마진·추정치** | `module_fundamentals_us` (SEC XBRL 교차검증) · `module_disclosure_us` (EDGAR 8-K Item 2.02 / 10-Q) | a US-earnings wire headline |
| **해외(US) 밸류·목표가·컨센서스** | `module_fundamentals_us` | a broker note |
| **해외 매크로(금리·CPI·달러·유가)** | `module_macro_us` (FRED) + 외부 정착값 (settle-number rule) | a one-index paraphrase |

- The published file cites the **primary body in plain Korean** (한국거래소·한국투자증권 시세 /
  금융감독원 전자공시 DART / 컨센서스), never the module name (ban list) — but the *pull* is from the module.
- **Measured 2026-07-25, why this is the rule**: a news cluster said 「재산분할 판결에 SKT 5% 급등」 and
  the brief carried it on the marquee session; `module_KIS` showed SKT closed **+0.5%** that day
  (the 5% was two sessions earlier). Separately 「기아 −12.88% / 130,500원」 and 「현대모비스 9,752억
  (+12.1%)」 came back **exact** from KIS/DART — the module is both the check and the source.
- If no module owns the number (e.g. an IR investment plan not filed to DART — measured 2026-07-25,
  HMM's 29조 plan returned **0 DART rows**), say so and tag it `[IR/보도]`, not `[DART]`. A number
  with no primary-source module is a reported figure, and is labelled as one.
- **Foreign numbers get the same treatment as domestic — a US earnings figure is verified against
  `module_fundamentals_us`/`module_disclosure_us`, not left on a wire headline.** Verified 2026-07-25:
  `module_fundamentals_us INTC` returns SEC-XBRL revenue/EPS cross-validated 4/4 quarters <5%, and
  `module_disclosure_us INTC` surfaces the EDGAR **8-K Item 2.02** (the earnings filing itself). The
  published file cites the primary body in plain Korean (**미국 증권거래위원회 공시 SEC / XBRL**),
  never the module name. A foreign earnings number that shipped on a wire headline alone is the same
  defect as a domestic one on a news cluster.

## Load-bearing-number rule — a number is not a fact until it is confirmed outside the cluster
The event passes cluster on **title + summary**, and the local news DB carries a body for only some
rows (measured 2026-07-25: `fts search` for 「하나금융 순이익」 and 「HMM 투자」 both returned **0 body
matches** — those corporate items existed in the DB as headlines only). So **any number the brief will
publish — earnings, deal size, a percentage, an index level — is confirmed against a body or an
external source before it ships**, and each carries which: `[DB본문 확인]` / `[외부대조]` /
`[제목 기준·미확인]`. A `[제목 기준]` number is written as reported, not as established.
- **Measured cost of skipping this, 2026-07-25**: two numbers synthesized from cluster headlines both
  shipped wrong. 「하나금융 2분기 순익 1조1,928억, 상반기 역대 최대」 attached 역대-최대 to the **2Q**
  figure when the record was the **H1 cumulative 2조4,029억(+4.4%)** — and dropped the 2.4조 entirely.
  「HMM 8조 투자 증액」 read the **increment** as the headline when the plan was **29조 total (up 8.2조)**.
  Both were catchable in one WebSearch each. **The error rate concentrates in numbers the brief
  *builds* from a headline — those are the ones to external-check first, not last.**

## Settle-number rule — overnight market figures are pulled, not paraphrased
For every **overnight US index move, oil, and FX** figure the brief will carry, **pull the actual
settle from an external source and quote the majors together** — Dow **and** S&P **and** Nasdaq, not
one index. A one-index paraphrase inverts the day: measured 2026-07-25, "다우 +360" (wrong, and Dow-only)
hid that **Nasdaq fell 0.6% on an AI-stock sell-off** — the opposite mood from the one the line implied.
Oil carries the same trap — name the **level, the daily direction, and the day it crossed** (the $100
print was 07-22/23; 07-24 was a ~4% reversal, and a line saying only "유가 100달러" would have shipped
the peak as if it were Friday's close).

## What this stage does
- Build `BRIEF_POOL.md`: every candidate fact, one row — `claim · number · origin · url ·
  발생시각(KST) · asof session`.
- **Reach for the origin now, not later.** For every row, record where the fact entered the world
  (the issuing body, the filing, the outlet + how many carried it). A row whose origin box is empty
  is a row that will be dropped downstream — better to find it here than to discover it at render.
- Mark each row's availability: `08:30-OK` / `prior-session-only` / `not-yet-knowable`.
- Do not rank, do not write prose, do not translate. Those are the next two stages' jobs.

## ✅ EXIT CHECK
- [ ] **The occurrence-dating WebSearch pass actually ran** — not "the rule was read". Every row
      carries an externally-verified 발생시각 in KST (with the local time it converts from), or is
      explicitly marked `발생일 미확인`. No date inherited from an article's publish time. (2026-07-25:
      skipping this pass shipped a mis-dated EU event and an unverified index number.)
- [ ] **Every overnight US index / oil / FX figure was pulled from an external settle** and the US
      indices are recorded together (Dow · S&P · Nasdaq), not one paraphrased from a cluster.
- [ ] **The 1-outlet tier was opened with `--singles-nb`** below the default, and the count of
      market-relevant rows recovered from it is recorded. A run that carries only the default
      single-outlet view states so and defends it — silence here is how the day gets over-cut.
- [ ] **Every price/flow number came from `module_KIS`, every KR contract/earnings figure from
      `module_disclosure` (DART), every multiple from `module_valuation`** — not from a news headline.
      The published file cites the primary body (KRX·KIS / DART / 컨센서스) in plain Korean.
      (2026-07-25: a news "SKT 5% 급등" was +0.5% on the session per KIS.)
- [ ] **Every FOREIGN (US) earnings/revenue/margin figure was verified against `module_fundamentals_us`
      (SEC XBRL) or `module_disclosure_us` (EDGAR 8-K Item 2.02 / 10-Q)** — not left on a wire headline.
      Cited in plain Korean as SEC 공시 / XBRL. A US number with no owning module is tagged `[보도]`.
- [ ] **Every load-bearing number was confirmed outside the cluster** (module, DB body, or external
      source) and tagged. Numbers the brief *synthesized* from a headline were checked first, and any
      number with no owning module is tagged `[IR/보도]` rather than implied as primary. (2026-07-25:
      하나금융 상반기·HMM 투자 shipped wrong from cluster headlines; both were one check from correct.)
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
- [ ] **The pool is domestic-spined (W6), and the split is stated as two numbers**: how many candidate
      rows came from the domestic pass, and how many foreign rows passed the domestic-print test out
      of how many were available. Measured 2026-07-24: **5 of 810 foreign (0.6%)** alongside a
      domestic pass of 357 market events. **A run whose foreign share climbs is not automatically
      wrong — it just has to be visible before it is published**, which is what this line makes true.
- [ ] Domestic pool emptiness at 08:30 applies to **today only** and is stated as a structural fact,
      never reported as "조용한 아침".
- [ ] Calendar pulled at 10 days, cross-checked against any dated item the prior run already carried.
- [ ] `BRIEF_POOL.md` written. No prose, no ranking, no reader-facing language yet.
