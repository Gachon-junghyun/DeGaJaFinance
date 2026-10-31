# FILE: scripts/company_score.py
"""COMPANY_SCORE — N개 company 프로토콜(mode research) 평결을 **한 척도로 환산**해 순위를 만든다.

왜 (2026-08-21): 배치로 10기업을 돌리면 리포트 10개가 나오는데, 서로 다른 사람이 쓴 산문 10개는
**비교가 안 된다.** 탑다운 런(industry_us BET)이 그걸 쓰려면 "어느 걸 먼저 볼까"가 기계로 나와야 한다.
이 스크립트는 판단하지 않는다 — `verdict.json` 의 이미 기록된 필드를 **정해진 가중치로 더할 뿐**이다.

⚠ **이 점수는 검증되지 않았다.** 가중치는 사람이 고른 것이고 수익과의 관계는 아직 측정된 적이 없다.
   그래서 `axes` 서브커맨드가 이 점수를 `out/ic/axes/` 로 내보내 **ic_ledger 가 IC 를 적립**하게 한다
   (`axis_inflection`·`axis_window_flow` 와 같은 배관). 그 전까지 이 점수는 **트리아지 순서**지
   기대수익이 아니다. 순위를 근거로 사이징하지 마라 — 사이징은 `kelly_size` 와 SIZE 스테이지 몫이다.

축과 가중치 (합 100) — 전부 verdict.json 에 이미 있는 필드에서만 나온다:
  gate_integrity  25 : G1~G8 중 해당되는 게이트의 통과 비율. FAIL 은 감점이 아니라 분모에 남는다.
  fundamental_mix 30 : 평결의 module_lens 근거 비중(`evidence_mix`) 중 filing+estimates+competition+macro 의 몫.
                       tape(수급·가격·포지셔닝·옵션) 몫은 점수에 안 든다.
  (evidence_grade — 테이프 등급 A=RS·B=KIS·C=OBV — 는 보고 칸으로만 남고 점수에 안 든다.)
  ⚠ 2026-10-31 사람 결정으로 v2: 옛 v1 은 gate 30 + evidence_grade 25 였고 점수의 최대 ~32점이 테이프에서 나왔다.
     장부 첫 학습(공시·실적 근거 6/8 맞음, 수급 5/32)에 맞춰 바꿨다. 점수 시계열이 끊기므로 IC 축 이름도 company_score_v2.
  driver_quality 20 : 드라이버가 이익의 몇 %를 설명하나 × 롤무결성(D2). 설명 못 하면 그만큼 깎인다.
  frame_integrity 10: 최근 다리가 peer set 공유(=섹터 베타)면 0, 종목 고유면 10. (D3)
  reward_risk    15 : upside/|downside| — 1.5 에서 시작해 3.0 에서 만점(그 위는 더 안 준다).

사용:
    python -X utf8 scripts/company_score.py rank --run 2026-08-21
    python -X utf8 scripts/company_score.py rank --run 2026-08-21 --json
    python -X utf8 scripts/company_score.py axes --run 2026-08-21     # → out/ic/axes/{market}_{run}.json
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH_DIR = os.path.join("llm_outputs", "{run}", "company_batch")
AXIS_DIR = os.path.join("out", "ic", "axes")

WEIGHTS = {
    "gate_integrity": 25.0,
    "fundamental_mix": 30.0,
    "driver_quality": 20.0,
    "frame_integrity": 10.0,
    "reward_risk": 15.0,
}
FUNDAMENTAL_BUCKETS = ("filing", "estimates", "competition", "macro")
AXIS_NAME = "company_score_v2"
# 평결이 실제로 방향을 갖는가 — 점수와 **분리해서** 보고한다(점수는 리서치 품질, 이건 행동).
ACTIONABLE = {"ENTER", "ADD"}
HOLDING = {"HOLD", "TRIM"}
EXITING = {"EXIT", "PASS"}


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _f(d: dict, *path, default=None):
    cur = d
    for k in path:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def score_one(v: dict) -> dict:
    """verdict.json 하나 → 축별 점수 + 총점. 결측 축은 **0 이 아니라 None** 으로 두고 분모에서 뺀다.

    ⚠ 결측을 0 으로 세면 '못 잰 것'이 '나쁜 것'이 된다 — 이 리포가 flow_score 에서 이미 당한 함정
    (clip(nan)=+1.0, 2026-08-10). 여기서는 반대로: 잰 축만으로 채점하고 **잰 축 개수를 같이 낸다.**
    """
    parts: dict[str, float | None] = {}

    gates = _f(v, "gates", default={}) or {}
    applicable = {k: b for k, b in gates.items() if b is not None}
    parts["gate_integrity"] = (
        sum(1.0 for b in applicable.values() if b) / len(applicable) * WEIGHTS["gate_integrity"]
        if applicable else None
    )

    mix = _f(v, "evidence_mix")
    if isinstance(mix, dict) and mix:
        fund = sum(float(mix.get(k) or 0) for k in FUNDAMENTAL_BUCKETS)
        parts["fundamental_mix"] = max(0.0, min(fund, 100.0)) / 100.0 * WEIGHTS["fundamental_mix"]
    else:
        parts["fundamental_mix"] = None       # 옛 평결(evidence_mix 없음)은 이 축을 분모에서 뺀다

    cov = _f(v, "driver", "coverage_pct")
    roll = _f(v, "driver", "roll_clean")
    if cov is None or roll is None:
        parts["driver_quality"] = None
    else:
        # 롤이 더러우면(D2 FAIL) 드라이버 축을 절반으로 — 값 자체를 못 믿는다는 뜻이지 0 은 아니다.
        parts["driver_quality"] = min(cov, 100.0) / 100.0 * WEIGHTS["driver_quality"] * (1.0 if roll else 0.5)

    beta_leg = _f(v, "frame", "beta_leg")
    parts["frame_integrity"] = None if beta_leg is None else (0.0 if beta_leg else WEIGHTS["frame_integrity"])

    ratio = _f(v, "rr", "ratio")
    if ratio is None:
        parts["reward_risk"] = None
    else:
        span = max(0.0, min(float(ratio), 3.0) - 1.5) / 1.5
        parts["reward_risk"] = span * WEIGHTS["reward_risk"]

    measured = {k: p for k, p in parts.items() if p is not None}
    denom = sum(WEIGHTS[k] for k in measured)
    raw = sum(measured.values())
    total = (raw / denom * 100.0) if denom else None

    return {
        "ticker": v.get("ticker"),
        "market": (v.get("market") or "").lower(),
        "verdict": v.get("verdict"),
        "parts": parts,
        "tape_grade": (_f(v, "evidence_grade") or "").upper() or None,   # 보고만 — 점수에 안 든다
        "axes_measured": len(measured),
        "axes_total": len(WEIGHTS),
        "coverage_pct_of_scale": round(denom, 1),
        "score": None if total is None else round(total, 1),
        "date": v.get("date"),
        "stop": v.get("stop"),
        "n_alpha": len(_f(v, "set_diff", "alpha_delta", default=[]) or []),
        "n_risk": len(_f(v, "set_diff", "risk_unseen", default=[]) or []),
        "n_obs": len(v.get("observation_points") or []),
        "source": v.get("_path"),
    }


def load_run(run: str) -> list[dict]:
    pat = os.path.join(ROOT, BATCH_DIR.format(run=run), "*", "verdict.json")
    out = []
    for p in sorted(glob.glob(pat)):
        try:
            with open(p, encoding="utf-8") as fh:
                v = json.load(fh)
            v["_path"] = os.path.relpath(p, ROOT)
            out.append(v)
        except Exception as e:  # 깨진 파일은 조용히 넘기지 않는다
            out.append({"ticker": os.path.basename(os.path.dirname(p)), "_error": f"{type(e).__name__}: {e}", "_path": p})
    return out


def cmd_rank(a) -> None:
    raw = load_run(a.run)
    if not raw:
        print(f"# COMPANY_SCORE — {a.run}: verdict.json 0건")
        print(f"  찾은 경로: {BATCH_DIR.format(run=a.run)}/*/verdict.json")
        print("  ⚠ 배치가 안 돌았거나 BET_VERDICT 가 verdict.json 을 안 썼다. 완주 정의를 확인하라.")
        return
    bad = [r for r in raw if r.get("_error")]
    rows = [score_one(r) for r in raw if not r.get("_error")]
    rows.sort(key=lambda r: (r["score"] is None, -(r["score"] or 0)))

    if a.json:
        print(json.dumps({"run": a.run, "weights": WEIGHTS, "rows": rows, "unreadable": bad},
                         ensure_ascii=False, indent=2))
        return

    print(f"# COMPANY_SCORE — run {a.run} · {len(rows)}건 채점" + (f" · 읽기실패 {len(bad)}" if bad else ""))
    print("  ⚠ 이 점수는 **미검증 트리아지 순서**다 — 기대수익 아님. 사이징 근거로 쓰지 마라(SIZE·kelly_size 몫).")
    print()
    print("순위 종목    시장 평결    점수  게이트 실적근거 드라이버 프레임  R/R  잰축  α/risk  관측점")
    print("  " + "─" * 92)
    for i, r in enumerate(rows, 1):
        p = r["parts"]
        def c(k):
            return " —  " if p[k] is None else f"{p[k]:4.1f}"
        sc = " n/a" if r["score"] is None else f"{r['score']:5.1f}"
        print(f"{i:>3}  {str(r['ticker'] or '?'):<7} {r['market']:<4} {str(r['verdict'] or '?'):<7}"
              f"{sc}  {c('gate_integrity')} {c('fundamental_mix')} {c('driver_quality')}"
              f"   {c('frame_integrity')} {c('reward_risk')}  {r['axes_measured']}/{r['axes_total']}"
              f"   {r['n_alpha']}/{r['n_risk']}     {r['n_obs']}")
    print()
    act = [r for r in rows if r["verdict"] in ACTIONABLE]
    hold = [r for r in rows if r["verdict"] in HOLDING]
    exi = [r for r in rows if r["verdict"] in EXITING]
    print(f"  방향별: ENTER/ADD {len(act)} · HOLD/TRIM {len(hold)} · EXIT/PASS {len(exi)}")
    print("  ⚠ 점수는 **리서치 품질**이고 평결은 **행동**이다 — 높은 점수의 PASS 는 '잘 조사해서 안 산다'는 뜻이다.")
    low = [r for r in rows if r["axes_measured"] < 4]
    if low:
        print(f"  🚨 잰 축 4개 미만 {len(low)}건 ({', '.join(str(r['ticker']) for r in low)}) — 척도가 달라 순위 비교 불가.")
    for r in bad:
        print(f"  🚨 읽기실패: {r.get('ticker')} — {r.get('_error')}")


def cmd_axes(a) -> None:
    """점수를 IC 원장 축 파일로 내보낸다 — `axis_inflection`·`axis_window_flow` 와 같은 서식(P1)."""
    rows = [score_one(r) for r in load_run(a.run) if not r.get("_error")]
    by_mkt: dict[str, dict[str, float]] = {}
    for r in rows:
        if r["score"] is None or not r["ticker"]:
            continue
        by_mkt.setdefault(r["market"] or "us", {})[str(r["ticker"])] = r["score"]
    if not by_mkt:
        print("축으로 낼 점수 0건 — 아무것도 쓰지 않았다.")
        return
    os.makedirs(os.path.join(ROOT, AXIS_DIR), exist_ok=True)
    for mkt, vals in by_mkt.items():
        path = os.path.join(ROOT, AXIS_DIR, f"{mkt}_{a.run}.json")
        prev = {}
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    prev = json.load(fh)
            except Exception:
                prev = {}
        prev.setdefault("axes", {})[AXIS_NAME] = vals
        prev["run"] = a.run
        prev["market"] = mkt
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(prev, fh, ensure_ascii=False, indent=2)
        print(f"[axes] {mkt}: {AXIS_NAME} {len(vals)}종목 → {os.path.relpath(path, ROOT)}")
    print("  ⇒ `python -X utf8 scripts/ic_ledger.py log` 가 다음 런에서 이 축의 IC 를 적립한다.")
    print("  ⚠ n_eff<4 면 ic_ledger 는 판정하지 않는다 — 몇 달 쌓여야 부호가 갈린다(설계대로).")


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser(description="company(mode research) 평결 N개 → 한 척도 환산(v2)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("rank", help="점수 순위표")
    r.add_argument("--run", required=True, help="YYYY-MM-DD (llm_outputs/{run}/company_batch/)")
    r.add_argument("--json", action="store_true")
    r.set_defaults(func=cmd_rank)
    x = sub.add_parser("axes", help="점수를 ic_ledger 축 파일로 내보내기")
    x.add_argument("--run", required=True)
    x.set_defaults(func=cmd_axes)
    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
