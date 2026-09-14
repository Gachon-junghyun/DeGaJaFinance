# L1 · SET_DIFF — Block C, the pre-priced set difference (stage)

> Phase C (main thread, after Block A + Block B — and Block D if it ran). Converts "is it cheap/expensive?"
> into "what do I know that the tape doesn't?". Calls L3. Output: the Block-C section of REPORT.

## Why this exists
Multiple level alone decides nothing (valuation veto). The edge is a **set difference**: the gap between
what the market already prices and what the forensic blocks actually verified. That gap — not the PER — is
the trade.

## L3 called
- [set_difference](../L3_functions/set_difference.md) — feed it two lists and it returns the deltas:
  - **① market-knows** — consensus target/rating(valuation), analyst & news-DB narrative, 52w-range implied
    expectation, rally decomposition(E-driven vs multiple-driven).
  - **② I-measured** — the labeled findings from Block A(product/bottleneck/moat) + Block B(money) + Block D(ops).

## What this stage does
- **② − ① = alpha_delta** — verified and *not* yet priced → the scoop (drives REAL).
- **① − ② = risk_unseen** — priced but I couldn't confirm → the blind spot (drives caution/BROKEN watch).
- **Sector cross-read**: before synthesizing, read this code's GICS-sector row in
  `llm_outputs/SECTOR_ALPHA_MAP_KR.md` (if present) — does the bottom-up single-name finding *agree or clash*
  with the top-down sector story? A clash is itself alpha or risk. If absent, this company is the first lens on that sector.
- **Guard**: to write "already priced in", attach the *list* of what is priced. alpha_delta empty ⇒ headed for
  REAL-but-PRICED, not REAL.

## ✅ EXIT CHECK
- [ ] ①/② lists both explicit; alpha_delta and risk_unseen both populated (or "비어있음" stated with meaning).
- [ ] No bare "밸류 부담" — every priced-in claim carries its list.
- [ ] Sector map row read/created; agreement-or-clash with the single-name finding noted.

---

## 🚨 U1-가드 · `risk_unseen` 에 「측정 불가」를 쓰기 전에

`risk_unseen` 행마다 **왜 확인 못 했나**를 적게 되어 있다. 그 이유가
**「비상장이라」 / 「사모라」 / 「감사받는 대응 계열이 없어서」** 면 **`driver_link` 의 U1 3단 확인을
통과한 뒤에만** 쓸 수 있다 — ① 상대방이 상장인가 ② **상장사가 지분법·VIE 로 인식하는가**
③ 대상 회사 공시가 이름을 대는가.

**2026-09-03 NVDA 런이 이 가드 없이 두 행을 잘못 닫았다**(`R1` ACIE 지불능력 · `R2` OpenAI 신용).
사후 탐색에서 **둘 다 측정 가능**한 것으로 드러났다(CRWV/NBIS 10-Q · MSFT 지분법 주석).
⇒ **등급이 「측정 불가」에서 「측정 가능, 아직 안 쟀음」으로 바뀌면 그건 더 나쁜 상태다** — 핑계가 사라진다.
`risk_unseen` 은 «못 잰 것» 목록이지 «못 재는 것» 목록이 아니다.
