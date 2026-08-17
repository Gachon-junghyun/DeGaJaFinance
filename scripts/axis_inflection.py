# -*- coding: utf-8 -*-
"""axis_inflection — `module_inflection` 의 패턴 신호를 **IC 원장의 축 파일로** 내보낸다.

왜 있나
------
이 리포에는 패턴 발견기가 이미 여러 개 있다(`module_inflection` 변곡·언급, `lab/ECONOPHYSICS`
수급·심리, `module_news_data thread` 사건 궤적). **없던 것은 발견기가 아니라 눈금자다** —
찾은 패턴이 진짜인지 가리는 장치. 실측으로 그 대가를 두 번 치렀다(2026-07-31):
`leak_scan` 의 "보유가 샌다"가 지평 바꾸니 뒤집혔고, `ic_ledger` 첫 실행이 `t=+6.7` 짜리
거짓 패턴을 냈다(3개 창이 전부 같은 반등으로 끝남).

그래서 순서가 **눈금자 → 발견기**다. 이 파일은 그 연결이다: 발견기의 산출을 축 파일로 떨구면
`ic_ledger` 가 런당 1행씩 IC 를 쌓고, **3~5개월 뒤 그 패턴이 신호인지 아닌지 자동으로 갈린다.**

내보내는 축
-----------
- **`mention_z`** — 종목별 뉴스 언급수의 z(직전 30일 기준, 당일 제외).
  "군중의 관심이 지금 이 종목에 비정상적으로 몰렸나" = **심리/관심 축**.
  ⚠ 방향 가설을 여기서 세우지 않는다. 관심 급증이 선행인지 꼭지인지는 **IC 가 답한다**(P4).
- **`mention_z_chg`** — 그 z 의 1일 변화(관심의 **가속**). 수준과 변화는 다른 축이다
  (`RESEARCH` 렌즈 B1: 가격순환 섹터를 2계도함수로 읽는 규칙의 관심축 버전).

⚠ **P6**: 무거운 서드파티를 최상단에서 import 하지 않는다. `module_inflection` 은 클라 전용이고
   `analog` 만 GPU 다 — 이 스크립트는 그 경로를 **쓰지 않는다**(mention 계열은 CPU·sqlite).
⚠ **선행참조 금지**: `mention_z` 는 정의상 직전 30일만 본다(당일 제외). 런 날짜의 z 는 그날
   장 시작 전에 알 수 있는 값이어야 한다 — 뉴스 `market_day` 기준이라 그 조건을 만족한다.

CLI
---
  python -X utf8 scripts/axis_inflection.py                  # 모든 런 날짜에 축 파일 생성
  python -X utf8 scripts/axis_inflection.py --run 2026-07-31
  python -X utf8 scripts/axis_inflection.py --status
그 뒤 `python -X utf8 scripts/ic_ledger.py log` 하면 새 축이 자동으로 잡힌다(원장 수정 0).
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sqlite3
import sys

import _repo_path  # noqa: F401

AXIS_DIR = os.path.join("out", "ic", "axes")
RUNS_GLOB = os.path.join("llm_outputs", "*", "industry_KR", "SECTOR_FLOW_KR.json")


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def run_dates() -> list[str]:
    out = []
    for f in sorted(glob.glob(RUNS_GLOB)):
        d = os.path.basename(os.path.dirname(os.path.dirname(f)))
        if len(d) == 10 and d[4] == "-":
            out.append(d)
    return out


def build(runs: list[str]) -> int:
    import pandas as pd

    from module_inflection._config import INFLECTION_DB    # 파생 DB 경로의 단일 원본
    from module_inflection._newslink import mention_frame, mention_z

    db = str(INFLECTION_DB)
    if not os.path.exists(db):
        print(f"[err] {db} 없음 — `python -m module_inflection build` 를 먼저 돌려라")
        return 1

    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    # 언급 프레임은 모듈 API 그대로 사용(재구현 0)
    all_days = [r[0] for r in con.execute("SELECT DISTINCT day FROM mentions ORDER BY day")]
    if not all_days:
        print("[err] mentions 비어있음 — `python -m module_inflection build` 필요")
        con.close()
        return 1
    m = mention_frame(con, all_days)
    con.close()
    z = mention_z(m)
    dz = z.diff()

    os.makedirs(AXIS_DIR, exist_ok=True)
    made = 0
    for run in runs:
        if run not in z.index:
            continue
        row, drow = z.loc[run], dz.loc[run]
        a1 = {str(k): float(v) for k, v in row.items() if pd.notna(v)}
        a2 = {str(k): float(v) for k, v in drow.items() if pd.notna(v)}
        if len(a1) < 50:
            continue
        p = os.path.join(AXIS_DIR, f"kr_{run}.json")
        prev = {}
        if os.path.exists(p):
            try:
                prev = json.load(open(p, encoding="utf-8"))
            except Exception:                                # noqa: BLE001
                prev = {}
        prev.update({"mention_z": a1, "mention_z_chg": a2,
                     "_source": "module_inflection._newslink.mention_z (재구현 0)",
                     "_run": run, "_n": len(a1)})
        json.dump(prev, open(p, "w", encoding="utf-8"), ensure_ascii=False)
        made += 1
        print(f"  {run}  mention_z {len(a1):>4}종목 · chg {len(a2):>4}종목 → {os.path.basename(p)}")
    print(f"\n[ok] 축 파일 {made}개 생성/갱신 → {AXIS_DIR}")
    print("  다음: python -X utf8 scripts/ic_ledger.py log   (새 축이 자동으로 잡힌다)")
    return 0


def status() -> int:
    files = sorted(glob.glob(os.path.join(AXIS_DIR, "kr_*.json")))
    print(f"# AXIS FILES — {len(files)}개  ({AXIS_DIR})")
    for f in files[-10:]:
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:                                    # noqa: BLE001
            continue
        axes = [k for k in d if not k.startswith("_")]
        print(f"  {os.path.basename(f):20s} 축 {len(axes)}개 {axes} · {d.get('_n','?')}종목")
    return 0


def main() -> int:
    utf8_stdout()
    ap = argparse.ArgumentParser(prog="axis_inflection")
    ap.add_argument("--run", default=None, help="특정 런 날짜만")
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    if a.status:
        return status()
    runs = [a.run] if a.run else run_dates()
    if not runs:
        print("[err] 런 날짜를 찾지 못했다")
        return 1
    return build(runs)


if __name__ == "__main__":
    raise SystemExit(main())
