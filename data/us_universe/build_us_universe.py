#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""build_us_universe — US 유니버스 빌더 (S&P 1500 = 500+400+600).

**왜 이 파일이 생겼나.** `data/us_universe/us_top300.csv` 는 **스냅샷 복사본**이었고 빌더가
없었다(MODULE_MAP 「다음 후보(미착수)」). 그래서 US 커버리지가 300종목에 고정돼 있었고,
유니버스 **밖의 이름은 「안 보이는」 게 아니라 「존재하지 않았다」** — 데스크는 `LNG` 에 대해
*"us_top300 밖 = flow·RS·OBV·숏 어느 축도 데스크 계기로는 존재하지 않는다"* 를 **9런 연속**
기록했고, 탱커 5종목(STNG·FRO·INSW·DHT·TNK)도 같은 이유로 태그 자체가 불가능했다.

**소스 두 축(둘 다 무료·무인증)**
  ① 구성종목 + **GICS 섹터/산업** — 위키피디아 S&P 500/400/600 목록.
     현행 CSV 스키마(`gics_sector`·`gics_industry`)와 **열이 그대로 일치**한다.
  ② 시총 — `yfinance` `fast_info.market_cap`. 실측 0.6초/종목 ⇒ 1,506종목 **약 15분**.
     ⚠ `fast_info` 의 dict 키는 camelCase(`marketCap`)인데 **속성은 snake_case(`market_cap`)** 다.
       `.get("market_cap")` 은 조용히 None 을 준다(실측). 속성으로 읽는다.

**안전 기본값(P4·KR 빌더와 동형)**: 기본 출력은 **후보 파일**이다. 라이브 `us_top300.csv` 를
덮어쓰려면 `--out` 으로 명시해야 한다. 그리고 기존 파일과의 **차집합을 항상 보고**한다 —
유니버스가 바뀌면 모든 스윕의 분모가 바뀌기 때문이다.

  python -X utf8 data/us_universe/build_us_universe.py                 # 후보 생성(전량)
  python -X utf8 data/us_universe/build_us_universe.py --limit 50      # 표본 테스트
  python -X utf8 data/us_universe/build_us_universe.py --from-cache    # 네트워크 0콜, 재집계만
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DEFAULT = ROOT / "data" / "us_universe" / "us_all_v2_candidate.csv"
CACHE_DEFAULT = ROOT / "data" / "us_universe" / ".build_cache.jsonl"
LIVE = ROOT / "data" / "us_universe" / "us_top300.csv"

UA = {"User-Agent": "DeGaJaFinance/1.0 (research universe builder)"}
SOURCES = {
    "sp500": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
    "sp400": "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
    "sp600": "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies",
}
COLS = ["rank", "ticker", "name", "market_cap_usd", "market_cap_h", "gics_sector", "gics_industry"]


def log(*a):
    print(*a, file=sys.stderr)


def _norm_ticker(t: str) -> str:
    """위키는 `BRK.B`, yfinance/현행 CSV 는 `BRK-B`. 표기를 현행 CSV 에 맞춘다."""
    return str(t).strip().upper().replace(".", "-")


def _cap_h(v: float) -> str:
    for unit, div in (("T", 1e12), ("B", 1e9), ("M", 1e6)):
        if v >= div:
            return f"{v/div:.2f}{unit}"
    return f"{v:.0f}"


def _fetch_constituents() -> tuple[list[dict], Counter]:
    """S&P 500/400/600 구성종목 + GICS. 지수별 개수를 함께 보고한다."""
    import pandas as pd
    import requests

    rows: dict[str, dict] = {}
    per_index = Counter()
    for label, url in SOURCES.items():
        try:
            r = requests.get(url, headers=UA, timeout=60)
            r.raise_for_status()
            tables = pd.read_html(io.StringIO(r.text))
        except Exception as e:                                        # noqa: BLE001
            log(f"[warn] {label} 실패 — {type(e).__name__}: {e}")
            continue
        tbl = None
        for t in tables:
            cols = [str(c) for c in t.columns]
            if any("GICS Sector" in c for c in cols) and any(
                c in ("Symbol", "Ticker", "Ticker symbol") for c in cols
            ):
                tbl = t
                break
        if tbl is None:
            log(f"[warn] {label}: GICS 표를 못 찾음 (표 {len(tables)}개) — 페이지 구조 변경 가능")
            continue
        cols = {str(c): c for c in tbl.columns}
        sym = cols.get("Symbol") or cols.get("Ticker") or cols.get("Ticker symbol")
        nm = cols.get("Security") or cols.get("Company")
        sec = next((v for k, v in cols.items() if "GICS Sector" in k), None)
        ind = next((v for k, v in cols.items() if "Sub-Industry" in k), None)
        n_new = 0
        for _, row in tbl.iterrows():
            tk = _norm_ticker(row[sym])
            if not tk or tk in rows:          # 중복 상장(지수 간 이동 중) — 먼저 본 것을 유지
                continue
            rows[tk] = {"ticker": tk,
                        "name": str(row[nm]).strip() if nm else tk,
                        "gics_sector": str(row[sec]).strip() if sec else "",
                        "gics_industry": str(row[ind]).strip() if ind else "",
                        "index": label}
            n_new += 1
        per_index[label] = n_new
        log(f"[src] {label}: {n_new}종목")
    return list(rows.values()), per_index


# yfinance 섹터 분류 → GICS 표기. 지수 밖 종목의 섹터를 채울 때만 쓴다.
YF_TO_GICS = {
    "Basic Materials": "Materials",
    "Communication Services": "Communication Services",
    "Consumer Cyclical": "Consumer Discretionary",
    "Consumer Defensive": "Consumer Staples",
    "Energy": "Energy",
    "Financial Services": "Financials",
    "Healthcare": "Health Care",
    "Industrials": "Industrials",
    "Real Estate": "Real Estate",
    "Technology": "Information Technology",
    "Utilities": "Utilities",
}


def _extra_tickers(include_live: bool, include_book: bool, extra: str) -> dict[str, dict]:
    """지수 밖이지만 **유니버스에 반드시 있어야 하는** 이름들.

    🚨 **지수 구성종목 목록은 유니버스가 아니다** (2026-08-10 실측). S&P 1500 은
      · **외국 국적을 배제한다** — ASML·ARM·TSM·PDD·SHOP·MELI·TRI·FER·CCEP 가 전부 빠진다.
      · **크기와 무관하게 비편입 종목을 배제한다** — `LNG`(Cheniere)는 목록에 아예 없고,
        탱커(STNG·FRO·DHT·TNK)도 없다.
    ⇒ 지수만으로 유니버스를 만들면 **고치려던 문제를 못 고친다.** 데스크는 `LNG` 에 대해
      *"어느 축도 데스크 계기로는 존재하지 않는다"* 를 9런 연속 기록했는데, 지수 기반 확장은
      그 이름을 여전히 못 담는다.

    ★ 그리고 그보다 강한 불변식이 있다: **데스크는 자기가 보유한 것을 태그할 수 있어야 한다.**
      실측 — 책의 US 보유 8종 중 **`TSM`·`LNG` 2종이 현행 유니버스에도 없었다.**
    """
    out: dict[str, dict] = {}
    if include_live and LIVE.exists():
        for r in csv.DictReader(LIVE.open(encoding="utf-8")):
            tk = _norm_ticker(r["ticker"])
            out[tk] = {"ticker": tk, "name": r.get("name") or tk,
                       "gics_sector": r.get("gics_sector") or "",
                       "gics_industry": r.get("gics_industry") or "",
                       "index": "live"}
    if include_book:
        try:
            import sqlite3
            db = ROOT / "data" / "paper_book.db"
            if db.exists():
                con = sqlite3.connect(str(db))
                try:
                    rows = con.execute(
                        "SELECT ticker FROM positions WHERE qty > 0"
                    ).fetchall()
                finally:
                    con.close()
                for (tk,) in rows:
                    tk = _norm_ticker(tk)
                    if tk.isalpha() and tk not in out:      # KR 6자리 코드는 제외
                        out[tk] = {"ticker": tk, "name": tk, "gics_sector": "",
                                   "gics_industry": "", "index": "book"}
        except Exception as e:                                        # noqa: BLE001
            log(f"[warn] 보유종목 읽기 실패(무시) — {type(e).__name__}: {e}")
    for tk in (t.strip().upper() for t in (extra or "").split(",") if t.strip()):
        tk = _norm_ticker(tk)
        if tk not in out:
            out[tk] = {"ticker": tk, "name": tk, "gics_sector": "",
                       "gics_industry": "", "index": "include"}
    return out


def _fill_sectors(rows: list[dict], sleep: float) -> int:
    """GICS 가 빈 종목만 yfinance `.info` 로 채운다(느리므로 소수 전용). 실패는 `(unmapped)`."""
    import yfinance as yf

    todo = [r for r in rows if not r.get("gics_sector")]
    if not todo:
        return 0
    log(f"[sector] 지수 밖 {len(todo)}종목의 섹터를 yfinance 로 채운다(느림)")
    filled = 0
    for r in todo:
        try:
            info = yf.Ticker(r["ticker"]).info or {}
            sec = YF_TO_GICS.get((info.get("sector") or "").strip())
            if sec:
                r["gics_sector"] = sec
                r["gics_industry"] = (info.get("industry") or "").strip()
                r["name"] = r.get("name") or info.get("shortName") or r["ticker"]
                filled += 1
            else:
                r["gics_sector"] = "(unmapped)"
        except Exception:                                             # noqa: BLE001
            r["gics_sector"] = "(unmapped)"
        if sleep:
            time.sleep(sleep)
    return filled


def _load_cache(path: Path) -> dict[str, float]:
    out: dict[str, float] = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            d = json.loads(line)
            if d.get("mcap"):
                out[d["ticker"]] = float(d["mcap"])
        except Exception:                                             # noqa: BLE001
            continue
    return out


def _fetch_mcaps(rows: list[dict], cache_path: Path, sleep: float, retry: int,
                 from_cache: bool) -> tuple[dict[str, float], Counter]:
    cached = _load_cache(cache_path)
    fails = Counter()
    if from_cache:
        log(f"[cache] 네트워크 0콜 — 캐시 {len(cached)}건으로 재집계")
        return cached, fails

    import yfinance as yf

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    got = dict(cached)
    todo = [r for r in rows if r["ticker"] not in got]
    log(f"[mcap] 조회 {len(todo)}종목 (캐시 적중 {len(rows)-len(todo)}) — 실측 0.6초/종목")
    t0 = time.time()
    with cache_path.open("a", encoding="utf-8") as fh:
        for i, r in enumerate(todo, 1):
            tk = r["ticker"]
            mc = None
            for attempt in range(retry + 1):
                try:
                    # ⚠ 속성으로 읽는다. `.get("market_cap")` 은 조용히 None(키는 camelCase).
                    mc = yf.Ticker(tk).fast_info.market_cap
                    if mc:
                        break
                except Exception:                                     # noqa: BLE001
                    mc = None
                if attempt < retry:
                    time.sleep(0.5)
            if mc:
                got[tk] = float(mc)
                fh.write(json.dumps({"ticker": tk, "mcap": float(mc)}) + "\n")
            else:
                fails[tk] = 1
            if sleep:
                time.sleep(sleep)
            if i % 100 == 0:
                el = time.time() - t0
                log(f"  … {i}/{len(todo)} · {el:.0f}s · 남은 추정 {(len(todo)-i)*el/i/60:.1f}분")
    return got, fails


def _threshold_table(rows: list[dict]) -> str:
    caps = sorted((r["market_cap_usd"] for r in rows), reverse=True)
    L = ["  시총 하한별 잔존 종목수 (임의 컷의 대안 효과 — 규칙 C5)"]
    for floor, lab in ((0, "없음"), (1e9, "1B"), (2e9, "2B"), (5e9, "5B"),
                       (1e10, "10B"), (2e10, "20B"), (5e10, "50B")):
        n = sum(1 for c in caps if c >= floor)
        L.append(f"    >= {lab:>5}  {n:5d}종목")
    return "\n".join(L)


def _diff_vs_live(rows: list[dict]) -> str:
    """현행 유니버스와의 차집합 — 유니버스가 바뀌면 모든 스윕의 분모가 바뀐다."""
    if not LIVE.exists():
        return "  (현행 us_top300.csv 없음 — 비교 생략)"
    old = {r["ticker"] for r in csv.DictReader(LIVE.open(encoding="utf-8"))}
    new = {r["ticker"] for r in rows}
    added, dropped = new - old, old - new
    L = [f"  현행 {len(old)}종목 → 신규 {len(new)}종목  (추가 {len(added)} · 이탈 {len(dropped)})"]
    if dropped:
        L.append(f"    ⚠ 이탈: {', '.join(sorted(dropped)[:20])}"
                 + (" …" if len(dropped) > 20 else ""))
        L.append("      이탈 종목은 스윕에서 **사라진다** — 보유 중이면 태그 불가가 된다. 확인 필수.")
    watch = {"LNG", "STNG", "FRO", "INSW", "DHT", "TNK"}
    hit = sorted(watch & new)
    miss = sorted(watch - new)
    if hit:
        L.append(f"    ★ 데스크가 「계기에 없다」고 기록해 온 이름 중 편입: {', '.join(hit)}")
    if miss:
        L.append(f"    ⚠ 아직 없는 관찰대상: {', '.join(miss)} — `--include` 로 강제 편입할 수 있다")
    # 🚨 불변식: 보유 종목은 반드시 유니버스에 있어야 한다. 없으면 스윕이 그 이름을 태그 못 한다.
    try:
        import sqlite3
        db = ROOT / "data" / "paper_book.db"
        if db.exists():
            con = sqlite3.connect(str(db))
            try:
                held = {t for (t,) in con.execute("SELECT ticker FROM positions WHERE qty > 0")
                        if str(t).isalpha()}
            finally:
                con.close()
            gap = sorted(held - new)
            L.append(f"    보유 US 종목 {len(held)}개 중 유니버스 밖: "
                     + (f"🚨 {', '.join(gap)}" if gap else "없음 ✅"))
    except Exception:                                                 # noqa: BLE001
        pass
    return "\n".join(L)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:                                                 # noqa: BLE001
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-cap-usd", type=float, default=0.0,
                    help="시총 하한(USD). 기본 0 = 하한 없음. 컷의 대안 효과는 표로 함께 낸다.")
    ap.add_argument("--limit", type=int, default=None, help="선두 N개만 조회(표본 테스트)")
    ap.add_argument("--sleep", type=float, default=0.0, help="호출 간 추가 대기(초)")
    ap.add_argument("--retry", type=int, default=1, help="일시 실패 재시도 횟수")
    ap.add_argument("--out", type=str, default=str(OUT_DEFAULT),
                    help="출력 CSV. 기본은 **후보 파일** — us_top300.csv 덮어쓰기는 명시해야 한다.")
    ap.add_argument("--cache", type=str, default=str(CACHE_DEFAULT), help="시총 캐시 JSONL")
    ap.add_argument("--from-cache", action="store_true", help="네트워크 0콜 — 캐시로 재집계만")
    ap.add_argument("--no-live", action="store_true",
                    help="현행 us_top300 을 합집합에 넣지 않는다 (기본은 넣는다 — ADR·외국국적 보존)")
    ap.add_argument("--no-book", action="store_true",
                    help="보유 종목을 강제 편입하지 않는다 (기본은 편입 — 「보유는 태그 가능해야 한다」)")
    ap.add_argument("--include", default="",
                    help="쉼표구분 강제 편입 티커 (지수 밖 관찰 대상, 예: LNG,STNG,FRO,DHT,TNK)")
    a = ap.parse_args()

    rows, per_index = _fetch_constituents()
    if not rows:
        log("[err] 구성종목을 하나도 못 받았다 — 페이지 구조 변경 또는 네트워크. 중단.")
        return 2
    log(f"[src] 지수 합계 {len(rows)}종목 · {dict(per_index)}")

    # ── 합집합: 지수 ∪ 현행 ∪ 보유 ∪ --include ──────────────────────────────
    # 지수 목록은 유니버스가 아니다(외국국적·비편입 배제). 상세는 `_extra_tickers` 주석.
    have = {r["ticker"] for r in rows}
    extras = {tk: r for tk, r in _extra_tickers(not a.no_live, not a.no_book, a.include).items()
              if tk not in have}
    if extras:
        by_src = Counter(r["index"] for r in extras.values())
        log(f"[union] 지수 밖 편입 {len(extras)}종목 · 출처 {dict(by_src)}")
        rows.extend(extras.values())
    truncated = 0
    if a.limit and a.limit < len(rows):
        truncated = len(rows) - a.limit
        rows = rows[:a.limit]

    if not a.from_cache:
        n_filled = _fill_sectors(rows, a.sleep)
        if n_filled:
            log(f"[sector] {n_filled}종목 섹터 보강 완료")

    caps, fails = _fetch_mcaps(rows, Path(a.cache), a.sleep, a.retry, a.from_cache)
    kept, no_cap, below = [], 0, 0
    for r in rows:
        mc = caps.get(r["ticker"])
        if not mc:
            no_cap += 1
            continue
        if mc < a.min_cap_usd:
            below += 1
            continue
        kept.append({**r, "market_cap_usd": int(mc), "market_cap_h": _cap_h(mc)})
    kept.sort(key=lambda r: -r["market_cap_usd"])
    for i, r in enumerate(kept, 1):
        r["rank"] = i

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(kept)

    print(f"# US 유니버스 빌드 — {len(kept)}종목 → {out}")
    print(f"  소스: {dict(per_index)}  (합계 {sum(per_index.values())})")
    if truncated:
        print(f"  ⚠ --limit 로 {truncated}종목 잘라냄 (표본 실행)")
    print(f"  제외: 시총 미조회 {no_cap}  ·  하한 미달 {below}  (하한 {a.min_cap_usd:,.0f} USD)")
    if fails:
        ex = ", ".join(sorted(fails)[:15])
        print(f"  ⚠ 시총 실패 {len(fails)}종목: {ex}{' …' if len(fails) > 15 else ''}")
        print(f"     — 실패는 **빈칸으로 남긴다**. 0 으로 채우면 랭킹 바닥에 가짜 종목이 생긴다(P4).")
    print()
    print(_threshold_table(kept))
    print()
    print("  현행 유니버스와의 차집합")
    print(_diff_vs_live(kept))
    print()
    sec = Counter(r["gics_sector"] for r in kept)
    print("  GICS 섹터 분포")
    for k, v in sec.most_common():
        print(f"    {v:5d}  {k}")
    print()
    print(f"  ⚠ 이 파일은 **후보**다. 라이브로 올리려면 사람이 확인하고 옮긴다 —")
    print(f"     유니버스가 바뀌면 스윕·섹터집계·거부원장 벤치의 **분모가 전부 바뀐다.**")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
