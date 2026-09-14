# -*- coding: utf-8 -*-
"""⑤⑥⑧ 공매도·옵션 포지셔닝 (양방향 — 크라우딩/공포. 방향성 4축과 별개 차원).

⑧ short_flow  : KR 공매도잔고 비중%(KRX/pykrx, 국내 전용, KRX_ID/PW 필요)
⑤ _short_interest : US 공매도 %float(yfinance .info, 캐싱)
⑥ _options_pos    : US ~30DTE P/C OI비율 + IV스큐
positioning   : ⑤+⑥ 합성 읽기(스퀴즈연료/안일/공포/중립)
"""
from __future__ import annotations

import contextlib
import io
import json
from datetime import datetime, timedelta

import yfinance as yf

from ._config import SI_CACHE, SI_TTL_DAYS, OUT_DIR, kr_code, load_kis_env


def short_flow(tk: str, days: int = 20) -> dict | None:
    """⑧ 공매도잔고 비중(%) + building/covering — KRX(pykrx), 국내 전용.

    US ⑤ short-interest(%float)의 KR 대응 = 공매도잔고/상장주식수. yfinance는 KR 공매도를
    안 줘서 KRX 정보데이터시스템(로그인 필요, KRX_ID/KRX_PW)에서 직접. 반환 None=KR아님 / {error}=조회실패.
    """
    code = kr_code(tk)
    if not code:
        return None
    try:
        load_kis_env()                               # .env 주입(KRX_ID/KRX_PW 포함)
        from pykrx import stock
        end = datetime.now().strftime("%Y%m%d")
        start = (datetime.now() - timedelta(days=45)).strftime("%Y%m%d")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):         # pykrx 로그인 프린트 억제(테이블 오염 방지)
            df = stock.get_shorting_balance_by_date(start, end, code)
        if df is None or len(df) == 0 or "비중" not in getattr(df, "columns", []):
            note = "KRX 로그인/데이터 확인"
            if "로그인 실패" in buf.getvalue() or "아이디" in buf.getvalue():
                note = "KRX 로그인 실패(KRX_ID/PW 확인)"
            return {"error": f"no data ({note})"}
        pcts = df["비중"].astype(float)
        si = float(pcts.iloc[-1])
        prev = float(pcts.iloc[-min(len(pcts), 10)])   # ~10영업일 전 대비
        chg = round(si - prev, 3)
        trend = "building" if chg > 0.02 else "covering" if chg < -0.02 else "flat"
        return {"si_pct": round(si, 3), "trend": trend, "chg": chg,
                "crowded": si >= 2.0,      # KR 스케일: ≥2%면 진짜 크라우디드(스퀴즈 연료)
                "notable": si >= 0.5,      # ≥0.5%면 주목(하락압력 후보)
                "days": len(df)}
    except Exception as e:
        return {"error": str(e)[:60]}


def _short_interest(tk: str) -> dict:
    """⑤ 공매도 — yfinance .info(캐싱). %float + 전월대비(building/covering) + crowded(스퀴즈연료)."""
    cache = {}
    if SI_CACHE.exists():
        try:
            cache = json.loads(SI_CACHE.read_text(encoding="utf-8"))
        except Exception:
            cache = {}
    today = datetime.now().strftime("%Y-%m-%d")
    hit = cache.get(tk)
    if hit and hit.get("_cached") and (datetime.now() - datetime.strptime(hit["_cached"], "%Y-%m-%d")).days < SI_TTL_DAYS:
        return hit
    try:
        info = yf.Ticker(tk).info
        ss, sp = info.get("sharesShort"), info.get("sharesShortPriorMonth")
        pf = info.get("shortPercentOfFloat")
        rec = {
            "pct_float": round(pf * 100, 1) if pf else None,
            "days_to_cover": info.get("shortRatio"),
            "trend": ("building" if (ss and sp and ss > sp) else "covering" if (ss and sp and ss < sp) else "flat"),
            "chg_pct": round((ss / sp - 1) * 100, 1) if (ss and sp) else None,
            "crowded": bool(pf and pf >= 0.10),     # ≥10% float = 크라우디드 숏(스퀴즈 연료)
            "_cached": today,
        }
    except Exception as e:
        rec = {"pct_float": None, "trend": None, "crowded": False, "error": str(e)[:40], "_cached": today}
    cache[tk] = rec
    try:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        SI_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass
    return rec


def _implied_move(t, exps: list[str], spot: float | None, through: str | None = None) -> dict:
    """⑥-b ATM 스트래들 = 시장이 이미 가격에 반영한 **예상 변동폭**.

    왜 필요한가 (2026-07-22 추가): 스큐·P/C 는 '방어에 얼마나 지불하나'를 말하지만
    '얼마나 움직일 거라 보나'는 말하지 않는다. 이벤트 시나리오의 임계값을 **사람이 임의로**
    정하는 대신 시장이 정하게 한다 — handoff/SCENARIOS.md 의 브래킷 임계값 근거.
    실측(2026-07-22): GOOGL ±7.1% (당일 실적) · MU ±4.5% · AMD ±3.6%.
    ⚠ 스트래들은 만기까지의 **총** 예상변동이지 이벤트 단독 기여분이 아니다.

    🚨 **`through` 를 주면 그 날짜를 «span 하는» 첫 만기를 고른다 (D315 수정, 2026-09-03).**
    이전에는 `exps[0]` — 무조건 최근접 만기 — 를 썼다. 그래서:
      · 2026-08-24 `NVDA`: 08-26 프린트 이틀 전에 **08-24 만기(D0)** 를 집어 ±1.3% 를 냈다.
        같은 프린트를 span 하는 08-28 체인은 **±6.13%**. **4.7배 과소이며, 그 위에
        "안일(연료적음)" 이라는 확신에 찬 «반대» 형용사가 붙었다.**
      · 2026-09-03 `NVDA`: 정산 창이 09-10 인데 **09-04 만기(D1)** 로 ±2.2% 를 냈다.
        직독한 09-11 체인은 ±3.97%, 09-18 은 ±5.39%.
    캘린더가 굴러가면 저절로 «나아 보여서» 6회 이상 재발했다(`D353` 계열 — 고쳐진 게 아니라 지나간 것).
    ⇒ **span 하는 만기가 없으면 값을 내지 않는다.** 틀린 숫자보다 빈칸이 싸다(P4).
    """
    if not exps or not spot:
        return {}
    try:
        today = datetime.now().date()
        if through:
            tgt = datetime.strptime(through, "%Y-%m-%d").date()
            span = [e for e in exps
                    if datetime.strptime(e, "%Y-%m-%d").date() >= tgt]
            if not span:
                return {"im_note": f"span 만기 없음 (through={through}) — 예상변동 미산출",
                        "im_through": through}
            near = span[0]
        else:
            near = exps[0]
        # 날짜끼리 뺀다 — datetime.now() 로 빼면 당일 만기가 D-1 로 찍힌다(실측 버그).
        dte = (datetime.strptime(near, "%Y-%m-%d").date() - today).days
        ch = t.option_chain(near)
        c, p = ch.calls, ch.puts
        if not len(c) or not len(p):
            return {}
        ca = c.iloc[(c["strike"] - spot).abs().argmin()]
        pa = p.iloc[(p["strike"] - spot).abs().argmin()]
        prem = float(ca["lastPrice"]) + float(pa["lastPrice"])
        if prem <= 0:
            return {}
        out = {"im_expiry": near, "im_dte": dte,
               "implied_move_pct": round(prem / spot * 100, 1)}
        if through:
            out["im_through"] = through
        elif dte <= 1:
            # `through` 없이 D0/D1 만기를 집었다 — 오늘·내일 밖의 어떤 창도 가격하지 못한다.
            out["im_note"] = (f"만기 D{dte} — 이 값은 «오늘~내일» 의 변동폭이다. "
                              f"이벤트 창을 재려면 --through <YYYY-MM-DD> 를 줘라 (D315)")
        return out
    except Exception:
        return {}


def _options_pos(tk: str, spot: float | None, through: str | None = None) -> dict:
    """⑥ 옵션 — ~30DTE 만기 P/C OI비율 + IV스큐(OTM풋 IV − OTM콜 IV) + 최근월 예상변동폭."""
    try:
        t = yf.Ticker(tk)
        exps = t.options or []
        if not exps:
            return {"pc_oi": None, "iv_skew": None, "note": "no options"}
        best, bestd = None, 1e9
        for e in exps:
            d = (datetime.strptime(e, "%Y-%m-%d") - datetime.now()).days
            if d >= 7 and abs(d - 30) < bestd:
                bestd, best = abs(d - 30), e
        best = best or exps[-1]
        ch = t.option_chain(best)
        c, p = ch.calls, ch.puts
        coi, poi = float(c["openInterest"].sum()), float(p["openInterest"].sum())
        pc_oi = round(poi / coi, 2) if coi else None
        skew = None
        if spot:
            def cln(df):
                v = df["impliedVolatility"]
                return df[(v > 0.01) & (v < 5.0)]            # 쓰레기 IV(1e-5, 비정상) 제거
            otm_p = cln(p[p["strike"] < spot * 0.95])
            otm_c = cln(c[c["strike"] > spot * 1.05])
            if len(otm_p) and len(otm_c):
                skew = round((otm_p["impliedVolatility"].median() - otm_c["impliedVolatility"].median()) * 100, 1)
        return {"expiry": best, "pc_oi": pc_oi, "iv_skew": skew,
                **_implied_move(t, exps, spot, through)}
    except Exception as e:
        return {"pc_oi": None, "iv_skew": None, "error": str(e)[:40]}


def positioning(tk: str, spot: float | None, through: str | None = None) -> dict:
    """⑤+⑥ 합성 포지셔닝 읽기 (양방향 — 크라우딩/공포). 방향성 4축과 별개 차원.

    `through` = 이 날짜를 span 하는 만기로 예상변동을 잰다 (D315). 없으면 최근접 만기이며,
    그게 D0/D1 이면 `im_note` 로 «오늘~내일 값» 임을 밝힌다.
    """
    si = _short_interest(tk)
    op = _options_pos(tk, spot, through)
    crowded_short = si.get("crowded")
    dtc = si.get("days_to_cover")
    fear = (op.get("pc_oi") or 0) >= 1.2 or (op.get("iv_skew") or 0) >= 5
    complacent = (op.get("pc_oi") is not None and op["pc_oi"] <= 0.6) and not crowded_short
    fuel = ""
    if crowded_short:
        fuel = " 지속" if (dtc and dtc >= 5) else " 빠른언와인드" if (dtc and dtc < 3) else ""
    if crowded_short and fear:
        read = f"최대비관(스퀴즈연료{fuel})"
    elif crowded_short:
        read = f"크라우디드숏(턴 시 연료{fuel})"
    elif complacent:
        read = "안일(연료적음)"
    elif fear:
        read = "헤지/공포"
    else:
        read = "중립"
    return {"short": si, "options": op, "read": read}
