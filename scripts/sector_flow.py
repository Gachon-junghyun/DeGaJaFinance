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
import pickle
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

import flow_read  # 같은 scripts/ — 엔진 재사용(수식 이식 0)

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


def flow_score(p: dict, vel) -> float | None:
    if "error" in p:
        return None
    axes = [
        clip(p["obv_norm"] / 0.16),
        clip((p["rs20"] or 0) / 8.0),
        clip((p["vol_surge"] - 1.0) / 0.6),
    ]
    if vel is not None:
        axes.append(clip((vel - 1.0) / 0.4))
    return round(sum(axes) / len(axes), 3)


# ── 종목별 flow 1건 ──────────────────────────────────────────────────────
def one_name(row: dict, bench_close, data, use_news: bool, positioning: bool) -> dict:
    tk = row["ticker"]
    df = slice_frame(data, tk)
    p = flow_read.price_flow(tk, bench_close, df=df)
    vel = None
    if use_news and "error" not in p:
        q = flow_read._news_query(tk, row.get("name") or None)
        nv = flow_read.news_velocity(q, 7, 30)
        vel = nv.get("velocity")
    tag = flow_read.flow_tag(p, vel) if "error" not in p else "?"
    fs = flow_score(p, vel)
    out = {**row, "flow_score": fs, "tag": tag, "velocity": vel}
    if "error" in p:
        out["error"] = p["error"]
    else:
        out.update({"last": p["last"], "obv_norm": p["obv_norm"], "obv_state": p["obv_state"],
                    "rs20": p["rs20"], "rs60": p["rs60"], "vol_surge": p["vol_surge"]})
    if positioning and "error" not in p:
        out["positioning"] = flow_read.positioning(tk, p.get("last"))
    return out


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
        out.append({"sector": sec, "n": len(names), "wflow": round(wflow, 3),
                    "eqflow": round(eqflow, 3), "green": greens, "red": reds,
                    "breadth": round(greens / len(names), 2),
                    "delta": round(wflow - pflow, 3) if pflow is not None else None})
    return sorted(out, key=lambda x: x["wflow"], reverse=True)


# ── 렌더 ─────────────────────────────────────────────────────────────────
def arrow(d):
    if d is None:
        return "  ·  "
    return f" {'▲' if d > 0 else '▼' if d < 0 else '─'}{abs(d):.2f}"


def render_text(asof, results, sectors, prev, sector_filter, top):
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
            L.append(f"{s['sector']:<26}{s['wflow']:>+8.3f}{arrow(s['delta']):>9}  "
                     f"{s['eqflow']:>+7.3f}  {str(s['green'])+'/'+str(s['n']):>7}  {s['breadth']:>5.0%}")

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
    L.append("\n범례: flow_score∈[-1,1]=4축(뉴스속도·OBV매집·RS20·거래량서지) 클립평균 · 태그=flow_read 권위값 "
             "· wFlow=시총가중 · Δ=직전 스냅샷 대비 · breadth=섹터 내 🟢 비율")
    return "\n".join(L)


def build_json(asof, results, sectors, prev):
    valid = [r for r in results if r.get("flow_score") is not None]
    W = sum(r["mcap"] for r in valid) or 1.0
    for r in valid:
        r["delta"] = round(r["flow_score"] - prev[r["ticker"]][0], 3) if prev and r["ticker"] in prev else None
        r["new_green"] = r["tag"] == "🟢가속" and (r["ticker"] not in prev or prev[r["ticker"]][1] != "🟢가속")
    return {
        "asof": asof,
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

    log(f"[flow] {len(rows)}종목 4축 계산 …")
    results = []
    for i, row in enumerate(rows, 1):
        results.append(one_name(row, bclose, data, use_news, a.positioning))
        if i % 50 == 0:
            log(f"  … {i}/{len(rows)}")

    asof = datetime.now().strftime("%Y-%m-%d")
    # asof는 실제 마지막 일봉일로 보정
    try:
        asof = str(bslice.index[-1].date())
    except Exception:
        pass

    mode = "news" if use_news else "nonews"
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
        print(json.dumps(build_json(asof, results, sectors, prev), ensure_ascii=False, indent=2))
    else:
        print(render_text(asof, results, sectors, prev, a.sector, a.top))


if __name__ == "__main__":
    main()
