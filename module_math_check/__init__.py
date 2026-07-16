"""리포트 markdown의 산식 자기검증 모듈.

LLM이 작성한 리포트 본문은 문장 단위 confabulation으로 산식 결과가 어긋나는 일이
잦다. 가중평균·peer 평균·상승여력 등 *기계적으로 검증 가능한* 숫자는 모두
이 모듈을 거쳐 사후 검산한다.

INVESTMENT_REPORT_PIPELINE.md §13.5 단계 (목표주가 산정 직후, 발행 전 의무).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CheckResult:
    name: str
    passed: bool
    expected: float = 0.0
    actual: float = 0.0
    delta_pct: float = 0.0
    location: str = ""
    detail: str = ""


_NUM_RE = re.compile(r"[+\-]?[\d,]+(?:\.\d+)?")


def _parse_num(s: str) -> float | None:
    if s is None:
        return None
    s = s.strip().replace("**", "").replace("`", "")
    m = _NUM_RE.search(s.replace(",", ""))
    if not m:
        return None
    try:
        return float(m.group(0).replace(",", ""))
    except ValueError:
        return None


def parse_markdown_tables(text: str) -> list[list[list[str]]]:
    """매우 단순 markdown 파이프 표 파서. 표마다 [rows[cells]] 반환."""
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and s.endswith("|") and len(s) > 2:
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", c) for c in cells if c):
                continue
            current.append(cells)
        else:
            if current:
                tables.append(current)
                current = []
    if current:
        tables.append(current)
    return tables


def _find_col(header: list[str], *keywords: str) -> int | None:
    for i, h in enumerate(header):
        for k in keywords:
            if k in h:
                return i
    return None


def check_weighted_avg(table: list[list[str]], tbl_idx: int) -> list[CheckResult]:
    """표 마지막 행이 '가중평균'이면 위 행들의 (값×가중치) 합과 비교."""
    out: list[CheckResult] = []
    if len(table) < 3:
        return out
    header = table[0]
    w_idx = _find_col(header, "가중")
    t_idx = _find_col(header, "목표주가", "목표가")
    if w_idx is None or t_idx is None:
        return out

    last_label = "".join(table[-1][:2])
    if "가중평균" not in last_label:
        return out

    total = 0.0
    weight_sum = 0.0
    rows = 0
    for row in table[1:-1]:
        if len(row) <= max(w_idx, t_idx):
            continue
        v = _parse_num(row[t_idx])
        w = _parse_num(row[w_idx])
        if v is None or w is None:
            continue
        if w > 1.0:
            w = w / 100.0
        total += v * w
        weight_sum += w
        rows += 1
    if rows == 0:
        return out

    actual = _parse_num(table[-1][t_idx])
    if actual is None:
        return out
    delta_pct = (total / actual - 1.0) * 100.0 if actual else 0.0
    out.append(CheckResult(
        name="weighted_avg",
        passed=abs(delta_pct) < 1.0,
        expected=total, actual=actual, delta_pct=delta_pct,
        location=f"표 #{tbl_idx} (가중평균)",
        detail=f"Σ(목표가×가중치) over {rows}행, 가중치합={weight_sum:.2f}",
    ))
    if abs(weight_sum - 1.0) > 0.01:
        out.append(CheckResult(
            name="weight_sum",
            passed=False,
            expected=1.0, actual=weight_sum,
            delta_pct=(weight_sum - 1.0) * 100.0,
            location=f"표 #{tbl_idx} (가중평균)",
            detail=f"가중치 합 100% 아님: {weight_sum*100:.1f}%",
        ))
    return out


def check_peer_avg(table: list[list[str]], tbl_idx: int) -> list[CheckResult]:
    """표 안 'Peer 평균' / 'Peer 중앙값' 행을 위 데이터 행으로 검산.

    자종 행(굵게 마킹 ``**...**``된 행)은 peer 평균 계산에서 제외 — module_valuation
    이 자종 제외 peer 평균을 산출하는 표준 컨벤션을 따른다.
    """
    out: list[CheckResult] = []
    if len(table) < 4:
        return out
    avg_idx = median_idx = None
    for i, row in enumerate(table):
        head = "".join(row[:2])
        if avg_idx is None and "Peer 평균" in head:
            avg_idx = i
        if median_idx is None and "Peer 중앙값" in head:
            median_idx = i
    if avg_idx is None and median_idx is None:
        return out

    data_end = min([i for i in [avg_idx, median_idx] if i is not None])
    raw_rows = table[1:data_end]
    # 자종 행 제외: 종목명 셀(0번 또는 1번)에 ** 굵은 마킹된 행
    data_rows = [r for r in raw_rows if not any("**" in c for c in r[:2])]
    if len(data_rows) < 2:
        return out

    header = table[0]
    for col_idx, col_name in enumerate(header):
        if col_idx < 2:
            continue
        vals: list[float] = []
        for r in data_rows:
            if len(r) <= col_idx:
                continue
            v = _parse_num(r[col_idx])
            if v is not None and v != 0:
                vals.append(v)
        if len(vals) < 2:
            continue
        if avg_idx is not None and len(table[avg_idx]) > col_idx:
            actual = _parse_num(table[avg_idx][col_idx])
            if actual is None or actual == 0:
                continue
            expected = sum(vals) / len(vals)
            delta_pct = (expected / actual - 1.0) * 100.0
            if abs(delta_pct) >= 1.0 and abs(expected - actual) > 0.5:
                out.append(CheckResult(
                    name=f"peer_avg[{col_name}]",
                    passed=False,
                    expected=expected, actual=actual, delta_pct=delta_pct,
                    location=f"표 #{tbl_idx} — '{col_name}' Peer 평균행",
                    detail=f"mean({len(vals)}개 peer) = {expected:.2f} vs 표기 {actual}",
                ))
        if median_idx is not None and len(table[median_idx]) > col_idx:
            actual = _parse_num(table[median_idx][col_idx])
            if actual is None or actual == 0:
                continue
            srt = sorted(vals)
            n = len(srt)
            expected = srt[n // 2] if n % 2 else (srt[n // 2 - 1] + srt[n // 2]) / 2
            delta_pct = (expected / actual - 1.0) * 100.0
            if abs(delta_pct) >= 1.0 and abs(expected - actual) > 0.5:
                out.append(CheckResult(
                    name=f"peer_median[{col_name}]",
                    passed=False,
                    expected=expected, actual=actual, delta_pct=delta_pct,
                    location=f"표 #{tbl_idx} — '{col_name}' Peer 중앙값행",
                    detail=f"median({len(vals)}개) = {expected:.2f} vs 표기 {actual}",
                ))
    return out


_UPSIDE_RE = re.compile(
    r"목표주가[^\n|:]*[:\s|*]+\s*\*?\*?([\d,]+)\s*원"
    r"[^()|\n]{0,40}?\(\s*상승여력?\s*([+\-]?[\d.]+)\s*%\s*\)"
)


def check_upside_consistency(text: str) -> list[CheckResult]:
    out: list[CheckResult] = []
    m_price = re.search(r"현재가[^:|]*[:\s|]+\s*\*?\*?([\d,]+)\s*원", text)
    if not m_price:
        return out
    price = _parse_num(m_price.group(1))
    if not price:
        return out

    targets: set[int] = set()
    for m in _UPSIDE_RE.finditer(text):
        target = _parse_num(m.group(1))
        upside = _parse_num(m.group(2))
        if target is None or upside is None:
            continue
        targets.add(round(target))
        expected = (target / price - 1.0) * 100.0
        delta = expected - upside
        out.append(CheckResult(
            name="upside_pct",
            passed=abs(delta) < 0.2,
            expected=expected, actual=upside, delta_pct=delta,
            location=f"목표가 {target:,.0f}원",
            detail=f"({target:,.0f}/{price:,.0f} - 1)*100 = {expected:.2f}%",
        ))

    if len(targets) > 1:
        out.append(CheckResult(
            name="target_consistency",
            passed=False,
            expected=1, actual=len(targets), delta_pct=0,
            location="리포트 전체",
            detail=f"목표주가가 {len(targets)}개 다른 값으로 등장: {sorted(targets)}",
        ))
    return out


def check_all(path: Path) -> tuple[list[CheckResult], list[CheckResult]]:
    text = path.read_text(encoding="utf-8")
    tables = parse_markdown_tables(text)
    checks: list[CheckResult] = []
    for i, t in enumerate(tables, 1):
        checks.extend(check_weighted_avg(t, i))
        checks.extend(check_peer_avg(t, i))
    checks.extend(check_upside_consistency(text))
    passed = [c for c in checks if c.passed]
    failed = [c for c in checks if not c.passed]
    return passed, failed


__all__ = [
    "check_all", "check_weighted_avg", "check_peer_avg",
    "check_upside_consistency", "parse_markdown_tables", "CheckResult",
]
