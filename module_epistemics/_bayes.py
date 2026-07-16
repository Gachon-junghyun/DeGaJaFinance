# -*- coding: utf-8 -*-
"""베이지안 충돌평가 (§4.8 a) — 신호가 모순일 때 손퉁 금지, 구조화.

prior P + 신호별 LR(우도비) × 신뢰도(민감도 원장에서) → posterior + 지배축(argmax LR×신뢰도).
"어떤 지표가 주가를 더 크게 움직이나" = LR×신뢰도 열이 답. 신뢰도는 종목별 학습값(_sensitivity).
결정론 계산 — 판단(신호·방향·LR)은 상위가 넣고, 여기선 합성만.
"""
from __future__ import annotations

import json

from ._config import canon, utf8_stdout
from ._sensitivity import factor_confidence


def _odds(p: float) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)
    return p / (1 - p)


def adjudicate(thesis: str, ticker: str, signals: list[dict], prior: float = 0.5) -> dict:
    """signals = [{axis, dir(+/-), lr, conf?}]. conf 없으면 민감도 원장에서 조회.

    베이즈: posterior_odds = prior_odds × Π (신호별 조정 LR).
    조정 LR = dir 방향으로 lr^conf (신뢰도가 낮으면 1로 수렴 = 영향 약화).
    지배축 = argmax(|log LR| × conf).
    """
    code = canon(ticker)
    post_odds = _odds(prior)
    rows = []
    for s in signals:
        axis = s["axis"]
        direction = 1 if str(s.get("dir", "+")).startswith("+") else -1
        lr = float(s.get("lr", 1.0))
        conf = s.get("conf")
        if conf is None:
            conf = factor_confidence(code, axis)   # 원장에서 학습된 신뢰도
        conf = float(conf)
        # 방향 반영 + 신뢰도 가중(conf=0이면 영향 0=LR 1)
        eff = lr ** conf if direction > 0 else (1.0 / lr) ** conf
        post_odds *= eff
        weight = abs(__import__("math").log(max(lr, 1e-6))) * conf
        rows.append({"axis": axis, "dir": "+" if direction > 0 else "-",
                     "lr": round(lr, 2), "conf": round(conf, 2),
                     "eff": round(eff, 3), "weight": round(weight, 3)})

    posterior = post_odds / (1 + post_odds)
    dominant = max(rows, key=lambda r: r["weight"]) if rows else None
    # 잔여충돌 = 방향이 갈리는 신호쌍(하나라도 +와 - 공존)
    dirs = {r["dir"] for r in rows}
    residual = len(dirs) > 1

    return {
        "thesis": thesis, "ticker": code, "prior": round(prior, 3),
        "posterior": round(posterior, 3),
        "dominant_axis": dominant["axis"] if dominant else None,
        "signals": rows, "residual_conflict": residual,
    }


def render(res: dict) -> str:
    L = [f"## 베이지안 충돌 — {res['ticker']} thesis:\"{res['thesis']}\"",
         f"prior P={res['prior']}",
         "| 신호(axis) | 방향 | LR | 신뢰도 | 기여 |", "|---|---|---|---|---|"]
    for r in res["signals"]:
        arrow = ("↑↑" if r["weight"] >= 0.5 else "↑") if r["dir"] == "+" else ("↓↓" if r["weight"] >= 0.5 else "↓")
        if abs(r["lr"] - 1.0) < 1e-9:
            arrow = "·"
        L.append(f"| {r['axis']} | {r['dir']} | {r['lr']} | {r['conf']} | {arrow} |")
    L.append(f"posterior P={res['posterior']} → 지배축 = **{res['dominant_axis']}** (argmax LR×신뢰도)")
    if res["residual_conflict"]:
        L.append("잔여충돌 = 방향 상충 신호 존재 → 실측(--investor 등)으로 해소 필요")
    return "\n".join(L)


def cli_register(sub) -> None:
    p = sub.add_parser("adjudicate", help="베이지안 충돌평가 → posterior + 지배축")
    p.add_argument("ticker")
    p.add_argument("--thesis", required=True)
    p.add_argument("--prior", type=float, default=0.5)
    p.add_argument("--signals", required=True,
                   help='JSON 리스트 [{"axis":..,"dir":"+","lr":2.1,"conf":0.85}] (conf 생략시 원장조회)')
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=lambda a: _run_cli(a))


def _run_cli(a) -> None:
    utf8_stdout()
    signals = json.loads(a.signals)
    res = adjudicate(a.thesis, a.ticker, signals, prior=a.prior)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(render(res))
