"""네이버 금융 종목 페이지에서 밸류에이션·수급 지표를 한 번에 긁어온다.

KRX는 2026년부터 인증을 요구해 pykrx 무인증 사용이 막혔다 — Naver 스크랩이 가장 안정적인 무인증 경로.
출처: https://finance.naver.com/item/main.naver?code=<6자리>
"""
from __future__ import annotations

import re
from dataclasses import dataclass, asdict
from typing import Optional

import requests
from bs4 import BeautifulSoup

_HEADERS = {"User-Agent": "Mozilla/5.0"}
_URL = "https://finance.naver.com/item/main.naver?code={code}"


@dataclass
class NaverSnapshot:
    code: str
    name: Optional[str] = None
    price: Optional[float] = None              # 현재가 (원)
    market_cap_eok: Optional[float] = None     # 시가총액 (억원)
    listed_shares: Optional[int] = None        # 상장주식수
    foreign_pct: Optional[float] = None        # 외국인 소진율 (%)
    target_price: Optional[float] = None       # 컨센 목표주가 (원)
    invest_opinion: Optional[float] = None     # 투자의견 (1~5, 4=매수)
    week52_high: Optional[float] = None
    week52_low: Optional[float] = None
    per_ttm: Optional[float] = None            # 최근 4분기 PER
    eps_ttm: Optional[float] = None
    per_fwd: Optional[float] = None            # 추정 PER (12M Fwd 컨센)
    eps_fwd: Optional[float] = None            # 추정 EPS
    pbr: Optional[float] = None
    bps: Optional[float] = None
    div_yield: Optional[float] = None          # 배당수익률 (%)
    industry_per: Optional[float] = None       # 동일업종 PER

    def upside_pct(self) -> Optional[float]:
        if self.target_price and self.price:
            return round((self.target_price / self.price - 1) * 100, 2)
        return None


def _to_float(s: str) -> Optional[float]:
    if s is None:
        return None
    s = s.replace(",", "").replace("%", "").replace("배", "").replace("원", "").strip()
    if s in {"", "-", "N/A"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _parse_market_cap(text: str) -> Optional[float]:
    """'45조 1,310억원' → 451310.0 (억원 단위)"""
    # 콤마·공백·탭·개행·파이프를 모두 제거하고 매칭 — 네이버 표는 br/td 경계가 잡혀
    # '45조|1,310|억원' 형태로 들어와 '|' 도 같이 제거해야 '45조1310억원'으로 합쳐진다
    cleaned = re.sub(r"[\s,|]", "", text)
    m = re.search(r"(\d+)조(?:(\d+)억)?", cleaned)
    if m:
        jo = int(m.group(1))
        eok = int(m.group(2)) if m.group(2) else 0
        return jo * 10_000 + eok
    m = re.search(r"(\d+)억", cleaned)
    if m:
        return float(m.group(1))
    return None


def fetch_naver_snapshot(code: str, timeout: int = 15) -> NaverSnapshot:
    """6자리 종목코드를 받아 네이버 금융 페이지에서 스냅샷을 긁어온다."""
    code = str(code).zfill(6)
    snap = NaverSnapshot(code=code)
    r = requests.get(_URL.format(code=code), headers=_HEADERS, timeout=timeout)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")

    # 종목명
    nm = soup.select_one("div.wrap_company h2")
    if nm:
        snap.name = nm.get_text(strip=True)

    # 현재가 — p.no_today 의 첫 .blind 가 "1,252,000" 형태로 들어있다
    price_el = soup.select_one("p.no_today .blind")
    if price_el:
        snap.price = _to_float(price_el.get_text(strip=True))

    # 투자정보 박스(#tab_con1) 안의 항목들
    tab1 = soup.select_one("#tab_con1")
    if tab1:
        text = tab1.get_text("|", strip=True)

        # 시가총액
        m = re.search(r"시가총액\|시가총액\|([^|]+(?:\|[^|]+)?)\|억원", text)
        if m:
            snap.market_cap_eok = _parse_market_cap(m.group(0))

        # 상장주식수
        m = re.search(r"상장주식수\|([\d,]+)", text)
        if m:
            snap.listed_shares = int(m.group(1).replace(",", ""))

        # 외국인 소진율 — '...|36.61%' 패턴
        m = re.search(r"외국인\(한도\)소진율[^|]*\|[^|]*\|[^|]*\|([\d.]+)%", text)
        if m:
            snap.foreign_pct = _to_float(m.group(1))
        else:
            # 일부 종목은 한도/보유 안내 텍스트 길이가 달라서 마지막 % 값을 잡는다
            m = re.search(r"외국인소진율[^%]*?([\d.]+)%", text)
            if m:
                snap.foreign_pct = _to_float(m.group(1))

        # 투자의견 / 목표주가 — '|4.00|매수|l|1,450,667|52주최고'
        m = re.search(r"투자의견\|투자의견\|l\|목표주가\|([\d.]+)\|[^|]+\|l\|([\d,]+)", text)
        if m:
            snap.invest_opinion = _to_float(m.group(1))
            snap.target_price = _to_float(m.group(2))

        # 52주 최고/최저
        m = re.search(r"52주최고\|l\|최저\|([\d,]+)\|l\|([\d,]+)", text)
        if m:
            snap.week52_high = _to_float(m.group(1))
            snap.week52_low = _to_float(m.group(2))

        # 동일업종 PER
        m = re.search(r"동일업종\s*PER\|동일업종\s*PER\|([\d.]+)\|배", text)
        if m:
            snap.industry_per = _to_float(m.group(1))

    # PER/PBR 표 — table.per_table
    per_rows = soup.select("table.per_table tr")
    for tr in per_rows:
        label = tr.select_one("th")
        if not label:
            continue
        label_text = label.get_text(" ", strip=True)
        cells = [td.get_text(" ", strip=True) for td in tr.select("td")]
        # cells 보통 한 줄에 2개의 값이 들어있다 (예: '61.60 배', '20,324 원')
        nums = []
        for c in cells:
            for token in re.findall(r"[\d,]+\.?\d*", c):
                if "," in token or "." in token or len(token) >= 3:
                    nums.append(_to_float(token))
        if "추정" in label_text and "PER" in label_text:
            if len(nums) >= 2:
                snap.per_fwd, snap.eps_fwd = nums[0], nums[1]
        elif "PER" in label_text and "EPS" in label_text:
            if len(nums) >= 2:
                snap.per_ttm, snap.eps_ttm = nums[0], nums[1]
        elif "PBR" in label_text:
            if len(nums) >= 2:
                snap.pbr, snap.bps = nums[0], nums[1]
        elif "배당수익률" in label_text:
            if nums:
                snap.div_yield = nums[-1]

    return snap


def to_dict(snap: NaverSnapshot) -> dict:
    d = asdict(snap)
    d["upside_pct"] = snap.upside_pct()
    return d
