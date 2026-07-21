# -*- coding: utf-8 -*-
"""말의 종류 → 이후 흐름. "이런 말이 나올 때 이렇게 흘렀다"의 표.

변곡 주변 제목을 사람이 읽어보니 같은 '뉴스 동반'이라도 **말의 종류가 전혀 달랐다** —
수주 공시와 ESG 보고서 발간과 '[특징주] 급등'이 한 칸에 뭉쳐 있었다. 그래서 뉴스를
있다/없다로 세지 않고 **유형별로** 갈라 이후 수익을 잰다.

측정 단위는 변곡일이 아니라 **모든 (종목, 기사일)** 이다. "이 말이 나오면 그 다음이 어떤가"는
변곡점에서만 묻는 질문이 아니고, 변곡으로 좁히면 표본이 수십 건으로 줄어 아무 말도 못 한다.

⚠ **거래 가능한 날로 옮겨 잰다.** 기사일이 토요일이면 그날 살 수 없다. 기사일 **이후 첫
거래일의 종가**를 기준점으로 삼고 거기서 앞으로 n일을 센다. 기사일 당일 종가를 기준으로
재면 '기사를 보고 그날 종가에 샀다'는 불가능한 가정이 섞인다.

⚠ **초과수익으로만 읽는다.** 이 창(2026-05~07)의 무조건부 5일 평균이 −1.7% 라, 원수익은
전부 음수로 보인다. 유형 간 비교는 같은 기준선을 빼면 그대로 유효하다.

⚠ 유형은 **제목의 표면 어휘**다. '수주'가 제목에 있다고 수주가 확정된 것도, 그게 그 종목의
수주인 것도 아니다(같은 제목에 회사 셋이 나온다). 정밀도를 재지 않은 프록시다.
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

# 순서가 곧 우선순위 — 위에서 먼저 맞으면 그걸로 분류한다(한 제목 = 한 유형).
# '사후보도'를 맨 위에 두는 이유: "[특징주] 수주 기대에 급등" 은 수주 뉴스가 아니라
# **이미 오른 걸 보도한 기사**다. 아래에 두면 수주 칸이 사후보도로 오염된다.
PATTERNS: list[tuple[str, str]] = [
    ("사후보도_급등", r"특징주|급등|상한가|강세 마감|장 초반 강세|들썩|훨훨|질주"),
    ("사후보도_급락", r"급락|하한가|약세 마감|폭락|미끄러|추락"),
    ("자본조달_희석", r"유상증자|전환사채|신주인수권|블록딜|CB\b|BW\b|자금조달|차입"),
    ("주주환원", r"자사주|소각|배당|주주환원|무상증자"),
    ("수주_계약", r"수주|공급 ?계약|납품 ?계약|낙찰|공급한다|공급 계약|계약 체결|턴키|입찰"),
    ("실적_호", r"최대 (?:실적|매출|영업익|영업이익)|흑자전환|영업이익.*(?:증가|늘|급증)|호실적|어닝 ?서프"),
    ("실적_악", r"적자|영업이익.*(?:감소|줄|급감)|어닝 ?쇼크|실적 부진"),
    ("규제_법률", r"과징금|추징|세금|소송|압수수색|제재|리콜|담합|검찰|공정위|불복"),
    ("증권가_의견", r"목표가|투자의견|매수 ?의견|커버리지|리포트|애널리스트|증권.*전망"),
    ("지분_MA", r"인수|매각|합병|지분 ?(?:취득|매입|처분)|경영권|자회사 편입"),
    ("설비_투자", r"증설|신공장|양산|착공|준공|설비 ?투자|생산능력|캐파"),
    ("제품_기술", r"신제품|출시|개발 ?성공|양산 ?기술|특허|세계 최초|국산화"),
    ("협약_MOU", r"MOU|업무협약|맞손|협약 ?체결|파트너십|손잡"),
    ("ESG_홍보", r"ESG|지속가능|보고서 발간|사회공헌|기부|출연|캠페인|봉사|표창|후원"),
]
_COMPILED = [(name, re.compile(pat)) for name, pat in PATTERNS]


def classify_title(title: str) -> str | None:
    """제목 → 유형 하나(우선순위 최상단 일치). 아무것도 안 맞으면 None(=일반)."""
    for name, rx in _COMPILED:
        if rx.search(title):
            return name
    return None


def _next_trading_day(days: list[str]) -> dict[str, str]:
    """달력일 → 그 날 이후 첫 거래일. 기사일 당일이 거래일이면 그날."""
    out: dict[str, str] = {}
    if not days:
        return out
    td = sorted(days)
    all_days = pd.date_range(td[0], pd.Timestamp(td[-1]) + pd.Timedelta(days=5))
    j = 0
    for d in all_days:
        s = d.strftime("%Y-%m-%d")
        while j < len(td) and td[j] < s:
            j += 1
        if j < len(td):
            out[s] = td[j]
    return out


def phrase_table(con, panel: pd.DataFrame, baseline: dict,
                 min_n: int = 25) -> list[dict]:
    """유형별 이후 초과수익 표. panel = 거래일 × 티커 종가."""
    from ._config import VEC_DB
    import sqlite3

    days = [str(d)[:10] for d in panel.index]
    nxt = _next_trading_day(days)
    pos = {d: i for i, d in enumerate(days)}
    rets = panel.pct_change(fill_method=None)
    cum = {n: rets.rolling(n).sum().shift(-n) for n in (1, 5, 20)}

    links = con.execute("SELECT ticker, url_hash, day FROM mention_link").fetchall()
    by_hash: dict[str, list[tuple[str, str]]] = {}
    for tic, h, day in links:
        by_hash.setdefault(h, []).append((tic, day))

    src = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    titles = dict(src.execute("SELECT url_hash, title FROM articles").fetchall())
    src.close()

    buckets: dict[str, dict[int, list[float]]] = {}
    seen: set[tuple[str, str, str]] = set()      # (유형,티커,거래일) 중복 제거
    for h, pairs in by_hash.items():
        t = titles.get(h)
        if not t:
            continue
        kind = classify_title(t)
        if kind is None:
            continue
        for tic, day in pairs:
            if tic not in panel.columns:
                continue
            trade_day = nxt.get(day)
            if trade_day is None or (kind, tic, trade_day) in seen:
                continue
            seen.add((kind, tic, trade_day))
            i = pos[trade_day]
            for n in (1, 5, 20):
                v = cum[n].iloc[i][tic] if i < len(cum[n]) else np.nan
                if np.isfinite(v):
                    buckets.setdefault(kind, {}).setdefault(n, []).append(float(v))

    rows = []
    for kind, per_n in buckets.items():
        f5 = np.array(per_n.get(5, []), dtype=float)
        if len(f5) < min_n:
            continue
        f1 = np.array(per_n.get(1, []), dtype=float)
        f20 = np.array(per_n.get(20, []), dtype=float)
        b5 = baseline["fwd5"]["mean_pct"]
        b20 = baseline["fwd20"]["mean_pct"]
        rows.append({
            "kind": kind, "n": int(len(f5)),
            "fwd1_pct": round(float(f1.mean()) * 100, 2) if len(f1) else None,
            "fwd5_pct": round(float(f5.mean()) * 100, 2),
            "fwd5_excess_pp": round(float(f5.mean()) * 100 - b5, 2),
            # ⚠ SE 는 표본이 독립이라는 가정 위에 있다 — 같은 날 시장이 함께 움직이므로
            # 실제 불확실성은 이보다 크다. 하한선으로만 읽는다(|초과| < 2·SE 면 잡음).
            "fwd5_se_pp": round(float(f5.std(ddof=1)) * 100 / np.sqrt(len(f5)), 2),
            "fwd5_win": round(float((f5 > 0).mean()), 3),
            "fwd20_excess_pp": round(float(f20.mean()) * 100 - b20, 2) if len(f20) else None,
            "n20": int(len(f20)),
        })
    rows.sort(key=lambda r: -r["fwd5_excess_pp"])
    return rows
