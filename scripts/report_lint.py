# FILE: scripts/report_lint.py
"""
REPORT_LINT — mechanical check of the desk's own output against the carry rules.

Why this exists (2026-07-22): `handoff/RESEARCH.md` holds 21 trigger-form rules, and every one of
them currently depends on the model REMEMBERING to apply it. Measured that same session: six
judgments were reversed, and the very commit that added three new data axes forgot to enforce any of
them — the rules were written as prose and prose does not fire.

Four of the rules are mechanically checkable. Those four live here. The linter does not judge
analysis; it only asks "did you write the thing the rule requires, in the same paragraph".

  C1  excess/relative return  → is a benchmark named in the same paragraph?
  C2  a YoY figure            → is a sequential (MoM/QoQ) figure in the same paragraph?
  S6  a future-using label    → is it tagged as a label?
  D6  OBV accumulation/dist.  → is it accompanied by an A/B-grade axis (RS, real flow)?

Usage:
  python -X utf8 scripts/report_lint.py llm_outputs/2026-07-21/industry_US/*.md
  python -X utf8 scripts/report_lint.py <file...> [--json] [--strict] [--rules C1,D6]

Exit code: 0 clean (or warnings without --strict) · 1 findings with --strict · 2 bad usage.
Analytical artifact — it checks form, never content. Zero buy/sell meaning.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from pathlib import Path

# ── 규칙 정의 ────────────────────────────────────────────────────────────────
# trigger  : 이게 걸리면 그 단락을 검사한다
# need     : 단락 안에 이것 중 하나가 있어야 통과
# 오탐 방지 : exempt 가 걸린 단락은 통째로 면제(규칙 자체를 서술하는 문서·헤더 등)

RULES: dict[str, dict] = {
    "C1": {
        "name": "기준선/벤치마크 미기재",
        # 표 셀의 RS20 컬럼은 데이터이지 주장이 아니다 → 산문 단락에서만 검사(skip_tables).
        "trigger": r"초과\s*수익|초과수익|상대강도|아웃퍼폼|언더퍼폼"
                   r"|excess\s+return|outperform|underperform|relative\s+strength",
        "need": r"\bSPY\b|\^KS11|KOSPI|\bQQQ\b|\bSMH\b|\bSOXX\b|\bXL[EFKVYIBPU]\b|벤치|bench"
                r"|vs\s+[A-Z\^][A-Za-z0-9^]{1,6}|대비",
        "skip_tables": True,
        "file_ctx": r"bench(?:mark)?[:\s=]+\S|벤치\s*\S",  # 파일이 벤치를 선언했으면 면제
        "why": "RULE C1 — 벤치마크를 안 밝히면 부호가 뒤집힌다. 실측: 005930 은 SPY 대비 −12.1%, "
               "^KS11 대비 +10.1% (같은 20일).",
    },
    "C2": {
        "name": "프린트 반쪽 인용 (YoY 만)",
        # 개별 종목 실적 성장률이 아니라 '발표된 지표'에만 건다.
        "trigger": r"(?:수출|출하|매출|판매|생산|물가|고용|재고|주문|CPI|PPI|exports?|shipments?)"
                   r"[^.\n]{0,40}(?:YoY|전년\s*(?:동기)?\s*대비|전년비)",
        "need": r"MoM|QoQ|전월\s*대비|전월비|전분기\s*대비|직전\s*분기|sequential|순차|d/d|WoW",
        "skip_tables": True,
        "why": "RULE C2 — 기록적 YoY 와 마이너스 MoM 이 같은 발표에 실린다. 실측: 반도체 수출 "
               "+180.6% YoY 인 날 같은 창(1~20일)이 −11.3% MoM.",
    },
    "S6": {
        "name": "미래를 쓰는 라벨 미표기",
        # 'regime'·'smoothed' 단독은 일상어라 오탐. pivot 계열 + 스무딩 레짐 라벨에만.
        "trigger": r"\bpivot_(?:up|down)\b|\bpivot\s+(?:label|classifier|판정)"
                   r"|smoothed\s+regime|스무딩\s*레짐|레짐\s*라벨",
        "need": r"\[label\]|\[라벨\]|사후\s*라벨|라벨이다|label only|not a signal|신호가\s*아니"
                r"|미래\s*\d*\s*일|forward-?looking|look-?ahead",
        "why": "RULE S6 — pivot 판정은 미래 10일을 쓴다. 신호로 쓰면 과거성적은 완벽하고 실전은 0.",
    },
    "D6": {
        "name": "OBV 단독 인용 (C급 신호)",
        # 'distribution/accumulation' 일반 용법 오탐 제거 — OBV 상태 주장에만 건다.
        "trigger": r"OBV\s*(?:는|가|:)?\s*(?:매집|분산|중립|accumulat|distribut)"
                   r"|(?:매집|분산)\s*(?:전환|중|상태|시그널)|OBV\s*[+-]?\d",
        "need": r"\bRS20\b|\bRS60\b|모멘텀|momentum|외국인|기관\s*순매수|KIS|투자자별"
                r"|foreign\s+net|real\s+flow|실수급|날짜\s*클러스터|C급|grade",
        "why": "RULE D6 — OBV 는 실수급의 절반 그림자(r≈0.49)이고 선행력이 없다(t=1.00). "
               "C급은 단독으로 명제를 지탱할 수 없다.",
    },
}

# 규칙 문서 자신(= 규칙을 서술하는 단락)은 검사 대상이 아니다.
EXEMPT = re.compile(
    r"RULE\s+[CSDWL]\d|carry rule|handoff/RESEARCH|Fires when|발동|트리거형|규칙 정의"
    r"|^\s*\|\s*(?:등급|Grade)\s*\||measured failure|Measured failure",
    re.I | re.M,
)

# 규칙별 오탐 제거 — 실측 보정(2026-07-21 데스크 9파일로 캘리브레이션).
# C1: Outperform/Market Perform 은 애널리스트 **등급명**이지 상대수익 주장이 아니다.
FALSE_POSITIVE = {
    "C1": re.compile(
        r"(?:down|up)grade\w*|rating|initiat\w+|reiterat\w+|Market\s+Perform|투자의견|목표주가",
        re.I),
}


def _paragraphs(text: str) -> list[tuple[int, str]]:
    """(시작 줄번호, 단락) 리스트. 표는 연속 행을 한 단락으로 묶는다."""
    out, buf, start = [], [], 1
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip():
            if not buf:
                start = i
            buf.append(line)
        else:
            if buf:
                out.append((start, "\n".join(buf)))
                buf = []
    if buf:
        out.append((start, "\n".join(buf)))
    return out


def lint_text(text: str, rules: list[str]) -> list[dict]:
    findings = []
    paras = _paragraphs(text)
    head = "\n".join(p for _, p in paras[:4])          # 파일 머리 = 선언부(벤치·asof 등)
    for lineno, para in paras:
        if EXEMPT.search(para):
            continue
        is_table = para.lstrip().startswith("|") or "\n|" in para
        is_exit = bool(re.match(r"\s*(?:---\s*)?\**\s*EXIT\s*CHECK", para, re.I))
        for rid in rules:
            spec = RULES[rid]
            if spec.get("skip_tables") and is_table:
                continue                                # 표 셀은 데이터이지 주장이 아니다
            if is_exit:
                continue                                # EXIT CHECK 는 체크리스트지 분석이 아니다
            if spec.get("file_ctx") and re.search(spec["file_ctx"], head, re.I):
                continue                                # 파일이 이미 벤치를 선언함
            m = re.search(spec["trigger"], para, re.I)
            if not m:
                continue
            if re.search(spec["need"], para, re.I):
                continue
            fp = FALSE_POSITIVE.get(rid)
            if fp and fp.search(para):
                continue                                # 실측 보정된 오탐 패턴
            snippet = " ".join(para.split())[:110]
            findings.append({
                "rule": rid, "name": spec["name"], "line": lineno,
                "hit": m.group(0), "why": spec["why"], "snippet": snippet,
            })
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description="데스크 산출물 규칙 린터 (형식 검사 전용)")
    ap.add_argument("paths", nargs="+", help="검사할 .md (glob 가능)")
    ap.add_argument("--rules", default=",".join(RULES), help=f"기본 {','.join(RULES)}")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true", help="발견 시 exit 1")
    a = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")  # Windows cp949 크래시 방지
    except Exception:
        pass

    rules = [r.strip().upper() for r in a.rules.split(",") if r.strip()]
    bad = [r for r in rules if r not in RULES]
    if bad:
        print(f"알 수 없는 규칙: {bad} (가능: {list(RULES)})", file=sys.stderr)
        return 2

    files: list[Path] = []
    for p in a.paths:
        files += [Path(x) for x in glob.glob(p)] or ([Path(p)] if Path(p).exists() else [])
    if not files:
        print("검사할 파일 없음", file=sys.stderr)
        return 2

    report: dict[str, list[dict]] = {}
    for f in files:
        try:
            report[str(f)] = lint_text(f.read_text(encoding="utf-8", errors="ignore"), rules)
        except Exception as e:
            print(f"[warn] {f}: {e}", file=sys.stderr)

    total = sum(len(v) for v in report.values())
    if a.json:
        print(json.dumps({"total": total, "findings": report}, ensure_ascii=False, indent=2))
    else:
        print(f"# REPORT_LINT — {len(report)}개 파일 · 규칙 {','.join(rules)}\n")
        for f, fs in report.items():
            if not fs:
                print(f"  ✅ {Path(f).name}")
                continue
            print(f"  ⚠ {Path(f).name} — {len(fs)}건")
            for x in fs:
                print(f"      L{x['line']:<5} [{x['rule']}] {x['name']}  ← \"{x['hit']}\"")
                print(f"             {x['snippet']}…")
        print(f"\n총 {total}건.")
        if total:
            for rid in sorted({x['rule'] for fs in report.values() for x in fs}):
                print(f"  · {RULES[rid]['why']}")
        print("\n형식 검사다 — 내용의 옳고 그름은 판정하지 않는다. 면제가 필요하면 그 단락에 "
              "규칙 ID(예: RULE C1)를 적고 왜 면제인지 쓴다.")
    return 1 if (total and a.strict) else 0


if __name__ == "__main__":
    raise SystemExit(main())
