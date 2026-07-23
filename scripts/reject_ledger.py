"""reject_ledger — 거부(DROP/PASS/강등) 원장 + 사후 채점.

왜 있나
-------
데스크의 거부는 지금까지 BET_SHEET/DECISIONS 의 **산문**에만 남았다. 그래서
"우리가 무엇을 왜 거부했고, 그 거부가 돈을 벌었나 잃었나"를 물으면 정규식으로
과거 마크다운을 복원해야 한다 — 즉 **채점되지 않는다.**

측정된 사실(2026-07-23, KR, 거부 24건, 창 3~12세션):
  - 16/24 = 67% 가 |초과| ≤5pp = **노이즈**. 거부 노동의 2/3 가 아무것도 바꾸지 않았다.
  - 손해 4건 합계 +83.8pp vs 이득 4건 합계 −38.5pp → **손해가 이득의 2.2배.**
  - 가장 비싼 사유는 **서사 기반**(테마소멸 +18.6pp · 공매도테제전환 +26.9pp),
    돈을 지킨 사유는 **측정 기반**(OBV분배 −5.1pp · 상관가드 −5.3pp).
  ⚠ n 이 작고(클래스별 1~4건) 창이 전부 한 반등국면이다. **규칙을 박제하지 말고
    누적 점수를 매 런 출력**하는 것이 이 도구의 목적이다.

P4: 판단은 하지 않는다. 관측값(거부시점가·현재가·벤치)과 초과수익만 계산한다.
P1: 가격은 sector_flow 가 이미 받아둔 캐시(`llm_outputs/sector_flow/prices_kr_*.pkl`)를
    재사용한다 — yfinance 를 다시 때리지 않는다.

CLI
---
  python -X utf8 scripts/reject_ledger.py add --date 2026-07-22 --ticker 005380 \
      --name 현대차 --cls K.본문반증 --why "파업 생산차질" --stage BET \
      --revives-if "기관 순매수 부호 유지 + 파업 타결" --recheck-date 2026-07-30
  python -X utf8 scripts/reject_ledger.py score            # 전체 채점 + 클래스 집계
  python -X utf8 scripts/reject_ledger.py score --json
  python -X utf8 scripts/reject_ledger.py due               # 재확인일 지난 거부 + 부활조건 없는 레거시 감사
  python -X utf8 scripts/reject_ledger.py resolve --ticker 475150 --date 2026-07-20 \
      --outcome revived --note "공매도 covering 복귀 + 진짜손 확인, 2026-07-23 재승격"
  python -X utf8 scripts/reject_ledger.py seed             # 07-11~07-22 기존 거부 24건 적재

⚠ **`--revives-if` 와 `--recheck-date` 는 `add` 의 필수 인자다(2026-07-23부로 강제).** 둘 중 하나라도
빠지면 `add` 자체가 실패한다 — 부활조건 없는 거부는 사실상 영구금지이고, 영구금지는 거의 언제나 과하다
(측정: 2026-07-16/07-20 두 차례 조건 없이 거부된 SK이터닉스가 원장 전체에서 가장 비싼 손해 +41.2pp/
+26.9pp를 냈다). 조건을 안 채운 채 넘어가려는 시도는 이 스크립트가 대신 막는다 — 사람이 매번
기억해서 지키는 규율이 아니다.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import glob
import json
import os
import sys

RESOLUTIONS = os.path.join("out", "reject_ledger_resolutions.jsonl")

LEDGER = os.path.join("out", "reject_ledger.jsonl")
NOISE_BAND = 5.0  # |초과| 이하 = 노이즈로 분류


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ── 사유 클래스 ─────────────────────────────────────────────────────────
# 측정 기반(measured) vs 서사 기반(narrative) 을 스키마에 박아둔다.
# 이 구분이 위 실측에서 유일하게 부호가 갈린 축이다.
CLASSES = {
    "A.flow미도착": "measured",   # 테제는 맞는데 수급이 아직 없음
    "B.모멘텀only": "measured",   # OBV 분배 into strength
    "C.차트붕괴": "measured",
    "D.약한손": "measured",       # 외국인/기관 이탈 + 개인 흡수
    "E.상관가드": "structural",   # 리스크유닛 중복 / 집중도
    "F.테마소멸": "narrative",    # 스레드 FADING/ENDED, "촉매 없음"
    "G.섹터중립": "structural",
    "H.밸류소진": "measured",
    "I.테제반증": "narrative",    # 부수 테제(스퀴즈 등)가 깨짐
    "J.사이즈미미": "measured",
    "K.본문반증": "narrative",
    "L.vehicle없음": "measured",
}


def load() -> list[dict]:
    if not os.path.exists(LEDGER):
        return []
    out = []
    with open(LEDGER, encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if ln:
                out.append(json.loads(ln))
    return out


def append(rec: dict) -> None:
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def load_resolutions() -> list[dict]:
    if not os.path.exists(RESOLUTIONS):
        return []
    out = []
    with open(RESOLUTIONS, encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if ln:
                out.append(json.loads(ln))
    return out


def append_resolution(rec: dict) -> None:
    os.makedirs(os.path.dirname(RESOLUTIONS), exist_ok=True)
    with open(RESOLUTIONS, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def due(asof: str | None = None) -> int:
    """재확인일이 지났는데 아직 해소되지 않은 거부 + 부활조건 자체가 없는 레거시 항목을 낸다.

    이 명령 없이 사람이 매 런 기억해서 원장을 다시 여는 방식으로는 이 발견(§ALPHA-2,
    2026-07-23)이 반복되지 않는다 — 그래서 HANDOVER 가 SCENARIOS.md 의 과거-날짜 시나리오를
    스코어링하는 것과 같은 자리에서, 이 명령도 같이 돈다(pipeline/L1_stages/handover.md).
    """
    today = _dt.date.fromisoformat(asof) if asof else _dt.date.today()
    recs = load()
    resolved_keys = {(r["ticker"], r["date"]) for r in load_resolutions()}
    if not recs:
        print("[info] 원장 비어있음")
        return 0

    legacy_no_condition = [r for r in recs if not r.get("revives_if")
                           and (r["ticker"], r["date"]) not in resolved_keys]
    overdue = []
    for r in recs:
        if (r["ticker"], r["date"]) in resolved_keys:
            continue
        rc = r.get("recheck_date")
        if not rc:
            continue
        d = _dt.date.fromisoformat(rc)
        if d <= today:
            overdue.append((r, (today - d).days))

    print(f"# REJECT LEDGER — 재확인 감사 asof {today.isoformat()}")
    print(f"  전체 {len(recs)}건 · 해소됨 {len(resolved_keys)}건 · "
          f"부활조건 없는 레거시(감사 필요) {len(legacy_no_condition)}건 · "
          f"재확인일 도래/경과 {len(overdue)}건\n")

    if overdue:
        print("## 재확인일이 지났다 — 확인 없이 다음 런으로 넘기지 않는다")
        for r, days in sorted(overdue, key=lambda x: -x[1]):
            print(f"  {r['date']} {r['ticker']} {r['name']:14s} [{r['cls']}] "
                  f"D+{days:<4d} 부활조건: {r['revives_if']}")
    if legacy_no_condition:
        print("\n## 부활조건이 처음부터 없던 레거시 항목 — 개별 재조사 없이는 영구금지로 방치되면 안 된다")
        for r in legacy_no_condition:
            print(f"  {r['date']} {r['ticker']} {r['name']:14s} [{r['cls']}] "
                  f"사유: {r['why']}")
    if not overdue and not legacy_no_condition:
        print("  확인할 항목 없음 — 모든 거부가 조건부이고 재확인일이 아직 도래하지 않았다.")
    return 0


def _prices():
    """sector_flow 가 받아둔 최신 가격 캐시를 재사용(P1)."""
    import pandas as pd

    caches = sorted(glob.glob(os.path.join("llm_outputs", "sector_flow", "prices_kr_*.pkl")))
    if not caches:
        raise SystemExit("[err] 가격 캐시 없음 — sector_flow --market kr 를 먼저 돌려라")
    return pd.read_pickle(caches[-1]).xs("Close", axis=1, level=1), caches[-1]


def _bench_universe(cl, floor_jo: float = 1.0) -> list[str]:
    """벤치 = 시총 floor 이상 종목의 동일가중. 지수(^KS11)는 대형주 사건에
    지배되므로(2026-07 실측: 동일가중 −2.6% vs 시총가중 −15.7%) 쓰지 않는다."""
    js = sorted(glob.glob(os.path.join("llm_outputs", "*", "industry_KR", "SECTOR_FLOW_KR.json")))
    if not js:
        return list(cl.columns)
    d = json.load(open(js[-1], encoding="utf-8"))
    return [x["ticker"] for x in d["names"]
            if x.get("mcap", 0) >= floor_jo * 1e12 and x["ticker"] in cl.columns]


def score(as_json: bool = False, floor_jo: float = 1.0) -> int:
    import pandas as pd

    recs = load()
    if not recs:
        print("[info] 원장 비어있음 — `seed` 또는 `add` 를 먼저 실행")
        return 0
    cl, cache = _prices()
    big = _bench_universe(cl, floor_jo)
    sub = cl[big]
    rows = []
    for r in recs:
        col = r["ticker"] + ".KS"
        if col not in cl.columns:
            r = {**r, "note": "가격없음"}
            rows.append(r)
            continue
        s = cl[col].dropna()
        bd = pd.Timestamp(r["date"])
        past = s[s.index <= bd]
        if past.empty:
            continue
        p0, p1 = past.iloc[-1], s.iloc[-1]
        fwd = (p1 / p0 - 1) * 100
        b0 = sub[sub.index <= bd].iloc[-1]
        bench = ((sub.iloc[-1] / b0 - 1) * 100).dropna().mean()
        rows.append({**r, "px0": float(p0), "px1": float(p1),
                     "fwd": round(float(fwd), 2), "bench": round(float(bench), 2),
                     "excess": round(float(fwd - bench), 2)})
    df = pd.DataFrame([x for x in rows if "excess" in x])
    if as_json:
        print(json.dumps({"asof": str(cl.index[-1].date()), "cache": cache,
                          "rows": rows}, ensure_ascii=False, indent=2))
        return 0

    print(f"# REJECT LEDGER — 채점 asof {cl.index[-1].date()}  (벤치 = 시총 {floor_jo}조+ 동일가중)")
    print(f"  가격캐시 {cache} · 기록 {len(recs)}건 · 채점가능 {len(df)}건\n")
    print(f"{'거부일':11s} {'종목':14s} {'사유클래스':13s} {'유형':10s} {'수익':>7s} {'벤치':>7s} {'초과':>8s}  판정")
    for _, x in df.sort_values("excess", ascending=False).iterrows():
        kind = CLASSES.get(x["cls"], "?")
        v = ("X 거부가 손해" if x.excess > NOISE_BAND
             else ("O 거부가 이득" if x.excess < -NOISE_BAND else "- 무의미"))
        print(f"{x['date']:11s} {str(x['name'])[:13]:14s} {x['cls']:13s} {kind:10s} "
              f"{x.fwd:>+7.1f} {x.bench:>+7.1f} {x.excess:>+8.1f}  {v}")

    print("\n## 사유 클래스별")
    g = df.groupby("cls")["excess"].agg(["size", "mean", "median"]).sort_values("mean", ascending=False)
    for k, v in g.iterrows():
        kind = CLASSES.get(k, "?")
        print(f"  {k:13s} [{kind:10s}] n={int(v['size']):>3d}  평균초과 {v['mean']:>+7.1f}pp  중앙 {v['median']:>+7.1f}pp")

    print("\n## 유형별 (measured / structural / narrative)")
    df = df.assign(kind=df["cls"].map(lambda c: CLASSES.get(c, "?")))
    for k, v in df.groupby("kind")["excess"].agg(["size", "mean"]).sort_values("mean", ascending=False).iterrows():
        print(f"  {k:12s} n={int(v['size']):>3d}  평균초과 {v['mean']:>+7.1f}pp")

    hurt = (df.excess > NOISE_BAND).sum()
    help_ = (df.excess < -NOISE_BAND).sum()
    noise = len(df) - hurt - help_
    print(f"\n  전체 {len(df)}건 · 평균초과 {df.excess.mean():+.1f}pp"
          f" · 손해 {hurt} · 이득 {help_} · 노이즈 {noise} ({noise/len(df)*100:.0f}%)")
    print(f"  손해합 {df[df.excess > NOISE_BAND].excess.sum():+.1f}pp"
          f" vs 이득합 {df[df.excess < -NOISE_BAND].excess.sum():+.1f}pp")
    print("\n⚠ 표본이 작고 창이 짧다 — 클래스 평균은 누적 관측이지 검증된 엣지가 아니다(P4).")
    return 0


SEED = [
    ("2026-07-11", "000500", "가온전선", "A.flow미도착", "테제 맞음 돈은 약한손", "BET"),
    ("2026-07-11", "103590", "일진전기", "A.flow미도착", "동상", "BET"),
    ("2026-07-13", "010120", "LS ELECTRIC", "A.flow미도착", "뉴스리드 flow미도착", "BET"),
    ("2026-07-15", "267260", "HD현대일렉트릭", "A.flow미도착", "수출순풍 최강 flow최악", "BET"),
    ("2026-07-15", "000660", "SK하이닉스", "B.모멘텀only", "OBV -34 분배 into strength", "BET"),
    ("2026-07-15", "055550", "신한지주", "B.모멘텀only", "OBV -44 모멘텀only", "BET"),
    ("2026-07-14", "042700", "한미반도체", "C.차트붕괴", "OBV-78 MA0/4 falling knife", "BET"),
    ("2026-07-15", "034020", "두산에너빌리티", "C.차트붕괴", "FALLING-KNIFE OBV-32", "BET"),
    ("2026-07-16", "073240", "금호타이어", "D.약한손", "외-921 기-467 개+1432", "BET"),
    ("2026-07-16", "008930", "한미사이언스", "D.약한손", "외-63 개인흡수 혼조", "BET"),
    ("2026-07-16", "161890", "한국콜마", "D.약한손", "외국인 이탈확대 OBV상충", "BET"),
    ("2026-07-20", "073240", "금호타이어", "D.약한손", "외-899 개+1390", "BET"),
    ("2026-07-16", "105560", "KB금융", "E.상관가드", "하나와 동일 리스크유닛", "미러링"),
    ("2026-07-16", "010950", "S-Oil", "E.상관가드", "energy 21% 최대유닛+RSI85.9", "미러링"),
    ("2026-07-16", "042700", "한미반도체", "E.상관가드", "AI-compute 유닛 중복", "미러링"),
    ("2026-07-16", "475150", "SK이터닉스", "F.테마소멸", "신재생FADING+PER62", "BET"),
    ("2026-07-20", "161890", "한국콜마", "F.테마소멸", "no card no fresh catalyst", "BET"),
    ("2026-07-20", "008930", "한미사이언스", "G.섹터중립", "HLTH is Neutral", "BET"),
    ("2026-07-20", "000810", "삼성화재", "H.밸류소진", "여력+2.98% 이미 움직임", "BET"),
    ("2026-07-20", "475150", "SK이터닉스", "I.테제반증", "공매도 covering->building +0.54", "BET"),
    ("2026-07-20", "089860", "롯데렌탈", "J.사이즈미미", "noise-level size", "BET"),
    ("2026-07-22", "005380", "현대차", "K.본문반증", "파업 생산차질", "EVENT_ALPHA"),
    ("2026-07-22", "373220", "LG에너지솔루션", "K.본문반증", "단독1건 체인전체 분산", "EVENT_ALPHA"),
    ("2026-07-22", "454910", "두산로보틱스", "L.vehicle없음", "랭크793 분산", "SWEEP"),
]


def main() -> int:
    utf8_stdout()
    ap = argparse.ArgumentParser(prog="reject_ledger")
    sp = ap.add_subparsers(dest="cmd", required=True)

    a = sp.add_parser("add", help="거부 1건 기록")
    a.add_argument("--date", required=True)
    a.add_argument("--ticker", required=True, help="6자리 (접미사 없이)")
    a.add_argument("--name", required=True)
    a.add_argument("--cls", required=True, choices=sorted(CLASSES))
    a.add_argument("--why", required=True)
    a.add_argument("--stage", default="")
    a.add_argument("--revives-if", required=True,
                    help="이 조건이 참이 되면 거부 해제 (필수 — 빈 값 금지, 킬 로그 만료조건)")
    a.add_argument("--recheck-date", required=True,
                    help="이 날짜(YYYY-MM-DD)가 지나면 `due` 가 확인 대상으로 올린다 (필수)")

    s = sp.add_parser("score", help="전체 채점")
    s.add_argument("--json", action="store_true")
    s.add_argument("--floor-jo", type=float, default=1.0)

    d = sp.add_parser("due", help="재확인일 도래/경과 + 부활조건 없는 레거시 감사")
    d.add_argument("--asof", default=None)

    r = sp.add_parser("resolve", help="재확인 완료(부활 또는 재확정) 기록 — 원장 행은 손대지 않는다(append-only)")
    r.add_argument("--ticker", required=True)
    r.add_argument("--date", required=True, help="원 거부일(원장의 date 값과 정확히 일치해야 매칭됨)")
    r.add_argument("--outcome", required=True, choices=["revived", "reaffirmed"])
    r.add_argument("--note", required=True)

    sp.add_parser("seed", help="07-11~07-22 기존 거부 적재(1회, 레거시 — revives_if 없이 적재됨, `due`가 감사 대상으로 잡는다)")
    sp.add_parser("list", help="원장 덤프")

    args = ap.parse_args()
    if args.cmd == "add":
        append({"date": args.date, "ticker": args.ticker, "name": args.name,
                "cls": args.cls, "why": args.why, "stage": args.stage,
                "revives_if": args.revives_if, "recheck_date": args.recheck_date})
        print(f"[ok] {args.date} {args.ticker} {args.name} [{args.cls}] 기록 "
              f"(재확인일 {args.recheck_date})")
        return 0
    if args.cmd == "seed":
        if load():
            print("[skip] 원장에 이미 기록이 있다 — 중복 적재 방지")
            return 0
        for d2, t, n, c, w, st in SEED:
            append({"date": d2, "ticker": t, "name": n, "cls": c, "why": w,
                    "stage": st, "revives_if": "", "recheck_date": ""})
        print(f"[ok] {len(SEED)}건 적재 → {LEDGER} (레거시 — revives_if 없음, `due`로 감사할 것)")
        return 0
    if args.cmd == "list":
        for r2 in load():
            print(json.dumps(r2, ensure_ascii=False))
        return 0
    if args.cmd == "due":
        return due(asof=args.asof)
    if args.cmd == "resolve":
        append_resolution({"ticker": args.ticker, "date": args.date,
                            "outcome": args.outcome, "note": args.note,
                            "resolved_asof": _dt.date.today().isoformat()})
        print(f"[ok] {args.ticker}({args.date}) → {args.outcome} 기록 (원장 원본은 미변경, append-only)")
        return 0
    return score(as_json=args.json, floor_jo=args.floor_jo)


if __name__ == "__main__":
    raise SystemExit(main())
