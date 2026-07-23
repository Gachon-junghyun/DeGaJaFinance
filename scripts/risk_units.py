# FILE: scripts/risk_units.py
# -*- coding: utf-8 -*-
"""RISK_UNITS — 책이 실제로 몇 개의 독립 베팅인지 **측정**한다 (라벨이 아니라 상관으로).

왜: `module_paper_book/_config.py MAX_THEME_PCT = 40.0` 은 "한 위험 단위"에 상한을 건다.
그런데 그 단위가 **테마/섹터 라벨**이다. 2026-07-22 US 런에서 그 라벨이 네 곳에서 깨졌다 —
Financials RS20 스프레드 44.4%p(중앙값 이동의 7.3배) · Energy 59.5%p(~17배) · IT ~40%p ·
Industrials 프라임 vs 자본재 0.705 flow 포인트. 반대 방향으로도 깨졌다: IT·리츠·유틸 언더웨이트가
사실 **AI 데이터센터 하나**였다(리츠의 적자는 AMT/EQIX/DLR/CCI, 유틸의 적자는 CEG).
즉 상한이 재는 단위가 위험 단위가 아니다. **이 스크립트는 그 단위를 실측으로 대체한다.**

근거(lab, A급): "잔차 클러스터가 섹터 라벨을 이긴다" — out-of-sample 그룹내 상관
**0.1289 vs 0.0786**, 페어 차이 +0.0511 [0.0435, 0.0588] ≈ 13 SE, 멤버십 ARI 0.568 vs 널 0.0165.
그 실험 코드는 이 리포에 없다(외부 Finance_PLAYGROUND). 여기서 방법론만 재구현한다.

⚠ 의존성: numpy/pandas/yfinance 만 쓴다. 군집·ARI 를 직접 구현해 **sklearn 을 import 하지 않는다**
   (CLAUDE.md P6 — 무거운 GPU 계열은 서버 기동을 막는다. 스크립트라 직접 영향은 없지만 규약을 따른다).

규칙 준수(handoff/RESEARCH.md):
  · C1 벤치마크를 항상 같이 출력한다(잔차는 벤치 대비 정의된다).
  · C5 임계값·링키지는 **임의 선택**이므로 대안의 효과를 같이 찍는다(임계값 스윕).
  · S5 짧은 표본은 구조를 지어낸다 — **적합도(그룹내 상관)와 안정성(ARI)을 따로** 보고한다.
        실측: 244일로 줄이면 ARI 0.093 으로 무너지는데 그룹내 상관은 **올라간다**.
  · S3 검정력 — 표본 일수를 찍고 250일 미만이면 경고한다.
  · D4 윈도우 오염 — KR/US 달력 교집합 손실률과 통화 축을 명시한다.

사용:
  python -X utf8 scripts/risk_units.py --book
  python -X utf8 scripts/risk_units.py --book --candidates VLO MPC PSX PANW CRWD FTNT DDOG GD
  python -X utf8 scripts/risk_units.py AVGO NVDA TSM --days 500 --threshold 0.35 --json

산출: llm_outputs/{date}/RISK_UNITS.md (+ --json)
⚠ 분석 산출물이다. 매수/매도 조언 0, 사이즈 권고 0 (P4). 단위를 재줄 뿐, 무엇을 담을지는 사람이 정한다.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

MIN_DAYS_POWER = 250          # S3/S5 — 이 밑이면 "구조를 지어낼 수 있다"고 경고
# 거리 = 1 − 잔차상관. ⚠ 잔차 상관은 원상관보다 훨씬 낮다(SPY 를 뺐으니 당연하다).
# 실측 2026-07-22, 이 책 9종목: 최대 잔차상관이 **0.584(KMI–LNG)**, 반도체 3인방이 0.38~0.44.
# 그래서 첫 구현의 기본값 0.35(=상관 0.65 이상 요구)는 **전부 싱글턴**을 만들었다 — 임계값이 데이터
# 스케일과 안 맞으면 "독립 9개"라는 그럴듯한 오답이 나온다. 기본값을 스케일에 맞추고, C5 대로
# **대안의 효과(스윕)를 항상 같이 찍어** 선택이 결론을 만들지 않게 한다.
DEFAULT_THRESHOLD = 0.65      # = 잔차상관 0.35 이상이면 같은 단위
SWEEP = (0.40, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85)


# ── 책 읽기 ─────────────────────────────────────────────────────────────
def read_book() -> list[dict]:
    """paper_book DB 에서 보유 종목 + 수량 + 테마 라벨을 읽는다(재구현 금지, P1)."""
    from module_paper_book._config import default_db_path
    import sqlite3
    con = sqlite3.connect(default_db_path())
    con.row_factory = sqlite3.Row
    cols = {r["name"] for r in con.execute("PRAGMA table_info(positions)")}
    qty = "qty" if "qty" in cols else ("quantity" if "quantity" in cols else None)
    if qty is None:
        raise SystemExit(f"positions 테이블에 수량 컬럼이 없다: {sorted(cols)}")
    theme = "theme" if "theme" in cols else None
    sel = f"SELECT ticker, {qty} AS qty" + (", theme" if theme else "") + " FROM positions"
    rows = [dict(r) for r in con.execute(sel) if (r[qty] or 0) > 0]
    con.close()
    return rows


def to_yf(ticker: str) -> str:
    """KR 6자리 코드는 .KS 접미사가 필요하다 — 없으면 **에러 없이 빈 행**이 온다(실측 함정)."""
    t = ticker.strip().upper()
    return f"{t}.KS" if (len(t) == 6 and t.isdigit()) else t


def read_cash_fx() -> tuple[dict, float, str]:
    """현금 잔고와 환율. 환율은 **실측 우선**(USDKRW=X), 실패 시 설정 기본값을 쓰고 그 사실을 밝힌다."""
    from module_paper_book._config import default_db_path, DEFAULT_FX_USDKRW
    import sqlite3
    con = sqlite3.connect(default_db_path())
    cash = {r[0]: float(r[1]) for r in con.execute("SELECT currency, amount FROM cash")}
    con.close()
    fx, fx_src = DEFAULT_FX_USDKRW, "config default (실측 실패)"
    try:
        import yfinance as yf
        s = yf.Ticker("USDKRW=X").history(period="5d")["Close"].dropna()
        if len(s):
            fx, fx_src = float(s.iloc[-1]), f"USDKRW=X {s.index[-1].date()}"
    except Exception:
        pass
    return cash, fx, fx_src


def last_prices(symbols: list[str]) -> tuple[dict, str]:
    import yfinance as yf
    px = yf.download(sorted(set(symbols)), period="5d", interval="1d", progress=False,
                     auto_adjust=False, group_by="ticker", threads=True)
    out, asof = {}, None
    for s in set(symbols):
        try:
            c = px[s]["Close"].dropna()
        except Exception:
            continue
        if len(c):
            out[s] = float(c.iloc[-1])
            asof = str(c.index[-1].date())
    return out, asof


# ── 수익률 · 잔차 ────────────────────────────────────────────────────────
def fetch_returns(tickers: list[str], days: int, bench: str) -> tuple[pd.DataFrame, dict]:
    import yfinance as yf
    syms = [to_yf(t) for t in tickers]
    want = sorted(set(syms + [bench]))
    px = yf.download(want, period=f"{int(days * 1.5)}d", interval="1d",
                     progress=False, auto_adjust=True, group_by="ticker", threads=True)
    close = {}
    for s in want:
        try:
            c = px[s]["Close"].dropna()
        except Exception:
            continue
        if len(c) > 20:
            close[s] = c
    if bench not in close:
        raise SystemExit(f"벤치마크 {bench} 를 못 받았다 — 중단(빈 값으로 진행하지 않는다).")

    raw = pd.DataFrame(close)
    per_name = {s: int(raw[s].notna().sum()) for s in raw.columns}
    full = raw.dropna()                          # D4 — 달력 교집합(트림 전)
    aligned = full.tail(days)                    # --days 트림은 '손실'이 아니다. 따로 센다.
    rets = np.log(aligned / aligned.shift(1)).dropna()
    # ⚠ 가격을 정렬한 뒤 차분하면 '3일 구멍을 건너뛴 1일 수익률'이 섞인다. 구멍 분포를 같이 낸다.
    gaps = pd.Series(aligned.index).diff().dt.days.dropna()
    meta = {
        "requested": want,
        "missing": sorted(set(want) - set(raw.columns)),
        "per_name_obs": per_name,
        "n_days_aligned": int(len(rets)),
        "n_days_intersection_full": int(len(full)),
        "trimmed_by_days_arg": int(max(0, len(full) - len(aligned))),
        # 달력 손실 = 그 종목이 가진 날 중, 교집합에서 빠진 날 (트림과 분리)
        "calendar_loss": {s: int(per_name[s] - len(full)) for s in raw.columns},
        "gap_days_median": float(gaps.median()) if len(gaps) else None,
        "gap_days_max": float(gaps.max()) if len(gaps) else None,
        "gaps_over_4d": int((gaps > 4).sum()) if len(gaps) else 0,
        "start": str(rets.index[0].date()) if len(rets) else None,
        "end": str(rets.index[-1].date()) if len(rets) else None,
    }
    return rets, meta


def residualize(rets: pd.DataFrame, bench: str) -> tuple[pd.DataFrame, dict]:
    """각 종목 수익률에서 **벤치 1팩터**를 회귀로 제거한다. 잔차 = 라벨이 아닌 진짜 공통성."""
    b = rets[bench].values
    bvar = float(np.var(b))
    out, betas = {}, {}
    for s in rets.columns:
        if s == bench:
            continue
        y = rets[s].values
        beta = float(np.cov(y, b)[0, 1] / bvar) if bvar > 0 else 0.0
        betas[s] = round(beta, 3)
        out[s] = y - beta * b
    return pd.DataFrame(out, index=rets.index), betas


# ── 군집(평균연결) + ARI — 직접 구현(sklearn 미사용) ──────────────────────
def agglomerative(corr: pd.DataFrame, threshold: float) -> dict[str, int]:
    names = list(corr.columns)
    D = (1.0 - corr.values).astype(float)
    np.fill_diagonal(D, 0.0)
    clusters = {i: [i] for i in range(len(names))}
    while len(clusters) > 1:
        keys = list(clusters)
        best, bi, bj = None, None, None
        for a in range(len(keys)):
            for c in range(a + 1, len(keys)):
                ia, ic = clusters[keys[a]], clusters[keys[c]]
                d = float(np.mean([D[x][y] for x in ia for y in ic]))   # average linkage
                if best is None or d < best:
                    best, bi, bj = d, keys[a], keys[c]
        if best is None or best > threshold:
            break
        clusters[bi] = clusters[bi] + clusters[bj]
        del clusters[bj]
    lab = {}
    for gid, (_, members) in enumerate(sorted(clusters.items(),
                                              key=lambda kv: -len(kv[1]))):
        for m in members:
            lab[names[m]] = gid
    return lab


def adjusted_rand(a: dict, b: dict) -> float:
    keys = sorted(set(a) & set(b))
    if len(keys) < 3:
        return float("nan")
    la, lb = [a[k] for k in keys], [b[k] for k in keys]
    ca, cb = sorted(set(la)), sorted(set(lb))
    tab = np.zeros((len(ca), len(cb)))
    for x, y in zip(la, lb):
        tab[ca.index(x)][cb.index(y)] += 1

    def c2(n):
        return n * (n - 1) / 2.0

    sij = sum(c2(v) for v in tab.flatten())
    sa = sum(c2(v) for v in tab.sum(axis=1))
    sb = sum(c2(v) for v in tab.sum(axis=0))
    n = c2(len(keys))
    exp = sa * sb / n if n else 0.0
    mx = (sa + sb) / 2.0
    return float((sij - exp) / (mx - exp)) if (mx - exp) else float("nan")


def within_group_corr(corr: pd.DataFrame, labels: dict[str, int]) -> float:
    vals = []
    names = list(corr.columns)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if labels.get(names[i]) == labels.get(names[j]):
                vals.append(corr.iloc[i, j])
    return float(np.mean(vals)) if vals else float("nan")


def between_group_corr(corr: pd.DataFrame, labels: dict[str, int]) -> float:
    vals = []
    names = list(corr.columns)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if labels.get(names[i]) != labels.get(names[j]):
                vals.append(corr.iloc[i, j])
    return float(np.mean(vals)) if vals else float("nan")


# ── 리포트 ──────────────────────────────────────────────────────────────
def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser("risk_units")
    ap.add_argument("tickers", nargs="*", help="측정할 티커(비우고 --book 쓰면 보유 종목)")
    ap.add_argument("--book", action="store_true", help="paper_book 보유 종목을 포함")
    ap.add_argument("--candidates", nargs="*", default=[], help="후보 종목 추가")
    ap.add_argument("--days", type=int, default=500, help="정렬 후 사용할 거래일 수")
    ap.add_argument("--bench", default="SPY")
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    ap.add_argument("--exposure", action="store_true",
                    help="측정 단위별 **현재 노출 %** 를 계산해 MAX_THEME_PCT 와 대조")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", default="")
    a = ap.parse_args()

    book = read_book() if a.book else []
    book_qty = {r["ticker"]: float(r["qty"]) for r in book}
    book_theme = {r["ticker"]: (r.get("theme") or "—") for r in book}
    names = list(dict.fromkeys([r["ticker"] for r in book] + a.tickers + a.candidates))
    if not names:
        raise SystemExit("측정할 종목이 없다 — --book 또는 티커를 줘라.")

    rets, meta = fetch_returns(names, a.days, a.bench)
    resid, betas = residualize(rets, a.bench)
    corr = resid.corr()

    n = meta["n_days_aligned"]
    labels = agglomerative(corr, a.threshold)

    # S5 — 안정성은 적합도와 따로 잰다. 전반/후반 절반씩 독립 군집 → ARI.
    half = len(resid) // 2
    lab_a = agglomerative(resid.iloc[:half].corr(), a.threshold)
    lab_b = agglomerative(resid.iloc[half:].corr(), a.threshold)
    ari = adjusted_rand(lab_a, lab_b)

    # C5 — 임계값은 임의 선택이므로 대안의 효과를 같이 찍는다.
    sweep = []
    for t in SWEEP:
        lb = agglomerative(corr, t)
        w = within_group_corr(corr, lb)
        sweep.append({"threshold": t, "min_corr_implied": round(1.0 - t, 2),
                      "n_units": len(set(lb.values())),
                      "within": None if (w != w) else round(w, 4)})

    # 라벨(테마) vs 측정 단위 대조
    groups: dict[int, list[str]] = {}
    for s, g in labels.items():
        groups.setdefault(g, []).append(s)

    def back(sym: str) -> str:
        return sym[:-3] if sym.endswith(".KS") else sym

    wg = within_group_corr(corr, labels)
    bg = between_group_corr(corr, labels)
    payload = {
        "date": date.today().isoformat(),
        "bench": a.bench,
        "threshold": a.threshold,
        "min_corr_implied": round(1.0 - a.threshold, 2),
        "n_days_aligned": n,
        "n_days_intersection_full": meta["n_days_intersection_full"],
        "trimmed_by_days_arg": meta["trimmed_by_days_arg"],
        "window": [meta["start"], meta["end"]],
        "missing": meta["missing"],
        "calendar_loss": meta["calendar_loss"],
        "gap_days_median": meta["gap_days_median"],
        "gap_days_max": meta["gap_days_max"],
        "gaps_over_4d": meta["gaps_over_4d"],
        "betas_vs_bench": betas,
        "ari_half_vs_half": None if (ari != ari) else round(ari, 4),
        "within_group_corr": None if (wg != wg) else round(wg, 4),
        "between_group_corr": None if (bg != bg) else round(bg, 4),
        "max_residual_corr": round(float(np.nanmax(corr.values[~np.eye(len(corr), dtype=bool)])), 4),
        "threshold_sweep": sweep,
        "residual_corr": {back(i): {back(j): round(float(corr.loc[i, j]), 3)
                                    for j in corr.columns} for i in corr.index},
        "units": {str(g): [back(s) for s in sorted(v)] for g, v in sorted(groups.items())},
        "book_theme_labels": book_theme,
    }

    if a.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    print(f"# RISK_UNITS — {payload['date']}  (벤치 {a.bench} · 잔차 1팩터 제거)")
    print(f"  윈도우 {meta['start']} → {meta['end']} · **정렬 후 {n} 거래일** · "
          f"임계 거리 {a.threshold} (= 잔차상관 {payload['min_corr_implied']} 이상이면 같은 단위)")
    if meta["trimmed_by_days_arg"]:
        print(f"  · 교집합 {meta['n_days_intersection_full']}일 중 --days 로 "
              f"{meta['trimmed_by_days_arg']}일 잘라냄(달력 손실 아님)")
    if n < MIN_DAYS_POWER:
        print(f"  ⚠ 표본 {n}일 < {MIN_DAYS_POWER}일 — **짧은 표본은 구조를 지어낸다(S5).** "
              f"적합도가 좋아 보여도 안정성(ARI)을 먼저 봐라.")
    if meta["missing"]:
        print(f"  ⚠ 시세 못 받은 종목(빈칸으로 둔다, 추정하지 않는다): {', '.join(meta['missing'])}")
    loss = {k: v for k, v in meta["calendar_loss"].items() if v > 0}
    if loss:
        print(f"  ⚠ 달력 교집합 손실: " +
              " · ".join(f"{k} −{v}일" for k, v in sorted(loss.items(), key=lambda kv: -kv[1])[:6]))
        print(f"     통화축도 섞인다 — KR 은 KRW, US 는 USD 로컬 수익률이다(공통 FX 요인 주입 가능).")
    if meta["gaps_over_4d"]:
        print(f"  ⚠ 교집합에 4일 초과 구멍 {meta['gaps_over_4d']}개(최대 {meta['gap_days_max']:.0f}일) — "
              f"그만큼 '1일 수익률'이 아닌 칸이 섞였다.")
    print()
    print(f"  최대 잔차상관 **{payload['max_residual_corr']:+.4f}** — 임계값은 이 스케일에 맞춰야 한다.")
    wgs = "n/a(그룹 없음)" if payload["within_group_corr"] is None else f"{payload['within_group_corr']:+.4f}"
    bgs = "n/a" if payload["between_group_corr"] is None else f"{payload['between_group_corr']:+.4f}"
    print(f"  적합도 그룹내 잔차상관 **{wgs}** vs 그룹간 {bgs}")
    print(f"  안정성 ARI(전반 vs 후반) **{payload['ari_half_vs_half']}** "
          f"— 적합도와 **반대로 움직인다**(S5). 낮으면 멤버십을 믿지 마라.")
    print()
    print("  ── 임계값 민감도(C5 — 임의 선택의 대안 효과) ──")
    for s in sweep:
        mark = " ←선택" if abs(s["threshold"] - a.threshold) < 1e-9 else ""
        w = "     n/a" if s["within"] is None else f"{s['within']:+.4f}"
        print(f"     dist {s['threshold']:.2f} (상관≥{s['min_corr_implied']:.2f}) → "
              f"단위 {s['n_units']:2d}개 · 그룹내 {w}{mark}")
    print()
    print(f"  ── 측정된 위험 단위 {len(groups)}개 ──")
    for g, v in sorted(groups.items()):
        syms = [back(s) for s in sorted(v)]
        themes = sorted({book_theme.get(s, "—") for s in syms if s in book_theme})
        held = [s for s in syms if s in book_qty]
        tail = ""
        if themes:
            tail = f"   [책 테마 라벨: {', '.join(themes)}]"
        print(f"   U{g}: {', '.join(syms)}{tail}")
        if held and themes and len(themes) > 1:
            print(f"        ⚠ 한 측정 단위 안에 **서로 다른 테마 라벨 {len(themes)}개** — "
                  f"MAX_THEME_PCT 가 이걸 {len(themes)}개로 쪼개 세고 있다.")
    # ── 노출 계산 (--exposure) ────────────────────────────────────────
    if a.exposure and book_qty:
        from module_paper_book._config import MAX_POS_PCT, MAX_THEME_PCT
        cash, fx, fx_src = read_cash_fx()
        prices, px_asof = last_prices([to_yf(t) for t in book_qty])
        rows, missing_px = [], []
        for t, q in book_qty.items():
            sym = to_yf(t)
            p = prices.get(sym)
            if p is None:
                missing_px.append(t); continue
            krw = p * q * (1.0 if sym.endswith(".KS") else fx)
            rows.append({"ticker": t, "qty": q, "price": p, "krw": krw,
                         "unit": labels.get(sym), "theme": book_theme.get(t, "—")})
        invested = sum(r["krw"] for r in rows)
        cash_krw = cash.get("KRW", 0.0) + cash.get("USD", 0.0) * fx
        total = invested + cash_krw

        print()
        print(f"  ══ 노출 (총자산 대비) — 가격 asof {px_asof} · fx {fx:,.1f} [{fx_src}] ══")
        print(f"     투자 {invested:,.0f} + 현금 {cash_krw:,.0f} = **총자산 {total:,.0f} KRW** "
              f"(현금 {cash_krw/total*100:.1f}%)")
        if missing_px:
            print(f"     ⚠ 시세 없음 → **빈칸 처리, 추정 안 함**: {', '.join(missing_px)} "
                  f"(그만큼 아래 %는 과소계상)")
        print()
        agg: dict = {}
        for r in rows:
            u = r["unit"]
            agg.setdefault(u, {"krw": 0.0, "names": [], "themes": set()})
            agg[u]["krw"] += r["krw"]
            agg[u]["names"].append(r["ticker"])
            agg[u]["themes"].add(r["theme"])
        print(f"     ── 측정 단위별 (상한 MAX_THEME_PCT = {MAX_THEME_PCT}%) ──")
        for u, v in sorted(agg.items(), key=lambda kv: -kv[1]["krw"]):
            pct = v["krw"] / total * 100
            flag = "  🚨 상한 초과" if pct > MAX_THEME_PCT else ""
            print(f"     U{u}: {pct:6.2f}%  {v['krw']:>12,.0f} KRW  "
                  f"[{', '.join(sorted(v['names']))}]{flag}")
            if len(v["themes"]) > 1:
                print(f"          ⚠ 이 한 단위를 테마 라벨은 **{len(v['themes'])}개로 쪼개 센다**: "
                      f"{', '.join(sorted(v['themes']))}")
        print()
        th: dict = {}
        for r in rows:
            th.setdefault(r["theme"], {"krw": 0.0, "units": set()})
            th[r["theme"]]["krw"] += r["krw"]
            th[r["theme"]]["units"].add(r["unit"])
        print(f"     ── 현행 테마 라벨별 (지금 상한이 실제로 재는 것) ──")
        for t, v in sorted(th.items(), key=lambda kv: -kv[1]["krw"]):
            print(f"     {v['krw']/total*100:6.2f}%  {t}")
        print()
        print(f"     ── 단일 종목 (상한 MAX_POS_PCT = {MAX_POS_PCT}%) ──")
        for r in sorted(rows, key=lambda x: -x["krw"]):
            pct = r["krw"] / total * 100
            flag = "  🚨" if pct > MAX_POS_PCT else ""
            print(f"     {pct:6.2f}%  {r['ticker']:<8} {r['qty']:g}주{flag}")
        payload["exposure"] = {
            "px_asof": px_asof, "fx": fx, "fx_source": fx_src,
            "invested_krw": round(invested), "cash_krw": round(cash_krw),
            "total_krw": round(total), "missing_price": missing_px,
            "by_unit": {f"U{u}": {"pct": round(v["krw"] / total * 100, 2),
                                  "krw": round(v["krw"]), "names": sorted(v["names"]),
                                  "themes": sorted(v["themes"])} for u, v in agg.items()},
            "by_theme": {t: round(v["krw"] / total * 100, 2) for t, v in th.items()},
            "by_name": {r["ticker"]: round(r["krw"] / total * 100, 2) for r in rows},
            "limits": {"MAX_POS_PCT": MAX_POS_PCT, "MAX_THEME_PCT": MAX_THEME_PCT},
        }

    print()
    print("  ⚠ 분석 산출물이다. 매수/매도 조언·사이즈 권고 없음(P4). 단위를 재줄 뿐이다.")

    outp = Path(a.out) if a.out else (ROOT / "llm_outputs" / payload["date"] / "RISK_UNITS.json")
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[saved] {outp}")


if __name__ == "__main__":
    main()
