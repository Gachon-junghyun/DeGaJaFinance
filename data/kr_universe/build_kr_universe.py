# -*- coding: utf-8 -*-
"""build_kr_universe — KR 유니버스 CSV 빌더 (sector_flow 와이드 스윕 해금용 1단계).

왜: sector_flow.py(유니버스 flow 스윕 → 신규🟢 LIVE 발굴)가 us_top300.csv 에만 물려 있다.
    KR판 유니버스 [ticker·시총·업종] CSV 를 만들어 `sector_flow --market kr` 를 배선하기 위한 전제.
    (INDUSTRY_ANALYSIS_KR.md §8-2 '섹터 배치 스크리너 부재' 갭 해소의 첫 조각.)

소스: KIS Open API `fetch_quote(code)` — 시가총액(억원, hts_avls) + 업종(bstp_kor_isnm) 한 번에.
      (pykrx 는 이 환경에서 KRX 서버 응답 부재로 미사용. KIS 가 라이브 작동하는 유일 소스.)
      이름은 로컬 data_build/kr_aliases.json 조인(추가 API 호출 0), 없으면 코드로 폴백.

유니버스: data_build/kospi_all.txt (Naver 시총 desc 정렬, KOSPI 839). KOSDAQ 는 v1.1(코드 소스 필요).

출력: data_build/kr_universe/kr_all.csv
      컬럼 = rank,ticker,name,market_cap_krw,market_cap_h,sector,market   (us_top300.csv 미러)
      ticker 는 flow_read/차트 규약대로 .KS 접미사.

사용:
  python -X utf8 data_build/kr_universe/build_kr_universe.py                 # 전체(839, ~수분)
  python -X utf8 data_build/kr_universe/build_kr_universe.py --limit 120     # 상위 120 테스트
  python -X utf8 data_build/kr_universe/build_kr_universe.py --sleep 0.05 --retry 2
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # research_Mvp
TICKERS = ROOT / "data_build" / "kospi_all.txt"
ALIASES = ROOT / "data_build" / "kr_aliases.json"
OUT_DEFAULT = ROOT / "data_build" / "kr_universe" / "kr_all.csv"


def _load_dotenv() -> None:
    """프로젝트 루트 .env 파싱해 환경변수 주입(module_kis __main__ 동일 패턴)."""
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


def _load_tickers(limit: int | None) -> list[str]:
    codes: list[str] = []
    raw = TICKERS.read_bytes()
    for enc in ("utf-8", "cp949", "euc-kr"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        text = raw.decode("utf-8", errors="ignore")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # 6자리 숫자 코드만
        code = line.split()[0].strip()
        if len(code) == 6 and code.isdigit():
            codes.append(code)
    if limit:
        codes = codes[:limit]
    return codes


def _load_names() -> dict:
    """code→name. 1차 DART corp_codes.csv(3,951종), 2차 kr_aliases.json 폴백."""
    names: dict = {}
    dart = ROOT / "module_disclosure" / "corp_codes.csv"
    if dart.exists():
        import csv as _csv
        with open(dart, encoding="utf-8") as f:
            for r in _csv.DictReader(f):
                sc = (r.get("stock_code") or "").strip()
                if sc and sc.isdigit():
                    names[sc.zfill(6)] = (r.get("corp_name") or "").strip()
    if ALIASES.exists():
        d = json.load(open(ALIASES, encoding="utf-8"))
        for k, v in d.items():                       # 별칭 우선(HTS 표기 선호)
            names[k] = v.get("name") or names.get(k) or k
    return names


def _won_h(won: float) -> str:
    """원 → 사람 읽는 조/억 표기."""
    if won >= 1e12:
        return f"{won/1e12:.2f}조"
    if won >= 1e8:
        return f"{won/1e8:.0f}억"
    return f"{won:.0f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="상위 N개만(테스트)")
    ap.add_argument("--sleep", type=float, default=0.0, help="호출 간 대기(초, 레이트리밋)")
    ap.add_argument("--retry", type=int, default=1, help="일시 실패 재시도 횟수")
    ap.add_argument("--out", type=str, default=str(OUT_DEFAULT))
    a = ap.parse_args()

    _load_dotenv()
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    try:
        from module_kis import fetch_quote, load_config
    except Exception as e:  # noqa
        print(f"[FATAL] module_kis import 실패: {e}", file=sys.stderr)
        return 2
    try:
        cfg = load_config()
    except Exception as e:  # noqa
        print(f"[FATAL] KIS config 실패(.env 확인): {e}", file=sys.stderr)
        return 2

    codes = _load_tickers(a.limit)
    names = _load_names()
    print(f"[info] 대상 {len(codes)}종 · 이름사전 {len(names)} · 소스 KIS fetch_quote",
          file=sys.stderr)

    rows: list[dict] = []
    fail: list[str] = []
    t0 = time.time()
    for i, code in enumerate(codes, 1):
        q = None
        for attempt in range(a.retry + 1):
            try:
                q = fetch_quote(code, cfg=cfg)
                break
            except Exception as e:  # noqa
                if attempt >= a.retry:
                    fail.append(code)
                    print(f"[warn] {code} 실패: {e}", file=sys.stderr)
                else:
                    time.sleep(0.3)
        if q is None:
            continue
        cap_eok = q.market_cap_eok
        if not cap_eok or cap_eok <= 0:
            fail.append(code)
            continue
        cap_won = float(cap_eok) * 1e8  # 억원 → 원
        rows.append({
            "ticker": f"{code}.KS",
            "name": names.get(code) or (q.name or code),
            "market_cap_krw": int(cap_won),
            "market_cap_h": _won_h(cap_won),
            "sector": (q.sector or "미분류").strip(),
            "market": "KOSPI",
        })
        if a.sleep:
            time.sleep(a.sleep)
        if i % 25 == 0:
            print(f"[info] {i}/{len(codes)} … ({time.time()-t0:.0f}s)", file=sys.stderr)

    # 시총 desc 정렬 + rank
    rows.sort(key=lambda r: r["market_cap_krw"], reverse=True)
    for rk, r in enumerate(rows, 1):
        r["rank"] = rk

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    cols = ["rank", "ticker", "name", "market_cap_krw", "market_cap_h", "sector", "market"]
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in cols})

    print(f"[done] {len(rows)}종 → {out}  (실패 {len(fail)}, {time.time()-t0:.0f}s)",
          file=sys.stderr)
    # 섹터 분포 요약(stderr)
    from collections import Counter
    sec = Counter(r["sector"] for r in rows)
    print("[sector] " + " · ".join(f"{s}:{n}" for s, n in sec.most_common(12)),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
