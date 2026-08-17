"""타임폴리오 콘테스트 타깃 산출 → 매매 계획.

★ 2026-07-31 SSOT 컷오버 (F4, 사람 결정)
----------------------------------------
**콘테스트 계좌 자체가 SSOT다. 중간 장부는 없앴다.**

이전 구조는 옛 mvp 리포의 `alert_bot` 책(id=6 '한국모의')을 읽어 그 시가비중을 콘테스트에
미러링했다. 두 가지가 동시에 깨져 있었다:

1. **구조적 불능** — `from alert_bot import alert_db` 는 이 리포에 존재하지 않는다(자립 리포, P5).
   `plan`·`sync` 가 **ModuleNotFoundError 로 크래시**했고, 그 침묵이 **9거래일**을 숨겼다.
2. **설계 결함(F5)** — `book_targets()` 는 **투자 슬리브 비중만** 냈다. 현금은 어느 층에서도
   결정 변수가 아니어서, 책이 41% 투자면 콘테스트도 영원히 41% 였다.
   실측 2026-07-31: 책 id=6 **투자 41.09%** vs 콘테스트 **52.9%** — 콘테스트는 그날 움직였고
   책은 07-24 에 멈춰 있었다. 미러가 살아났다면 콘테스트를 **41% 로 되돌렸을 것이다.**

지금 구조 — 타깃은 두 곳에서 온다:
  · **얼마나 투자할 것인가(현금 총량)** = `scripts/exposure_rule.py` (규칙·사람이 정한 밴드)
  · **무엇을 담을 것인가(이름과 상대비중)** = 데스크가 쓴 인텐트 파일
그 둘을 곱해 절대 타깃을 만들고, 콘테스트 현재 보유와의 차이만 주문한다.
**현금은 이제 명시 타깃이다** — `apply_exposure_rule` 이 `_cash` 항목으로 돌려준다.

★ 이 계층은 '무엇을'만 결정한다. 실제 제출 arming 은 상위에서.
⚠ 조용한 폴백 금지 — 인텐트가 없거나 규칙이 밴드미설정이면 **계획을 내지 않고 소리 내어 멈춘다.**
   조용한 실패가 이 결함을 9일간 숨겼다.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from dataclasses import dataclass
from typing import Optional

INTENTS = os.path.join("out", "timefolio", "targets.json")


def code6(ticker: str) -> str:
    """'067310.KQ' → '067310'."""
    return ticker.split(".")[0].strip().zfill(6)


@dataclass
class TradePlan:
    code: str
    name: str
    side: str            # buy | sell
    order_weight: float  # 주문 비중(%) = |target-current|
    target_w: float
    current_w: float
    reason: str = ""


class SyncBlocked(RuntimeError):
    """계획을 낼 수 없는 상태. 삼키지 말고 그대로 올려라(조용한 폴백 금지)."""


def book_targets(*_a, **_kw):
    """★ 은퇴함 (2026-07-31 F4 컷오버). 호출되면 조용히 죽지 말고 이유를 말하고 죽는다."""
    raise SyncBlocked(
        "book_targets() 는 은퇴했다 — 옛 mvp `alert_bot` 책(id=6) 의존은 2026-07-31 에 끊겼다(F4).\n"
        "  콘테스트 계좌가 SSOT 다. 타깃은 이제 두 조각으로 온다:\n"
        "   · 투자 총량 = scripts/exposure_rule.py target --json (사람이 정한 밴드)\n"
        f"   · 종목·상대비중 = {INTENTS} (데스크가 쓴 인텐트)\n"
        "  → targets_from_intents() + apply_exposure_rule() 를 써라."
    )


def targets_from_intents(path: str = INTENTS) -> dict[str, dict]:
    """데스크가 쓴 인텐트 파일 → {code6: {name, weight}}.

    서식:
      {"_asof": "2026-07-31", "_source": "industry_kr BET_SHEET 2026-07-31",
       "names": {"005930": {"name": "삼성전자", "weight": 9.9}, ...}}
    `weight` 는 **상대치로 취급**되어 노출 규칙의 투자 총량에 맞춰 재정규화된다.
    """
    if not os.path.exists(path):
        raise SyncBlocked(
            f"인텐트 파일이 없다: {path}\n"
            "  콘테스트가 SSOT 라는 것은 '무엇을 담을지'를 데스크가 명시해야 한다는 뜻이다.\n"
            "  BET_SHEET 를 읽고 이 파일을 쓰기 전에는 계획을 내지 않는다(P4 — 알아야 말한다)."
        )
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    names = d.get("names") or {}
    if not names:
        raise SyncBlocked(f"{path} 의 `names` 가 비었다 — 빈 계획과 '전량 청산'은 다르다.")
    return {code6(k): {"name": v.get("name", k), "weight": float(v["weight"])}
            for k, v in names.items()}


def exposure_target(repo_root: str | None = None) -> dict:
    """노출 규칙에서 투자·현금 목표비중을 받는다 — **현금 타깃의 단일 원본**(F5).

    규칙을 재구현하지 않고 그 CLI 를 부른다(P1). 밴드 미설정이면 막는다.
    """
    root = repo_root or os.getcwd()
    out = subprocess.run(
        [sys.executable, "-X", "utf8", os.path.join("scripts", "exposure_rule.py"),
         "target", "--json"],
        cwd=root, capture_output=True, text=True, encoding="utf-8",
    )
    if out.returncode != 0:
        raise SyncBlocked(f"exposure_rule target 실패:\n{out.stderr.strip()[:500]}")
    d = json.loads(out.stdout[out.stdout.index("{"):])
    if not d.get("bands_set") or d.get("invested_target_pct") is None:
        raise SyncBlocked(
            "노출 밴드가 설정되지 않았다(data/exposure_bands.json) — 투자 총량을 모른다.\n"
            "  밴드 없이 비중을 정하는 것은 규칙이 아니라 즉흥이다(P5). 계획을 내지 않는다."
        )
    return d


# 콘테스트 종목별 비중 상한 (가이드라인 — `timefolio-close-check` SKILL 이 같은 값을 검사한다).
# ⚠ 여기 없는 규정(시총 1조 미만 합계 30%)은 유니버스 데이터가 필요해 LIVENESS 쪽이 본다.
NAME_CAP_DEFAULT = 15.0
NAME_CAP = {"005930": 40.0}


def _apply_caps(w: dict[str, float]) -> tuple[dict[str, float], list[str]]:
    """종목별 상한을 걸고 초과분을 여유 있는 종목에 비례 재배분한다.

    ⚠ 왜 필요한가: 재정규화는 상한을 모른다. 투자 목표가 90% 인데 종목이 7개 미만이면
    **균등 배분만으로도 15% 상한을 깬다**(실측 산술). `build_plan` 에는 가드가 없었으므로
    규정 위반 주문을 그대로 제안했을 것이다 — 콘테스트 누적 위반은 이미 1건이다.
    ⚠ 조용히 깎지 않는다. 깎인 내역을 문자열로 돌려주고 호출부가 반드시 출력한다.
    """
    w = dict(w)
    notes: list[str] = []
    for _ in range(10):                       # 재배분이 다른 종목을 상한 위로 밀 수 있어 반복
        over = {k: v - min(v, NAME_CAP.get(k, NAME_CAP_DEFAULT)) for k, v in w.items()}
        excess = sum(x for x in over.values() if x > 0)
        if excess < 0.01:
            break
        for k, x in over.items():
            if x > 0:
                notes.append(f"{k} {w[k]:.2f}%→{NAME_CAP.get(k, NAME_CAP_DEFAULT):.2f}% (상한)")
                w[k] -= x
        room = {k: NAME_CAP.get(k, NAME_CAP_DEFAULT) - v for k, v in w.items()
                if NAME_CAP.get(k, NAME_CAP_DEFAULT) - v > 0.01}
        tot = sum(room.values())
        if tot < 0.01:
            notes.append(f"⚠재배분 불가 — {excess:.2f}%p 가 현금으로 남는다(종목 수 부족)")
            break
        for k, r in room.items():
            w[k] += excess * r / tot
    return {k: round(v, 2) for k, v in w.items()}, notes


def apply_exposure_rule(targets: dict[str, dict], exp: dict) -> dict[str, dict]:
    """인텐트의 상대비중을 노출 규칙의 투자 총량에 맞춰 재정규화 + **현금을 명시 항목으로**.

    F5 가 지적한 것이 정확히 이 지점이다: 예전엔 종목 비중만 나오고 현금은 '나머지'였다.
    이제 현금은 `_cash` 로 **계산되어 나온다** — 규칙이 정한 값이지 잔여물이 아니다.
    """
    inv = float(exp["invested_target_pct"])
    tot = sum(v["weight"] for v in targets.values())
    if tot <= 0:
        raise SyncBlocked("인텐트 비중 합이 0 이다.")
    raw = {k: v["weight"] / tot * inv for k, v in targets.items()}
    capped, cap_notes = _apply_caps(raw)
    out = {k: {**targets[k], "weight": capped[k]} for k in targets}
    placed = sum(capped.values())
    out["_cash"] = {"name": "현금", "weight": round(100.0 - placed, 2),
                    "state": exp["state"], "asof": exp["asof"],
                    "bar_status": exp.get("bar_status", ""),
                    "cap_notes": cap_notes,
                    "_note": ("규칙 현금목표 %.2f%%" % (100.0 - inv)) +
                             ("" if not cap_notes else
                              " / 상한 재배분 후 실제 현금 %.2f%%" % (100.0 - placed))}
    return out


def build_plan(targets: dict[str, dict], holdings: list, *, min_drift: float = 0.5) -> list[TradePlan]:
    """타깃 vs 현재(콘테스트 보유) diff → 매매 계획. `_cash` 는 주문 대상이 아니라 결과다."""
    tg = {k: v for k, v in targets.items() if not k.startswith("_")}
    current = {h.code: h.weight for h in holdings}
    names = {h.code: h.name for h in holdings}
    plans: list[TradePlan] = []
    for code in sorted(set(tg) | set(current)):
        tgt = tg.get(code, {}).get("weight", 0.0)
        cur = current.get(code, 0.0)
        drift = round(tgt - cur, 2)
        if abs(drift) < min_drift:
            continue
        name = tg.get(code, {}).get("name") or names.get(code, code)
        plans.append(TradePlan(
            code=code, name=name,
            side="buy" if drift > 0 else "sell",
            order_weight=abs(drift), target_w=tgt, current_w=cur,
            reason=("신규/증량" if drift > 0 and cur == 0 else
                    "증량" if drift > 0 else
                    "청산" if tgt == 0 else "감량"),
        ))
    return plans


def plan_targets(*, intents_path: str = INTENTS) -> tuple[dict[str, dict], dict]:
    """인텐트 + 노출규칙 → 절대 타깃. 어느 쪽이든 막히면 SyncBlocked 를 그대로 올린다."""
    exp = exposure_target()
    return apply_exposure_rule(targets_from_intents(intents_path), exp), exp


def sync(tf, *, min_drift: float = 0.5, execute: bool = False,
         shot_dir: Optional[str] = None, intents_path: str = INTENTS) -> dict:
    """콘테스트 동기화 실행. tf=Timefolio. execute+arming 없으면 드라이런."""
    targets, exp = plan_targets(intents_path=intents_path)
    holdings = tf.read_holdings()
    if not holdings:
        raise SyncBlocked(
            "보유 조회가 0건이다 — '현재=0' 이 아니라 **파서 회귀**일 수 있다.\n"
            "  2026-07-06 실사고: 빈 반환을 0 으로 읽고 기존 위에 덧샀다. 스크린샷 대조 전엔 계획 없음."
        )
    plans = build_plan(targets, holdings, min_drift=min_drift)
    results = []
    for p in plans:
        shot = f"{shot_dir}/tf_order_{p.code}.jpg" if shot_dir else None
        r = tf.place_order(p.code, p.side, p.order_weight, prc_ty="Opp",
                           execute=execute, shot=shot)
        r.update(reason=p.reason, target_w=p.target_w, current_w=p.current_w, name=p.name)
        results.append(r)
    return {"exposure": exp, "targets": targets,
            "holdings": [h.__dict__ for h in holdings],
            "plans": [p.__dict__ for p in plans], "results": results}
