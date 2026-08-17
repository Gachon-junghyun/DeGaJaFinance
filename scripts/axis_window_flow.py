# -*- coding: utf-8 -*-
"""axis_window_flow — 투자자 수급의 **창 의존성**을 정식 지표로 만들고 IC 원장에 축으로 넣는다.

왜 있나 (2026-08-03 실측)
------------------------
`module_KIS --investor` 는 M295 이래 있었지만 **한 번에 한 종목씩** 쓰였다. 같은 검사를
**코호트 단위**로 돌리자 창이 답을 바꾼다는 것이 드러났다 — 「외국인·기관 **양다리 모두 순매수**인
종목 수」를 20일/12일/5일 세 창으로 세면:

| 코호트 | 20일 | 12일 | 5일 | 모양 |
|---|---|---|---|---|
| 산업재(조선·방산·중공업) 14종 | 1 | 4 | 5 | 창이 짧아질수록 **증가** |
| 소비·화장품 11종 | 6 | 6 | 4 | **감소** |

극단 사례 **042660 한화오션**: 20일 외국인 **−137.4만** → 12일 **+52.1만** → 5일 **+103.7만**.
20일의 음수는 **창 앞쪽 유물**이다(롤오버 착시). 같은 종목에 대해 「외국인이 던진다」와
「외국인이 받는다」가 **둘 다 참**인데, 어느 쪽을 쓰느냐는 **창을 고른 사람**이 정했다.

⚠ **여기서 방향 가설을 세우지 않는다(P4).** 창 단축 시 증가가 좋은 신호인지 착시인지는
   **IC 가 답한다.** 이 파일은 그 질문을 **측정 가능한 스칼라**로 바꿔 원장에 배관할 뿐이다.

내보내는 축 (3개 · 서로 다른 질문)
---------------------------------
- **`bothleg_rollover`** = b(5) − b(20),  b(w) = +1(양다리 순매수) / −1(양다리 순매도) / 0(대립)
  ⇒ 위 코호트 표를 **종목 단위로 환원한 그 자체**. 이산(−2..+2)이라 크기에 둔감하고 부호만 본다.
- **`flow_accel_5_20`** = z(5) − z(20),  z(w) = (F_w + I_w) / (w · scale)
  ⇒ 같은 질문의 **연속판**. 042660 의 −137.4 → +103.7 같은 **크기**를 이산 축은 ±2 로 뭉갠다.
     `scale` = 그 종목의 20일 일평균 |외국인|+|기관| ⇒ 종목 규모로 나눈 **무차원** 값.
- **`flow_level_20`** = z(20)  ⇒ **대조축**. 이게 없으면 위 두 축의 IC 가 「창 의존성」때문인지
  그냥 **「20일 수급이 좋다」를 다시 포장한 것**인지 구분할 수 없다(C5 — 임의 선택을 노출한다).

⚠ **다중비교 비용을 알고 추가한다**: 원장의 검정 칸이 21 → 30 으로 는다. Bonferroni 임계는
   이미 |t|>2.8 이고 그대로다. 축 3개는 **공짜가 아니다** — 대조축까지 3개인 이유가 위에 있다.

측정된 제약 (읽고 나서 인용해라)
-------------------------------
- **API 비용 = 종목당 1콜.** `inquire-investor` 는 창 인자가 없다 — **30영업일을 통째로** 주고
  `days=` 는 클라이언트에서 자르기만 한다. **창 3개 = 3콜이 아니라 1콜**이다(실측 ~0.15s/콜).
- **백필 불가.** 그 엔드포인트는 **오늘 기준 30일**만 준다. 과거 런의 축을 소급 생성할 수 없다 ⇒
  이 축은 **오늘부터 하루 1행씩 쌓인다**. n=1 로 시작하는 게 정상이다.
- **장중이면 오늘 행이 자리표시자다**(수량 전부 `None`, 종가만 있음). 즉 이 축에 **선행참조가 없다** —
  런 d 의 값은 d 의 수급을 모른다. 창 정의는 `--settled`(기본: `None` 행 제외) 로 고정한다.

CLI
---
  # 코호트 (창 × 양다리개수) 표 + 단조 판정
  python -X utf8 scripts/axis_window_flow.py cohort --preset indu
  python -X utf8 scripts/axis_window_flow.py cohort --preset stpl
  python -X utf8 scripts/axis_window_flow.py cohort --tickers 005930,000660,042660

  # 유니버스 전수 → out/ic/axes/kr_{run}.json (ic_ledger 가 자동으로 잡는다)
  python -X utf8 scripts/axis_window_flow.py axes --limit 300
  python -X utf8 scripts/axis_window_flow.py axes --limit 0        # 827종 전수
  python -X utf8 scripts/axis_window_flow.py axes --limit 60 --dry-run
그 뒤 `python -X utf8 scripts/ic_ledger.py log` — **원장·axis_inflection 수정 0.**
"""
from __future__ import annotations

import argparse
import datetime as _dt
import glob
import json
import os
import sys
import time

import _repo_path  # noqa: F401

from module_KIS import fetch_investor_trend            # 수급 조회의 단일 원본(재구현 0)
from module_KIS.__main__ import _maybe_load_dotenv     # .env 주입도 재구현하지 않는다(P1)

AXIS_DIR = os.path.join("out", "ic", "axes")
FLOW_GLOB = os.path.join("llm_outputs", "*", "industry_KR", "SECTOR_FLOW_KR.json")
WINDOWS = (20, 12, 5)          # 길다 → 짧다 (표의 열 순서이자 판정의 방향)
MIN_NAMES = 50                 # ic_ledger.MIN_NAMES 와 같은 바닥 — 이보다 적으면 원장이 버린다

# 2026-08-03 industry_kr 런의 DEEP 코호트. **발견을 재측정할 수 있게** 고정해 둔다.
# 출처: llm_outputs/2026-08-03/industry_KR/SECTOR_DEEP_INDU.md §1 · SECTOR_DEEP_STPL.md §1
COHORTS = {
    "indu": [("012450", "한화에어로"), ("042660", "한화오션"), ("329180", "HD현대중공업"),
             ("009540", "HD한국조선해양"), ("010140", "삼성중공업"), ("064350", "현대로템"),
             ("047810", "한국항공우주"), ("034020", "두산에너빌리티"), ("082740", "한화엔진"),
             ("071970", "HD현대마린엔진"), ("267270", "HD건설기계"), ("439260", "대한조선"),
             ("003570", "SNT다이내믹스"), ("042700", "한미반도체")],
    "stpl": [("051900", "LG생활건강"), ("483650", "달바글로벌"), ("002790", "아모레G"),
             ("003230", "삼양식품"), ("090430", "아모레퍼시픽"), ("004370", "농심"),
             ("192820", "코스맥스"), ("271560", "오리온"), ("033780", "KT&G"),
             ("097950", "CJ제일제당"), ("161890", "한국콜마")],
}


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:                                   # noqa: BLE001
        pass


# ── 지표 ────────────────────────────────────────────────────────────────
def window_flows(rows, settled: bool = True) -> dict:
    """한 종목의 (창 × 외국인/기관 누적 순매수) + 종목 단위 스칼라 3종.

    settled=True  — 수량이 `None` 인 행(장중 자리표시자)을 **버린 뒤** 창을 센다(기본).
    settled=False — 반환된 꼬리를 그대로 센다(`None`→0). 2026-08-03 DEEP 리포트가 쓴 관례.
    """
    if settled:
        rows = [r for r in rows if r.foreign_qty is not None or r.institution_qty is not None]
    if len(rows) < max(WINDOWS):
        return {}

    def _sum(w: int, attr: str) -> float:
        return float(sum(getattr(r, attr) or 0 for r in rows[-w:]))

    legs = {w: (_sum(w, "foreign_qty"), _sum(w, "institution_qty")) for w in WINDOWS}

    # 종목 규모 정규화: 그 종목의 20일 일평균 |외국인|+|기관| (0 이면 스칼라 정의 불가)
    base = max(WINDOWS)
    scale = sum(abs(r.foreign_qty or 0) + abs(r.institution_qty or 0)
                for r in rows[-base:]) / float(base)

    def b(w: int) -> int:
        f, i = legs[w]
        if f > 0 and i > 0:
            return 1
        if f < 0 and i < 0:
            return -1
        return 0

    def z(w: int) -> float:
        if scale <= 0:
            return float("nan")
        f, i = legs[w]
        return (f + i) / (w * scale)

    return {
        "legs": legs,
        "both": {w: b(w) for w in WINDOWS},
        "scale": scale,
        "bothleg_rollover": float(b(min(WINDOWS)) - b(max(WINDOWS))),
        "flow_accel_5_20": z(min(WINDOWS)) - z(max(WINDOWS)),
        "flow_level_20": z(max(WINDOWS)),
        "last_date": rows[-1].date,
    }


def verdict(counts: list[int]) -> str:
    """창을 **길다→짧다** 로 읽었을 때의 모양. 좋고 나쁨은 판정하지 않는다(P4)."""
    a = list(counts)
    if len(set(a)) == 1:
        return "평평(창에 강건)"
    inc = all(x <= y for x, y in zip(a, a[1:]))
    dec = all(x >= y for x, y in zip(a, a[1:]))
    if inc:
        return "단조 증가(창 단축 시 증가) — 롤오버 착시 후보"
    if dec:
        return "단조 감소(창 단축 시 감소)"
    return "비단조"


def fetch_many(codes: list[str], quiet: bool = False) -> tuple[dict, float, int]:
    """코드마다 **1콜**. (결과dict, 총초, 콜수) — 비용을 항상 같이 낸다."""
    out, t0, calls = {}, time.time(), 0
    for i, c in enumerate(codes, 1):
        try:
            out[c] = fetch_investor_trend(c, days=40)
            calls += 1
        except Exception as e:                          # noqa: BLE001
            out[c] = None
            calls += 1
            if not quiet:
                print(f"  [skip] {c}: {type(e).__name__}: {e}")
        if not quiet and i % 100 == 0:
            print(f"  … {i}/{len(codes)}  {time.time()-t0:.0f}s")
    return out, time.time() - t0, calls


# ── cohort ──────────────────────────────────────────────────────────────
def cmd_cohort(args) -> int:
    if args.preset:
        pairs = COHORTS[args.preset]
    else:
        pairs = [(c.strip().split(".")[0].zfill(6), "") for c in args.tickers.split(",") if c.strip()]
    codes = [c for c, _ in pairs]
    names = dict(pairs)

    raw, el, calls = fetch_many(codes)
    print(f"# COHORT × WINDOW — {args.preset or 'ad-hoc'} · {len(codes)}종")
    print(f"  [비용 실측] {calls}콜 · {el:.1f}s · 종목당 {el/max(1,calls):.3f}s "
          f"· **창 3개 = 1콜**(엔드포인트가 30일을 통째로 준다)\n")

    for settled in (True, False):
        res = {}
        for c in codes:
            if raw.get(c):
                m = window_flows(raw[c], settled=settled)
                if m:
                    res[c] = m
        if not res:
            continue
        tag = "settled(None 행 제외)" if settled else "raw-tail(리포트 관례)"
        print(f"## 창 정의 = {tag}")
        print(f"{'티커':8s} {'종목':14s} " + " ".join(f"{w:>2}일 외/기{'':>7}" for w in WINDOWS)
              + f" {'rollover':>9} {'accel':>8} {'lvl20':>8}")
        for c in codes:
            m = res.get(c)
            if not m:
                print(f"{c:8s} {names.get(c,''):14s} (데이터 없음)")
                continue
            cells = " ".join(f"{m['legs'][w][0]/1e4:>+7.1f}/{m['legs'][w][1]/1e4:>+6.1f}"
                             for w in WINDOWS)
            print(f"{c:8s} {names.get(c,''):14s} {cells} "
                  f"{m['bothleg_rollover']:>+9.0f} {m['flow_accel_5_20']:>+8.3f} "
                  f"{m['flow_level_20']:>+8.3f}")
        counts = [sum(1 for m in res.values() if m["both"][w] == 1) for w in WINDOWS]
        print(f"\n  ★ 양다리 모두 순매수인 종목 수: "
              + " → ".join(f"{w}일 {n}" for w, n in zip(WINDOWS, counts))
              + f"   ⇒ **{verdict(counts)}**")
        print(f"  (n={len(res)} · 마지막 관측일 {sorted({m['last_date'] for m in res.values()})[-1]})\n")
    print("⚠ 이 표는 **어느 창이 옳은지 말하지 않는다**. 그 답은 IC 원장이 낸다(P4).")
    return 0


# ── axes ────────────────────────────────────────────────────────────────
def latest_run() -> tuple[str, list[dict]]:
    fs = sorted(glob.glob(FLOW_GLOB))
    if not fs:
        raise SystemExit("[err] SECTOR_FLOW_KR.json 이 없다 — sector_flow --market kr 를 먼저 돌려라")
    f = fs[-1]
    run = os.path.basename(os.path.dirname(os.path.dirname(f)))
    return run, json.load(open(f, encoding="utf-8")).get("names", [])


def cmd_axes(args) -> int:
    run, names = latest_run()
    if args.run and args.run != run:
        print(f"[err] 이 축은 **백필할 수 없다** — KIS 는 오늘 기준 30일만 준다. "
              f"최신 런 {run} 만 생성 가능(요청 {args.run}).")
        return 1
    today = _dt.date.today().isoformat()
    if run != today:
        print(f"⚠ 최신 런({run}) ≠ 오늘({today}) — 수급 창은 **오늘 기준**이다. 값이 그 런의 "
              f"시점 정보가 아닐 수 있다.")

    names = sorted(names, key=lambda n: -(n.get("mcap") or 0))
    if args.limit:
        names = names[: args.limit]
    codes = [n["ticker"].split(".")[0] for n in names]
    print(f"# AXIS window-flow — 런 {run} · 대상 {len(codes)}종(시총 상위순)")

    raw, el, calls = fetch_many(codes)
    print(f"  [비용 실측] {calls}콜 · {el:.1f}s · 종목당 {el/max(1,calls):.3f}s")

    ax = {"bothleg_rollover": {}, "flow_accel_5_20": {}, "flow_level_20": {}}
    lastdays = set()
    for n, c in zip(names, codes):
        rows = raw.get(c)
        if not rows:
            continue
        m = window_flows(rows, settled=True)
        if not m:
            continue
        lastdays.add(m["last_date"])
        for k in ax:
            v = m[k]
            if v == v:                                  # not nan
                ax[k][n["ticker"]] = round(float(v), 6)

    n_ok = len(ax["flow_level_20"])
    print("  " + " · ".join(f"{k} {len(v)}종" for k, v in ax.items())
          + f" · 마지막 관측일 {sorted(lastdays)[-1] if lastdays else '?'}")
    print(f"  (z 계열이 더 적은 이유 = scale 0 인 종목 {len(ax['bothleg_rollover'])-n_ok}개 "
          f"— 20일간 외국인·기관 거래가 전혀 없어 무차원화 불가. 0 으로 채우지 않는다(C3))")
    if n_ok < MIN_NAMES:
        print(f"[err] {n_ok} < MIN_NAMES {MIN_NAMES} — 원장이 버린다. --limit 를 늘려라.")
        return 1
    if args.dry_run:
        print("[dry-run] 파일을 쓰지 않았다.")
        return 0

    os.makedirs(AXIS_DIR, exist_ok=True)
    p = os.path.join(AXIS_DIR, f"kr_{run}.json")
    prev = {}
    if os.path.exists(p):
        try:
            prev = json.load(open(p, encoding="utf-8"))
        except Exception:                               # noqa: BLE001
            prev = {}
    prev.update(ax)
    prev.update({"_wf_source": "module_KIS.fetch_investor_trend (재구현 0) · 창 20/12/5 · settled",
                 "_wf_run": run, "_wf_n": n_ok,
                 "_wf_last_obs": sorted(lastdays)[-1] if lastdays else None})
    json.dump(prev, open(p, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"[ok] → {p}  (기존 축 보존, window-flow 3축 추가)")
    print("  다음: python -X utf8 scripts/ic_ledger.py log   (원장 수정 0으로 잡힌다)")
    return 0


def main() -> int:
    utf8_stdout()
    _maybe_load_dotenv()
    ap = argparse.ArgumentParser(prog="axis_window_flow")
    sp = ap.add_subparsers(dest="cmd", required=True)

    c = sp.add_parser("cohort", help="(창 × 양다리개수) 표 + 단조 판정")
    g = c.add_mutually_exclusive_group(required=True)
    g.add_argument("--preset", choices=sorted(COHORTS))
    g.add_argument("--tickers", help="쉼표 구분 6자리 코드")
    c.set_defaults(func=cmd_cohort)

    a = sp.add_parser("axes", help="유니버스 전수 → out/ic/axes/kr_{run}.json")
    a.add_argument("--limit", type=int, default=0,
                   help="시총 상위 N종(0=전수, 기본). ⚠ 런마다 바꾸면 횡단면이 달라져 IC 가 비교 불가")
    a.add_argument("--run", default=None, help="안전장치 — 최신 런과 다르면 거부(백필 불가)")
    a.add_argument("--dry-run", action="store_true")
    a.set_defaults(func=cmd_axes)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
