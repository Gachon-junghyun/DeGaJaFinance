# -*- coding: utf-8 -*-
"""build_kr_universe — KR 유니버스 CSV 빌더 (KOSPI + KOSDAQ).

왜: sector_flow / breadth / 잔차 기저율 등 모든 KR 스테이지의 **분모**가 이 CSV 다.
    v1 은 KOSPI 전용(832종, market 컬럼 "KOSPI" 하드코딩)이라 코스닥이 통째로 0종이었다.
    2026-08-03 실측 비용: 대회 상위 책의 상승 상위 5종이 전부 분모 밖이었고,
    그중 319400(현대무벡스)은 우리 게이트를 통과하는 이름이었다.

티커 소스: `module_disclosure/corp_codes.csv` (DART 전체 법인 → stock_code 있는 6자리 3,914종).
    v1 이 읽던 `data_build/kospi_all.txt` 는 이 리포에 **존재하지 않는다**(KOSPI 조차 재빌드 불가였음).
    같은 파일을 v1 도 이미 '이름' 용으로 읽고 있었다 — 코드만 안 가져왔다.

시세/시총/업종/시장 소스: KIS Open API `inquire-price` 1콜 (module_KIS._client.kis_get 재사용, P1).
    - 시총 = hts_avls(억원)  ← v1 과 동일 경로
    - 업종 = bstp_kor_isnm   ← v1 과 동일 경로
    - **시장 = rprs_mrkt_kor_name**(KOSPI/KOSPI200/KOSDAQ/KSQ150/KONEX …) ← v1 이 안 읽던 필드
    ⚠ 실측 함정: **상장폐지 코드도 rprs_mrkt_kor_name='KOSPI' 를 그대로 돌려준다**(hts_avls='0').
      그래서 시장 판정은 반드시 `hts_avls > 0` 인 살아있는 응답에만 적용한다.
    (pykrx 는 2026년부터 KRX 인증 요구로 무인증 사용 불가 — module_valuation/_naver_fetch.py 주석 참조.)

출력: 기본 `data/kr_universe/kr_all_v2_candidate.csv` (**후보 파일**).
    ⚠ 라이브 분모인 `kr_all.csv` 는 사람 승인 없이 덮어쓰지 않는다 — 덮어쓰려면 --out 을 명시해야 한다.
    컬럼 = rank,ticker,name,market_cap_krw,market_cap_h,sector,market  (us_top300.csv 미러)
    ticker 접미사 = KOSPI→.KS / KOSDAQ→.KQ (module_flow/_config·module_paper_book/_allocate 규약).

사용:
  python -X utf8 data/kr_universe/build_kr_universe.py --limit 60          # 표본 테스트
  python -X utf8 data/kr_universe/build_kr_universe.py                     # 전수(~8분)
  python -X utf8 data/kr_universe/build_kr_universe.py --min-cap-eok 1000  # 시총 하한 변경
  python -X utf8 data/kr_universe/build_kr_universe.py --from-cache        # API 0콜, 캐시 재집계
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # 리포 루트
CORP_CODES = ROOT / "module_disclosure" / "corp_codes.csv"
OUT_DEFAULT = ROOT / "data" / "kr_universe" / "kr_all_v2_candidate.csv"
CACHE_DEFAULT = ROOT / "out" / "kr_universe" / "kr_quotes_raw.jsonl"

# 시총 하한 후보(억원) — 사람이 고르라고 항상 같이 낸다.
THRESHOLDS_EOK = [1000, 2000, 3000, 5000, 10000]

# 이름으로 거르는 스팩(SPAC). DART 법인명 기준.
SPAC_TOKENS = ("기업인수목적", "스팩")

# ⚠ iscd_stat_cls_code 는 **배제에 쓰지 않는다** — 실측으로 못 믿을 필드다.
#   2026-08-03 전수: status='58'(모듈 라벨상 '거래정지') 123종 전부 temp_stop_yn='N' 이고
#   실시간 체결가가 살아있다. 그 안에 한화(000880, 5.9조, KOSPI200)·코미코(183300, 1.1조)가 있다.
#   즉 58 을 거래정지로 읽으면 멀쩡한 대형주를 조용히 떨어뜨린다(모듈 `_quote._RISK_STATUS` 도
#   58 을 리스크로 넣고 있다 — 별건 결함, 사람 판단으로 남긴다).
#   배제는 뜻이 분명한 플래그로만 한다: mang_issu_cls_code / sltr_yn / temp_stop_yn / mrkt_warn_cls_code.
#   status 는 세어서 보고만 한다(조용한 절단 금지).
STATUS_OBSERVE = ("51", "52", "53", "54", "58", "59")
# mrkt_warn_cls_code — 02 투자경고 / 03 투자위험 배제(01 투자주의는 유지).
# 실측: warn='02' 16종은 status 53(투자경고)과 일치 — 경고 축은 warn 이 단일 원본.
WARN_EXCLUDE = {"02", "03"}


def _load_dotenv() -> None:
    """프로젝트 루트 .env 파싱해 환경변수 주입(module_KIS __main__ 동일 패턴)."""
    if os.environ.get("KIS_APP_KEY") and os.environ.get("KIS_APP_SECRET"):
        return
    p = ROOT / ".env"
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and v and k not in os.environ:
            os.environ[k] = v


def _load_candidates() -> tuple[list[tuple[str, str]], Counter]:
    """corp_codes.csv → [(code6, name)] + 사전(pre-API) 제외 카운터.

    DART corp_codes 는 상장/비상장/폐지 법인을 모두 담는다. stock_code 가 채워진 행만
    상장(이력) 이고, 실제 생존 여부는 KIS 응답이 판정한다.
    """
    excl = Counter()
    rows = []
    with open(CORP_CODES, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            sc = (r.get("stock_code") or "").strip()
            nm = (r.get("corp_name") or "").strip()
            if not sc:
                excl["stock_code 없음(비상장 법인)"] += 1
                continue
            if len(sc) != 6 or not sc.isdigit():
                excl["6자리 숫자코드 아님"] += 1
                continue
            if sc[-1] != "0":
                # 우선주는 끝자리가 5/7/K 등. DART 는 법인 단위라 실측 0건이지만
                # 소스가 바뀌어도 조용히 새지 않게 명시적으로 남긴다.
                excl["우선주(코드 끝자리≠0)"] += 1
                continue
            if any(t in nm for t in SPAC_TOKENS):
                excl["스팩(기업인수목적·스팩)"] += 1
                continue
            rows.append((sc, nm))
    return rows, excl


def _classify_market(raw_name: str) -> str:
    """rprs_mrkt_kor_name → KOSPI / KOSDAQ / KONEX / UNKNOWN.

    실측값: 'KOSPI', 'KOSPI200', 'KOSDAQ', 'KSQ150', 'KONEX'.
    ⚠ 살아있는 응답(hts_avls>0)에만 적용할 것 — 폐지 코드는 무조건 'KOSPI' 를 준다.
    """
    n = (raw_name or "").strip().upper()
    if not n:
        return "UNKNOWN"
    if n.startswith("KSQ") or "KOSDAQ" in n or "코스닥" in n:
        return "KOSDAQ"
    if "KONEX" in n or "코넥스" in n:
        return "KONEX"
    if "KOSPI" in n or "코스피" in n:
        return "KOSPI"
    return "UNKNOWN"


def _won_h(won: float) -> str:
    """원 → 사람 읽는 조/억 표기."""
    if won >= 1e12:
        return f"{won/1e12:.2f}조"
    if won >= 1e8:
        return f"{won/1e8:.0f}억"
    return f"{won:.0f}"


def _fetch_raw(codes: list[tuple[str, str]], sleep: float, retry: int,
               cache_path: Path) -> tuple[list[dict], Counter]:
    """KIS inquire-price 전수 조회 → 원시 필드 dict 리스트 + 실패 카운터. 캐시 동시 기록."""
    sys.path.insert(0, str(ROOT)) if str(ROOT) not in sys.path else None
    from module_KIS._client import kis_get          # 인증·레이트리밋·토큰재발급 재사용(P1)
    from module_KIS._auth import load_config
    from module_KIS._quote import _PATH, _TR_ID     # 엔드포인트 단일 원본

    cfg = load_config()
    fails = Counter()
    out: list[dict] = []
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    fcache = open(cache_path, "w", encoding="utf-8")
    t0 = time.time()
    for i, (code, name) in enumerate(codes, 1):
        o = None
        for attempt in range(retry + 1):
            try:
                body = kis_get(_PATH, _TR_ID,
                               {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": code},
                               cfg=cfg)
                o = body.get("output") or {}
                break
            except Exception as e:                                   # noqa: BLE001
                if attempt >= retry:
                    fails["API 오류"] += 1
                    print(f"[warn] {code} {name} API 실패: {type(e).__name__}: {e}",
                          file=sys.stderr)
                else:
                    time.sleep(0.3)
        if o is None:
            continue
        rec = {
            "code": code,
            "name": name,
            "cap_eok": (o.get("hts_avls") or "").strip(),
            "sector": (o.get("bstp_kor_isnm") or "").strip(),
            "mrkt_raw": (o.get("rprs_mrkt_kor_name") or "").strip(),
            "status": (o.get("iscd_stat_cls_code") or "").strip(),
            "warn": (o.get("mrkt_warn_cls_code") or "").strip(),
            "mang": (o.get("mang_issu_cls_code") or "").strip(),
            "temp_stop": (o.get("temp_stop_yn") or "").strip(),
            "sltr": (o.get("sltr_yn") or "").strip(),
            "price": (o.get("stck_prpr") or "").strip(),
        }
        out.append(rec)
        fcache.write(json.dumps(rec, ensure_ascii=False) + "\n")
        if sleep:
            time.sleep(sleep)
        if i % 200 == 0:
            print(f"[info] {i}/{len(codes)} … ({time.time()-t0:.0f}s)", file=sys.stderr)
    fcache.close()
    print(f"[info] 조회 완료 {len(out)}/{len(codes)} ({time.time()-t0:.0f}s) → 캐시 {cache_path}",
          file=sys.stderr)
    return out, fails


def _apply_filters(raws: list[dict]) -> tuple[list[dict], Counter, Counter]:
    """원시 응답 → 유니버스 행(시총 하한 적용 전) + 필터별 제외 카운터 + 관측만 한 플래그."""
    excl = Counter()
    obs = Counter()
    rows: list[dict] = []
    for r in raws:
        try:
            cap_eok = float(r["cap_eok"]) if r["cap_eok"] else 0.0
        except ValueError:
            cap_eok = 0.0
        if cap_eok <= 0:
            # 폐지·비상장·거래불가 — KIS 가 빈 응답(시총 0)을 준다.
            excl["미상장/폐지(시총 0 응답)"] += 1
            continue
        mkt = _classify_market(r["mrkt_raw"])
        if mkt == "KONEX":
            excl["코넥스"] += 1
            continue
        if mkt == "UNKNOWN":
            excl["시장 판정 불가"] += 1
            continue
        if r["mang"] == "Y":
            excl["관리종목(mang_issu_cls_code=Y)"] += 1
            continue
        if r["sltr"] == "Y":
            excl["정리매매(sltr_yn=Y)"] += 1
            continue
        if r["temp_stop"] == "Y":
            excl["거래정지(temp_stop_yn=Y)"] += 1
            continue
        if r["warn"] in WARN_EXCLUDE:
            excl[f"시장경고 {r['warn']}(투자경고/위험)"] += 1
            continue
        if r["status"] in STATUS_OBSERVE:                 # 배제 아님 — 세기만 한다
            obs[f"iscd_stat_cls_code={r['status']} (편입됨, 미배제)"] += 1
        cap_won = cap_eok * 1e8
        suf = ".KQ" if mkt == "KOSDAQ" else ".KS"
        rows.append({
            "ticker": f"{r['code']}{suf}",
            "name": r["name"] or r["code"],
            "market_cap_krw": int(cap_won),
            "market_cap_h": _won_h(cap_won),
            "sector": r["sector"] or "미분류",
            "market": mkt,
            "_cap_eok": cap_eok,
        })
    return rows, excl, obs


def _threshold_table(rows: list[dict]) -> str:
    lines = ["시총하한(억) | KOSPI | KOSDAQ | 합계",
             "---|---|---|---"]
    for th in THRESHOLDS_EOK:
        sel = [r for r in rows if r["_cap_eok"] >= th]
        kp = sum(1 for r in sel if r["market"] == "KOSPI")
        kq = sum(1 for r in sel if r["market"] == "KOSDAQ")
        lines.append(f"{th:,} | {kp} | {kq} | {kp+kq}")
    kp = sum(1 for r in rows if r["market"] == "KOSPI")
    kq = sum(1 for r in rows if r["market"] == "KOSDAQ")
    lines.append(f"하한없음 | {kp} | {kq} | {kp+kq}")
    return "\n".join(lines)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:                                                 # noqa: BLE001
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-cap-eok", type=float, default=3000.0,
                    help="시총 하한(억원). 기본 3000억. 0 이면 하한 없음.")
    ap.add_argument("--limit", type=int, default=None,
                    help="선두 N개만 조회(표본 테스트). 잘라낸 개수를 보고한다.")
    ap.add_argument("--sleep", type=float, default=0.0, help="호출 간 추가 대기(초)")
    ap.add_argument("--retry", type=int, default=1, help="일시 실패 재시도 횟수")
    ap.add_argument("--out", type=str, default=str(OUT_DEFAULT),
                    help="출력 CSV. 기본은 후보 파일 — kr_all.csv 덮어쓰기는 명시해야 한다.")
    ap.add_argument("--cache", type=str, default=str(CACHE_DEFAULT),
                    help="원시 응답 JSONL 캐시 경로")
    ap.add_argument("--from-cache", action="store_true",
                    help="API 0콜 — 기존 캐시로 필터·표만 재집계")
    a = ap.parse_args()

    cands, pre_excl = _load_candidates()
    total_cand = len(cands)
    truncated = 0
    if a.limit and a.limit < len(cands):
        truncated = len(cands) - a.limit
        cands = cands[:a.limit]

    cache_path = Path(a.cache)
    if a.from_cache:
        raws = [json.loads(l) for l in open(cache_path, encoding="utf-8") if l.strip()]
        api_fail = Counter()
        print(f"[info] 캐시 {len(raws)}행 재사용 ({cache_path}) — API 0콜", file=sys.stderr)
    else:
        _load_dotenv()
        print(f"[info] 후보 {len(cands)}종 조회 시작 (KIS inquire-price 1콜/종)",
              file=sys.stderr)
        raws, api_fail = _fetch_raw(cands, a.sleep, a.retry, cache_path)

    rows, excl, obs = _apply_filters(raws)
    excl.update(api_fail)

    # 시총 하한 적용
    kept = [r for r in rows if r["_cap_eok"] >= a.min_cap_eok] if a.min_cap_eok > 0 else rows
    excl[f"시총 < {a.min_cap_eok:,.0f}억"] = len(rows) - len(kept)

    kept.sort(key=lambda r: r["market_cap_krw"], reverse=True)
    for rk, r in enumerate(kept, 1):
        r["rank"] = rk

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    cols = ["rank", "ticker", "name", "market_cap_krw", "market_cap_h", "sector", "market"]
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in kept:
            w.writerow({k: r[k] for k in cols})

    # ── 보고 ────────────────────────────────────────────────────────────
    print(f"\n[source] corp_codes 후보 {total_cand}종" +
          (f" · --limit 로 잘라낸 것 {truncated}종(조용한 절단 아님)" if truncated else ""))
    print("\n[pre-API 제외]")
    for k, v in pre_excl.most_common():
        print(f"  {k}: {v}")
    print("\n[post-API 필터별 제외]")
    for k, v in excl.most_common():
        print(f"  {k}: {v}")
    print("\n[관측만 · 배제 안 함]")
    for k, v in obs.most_common():
        print(f"  {k}: {v}")
    print(f"\n[통과] 하한 적용 전 {len(rows)}종 · 하한 {a.min_cap_eok:,.0f}억 적용 후 {len(kept)}종")
    print("\n[시총 하한별 편입 수]")
    print(_threshold_table(rows))
    sec = Counter(r["sector"] for r in kept)
    print("\n[섹터 상위] " + " · ".join(f"{s}:{n}" for s, n in sec.most_common(12)))
    print(f"\n[out] {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
