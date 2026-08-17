# -*- coding: utf-8 -*-
"""장기 총이익률 시계열 (KR · DART 전체재무제표).

왜 (handoff/RESEARCH.md dig **D70**): DEEP EXIT CHECK 는 "싸다" 주장에 **그 이름 자기 역사에서의
마진 백분위**를 요구하는데, 그 계산기(`scripts/margin_history.py`)는 SEC CIK 로만 동작해 KR 종목에서
"CIK not found" 로 죽었다. 그래서 KR 밸류 논증은 규정 준수로는 불가능했고 게이트는 "호출되지 않음"으로
조용히 통과했다. 이 파일이 그 한쪽 다리를 세운다.

**US 스크립트의 미러 복제가 아니다** — 데이터 소스가 다르다(SEC companyfacts vs DART
fnlttSinglAcntAll). 산식과 출력 서식만 맞춘다.

DART API 경로는 `_dart_fin` 을 재사용한다(P1 — 같은 외부 API 를 두 번 구현하지 않는다).

---
## 실측(2026-08-03) — 이 파일이 기대는 사실과 함정

**받아지는 양** (042700 한미반도체 · 005930 삼성전자, fs_div=CFS)
- 연간: `bsns_year` 2015~2025 **11/11 년 전부 status=000**, 총이익률 산출 가능. 결측 0.
- 분기: 042700 2015~2026 sweep **42/48 기간 OK**. 못 받은 6개는 2015 Q1~Q3(공시 없음, status=013)와
  2026 Q2·Q3·연간(아직 미제출 — 오늘 2026-08-03).

**함정 1 — US 의 기간길이 함정은 KR 에 없다.** SEC companyfacts 는 `fy` 가 제출연도라 기간이 어긋나
총이익률이 −200% 가 되지만, DART 는 한 보고서가 `thstrm`(당기)·`frmtrm`(전기)·`bfefrmtrm`(전전기)
**세 열로 명시**된다. `bsns_year=Y` 를 요청해 `thstrm_amount` 만 쓰면 기간이 어긋날 수 없다.
실측 검증: 042700 FY2018 을 8개 보고서 빈티지에서 읽어 당기/전기/전전기 값이 **전부 동일**
(217,114,859,555 · 44.6%) — 재작성 불일치 0.

**함정 2 — 분기의 3개월 vs 누적.** 분기보고서에서 `thstrm_amount` 는 **3개월**,
`thstrm_add_amount` 는 **누적**이다. 섞으면 마진이 쓰레기가 된다. 실측(2025):
005930 Q1 amt 791,405억 = add 791,405억 / 반기 amt 745,663억(=Q2 3개월) vs add 1,537,068억(=H1),
그리고 Q1+Q2amt == H1add 로 3개월 기준임을 확인. 이 파일은 **분기에서 `thstrm_amount` 만** 쓴다.
Q4 는 공시가 없어 **연간 − 3분기누적**으로 유도하고 `derived=True` 로 표시한다.

**함정 3 — FY2019 이전은 account_id 가 없다.** 042700·005930 모두 2015~2018 은 IFRS 표준태그
미사용이라 `ifrs-full_Revenue` 로는 0건이고 **한글명 정확일치 폴백**으로만 잡힌다(2019년부터 id 매칭).
`matched_by` 로 어느 쪽이 잡았는지 행마다 남긴다.

**함정 4 — 총이익률이 정의되지 않는 업종이 있다.** 실측 2025 연간 8종목:
042700·005930·000660·034020·003490 = 매출원가·매출총이익 있음. **035420 NAVER = 매출은 있으나
매출원가 없음**(비용의 성격별 분류), **105560 KB금융·086790 하나금융지주 = 매출 자체 없음**.
금융·일부 플랫폼은 이 축이 **구조적으로 부재**하다 — 버그가 아니라 회계 표시방법의 문제이고,
그 경우 빈 시계열과 사유를 낸다(P4 — 빈칸이 틀린 숫자보다 낫다).

**함정 5 — 12월 결산이 아니면 bsns_year→FY 매핑이 어긋난다.** `company.json` 의 `acc_mt` 로
결산월을 확인해 12월이 아니면 경고를 실어 보낸다(실측 7종목 전부 acc_mt='12').

결정론 산출물 — 판단은 하지 않는다(P4).
"""
from __future__ import annotations

import os
import time
from typing import Optional

import requests

from ._dart_fin import _fetch_raw, _norm, _num

_COMPANY_URL = "https://opendart.fss.or.kr/api/company.json"

# 총이익률에 필요한 계정만. account_id(IFRS 표준태그) 우선, 한글명 정확일치 폴백 —
# 규칙은 _dart_fin 과 동일하되 여기서만 쓰는 매출원가 태그가 추가된다.
_IDS: dict[str, tuple[str, ...]] = {
    "revenue": ("ifrs-full_Revenue",),
    "gross_profit": ("ifrs-full_GrossProfit",),
    "cost_of_sales": ("ifrs-full_CostOfSales",),
    "operating_income": ("dart_OperatingIncomeLoss", "ifrs-full_ProfitLossFromOperatingActivities"),
}
_NAMES: dict[str, tuple[str, ...]] = {
    "revenue": ("수익(매출액)", "매출액", "매출", "영업수익"),
    "gross_profit": ("매출총이익", "매출총이익(손실)"),
    "cost_of_sales": ("매출원가",),
    "operating_income": ("영업이익(손실)", "영업이익"),
}

_QUARTER_REPRT = [("Q1", "11013"), ("Q2", "11012"), ("Q3", "11014")]


def _pick(rows: list[dict]) -> dict[str, tuple[dict, str]]:
    """계정행 추출. 반환 {key: (row, 'id'|'name')}."""
    by_id: dict[str, dict] = {}
    for row in rows:
        aid = (row.get("account_id") or "").strip()
        if aid and aid not in by_id:
            by_id[aid] = row
    out: dict[str, tuple[dict, str]] = {}
    for key, ids in _IDS.items():
        for aid in ids:
            if aid in by_id:
                out[key] = (by_id[aid], "id")
                break
    for key, names in _NAMES.items():
        if key in out:
            continue
        for want in names:
            wn = _norm(want)
            if not wn:
                continue
            for row in rows:
                if wn == _norm(row.get("account_nm", "")):
                    out[key] = (row, "name")
                    break
            if key in out:
                break
    return out


def _margin(revenue: Optional[float], gp: Optional[float], cos: Optional[float]) -> Optional[float]:
    """총이익률(%). 매출총이익이 있으면 그것을, 없으면 1−매출원가/매출."""
    if not revenue or revenue <= 0:
        return None
    if gp is not None:
        return round(gp / revenue * 100, 1)
    if cos is not None:
        return round((1 - cos / revenue) * 100, 1)
    return None


def _acc_mt(corp_code: str) -> Optional[str]:
    """결산월. 12 가 아니면 bsns_year→FY 매핑이 어긋난다(함정 5)."""
    key = os.environ.get("DART_API_KEY", "").strip()
    if not key:
        return None
    try:
        d = requests.get(
            _COMPANY_URL, params={"crtfc_key": key, "corp_code": corp_code}, timeout=20
        ).json()
    except Exception:
        return None
    return (d.get("acc_mt") or "").strip() or None


def _point(rows: list[dict], field: str) -> dict:
    """한 보고서의 지정 열(thstrm_amount 등)에서 매출·총이익·마진을 뽑는다."""
    got = _pick(rows)

    def val(key: str) -> Optional[float]:
        hit = got.get(key)
        return _num(hit[0].get(field)) if hit else None

    rev, gp, cos, op = val("revenue"), val("gross_profit"), val("cost_of_sales"), val("operating_income")
    matched = {k: v[1] for k, v in got.items()}
    return {
        "revenue": rev,
        "gross_profit": gp,
        "cost_of_sales": cos,
        "operating_income": op,
        "gross_margin_pct": _margin(rev, gp, cos),
        "operating_margin_pct": (round(op / rev * 100, 1) if (rev and rev > 0 and op is not None) else None),
        "matched_by": ("id" if matched.get("revenue") == "id" else "name") if matched else None,
        "term_nm": (got["revenue"][0].get("thstrm_nm") if "revenue" in got else None),
    }


def build_margin_history(
    stock_or_name: str,
    *,
    start_year: int = 2015,
    end_year: Optional[int] = None,
    fs_div: str = "CFS",
    quarterly: bool = False,
    sleep: float = 0.12,
) -> dict:
    """종목코드/기업명 → 연간(또는 분기) 총이익률 시계열.

    ⚠ 연간은 `thstrm_amount`(당기)만 쓴다 — 전기/전전기 열은 같은 값을 중복으로 줄 뿐이고
      (실측 재작성 불일치 0), 요청 연도의 당기만 쓰면 기간 어긋남이 원천적으로 불가능하다.
    ⚠ 분기는 `thstrm_amount`(3개월)만 쓴다. 누적(`thstrm_add_amount`)과 섞지 않는다.
    """
    from datetime import datetime

    from module_disclosure import resolve_corp_code  # P1 — corp_code 해석은 한 곳

    if not os.environ.get("DART_API_KEY", "").strip():
        return {"stock": stock_or_name, "error": "DART_API_KEY 미설정 — .env 를 확인하라"}

    resolved = resolve_corp_code(stock_or_name)
    if not resolved:
        return {"stock": stock_or_name, "error": "corp_code 해석 실패"}
    corp_code, corp_name = resolved
    end_year = end_year or datetime.now().year

    acc_mt = _acc_mt(corp_code)
    warnings: list[str] = []
    if acc_mt and acc_mt != "12":
        warnings.append(
            f"결산월 {acc_mt}월 — 12월 결산이 아니라 bsns_year 와 역년(FY)이 어긋난다. "
            "연도 라벨을 그대로 믿지 마라."
        )

    series: list[dict] = []
    missing: list[dict] = []
    used_fs: set[str] = set()

    for year in range(start_year, end_year + 1):
        rows, div = [], fs_div
        for cand in ([fs_div, "OFS"] if fs_div == "CFS" else [fs_div]):
            try:
                rows = _fetch_raw(corp_code, str(year), "11011", cand)
            except Exception as e:  # noqa: BLE001
                missing.append({"period": f"FY{year}", "reason": f"API 오류: {e}"})
                rows = []
                break
            if rows:
                div = cand
                break
            time.sleep(sleep)
        pt: dict = {}
        if not rows:
            if not any(m["period"] == f"FY{year}" for m in missing):
                missing.append({"period": f"FY{year}", "reason": "DART 에 해당 연도 사업보고서 없음"})
            # ⚠ 연간이 없어도 분기는 있을 수 있다(당해 연도 진행 중) — 여기서 continue 하면
            #   올해 분기를 통째로 잃는다.
            if not quarterly:
                time.sleep(sleep)
                continue
        else:
            pt = _point(rows, "thstrm_amount")
            used_fs.add(div)
            if pt["gross_margin_pct"] is None:
                missing.append({
                    "period": f"FY{year}",
                    "reason": ("매출 계정 없음(금융업 등 — 총이익률 정의 안 됨)" if pt["revenue"] is None
                               else "매출원가·매출총이익 없음(비용의 성격별 분류 — 총이익률 정의 안 됨)"),
                })
            elif not quarterly:
                # ⚠ 분기 모드에서는 연간 행을 시계열에 섞지 않는다 — 기준이 다른 관측을 한 표본에
                #   넣으면 백분위·중앙값이 오염된다.
                series.append({"fy": year, "period": f"FY{year}", "fs_div": div,
                               "derived": False, **pt})

        if quarterly:
            cum_rev = 0.0
            cum_gp: Optional[float] = 0.0
            for label, rc in _QUARTER_REPRT:
                try:
                    qrows = _fetch_raw(corp_code, str(year), rc, div)
                except Exception as e:  # noqa: BLE001
                    missing.append({"period": f"{year}{label}", "reason": f"API 오류: {e}"})
                    continue
                time.sleep(sleep)
                if not qrows:
                    missing.append({"period": f"{year}{label}", "reason": "DART 에 해당 분기보고서 없음"})
                    continue
                qpt = _point(qrows, "thstrm_amount")  # ⚠ 3개월 기준. 누적과 섞지 않는다
                if qpt["gross_margin_pct"] is None:
                    missing.append({"period": f"{year}{label}", "reason": "총이익률 산출 계정 없음"})
                    continue
                series.append({"fy": year, "period": f"{year}{label}", "fs_div": div,
                               "derived": False, **qpt})
                cum_rev += qpt["revenue"] or 0.0
                q_gp = qpt["gross_profit"]
                if q_gp is None and qpt["revenue"] is not None and qpt["cost_of_sales"] is not None:
                    q_gp = qpt["revenue"] - qpt["cost_of_sales"]
                cum_gp = None if (cum_gp is None or q_gp is None) else cum_gp + q_gp

            # Q4 는 공시가 없다 — 연간 − 3분기누적으로 유도한다(derived).
            fy_rev = pt.get("revenue")
            fy_gp = pt.get("gross_profit")
            if fy_gp is None and fy_rev is not None and pt.get("cost_of_sales") is not None:
                fy_gp = fy_rev - pt["cost_of_sales"]
            if fy_rev and cum_rev > 0 and fy_gp is not None and cum_gp is not None:
                q4_rev, q4_gp = fy_rev - cum_rev, fy_gp - cum_gp
                q4_gm = _margin(q4_rev, q4_gp, None)
                if q4_gm is not None:
                    series.append({
                        "fy": year, "period": f"{year}Q4", "fs_div": div, "derived": True,
                        "revenue": q4_rev, "gross_profit": q4_gp, "cost_of_sales": None,
                        "operating_income": None, "gross_margin_pct": q4_gm,
                        "operating_margin_pct": None, "matched_by": pt.get("matched_by"),
                        "term_nm": "연간−3분기누적",
                    })
                else:
                    missing.append({"period": f"{year}Q4", "reason": "연간−3분기누적 유도 불가"})
            else:
                missing.append({"period": f"{year}Q4", "reason": "연간 또는 분기 누적이 비어 유도 불가"})

        time.sleep(sleep)

    if len(used_fs) > 1:
        warnings.append(
            f"연결/별도가 시계열 안에서 섞였다({'·'.join(sorted(used_fs))}) — 마진 기준이 바뀐 구간이 있다."
        )

    series.sort(key=lambda x: (x["fy"], x["period"]))
    return {
        "stock": stock_or_name,
        "corp_code": corp_code,
        "corp_name": corp_name,
        "source": "DART fnlttSinglAcntAll (전체재무제표)",
        "basis": "quarterly(3M, Q4=연간−3분기누적)" if quarterly else "annual(당기 thstrm_amount)",
        "acc_mt": acc_mt,
        "fs_div_used": sorted(used_fs),
        "warnings": warnings,
        "series": series,
        "missing": missing,
    }


def render_text(d: dict, current: Optional[float] = None) -> str:
    """`scripts/margin_history.py`(US) 와 같은 서식. 억원 단위."""
    if d.get("error"):
        return f"{d.get('stock')}: {d['error']}"
    s = d["series"]
    name = f"{d['corp_name']} ({d['stock']})"
    if not s:
        why = "; ".join(f"{m['period']} {m['reason']}" for m in d.get("missing", [])[:3])
        return (f"{name}: 총이익률 시계열 없음 — {why or '사유 미상'}\n"
                f"  (source: {d['source']})")

    lines: list[str] = []
    gms = [x["gross_margin_pct"] for x in s]
    lines.append(f"\n# {name} 총이익률 — DART 전체재무제표 "
                 f"({len(s)}기, {s[0]['period']}~{s[-1]['period']})\n")
    lines.append(f"  basis: {d['basis']} · fs_div: {'·'.join(d['fs_div_used']) or '—'} · 결산월 {d.get('acc_mt') or '?'}\n")
    for w in d.get("warnings", []):
        lines.append(f"  ⚠ {w}")
    if d.get("warnings"):
        lines.append("")
    lines.append(f"{'기간':<9}{'매출(억원)':>14}{'총이익률':>10}")
    for x in s:
        g = x["gross_margin_pct"]
        bar = "█" * max(0, int(g / 3)) if g > 0 else "▁" * max(1, int(-g / 3))
        mark = "*" if x.get("derived") else " "
        rev_eok = (x["revenue"] or 0) / 1e8
        lines.append(f"{x['period']:<9}{rev_eok:>13,.0f}{mark}{g:>9.1f}%   {bar}")
    hi = max(s, key=lambda x: x["gross_margin_pct"])
    lo = min(s, key=lambda x: x["gross_margin_pct"])
    med = sorted(gms)[len(gms) // 2]
    lines.append("")
    lines.append(f"  최고 {hi['period']} {hi['gross_margin_pct']}%  ·  최저 {lo['period']} "
                 f"{lo['gross_margin_pct']}%  ·  중앙값 {med}%")
    if any(x.get("derived") for x in s):
        lines.append("  * = 유도값(연간−3분기누적) — 공시된 수치가 아니다")
    if d.get("missing"):
        lines.append(f"  결측 {len(d['missing'])}건: "
                     + "; ".join(f"{m['period']}({m['reason']})" for m in d["missing"][:6])
                     + (" …" if len(d["missing"]) > 6 else ""))
    if current is not None:
        pct = sum(1 for g in gms if g < current) / len(gms) * 100
        lines.append(f"  ★ 현재 {current}% → 자기 역사 **{pct:.0f} 백분위**, "
                     f"표본 최고 대비 {current - hi['gross_margin_pct']:+.1f}%p")
        lines.append("     (lens B2 — 멀티플은 마진 백분위와 같이 읽어야 밸류에이션이 된다)")
    return "\n".join(lines)
