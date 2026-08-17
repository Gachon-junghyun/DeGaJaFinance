# FILE: scripts/snapshot_estimates.py
"""
SNAPSHOT_ESTIMATES — 추정치 리비전을 **시계열로 쌓는다** (dig D16).

왜: yfinance `eps_trend` 는 시계열이 아니라 **스냅샷**(현재/7·30·60·90일전 수준)이다. 그래서
`scripts/measure_ic.py` 가 낼 수 있는 건 한 시점의 횡단면 IC 뿐이고, 규칙 S1 상 유효 표본이
**날짜 수**이므로 그걸로는 `kelly_size.py --ic` 를 정당화할 수 없다(2026-07-22 실측: IC +0.249
지만 Q5 의 72% 가 IT 한 섹터 → 구분 불가).

★ **이 데이터는 소급 복구가 불가능하다.** 오늘 저장하지 않은 날은 영영 사라진다. 시작 비용은
파일 하나이고 미루는 비용은 매일 하루씩 커진다 — dig 목록에서 이 비대칭이 가장 큰 항목이다.

저장: `data/estimates/eps_YYYY-MM-DD.json`  (날짜당 1파일 · 재실행 멱등 · 사람이 열어볼 수 있음)
      DB 를 새로 만들지 않는다(P1: 두 번째 DB 금지). 작고 append-only 라 커밋 대상이다.

사용:
  python -X utf8 scripts/snapshot_estimates.py                    # us_top300 상위 120
  python -X utf8 scripts/snapshot_estimates.py --limit 300 --force
  python -X utf8 scripts/snapshot_estimates.py --status           # 쌓인 날짜 현황

⚠ 매일 돌려야 의미가 있다. 스케줄러가 자동 발사하는 **주문** 코드는 만들지 않지만(CLAUDE.md),
   이건 조회·저장 전용이라 사람이 cron/작업스케줄러에 걸어도 안전하다.
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "data" / "estimates"
PERIODS = ("0q", "+1q", "0y", "+1y")
LEVEL_COLS = ("current", "7daysAgo", "30daysAgo", "60daysAgo", "90daysAgo")
REV_COLS = ("upLast7days", "upLast30days", "downLast7Days", "downLast30days")


def _universe(name: str, limit: int) -> list[str]:
    f = ROOT / "data" / "us_universe" / f"{name}.csv"
    if not f.exists():
        return []
    out = [(r.get("ticker") or "").strip().upper()
           for r in csv.DictReader(f.open(encoding="utf-8"))]
    return [t for t in out if t][:limit]


def _frame_to_dict(df, cols) -> dict:
    """period 인덱스 프레임 → {period: {col: float}}. 숫자만 남긴다."""
    out: dict = {}
    if df is None:
        return out
    try:
        if df.empty:
            return out
    except Exception:
        return out
    for idx, row in df.iterrows():
        p = str(idx)
        if p not in PERIODS:
            continue
        d = {}
        for c in cols:
            if c in df.columns:
                try:
                    v = float(row[c])
                    if v == v:                      # NaN 제외
                        d[c] = v
                except Exception:
                    pass
        if d:
            out[p] = d
    return out


def snapshot(tickers: list[str], verbose: bool = True) -> dict:
    import warnings
    warnings.filterwarnings("ignore")
    import yfinance as yf

    rows: dict[str, dict] = {}
    for i, t in enumerate(tickers, 1):
        if verbose and i % 25 == 0:
            sys.stderr.write(f"  [{i}/{len(tickers)}]\n")
        try:
            tk = yf.Ticker(t)
            trend = _frame_to_dict(tk.eps_trend, LEVEL_COLS)
            revs = _frame_to_dict(tk.eps_revisions, REV_COLS)
            if not trend and not revs:
                continue
            rec: dict = {}
            if trend:
                rec["eps_trend"] = trend
            if revs:
                rec["eps_revisions"] = revs
            try:                                    # 그날 종가 — 나중 수익률 계산의 앵커
                h = tk.history(period="2d")["Close"]
                if len(h):
                    rec["close"] = float(h.iloc[-1])
            except Exception:
                pass
            rows[t] = rec
        except Exception:
            continue
    return rows


def cadence_report(files: list[Path], target: int = 40) -> list[str]:
    """저장 **속도를 실측**해 남은 기간을 캘린더 일로 낸다.

    🚨 예전 구현은 `40 - len(files)` 를 *"N일 더 필요"* 라고 출력했다. 그건 **하루도 안 거르고
    저장될 때만 참**이다. 실측(2026-08-09): 19 캘린더일에 **5개**, 간격 **2→3→4→6 단조 증가** —
    그 상태에서 화면은 *"35일 더"* 라고 말했지만 실제 속도로는 **~134일**이었다.
    ⇒ **계기가 진행률의 단위를 바꿔 자기 고장을 숨겼다.** 파일 개수는 진행률이 아니다.

    근본 원인은 코드가 아니라 배치다(P6): 이 데몬은 *"필요할 때만 켜는"* 클라이언트 PC 의 일일
    작업으로 걸려 있고, 24시간 도는 것은 서버 PC 다. 간격 증가는 사실상 **PC 를 켜는 빈도**다.
    """
    out: list[str] = []
    dates: list[_dt.date] = []
    for f in files:
        try:
            dates.append(_dt.date.fromisoformat(f.stem.replace("eps_", "")))
        except Exception:
            continue
    n = len(dates)
    if n == 0:
        return ["· 저장된 날짜 없음."]
    dates.sort()
    today = _dt.date.today()
    span = (dates[-1] - dates[0]).days + 1
    rate = n / span if span > 0 else 1.0
    remain = max(0, target - n)

    out.append(f"· 누적 **{n}개 파일** / **{span} 캘린더일** (첫 {dates[0]} → 끝 {dates[-1]})"
               f" ⇒ 실측 속도 **{rate:.2f}개/일**")
    if remain == 0:
        out.append(f"· 목표 {target}일치 도달 (규칙 S1: 유효 표본 = 날짜 수)")
    else:
        eta = remain / rate if rate > 0 else float("inf")
        ideal = remain
        out.append(f"· 목표 {target}일치까지 **{remain}개** 더 — 매일 쌓으면 {ideal}일, "
                   f"**실측 속도로는 약 {eta:.0f}일** (규칙 S1: 유효 표본 = 날짜 수)")
        if eta > ideal * 1.5:
            out.append(f"  🚨 실측 속도가 이상 대비 **{eta/ideal:.1f}배 느리다** — 스케줄이 도는지 확인하라. "
                       f"「파일 개수」로 보면 정상처럼 보이는 것이 이 계기의 함정이다(D16).")

    gaps = [(dates[i] - dates[i - 1]).days for i in range(1, n)]
    if gaps:
        out.append(f"· 간격(일): {gaps[-8:]} · 중앙 {sorted(gaps)[len(gaps)//2]} · 최대 {max(gaps)}")
        if len(gaps) >= 3 and gaps[-1] > gaps[0] and gaps[-1] >= 3:
            out.append("  ⚠ 간격이 **벌어지는 추세** — 하루 거르면 그날 관측은 영영 없다(소급 불가).")
    stale = (today - dates[-1]).days
    if stale >= 1:
        out.append(f"· 마지막 저장 이후 **{stale}일** 경과"
                   + ("  🚨 오늘 것부터 회수하라." if stale >= 2 else ""))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="추정치 스냅샷 저장 (dig D16)")
    ap.add_argument("--universe", default="us_top300")
    ap.add_argument("--limit", type=int, default=120)
    ap.add_argument("--tickers", default=None)
    ap.add_argument("--force", action="store_true", help="오늘 파일이 있어도 덮어쓴다")
    ap.add_argument("--status", action="store_true", help="쌓인 날짜만 보고 종료")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


    STORE.mkdir(parents=True, exist_ok=True)
    files = sorted(STORE.glob("eps_*.json"))

    if a.status:
        print(f"# 추정치 스냅샷 현황 — {STORE}")
        if not files:
            print("  저장된 날짜 없음. 오늘부터 쌓기 시작하면 된다.")
            return 0
        for f in files:
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
                print(f"  {d.get('date','?')}  {len(d.get('rows',{})):4d}종목  {f.stat().st_size/1024:6.1f}KB")
            except Exception as e:
                print(f"  {f.name}  읽기 실패 {e}")
        print(f"\n  총 {len(files)}일치.")
        for line in cadence_report(files, target=40):
            print("  " + line)
        print("  · ⚠ 소급 복구 불가. 안 쌓은 날은 영영 없다.")
        return 0

    today = _dt.date.today().isoformat()
    out = STORE / f"eps_{today}.json"
    if out.exists() and not a.force:
        print(f"오늘({today}) 스냅샷이 이미 있다 — {out.name}. 덮어쓰려면 --force")
        return 0

    tks = ([t.strip().upper() for t in a.tickers.split(",")] if a.tickers
           else _universe(a.universe, a.limit))
    if not tks:
        print("유니버스 비어 있음", file=sys.stderr)
        return 2

    print(f"# 추정치 스냅샷 {today} — {len(tks)}종목 수집")
    rows = snapshot(tks)
    payload = {
        "date": today,
        "source": "yfinance Ticker.eps_trend / eps_revisions",
        "note": "소급 복구 불가. 날짜당 1파일, 재실행 멱등. dig D16.",
        "periods": list(PERIODS),
        "rows": rows,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  저장 {out}  ({len(rows)}종목, {out.stat().st_size/1024:.1f}KB)")
    for line in cadence_report(sorted(STORE.glob("eps_*.json")), target=40):
        print("  " + line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
