# L3 · driver_link — one segment → the thing that actually moves it, measured at the source

> **Single-role unit.** Independent — no ordering; an L2/L1 calls it when needed. Does ONE thing:
> for **one segment** named by [segment_pnl](segment_pnl.md), identify its driver, pull that driver's
> own series, and measure it — with the **roll guard** below applied before any number is reported.
> It states the driver's level, percentile and change. It does not say what the stock should do.

## The roll guard (this is most of the unit's value)
A driver quoted off a **continuous futures series** (`CL=F`, `RB=F`, `HO=F`, `NG=F`, `HG=F` …) is a
chain of different contracts. When the chain steps to the next contract the series jumps, and that jump
is **not a price move**. Before reporting any driver change:

1. Compute the daily change series and its σ over ≥6 months.
2. For every `|Δ| > 3σ` day in the reporting window, **decompose the move into its legs**.
3. **One leg alone moving ⇒ roll/spec artifact.** All legs moving together ⇒ a real move.
4. If it is a roll, back-adjust by the ratio gap and report **both** series, labelled.

**Measured 2026-08-21 (PSX, 3-2-1 crack).** The crack fell **−$9.48/bbl in one day (4.6σ)** on 08-20.
Legs: `CL +0.94%`, `HO −2.32%`, **`RB −7.93%`** — one leg, and RBOB's September→October step is the
summer→winter RVP spec change. Back-adjusted:

| | raw (roll included) | roll-adjusted |
|---|---:|---:|
| 20-day change | **−12.5%** | **−1.0%** |
| 12-month percentile | 84.9% | **92.8%** |

The raw series reads *"margin collapse"*; the adjusted series reads *"at a 12-month high, flat for a
month"*. Same day, opposite thesis. This exact trap is on record twice — see the repo memory note
*"RB=F 롤이 크랙 붕괴로 위장한다"*, which this unit turns from a remembered anecdote into a required step.

## Not every driver has a price series — say so
| driver type | example (PSX) | how to handle |
|---|---|---|
| traded spread | Refining ← 3-2-1 crack | series + roll guard above |
| traded outright | Chemicals ← ethane–ethylene | series + roll guard |
| **policy / credit** | Renewable Fuels ← RIN·LCFS credit pricing | **no clean public series in this repo** ⇒ tag `미확보` and carry the segment's own reported cause verbatim. **Do not substitute a price proxy** — a proxy for a policy variable is a fabricated driver |
| volume / throughput | Midstream ← NGL fractionation·LPG export volumes | company-reported volumes + the theme's news trajectory ([event_threads](event_threads.md)) |
| accounting | any segment ← mark-to-market | **not a driver** — it is a timing item. Name it, exclude it from the run-rate, never model it |

## ⚠ The driver is evidence about earnings, not about price
A driver at its 12-month high says the *earnings* are real; it says nothing about whether they are
priced. That question belongs to [peer_pricing](peer_pricing.md) and to the valuation stage. Reporting
a high driver percentile as a bullish conclusion is the P4 violation this unit is built to prevent.

## Output (per segment, no verdict)
`segment · driver · series id · asof · level · 12M percentile · 5/20/60/120-day change (raw AND
roll-adjusted, both shown when they differ) · roll events found in window · [company's own stated cause,
quoted]`. A driver you could not measure is a row with `미확보` and a reason — never an omitted row.

---

## 🚨 U1 · 「비상장이라 측정 불가」는 **3단 확인 뒤에만** 쓴다 (2026-09-03, NVDA 런에서 실패)

`미확보` 는 값싼 도피처가 아니다. 이 세 질문에 **전부 아니오** 여야 쓸 수 있다:

| # | 질문 | 어떻게 확인하나 |
|---|---|---|
| **①** | 그 상대방이 **상장사인가** | `https://efts.sec.gov/LATEST/search-index?q=%22<이름>%22` · `data.sec.gov/submissions/CIK*.json` |
| **②** | **상장사가 그것을 지분법·VIE 로 인식하는가** | 그 상장사 10-Q 에서 `"equity method"` · `"variable interest"` · `<상대방 이름>` 검색 |
| **③** | 대상 회사 **자기 공시가 그 상대방을 이름으로 대는가** | 8-K / 10-K Item 1 / 실적 보도자료 |

**실패 실측 (2026-09-03 NVDA)** — 이 런은 *"ACIE 41.9% 는 고객이 사모·비상장·소버린이라
감사받는 대응 계열이 **구조적으로** 존재하지 않는다"* 로 닫았다. **①과 ② 둘 다 참이었다**:
- ① NVDA 자기 8-K 가 Vera Rubin 파트너로 이름을 댄 **CoreWeave(CRWV) · Nebius(NBIS) 가 상장사**다.
  CRWV 차입금 **$51.6bn > 시총 $44.6bn**, 차입금/EBITDA **13.6배**, 선행 PER **−41.5(적자)**.
  NBIS 차입금/EBITDA **34배**. ⇒ CFO 가 쓴 *"balance sheets and long-term credit profiles"* 문장의 **실체**.
- ② **마이크로소프트가 OpenAI 지분 27% 를 지분법으로 인식한다**(10-Q, VIE, HLBV).
  Note 3 에 분기 숫자가 있다: FY25 9M **−$2.7bn** · FY25 3M **−$768M** · FY26 3M **−$19M**.
  ⇒ 공시 의무가 없는 회사의 경제성이 **상대방의 감사받는 재무제표로 측정된다.**

⚠ **선을 지켜라**: HLBV 는 지분율 단순 그로스업을 막는다. 측정 가능한 것은 **「그 상장사가 인식한 몫」**
이지 **「비상장사의 총손실」** 이 아니다. 그 구분을 안 하면 U1 이 새 오류를 만든다.

⚠ **가격 프록시 대체 금지 원칙은 그대로다.** U1 은 「다른 1차 출처를 찾아라」이지
「없으면 프록시를 써라」가 아니다.
