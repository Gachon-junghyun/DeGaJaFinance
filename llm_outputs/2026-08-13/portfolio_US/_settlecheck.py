# -*- coding: utf-8 -*-
"""마지막 봉이 정착(settled)인가 미정착(live partial)인가를 기계적으로 판정한다.

D74 의 재발 방지. S63 등록문 자체가 이 실수를 기록하고 있다:
  "첫 검증 패스가 LIVE 2026-08-06 부분봉을 포함해 DUR −5.336 을 읽었고,
   08-05 정착에 고정하니 −6.197 이었다. 0.86 포인트 갭이 D74."

테스트 3개 (S68-ANNEX 의 successor construction 을 시각축에 적용):
  (a) 마지막 봉 거래량 / 직전 20봉 중앙값  — 장중이면 현저히 낮다
  (b) 현재 ET 시각이 16:00 이전인가
  (c) 마지막 봉 날짜 == 오늘(ET) 인가
"""
import sys, io, datetime as dt, zoneinfo
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import yfinance as yf

ET = zoneinfo.ZoneInfo("America/New_York")
now_et = dt.datetime.now(tz=ET)
print(f"[clock] now(ET) = {now_et:%Y-%m-%d %H:%M:%S %Z}")
print(f"[clock] now(KST) = {dt.datetime.now(tz=zoneinfo.ZoneInfo('Asia/Seoul')):%Y-%m-%d %H:%M:%S %Z}")
print(f"[clock] US 정규장 마감 16:00 ET ⇒ 오늘 마감까지 남은 시간: "
      f"{(now_et.replace(hour=16, minute=0, second=0) - now_et)}")
print()

for t in ("SPY", "XLU", "XLI", "HPE", "ANET"):
    d = yf.download(t, period="2mo", progress=False, auto_adjust=False)
    if isinstance(d.columns, type(d.columns)) and hasattr(d.columns, "get_level_values"):
        try:
            d.columns = d.columns.get_level_values(0)
        except Exception:
            pass
    v = d["Volume"].astype(float)
    med20 = float(v.iloc[-21:-1].median())
    lastv = float(v.iloc[-1])
    lastd = d.index[-1].date()
    ratio = lastv / med20 if med20 else float("nan")
    verdict = "미정착(LIVE 부분봉)" if (ratio < 0.75 and str(lastd) == f"{now_et:%Y-%m-%d}") else "정착 가능성"
    print(f"  {t:<5} 마지막봉 {lastd}  vol {lastv:>14,.0f} / 20봉중앙 {med20:>14,.0f} "
          f"= {ratio:.2f}x  ⇒ {verdict}")
