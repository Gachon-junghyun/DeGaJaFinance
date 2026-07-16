from __future__ import annotations

import numpy as np
import pandas as pd

from ._utils import _fmt_price, _norm


def generate_metadata(df: pd.DataFrame) -> str:
    """
    차트 구간의 시장 상태를 텍스트로 자동 생성.
    LLM 프롬프트에 차트 텍스트와 함께 붙여 문맥을 제공한다.

    항목: MA 상태 / 볼린저 수축·확장 / 거래량 추세 / 모멘텀 / RSI / 캔들힌트
    """
    _df   = _norm(df)
    close = _df["close"]
    vol   = _df["volume"] if "volume" in _df.columns else None
    lines: list[str] = []
    last  = float(close.iloc[-1])

    # ── MA 상태 ──────────────────────────────────────────────────────────────
    ma_parts: list[str] = []
    for w in [5, 20, 60, 120]:
        if len(close) >= w:
            ma_val = float(close.rolling(w).mean().iloc[-1])
            state  = "위" if last > ma_val else "아래"
            ma_parts.append(f"MA{w} {state}({_fmt_price(ma_val)})")
    if ma_parts:
        lines.append("이평선: " + " | ".join(ma_parts))

    # ── 볼린저 밴드 수축/확장 ───────────────────────────────────────────────
    if len(close) >= 20:
        mid = close.rolling(20).mean()
        std = close.rolling(20).std()
        bw      = std * 4 / mid * 100
        bw_now  = float(bw.iloc[-1])
        bw_prev = float(bw.iloc[-10]) if len(bw) > 10 else float(bw.iloc[0])
        bb_dir  = "수축 중 ▼" if bw_now < bw_prev else "확장 중 ▲"
        bb_pos  = ""
        upper = float((mid + std * 2).iloc[-1])
        lower = float((mid - std * 2).iloc[-1])
        if last >= upper * 0.98:
            bb_pos = " / 상단 밴드 접근"
        elif last <= lower * 1.02:
            bb_pos = " / 하단 밴드 접근"
        lines.append(f"볼린저: 밴드폭 {bw_now:.1f}% ({bb_dir}){bb_pos}")

    # ── 거래량 추세 ──────────────────────────────────────────────────────────
    if vol is not None and len(vol) >= 10:
        v_rec  = float(vol.iloc[-5:].mean())
        v_prev = float(vol.iloc[-10:-5].mean())
        ratio  = v_rec / (v_prev + 1e-10)
        if   ratio >= 1.5: vstatus = f"급증 ({ratio:.1f}x) ▲▲"
        elif ratio >= 1.1: vstatus = f"증가 ({ratio:.1f}x) ▲"
        elif ratio <= 0.5: vstatus = f"급감 ({ratio:.1f}x) ▼▼"
        elif ratio <= 0.9: vstatus = f"감소 ({ratio:.1f}x) ▼"
        else:              vstatus = "보합"
        lines.append(f"거래량: {vstatus}")

    # ── 가격 모멘텀 ──────────────────────────────────────────────────────────
    mom_parts: list[str] = []
    for n, label in [(5, "5일"), (20, "20일")]:
        if len(close) >= n:
            ret = (close.iloc[-1] / close.iloc[-n] - 1) * 100
            mom_parts.append(f"{label} {ret:+.1f}%")
    if mom_parts:
        lines.append("모멘텀: " + " | ".join(mom_parts))

    # ── RSI ──────────────────────────────────────────────────────────────────
    if len(close) >= 15:
        delta = close.diff()
        gain  = delta.clip(lower=0).rolling(14).mean()
        loss  = (-delta.clip(upper=0)).rolling(14).mean()
        rs    = gain / loss.replace(0, np.nan)
        rsi   = float((100 - 100 / (1 + rs)).iloc[-1])
        if not np.isnan(rsi):
            rsi_label = "과매수 ⚠" if rsi >= 70 else ("과매도 ⚠" if rsi <= 30 else "중립")
            lines.append(f"RSI(14): {rsi:.1f} ({rsi_label})")

    # ── 최근 캔들 패턴 힌트 ──────────────────────────────────────────────────
    if len(_df) >= 3 and all(c in _df.columns for c in ["open", "high", "low", "close"]):
        hints: list[str] = []
        c0    = _df.iloc[-1]
        c1    = _df.iloc[-2]
        body0 = abs(float(c0["close"]) - float(c0["open"]))
        wick0 = float(c0["high"]) - float(c0["low"])
        if wick0 > 0 and body0 / wick0 < 0.2:
            hints.append("도지(우유부단)")
        if float(c0["close"]) < float(c0["open"]) and float(c1["close"]) > float(c1["open"]):
            hints.append("양→음 전환")
        if float(c0["close"]) > float(c0["open"]) and float(c1["close"]) < float(c1["open"]):
            hints.append("음→양 전환")
        if hints:
            lines.append("캔들힌트: " + " / ".join(hints))

    return "\n".join(lines) if lines else "(데이터 부족 — 메타데이터 생성 불가)"


def generate_chart_read(df: pd.DataFrame) -> str:
    """결정론적 차트 *구조* 읽기 (generate_metadata 가 '값'이라면 이건 '판정').

    목적: OBV 분배/누적 · 다이버전스 · 칼-vs-베이스 같은 구조 신호를 사람이
    ASCII 로 눈대중하는 의존을 없애고 기계가 매번 동일하게 판정해서 출력한다.
    에이전트 브리프의 ★CHART-STRUCTURE READ 슬롯에 그대로 박는 블록.

    임계값은 함수 상단에 모아 둠 — 튜닝 지점.
    """
    # ── 튜닝 임계값 ──────────────────────────────────────────────────────────
    OBV_WIN, OBV_LB = 20, 10      # 롤링 OBV 윈도우 / 기울기 lookback
    OBV_TH          = 0.15        # |기울기/레인지| 이상이면 누적/분배 판정
    DIV_WIN         = 10          # 다이버전스 비교 윈도우(최근 vs 직전)
    KNIFE_RSI       = 35          # 칼 판정 RSI 상한
    SWING_LB        = 20          # 스윙 저점(스탑) lookback

    _df   = _norm(df)
    close = _df["close"]
    vol   = _df["volume"] if "volume" in _df.columns else None
    n     = len(close)
    if n < 30 or vol is None:
        return "(데이터 부족 — CHART_READ 생성 불가)"
    last = float(close.iloc[-1])

    mas = {w: float(close.rolling(w).mean().iloc[-1]) for w in (5, 20, 60, 120) if n >= w}

    # ── OBV 상태(누적/분배) ──────────────────────────────────────────────────
    signed  = np.sign(close.diff().fillna(0.0)) * vol
    obv     = signed.rolling(OBV_WIN, min_periods=1).sum()
    obv_now = float(obv.iloc[-1])
    obv_ref = float(obv.iloc[-OBV_LB]) if n > OBV_LB else float(obv.iloc[0])
    obv_rng = float(obv.abs().iloc[-SWING_LB:].max()) + 1e-9
    obv_chg = (obv_now - obv_ref) / obv_rng
    obv_state = ("누적(매수압력↑)" if obv_chg > OBV_TH
                 else "분배(매도압력↑)" if obv_chg < -OBV_TH else "중립")

    # ── RSI 시계열 ───────────────────────────────────────────────────────────
    delta = close.diff()
    gain  = delta.clip(lower=0).rolling(14).mean()
    loss  = (-delta.clip(upper=0)).rolling(14).mean()
    rsi_s = 100 - 100 / (1 + gain / loss.replace(0, np.nan))
    rsi   = float(rsi_s.iloc[-1])

    # ── 다이버전스(가격 저점 vs RSI 저점, 최근 vs 직전) ──────────────────────
    div = "없음"
    if n >= DIV_WIN * 2:
        p_rec, p_prv = close.iloc[-DIV_WIN:], close.iloc[-DIV_WIN*2:-DIV_WIN]
        r_rec, r_prv = rsi_s.iloc[-DIV_WIN:], rsi_s.iloc[-DIV_WIN*2:-DIV_WIN]
        if p_rec.min() < p_prv.min() and r_rec.min() > r_prv.min():
            div = "강세(가격 저점↓ · RSI 저점↑)"
        elif p_rec.max() > p_prv.max() and r_rec.max() < r_prv.max():
            div = "약세(가격 고점↑ · RSI 고점↓)"

    # ── MA 정렬 ──────────────────────────────────────────────────────────────
    if all(w in mas for w in (5, 20, 60, 120)):
        order = [mas[5], mas[20], mas[60], mas[120]]
        align = ("강세스택(5>20>60>120)" if order == sorted(order, reverse=True)
                 else "약세스택(5<20<60<120)" if order == sorted(order) else "혼조")
        align += f" · 가격 {sum(1 for w in (5,20,60,120) if last > mas[w])}/4 MA 위"
    else:
        align = "MA 부족"

    # ── 볼린저 레짐 ──────────────────────────────────────────────────────────
    mid, std = close.rolling(20).mean(), close.rolling(20).std()
    bw_s  = std * 4 / mid * 100
    bw    = float(bw_s.iloc[-1])
    bb_reg = "수축(코일링)" if bw < float(bw_s.iloc[-10]) else "확장"
    upper, lower = float((mid + std*2).iloc[-1]), float((mid - std*2).iloc[-1])
    bb_pos = ("상단밴드" if last >= upper*0.98
              else "하단밴드" if last <= lower*1.02 else "중단")

    mom20 = (last / float(close.iloc[-20]) - 1) * 100 if n >= 20 else 0.0
    swing_low = float(close.iloc[-SWING_LB:].min())
    above_mas = sorted(m for m in mas.values() if m > last)
    trigger   = above_mas[0] if above_mas else None

    # ── 턴-판정(룰) ──────────────────────────────────────────────────────────
    below_all = bool(mas) and all(last < m for m in mas.values())
    above_200 = 120 in mas and last > mas[120]
    if (below_all and rsi < KNIFE_RSI and obv_state.startswith("분배")
            and bb_reg == "확장" and mom20 < 0 and not div.startswith("강세")):
        verdict = "FALLING-KNIFE (떨어지는 칼 · 진입 금지)"
    elif (5 in mas and last > mas[5] and 35 <= rsi <= 52
          and obv_state != "누적(매수압력↑)" and not (20 in mas and last > mas[20])):
        verdict = "BASING (바닥 다지기 · 미확인 턴)"
    elif above_200 and 40 <= rsi <= 58 and not below_all:
        verdict = "PULLBACK-TO-SUPPORT (추세 눌림목)"
    elif (20 in mas and last > mas[20] and 60 in mas and last > mas[60]
          and obv_state.startswith("누적") and rsi > 50):
        verdict = "CONFIRMED-TURN (확인된 반전)"
    elif bb_pos == "상단밴드" and rsi > 60:
        verdict = "BREAKOUT (상단 돌파)"
    else:
        verdict = "NEUTRAL/CHOP (방향 불명확)"

    trig_s = _fmt_price(trigger) if trigger else "—(전 MA 위)"
    return "\n".join([
        f"OBV: {obv_state} (20d기울기 {obv_chg:+.0%})",
        f"다이버전스: {div}",
        f"MA정렬: {align}",
        f"볼린저: {bb_reg} {bw:.1f}% · {bb_pos}",
        f"RSI: {rsi:.1f} · 모멘텀20d {mom20:+.1f}%",
        f"턴-판정: {verdict}",
        f"트리거(점화): close>{trig_s} + OBV→누적 / 스탑(스윙저점): {_fmt_price(swing_low)}",
    ])
