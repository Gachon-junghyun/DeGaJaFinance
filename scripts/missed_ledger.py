# -*- coding: utf-8 -*-
"""missed_ledger — **기회비용 원장**. `reject_ledger` 의 대칭 짝.

왜 있나 (결함 F2, 2026-07-31 실측)
----------------------------------
점수판이 비대칭이다. **거부는 채점되는데 미진입은 어느 숫자에도 안 남는다.**
`scripts/reject_ledger.py` 는 거부 45건을 사유클래스·부활조건·초과수익까지 채점하는데,
"검토했지만 사지 않은 것"을 재는 장치는 **리포 전체에 없었다.**
구체적 비용: **042700 한미반도체 +27.4%(07-31)** — 데스크가 07-14 에 보고 지나쳤고,
그 사실이 어떤 원장에도 남지 않았다. 남지 않으면 개선되지 않는다.

거부 원장과 무엇이 다른가
-------------------------
**부호가 반대다.** 거부 원장에서 `excess > 0` 은 "거부가 손해"였다.
여기서는 사지 않은 것이 올랐으면 그것이 손해이므로, `excess > 0` = **놓쳐서 손해**.
같은 축(사유클래스 · 부활조건 · 재확인일 · 벤치)을 그대로 쓰되 **판정 문구만 뒤집는다.**

⚠ 거부 원장과 겹치지 않게 하라
------------------------------
`reject_ledger` 에 이미 DROP 으로 기록된 종목·날짜는 **여기 다시 넣지 않는다**
(`add` 가 자동 검사해 거부한다). 두 원장이 같은 사건을 두 번 세면 합산이 거짓말이 된다.
이 원장의 대상은 **"거부라고 말할 만큼도 다루지 않고 지나간 것"** — 스윕에 떴는데 숏리스트에
못 올랐거나, 후보로 언급만 되고 BET 에 안 들어간 이름이다.

P1 — 재구현 0
-------------
가격 캐시·벤치 유니버스·채점 산술은 **`reject_ledger` 에서 import** 한다. 벤치도 같은 것
(시총 1조+ 동일가중 — 지수는 대형주 사건에 지배됨: 실측 동일가중 −2.6% vs 시총가중 −15.7%).
같은 질문에 두 개의 벤치를 쓰면 두 원장을 나란히 놓을 수 없다.

P4 — 판단하지 않는다. 관측값(미진입시점가·현재가·벤치)과 초과수익만 낸다.

CLI (reject_ledger 와 동형)
---------------------------
  python -X utf8 scripts/missed_ledger.py add --date 2026-07-14 --ticker 042700 \\
      --name 한미반도체 --cls M.숏리스트탈락 --why "OBV-78 MA0/4 falling knife 로 스윕에서 하차" \\
      --stage SWEEP --enters-if "OBV 매집 전환 + 20일선 회복" --recheck-date 2026-08-07
  python -X utf8 scripts/missed_ledger.py score            # 전체 채점 + 클래스 집계
  python -X utf8 scripts/missed_ledger.py score --json
  python -X utf8 scripts/missed_ledger.py due              # 재확인일 지난 미진입
  python -X utf8 scripts/missed_ledger.py resolve --ticker 042700 --date 2026-07-14 \\
      --outcome entered --note "07-31 B안에서 +6.0% 신규 진입"
  python -X utf8 scripts/missed_ledger.py list
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys

import reject_ledger as RL          # ★ P1 — 가격·벤치·채점 산술을 여기서 재사용

LEDGER = os.path.join("out", "missed_ledger.jsonl")
RESOLUTIONS = os.path.join("out", "missed_ledger_resolutions.jsonl")
NOISE_BAND = RL.NOISE_BAND          # 거부 원장과 같은 노이즈 밴드(±5pp) — 비교 가능해야 한다

# ── 미진입 사유 클래스 ───────────────────────────────────────────────────
# 거부 원장의 measured/structural/narrative 3분류를 그대로 쓴다. 그 축이 실측에서
# 유일하게 부호가 갈린 축이기 때문이고, 두 원장을 같은 축으로 합산해야 하기 때문이다.
CLASSES = {
    "M.숏리스트탈락": "measured",    # 스윕엔 떴는데 정량 컷에서 하차
    "N.유니버스부재": "structural",  # 애초에 분모에 없었다 (D44 KOSDAQ 공백 계열)
    "O.커버리지소실": "structural",  # 이전 런엔 있었는데 이번 런에서 사라짐
    "P.현금부족": "structural",      # 사고 싶었으나 노출 규칙/현금이 막음 ← ①과 직결
    "Q.확신부족": "narrative",       # "더 보고 싶다" 로 미룸
    "R.타이밍대기": "narrative",     # 눌림목/재확인 기다리다 놓침
    "S.테마회피": "narrative",       # 테마 자체를 안 봄
    "T.사이즈미미": "measured",      # 넣어도 의미 없는 크기라 패스
    "U.발굴부재": "structural",      # 어떤 산출물에도 등장한 적 없음 (leak_scan D 버킷)
}

# leak_scan(`scripts/leak_scan.py`)의 누수 분류 → 이 원장의 사유클래스 매핑.
# 두 도구가 같은 사건을 다른 이름으로 부르면 합산이 안 된다(P1 의 정신).
LEAK_MAP = {
    "A.런에있었음": "Q.확신부족",
    "B.커버리지소실": "O.커버리지소실",
    "C.스쳐감": "M.숏리스트탈락",
    "D.발굴부재": "U.발굴부재",
}


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _load(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if ln:
                out.append(json.loads(ln))
    return out


def _append(path: str, rec: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def load() -> list[dict]:
    return _load(LEDGER)


def load_resolutions() -> list[dict]:
    return _load(RESOLUTIONS)


# ── 채점 ─────────────────────────────────────────────────────────────────
def score(as_json: bool = False, floor_jo: float = 1.0) -> int:
    import pandas as pd

    recs = load()
    if not recs:
        print(f"[info] 기회비용 원장 비어있음 — `add` 를 먼저 실행 ({LEDGER})")
        print("  ⚠ 비어있음은 '놓친 게 없다'가 아니라 '아직 아무도 안 적었다'다(F2 의 본체).")
        return 0

    cl, cache = RL._prices()                 # P1 — sector_flow 가 받아둔 캐시 재사용
    big = RL._bench_universe(cl, floor_jo)   # P1 — 같은 벤치(시총 1조+ 동일가중)
    sub = cl[big]
    rows = []
    for r in recs:
        col = r["ticker"] + ".KS"
        if col not in cl.columns:
            rows.append({**r, "note": "가격없음"})
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

    print(f"# MISSED LEDGER — 기회비용 채점 asof {cl.index[-1].date()}  "
          f"(벤치 = 시총 {floor_jo}조+ 동일가중, 거부 원장과 동일)")
    print(f"  가격캐시 {cache} · 기록 {len(recs)}건 · 채점가능 {len(df)}건")
    print("  ★ 부호 주의: 거부 원장과 **반대**다. `초과 > 0` = 놓쳐서 손해.\n")
    print(f"{'미진입일':11s} {'종목':14s} {'사유클래스':15s} {'유형':10s} "
          f"{'수익':>7s} {'벤치':>7s} {'초과':>8s}  판정")
    for _, x in df.sort_values("excess", ascending=False).iterrows():
        kind = CLASSES.get(x["cls"], "?")
        v = ("X 놓쳐서 손해" if x.excess > NOISE_BAND
             else ("O 안 사서 이득" if x.excess < -NOISE_BAND else "- 무의미"))
        print(f"{x['date']:11s} {str(x['name'])[:13]:14s} {x['cls']:15s} {kind:10s} "
              f"{x.fwd:>+7.1f} {x.bench:>+7.1f} {x.excess:>+8.1f}  {v}")

    print("\n## 사유 클래스별")
    g = df.groupby("cls")["excess"].agg(["size", "mean", "median"]).sort_values("mean", ascending=False)
    for k, v in g.iterrows():
        print(f"  {k:15s} [{CLASSES.get(k,'?'):10s}] n={int(v['size']):>3d}  "
              f"평균초과 {v['mean']:>+7.1f}pp  중앙 {v['median']:>+7.1f}pp")

    print("\n## 유형별 (measured / structural / narrative)")
    df = df.assign(kind=df["cls"].map(lambda c: CLASSES.get(c, "?")))
    for k, v in df.groupby("kind")["excess"].agg(["size", "mean"]).sort_values(
            "mean", ascending=False).iterrows():
        print(f"  {k:12s} n={int(v['size']):>3d}  평균초과 {v['mean']:>+7.1f}pp")

    hurt = (df.excess > NOISE_BAND).sum()
    help_ = (df.excess < -NOISE_BAND).sum()
    noise = len(df) - hurt - help_
    print(f"\n  전체 {len(df)}건 · 평균초과 {df.excess.mean():+.1f}pp"
          f" · 놓쳐손해 {hurt} · 안사서이득 {help_} · 노이즈 {noise} ({noise/len(df)*100:.0f}%)")
    print(f"  놓친합 {df[df.excess > NOISE_BAND].excess.sum():+.1f}pp"
          f" vs 피한합 {df[df.excess < -NOISE_BAND].excess.sum():+.1f}pp")

    # ★ 두 원장을 나란히 — 이것이 이 파일의 존재 이유다
    try:
        rj = RL.load()
        print(f"\n## 점수판 대칭 확인 — 거부 {len(rj)}건 vs 미진입 {len(recs)}건")
        if len(recs) * 3 < len(rj):
            print("  🚨 여전히 비대칭이다. 거부만 적고 미진입은 안 적으면 F2 는 안 닫힌다.")
    except Exception:                                    # noqa: BLE001
        pass
    # ★ 표본 층별 집계 — 이 원장에서 **가장 중요한 표**다.
    # 어떻게 뽑혔는지가 다른 행들을 한 평균으로 접으면, 그 평균은 아무것도 뜻하지 않는다.
    df = df.assign(sample=df.get("sample", pd.Series(["outcome_selected"] * len(df))).fillna(
        "outcome_selected"))
    print("\n## ★ 표본 층별 — 층을 섞은 평균은 읽지 마라")
    for k, v in df.groupby("sample")["excess"].agg(["size", "mean", "median"]).iterrows():
        tag = {"prospective": "✅ 편향 없음 — 이 층만 엣지 추정에 쓸 수 있다",
               "random": "△ 사후지만 무작위 — 클래스 비교엔 쓸 수 있음",
               "outcome_selected": "🚨 상승 상위에서 추출 — 평균이 구조적으로 양수. 추정에 쓰지 마라"}
        print(f"  {k:17s} n={int(v['size']):>3d}  평균초과 {v['mean']:>+7.1f}pp  "
              f"중앙 {v['median']:>+7.1f}pp   {tag.get(k, '?')}")
    if "prospective" not in set(df["sample"]):
        print("\n  ⚠ **사전등록(`prospective`) 행이 아직 0건이다.** 지금 이 원장은 '적립 방식의 시연'이고,"
              "\n    엣지 추정에는 쓸 수 없다. 다음 런의 BET/EVENT_ALPHA 가 결정 시점에 적기 시작해야"
              "\n    비로소 측정이 된다(C4).")
    print("\n⚠ 표본이 작고 창이 짧다 — 클래스 평균은 누적 관측이지 검증된 엣지가 아니다(P4·C4).")
    return 0


def due(asof: str | None = None) -> int:
    """재확인일이 지났는데 아직 해소되지 않은 미진입 + 진입조건 없는 레거시."""
    today = _dt.date.fromisoformat(asof) if asof else _dt.date.today()
    recs = load()
    resolved = {(r["ticker"], r["date"]) for r in load_resolutions()}
    if not recs:
        print("[info] 원장 비어있음")
        return 0
    legacy = [r for r in recs if not r.get("enters_if")
              and (r["ticker"], r["date"]) not in resolved]
    overdue = []
    for r in recs:
        if (r["ticker"], r["date"]) in resolved:
            continue
        rc = r.get("recheck_date")
        if rc and _dt.date.fromisoformat(rc) <= today:
            overdue.append((r, (today - _dt.date.fromisoformat(rc)).days))

    print(f"# MISSED LEDGER — 재확인 감사 asof {today.isoformat()}")
    print(f"  전체 {len(recs)}건 · 해소됨 {len(resolved)}건 · "
          f"진입조건 없는 레거시 {len(legacy)}건 · 재확인일 도래/경과 {len(overdue)}건\n")
    if overdue:
        print("## 재확인일이 지났다 — 확인 없이 다음 런으로 넘기지 않는다")
        for r, d in sorted(overdue, key=lambda x: -x[1]):
            print(f"  {r['date']} {r['ticker']} {r['name']:14s} [{r['cls']}] "
                  f"D+{d:<4d} 진입조건: {r['enters_if']}")
    if legacy:
        print("\n## 진입조건이 처음부터 없던 항목 — 영구 미진입으로 방치되면 안 된다")
        for r in legacy:
            print(f"  {r['date']} {r['ticker']} {r['name']:14s} [{r['cls']}] 사유: {r['why']}")
    if not overdue and not legacy:
        print("  확인할 항목 없음 — 모든 미진입이 조건부이고 재확인일이 아직 도래하지 않았다.")
    return 0


def main() -> int:
    utf8_stdout()
    ap = argparse.ArgumentParser(prog="missed_ledger")
    sp = ap.add_subparsers(dest="cmd", required=True)

    a = sp.add_parser("add", help="미진입 1건 기록")
    a.add_argument("--date", required=True, help="검토했으나 사지 않은 날")
    a.add_argument("--ticker", required=True, help="6자리 (접미사 없이)")
    a.add_argument("--name", required=True)
    a.add_argument("--cls", required=True, choices=sorted(CLASSES))
    a.add_argument("--why", required=True)
    a.add_argument("--stage", default="")
    # 거부 원장의 `--revives-if` 와 대칭. 거기서 조건 없는 거부가 원장 최악의 손해였듯
    # (SK이터닉스 +41.2pp), 조건 없는 미진입은 영구 관망이 된다.
    a.add_argument("--enters-if", required=True,
                   help="이 조건이 참이 되면 진입 후보로 되살린다 (필수 — 빈 값 금지)")
    a.add_argument("--recheck-date", required=True,
                   help="이 날짜(YYYY-MM-DD)가 지나면 `due` 가 확인 대상으로 올린다 (필수)")
    # ★ 표본 층(stratum). 이 원장의 클래스 평균이 읽을 수 있는 값이 되려면
    #   '어떻게 뽑혔는지'가 행마다 붙어 있어야 한다. `score` 가 층별로 나눠 집계한다.
    a.add_argument("--sample", default="prospective",
                   choices=["prospective", "random", "outcome_selected"],
                   help="prospective=결정 시점에 사전 기록(기본, 유일하게 편향 없음) · "
                        "random=사후지만 무작위 추출 · outcome_selected=사후 상승 상위에서 추출(편향)")

    s = sp.add_parser("score", help="전체 채점")
    s.add_argument("--json", action="store_true")
    s.add_argument("--floor-jo", type=float, default=1.0)

    d = sp.add_parser("due", help="재확인일 도래/경과 감사")
    d.add_argument("--asof", default=None)

    r = sp.add_parser("resolve", help="해소 기록 — 원장 행은 손대지 않는다(append-only)")
    r.add_argument("--ticker", required=True)
    r.add_argument("--date", required=True, help="원 미진입일(원장의 date 값과 정확히 일치)")
    r.add_argument("--outcome", required=True, choices=["entered", "reaffirmed", "expired"])
    r.add_argument("--note", required=True)

    sp.add_parser("list", help="원장 덤프")

    args = ap.parse_args()

    if args.cmd == "add":
        # 거부 원장과의 중복 방지 — 같은 사건을 두 원장이 각각 세면 합산이 거짓말이 된다
        dup = [x for x in RL.load() if x["ticker"] == args.ticker and x["date"] == args.date]
        if dup:
            print(f"[거부] {args.date} {args.ticker} 는 이미 **거부 원장**에 있다 "
                  f"[{dup[0]['cls']}] — 미진입이 아니라 거부다. reject_ledger 로 채점하라.")
            return 1
        _append(LEDGER, {"date": args.date, "ticker": args.ticker, "name": args.name,
                         "cls": args.cls, "why": args.why, "stage": args.stage,
                         "enters_if": args.enters_if, "recheck_date": args.recheck_date,
                         "sample": args.sample})
        print(f"[ok] {args.date} {args.ticker} {args.name} [{args.cls}] 기록 "
              f"(재확인일 {args.recheck_date}) → {LEDGER}")
        return 0
    if args.cmd == "list":
        for r2 in load():
            print(json.dumps(r2, ensure_ascii=False))
        return 0
    if args.cmd == "due":
        return due(asof=args.asof)
    if args.cmd == "resolve":
        _append(RESOLUTIONS, {"ticker": args.ticker, "date": args.date,
                              "outcome": args.outcome, "note": args.note,
                              "resolved_asof": _dt.date.today().isoformat()})
        print(f"[ok] {args.ticker}({args.date}) → {args.outcome} 기록 (원장 원본 미변경, append-only)")
        return 0
    return score(as_json=args.json, floor_jo=args.floor_jo)


if __name__ == "__main__":
    raise SystemExit(main())
