# -*- coding: utf-8 -*-
"""Render the learned playbook — what the scored ledger says to prefer, avoid and recalibrate.

`credit` (rebuilt by `learn`) and `calib` are the only inputs. The output is a derived
markdown file that routines paste into child prompts, so a scored outcome changes the
next run without a human edit. Deterministic: same ledger, same file. Callers own commits.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from module_lens._learn import calib
from module_lens._score import _ensure_schema, _rows

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "pipeline" / "LEARNED.md"

MIN_N = 5          # 이보다 적게 정산된 방법은 «지켜봄»에만 둔다
PREFER_LO80 = 0.5  # 80% 하한이 동전보다 나으면 «먼저 쓴다»
AVOID_HI80 = 0.5   # 80% 상한조차 동전보다 못하면 «쓰지 않는다»
CALIB_MIN = 5      # 확률 구간 표본이 이보다 적으면 눈금을 안 고친다
CALIB_GAP = 0.15   # 말한 확률과 일어난 빈도가 이만큼 벌어지면 고친다


def _pct(x):
    return "—" if x is None else f"{x * 100:.0f}%"


def rules(con) -> dict:
    _ensure_schema(con)
    # 방법 판정은 적중률이 아니라 «변동성 기준률 대비 브라이어 개선»으로 한다 (2026-10-31, `_replay.method_skill`).
    from module_lens._replay import method_skill
    credit = {m["name"]: m for m in _rows(con, "SELECT * FROM credit WHERE level='method'")}
    prefer, avoid, watch = [], [], []
    for name, k in sorted(method_skill(con).items(), key=lambda kv: -kv[1]["n"]):
        m = dict(credit.get(name, {}), name=name, **k)
        if k["n"] >= MIN_N and k["lo90"] is not None and k["lo90"] > 0:
            prefer.append(m)
        elif k["n"] >= MIN_N and k["hi90"] is not None and k["hi90"] < 0:
            avoid.append(m)
        elif k["n"] >= 3:
            watch.append(m)
    c = calib(con)
    recal = [b for b in c["buckets"]
             if b["count"] >= CALIB_MIN and b["observed_frequency"] is not None
             and abs(b["observed_frequency"] - b["predicted_mean"]) >= CALIB_GAP]
    n_out = _rows(con, "SELECT count(*) AS n FROM outcomes")[0]["n"]
    from module_lens._replay import replay
    from module_lens._replay import vol_table
    # 금지는 날짜가 여러 달에 퍼졌을 때만 — 2026-10-31 sim flow: 0/7 은 한 국면에 몰린 결과였다
    spread = {r["method"]: r["months"] for r in _rows(con, """SELECT e.method, COUNT(DISTINCT substr(q.settle,1,7)) AS months
        FROM evidence e JOIN questions q ON q.id=e.question JOIN outcomes o ON o.question=q.id
        WHERE e.dead IS NULL AND e.weight>0 GROUP BY e.method""")}
    held = [m for m in avoid if spread.get(m["name"], 0) < 3]
    avoid = [m for m in avoid if spread.get(m["name"], 0) >= 3]
    watch = held + watch
    return {"prefer": prefer, "avoid": avoid, "watch": watch, "recal": recal,
            "by_kind": c["by_kind"], "outcomes": n_out, "replay": replay(con),
            "vol_5": vol_table(con, 5), "vol_1": vol_table(con, 1)}


def render(r: dict, now: str) -> str:
    def line(m):
        lo = "—" if m.get("lo90") is None else f"{m['lo90']:+.3f}"
        hi = "—" if m.get("hi90") is None else f"{m['hi90']:+.3f}"
        hits = f" · 적중 {m['hits']}/{m.get('n')}" if m.get("hits") is not None else ""
        return f"- {m['name']} — 정산 {m['n']}, 변동성 기준률 대비 브라이어 개선 {m['skill']:+.3f} (90% {lo}~{hi}){hits}"
    out = [
        "# LEARNED — 채점된 장부가 다음 회차에 시키는 것 (자동 생성)",
        "",
        "> **뭐냐:** `module_lens` 의 정산 결과(credit·calib)로 기계가 쓴 방법 선호·금지·확률 눈금. 손으로 고치지 마라 — `python -X utf8 -m module_lens playbook` 이 다시 쓴다.",
        "> **언제 읽나:** 루틴 메인이 자식에게 일을 넘길 때 이 파일 본문을 지시문 끝에 붙인다. 자식은 근거 방법을 고를 때 이 순서를 따른다.",
        "> **안 담는 것:** 주문·투자총량·금지 목록(루틴 본문이 정본이고 이 파일로 못 바꾼다) · 말로 된 교훈(개선 루틴이 루틴 문서에 직접 쓴다).",
        "",
        f"생성 {now} · 정산된 물음 {r['outcomes']}건 · 문턱: 정산 {MIN_N}회 이상, «변동성 기준률 대비 브라이어 개선»의 90% 구간 전체가 0 위면 먼저, 아래면 금지. 금지는 정산이 3개월 이상에 퍼졌을 때만.",
        "",
        "## 먼저 쓸 방법",
        *([line(m) for m in r["prefer"]] or ["- (아직 문턱을 넘은 방법이 없다)"]),
        "",
        "## 쓰지 않을 방법 — 기준률보다 확률을 나쁘게 만들었다. 근거 비중에 넣지 마라(맥락으로 읽는 것까지는 된다)",
        *([line(m) for m in r["avoid"]] or ["- (없음)"]),
        "",
        "## 지켜보는 방법 (정산 3회 이상, 아직 문턱 사이 — 겨뤄 볼 후보)",
        *([line(m) for m in r["watch"][:15]] or ["- (없음)"]),
        "",
        "## 확률을 고치는 정책 — 되돌려 돌린 시뮬레이션(`replay`)에서 90% 구간 전체가 브라이어를 낮춘 것만 시킨다",
    ]
    rp = r["replay"]
    adopted = [k for k, v in rp.get("policies", {}).items() if v["adopt"]]
    out.append(f"- 시뮬레이션 표본: 갈래 확률이 있는 정산 {rp['usable']}건 중 평가 {rp['evaluated']}건, 정산 5회 이상 방법 {rp['methods_settled_5plus']}개.")
    for k, v in rp.get("policies", {}).items():
        out.append(f"  - {k}: 브라이어 차 {v['diff']:+.3f} (90% {v['lo90']:+.3f}~{v['hi90']:+.3f}) → {'채택' if v['adopt'] else '아직 효과 확인 못 함'}")
    if any(k.startswith("vol_rate") for k in adopted):
        from module_lens._replay import vol_table
        import sqlite3 as _sq
        out.append("- 🟢 **변동성 기준률 채택** — 갈래 확률을 매길 땐 먼저 그 종목의 60일 일간 수익 표준편차(σ60)로 아래 칸을 찾아 그 빈도에서 출발하고, 근거로 옮기는 건 그다음이다(시뮬: 확률을 이 칸 쪽으로 70% 당기면 브라이어가 낮아졌다).")
        for h in (5, 1):
            vt = r.get(f"vol_{h}") or {}
            if vt.get("bands"):
                def _band(b):
                    hi = "" if b["vol_hi"] is None else f"{b['vol_hi'] * 100:.1f}"
                    return f"σ60 {b['vol_lo'] * 100:.1f}~{hi}% → A {b['A'] * 100:.0f} / C {b['C'] * 100:.0f} / B {b['B'] * 100:.0f}"
                out.append(f"  - h={h} (정산 {vt['n']}건): " + " · ".join(_band(b) for b in vt["bands"]))
    if not adopted:
        out.append("- 채택된 정책이 없다. 아래 눈금은 **참고로만** 보고, 확률은 지금처럼 매긴다. 표본이 늘면 이 줄이 저절로 바뀐다.")
    out += ["", "## 갈래 치우침 — 근거가 어느 갈래를 지지했고 실제로 무엇이 일어났나",
            f"- 근거가 지지한 갈래: {rp.get('evidence_support_share')} · 실제 일어난 갈래: {rp.get('fired_share')}",
            "- 일어난 쪽(대개 가운데·현상유지 갈래)을 지지하는 근거가 적으면, **현상유지 갈래를 지지하는 근거를 일부러 하나 찾아 붙인다**(극단 갈래만 근거를 모으는 치우침).",
            "", "## 확률 눈금 (참고)"]
    if r["recal"]:
        for b in r["recal"]:
            out.append(f"- {b['lo']}~{b['hi']}% 라고 한 갈래는 실제로 {_pct(b['observed_frequency'])} 일어났다"
                       f"(표본 {b['count']}, 말한 평균 {_pct(b['predicted_mean'])}). 이 구간을 매길 땐 일어난 빈도 쪽으로 옮겨라.")
    else:
        out.append("- (눈금이 문턱 안이다)")
    out += ["", "## 근거 종류별 브라이어 (낮을수록 잘 맞음)"]
    for k in sorted(r["by_kind"], key=lambda x: x["mean_brier"]):
        out.append(f"- {k['kind']}: {k['mean_brier']:.2f} (물음 {k['count']})")
    out += ["", "## 변경 이력", f"- {now[:10]} — 자동 생성. 이력은 git 과 개선 루틴 일기(`pipeline/routines/UPGRADE_LOG.md`)에 남는다.", ""]
    return "\n".join(out)


def playbook(con, out=None) -> dict:
    r = rules(con)
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="minutes")
    path = Path(out) if out else DEFAULT_OUT
    path.write_text(render(r, now), encoding="utf-8")
    return {"path": str(path), "prefer": len(r["prefer"]), "avoid": len(r["avoid"]),
            "watch": len(r["watch"]), "recal": len(r["recal"]), "outcomes": r["outcomes"]}
