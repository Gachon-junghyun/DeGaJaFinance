# -*- coding: utf-8 -*-
"""ic_ledger — 신호 축의 **정보계수(IC)를 매일 1행씩 적립**한다.

왜 있나 (2026-07-31 실측)
------------------------
이 리포는 실력을 **11개 포지션의 손익**으로 배우려 했다. 그러면 월 11관측이고,
IC 0.06 을 t=2 로 검출하는 데 **수십 년**이 걸린다 — 사실상 영원히 모른다.

같은 신호를 **횡단면으로** 재면 관측 1개 = **하루**다. `sector_flow` 는 이미 매일 828종목에
점수를 매긴다. 그 랭킹이 다음 세션 수익을 예측했는지 재면 **하루에 IC 관측 1개**가 쌓인다.
⇒ **시계가 75배 빨라진다.** 실측(런 15개):

| 축 | 지금 n | t=2 까지 필요 n | 소요 |
|---|---|---|---|
| `vol_surge` | 14 | 14 | **이미 도달** |
| `rs60` | 13 | 80 | 4개월 |
| `rs20` | 9 | 67 | 3개월 |
| `obv_norm` | 9 | 114 | 5개월 |

**"이 데스크의 축에 신호가 있나"는 16년이 아니라 3~5개월 문제다.** 이 파일이 그 시계다.

첫 관측 (2026-07-31, 런 15개)
-----------------------------
`flow_score` +0.022 (t +0.35) · `obv_norm` +0.022 (t +0.54) · `rs20` +0.053 (t +0.73) ·
`rs60` +0.045 (t +0.81) — **전부 구분 불가**. 유일하게 부호가 선 것은
**`vol_surge` −0.044 (t −2.01, 양수 29%)** 이고 **h=5 에서도 −0.046 (t −1.91) 으로 같은 부호**다.
⇒ 거래량 급증 상위가 다음 세션 **더 빠졌다**. 🟢 판정은 이걸 **양의 가중**으로 쓰고 있다.
⚠ 다중비교: 10개 검정 중 1개라 Bonferroni 임계는 |t|>2.8 — **확정 아님.** 그리고 창이
−27% 폭락 구간이라 "거래량 급증 = 패닉"이 레짐 특성일 수 있다. `score` 가 두 경고를 매번 찍는다.
⚠ M224(스윕 4축 ρ −0.21~+0.19, n=22)와 **독립적으로 같은 방향** — 두 번째 측정이 첫 번째와 일치.

설계 원칙
---------
- **해소되는 대로 적립한다.** 런 d 의 지평 h IC 는 d+h 봉이 정착해야 계산된다. `log` 는
  "이제 계산 가능해진 (런 × 축 × 지평)" 전부를 채운다 — 오늘치만 보는 게 아니다.
- **미정착 봉은 쓰지 않는다**(D74). 장중이면 오늘 종가로 해소되는 칸은 건너뛴다.
- **가격은 `sector_flow` 캐시 재사용**(P1) — yfinance 를 다시 때리지 않는다.
- P4: 판정하지 않는다. IC 와 t 와 **필요 표본수**만 낸다.

CLI
---
  python -X utf8 scripts/ic_ledger.py log                # 해소 가능한 칸 전부 적립(멱등)
  python -X utf8 scripts/ic_ledger.py score              # 축×지평 IC 시계열 + 다중비교 + 필요 n
  python -X utf8 scripts/ic_ledger.py score --json
  python -X utf8 scripts/ic_ledger.py show --tail 20
  python -X utf8 scripts/ic_ledger.py log --market us    # US 스윕 (SECTOR_FLOW_US.json)
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import glob
import json
import os
import sys

import _repo_path  # noqa: F401

LEDGER = os.path.join("out", "ic", "ledger.csv")
AXES = ["flow_score", "obv_norm", "rs20", "rs60", "vol_surge"]
HORIZONS = [1, 5, 10]
MIN_NAMES = 50
FIELDS = ["run_date", "market", "axis", "horizon", "ic", "n_names", "resolved_date", "asof_cache"]


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def kr_session_now() -> bool:
    now = _dt.datetime.now()
    return now.weekday() < 5 and _dt.time(9, 0) <= now.time() <= _dt.time(15, 30)


# ── 원장 ────────────────────────────────────────────────────────────────
def load() -> list[dict]:
    if not os.path.exists(LEDGER):
        return []
    with open(LEDGER, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write(rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    rows = sorted(rows, key=lambda r: (r["run_date"], r["axis"], int(r["horizon"])))
    with open(LEDGER, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


# ── 계산 ────────────────────────────────────────────────────────────────
def _prices(market: str):
    """`sector_flow` 가 이미 받아둔 캐시 재사용(P1) — reject_ledger 와 같은 원본."""
    import pandas as pd

    pat = "prices_kr_*.pkl" if market == "kr" else "prices_2*.pkl"
    caches = sorted(glob.glob(os.path.join("llm_outputs", "sector_flow", pat)))
    if not caches:
        raise SystemExit(f"[err] 가격 캐시 없음({pat}) — sector_flow --market {market} 를 먼저 돌려라")
    cl = pd.read_pickle(caches[-1]).xs("Close", axis=1, level=1)
    cl.index = [d.date() for d in cl.index]
    return cl, os.path.basename(caches[-1])


def _nw_t(a, max_lag: int) -> float:
    """Newey-West 보정 t. **겹치는 선행창을 독립으로 세지 않기 위한 최소 장치.**

    ⚠ 이 함수가 없어서 이 스크립트가 처음 돌 때 **거짓 양성**을 냈다(2026-07-31 실측):
    h=10 칸이 `n=3 · 양수 100% · t=+6.7` 로 나왔는데, 그 3개 창은 **전부 07-31 반등 하나로
    끝난다** — 같은 사건을 세 번 센 것이다. 겹침 보정 없이 일별 런의 h일 선행 IC 를 모으면
    자기상관이 t 를 통째로 부풀린다. lag = h−1 로 보정한다.
    ⚠ 그래도 n 이 작으면 NW 자체가 못 믿는다 — 그래서 `n_eff = n/h` 를 같이 낸다.
    """
    import numpy as np

    a = np.asarray(a, float)
    n = len(a)
    if n < 3:
        return 0.0
    m = a.mean()
    e = a - m
    g0 = float((e * e).sum() / n)
    s = g0
    for L in range(1, min(max_lag, n - 1) + 1):
        g = float((e[L:] * e[:-L]).sum() / n)
        s += 2.0 * (1.0 - L / (max_lag + 1.0)) * g
    if s <= 0:
        return 0.0
    return float(m / np.sqrt(s / n))


def _spearman(a, b) -> float:
    import numpy as np
    import pandas as pd

    ra = pd.Series(a).rank().to_numpy()
    rb = pd.Series(b).rank().to_numpy()
    if len(ra) < MIN_NAMES or np.std(ra) == 0 or np.std(rb) == 0:
        return float("nan")
    return float(np.corrcoef(ra, rb)[0, 1])


AXIS_DIR = os.path.join("out", "ic", "axes")


def load_extra_axes(market: str, run: str) -> dict[str, dict]:
    """외부 패턴 모듈이 기여한 축을 읽는다 — **이 원장을 공용 점수판으로 만드는 부분.**

    서식: `out/ic/axes/{market}_{run}.json` = {"축이름": {"티커": 점수, ...}, ...}

    왜 파일인가: 패턴 발견기는 앞으로 계속 늘어난다(변곡·경제레짐·군중심리…). 그때마다
    `ic_ledger` 를 고치면 이 파일이 모든 생산자를 아는 신이 된다. **생산자가 파일을 쓰고
    원장은 읽기만 한다** — 축을 추가하는 데 이 스크립트 수정이 0 이어야 한다.
    ⚠ 발견기는 **거짓 패턴을 대량 생산한다**(828종목 × 지표 × 지평이면 t>2 가 우연히 수십 개).
    그래서 순서가 중요하다: **눈금자를 먼저 놓고 발견기를 붙인다.** 이 파일이 그 눈금자다.
    """
    p = os.path.join(AXIS_DIR, f"{market}_{run}.json")
    if not os.path.exists(p):
        return {}
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception:                                       # noqa: BLE001
        return {}
    return {k: v for k, v in d.items() if isinstance(v, dict) and not k.startswith("_")}


def cmd_log(args) -> int:
    import numpy as np

    mk = args.market
    folder = "industry_KR" if mk == "kr" else "industry_US"
    fname = "SECTOR_FLOW_KR.json" if mk == "kr" else "SECTOR_FLOW_US.json"
    cl, cache = _prices(mk)
    files = sorted(glob.glob(os.path.join("llm_outputs", "*", folder, fname)))
    have = {(r["run_date"], r["market"], r["axis"], r["horizon"]) for r in load()}
    rows = load()
    added = skipped_live = 0
    today = _dt.date.today()
    live = kr_session_now() and mk == "kr"

    for f in files:
        run = os.path.basename(os.path.dirname(os.path.dirname(f)))
        try:
            rd = _dt.date.fromisoformat(run)
        except ValueError:
            continue
        idx = [i for i, x in enumerate(cl.index) if x >= rd]
        if not idx:
            continue
        i0 = idx[0]
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:                                   # noqa: BLE001
            continue
        names = [n for n in d.get("names", []) if n.get("ticker") in cl.columns]
        if len(names) < MIN_NAMES:
            continue
        tks = [n["ticker"] for n in names]
        # 외부 패턴 축을 같은 종목 순서로 정렬해 붙인다(없으면 그냥 비어 있다)
        extra = load_extra_axes(mk, run)
        for axname, scores in extra.items():
            for n in names:
                n[axname] = scores.get(n["ticker"])
        axes = AXES + sorted(extra)
        for h in HORIZONS:
            if i0 + h >= len(cl.index):
                continue
            rdate = cl.index[i0 + h]
            if live and rdate == today:                     # D74 — 미정착 봉으로 해소하지 않는다
                skipped_live += 1
                continue
            p0 = cl.iloc[i0][tks].to_numpy(float)
            p1 = cl.iloc[i0 + h][tks].to_numpy(float)
            fwd = p1 / p0 - 1.0
            for ax in axes:
                key = (run, mk, ax, str(h))
                if key in have:
                    continue
                v = np.array([n.get(ax) if n.get(ax) is not None else np.nan for n in names], float)
                ok = ~(np.isnan(v) | np.isnan(fwd))
                if ok.sum() < MIN_NAMES:
                    continue
                ic = _spearman(v[ok], fwd[ok])
                if ic != ic:                                # nan
                    continue
                rows.append({"run_date": run, "market": mk, "axis": ax, "horizon": h,
                             "ic": round(ic, 5), "n_names": int(ok.sum()),
                             "resolved_date": rdate.isoformat(), "asof_cache": cache})
                have.add(key)
                added += 1
    write(rows)
    print(f"[ok] {added}행 신규 적립 → {LEDGER} (총 {len(rows)}행 · market={mk})")
    if skipped_live:
        print(f"  ⚠ 미정착 봉으로 해소되는 칸 {skipped_live}개 건너뜀(D74) — 종가 후 다시 돌리면 채워진다")
    if added == 0:
        print("  (새로 해소된 칸 없음 — 다음 런/세션이 지나야 늘어난다)")
    return 0


def cmd_score(args) -> int:
    import numpy as np

    rows = [r for r in load() if r["market"] == args.market]
    if not rows:
        print(f"[info] 원장 비어있음 — `log` 를 먼저 실행 ({LEDGER})")
        return 0
    cells = {}
    for r in rows:
        cells.setdefault((r["axis"], int(r["horizon"])), []).append(float(r["ic"]))

    out = []
    for (ax, h), v in sorted(cells.items()):
        a = np.array(v, float)
        if len(a) < 3:
            continue
        m, sd = float(a.mean()), float(a.std(ddof=1))
        t_raw = m / (sd / np.sqrt(len(a))) if sd > 0 else 0.0
        t_nw = _nw_t(a, h - 1)
        n_eff = max(1.0, len(a) / h)          # 겹치지 않는 창 수의 근사
        need = (2 * sd / abs(m)) ** 2 if abs(m) > 1e-9 else float("inf")
        out.append({"axis": ax, "horizon": h, "n": len(a), "n_eff": round(n_eff, 1),
                    "mean_ic": round(m, 5), "sd": round(sd, 5),
                    "t": round(t_nw, 3), "t_raw": round(t_raw, 3),
                    "pos_rate": round(float((a > 0).mean()), 3),
                    "n_needed": None if need == float("inf") else int(round(need))})
    k = len(out)
    bonf = 2.8 if k >= 10 else (2.5 if k >= 5 else 2.0)

    if args.json:
        print(json.dumps({"market": args.market, "n_tests": k, "bonferroni_t": bonf,
                          "cells": out}, ensure_ascii=False, indent=2))
        return 0

    print(f"# IC LEDGER — {args.market.upper()} · 검정 {k}개 · 원장 {len(rows)}행")
    print("  IC = 그날 랭킹 vs 선행수익의 횡단면 스피어만. **관측 1개 = 런 1개**(종목 수 아님, 규칙 S1).\n")
    print(f"{'축':13s} {'지평':>4} {'n':>3} {'n_eff':>6} {'평균IC':>9} {'t(NW)':>7} {'t(raw)':>7} "
          f"{'양수':>6} {'필요n':>7}  판정")
    for c in sorted(out, key=lambda x: -abs(x["t"])):
        if c["n_eff"] < 4:
            v = "🚨n_eff<4 — 판정 불가(겹침)"
        elif abs(c["t"]) > bonf:
            v = "★유의(다중비교 통과)"
        elif abs(c["t"]) > 2:
            v = "유의(단독기준)"
        else:
            v = "구분 불가"
        nn = "—" if c["n_needed"] is None else f"{c['n_needed']}"
        print(f"{c['axis']:13s} {c['horizon']:>4} {c['n']:>3} {c['n_eff']:>6.1f} "
              f"{c['mean_ic']:>+9.4f} {c['t']:>+7.2f} {c['t_raw']:>+7.2f} "
              f"{c['pos_rate']*100:>5.0f}% {nn:>7}  {v}")
    print("\n⚠ **겹침 보정**: 일별 런의 h일 선행창은 서로 겹친다 ⇒ t 는 Newey-West(lag h−1),")
    print("   `n_eff = n/h` 는 겹치지 않는 창 수의 근사다. **n_eff<4 면 판정하지 않는다.**")
    print("   실측 2026-07-31: 보정 전 h=10 이 `n=3·양수100%·t=+6.7` 로 나왔는데 그 3개 창은")
    print("   **전부 07-31 반등 하나로 끝났다** — 같은 사건을 세 번 센 것이다.")

    print(f"\n⚠ **다중비교**: 검정 {k}개를 동시에 봤다. 단독 |t|>2 는 {k}개 중 "
          f"{k*0.05:.1f}개가 우연히 나온다 ⇒ **Bonferroni 임계 |t|>{bonf}** 를 쓴다.")
    print("⚠ **두 지평 부호 일치**를 같이 보라(D105) — 한 지평만 유의한 것은 지평 의존일 수 있다.")
    sign = {}
    for c in out:
        sign.setdefault(c["axis"], []).append((c["horizon"], c["mean_ic"]))
    cons = [a for a, v in sign.items() if len(v) > 1 and len({x[1] > 0 for x in v}) == 1]
    print(f"   두 지평 이상에서 부호가 같은 축: {cons or '없음'}")
    print("⚠ **레짐**: 이 창이 어떤 국면이었는지 적어라. 폭락장의 IC 는 평시로 일반화되지 않는다.")
    print("\n  이 표의 목적은 판정이 아니라 **시계**다 — `t=2까지 필요n` 이 축을 언제 죽이거나")
    print("  살릴지 알려준다. 하루 1관측이므로 필요n ÷ 21 ≈ 개월 수다.")
    return 0


def cmd_show(args) -> int:
    rows = [r for r in load() if r["market"] == args.market]
    if not rows:
        print("[info] 원장 비어있음")
        return 0
    tail = rows[-args.tail:]
    print(f"# IC LEDGER — {len(rows)}행 (표시 {len(tail)})  {LEDGER}")
    print(f"{'런':11s} {'축':13s} {'지평':>4} {'IC':>9} {'종목':>5} {'해소일':11s}")
    for r in tail:
        print(f"{r['run_date']:11s} {r['axis']:13s} {r['horizon']:>4} "
              f"{float(r['ic']):>+9.4f} {r['n_names']:>5} {r['resolved_date']:11s}")
    return 0


def main() -> int:
    utf8_stdout()
    ap = argparse.ArgumentParser(prog="ic_ledger")
    sp = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in (("log", cmd_log), ("score", cmd_score), ("show", cmd_show)):
        p = sp.add_parser(name)
        p.add_argument("--market", choices=["kr", "us"], default="kr")
        if name == "score":
            p.add_argument("--json", action="store_true")
        if name == "show":
            p.add_argument("--tail", type=int, default=20)
        p.set_defaults(func=fn)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
