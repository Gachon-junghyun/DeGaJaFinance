# -*- coding: utf-8 -*-
"""민감도 원장 (§4.8 b) — "이 종목은 뭐에 민감한가"를 축적·검증.

sensitivity/{id}.json(기계 source) + {id}.md(사람 뷰). factor별 방향/탄력·근거이벤트·신뢰도·갱신일.
갱신 규칙: catalyst 발화 → 실제 가격반응 관측 → 탄력·신뢰도 update(사후검증 = alert-postmortem 패턴).
bayes 충돌평가가 factor_confidence()로 학습된 신뢰도를 끌어 쓴다.
"""
from __future__ import annotations

import json
import re
from datetime import datetime

from ._config import SENSITIVITY_DIR, canon, utf8_stdout


def _paths(code: str):
    return SENSITIVITY_DIR / f"{code}.json", SENSITIVITY_DIR / f"{code}.md"


def load(code: str) -> dict:
    j, _ = _paths(code)
    if j.exists():
        try:
            return json.loads(j.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"ticker": code, "factors": {}}


def _tokens(s: str) -> set[str]:
    """factor/axis 매칭용 토큰 — 괄호주석 제거 + 2자+ 한글/영문 조각."""
    base = re.sub(r"\(.*?\)", "", s)
    return {t for t in re.split(r"[\s/·,]+", base) if len(t) >= 2}


def factor_confidence(code: str, axis: str, default: float = 0.5) -> float:
    """axis(신호명)를 원장 factor와 퍼지 매칭 → 학습된 신뢰도. 없으면 default(중립)."""
    led = load(code)
    a_tok = _tokens(axis)
    best, best_conf = 0, default
    for factor, info in led.get("factors", {}).items():
        overlap = len(a_tok & _tokens(factor))
        if overlap > best:
            best, best_conf = overlap, float(info.get("conf", default))
    return best_conf


def update(code: str, factor: str, direction: str, event: str, conf: float,
           updated: str | None = None) -> dict:
    """factor 민감도 추가/갱신. updated 미지정 시 오늘."""
    SENSITIVITY_DIR.mkdir(parents=True, exist_ok=True)
    led = load(code)
    led["ticker"] = code
    led.setdefault("factors", {})[factor] = {
        "dir": direction, "event": event, "conf": float(conf),
        "updated": updated or datetime.now().strftime("%Y-%m-%d"),
    }
    j, m = _paths(code)
    j.write_text(json.dumps(led, ensure_ascii=False, indent=2), encoding="utf-8")
    m.write_text(render(led), encoding="utf-8")
    return led


def render(led: dict) -> str:
    L = [f"# sensitivity/{led.get('ticker')} — 민감도 원장", "",
         "| factor | 방향/탄력 | 근거 이벤트 | 신뢰도 | 최근갱신 |", "|---|---|---|---|---|"]
    for factor, i in sorted(led.get("factors", {}).items(), key=lambda x: -float(x[1].get("conf", 0))):
        L.append(f"| {factor} | {i.get('dir','')} | {i.get('event','')} | {i.get('conf')} | {i.get('updated','')} |")
    L.append("")
    L.append("_갱신규칙: catalyst 발화→실제 가격반응 관측→탄력·신뢰도 update(사후검증)._")
    return "\n".join(L)


def cli_register(sub) -> None:
    p = sub.add_parser("sensitivity", help="종목별 민감도 원장 조회/갱신")
    p.add_argument("ticker")
    p.add_argument("--add", metavar="FACTOR", help="추가/갱신할 factor 이름")
    p.add_argument("--dir", default="+중", help="방향/탄력 (예: +강/+중/무)")
    p.add_argument("--event", default="", help="근거 이벤트")
    p.add_argument("--conf", type=float, default=0.5, help="신뢰도 0~1")
    p.add_argument("--date", default=None, help="갱신일 YYYY-MM-DD (기본 오늘)")
    p.set_defaults(func=lambda a: _run_cli(a))


def _run_cli(a) -> None:
    utf8_stdout()
    code = canon(a.ticker)
    if a.add:
        led = update(code, a.add, a.dir, a.event, a.conf, a.date)
        print(f"갱신: {code} · {a.add} (신뢰도 {a.conf})")
        print(render(led))
    else:
        led = load(code)
        if not led.get("factors"):
            print(f"{code} 민감도 원장 비어있음 — --add 로 factor 추가.")
        else:
            print(render(led))
