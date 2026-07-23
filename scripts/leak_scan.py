"""leak_scan — 끝난 런이 '무엇을 지불하고 걷지 않았는가'를 계산한다.

왜 있나
-------
데스크는 진입을 채점한다(자기채점 §5). 그런데 **놓친 것**은 채점되지 않는다.
2026-07-23 수동 감사에서 실제로 나온 것:
  · 475150 — 우리 필터가 07-16 에 🟢LIVE 리드로 **잡았고**, 서사 사유로 두 번 버렸다 (+38.9%).
  · 006360 — 07-20 ALPHA 태그 + 컨센여력 +64.40% 로 **잡았고**, 섹터가 DEEP 에서 쉬자
    추적 주체가 사라졌다 (5세션 +12.3%).
  · 15종목 — 어떤 산출물에도 한 번도 등장하지 않았다.
이 스크립트는 그 세 가지를 **분류해서** 센다. 판단은 하지 않는다(P4) — L1·LEAK_AUDIT 몫.

★ 방법론 핵심 — 이 스크립트가 존재하는 진짜 이유
------------------------------------------------
"급등주 목록"을 만들어 후회하는 것은 감사가 아니라 사후확신이다. 그래서 두 가지를 강제한다:

 1. **선행검정(forward test).** 런 시점의 태그/상태 → 그 이후 실현수익. 과거 20일 수익률로
    OBV 를 채점하면 **동어반복**이다(OBV = 가격방향×거래량 누적). 실측: 후행으로 보면
    OBV 매집이 +42.2% 로 압도적이었으나, 선행으로 보면 🟡+매집은 유니버스에 **졌다**
    (−1.1% / +1.2% vs +0.7% / +5.1%). 후행 채점은 시스템을 정확히 반대로 고치게 만든다.
 2. **벤치는 지수가 아니라 시총 floor 이상 동일가중.** 실측 2026-07-23: 동일가중 −2.6% vs
    시총가중 −15.7% vs ^KS11 −21.6%. 지수 대비로 재면 거의 모든 것이 "우리가 옳았다"가 된다.

CLI
---
  python -X utf8 scripts/leak_scan.py --run 2026-07-22 --market kr
  python -X utf8 scripts/leak_scan.py --run 2026-07-22 --floor-jo 1.0 --top 25 --json
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

NOISE_BAND = 5.0


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _desk(market: str) -> str:
    return "industry_KR" if market == "kr" else "industry_US"


def _load_prices():
    import pandas as pd
    caches = sorted(glob.glob(os.path.join("llm_outputs", "sector_flow", "prices_kr_*.pkl")))
    if not caches:
        raise SystemExit("[err] 가격 캐시 없음 — `sector_flow.py --market kr` 를 먼저 돌려라")
    return pd.read_pickle(caches[-1]).xs("Close", axis=1, level=1), caches[-1]


def _universe(run: str, market: str):
    """런 시점 스냅샷 우선 — 오늘 파일로 과거 런을 채점하면 상태가 오염된다."""
    p = os.path.join("llm_outputs", run, _desk(market), "SECTOR_FLOW_KR.json")
    if not os.path.exists(p):
        cands = sorted(glob.glob(os.path.join("llm_outputs", "*", _desk(market), "SECTOR_FLOW_KR.json")))
        if not cands:
            raise SystemExit("[err] SECTOR_FLOW json 없음")
        p = cands[-1]
        print(f"[warn] {run} 스냅샷 없음 → {p} 로 대체(상태 오염 가능)", file=sys.stderr)
    return json.load(open(p, encoding="utf-8"))["names"], p


def _mentions(run: str, market: str) -> tuple[set, dict]:
    """이 런의 산출물이 실제로 언급한 6자리 코드 + 코드별 최초/최종 등장 런."""
    txt = {}
    for f in glob.glob(os.path.join("llm_outputs", "2026-*", "**", "*.md"), recursive=True):
        try:
            txt[f] = open(f, encoding="utf-8").read()
        except Exception:
            pass
    this_run, hist = set(), {}
    for f, t in txt.items():
        d = f.split(os.sep)[1]
        for c in set(re.findall(r"\b(\d{6})\b", t)):
            hist.setdefault(c, []).append(d)
            if d == run:
                this_run.add(c)
    return this_run, {k: (min(v), max(v), len(set(v))) for k, v in hist.items()}


def main() -> int:
    utf8_stdout()
    ap = argparse.ArgumentParser(prog="leak_scan")
    ap.add_argument("--run", required=True, help="감사 대상 런 날짜 (YYYY-MM-DD)")
    ap.add_argument("--market", default="kr", choices=["kr"])
    ap.add_argument("--floor-jo", type=float, default=1.0, help="시총 하한(조)")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    import pandas as pd
    cl, cache = _load_prices()
    names, upath = _universe(a.run, a.market)
    seen, hist = _mentions(a.run, a.market)
    bd = pd.Timestamp(a.run)

    rows = []
    for m in names:
        t = m["ticker"]
        if t not in cl.columns or m.get("mcap", 0) < a.floor_jo * 1e12:
            continue
        s = cl[t].dropna()
        past, fut = s[s.index <= bd], s[s.index > bd]
        if past.empty or fut.empty:
            continue
        fwd = (fut.iloc[-1] / past.iloc[-1] - 1) * 100
        code = t[:6]
        h = hist.get(code)
        rows.append(dict(code=code, name=m["name"], sec=m["sector"],
                         mcap=round(m["mcap"] / 1e12, 2), tag=m["tag"], obv=m["obv_state"],
                         flow=m["flow_score"], fwd=round(float(fwd), 2),
                         in_run=code in seen, runs=(h[2] if h else 0),
                         last_seen=(h[1] if h else None)))
    df = pd.DataFrame(rows)
    if df.empty:
        print("[err] 채점 가능한 행 없음 — 런 날짜 이후 가격이 있어야 한다")
        return 1

    bench = df.fwd.mean()
    df["excess"] = (df.fwd - bench).round(2)

    def cls(r):
        if r.in_run:
            return "A.런에 있었음"
        if r.runs >= 3:
            return "B.커버리지 소실"      # 과거에 여러 번 다뤘는데 이 런에는 없음
        if r.runs >= 1:
            return "C.스쳐감"
        return "D.발굴 부재"
    df["cls"] = df.apply(cls, axis=1)

    if a.json:
        print(json.dumps({"run": a.run, "asof": str(cl.index[-1].date()), "bench_ew": round(bench, 2),
                          "cache": cache, "universe": upath,
                          "rows": df.to_dict("records")}, ensure_ascii=False, indent=2))
        return 0

    print(f"# LEAK SCAN — 런 {a.run} → 실현 {cl.index[-1].date()}  (시총 {a.floor_jo}조+, n={len(df)})")
    print(f"  유니버스 스냅샷 {upath}\n  가격캐시 {cache}")
    print(f"  ★ 벤치 = 동일가중 평균 {bench:+.2f}%  (지수 아님 — 지수는 대형주 사건에 지배된다)\n")

    print(f"## 상위 상승 {a.top}종목 — 이 런이 걷었나")
    print(f"{'코드':7s} {'종목':16s} {'섹터':10s} {'시총':>5s} {'실현':>7s} {'초과':>7s} {'런시점태그':10s} {'OBV':5s} 분류")
    for _, x in df.nlargest(a.top, "fwd").iterrows():
        print(f"{x.code:7s} {str(x['name'])[:15]:16s} {str(x.sec)[:9]:10s} {x.mcap:>5.1f} "
              f"{x.fwd:>+7.1f} {x.excess:>+7.1f} {x.tag:10s} {str(x.obv):5s} {x.cls}")

    print("\n## ★ 선행검정 — 런 시점 상태가 이후를 예측했나 (동어반복 없음)")
    for key, lab in (("tag", "태그"), ("obv", "OBV")):
        g = df.groupby(key)["fwd"].agg(["size", "mean"]).sort_values("mean", ascending=False)
        print(f"  [{lab}]")
        for k, v in g.iterrows():
            print(f"    {str(k):10s} n={int(v['size']):>3d}  선행 {v['mean']:>+6.2f}%  "
                  f"(벤치 {bench:+.2f}%, 초과 {v['mean'] - bench:>+6.2f}pp)")

    print("\n## 누수 분류")
    g = df.groupby("cls")["fwd"].agg(["size", "mean"])
    for k, v in g.sort_values("mean", ascending=False).iterrows():
        print(f"  {k:14s} n={int(v['size']):>3d}  평균 실현 {v['mean']:>+6.2f}%  초과 {v['mean'] - bench:>+6.2f}pp")

    big = df[(df.excess > NOISE_BAND) & (~df.in_run)]
    print(f"\n## 이 런 밖에서 벤치를 {NOISE_BAND:.0f}pp 이상 이긴 이름 — {len(big)}건")
    for _, x in big.nlargest(15, "excess").iterrows():
        prev = f"최종등장 {x.last_seen}" if x.last_seen else "등장 이력 없음"
        print(f"  {x.code} {str(x['name'])[:14]:16s} 초과 {x.excess:>+6.1f}pp · {x.cls} · {prev} · 런시점 {x.tag}/{x.obv}")

    print("\n⚠ 이 표는 '놓쳤다'를 세지 않는다 — **런 시점 상태로 잡을 수 있었는가**를 묻는 재료다.")
    print("   선행검정에서 그 상태가 벤치를 못 이겼다면, 안 잡은 것은 실패가 아니라 규율이다(P4).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
