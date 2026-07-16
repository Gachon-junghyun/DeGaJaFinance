# -*- coding: utf-8 -*-
"""US 셋업 스크리너 — top300 모수에서 HYPER 3바구니 후보를 결정론(토큰0)으로 긁는다.

HYPER 헌트(execute stages/03_hunt §3a, propose 02_hunt)가 손으로 박은 9개 리스트
(NOC LMT PLTR KTOS AMD AVGO SMH ANET CRWD)로 후보가 좁아져 1~2개로 귀결되던
문제를 메운다. data_build/us_universe/us_top300.csv 전수를 yfinance 일봉으로
스캔해 3바구니 raw 후보를 바구니별 top-N 으로 surface 한다.

⚠️ 이건 '후보 발굴'일 뿐 매수신호가 아님 — 턴 미확정(raw setup). 다운스트림
(CHART_READ 턴-판정 → STRUCTURE GATE → 4Phase 기업분석)이 품질을 거른다.
스크리너는 깔때기 '입구'만 넓힌다. 필터는 그대로다.

바구니(3a HUNT 와 1:1):
  A 리더 눌림목  : 추세상단(last>sma200) & rsi<45 & 50DMA 근접(±NEAR_50%)        — 가장 깔끔한 R/R
  B 디레이트     : 추세하단(last<sma50 & last<sma200) & px/sma200<=DERATE & rsi DERATE_RSI  — 갭업 잠재
  C 워시아웃     : rsi<WASH_RSI & 52주 저점 근접(last<=l52w*(1+WASH_NEAR))           — 최소사이즈·1개만

각 항목 플래그:
  in_book       : 광기(id=5) 책에 이미 보유 중인가
  already_listed: 기존 하드코딩 9개 리스트에 이미 있나 (= 이 스크리너가 '새로' 발굴한 게 아님)
  → in_book=False & already_listed=False = 진짜 신규 발굴(헌트가 못 보던 후보)

사용:
  python -X utf8 scripts/us_setup_screener.py                       # 최신, 바구니별 top8, 표+JSON
  python -X utf8 scripts/us_setup_screener.py --date 2026-06-27 --per-bucket 10 --limit 300 --json
  python -X utf8 scripts/us_setup_screener.py --limit 150          # 시총 top150만(빠름)
"""
from __future__ import annotations
import argparse
import csv
import datetime as _dt
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path

import pandas as pd
import yfinance as yf

import yf_snapshot  # same dir (scripts/) — compute() 재사용

ROOT = Path(__file__).resolve().parent.parent
TOP300 = ROOT / "data" / "us_universe" / "us_top300.csv"
DB = ROOT / "data" / "indicator_alerts.db"
OUT_DIR = ROOT / "llm_outputs" / "us_screen"
HYPER_PID = 5  # 광기

# 기존 헌트 하드코딩 리스트 — '새 발굴'을 표시하기 위한 기준
HARDCODED = {"NOC", "LMT", "PLTR", "KTOS", "AMD", "AVGO", "SMH", "ANET", "CRWD"}

# ── 바구니 임계값 (한 곳에서 조정) ─────────────────────────────
NEAR_50 = 0.04        # A: 50DMA ±4% 이내 = '근접'
DERATE_MAX = -12.0    # B: px/sma200 <= -12% = '디레이트'
DERATE_RSI = (30.0, 52.0)  # B: rsi 이 구간 = 붕괴아닌 베이싱
WASH_RSI = 28.0       # C: rsi < 28 = 워시아웃
WASH_NEAR = 0.15      # C: 52주 저점 +15% 이내
SECTOR_CAP = 2        # 바구니별 동일 GICS 섹터 최대 N (다양성 강제)


def load_universe(limit: int, sector: str | None = None) -> list[dict]:
    rows = []
    sec = (sector or "").strip().lower()
    with TOP300.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if sec and sec not in (r.get("gics_sector", "") or "").lower():
                continue       # --sector: GICS 섹터명 substring 매칭(예: "Energy", "Financials")
            rows.append(r)
            if limit and len(rows) >= limit:
                break
    return rows


def hyper_holdings() -> set[str]:
    if not DB.exists():
        return set()
    con = sqlite3.connect(DB)
    try:
        q = "SELECT DISTINCT ticker FROM positions WHERE active=1 AND portfolio_id=?"
        return {r[0] for r in con.execute(q, (HYPER_PID,)).fetchall()}
    except Exception:
        return set()
    finally:
        con.close()


def fetch(tickers: list[str], chunk: int = 40) -> dict[str, dict]:
    """yfinance 일봉을 청크 배치로 받아 ticker별 compute() 결과 + l52w 추가."""
    out: dict[str, dict] = {}
    for i in range(0, len(tickers), chunk):
        batch = tickers[i:i + chunk]
        try:
            df = yf.download(batch, period="13mo", group_by="ticker",
                             progress=False, auto_adjust=False, threads=True)
        except Exception as e:
            print(f"  배치 {i//chunk} 다운로드 실패: {e}", file=sys.stderr)
            continue
        for t in batch:
            try:
                sub = df[t] if isinstance(df.columns, pd.MultiIndex) else df
                if sub is None or sub.dropna(how="all").empty:
                    continue
                sub = sub.copy()
                sub.columns = [str(c).lower() for c in sub.columns]
                sub = sub.dropna(subset=["close"])
                if len(sub) < 60:        # 50/200DMA 의미있으려면 최소봉
                    continue
                m = yf_snapshot.compute(sub)
                close = sub["close"].astype(float)
                m["l52w"] = float(close.tail(252).min())
                out[t] = m
            except Exception:
                continue
        print(f"  ...{min(i+chunk, len(tickers))}/{len(tickers)} 처리", file=sys.stderr)
    return out


def _dist_pct(a, b):
    return None if not (a and b) else (a / b - 1.0) * 100.0


def classify(meta: dict[str, dict], info: dict[str, dict],
             holds: set[str], per_bucket: int, sector_cap: int = SECTOR_CAP) -> dict[str, list]:
    A, B, C = [], [], []
    for t, m in meta.items():
        last, rsi = m.get("last"), m.get("rsi14")
        s50, s200 = m.get("sma50"), m.get("sma200")
        pvs200, l52w = m.get("px_vs_sma200"), m.get("l52w")
        if last is None or rsi is None:
            continue
        d50 = _dist_pct(last, s50)
        dlow = _dist_pct(last, l52w)
        rec = {
            "ticker": t,
            "name": info.get(t, {}).get("name", ""),
            "sector": info.get(t, {}).get("gics_sector", ""),
            "last": round(last, 2),
            "rsi": round(rsi, 1),
            "sma50": None if s50 is None else round(s50, 2),
            "sma200": None if s200 is None else round(s200, 2),
            "px_vs_sma200_pct": None if pvs200 is None else round(pvs200, 1),
            "dist_50dma_pct": None if d50 is None else round(d50, 1),
            "dist_52wlow_pct": None if dlow is None else round(dlow, 1),
            "in_book": t in holds,
            "already_listed": t in HARDCODED,
        }
        # A 리더 눌림목 — 추세상단 & 약세 & 50DMA 근접
        if s200 and last > s200 and rsi < 45 and d50 is not None and abs(d50) <= NEAR_50 * 100:
            A.append({**rec, "_score": rsi + abs(d50)})        # 낮을수록(더 눌림+더 근접) 우선
        # B 디레이트 스냅백 — 추세하단 & 깊은 디레이트 & 베이싱
        elif (s50 and s200 and last < s50 and last < s200 and pvs200 is not None
              and pvs200 <= DERATE_MAX and DERATE_RSI[0] <= rsi <= DERATE_RSI[1]):
            B.append({**rec, "_score": pvs200})                # 더 깊은 디레이트 우선(작을수록)
        # C 워시아웃 옥탄 — 극과매도 & 52주저점 근접
        elif rsi < WASH_RSI and dlow is not None and dlow <= WASH_NEAR * 100:
            C.append({**rec, "_score": rsi})                   # 더 씻길수록 우선

    def top(lst):
        lst.sort(key=lambda x: x["_score"])
        picked, scnt = [], Counter()
        for x in lst:
            sec = x["sector"] or "?"
            if scnt[sec] >= sector_cap:        # 섹터 다양성 강제 (단일섹터 모드면 캡 해제)
                continue
            scnt[sec] += 1
            picked.append({k: v for k, v in x.items() if k != "_score"})
            if len(picked) >= per_bucket:
                break
        return picked

    return {"A_leader_pullback": top(A), "B_derate_snapback": top(B), "C_washout_octane": top(C)}


def _print_bucket(title: str, rows: list[dict]):
    print(f"\n## {title}  ({len(rows)})")
    if not rows:
        print("  (없음)")
        return
    print(f"  {'TICKER':<7}{'RSI':>6}{'px/200':>8}{'~50DMA':>8}{'~52wL':>7}  flags  sector")
    for r in rows:
        flags = []
        if not r["in_book"] and not r["already_listed"]:
            flags.append("🆕신규")
        if r["in_book"]:
            flags.append("보유")
        if r["already_listed"]:
            flags.append("기존")
        pvs = "n/a" if r["px_vs_sma200_pct"] is None else f"{r['px_vs_sma200_pct']:+.0f}%"
        d50 = "n/a" if r["dist_50dma_pct"] is None else f"{r['dist_50dma_pct']:+.0f}%"
        dlo = "n/a" if r["dist_52wlow_pct"] is None else f"+{r['dist_52wlow_pct']:.0f}%"
        print(f"  {r['ticker']:<7}{r['rsi']:>6.1f}{pvs:>8}{d50:>8}{dlo:>7}  "
              f"{','.join(flags) or '-':<10} {r['sector']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=str(_dt.date.today()))
    ap.add_argument("--per-bucket", type=int, default=8)
    ap.add_argument("--limit", type=int, default=300, help="시총 top-N 만 스캔(속도)")
    ap.add_argument("--sector", default=None,
                    help="GICS 섹터명으로 모수 한정(예: Energy, Financials). industry-us Phase3 섹터내 후보 발굴용 — 단일섹터면 섹터캡 해제.")
    ap.add_argument("--json", action="store_true", help="JSON 파일로도 저장")
    args = ap.parse_args()

    if not TOP300.exists():
        print(f"FATAL: {TOP300} 없음 — build_top300.py 먼저 실행", file=sys.stderr)
        sys.exit(1)

    uni = load_universe(args.limit, args.sector)
    info = {r["ticker"]: r for r in uni}
    tickers = [r["ticker"] for r in uni]
    holds = hyper_holdings()
    scope = f"sector='{args.sector}' " if args.sector else ""
    print(f"스캔: {scope}{len(tickers)}종 (광기 보유 {len(holds)}종 교차표시) ...", file=sys.stderr)
    if args.sector and not tickers:
        print(f"⚠️ '{args.sector}' 매칭 종목 0 — GICS 섹터명 철자 확인(예: Information Technology, Health Care).", file=sys.stderr)

    meta = fetch(tickers)
    print(f"가격 확보 {len(meta)}/{len(tickers)}종", file=sys.stderr)
    # 단일섹터 모드면 섹터캡 해제(전부 같은 섹터라 캡이 무의미)
    cap = 999 if args.sector else SECTOR_CAP
    buckets = classify(meta, info, holds, args.per_bucket, cap)

    capdesc = "섹터캡 해제(단일섹터)" if args.sector else f"섹터캡 {SECTOR_CAP}"
    scope_h = f"sector='{args.sector}', " if args.sector else ""
    print(f"\n# US 셋업 스크리너 — {args.date}  ({scope_h}{len(tickers)} 모수, 바구니별 ≤{args.per_bucket}, {capdesc})")
    print("# ⚠️ raw 후보(턴 미확정) — CHART_READ·STRUCTURE GATE·기업분석이 다운스트림에서 거른다. 매수신호 아님.")
    _print_bucket("A. 리더 눌림목 (leader pullback) — 추세상단·rsi<45·50DMA근접", buckets["A_leader_pullback"])
    _print_bucket("B. 디레이트 스냅백 (de-rate snapback) — 추세하단·px/200≤-12%·rsi 30~52", buckets["B_derate_snapback"])
    _print_bucket("C. 워시아웃 옥탄 (washout) — rsi<28·52주저점 근접", buckets["C_washout_octane"])

    newcomers = [r["ticker"] for b in buckets.values() for r in b
                 if not r["in_book"] and not r["already_listed"]]
    print(f"\n→ 🆕 신규 발굴(기존 9개·보유 밖): {len(newcomers)}종 — {' '.join(newcomers) or '없음'}")
    print("→ 이 티커들을 snapshot_universe.py argv 에 넣어 헌트 후보로 승격(CHART_READ→기업분석).")

    if args.json:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        fp = OUT_DIR / f"{args.date}.json"
        fp.write_text(json.dumps(
            {"date": args.date, "universe_size": len(tickers), "priced": len(meta),
             "params": {"NEAR_50": NEAR_50, "DERATE_MAX": DERATE_MAX, "DERATE_RSI": DERATE_RSI,
                        "WASH_RSI": WASH_RSI, "WASH_NEAR": WASH_NEAR, "SECTOR_CAP": SECTOR_CAP},
             "buckets": buckets, "newcomers": newcomers},
            indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nJSON: {fp}")


if __name__ == "__main__":
    main()
