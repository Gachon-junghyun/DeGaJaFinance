# -*- coding: utf-8 -*-
"""exposure_rule — 대칭 노출 규칙(정상/방어/복귀/과열) + 일별 노출·수익분해 적립.

왜 있나 (2026-07-31 실측)
------------------------
데스크는 폭락을 **현금 58%** 로 통과해 KOSPI 대비 **+16.77pp** 를 만들고, 그다음 날
**같은 현금 58%** 로 +17% 반등을 놓쳐 하루에 **−12.5pp** 를 반납했다. 같은 변수, 반대 방향.
같은 주의 수익분해(`HARNESS_UPGRADE_20260731.md §1-c`): 대비 **+16.86pp 중 약 14pp가 현금비중**,
**종목선택 초과는 +2.54pp(삼성물산 단독 +0.89pp)** = n=11·창 1개 ⇒ **0과 구분 불가(C4)**.

⇒ 이 구조가 실제로 하는 일은 **베타 관리**다. 그리고 그 변수는 하루 1관측씩 쌓여
**한 달이면 n=20** — 이 리포에서 **유의성이 산술적으로 나올 수 있는 유일한 영역**이다
(종목선택은 연간 독립관측 10~20개).

결함 F1 이 "비대칭 게이트"였다: **위험 줄이기 트리거만 있고 되돌리기 트리거가 없다.**
그래서 이 파일의 본체는 **복귀 규칙**이다.

★ 복귀는 바닥을 예측하지 않는다
--------------------------------
"돌아섰다는 **증거**가 인쇄되면 되돌린다"만 한다 — 20일 저점 대비 회복률 ∧ 거래량 ∧ 상승마감.
목적은 예측 성공이 아니라 **예측 실패를 전손이 아니라 지연으로 바꾸는 것**이다.
07-31 같은 날이 −12.5pp 전손이 아니라 **수 pp 지각**이 된다. 지각의 크기는 `propose` 가 실측한다.

⚠ 밴드 숫자는 이 파일이 정하지 않는다 (사람 결정, CLAUDE.md P5)
---------------------------------------------------------------
정상/방어/복귀/과열의 목표 투자비중(%)과 발화 임계값은 **위험선호이지 분석이 아니다.**
`data/exposure_bands.json` 이 없으면 이 도구는 **판정을 내리지 않고 `밴드미설정` + 🚨** 로 적립한다.
(조용한 폴백 금지 — F4 를 9일간 숨긴 것이 조용한 실패였다.)
숫자를 정하는 데 필요한 실측표는 `propose` 가 낸다: 임계값 후보마다 **발화 횟수 · 바닥 대비 지각일수 ·
그 사이 벤치 수익**을 계산해 준다. 기계가 재고, 사람이 고른다.

⚠ 벤치는 `069500.KS`(KODEX 200) — `^KS11` 을 쓰지 않는다
---------------------------------------------------------
`^KS11` 은 봉이 통째로 빠지는 이력이 3회 재현됐다(M49·M194: 07-23·07-27·07-30 무봉).
`069500.KS` 는 같은 날 봉이 있고 뉴스보도 KOSPI 등락과 0.14pp 로 맞았다.

⚠ 장중 실행 = 미정착 봉 (D74)
------------------------------
KR 정규장(09:00~15:30 KST) 중에 yfinance 마지막 행은 **살아 움직이는 봉**이다.
실측 2026-07-31 10:2x: 같은 분에 두 번 호출해 `103,800 → 103,625` 로 달라졌다.
그래서 모든 산출에 `bar_status = live|settled` 를 박고, 원장은 **날짜 키로 upsert** 한다 —
장중에 적립한 행은 종가 후 다시 돌리면 정착값으로 덮인다. 지우고 다시 쓰지 않으면 장중값이 화석이 된다.

일별 수익분해 (§1-c 를 매일 자동화)
-----------------------------------
    총초과 = NAV당일 − 벤치당일
           = **현금기여** (w−1)×벤치당일   +   **선택기여** w×(슬리브당일 − 벤치당일)
w = 투자비중(0~1). 항등식이라 두 항의 합은 정의상 총초과와 같다 — 반올림 외 잔차는 0이어야 한다.
슬리브당일은 (a) 보유종목 당일등락의 비중가중, 없으면 (b) NAV당일/w 로 역산(무거래 가정, `src` 에 표기).

CLI
---
  python -X utf8 scripts/exposure_rule.py state                 # 오늘 판정(적립 안 함)
  python -X utf8 scripts/exposure_rule.py log                   # 오늘 1행 적립(upsert)
  python -X utf8 scripts/exposure_rule.py log --nav 954.18 --invested 53.3
  python -X utf8 scripts/exposure_rule.py log --from-timefolio  # CDP 브라우저에서 NAV·비중 직접 읽기
  python -X utf8 scripts/exposure_rule.py target --json         # 현금·투자 목표비중(F5 의 현금 SSOT)
  python -X utf8 scripts/exposure_rule.py propose --days 120    # 밴드 숫자 정하기용 실측표
  python -X utf8 scripts/exposure_rule.py show [--tail 30]      # 적립 원장 + 누적 분해

P4: 판단은 하지 않는다. 관측값(벤치·NAV·비중)과 **사람이 정한 규칙의 기계적 적용**만 낸다.
P1: 벤치 시세는 yfinance 1곳. 콘테스트 계좌는 `module_timefolio` 1곳. 재구현 0.
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import json
import os
import sys

import _repo_path  # noqa: F401  (sys.path 부트스트랩)

BENCH = "069500.KS"          # M49/M194 — ^KS11 은 봉 누락 이력 3회
BANDS = os.path.join("data", "exposure_bands.json")
LEDGER = os.path.join("out", "exposure", "ledger.csv")

STATES = ("정상", "방어", "복귀", "과열", "밴드미설정")

FIELDS = [
    "date", "bar_status", "state", "prev_state",
    "bench_close", "bench_ret_d", "bench_dd20", "bench_off_low20", "bench_volmult20",
    "nav", "nav_ret_d", "invested_pct", "cash_pct",
    "target_invested_pct", "band_gap_pp",
    "sleeve_ret_d", "sleeve_ret_holdings", "timing_gap_pp", "sleeve_src",
    "excess_total_pp", "cash_contrib_pp", "select_contrib_pp",
    "alarms", "note",
]


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ── 밴드(사람 결정) ──────────────────────────────────────────────────────
def load_bands() -> dict | None:
    if not os.path.exists(BANDS):
        return None
    with open(BANDS, encoding="utf-8") as f:
        return json.load(f)


def arming_status() -> str:
    """F8 — arming 상태를 **양방향으로** 보고한다. 값은 출력하지 않고 상태만 낸다.

    ⚠ 실측 2026-07-31: 인수인계 문서(F8)는 *".env 에 `TIMEFOLIO_EXECUTE` 키가 아예 없다"* 라고
    적었지만 **틀렸다 — 키가 있고 값이 `1`(장전)이다.** `place_order` 는 `os.environ` 을 직접 보고
    `Timefolio.attach()` 가 로그인 과정에서 `.env` 를 주입하므로, 지금 `--execute` 를 붙이면
    **실제로 제출된다.** 07-31 B안 집행 때 켠 뒤 꺼지지 않은 것으로 보인다.
    미설정도 경보(규칙이 집행으로 못 감)이고, 설정도 경보(실탄)다 — 어느 쪽도 침묵하지 않는다.
    """
    try:
        from module_webctl._env import load_dotenv
        load_dotenv()
    except Exception:                                  # noqa: BLE001
        pass
    v = os.environ.get("TIMEFOLIO_EXECUTE", "").strip()
    if v == "":
        return "🚨arming미설정(--execute 가 조용히 드라이런 — 규칙이 집행에 닿지 못한다)"
    if v == "1":
        return "🚨🚨ARMED(TIMEFOLIO_EXECUTE=1 — --execute 를 붙이면 실제 제출된다. 사람 확인 필요)"
    return f"⚠arming값 비정상(len={len(v)}) — 1 도 아니고 빈 값도 아니다"


def bands_missing_banner() -> str:
    return (
        "🚨 밴드 미설정 — `data/exposure_bands.json` 이 없다.\n"
        "   이 도구는 목표 비중·발화 임계값을 **스스로 정하지 않는다**(위험선호는 사람 몫, P5).\n"
        "   `propose` 로 실측표를 뽑아 사람이 숫자를 박기 전까지 판정은 `밴드미설정` 으로 적립된다.\n"
        "   ⚠ 미설정 상태 자체가 경보다 — 규칙 없는 노출은 '규칙대로 굴렸다'가 성립하지 않는다."
    )


# ── 벤치 ─────────────────────────────────────────────────────────────────
def kr_session_now() -> bool:
    """지금이 KR 정규장(09:00~15:30 KST, 평일)인가. 로컬 시계가 KST 라고 가정한다."""
    now = _dt.datetime.now()
    if now.weekday() >= 5:
        return False
    return _dt.time(9, 0) <= now.time() <= _dt.time(15, 30)


def session_elapsed() -> float:
    """정규장 경과 비율(0~1). 장 전 0, 장 후 1."""
    now = _dt.datetime.now()
    mins = now.hour * 60 + now.minute - (9 * 60)
    return max(0.0, min(1.0, mins / 390.0))          # 09:00~15:30 = 390분


def live_bench_kis() -> dict | None:
    """KIS 실시간 현재가·누적거래량. yfinance 의 장중 봉은 **존재하지만 지연된다**.

    실측 2026-07-31 10:3x: yfinance 103,625 / 10,485,436주  vs  KIS 102,545 / 12,094,041주
    — 가격 1.05% · 거래량 1.6M 괴리. 장중 판정은 KIS 를 1차로 쓴다.
    """
    try:
        from module_webctl._env import load_dotenv    # 시크릿 로딩의 기존 구현 재사용(P1)
        load_dotenv()
        from module_KIS import fetch_quote
        q = fetch_quote("069500")
        d = q if isinstance(q, dict) else vars(q)
        px = d.get("stck_prpr") or d.get("price") or d.get("last") or d.get("현재가")
        vol = d.get("acml_vol") or d.get("volume") or d.get("거래량")
        return {"close": float(str(px).replace(",", "")),
                "volume": float(str(vol).replace(",", ""))}
    except Exception as e:                             # noqa: BLE001
        print(f"[warn] KIS 실시간 벤치 실패({type(e).__name__}: {e}) → yfinance 지연 봉 사용",
              file=sys.stderr)
        return None


def bench_frame(days: int = 400):
    import yfinance as yf

    df = yf.Ticker(BENCH).history(period=f"{max(days, 60)}d", auto_adjust=False)
    if df.empty:
        raise SystemExit(f"[err] {BENCH} 봉 없음 — 네트워크/티커 확인")
    df = df[["Close", "Volume"]].dropna()
    df.index = [d.date() for d in df.index]
    return df


def bench_metrics(df, i: int | None = None, *, live: bool = False,
                  live_px: dict | None = None) -> dict:
    """i 번째 행(기본 마지막) 기준 벤치 파생값. 창은 그 시점까지만 본다(선행참조 금지).

    ★ 장중(live)의 거래량 처리 — 이 도구가 자기 자신에게서 F1 을 재현하지 않기 위한 장치.
    미정착 봉의 누적거래량은 정의상 부분치라 `vol/20일평균` 이 **아래로 편향**된다(D74 의 산술).
    실측 2026-07-31 10:2x: 원시 배수 **0.47×** — 즉 그대로 쓰면 **가격 조건은 이미 충족인데
    거래량 조건이 구조적으로 거짓**이 되어, 방어(가격만으로 발화)는 되고 복귀는 안 되는
    **비대칭 게이트가 도구 안에서 되살아난다.**

    그래서: 경과비율로 **정규화한 투영치**를 쓰되 그 사실을 라벨로 달고,
    장 초반(경과 < `min_frac`)에는 투영 자체가 노이즈라 **거짓이 아니라 '판정불가'** 로 둔다(C3).
    """
    n = len(df)
    i = (n - 1) if i is None else i
    win = df.iloc[max(0, i - 19): i + 1]
    close = float(df["Close"].iloc[i])
    prev = float(df["Close"].iloc[i - 1]) if i >= 1 else close
    vol = float(df["Volume"].iloc[i])
    if live and live_px:                      # KIS 실시간이 있으면 가격·거래량 모두 교체
        close, vol = live_px["close"], live_px["volume"]
    hi20 = float(win["Close"].max())
    lo20 = float(win["Close"].min())
    volavg = float(win["Volume"].mean()) or 1.0
    ma20 = float(win["Close"].mean())

    raw_mult = vol / volavg
    if live:
        frac = session_elapsed()
        if frac < 0.15:
            mult, vstat = raw_mult, f"판정불가(경과 {frac:.0%} — 투영이 노이즈)"
        else:
            mult, vstat = raw_mult / frac, f"투영(경과 {frac:.0%}, 원시 {raw_mult:.2f}×)"
    else:
        mult, vstat = raw_mult, "정착"

    return {
        "date": df.index[i],
        "close": close,
        "ret_d": (close / prev - 1) * 100 if prev else 0.0,
        "dd20": (close / hi20 - 1) * 100 if hi20 else 0.0,        # 20일 고점 대비 (음수)
        "off_low20": (close / lo20 - 1) * 100 if lo20 else 0.0,   # 20일 저점 대비 회복률 (양수)
        "volmult20": mult,
        "volmult20_raw": raw_mult,
        "vol_status": vstat,
        "ma20_dev": (close / ma20 - 1) * 100 if ma20 else 0.0,
    }


# ── 상태 판정 (사람이 정한 임계값의 기계적 적용) ─────────────────────────
def classify(m: dict, prev_state: str, b: dict | None) -> tuple[str, list[str]]:
    """(state, 발화근거). b=None 이면 밴드미설정."""
    if not b:
        return "밴드미설정", ["밴드 파일 없음"]

    d = b.get("defend", {})
    r = b.get("recover", {})
    o = b.get("overheat", {})
    why: list[str] = []

    defend_hit = False
    if "drawdown_from_20d_high_pct" in d and m["dd20"] <= -abs(d["drawdown_from_20d_high_pct"]):
        defend_hit = True
        why.append(f"20일고점 대비 {m['dd20']:+.1f}% ≤ −{abs(d['drawdown_from_20d_high_pct'])}")
    if "one_day_ret_pct" in d and m["ret_d"] <= -abs(d["one_day_ret_pct"]):
        defend_hit = True
        why.append(f"당일 {m['ret_d']:+.1f}% ≤ −{abs(d['one_day_ret_pct'])}")

    # ★ 복귀 — 방어 상태에서만 발화한다. 바닥 예측이 아니라 '돌아섰다는 증거'.
    recover_hit = False
    if prev_state in ("방어", "복귀"):
        legs, ok = [], True
        if "off_20d_low_pct" in r:
            good = m["off_low20"] >= abs(r["off_20d_low_pct"])
            ok &= good
            legs.append(f"20일저점 대비 {m['off_low20']:+.1f}% "
                        f"{'≥' if good else '<'} {abs(r['off_20d_low_pct'])}")
        if "vol_mult_20d" in r:
            if m.get("vol_status", "").startswith("판정불가"):
                ok = False
                legs.append(f"거래량 {m['vol_status']} ⇒ ★복귀 판정보류(거짓 아님, C3)")
                why += legs
                return ("복귀판정보류:" + prev_state), why
            good = m["volmult20"] >= r["vol_mult_20d"]
            ok &= good
            legs.append(f"거래량 {m['volmult20']:.2f}× [{m['vol_status']}] "
                        f"{'≥' if good else '<'} {r['vol_mult_20d']}")
        if r.get("require_up_day", True):
            good = m["ret_d"] > 0
            ok &= good
            legs.append(f"당일 {m['ret_d']:+.1f}% {'>' if good else '≤'} 0")
        recover_hit = ok
        why += legs

    if recover_hit:
        return "복귀", why
    if defend_hit:
        return "방어", why
    if prev_state == "복귀":
        # 복귀는 통과 상태 — 조건이 유지되면 복귀, 깨지면 정상으로 복원
        return "정상", why + ["복귀 조건 미유지 → 정상 복원"]
    if "above_20d_ma_pct" in o and m["ma20_dev"] >= abs(o["above_20d_ma_pct"]):
        return "과열", why + [f"20일MA 대비 {m['ma20_dev']:+.1f}% ≥ {abs(o['above_20d_ma_pct'])}"]
    return "정상", why or ["발화 조건 없음"]


def apply_min_hold(new: str, prev: str, held: int, b: dict | None) -> tuple[str, str]:
    """최소 유지일수 게이트 — 상태가 하루 만에 뒤집혀 회전율 규정을 깨는 것을 막는다.

    ★ 실측 2026-07-31 (069500.KS 120세션, '공격' 밴드):
      최소유지 0 → 전이 **36회** · 노출규칙만의 회전 **1040pp = 주당 43.3pp**
      최소유지 3 → 전이 **19회** · 회전 **510pp = 주당 21.2pp**  (절반)
      최소유지 5 → 전이 15회지만 **복귀 발화가 0회** — 규칙의 존재 이유가 사라진다.
    콘테스트의 그 주 회전율이 26.9%, 누적 위반 1건이다. **게이트 없이는 노출 규칙 하나가
    데스크 전체 회전율의 1.6배를 혼자 쓴다** — 종목 매매를 하기도 전에.

    ⚠ 그리고 이 게이트는 **이 프로젝트를 만든 사건에 비용이 없다**: 07-30 시점 상태가 `방어` 이고
    그 상태가 오래됐으므로, 최소유지 0·2·3·5 **전부** 07-31 을 `복귀` 로 판정한다(실측).
    즉 잃는 것은 휩소뿐이다.
    """
    m = (b or {}).get("min_hold_sessions", 0)
    if not m or new == prev or held >= m:
        return new, ""
    return prev, f"⚠전이 보류({prev}→{new}) — 최소유지 {held}/{m}세션"


def target_for(state: str, b: dict | None) -> float | None:
    """`복귀판정보류:방어` 처럼 보류 접두가 붙으면 **직전 상태의 타깃을 유지**한다.
    판정불가를 '정상 복귀'로 오독하지 않기 위해서다 — 모르면 움직이지 않는다."""
    if not b:
        return None
    if state.startswith("복귀판정보류:"):
        state = state.split(":", 1)[1]
    return b.get("targets", {}).get(state)


# ── 원장 ─────────────────────────────────────────────────────────────────
def load_ledger() -> list[dict]:
    if not os.path.exists(LEDGER):
        return []
    with open(LEDGER, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_ledger(rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    rows = sorted(rows, key=lambda r: r["date"])
    with open(LEDGER, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


def upsert(row: dict) -> list[dict]:
    """날짜 키로 덮어쓴다 — 장중(live) 적립분이 종가 재실행 때 정착값으로 교체되도록."""
    rows = [r for r in load_ledger() if r["date"] != row["date"]]
    rows.append(row)
    write_ledger(rows)
    return rows


def prev_state_from_ledger(today: str) -> str:
    rows = [r for r in load_ledger() if r["date"] < today and r.get("state")]
    return rows[-1]["state"] if rows else "정상"


def held_sessions(today: str) -> int:
    """직전 상태가 **연속 몇 세션** 유지됐나 — 최소유지 게이트의 입력."""
    rows = [r for r in load_ledger() if r["date"] < today and r.get("state")]
    if not rows:
        return 99                       # 이력 없음 = 게이트 걸지 않음(냉시동)
    last, k = rows[-1]["state"], 0
    for r in reversed(rows):
        if r["state"] != last:
            break
        k += 1
    return k


# ── 콘테스트 계좌 ────────────────────────────────────────────────────────
def read_contest(from_timefolio: bool) -> dict:
    """NAV·당일수익률·보유비중. 실패는 조용히 넘기지 않고 alarms 로 올린다."""
    out = {"nav": None, "nav_ret_d": None, "invested_pct": None,
           "sleeve_ret_d": None, "sleeve_src": "", "alarms": []}
    if not from_timefolio:
        return out
    try:
        from module_timefolio import Timefolio
        tf = Timefolio.attach()
        acc = tf.read_account()
        hs = tf.read_holdings()
        tf.close()
    except Exception as e:                              # noqa: BLE001
        out["alarms"].append(f"🚨timefolio조회실패:{type(e).__name__}")
        return out
    out["nav"] = acc.nav
    out["nav_ret_d"] = acc.ret_pct
    if not hs:
        out["alarms"].append("🚨보유0건(파서회귀 의심 — 스크린샷 대조 필요)")
        return out
    out["invested_pct"] = round(sum(h.weight for h in hs), 2)
    day = [(h.weight, h.day_pct) for h in hs if getattr(h, "day_pct", None) is not None]
    wsum = sum(w for w, _ in day)
    if wsum > 0:
        out["sleeve_ret_d"] = round(sum(w * d for w, d in day) / wsum, 3)
        out["sleeve_src"] = "holdings(비중가중)"
    return out


# ── 명령 ─────────────────────────────────────────────────────────────────
def build_row(args, b: dict | None) -> dict:
    df = bench_frame()
    live = kr_session_now() and df.index[-1] == _dt.date.today()
    lpx = live_bench_kis() if (live and not args.no_live_bench) else None
    m = bench_metrics(df, live=live, live_px=lpx)
    today = m["date"].isoformat()
    prev = prev_state_from_ledger(today)
    raw, why = classify(m, prev, b)
    state, hold_note = apply_min_hold(raw, prev, held_sessions(today), b)
    if hold_note:
        why = [hold_note] + why
    tgt = target_for(state, b)

    c = read_contest(args.from_timefolio)
    if args.nav is not None:
        c["nav"] = args.nav
    if args.nav_ret is not None:
        c["nav_ret_d"] = args.nav_ret
    if args.invested is not None:
        c["invested_pct"] = args.invested
    if args.sleeve_ret is not None:
        c["sleeve_ret_d"], c["sleeve_src"] = args.sleeve_ret, "인자"

    alarms = list(c["alarms"])
    if b is None:
        alarms.append("🚨밴드미설정")
    alarms.append(arming_status())
    if live:
        alarms.append(f"⚠미정착봉(장중·{'KIS실시간' if lpx else 'yfinance지연'})")
    if state.startswith("복귀판정보류"):
        alarms.append("🚨복귀판정보류(거래량 미정착) — 종가 후 재실행 필수")
    if c["invested_pct"] is None:
        alarms.append("🚨투자비중미상(계좌조회 없음)")

    # ── 수익분해 ────────────────────────────────────────────────────────
    # 항등식으로 **닫는다**: 총초과 = 현금기여 + 선택기여, 선택기여는 잔차로 정의.
    # 그래야 두 항의 합이 언제나 총초과와 같고, "합이 안 맞는데 그냥 출력"이 불가능해진다.
    #
    # ⚠ 실측 2026-07-31: 보유 당일등락의 비중가중 슬리브(**12.44%**)로 선택기여를 직접 계산하면
    #    합이 총초과와 **4.99pp** 어긋났다. 원인은 오류가 아니라 **그날 매매**다 — 그날 10:2x 에
    #    5종목을 신규/증량했고, 그 이름들의 "당일%" 는 **보유하지도 않은 시간대의 상승분까지** 담는다.
    #    그래서 두 슬리브 추정치를 **둘 다** 남기고, 그 차이를 `timing_gap_pp`(매매 타이밍 흔적)로
    #    따로 잰다. 무거래일에는 0 에 수렴해야 한다 — 수렴하지 않으면 그게 파서 결함의 신호다.
    w = (c["invested_pct"] / 100.0) if c["invested_pct"] is not None else None
    sleeve_h, src = c["sleeve_ret_d"], c["sleeve_src"]      # 보유 비중가중(교차확인)
    sleeve_i = None                                          # NAV 역산(분해의 기준)
    if w not in (None, 0) and c["nav_ret_d"] is not None:
        sleeve_i = round(c["nav_ret_d"] / w, 3)

    cash_c = sel_c = tot = tgap = None
    if w is not None and c["nav_ret_d"] is not None:
        tot = round(c["nav_ret_d"] - m["ret_d"], 3)
        cash_c = round((w - 1) * m["ret_d"], 3)
        sel_c = round(tot - cash_c, 3)                       # 정의상 잔차 0
        if sleeve_h is not None and sleeve_i is not None:
            tgap = round(w * (sleeve_h - sleeve_i), 3)
            if abs(tgap) > 1.0:
                alarms.append(f"⚠슬리브추정 불일치 {tgap:+.2f}pp(당일 매매 또는 파서결함)")
    sleeve, src = (sleeve_i, (src + " / NAV역산 기준") if src else "NAV/투자비중 역산")

    gap = (round(c["invested_pct"] - tgt, 2)
           if (tgt is not None and c["invested_pct"] is not None) else "")
    if isinstance(gap, float) and abs(gap) > (b or {}).get("gap_alarm_pp", 5.0):
        alarms.append(f"🚨밴드이탈 {gap:+.1f}pp")

    return {
        "date": today,
        "bar_status": "live" if live else "settled",
        "state": state, "prev_state": prev,
        "bench_close": round(m["close"], 2), "bench_ret_d": round(m["ret_d"], 3),
        "bench_dd20": round(m["dd20"], 2), "bench_off_low20": round(m["off_low20"], 2),
        "bench_volmult20": round(m["volmult20"], 3),
        "nav": c["nav"] if c["nav"] is not None else "",
        "nav_ret_d": c["nav_ret_d"] if c["nav_ret_d"] is not None else "",
        "invested_pct": c["invested_pct"] if c["invested_pct"] is not None else "",
        "cash_pct": (round(100 - c["invested_pct"], 2) if c["invested_pct"] is not None else ""),
        "target_invested_pct": tgt if tgt is not None else "",
        "band_gap_pp": gap,
        "sleeve_ret_d": sleeve if sleeve is not None else "",
        "sleeve_ret_holdings": sleeve_h if sleeve_h is not None else "",
        "timing_gap_pp": tgap if tgap is not None else "",
        "sleeve_src": src,
        "excess_total_pp": tot if tot is not None else "",
        "cash_contrib_pp": cash_c if cash_c is not None else "",
        "select_contrib_pp": sel_c if sel_c is not None else "",
        "alarms": " ".join(alarms),
        "note": " / ".join(why)[:300],
    }


def render(row: dict, b: dict | None) -> None:
    print(f"# EXPOSURE RULE — {row['date']} ({row['bar_status']})  벤치 {BENCH}")
    if b is None:
        print(bands_missing_banner())
    print()
    print(f"  벤치 종가 {row['bench_close']} · 당일 {row['bench_ret_d']:>+7}% · "
          f"20일고점대비 {row['bench_dd20']:>+6}% · 20일저점대비 {row['bench_off_low20']:>+6}% · "
          f"거래량 {row['bench_volmult20']}×")
    print(f"  규칙상태 **{row['state']}** (직전 {row['prev_state']})  근거: {row['note']}")
    if row["target_invested_pct"] != "":
        print(f"  목표 투자비중 {row['target_invested_pct']}% · 현재 {row['invested_pct']}% "
              f"· 괴리 {row['band_gap_pp']}pp")
    else:
        print("  목표 투자비중 — (밴드 미설정)")
    if row["excess_total_pp"] != "":
        print()
        print("  ── 일별 수익분해 (총초과 = 현금기여 + 선택기여, 항등식) ──")
        print(f"   NAV당일 {row['nav_ret_d']:>+8}%  벤치당일 {row['bench_ret_d']:>+8}%  "
              f"⇒ 총초과 {row['excess_total_pp']:>+8}pp")
        print(f"   현금기여 (w−1)×벤치  = {row['cash_contrib_pp']:>+8}pp   ← 베타 결정")
        print(f"   선택기여 (잔차)      = {row['select_contrib_pp']:>+8}pp   ← 종목 결정")
        print(f"   [슬리브 NAV역산 {row['sleeve_ret_d']}% · 보유가중 "
              f"{row['sleeve_ret_holdings'] or '—'}% · 타이밍갭 {row['timing_gap_pp'] or '—'}pp]")
    else:
        print("\n  ── 수익분해 불가: NAV/투자비중이 없다(계좌조회 실패 또는 인자 미제공) ──")
    if row["alarms"]:
        print(f"\n  경보: {row['alarms']}")


def cmd_state(args) -> int:
    b = load_bands()
    row = build_row(args, b)
    render(row, b)
    print("\n(적립하지 않음 — 원장에 넣으려면 `log`)")
    return 0


def cmd_log(args) -> int:
    b = load_bands()
    row = build_row(args, b)
    rows = upsert(row)
    render(row, b)
    print(f"\n[ok] {LEDGER} 적립 — 총 {len(rows)}행 (오늘 행은 date 키로 upsert)")
    print("  " + ",".join(str(row.get(k, "")) for k in FIELDS))
    return 0


def cmd_target(args) -> int:
    """F5 대응 — 현금을 '명시 타깃'으로 내는 단일 원본.

    `_sync.book_targets()` 는 투자 슬리브 비중만 낸다(책이 42% 투자면 콘테스트도 영원히 42%).
    현금 타깃은 그 함수가 아니라 **여기서** 나온다. F4(SSOT) 결정 후 `_sync` 가 이걸 읽어 쓰면
    투자 슬리브 비중은 규칙이 정한 투자총량으로 **재정규화**된다.
    """
    b = load_bands()
    df = bench_frame()
    live = kr_session_now() and df.index[-1] == _dt.date.today()
    m = bench_metrics(df, live=live, live_px=live_bench_kis() if live else None)
    today = m["date"].isoformat()
    state, why = classify(m, prev_state_from_ledger(today), b)
    tgt = target_for(state, b)
    out = {
        "asof": today,
        "bar_status": "live" if live else "settled",
        "bench": BENCH, "state": state,
        "invested_target_pct": tgt,
        "cash_target_pct": (round(100 - tgt, 2) if tgt is not None else None),
        "why": why,
        "bands_set": b is not None,
        "blocked": None if b is not None else "밴드미설정 — 타깃 없음(사람 결정 대기)",
    }
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        if b is None:
            print(bands_missing_banner())
        print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


def cmd_propose(args) -> int:
    """밴드 숫자를 **사람이** 정하기 위한 실측표. 여기서 아무것도 채택하지 않는다.

    각 (방어 임계, 복귀 임계, 거래량배수) 후보에 대해 과거 창을 훑어:
      · 방어 발화 횟수/일수  · 복귀 발화가 **직전 저점에서 며칠 늦었나**
      · 그 지각 동안 벤치가 얼마나 올랐나(= 놓친 폭)
    를 센다. '얼마나 늦어도 견딜 수 있나'가 곧 밴드 선택이다.
    """
    df = bench_frame(max(args.days + 40, 120))
    dropped = ""
    if kr_session_now() and df.index[-1] == _dt.date.today():
        df = df.iloc[:-1]           # 미정착 봉은 통계에서 뺀다(D74) — 섞으면 표가 오염된다
        dropped = f"  ⚠ 오늘({_dt.date.today()}) 미정착 봉 1개 제외(장중)\n"
    df = df.iloc[-(args.days + 25):]
    n = len(df)
    print(f"# EXPOSURE BANDS — 실측표 (벤치 {BENCH} · {df.index[0]} ~ {df.index[-1]} · {n}봉)")
    print(dropped, end="")
    print("  ⚠ 이 표는 후보의 결과를 보여줄 뿐 아무것도 채택하지 않는다. 숫자는 사람이 고른다(P5).")
    print("  ⚠ 이 표는 상태기계를 무시하고 임계값만 스캔한다(실제 복귀는 방어 상태에서만 발화) "
          "— 발화 횟수는 상한이다.\n")

    metrics = [bench_metrics(df, i) for i in range(n)]

    print("## 1) 방어 임계 후보 — '20일 고점 대비 몇 % 빠지면 줄이나'")
    print(f"{'임계':>6}  {'발화일수':>8} {'발화율':>7}  {'첫 발화':>12}  {'발화 다음날 평균 벤치':>20}")
    for th in args.defend_grid:
        fire = [i for i, m in enumerate(metrics) if m["dd20"] <= -th]
        nxt = [(float(df['Close'].iloc[i + 1]) / m['close'] - 1) * 100
               for i, m in ((i, metrics[i]) for i in fire) if i + 1 < n]
        avg = f"{sum(nxt)/len(nxt):+.2f}%" if nxt else "—"
        first = str(metrics[fire[0]]["date"]) if fire else "—"
        print(f"{th:>5.1f}%  {len(fire):>8d} {len(fire)/n*100:>6.1f}%  {first:>12}  {avg:>20}")

    print("\n## 2) ★ 복귀 임계 후보 — '20일 저점 대비 몇 % 되돌리면 돌아섰다고 보나'")
    print("   지각 = 그 창의 저점일로부터 발화까지 며칠 · 놓친폭 = 저점→발화일 벤치 상승률")
    print(f"{'회복%':>6} {'거래량배수':>9}  {'발화횟수':>8}  {'평균지각(일)':>12}  {'평균놓친폭':>10}  {'발화일 예시':>26}")
    lows: list[int] = []
    for i in range(1, n - 1):                       # 국소 저점(창 20일 최저 = 그날)
        w = df.iloc[max(0, i - 19): i + 1]
        if float(df["Close"].iloc[i]) == float(w["Close"].min()):
            lows.append(i)
    for th in args.recover_grid:
        for vm in args.vol_grid:
            fires, lags, missed = [], [], []
            for i, m in enumerate(metrics):
                if m["off_low20"] >= th and m["volmult20"] >= vm and m["ret_d"] > 0:
                    prior = [j for j in lows if j <= i]
                    if not prior:
                        continue
                    j = prior[-1]
                    if i - j > 20:
                        continue
                    fires.append(m["date"])
                    lags.append(i - j)
                    missed.append((m["close"] / float(df["Close"].iloc[j]) - 1) * 100)
            if not fires:
                print(f"{th:>5.1f}% {vm:>9.2f}  {0:>8d}  {'—':>12}  {'—':>10}  {'발화 없음':>26}")
                continue
            ex = ", ".join(str(d) for d in fires[-2:])
            print(f"{th:>5.1f}% {vm:>9.2f}  {len(fires):>8d}  {sum(lags)/len(lags):>12.1f}  "
                  f"{sum(missed)/len(missed):>+9.2f}%  {ex:>26}")

    print("\n### 2-bis) ★ 어느 다리가 발화를 막는가 — 임계값을 고르기 전에 이걸 먼저 본다")
    print("   (저점 후 20일 이내 봉만 대상. '가격만'과 '거래량만'을 따로 세면 병목이 드러난다)")
    cand = [i for i in range(n) if any(j <= i <= j + 20 for j in lows)]
    print(f"{'회복%':>6} {'거래량배수':>9}  {'가격 통과':>9} {'거래량 통과':>11} {'상승마감 통과':>13} {'전부':>6}")
    for th in args.recover_grid:
        for vm in args.vol_grid:
            pp = sum(1 for i in cand if metrics[i]["off_low20"] >= th)
            vv = sum(1 for i in cand if metrics[i]["volmult20"] >= vm)
            uu = sum(1 for i in cand if metrics[i]["ret_d"] > 0)
            aa = sum(1 for i in cand if metrics[i]["off_low20"] >= th
                     and metrics[i]["volmult20"] >= vm and metrics[i]["ret_d"] > 0)
            print(f"{th:>5.1f}% {vm:>9.2f}  {pp:>9d} {vv:>11d} {uu:>13d} {aa:>6d}   (후보 {len(cand)}봉)")

    print("\n## 3) 이번 사고 구간에 각 후보가 실제로 언제 발화했나 (정착봉만)")
    since = args.since_date or (df.index[-1] - _dt.timedelta(days=10))
    for th in args.recover_grid:
        for vm in args.vol_grid:
            hits = [str(m["date"]) for m in metrics
                    if m["date"] >= since
                    and m["off_low20"] >= th and m["volmult20"] >= vm and m["ret_d"] > 0]
            print(f"  회복 {th:>4.1f}% ∧ 거래량 {vm:.2f}× → {hits or '발화 없음'}")

    # 오늘이 장중이면, 미정착 봉을 **따로** 투영해서 보여준다(통계에는 섞지 않는다).
    full = bench_frame()
    if kr_session_now() and full.index[-1] == _dt.date.today():
        lm = bench_metrics(full, live=True, live_px=live_bench_kis())
        print(f"\n### 3-bis) 오늘 {lm['date']} — **미정착 봉**, 위 통계에서 제외된 행")
        print(f"  종가(잠정) {lm['close']:,.0f} · 당일 {lm['ret_d']:+.2f}% · "
              f"20일저점대비 {lm['off_low20']:+.2f}% · 거래량 {lm['volmult20']:.2f}× [{lm['vol_status']}]")
        for th in args.recover_grid:
            for vm in args.vol_grid:
                ok = lm["off_low20"] >= th and lm["volmult20"] >= vm and lm["ret_d"] > 0
                print(f"  회복 {th:>4.1f}% ∧ 거래량 {vm:.2f}× → "
                      f"{'발화(잠정)' if ok else '미발화'}")
        print("  ⚠ 잠정이다. 종가 후 다시 돌려 정착값으로 덮어라(원장은 date 로 upsert).")
    print("\n⚠ 일봉 규칙은 **종가에만** 발화한다 ⇒ 집행은 그다음 세션. 전손이 아니라 지연이지만 0 은 아니다.")
    print("   장중에 앞당기려면 `--live-bench`(module_KIS 현재가) 를 09:10 태스크에서 쓴다.")
    print("\n## 4) 밴드 파일 서식 — 사람이 채워 `data/exposure_bands.json` 로 저장")
    print(json.dumps({
        "_set_by": "사람이 채운다", "_asof": _dt.date.today().isoformat(),
        "targets": {"정상": "??", "방어": "??", "복귀": "??", "과열": "??"},
        "defend": {"drawdown_from_20d_high_pct": "??", "one_day_ret_pct": "??"},
        "recover": {"off_20d_low_pct": "??", "vol_mult_20d": "??", "require_up_day": True},
        "overheat": {"above_20d_ma_pct": "??"},
        "gap_alarm_pp": 5.0,
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_simulate(args) -> int:
    """설정된 밴드로 과거 정착봉을 **상태기계째** 돌린다 — 임계값 스캔(`propose`)과 다르다.

    `propose` 는 다리별 통과 여부만 세지만, 실제 규칙은 **경로 의존**이다(복귀는 방어에서만 발화).
    "07-28~31 에 이 규칙이 실제로 무엇을 했을 것인가" 는 이 명령으로만 답할 수 있다.
    ⚠ 사후 시뮬레이션이다 — 이미 아는 가격에 규칙을 얹은 것이지 실적이 아니다.
    """
    b = load_bands()
    if not b:
        print(bands_missing_banner())
        return 1
    df = bench_frame()
    if kr_session_now() and df.index[-1] == _dt.date.today():
        df = df.iloc[:-1]                    # 미정착 봉 제외(D74)
    n = len(df)
    start = max(20, n - args.days)
    state = "정상"
    print(f"# EXPOSURE RULE — 상태기계 시뮬레이션 (벤치 {BENCH} · 정착봉 {n - start}개)")
    print("  ⚠ 사후 시뮬레이션. 규칙이 그때 실제로 돌지 않았다 — 경로만 보여준다.\n")
    print(f"{'날짜':11s} {'벤치종가':>10} {'당일%':>7} {'고점대비':>8} {'저점대비':>8} "
          f"{'거래량':>6}  {'상태':6s} {'목표%':>5}  전이")
    prev_t, held, turn, nch = None, 99, 0.0, 0
    for i in range(start, n):
        m = bench_metrics(df, i)
        raw, why = classify(m, state, b)
        new, hn = apply_min_hold(raw, state, held, b)
        held = 0 if new != state else held + 1
        if hn:
            why = [hn] + why
        tgt = target_for(new, b)
        if new != state and prev_t is not None and tgt is not None:
            turn += abs(tgt - prev_t)
            nch += 1
        moved = ""
        if new != state:
            moved = f"★ {state} → {new}"
            if prev_t is not None and tgt is not None:
                moved += f"  (투자 {prev_t}% → {tgt}%)"
            moved += f"   ∵ {'; '.join(why)[:90]}"
        print(f"{str(m['date']):11s} {m['close']:>10,.0f} {m['ret_d']:>+7.2f} "
              f"{m['dd20']:>+8.2f} {m['off_low20']:>+8.2f} {m['volmult20']:>6.2f}  "
              f"{new:6s} {tgt if tgt is not None else '—':>5}  {moved}")
        state, prev_t = new, tgt
    wk = max(1.0, (n - start) / 5.0)
    print(f"\n  마지막 상태 **{state}** · 목표 투자비중 {prev_t}%")
    print(f"  ★ 회전 비용: 상태 전이 {nch}회 · 노출규칙만의 누적 회전 {turn:.0f}pp "
          f"· **주당 {turn/wk:.1f}pp**  (최소유지 {(b or {}).get('min_hold_sessions', 0)}세션)")
    print("  ⚠ 콘테스트 회전율 규정과 대조하라 — 이 수치는 종목 매매를 하기 **전**의 비용이다.")
    return 0


def cmd_backfill(args) -> int:
    """정착봉 구간의 **벤치·상태만** 원장에 채운다(NAV·비중은 빈칸).

    왜 필요한가: 상태는 **경로 의존**이라 원장이 비어 있으면 첫 실행이 `prev_state=정상` 으로 냉시동한다.
    실측 2026-07-31: 그 냉시동 때문에 오늘 행이 `방어` 로 찍혔지만, 정착 시계열(…07-30)의 마지막 상태는
    `방어` 이고 그 위에서 오늘을 판정하면 `복귀` 다 — **밴드 괴리가 −1.9pp 에서 −36.9pp 로 뒤집힌다.**
    즉 냉시동은 경보를 통째로 삼킨다.

    ⚠ 채워지는 행은 `bar_status=backfill` 로 표시된다. **수익분해는 넣지 않는다** —
    그날의 NAV·투자비중을 우리가 모르기 때문이다. 없는 걸 지어내지 않는다(P4).
    """
    b = load_bands()
    if not b:
        print(bands_missing_banner())
        return 1
    df = bench_frame()
    if kr_session_now() and df.index[-1] == _dt.date.today():
        df = df.iloc[:-1]
    n = len(df)
    start = max(20, n - args.days)
    existing = {r["date"]: r for r in load_ledger()}
    state = "정상"
    rows, added = list(existing.values()), 0
    held = 99
    for i in range(start, n):
        m = bench_metrics(df, i)
        raw, why = classify(m, state, b)
        new, hn = apply_min_hold(raw, state, held, b)
        held = 0 if new != state else held + 1
        state = new
        if hn:
            why = [hn] + why
        d = m["date"].isoformat()
        if d in existing and existing[d].get("bar_status") != "backfill":
            continue                          # 실제 적립분은 덮지 않는다
        rows = [r for r in rows if r["date"] != d]
        rows.append({
            "date": d, "bar_status": "backfill", "state": state, "prev_state": "",
            "bench_close": round(m["close"], 2), "bench_ret_d": round(m["ret_d"], 3),
            "bench_dd20": round(m["dd20"], 2), "bench_off_low20": round(m["off_low20"], 2),
            "bench_volmult20": round(m["volmult20"], 3),
            "target_invested_pct": target_for(state, b),
            "note": "backfill(벤치만) / " + "; ".join(why)[:200],
            "alarms": "⚠backfill — NAV·비중 없음, 수익분해 불가",
        })
        added += 1
    write_ledger(rows)
    print(f"[ok] {added}행 backfill → {LEDGER} (마지막 상태 **{state}**)")
    print("  ⚠ 벤치·상태만 채웠다. 그날의 NAV·투자비중은 알 수 없으므로 수익분해는 비어 있다.")
    print("  이제 `log` 를 다시 돌려라 — 오늘 행의 prev_state 가 제대로 잡힌다.")
    return 0


def cmd_backtest(args) -> int:
    """★ 규칙 자체가 **타이밍 가치**가 있나 — 종목선택을 완전히 배제하고 잰다.

    설계: 위험자산 = 벤치(`069500.KS`) 그 자체. 규칙이 정한 `target_invested_pct` 만큼 벤치를 들고
    나머지는 현금(수익 0). 비교 대상 = 벤치 매수후보유(buy&hold). **차이 = 순수하게 비중 결정의 기여.**
    이 리포가 만든 +16.86pp 중 ~14pp 가 이 변수였다면, 그 변수가 반복 가능한지는 여기서만 답한다.

    ⚠ **체결 지연 t+1 강제.** 규칙은 **종가**를 보고 발화하므로 그 종가에 살 수 없다.
    `shift(1)` 없이 재면 백테스트가 완벽하고 실전이 0 이 되는 고전적 선행참조다.
    ⚠ **거래비용을 뺀다.** 이 규칙은 실측 주당 19.6pp 를 돌린다 — 비용 0 가정은 정직하지 않다.
    ⚠ **독립 관측 수 = 세션 수가 아니라 상태 전이 수**다. 120세션이어도 결정은 18번뿐이다(C4).
    ⚠ **여러 시작일에서 돌린다** — 창을 결과로 고르지 않기 위해서다(D106).
    ⚠ **여러 지평에서 본다** — 클래스 평균이 지평에 따라 뒤집힌 전례가 있다(D105).
    """
    b = load_bands()
    if not b:
        print(bands_missing_banner())
        return 1
    import numpy as np

    df = bench_frame(600)
    if kr_session_now() and df.index[-1] == _dt.date.today():
        df = df.iloc[:-1]
    close = df["Close"].to_numpy(dtype=float)
    n = len(df)
    ret = np.zeros(n)
    ret[1:] = close[1:] / close[:-1] - 1.0

    # 규칙 목표비중 시계열 (그날 종가 기준 판정)
    w = np.full(n, np.nan)
    state, held = "정상", 99
    for i in range(20, n):
        m = bench_metrics(df, i)
        raw, _ = classify(m, state, b)
        new, _ = apply_min_hold(raw, state, held, b)
        held = 0 if new != state else held + 1
        state = new
        t = target_for(new, b)
        w[i] = (t or 0) / 100.0

    print(f"# EXPOSURE RULE — 타이밍 가치 백테스트  (벤치 {BENCH} = 위험자산)")
    print(f"  {df.index[20]} ~ {df.index[-1]} · {n-20}세션")
    print("  설계: 규칙 비중만큼 벤치 보유, 나머지 현금(0%). 비교 = 벤치 매수후보유.")
    print("  ★ 체결 t+1 (종가 보고 다음 세션 집행) · 거래비용 차감 · 종목선택 기여 0\n")

    for cost_bp in args.cost_bp:
        print(f"## 편도 거래비용 {cost_bp}bp")
        print(f"{'시작':>6} {'세션':>5} {'전이':>4} | {'규칙':>8} {'매수후보유':>10} {'차이':>8} | "
              f"{'규칙MDD':>8} {'B&H MDD':>8}")
        for back in args.starts:
            s = max(20, n - back)
            ww = np.nan_to_num(w[s:])
            rr = ret[s:]
            wl = np.concatenate([[ww[0]], ww[:-1]])          # ★ t+1 체결
            turn = np.abs(np.diff(np.concatenate([[wl[0]], wl])))
            cost = turn * (cost_bp / 10000.0)
            strat = wl * rr - cost
            cum_s = float(np.prod(1 + strat) - 1) * 100
            cum_b = float(np.prod(1 + rr) - 1) * 100
            eq_s = np.cumprod(1 + strat)
            eq_b = np.cumprod(1 + rr)
            mdd_s = float((eq_s / np.maximum.accumulate(eq_s) - 1).min()) * 100
            mdd_b = float((eq_b / np.maximum.accumulate(eq_b) - 1).min()) * 100
            nch = int((np.diff(ww) != 0).sum())
            print(f"{back:>6} {len(rr):>5} {nch:>4} | {cum_s:>+7.2f}% {cum_b:>+9.2f}% "
                  f"{cum_s-cum_b:>+7.2f}pp | {mdd_s:>+7.1f}% {mdd_b:>+7.1f}%")
        print()

    # 전이별 = 진짜 독립 관측. 각 '방어/복귀 구간'이 벤치 대비 어땠나.
    s = max(20, n - max(args.starts))
    ww, rr = np.nan_to_num(w[s:]), ret[s:]
    wl = np.concatenate([[ww[0]], ww[:-1]])
    segs, cur, i0 = [], wl[0], 0
    for i in range(1, len(wl)):
        if wl[i] != cur:
            segs.append((cur, i0, i))
            cur, i0 = wl[i], i
    segs.append((cur, i0, len(wl)))
    print("## ★ 상태 구간별 — 독립 관측은 세션이 아니라 이것이다")
    print(f"{'비중':>6} {'세션':>5} {'벤치구간수익':>12} {'규칙기여(비중-1)×벤치':>22}")
    contrib = []
    for wv, a, z in segs:
        br = float(np.prod(1 + rr[a:z]) - 1) * 100
        c = (wv - 1.0) * br
        contrib.append(c)
        print(f"{wv*100:>5.0f}% {z-a:>5} {br:>+11.2f}% {c:>+21.2f}pp")
    contrib = np.array(contrib)
    pos = int((contrib > 0).sum())
    print(f"\n  구간 {len(contrib)}개 · 기여 합 {contrib.sum():+.2f}pp · 평균 {contrib.mean():+.2f}pp "
          f"· 양수 {pos}/{len(contrib)}")
    if len(contrib) > 2:
        t = contrib.mean() / (contrib.std(ddof=1) / np.sqrt(len(contrib)))
        print(f"  단순 t = {t:+.2f} (n={len(contrib)})  ⇒ "
              f"{'유의' if abs(t) > 2 else '**구분 불가 — 검정력 없음(C4)**'}")
    print("\n⚠ 이것은 사후 시뮬레이션이다. 규칙은 그때 돌지 않았고, 밴드는 이 창을 본 뒤에 정해졌다.")
    print("  ⇒ **밴드 선택 자체가 이 창에 적합화됐을 수 있다.** 진짜 검정은 오늘 이후의 사전등록 관측이다.")
    return 0


def cmd_show(args) -> int:
    rows = load_ledger()
    if not rows:
        print(f"[info] 원장 비어있음 — `log` 를 먼저 실행 ({LEDGER})")
        return 0
    tail = rows[-args.tail:]
    print(f"# EXPOSURE LEDGER — {len(rows)}행 (표시 {len(tail)})  {LEDGER}")
    print(f"{'날짜':11s} {'봉':8s} {'상태':10s} {'벤치%':>7} {'NAV%':>7} {'투자%':>6} "
          f"{'총초과':>7} {'현금기여':>8} {'선택기여':>8}  경보")
    for r in tail:
        print(f"{r['date']:11s} {r['bar_status']:8s} {r['state']:10s} "
              f"{r['bench_ret_d'] or '':>7} {r['nav_ret_d'] or '':>7} {r['invested_pct'] or '':>6} "
              f"{r['excess_total_pp'] or '':>7} {r['cash_contrib_pp'] or '':>8} "
              f"{r['select_contrib_pp'] or '':>8}  {r['alarms']}")

    def s(k):
        return [float(r[k]) for r in rows if r.get(k) not in (None, "")]

    cash, sel, tot = s("cash_contrib_pp"), s("select_contrib_pp"), s("excess_total_pp")
    print(f"\n  누적(단순합) — 총초과 {sum(tot):+.2f}pp = 현금기여 {sum(cash):+.2f}pp "
          f"+ 선택기여 {sum(sel):+.2f}pp   (n={len(tot)})")
    print(f"  ⚠ n={len(tot)}. 이 리포의 목표는 이 n 을 매일 1씩 올리는 것이다 — "
          f"한 달이면 n≈20, 그때 비로소 부호를 물을 수 있다(C4).")
    return 0


def main() -> int:
    utf8_stdout()
    ap = argparse.ArgumentParser(prog="exposure_rule")
    sp = ap.add_subparsers(dest="cmd", required=True)

    def acct(p):
        p.add_argument("--nav", type=float, default=None)
        p.add_argument("--nav-ret", type=float, default=None, help="NAV 당일 수익률 %")
        p.add_argument("--invested", type=float, default=None, help="투자비중 % (100−현금)")
        p.add_argument("--sleeve-ret", type=float, default=None, help="투자슬리브 당일 수익률 %")
        p.add_argument("--from-timefolio", action="store_true",
                       help="CDP 브라우저에서 module_timefolio 로 직접 읽기")
        p.add_argument("--no-live-bench", action="store_true",
                       help="장중이라도 KIS 실시간을 쓰지 않고 yfinance 봉만 쓴다")
        return p

    acct(sp.add_parser("state", help="오늘 판정(적립 안 함)")).set_defaults(func=cmd_state)
    acct(sp.add_parser("log", help="오늘 1행 적립(날짜 upsert)")).set_defaults(func=cmd_log)

    t = sp.add_parser("target", help="현금·투자 목표비중 JSON (F5 의 현금 SSOT)")
    t.add_argument("--json", action="store_true")
    t.set_defaults(func=cmd_target)

    p = sp.add_parser("propose", help="밴드 숫자를 사람이 정하기 위한 실측표")
    p.add_argument("--days", type=int, default=120)
    p.add_argument("--defend-grid", type=float, nargs="*", default=[5, 8, 10, 12, 15])
    p.add_argument("--recover-grid", type=float, nargs="*", default=[3, 5, 7, 10])
    p.add_argument("--vol-grid", type=float, nargs="*", default=[1.0, 1.3])
    p.add_argument("--since-date", type=_dt.date.fromisoformat, default=None,
                   help="§3 의 시작일(기본: 최근 10일)")
    p.set_defaults(func=cmd_propose)

    bf = sp.add_parser("backfill", help="정착봉 구간의 벤치·상태를 원장에 채운다(냉시동 방지)")
    bf.add_argument("--days", type=int, default=25)
    bf.set_defaults(func=cmd_backfill)

    sm = sp.add_parser("simulate", help="설정된 밴드로 과거 정착봉을 상태기계째 돌린다")
    sm.add_argument("--days", type=int, default=25)
    sm.set_defaults(func=cmd_simulate)

    bt = sp.add_parser("backtest", help="★ 규칙 자체의 타이밍 가치 (종목선택 배제, t+1 체결, 비용 차감)")
    bt.add_argument("--starts", type=int, nargs="*", default=[60, 120, 250, 500],
                    help="최근 N세션 창들 — 창을 결과로 고르지 않기 위해 여러 개")
    bt.add_argument("--cost-bp", type=int, nargs="*", default=[0, 10, 25],
                    help="편도 거래비용(bp)")
    bt.set_defaults(func=cmd_backtest)

    sh = sp.add_parser("show", help="적립 원장 + 누적 분해")
    sh.add_argument("--tail", type=int, default=30)
    sh.set_defaults(func=cmd_show)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
