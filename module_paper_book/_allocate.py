# -*- coding: utf-8 -*-
"""module_paper_book._allocate — 랩어카운트(wrap account) 배분 규율: 섹터 만다트·드리프트·베타·리밸런스.

장부를 '무차별 한 덩어리'가 아니라 **일임 만다트**로 굴린다. 섹터별 목표비중을 걸어두고,
현재 비중이 밴드를 벗어났는지 재고, 포트폴리오 베타가 목표 밴드 안인지 보고, 밴드로
되돌리는 결정론 리밸런스 안(案)을 만든다.

단일 원본(P1)
  · 만다트·섹터오버라이드 테이블은 **paper_book.db 안에** 산다(_book.connect 규약 재사용).
    두 번째 DB 를 만들지 않는다.
  · 시가평가는 `_mark.mark_book/get_price` 재사용 — 가격을 여기서 다시 긁지 않는다.
  · 집중도 상한은 `_risk.RiskParams(MAX_POS_PCT·MAX_THEME_PCT)` 재사용 — 상수를 복제하지 않는다.
  · 자기자본(원화환산)은 `_book.equity_krw` 재사용.
  · **베타는 이 파일이 소유한다** — 리포 전체를 뒤져도 회귀 베타 구현이 없었다
    (`module_flow._price_flow` 의 RS 는 '수익률 차'이지 공분산이 아니고,
     `module_fundamentals_us` 의 beta 는 yfinance `.info` 가 주는 남의 숫자다).

판단 경계(P4) — 여기가 어디까지 하고 어디부터 프로토콜인가
  · 이 모듈이 하는 것 = **결정론적으로 답이 하나인 것만**.
      - 섹터별 현재비중·목표비중·괴리(pp)·밴드 이탈 플래그
      - 종목별 베타(일별수익률 회귀)와 그 가중합(책 베타)
      - "이 섹터에서 X원을 덜어내야 밴드 안" 이라는 **금액**
      - 그 금액을 **이미 보유한 종목** 중에서 규칙으로 배분: 트림은 `스탑까지 거리가 가장
        가까운(=가장 약한) 종목` 우선, 동률이면 평가금액 큰 순 / 애드는 그 역순.
        규칙은 코드에 박혀 있고 인자로 바뀌지 않는다 — 재현 가능해야 하니까.
  · 이 모듈이 **하지 않는 것** = 답이 여럿인 것.
      - 언더웨이트 섹터에 **새 종목을 고르는 일**. 보유가 없으면 `NEEDS_CANDIDATE` 로
        금액만 남기고 비운다 — 어떤 이름을 넣을지는 리서치 데스크(프로토콜)의 몫이다.
      - 목표비중 자체를 정하는 일(만다트는 사람이 `mandate --set` 으로 건다).
      - 밴드를 벗어났으니 '지금 실행해야 한다'는 판단. 계획은 계획일 뿐,
        장부 반영은 사람이 `--commit` 을 칠 때만 일어난다(스케줄러 자동발사 없음).

섹터 출처
  · KR = `data/kr_universe/kr_all.csv` 의 `sector` 열, US = `data/us_universe/us_top300.csv`
    의 `gics_sector` 열. 유니버스에 없는 종목(ADR·비-top300)은 조용히 추측하지 않고
    `(unmapped)` 로 남기며, 사람이 `mandate --map TSM="Information Technology"` 로 박는다.
"""
from __future__ import annotations

import csv
import json
import math
import sqlite3
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from ._book import Position, equity_krw, get_cash, get_positions
from ._config import DATA_DIR, REPO_ROOT, is_kr_ticker, market_of
from ._mark import mark_book, position_pnl, price_move
from ._risk import RiskParams, concentration_check

# ── 벤치마크(시장별) — 베타의 기준축 ─────────────────────────────────────────────
BENCH = {"KR": "^KS11", "US": "SPY"}

DEFAULT_BAND_PP = 5.0          # 섹터 드리프트 허용 밴드(±pp)
DEFAULT_TARGET_BETA = 1.00     # 만다트 목표 베타
DEFAULT_BETA_BAND = 0.15       # 목표 베타 허용 밴드(±)
BETA_PERIOD = "1y"             # 베타 회귀 구간(일별 수익률)
MIN_BETA_OBS = 60              # 이보다 관측이 적으면 베타를 내지 않는다(빈칸이 추정보다 낫다)

UNMAPPED = "(unmapped)"

KR_UNIVERSE_CSV = DATA_DIR / "kr_universe" / "kr_all.csv"
US_UNIVERSE_CSV = DATA_DIR / "us_universe" / "us_top300.csv"

OUT_DIR = REPO_ROOT / "out" / "paper_book"

_WRAP_SCHEMA = """
CREATE TABLE IF NOT EXISTS mandate (
    market     TEXT NOT NULL,          -- 'KR' | 'US'
    sector     TEXT NOT NULL,          -- 유니버스 CSV 의 섹터명 그대로
    target_pct REAL NOT NULL,          -- 총자산(원화환산) 대비 목표비중 %
    band_pp    REAL NOT NULL DEFAULT 5.0,
    updated_at TEXT,
    PRIMARY KEY (market, sector)
);
CREATE TABLE IF NOT EXISTS mandate_meta (
    k TEXT PRIMARY KEY,
    v TEXT
);
CREATE TABLE IF NOT EXISTS sector_override (
    ticker     TEXT PRIMARY KEY,
    market     TEXT,
    sector     TEXT NOT NULL,
    updated_at TEXT
);
"""


def _now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def ensure_schema(conn: sqlite3.Connection) -> None:
    """만다트 테이블을 장부 DB 안에 보장(두 번째 DB 금지)."""
    conn.executescript(_WRAP_SCHEMA)


# ── 섹터 해석 ────────────────────────────────────────────────────────────────────
_UNIV_CACHE: dict[str, dict[str, str]] = {}


def _norm(ticker: str) -> str:
    """장부 티커 정규화: 'A005930'/'005930.KS' → '005930', 그 외 대문자."""
    t = ticker.strip().upper()
    if "." in t:
        head = t.split(".")[0]
        if head.isdigit():
            return head
    return t


def _universe_sectors(market: str) -> dict[str, str]:
    """유니버스 CSV → {정규화티커: 섹터}. 파일이 없으면 빈 dict(조용히 추측 금지)."""
    market = market.upper()
    if market in _UNIV_CACHE:
        return _UNIV_CACHE[market]
    path, col = (KR_UNIVERSE_CSV, "sector") if market == "KR" else (US_UNIVERSE_CSV, "gics_sector")
    out: dict[str, str] = {}
    if path.exists():
        with open(path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                t = _norm(r.get("ticker") or "")
                s = (r.get(col) or "").strip()
                if t and s:
                    out[t] = s
    _UNIV_CACHE[market] = out
    return out


def _universe_symbols(market: str) -> dict[str, str]:
    """{정규화티커: 유니버스 CSV 의 원래 심볼} — KR 의 .KS/.KQ 접미사 복원용."""
    key = f"{market.upper()}__sym"
    if key in _UNIV_CACHE:
        return _UNIV_CACHE[key]
    path = KR_UNIVERSE_CSV if market.upper() == "KR" else US_UNIVERSE_CSV
    out: dict[str, str] = {}
    if path.exists():
        with open(path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                raw = (r.get("ticker") or "").strip().upper()
                if raw:
                    out[_norm(raw)] = raw
    _UNIV_CACHE[key] = out
    return out


def yf_symbol(ticker: str) -> str:
    """yfinance 조회 심볼. KR 6자리는 유니버스의 .KS/.KQ 를 쓰고, 없으면 .KS 폴백."""
    t = _norm(ticker)
    if is_kr_ticker(t):
        return _universe_symbols("KR").get(t, f"{t}.KS")
    return t


def get_overrides(conn: sqlite3.Connection) -> dict[str, str]:
    ensure_schema(conn)
    return {r["ticker"]: r["sector"]
            for r in conn.execute("SELECT ticker, sector FROM sector_override").fetchall()}


def set_override(conn: sqlite3.Connection, ticker: str, sector: str) -> None:
    ensure_schema(conn)
    t = _norm(ticker)
    conn.execute(
        "INSERT OR REPLACE INTO sector_override(ticker, market, sector, updated_at) VALUES(?,?,?,?)",
        (t, market_of(t), sector, _now()),
    )


def resolve_sector(ticker: str, market: Optional[str] = None,
                   overrides: Optional[dict] = None) -> str:
    """티커 → 섹터. 우선순위: 사람이 박은 오버라이드 > 유니버스 CSV > `(unmapped)`."""
    t = _norm(ticker)
    if overrides and t in overrides:
        return overrides[t]
    mk = (market or market_of(t)).upper()
    return _universe_sectors(mk).get(t, UNMAPPED)


# ── 만다트(목표비중) ────────────────────────────────────────────────────────────
def set_mandate(conn: sqlite3.Connection, market: str, weights: dict[str, float],
                band_pp: float = DEFAULT_BAND_PP, replace_market: bool = True) -> dict:
    """섹터 목표비중을 건다. 단위 = **총자산(원화환산) 대비 %**.

    합이 100 을 넘으면 거부(현금 목표가 음수가 된다). 100 미만이면 잔여가 현금 목표.
    """
    ensure_schema(conn)
    mk = market.upper()
    total = sum(float(v) for v in weights.values())
    if total > 100.0 + 1e-9:
        raise ValueError(f"목표비중 합 {total:.1f}% > 100% — 현금 목표가 음수가 된다")
    if replace_market:
        conn.execute("DELETE FROM mandate WHERE market=?", (mk,))
    for sector, w in weights.items():
        conn.execute(
            "INSERT OR REPLACE INTO mandate(market, sector, target_pct, band_pp, updated_at) "
            "VALUES(?,?,?,?,?)", (mk, sector.strip(), float(w), float(band_pp), _now()),
        )
    return {"market": mk, "n": len(weights), "sum_pct": round(total, 2),
            "band_pp": band_pp}


def get_mandate(conn: sqlite3.Connection, market: Optional[str] = None) -> list[dict]:
    ensure_schema(conn)
    q = "SELECT market, sector, target_pct, band_pp, updated_at FROM mandate"
    args: tuple = ()
    if market:
        q += " WHERE market=?"
        args = (market.upper(),)
    q += " ORDER BY market, target_pct DESC, sector"
    return [dict(r) for r in conn.execute(q, args).fetchall()]


def set_meta(conn: sqlite3.Connection, k: str, v) -> None:
    ensure_schema(conn)
    conn.execute("INSERT OR REPLACE INTO mandate_meta(k, v) VALUES(?, ?)", (k, str(v)))


def get_meta(conn: sqlite3.Connection, k: str, default=None):
    ensure_schema(conn)
    r = conn.execute("SELECT v FROM mandate_meta WHERE k=?", (k,)).fetchone()
    return r["v"] if r else default


def mandate_beta_target(conn: sqlite3.Connection) -> tuple[float, float]:
    return (float(get_meta(conn, "target_beta", DEFAULT_TARGET_BETA)),
            float(get_meta(conn, "beta_band", DEFAULT_BETA_BAND)))


# ── 현재 비중(시가평가 기준) ─────────────────────────────────────────────────────
def marks_for_book(conn: sqlite3.Connection) -> dict:
    """`_mark.mark_book` + 실패분만 `_mark.price_move`(yfinance) 로 메움.

    비중은 분모가 총자산이라 **한 종목이라도 원가로 평가되면 만다트 전체가 흔들린다**.
    KR 마크는 KIS 인증이 필요한데(`_mark.get_price`) 키가 없는 PC 에선 통째로 None 이 된다 —
    그때만 `mark_book(fallback=…)` 의 설계된 훅으로 yfinance 종가를 넣는다.
    새 가격 코드는 없다(P1): 두 함수 모두 `_mark` 소유.
    """
    marks = mark_book(conn)
    missing = [t for t, v in marks.items() if v is None]
    if not missing:
        return marks
    for t in missing:
        mv = price_move(t)
        if mv.get("price") is not None:
            marks[t] = mv["price"]
    return marks



def position_weights(conn: sqlite3.Connection, fx: float,
                     marks: Optional[dict] = None) -> dict:
    """열린 포지션 전부를 시가평가해 원화환산 평가액·비중(총자산 대비)을 낸다.

    마크 실패 종목은 평단으로 평가하고 `mark_ok=False` 로 표시한다(빈칸을 0 으로 치지 않되,
    비중 분모를 왜곡하지 않게 원가로 대체한 사실을 드러낸다).
    """
    marks = marks_for_book(conn) if marks is None else marks
    eq = equity_krw(conn, marks, fx)
    overrides = get_overrides(conn)
    rows = []
    for p in get_positions(conn, open_only=True):
        px = marks.get(p.ticker)
        mark_ok = px is not None
        px_used = px if mark_ok else p.avg_cost
        rate = 1.0 if p.currency == "KRW" else fx
        val_krw = px_used * p.qty * rate
        pnl = position_pnl(p, px)
        rows.append({
            "ticker": p.ticker, "market": p.market, "currency": p.currency,
            "name": p.name, "qty": p.qty, "price": px_used, "mark_ok": mark_ok,
            "sector": resolve_sector(p.ticker, p.market, overrides),
            "theme": p.theme, "stop": p.stop,
            "stop_dist_pct": pnl.get("stop_dist_pct"),
            "value_krw": val_krw,
            "weight_pct": (val_krw / eq * 100.0) if eq > 0 else 0.0,
        })
    rows.sort(key=lambda r: -r["value_krw"])
    cash_krw, cash_usd = get_cash(conn, "KRW"), get_cash(conn, "USD")
    cash_total_krw = cash_krw + cash_usd * fx
    return {
        "equity_krw": eq, "fx": fx,
        "cash_krw": cash_krw, "cash_usd": cash_usd,
        "cash_pct": (cash_total_krw / eq * 100.0) if eq > 0 else 0.0,
        "positions": rows,
    }


def sector_drift(conn: sqlite3.Connection, fx: float,
                 marks: Optional[dict] = None) -> dict:
    """섹터별 현재비중 vs 만다트 목표 → 괴리(pp) + 밴드 이탈 플래그.

    만다트에 없는데 보유 중인 섹터는 target 0 으로 잡아 **전액 오버웨이트**로 드러낸다
    (조용히 빠지면 만다트 밖 노출이 안 보인다).
    """
    w = position_weights(conn, fx, marks)
    mandate = get_mandate(conn)
    cur: dict[tuple[str, str], float] = {}
    for p in w["positions"]:
        k = (p["market"], p["sector"])
        cur[k] = cur.get(k, 0.0) + p["weight_pct"]

    rows = []
    seen = set()
    for m in mandate:
        k = (m["market"], m["sector"])
        seen.add(k)
        c = cur.get(k, 0.0)
        drift = c - m["target_pct"]
        band = m["band_pp"]
        rows.append({
            "market": m["market"], "sector": m["sector"],
            "target_pct": m["target_pct"], "current_pct": round(c, 2),
            "drift_pp": round(drift, 2), "band_pp": band,
            "breach": "OVER" if drift > band else "UNDER" if drift < -band else "",
        })
    for k, c in cur.items():
        if k in seen:
            continue
        rows.append({
            "market": k[0], "sector": k[1], "target_pct": 0.0,
            "current_pct": round(c, 2), "drift_pp": round(c, 2),
            "band_pp": 0.0, "breach": "OVER" if c > 0 else "",
            "off_mandate": True,
        })
    rows.sort(key=lambda r: -abs(r["drift_pp"]))
    target_sum = sum(m["target_pct"] for m in mandate)
    return {
        "equity_krw": w["equity_krw"], "fx": fx,
        "cash_pct": round(w["cash_pct"], 2),
        "cash_target_pct": round(100.0 - target_sum, 2),
        "mandate_sum_pct": round(target_sum, 2),
        "sectors": rows, "positions": w["positions"],
        "n_breach": sum(1 for r in rows if r["breach"]),
    }


# ── 베타 (이 파일이 단일 원본) ───────────────────────────────────────────────────
def _daily_returns(symbols: list[str], period: str = BETA_PERIOD):
    """yfinance 일괄 다운로드 → 일별 수익률 DataFrame. 실패하면 None(추정 금지)."""
    import pandas as pd  # noqa: F401  (pandas 는 데이터 모듈 허용 의존)
    import yfinance as yf
    uniq = sorted(set(symbols))
    if not uniq:
        return None
    df = yf.download(uniq, period=period, progress=False, auto_adjust=True)
    if df is None or len(df) == 0:
        return None
    close = df["Close"] if "Close" in df.columns else df
    if hasattr(close, "to_frame") and getattr(close, "ndim", 2) == 1:
        close = close.to_frame(uniq[0])
    return close.pct_change(fill_method=None).dropna(how="all")


def compute_betas(tickers: list[str], market: str, period: str = BETA_PERIOD) -> dict:
    """일별 수익률 회귀 베타 = cov(r_i, r_bench) / var(r_bench).

    벤치: KR `^KS11`, US `SPY`(BENCH). 관측이 MIN_BETA_OBS 미만이면 None —
    빈칸이 추정보다 낫다(P4). 반환: {ticker: {"beta":…, "n_obs":…, "bench":…}}
    """
    mk = market.upper()
    bench = BENCH[mk]
    syms = [yf_symbol(t) for t in tickers]
    rets = _daily_returns(syms + [bench], period)
    out: dict[str, dict] = {}
    if rets is None or bench not in rets.columns:
        return {t: {"beta": None, "n_obs": 0, "bench": bench, "error": "no data"} for t in tickers}
    b = rets[bench]
    var_b = float(b.var())
    for t, sym in zip(tickers, syms):
        if sym not in rets.columns:
            out[t] = {"beta": None, "n_obs": 0, "bench": bench, "error": "symbol missing"}
            continue
        pair = rets[[sym, bench]].dropna()
        n = len(pair)
        if n < MIN_BETA_OBS or var_b <= 0:
            out[t] = {"beta": None, "n_obs": n, "bench": bench, "error": "short history"}
            continue
        cov = float(pair[sym].cov(pair[bench]))
        v = float(pair[bench].var())
        out[t] = {"beta": round(cov / v, 3) if v > 0 else None, "n_obs": n, "bench": bench}
    return out


def book_beta(conn: sqlite3.Connection, fx: float, marks: Optional[dict] = None,
              period: str = BETA_PERIOD) -> dict:
    """책 전체의 가중 베타.

    · 종목 베타는 **자기 시장의 벤치** 기준(KR=^KS11, US=SPY). 두 시장을 하나의 숫자로
      합칠 때는 각자의 시장베타를 그대로 가중평균한다 — KR/US 를 잇는 단일 벤치가 없으니
      이건 '통화·시장 혼합 근사'다. 절대값 비교가 아니라 **만다트 밴드 대비 관리**용.
    · 분모는 총자산(현금 포함, 현금 베타=0) → 현금이 많으면 책 베타는 자연히 낮아진다.
      투자자산만 본 `invested_beta` 도 같이 낸다.
    """
    w = position_weights(conn, fx, marks)
    by_mkt: dict[str, list[str]] = {}
    for p in w["positions"]:
        by_mkt.setdefault(p["market"], []).append(p["ticker"])
    betas: dict[str, dict] = {}
    for mk, tks in by_mkt.items():
        betas.update(compute_betas(tks, mk, period))

    eq = w["equity_krw"]
    num = den_invested = num_invested = 0.0
    rows = []
    for p in w["positions"]:
        info = betas.get(p["ticker"], {})
        beta = info.get("beta")
        wt = p["weight_pct"]
        rows.append({**p, "beta": beta, "n_obs": info.get("n_obs"),
                     "bench": info.get("bench"), "beta_error": info.get("error"),
                     "beta_contrib": round(beta * wt / 100.0, 4) if beta is not None else None})
        if beta is not None:
            num += beta * wt / 100.0
            num_invested += beta * p["value_krw"]
            den_invested += p["value_krw"]
    target, band = mandate_beta_target(conn)
    bb = round(num, 3)
    inv_b = round(num_invested / den_invested, 3) if den_invested > 0 else None
    missing = [r["ticker"] for r in rows if r["beta"] is None]
    return {
        "equity_krw": eq, "fx": fx, "period": period,
        "book_beta": bb, "invested_beta": inv_b,
        "target_beta": target, "beta_band": band,
        "beta_breach": "HIGH" if bb > target + band else "LOW" if bb < target - band else "",
        "cash_pct": round(w["cash_pct"], 2),
        "missing_beta": missing,
        "positions": rows,
    }


# ── 리밸런스 계획 ────────────────────────────────────────────────────────────────
def _trim_rank(p: dict) -> tuple:
    """트림 우선순위: 스탑까지 거리가 가까운(=약한) 것 먼저, 동률이면 평가금액 큰 것 먼저.

    스탑 미설정은 '약함의 증거 없음' 이므로 뒤로(1e9). 규칙은 고정 — 재현성이 목적.
    """
    d = p.get("stop_dist_pct")
    return (d if d is not None else 1e9, -p["value_krw"])


def _add_rank(p: dict) -> tuple:
    """애드 우선순위: 스탑까지 거리가 먼(=버티는) 것 먼저, 동률이면 평가금액 작은 것 먼저."""
    d = p.get("stop_dist_pct")
    return (-(d if d is not None else -1e9), p["value_krw"])


def rebalance_plan(conn: sqlite3.Connection, fx: float, marks: Optional[dict] = None,
                   to: str = "target", params: Optional[RiskParams] = None,
                   with_beta: bool = False) -> dict:
    """밴드를 벗어난 섹터를 되돌리는 **결정론 트림/애드 목록**.

    to='target' → 목표비중까지 완전복원(기관 랩의 표준). to='band' → 밴드 가장자리까지만.
    보유 종목 안에서만 배분한다. 언더웨이트인데 그 섹터 보유가 없으면 종목을 **고르지 않고**
    `NEEDS_CANDIDATE` 로 금액만 남긴다(P4 — 이름 고르기는 리서치 데스크의 판단).

    가드(재사용): 단일종목 `MAX_POS_PCT` 상한을 넘겨 사지 않고, 계획 반영 후의 가상 장부에
    `_risk.concentration_check` 를 다시 돌려 테마 상한(`MAX_THEME_PCT`) 위반을 표시한다.
    """
    prm = params or RiskParams()
    marks = marks_for_book(conn) if marks is None else marks
    d = sector_drift(conn, fx, marks)
    eq = d["equity_krw"]
    positions = d["positions"]
    by_sector: dict[tuple[str, str], list[dict]] = {}
    for p in positions:
        by_sector.setdefault((p["market"], p["sector"]), []).append(p)

    legs: list[dict] = []
    unfilled: list[dict] = []
    # 통화별 가용현금. **트림을 먼저 전부 처리**한 뒤 애드를 처리한다 — 안 그러면
    # 섹터 처리 순서(괴리 큰 순)에 따라 "아직 안 판 돈으로 못 산다"는 가짜 제약이 생긴다.
    cash_avail = {"KRW": get_cash(conn, "KRW"), "USD": get_cash(conn, "USD")}
    delta_qty: dict[str, float] = {}

    # 처리 순서: 매도(트림) 전부 → 매수(애드) 괴리 큰 순
    def _order_key(s: dict) -> tuple:
        return (0 if s["drift_pp"] > 0 else 1, -abs(s["drift_pp"]))

    for s in sorted([x for x in d["sectors"] if x["breach"]], key=_order_key):
        drift = s["drift_pp"]
        band = s["band_pp"]
        target_pp = abs(drift) if to == "target" else max(abs(drift) - band, 0.0)
        amount_krw = target_pp / 100.0 * eq
        if amount_krw <= 0:
            continue
        key = (s["market"], s["sector"])
        pool = by_sector.get(key, [])
        side = "sell" if drift > 0 else "buy"
        ranked = sorted(pool, key=_trim_rank if side == "sell" else _add_rank)
        remaining = amount_krw

        if side == "buy" and not pool:
            unfilled.append({"market": s["market"], "sector": s["sector"], "side": "buy",
                             "amount_krw": round(amount_krw), "gap_pp": round(target_pp, 2),
                             "drift_pp": round(drift, 2),
                             "note": "NEEDS_CANDIDATE — 그 섹터 보유 0. 종목 선정은 프로토콜(P4)"})
            continue

        for p in ranked:
            if remaining <= 1e-6:
                break
            rate = 1.0 if p["currency"] == "KRW" else fx
            px = p["price"]
            if not px or px <= 0:
                continue
            unit_krw = px * rate
            if side == "sell":
                cap_krw = p["value_krw"]                       # 전량까지만
            else:
                headroom_pct = prm.max_pos_pct - p["weight_pct"]
                cap_krw = max(headroom_pct, 0.0) / 100.0 * eq  # 단일종목 상한 준수
                cash_cap = cash_avail.get(p["currency"], 0.0) * rate
                cap_krw = min(cap_krw, cash_cap)
            take_krw = min(remaining, cap_krw)
            qty = math.floor(take_krw / unit_krw)
            if qty < 1:
                continue
            amt_krw = qty * unit_krw
            amt_local = qty * px
            remaining -= amt_krw
            if side == "sell":
                cash_avail[p["currency"]] = cash_avail.get(p["currency"], 0.0) + amt_local
            else:
                cash_avail[p["currency"]] = cash_avail.get(p["currency"], 0.0) - amt_local
            delta_qty[p["ticker"]] = delta_qty.get(p["ticker"], 0.0) + (-qty if side == "sell" else qty)
            new_val = p["value_krw"] + (-amt_krw if side == "sell" else amt_krw)
            legs.append({
                "market": s["market"], "sector": s["sector"], "ticker": p["ticker"],
                "name": p["name"], "side": side, "qty": qty, "price": px,
                "currency": p["currency"], "amount_local": round(amt_local, 2),
                "amount_krw": round(amt_krw),
                "weight_before_pct": round(p["weight_pct"], 2),
                "weight_after_pct": round(new_val / eq * 100.0, 2) if eq > 0 else 0.0,
                "stop_dist_pct": (round(p["stop_dist_pct"], 1)
                                  if p["stop_dist_pct"] is not None else None),
                "rule": ("트림: 스탑거리 최소 우선" if side == "sell"
                         else "애드: 스탑거리 최대 우선"),
            })
        # 남은 잔여가 **아직도 밴드 밖**일 때만 미충족으로 올린다(밴드 안이면 목적 달성).
        resid_pp = remaining / eq * 100.0 if eq > 0 else 0.0
        if resid_pp > band:
            ccy = "KRW" if s["market"] == "KR" else "USD"
            if side == "buy":
                note = (f"NEEDS_CANDIDATE — 보유분으론 부족(단일종목 {prm.max_pos_pct:.0f}% 상한 / "
                        f"{ccy} 슬리브 잔액 {cash_avail.get(ccy, 0):,.0f}). 종목 선정은 프로토콜(P4)")
            else:
                note = "보유분 전량으로도 부족 — 섹터 목표 재검토"
            unfilled.append({
                "market": s["market"], "sector": s["sector"], "side": side,
                "amount_krw": round(remaining), "gap_pp": round(resid_pp, 2),
                "sleeve": ccy, "sleeve_cash": round(cash_avail.get(ccy, 0.0), 2),
                "note": note,
            })

    # 계획 반영 후 가상 장부에 집중도 가드 재적용(테마 상한은 _risk 소유)
    proj_positions, proj_marks = [], {}
    for p in get_positions(conn, open_only=True):
        newq = p.qty + delta_qty.get(p.ticker, 0.0)
        if newq <= 0:
            continue
        proj_positions.append(replace(p, qty=newq))
        proj_marks[p.ticker] = marks.get(p.ticker)
    proj_flags = concentration_check(proj_positions, proj_marks, eq, fx, prm)

    return {
        "asof": _now(), "fx": fx, "equity_krw": eq, "mode": to,
        "cash_target_pct": d["cash_target_pct"], "cash_pct": d["cash_pct"],
        "sectors": d["sectors"], "legs": legs, "unfilled": unfilled,
        "projected_concentration_flags": proj_flags,
        "n_breach": d["n_breach"],
        "beta": book_beta(conn, fx, marks) if with_beta else None,
    }


def save_plan(plan: dict, date: Optional[str] = None) -> Path:
    """계획을 `out/paper_book/WRAP_REBALANCE_{date}.json` 으로 저장(커밋 대상 아님)."""
    date = date or datetime.now().strftime("%Y-%m-%d")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    p = OUT_DIR / f"WRAP_REBALANCE_{date}.json"
    slim = {k: v for k, v in plan.items() if k != "beta"}
    if plan.get("beta"):
        slim["beta"] = {k: v for k, v in plan["beta"].items() if k != "positions"}
    p.write_text(json.dumps(slim, ensure_ascii=False, indent=2), encoding="utf-8")
    return p
