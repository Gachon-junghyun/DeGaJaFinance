# -*- coding: utf-8 -*-
"""sector_flow — 유니버스 수급 와이드 스윕(수치화 → 섹터·랭킹). 데스크 최상단 오프닝 스윕.

왜: 이름(watchlist)부터 보면 터널에 빠진다. 이 스윕은 데스크가 '돈이 어느 섹터로 흐르나'를
    정량 맵으로 먼저 잡게 한다 — flow_read 4축을 유니버스 전체에 돌려 수치화(flow_score)하고
    시총가중 GICS 섹터로 접어 랭킹. find-cycle의 반-터널 철학 + industry-us Phase 1 로테이션의
    노이즈 뉴스카운트 대체가 목적.

엔진 재사용(수식 이식 0): scripts/flow_read.py 의 price_flow / news_velocity / flow_tag 를 import.
  price_flow(tk, bench_close, df=slice) 로 배치다운로드 프레임을 주입해 동일 수식 재사용.
유니버스: data_build/us_universe/us_top300.csv (clean gics_sector + market_cap_usd).

flow_score(∈[-1,1]) = 4축 클립 평균(스케일 휴리스틱):
  뉴스 (vel-1)/0.4 · OBV obv_norm/0.16 · RS20 rs20/8.0 · 서지 (surge-1)/0.6  (뉴스 n/a면 3축 평균)
합성태그(🟢/🟡/🔴)는 flow_read.flow_tag 권위값 그대로. flow_score는 랭킹·집계용 수치 레이어.

Δflow: llm_outputs/sector_flow/history.json 에 asof(마지막 일봉일)별 {ticker:[score,tag]} 스냅샷.
  직전 스냅샷 대비 Δscore, 오늘 🟢로 처음 전환 = 신규🟢(사이클 점화 tell).

출력: stdout=데이터(리포트 or --json), stderr=진행로그(파이프로 받아도 안 섞임).

사용:
  python -X utf8 scripts/sector_flow.py                     # 전체 리포트
  python -X utf8 scripts/sector_flow.py --json              # stdout JSON
  python -X utf8 scripts/sector_flow.py --sector Energy     # 한 섹터 전 종목 테이블
  python -X utf8 scripts/sector_flow.py --tickers MPC PSX VLO --positioning
  python -X utf8 scripts/sector_flow.py --top 15 --no-news --refresh
"""
from __future__ import annotations
import argparse
import csv
import json
import math
import pickle
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

import flow_read  # 같은 scripts/ — 엔진 재사용(수식 이식 0)
from module_flow._config import kr_code  # KR 티커 자동판별(P3) — 뉴스 스코프 결정에 필요

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "llm_outputs" / "sector_flow"

# ── 시장 설정 (--market으로 선택; 유니버스 경로·벤치·컬럼명·캐시 네임스페이스) ──
MARKETS = {
    "us": {"universe": ROOT / "data" / "us_universe" / "us_top300.csv",
           "bench": "SPY",   "mcap": "market_cap_usd", "sector": "gics_sector",
           "industry": "gics_industry"},
    "kr": {"universe": ROOT / "data" / "kr_universe" / "kr_all.csv",
           "bench": "^KS11", "mcap": "market_cap_krw", "sector": "sector",
           "industry": None},
}
# 아래 4개는 main()에서 --market 으로 재설정(기본 us — 기존 동작 보존).
MKT = "us"
UNIVERSE = MARKETS["us"]["universe"]
HISTORY = OUT_DIR / "history.json"
BENCH = "SPY"
COLS = MARKETS["us"]


def log(*a):
    """진행로그는 stderr로 (stdout=데이터 순수 유지)."""
    print(*a, file=sys.stderr, flush=True)


# ── 유니버스 ─────────────────────────────────────────────────────────────
def load_universe(sector: str | None, tickers: list[str] | None) -> list[dict]:
    rows = []
    with open(UNIVERSE, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({
                "ticker": (r.get("ticker") or "").strip(),
                "name": (r.get("name") or "").strip(),
                "sector": (r.get(COLS["sector"]) or "").strip(),
                "industry": (r.get(COLS["industry"]) or "").strip() if COLS["industry"] else "",
                "mcap": float(r[COLS["mcap"]]) if r.get(COLS["mcap"]) else 0.0,
            })
    rows = [x for x in rows if x["ticker"]]
    if tickers:
        want = {t.upper() for t in tickers}
        rows = [x for x in rows if x["ticker"].upper() in want]
        # 유니버스에 없는 요청 티커는 최소 정보로 보강(섹터/시총 미상)
        have = {x["ticker"].upper() for x in rows}
        for t in tickers:
            if t.upper() not in have:
                rows.append({"ticker": t.upper(), "name": "", "sector": "(unlisted)",
                             "industry": "", "mcap": 0.0})
    elif sector:
        s = sector.lower()
        rows = [x for x in rows if s in x["sector"].lower()]
    return rows


# ── 가격 배치다운로드(당일 캐시) ──────────────────────────────────────────
def batch_prices(tickers: list[str], refresh: bool):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    suf = "" if MKT == "us" else f"_{MKT}"   # 시장별 캐시 네임스페이스(US↔KR 티커 충돌 방지)
    cache = OUT_DIR / f"prices{suf}_{today}.pkl"
    syms = sorted(set(tickers) | {BENCH})
    if cache.exists() and not refresh:
        with open(cache, "rb") as f:
            cached = pickle.load(f)
        have = set(cached.columns.get_level_values(0)) if isinstance(cached.columns, pd.MultiIndex) else set()
        missing = [s for s in syms if s not in have]
        if not missing:
            log(f"[cache] {cache.name} 재사용 ({len(syms)}종목 커버)")
            return cached
        log(f"[cache] {cache.name} 커버부족({len(missing)}종목 누락) → 재다운로드")
    log(f"[dl] yfinance 배치 {len(syms)}종목 4mo …")
    data = yf.download(syms, period="4mo", auto_adjust=False, group_by="ticker",
                       progress=False, threads=True)
    with open(cache, "wb") as f:
        pickle.dump(data, f)
    log(f"[dl] 완료 → {cache.name}")
    return data


def slice_frame(data, tk: str) -> pd.DataFrame | None:
    """배치 프레임에서 단일 티커 OHLCV 슬라이스(price_flow가 먹는 형태)."""
    try:
        if isinstance(data.columns, pd.MultiIndex):
            if tk not in data.columns.get_level_values(0):
                return None
            df = data[tk].dropna(how="all")
        else:
            df = data  # 단일 티커 다운로드였던 경우
        return df if df is not None and not df.empty else None
    except Exception:
        return None


# ── flow_score 수치화 ────────────────────────────────────────────────────
def clip(x):
    return max(-1.0, min(1.0, x))


def _finite(x):
    """NaN·inf 는 축이 될 수 없다.

    ⚠ `clip(nan)` 은 **+1.0** 이다 — `min(1.0, nan)` 이 파이썬에서 1.0 을 돌려주기 때문.
    즉 예전 구현에서 **결측 축이 최대 양수 점수**가 됐다(D225-KR (b)).
    실측 2026-08-09: `vol_surge` NaN 인 20종이 전부 동일 대체 패널을 달고 `flow_score +0.667`,
    같은 자리에서 **측정된** `vol_surge=0.0` 인 031440 은 그 절반.
    """
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


# 속도축을 점수에 넣으려면 유니버스의 이 비율 이상에서 실제로 측정돼야 한다(D225-KR (a)).
VEL_COVERAGE_MIN = 0.80


def price_axes(p: dict) -> list[float] | None:
    """가격 3축. 하나라도 결측이면 **None** — 점수를 주는 대신 집계에서 뺀다.

    예전엔 결측이 `clip(nan)=+1.0` 으로 들어가 **점수를 받았다.** 유니버스에서 빠지는 것과
    최고점을 받는 것은 정반대다(P4: 모르면 빈칸, 지어내지 않는다).
    """
    obv = _finite(p.get("obv_norm"))
    rs20 = _finite(p.get("rs20"))
    vs = _finite(p.get("vol_surge"))
    if obv is None or rs20 is None or vs is None:
        return None
    return [clip(obv / 0.16), clip(rs20 / 8.0), clip((vs - 1.0) / 0.6)]


def flow_score(p: dict, vel, use_vel_axis: bool) -> float | None:
    """축 개수를 **종목마다 다르게 두지 않는다** (D225-KR (a), 2026-08-09).

    예전 구현은 `if vel is not None:` 으로 4번째 축을 **종목별로** 드롭했다. 드롭한 종목은
    3축 평균, 넣은 종목은 4축 평균이라 **같은 척도가 아니다** — 그런데 두 값이 그대로
    섹터 wflow/eqflow 로 평균된다.

    일반형: 속도축이 하한(−1.0)일 때  **3축평균 − 4축평균 = (s₃+3)/12 ∈ [0, +0.5]**
    (s₃ = 가격 3축의 합 ∈ [−3,3]) ⇒ **드롭은 어떤 s₃ 에서도 손해가 아니고 최대 +0.5 이득.**
    실측: 827종 중 **799종(96.6%)** 이 3축이었고 평균 보너스 **+0.305**. 결측이 측정을 이겼다.

    고침: 속도축은 **런 단위로 전원 포함이거나 전원 제외**(`use_vel_axis`). 포함하기로 한
    런에서 개별 종목의 속도가 결측이면 그 종목은 **점수 없음**(=집계 제외)이지, 3축으로
    슬쩍 내려앉지 않는다.

    ⚠ 이 함수는 `module_flow._synthesize.flow_tag` 를 건드리지 않는다. 태그 쪽은 같은 결측을
    **양쪽(green·red) 어디에도 넣지 않아** 규칙 C3 대로 중립이다 — 거기엔 척도 버그가 없다.
    """
    if "error" in p:
        return None
    axes = price_axes(p)
    if axes is None:
        return None
    if use_vel_axis:
        v = _finite(vel)
        if v is None:
            return None
        axes.append(clip((v - 1.0) / 0.4))
    return round(sum(axes) / len(axes), 3)


# ── 종목별 flow 1건 ──────────────────────────────────────────────────────
def one_name(row: dict, bench_close, data, use_news: bool, positioning: bool) -> dict:
    tk = row["ticker"]
    df = slice_frame(data, tk)
    p = flow_read.price_flow(tk, bench_close, df=df)
    vel = None
    if use_news and "error" not in p:
        q = flow_read._news_query(tk, row.get("name") or None)
        # 🚨 `kr=` 를 반드시 넘긴다. `news_velocity` 의 docstring 이 명시한 계약이고
        #    (*"호출부는 kr_code(ticker) 로 자동판별해 넘긴다"*), `module_flow/__main__.py:56`
        #    은 지키는데 **이 전수 스윕만 안 지키고 있었다** — 기본값 `kr=False` 라
        #    한국 기업명을 **해외(영문) 풀**에 던졌다.
        #    실측 2026-08-09: 삼성바이오로직스 base **5건** · LG에너지솔루션 **2건** ⇒ velocity 0.0,
        #    그리고 그 0.0 이 flow_score 에서 clip(-2.5) = **−1.0 최대 페널티**로 변환돼
        #    **시총가중**으로 섹터 순위에 꽂혔다. 축이 보상으로 발화한 적은 한 번도 없었다.
        nv = flow_read.news_velocity(q, 7, 30, kr=bool(kr_code(tk)))
        vel = nv.get("velocity")
    tag = flow_read.flow_tag(p, vel) if "error" not in p else "?"
    # flow_score 는 여기서 매기지 않는다 — 속도축 포함 여부가 **런 단위** 결정이라
    # 전 종목의 velocity 커버리지를 본 뒤 2패스(score_all)로 매긴다(D225-KR).
    out = {**row, "flow_score": None, "tag": tag, "velocity": vel}
    if "error" in p:
        out["error"] = p["error"]
    else:
        out.update({"last": p["last"], "obv_norm": p["obv_norm"], "obv_state": p["obv_state"],
                    "rs20": p["rs20"], "rs60": p["rs60"], "vol_surge": p["vol_surge"]})
    if positioning and "error" not in p:
        out["positioning"] = flow_read.positioning(tk, p.get("last"))
    return out


def score_all(results: list[dict], use_news: bool) -> dict:
    """2패스 채점 — 축 집합을 **런 단위**로 확정한 뒤 전 종목에 같은 척도를 매긴다(D225-KR).

    1패스(`one_name`)는 가격·속도만 읽고 점수를 비워 둔다. 여기서 커버리지를 본 뒤 축 집합을
    정하고 한 번에 매긴다 — 그래야 섹터 wflow/eqflow 가 **같은 단위의 평균**이 된다.
    """
    scorable = [r for r in results if "error" not in r]
    vel_ok = sum(1 for r in scorable if _finite(r.get("velocity")) is not None)
    cov = (vel_ok / len(scorable)) if scorable else 0.0
    use_vel_axis = bool(use_news) and cov >= VEL_COVERAGE_MIN

    for r in results:
        r["flow_score"] = flow_score(r, r.get("velocity"), use_vel_axis)

    dropped = sum(1 for r in scorable if r.get("flow_score") is None)
    log(f"[axis] velocity 측정 {vel_ok}/{len(scorable)} = {cov:.1%} → "
        f"속도축 {'포함(전원 4축)' if use_vel_axis else '제외(전원 3축)'} "
        f"· 기준 {VEL_COVERAGE_MIN:.0%} (D225-KR)")
    if use_news and cov < VEL_COVERAGE_MIN:
        log(f"🚨 [axis] 뉴스축이 이 런에서 **죽었다** (측정 {cov:.1%}). 「기사가 없다」가 아니라 "
            f"「세지 못했다」일 가능성이 높다 — 뉴스 검색은 원격 API 를 타고, 그 터널이 끊기면 "
            f"velocity 가 전부 None 이 되는데 그게 '무기사'와 구분되지 않는다.")
        log(f"   확인: python -X utf8 -m module_news_data fts search 삼성전자 --days 7 --count "
            f"· 로컬 폴백 색인 존재 여부 · DEGAJA_NEWS_API")
        log(f"   ⚠ 예전 구현은 이 상황에서 축을 조용히 드롭해 **전 종목 점수를 평균 +0.305 부풀렸다.** "
            f"지금은 전원 동일 축으로 매기고 이 줄을 남긴다.")
    if dropped:
        log(f"[axis] 축 결측으로 점수 미부여 {dropped}종목 — 집계 제외 "
            f"(예전엔 clip(nan)=+1.0 로 **최대 양수**를 받았다)")
    return {"vel_axis": use_vel_axis, "vel_coverage": round(cov, 4),
            "n_axes": 4 if use_vel_axis else 3,
            "scored": len(scorable) - dropped, "dropped_missing_axis": dropped}


# ── Δflow 히스토리 ───────────────────────────────────────────────────────
def load_history() -> dict:
    if HISTORY.exists():
        try:
            return json.loads(HISTORY.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_snapshot(hist: dict, asof: str, results: list[dict], mode: str):
    # _mode 각인 — 3축(nonews) vs 4축(news) flow_score는 크기가 달라 Δ를 섞으면 안 됨.
    snap = {"_mode": mode}
    snap.update({r["ticker"]: [r["flow_score"], r["tag"]]
                 for r in results if r.get("flow_score") is not None})
    hist[asof] = snap
    for k in sorted(hist)[:-40]:  # 최근 40 스냅샷만 유지
        hist.pop(k, None)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY.write_text(json.dumps(hist, ensure_ascii=False, indent=0), encoding="utf-8")


def prev_snapshot(hist: dict, asof: str, mode: str) -> dict:
    # 같은 모드의 가장 최근 이전 스냅샷만 — mixed-mode Δ(사과-오렌지) 차단.
    for k in sorted((k for k in hist if k < asof), reverse=True):
        snap = hist[k]
        if snap.get("_mode", "news") == mode:
            return {t: v for t, v in snap.items() if not t.startswith("_")}
    return {}


# ── 섹터 집계 ────────────────────────────────────────────────────────────
def aggregate_sectors(results: list[dict], prev: dict) -> list[dict]:
    from collections import defaultdict
    by = defaultdict(list)
    for r in results:
        if r.get("flow_score") is not None and r["sector"] and r["sector"] != "(unlisted)":
            by[r["sector"]].append(r)
    out = []
    for sec, names in by.items():
        w = sum(n["mcap"] for n in names) or 1.0
        wflow = sum(n["flow_score"] * n["mcap"] for n in names) / w
        eqflow = sum(n["flow_score"] for n in names) / len(names)
        greens = sum(1 for n in names if n["tag"] == "🟢가속")
        reds = sum(1 for n in names if n["tag"] == "🔴분산")
        # 섹터 Δ = 시총가중 flow 오늘 − 직전(공통 종목)
        pflow = None
        common = [n for n in names if n["ticker"] in prev]
        if common:
            pw = sum(n["mcap"] for n in common) or 1.0
            pflow = sum(prev[n["ticker"]][0] * n["mcap"] for n in common) / pw
        # ── D9: 이 버킷의 숫자가 **한 이름**인지 드러낸다 ──────────────────────
        # 숫자를 바꾸지 않는다. 「시총가중 평균」은 정의상 최대 종목이 지배할 수 있고,
        # 그게 정상인지 사고인지는 소비자가 판단할 문제다(P4). 다만 **판단할 재료 없이
        # 승격/강등하는 것**이 D9 가 지적한 실패다 — 실측 2026-08-09: 금융 wflow 의 음(−)
        # 전체가 `402340 SK스퀘어`(버킷 26.5%) 한 이름이었고 빼면 **부호가 뒤집혔다**
        # (−0.111 → +0.163). 유통도 `028260 삼성물산`(52.6%) 하나로 −0.045 → +0.155.
        # 지주가 KRX 분류상 금융에 섞이는 것도 같은 가족의 문제다.
        conc: dict = {}
        if len(names) >= 2:
            top = max(names, key=lambda n: n["mcap"])
            rest = [n for n in names if n["ticker"] != top["ticker"]]
            rw = sum(n["mcap"] for n in rest) or 1.0
            wf_ex = sum(n["flow_score"] * n["mcap"] for n in rest) / rw
            conc = {"top1": top["ticker"], "top1_name": top.get("name"),
                    "top1_w": round(top["mcap"] / w * 100, 1),
                    "wflow_ex_top1": round(wf_ex, 3),
                    "top1_flips_sign": (wflow > 0) != (wf_ex > 0)}
        out.append({"sector": sec, "n": len(names), "wflow": round(wflow, 3),
                    "eqflow": round(eqflow, 3), "green": greens, "red": reds,
                    "breadth": round(greens / len(names), 2),
                    "delta": round(wflow - pflow, 3) if pflow is not None else None,
                    **conc})
    return sorted(out, key=lambda x: x["wflow"], reverse=True)


# ── 렌더 ─────────────────────────────────────────────────────────────────
def arrow(d):
    if d is None:
        return "  ·  "
    return f" {'▲' if d > 0 else '▼' if d < 0 else '─'}{abs(d):.2f}"


def render_text(asof, results, sectors, prev, sector_filter, top, axis_meta: dict | None = None):
    valid = [r for r in results if r.get("flow_score") is not None]
    W = sum(r["mcap"] for r in valid) or 1.0
    uni = sum(r["flow_score"] * r["mcap"] for r in valid) / W
    g = sum(1 for r in valid if r["tag"] == "🟢가속")
    rd = sum(1 for r in valid if r["tag"] == "🔴분산")
    L = []
    L.append(f"# SECTOR FLOW — 유니버스 수급 와이드 스윕  (asof {asof}, n={len(valid)}/{len(results)})")
    L.append(f"시총가중 유니버스 flow {uni:+.3f}  ·  🟢{g} 🟡{len(valid)-g-rd} 🔴{rd}  ·  breadth(🟢%) {g/max(1,len(valid)):.0%}")
    # 신규 🟢
    newg = [r for r in valid if r["tag"] == "🟢가속"
            and (r["ticker"] not in prev or prev[r["ticker"]][1] != "🟢가속")]
    if newg and prev:
        newg.sort(key=lambda r: r["flow_score"], reverse=True)
        L.append("신규🟢(오늘 첫 가속): " + ", ".join(f"{r['ticker']}({r['flow_score']:+.2f})" for r in newg[:12]))

    if not sector_filter and not any(r["sector"] == "(unlisted)" for r in results):
        L.append("\n## 섹터 로테이션 (시총가중 flow 순)")
        L.append(f"{'SECTOR':<26}{'wFlow':>8}{'Δ':>7}  {'eqFlow':>7}  {'🟢/n':>7}  breadth")
        for s in sectors:
            mark = "  🚨1名" if s.get("top1_flips_sign") else ""
            L.append(f"{s['sector']:<26}{s['wflow']:>+8.3f}{arrow(s['delta']):>9}  "
                     f"{s['eqflow']:>+7.3f}  {str(s['green'])+'/'+str(s['n']):>7}  {s['breadth']:>5.0%}{mark}")

        # D9: 부호가 최대 종목 하나로 뒤집히는 버킷은 승격·강등의 근거가 될 수 없다.
        flips = [s for s in sectors if s.get("top1_flips_sign")]
        if flips:
            L.append(f"\n🚨 최대 종목 1개를 빼면 **부호가 뒤집히는** 섹터 {len(flips)}개 (D9) — "
                     f"이 버킷으로는 승격도 강등도 정당화할 수 없다:")
            for s in sorted(flips, key=lambda x: -x.get("top1_w", 0)):
                L.append(f"   {s['sector']:<14} {s['wflow']:+.3f} → ex-{s.get('top1_name') or s['top1']} "
                         f"{s['wflow_ex_top1']:+.3f}  (그 이름이 섹터 시총의 {s['top1_w']:.1f}%, n={s['n']})")

    # Δ 무버
    if prev:
        for r in valid:
            r["_d"] = (r["flow_score"] - prev[r["ticker"]][0]) if r["ticker"] in prev else None
        movers = [r for r in valid if r.get("_d") is not None]
        up = sorted(movers, key=lambda r: r["_d"], reverse=True)[:6]
        dn = sorted(movers, key=lambda r: r["_d"])[:6]
        if up:
            L.append("\nΔ상승: " + ", ".join(f"{r['ticker']}{arrow(r['_d'])}" for r in up))
            L.append("Δ하락: " + ", ".join(f"{r['ticker']}{arrow(r['_d'])}" for r in dn))

    # 상/하위 테이블 (or 섹터 필터면 전 종목)
    title = f"섹터 '{sector_filter}' 전 종목" if sector_filter else f"상·하위 {top}"
    L.append(f"\n## 종목 {title} (flow_score 순)")
    L.append(f"{'TICKER':<8}{'SEC':<14}{'flow':>7}{'Δ':>7}  {'tag':<7}{'OBV':>6} {'RS20':>6} {'서지':>5} {'vel':>5}")
    ranked = sorted(valid, key=lambda r: (r["flow_score"] is not None, r["flow_score"]), reverse=True)
    show = ranked if sector_filter else (ranked[:top] + ranked[-top:])
    seen = set()
    for r in show:
        if r["ticker"] in seen:
            continue
        seen.add(r["ticker"])
        d = (r["flow_score"] - prev[r["ticker"]][0]) if prev and r["ticker"] in prev else None
        vel = f"{r['velocity']:.2f}" if r.get("velocity") is not None else " n/a"
        L.append(f"{r['ticker']:<8}{r['sector'][:13]:<14}{r['flow_score']:>+7.3f}{arrow(d):>9}  "
                 f"{r['tag']:<7}{r.get('obv_norm',0):>+6.2f} {str(r.get('rs20','')):>6} "
                 f"{r.get('vol_surge',''):>5} {vel:>5}")
    n_ax = (axis_meta or {}).get("n_axes")
    ax_txt = (f"{n_ax}축" if n_ax else "축")
    ax_which = ("뉴스속도·OBV매집·RS20·거래량서지" if n_ax == 4 else "OBV매집·RS20·거래량서지 — 뉴스축 제외")
    L.append(f"\n범례: flow_score∈[-1,1]={ax_txt}({ax_which}) 클립평균 · 태그=flow_read 권위값 "
             "· wFlow=시총가중 · Δ=직전 스냅샷 대비 · breadth=섹터 내 🟢 비율")
    if n_ax == 3:
        L.append("⚠ 이 런은 뉴스축 없이 매겼다 — 점수를 4축 런의 점수와 직접 비교하지 마라(척도가 다르다).")
    return "\n".join(L)


def build_json(asof, results, sectors, prev, axis_meta: dict | None = None):
    valid = [r for r in results if r.get("flow_score") is not None]
    W = sum(r["mcap"] for r in valid) or 1.0
    for r in valid:
        r["delta"] = round(r["flow_score"] - prev[r["ticker"]][0], 3) if prev and r["ticker"] in prev else None
        r["new_green"] = r["tag"] == "🟢가속" and (r["ticker"] not in prev or prev[r["ticker"]][1] != "🟢가속")
    return {
        "asof": asof,
        # D225-KR: 이 런이 몇 축으로 매겼는지를 산출물에 박는다. 축 개수가 다르면 점수는
        # 비교 가능한 값이 아니다 — 소비자가 그 사실을 알 수 있어야 한다.
        "scoring": axis_meta or {},
        "universe": {"n": len(valid), "n_requested": len(results),
                     "wflow": round(sum(r["flow_score"] * r["mcap"] for r in valid) / W, 3),
                     "green": sum(1 for r in valid if r["tag"] == "🟢가속"),
                     "red": sum(1 for r in valid if r["tag"] == "🔴분산")},
        "sector_rotation": sectors,
        "names": sorted(valid, key=lambda r: r["flow_score"], reverse=True),
    }


def main():
    ap = argparse.ArgumentParser(description="유니버스 수급 와이드 스윕(수치화→섹터·랭킹)")
    ap.add_argument("--market", choices=["us", "kr"], default="us",
                    help="유니버스/벤치 시장 (us=us_top300/SPY · kr=kr_all/^KS11)")
    ap.add_argument("--sector", default=None, help="한 섹터만(부분매칭, 예: Energy / 화학)")
    ap.add_argument("--tickers", nargs="+", default=None, help="특정 종목만")
    ap.add_argument("--limit", type=int, default=None,
                    help="시총 상위 N만 스윕(유니버스는 이미 desc 정렬 — 매일 스윕 경량화)")
    ap.add_argument("--top", type=int, default=12, help="상·하위 N 표시")
    ap.add_argument("--no-news", action="store_true", help="뉴스속도 축 생략(빠름)")
    ap.add_argument("--positioning", action="store_true", help="종목 ⑤숏+⑥옵션 조회(≤20 권장)")
    ap.add_argument("--refresh", action="store_true", help="가격 캐시 무시하고 재다운로드")
    ap.add_argument("--json", action="store_true", help="stdout에 JSON(로그는 stderr)")
    a = ap.parse_args()

    # ── 시장 해석 → 전역(유니버스·벤치·컬럼·캐시/히스토리 네임스페이스) 재설정 ──
    global MKT, UNIVERSE, BENCH, COLS, HISTORY
    mk = MARKETS[a.market]
    MKT, UNIVERSE, BENCH, COLS = a.market, mk["universe"], mk["bench"], mk
    HISTORY = OUT_DIR / ("history.json" if a.market == "us" else f"history_{a.market}.json")

    # 유니버스 존재·신선도 가드 (빌드는 별도 주간 잡 — 여기선 읽기만, stale면 경고).
    if not UNIVERSE.exists():
        log(f"[err] 유니버스 파일 없음: {UNIVERSE}")
        if a.market == "kr":
            log("      → python -X utf8 data_build/kr_universe/build_kr_universe.py 로 먼저 빌드")
        sys.exit(1)
    import time as _t
    age_days = (_t.time() - UNIVERSE.stat().st_mtime) / 86400
    if age_days > 8:
        log(f"[warn] 유니버스 {UNIVERSE.name} {age_days:.0f}일 경과 — 시총 stale. "
            f"{'build_kr_universe.py' if a.market=='kr' else 'build_top300.py'} 재빌드 권장(주1회).")

    rows = load_universe(a.sector, a.tickers)
    if a.limit and not (a.sector or a.tickers):
        rows = rows[:a.limit]   # 유니버스 시총 desc → 상위 N 슬라이스
    if not rows:
        log("유니버스 비었음(섹터/티커 필터 확인)")
        sys.exit(1)
    if a.positioning and len(rows) > 20:
        log(f"[warn] positioning은 종목당 수초 → {len(rows)}종목이면 느림. --tickers로 좁히길 권장.")
    use_news = not a.no_news
    if not use_news:
        log("[warn] --no-news: 뉴스축 제외 → flow_score 3축 평균, 🟢 태그가 OBV 매집에만 의존해 "
            "체계적으로 강등됨(신규🟢/earliness 판단엔 부적합). 뉴스 비용은 ~10ms/종목이라 켜길 권장.")

    data = batch_prices([r["ticker"] for r in rows], a.refresh)
    bslice = slice_frame(data, BENCH)
    if bslice is None:
        log(f"[err] 벤치 {BENCH} 가격 없음"); sys.exit(1)
    bclose = bslice["Close"].astype(float) if "Close" in bslice else bslice[[c for c in bslice.columns if str(c).lower() == "close"][0]].astype(float)

    log(f"[flow] {len(rows)}종목 축 계산 …")
    results = []
    for i, row in enumerate(rows, 1):
        results.append(one_name(row, bclose, data, use_news, a.positioning))
        if i % 50 == 0:
            log(f"  … {i}/{len(rows)}")

    axis_meta = score_all(results, use_news)   # D225-KR: 축 집합 확정 후 일괄 채점

    asof = datetime.now().strftime("%Y-%m-%d")
    # asof는 실제 마지막 일봉일로 보정
    try:
        asof = str(bslice.index[-1].date())
    except Exception:
        pass

    # 🚨 mode 는 **의도(CLI 플래그)가 아니라 실제로 쓴 축 수**에서 나와야 한다.
    #    `save_snapshot`/`prev_snapshot` 은 이미 "3축 vs 4축 Δ 를 섞지 마라"를 _mode 로 막고
    #    있었는데, mode 가 `use_news` 에서 나오는 바람에 **뉴스축이 죽은 런도 "news" 로 각인**돼
    #    가드가 정확히 실패 케이스에서만 우회됐다. 뉴스 API 터널은 실제로 끊긴다(실측 2026-08-09).
    mode = "news" if axis_meta.get("vel_axis") else "nonews"
    hist = load_history()
    prev = prev_snapshot(hist, asof, mode)
    sectors = aggregate_sectors(results, prev)
    # 필터런(--sector/--tickers)은 애드혹 쿼리 → 히스토리 read-only(전체 유니버스 스냅샷 클로버 금지).
    # Δ는 여전히 전체 스냅샷 대비 계산해 보여주되, 저장은 전체런만.
    is_full = not (a.sector or a.tickers)
    if is_full:
        save_snapshot(hist, asof, results, mode)
    else:
        log(f"[hist] 필터런 → 스냅샷 저장 생략(전체 유니버스 Δ 기준선 보존)")

    if a.json:
        print(json.dumps(build_json(asof, results, sectors, prev, axis_meta), ensure_ascii=False, indent=2))
    else:
        print(render_text(asof, results, sectors, prev, a.sector, a.top, axis_meta))


if __name__ == "__main__":
    main()
