# SWEEP_READ — industry_KR · 2026-07-23

> Stage 3/8. The reading only — full data in `SECTOR_FLOW_KR.json` (this run) and
> `out/kr_live_shortlist` console output (not re-saved to JSON by the script; console captured below).
> No table here that the JSON already holds.

## 1. Universe headline

**n=829 (of 832 requested) · universe wflow −0.384 · 33 green / 65 red.**

## 2. Cross-checks vs the MACRO matrix — three confirm/contradict

**(a) CONFIRMS, at 17x the sample size** — MACRO's "IT gate still shut" read (§4, 4 bellwether names:
005930/000660/042700/009150, all 🔴/🟡) holds at the full sector level: **전기·전자 (electronics, n=69)
is the single worst sector on the board — wflow −0.552, only 2 green / 18 red.** This is not a
4-name spot-check artifact; it is the broadest and most negative sector by breadth in the universe.
The GDP-beat/semis narrative in MACRO §1 has **not** translated into sector-wide flow.

**(b) CONTRADICTS** — MACRO tilted UTIL **UW** on 두산에너빌리티 alone (RS60 −51.7%, board-worst
name). But the KRX **전기·가스 (regulated utility/power distribution, n=10) sector wflow is
POSITIVE (+0.067), 1 green / 0 red** — the only sector in the whole universe with zero red names.
**Read**: 두산에너빌리티 is specifically an SMR/nuclear-equipment name, not a regulated-utility proxy;
the UW read should stay scoped to the 원전-equipment leg, not generalize to "utilities" as a KRX
sector. ROTATION should split M-03's UTIL tilt explicitly rather than let one ticker stand for ten.

**(c) CONTRADICTS, thin sample** — MACRO tilted RE **UW** on the real-10Y discount-rate argument
alone (no KR equity read). **부동산 (n=3) + 리츠 (n=22) show wflow +0.322 / +0.057, and 부동산's
breadth (0.33) is the highest of any sector in the universe.** n=3 for 부동산 proper is too thin to
lean on, but 리츠 at n=22 with positive wflow is a real, if small, contradiction of a UW built purely
on rates. Flagged for ROTATION — not enough to flip the tilt, enough to state the rate argument is
currently unconfirmed by KR REIT flow.

## 3. Shortlist — read the absences

Filter (mcap ≥1조 · tag 🟢가속 · top-15 flow_score) cut **33 green names down to 4**: SK이터닉스
(475150), 롯데렌탈 (089860), SK이노베이션 (096770), 케이뱅크 (279570) — all four confirmed
**real-hands** (foreign+institution net buyers, KIS 20d actuals).

- **Absence 1 — zero IT/전기전자 names**, consistent with cross-check (a): the sector with 18 reds
  produced nothing for the shortlist even before the mcap/rank filter bit. Not a filter artifact —
  the sector genuinely has no accelerating large-cap flow today.
- **Absence 2 — none of the four shortlisted names sit inside any MACRO-tilted sector** (FIN/ENRG/
  HLTH/UTIL/IT). Three of four (SK이터닉스, SK이노베이션, 롯데렌탈) already carry standing thesis
  coverage in `REPORT/industry_KR/BET_SHEET.md` per `module_report_tags show` — **this is a
  recurring accelerating group, not a one-day blip.** 케이뱅크 is new to the shortlist.
- **Diagnosis, not filter artifact**: with 33 green names total and only 4 clearing mcap+rank, most
  of today's 🟢 tags sit in sub-1조-cap or lower-flow-score names — the accelerating money is real
  but concentrated below large-cap. **Owner: DEEP/ROTATION** — decide whether SK이터닉스/SK이노베이션
  (both energy-transition-adjacent, both already covered) deserve a fresh DEEP look given 2 straight
  appearances, or whether 케이뱅크 (new, fintech/banking-adjacent) is worth a first look.

## ✅ EXIT CHECK
- [x] Sweep done → `SECTOR_FLOW_KR.json` (829 names, 30 sectors); ranking + green/red counts read.
- [x] LIVE_SHORTLIST run; 4/33 real-hands names identified, none personally-known bellwethers.
- [x] No table reprinted from the JSONs — cross-checks and absences only.
- [x] Two contradictions + one confirmation of the MACRO matrix stated explicitly, each diagnosed.
