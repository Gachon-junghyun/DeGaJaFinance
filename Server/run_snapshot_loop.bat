@echo off
REM ============================================================
REM  DeGaJaFinance — analyst-estimate snapshot loop (SERVER PC role). dig D16.
REM
REM  WHY THIS LIVES ON THE SERVER (P6):
REM    yfinance eps_trend is a SNAPSHOT, not a time series, and it is NOT
REM    retroactively recoverable — every day not stored is gone for good.
REM    The job was originally a Windows scheduled task on the CLIENT PC at
REM    08:10 KST. But the client is "turned on only when needed" while the
REM    server runs 24h. Measured 2026-08-09: 19 calendar days produced only
REM    6 files, gaps growing 2 -> 3 -> 4 -> 6. At that rate the 40-day panel
REM    arrives in ~108 days instead of ~34. The gap sequence was effectively
REM    a measurement of how often the client PC was switched on.
REM
REM  WHY A LOOP AND NOT A SCHEDULED TASK:
REM    A fixed 08:10 task loses the whole day if the machine is down at 08:10.
REM    This loop retries hourly and the script itself is idempotent (it refuses
REM    to overwrite an existing same-day file without --force), so the day is
REM    captured whenever the machine is up at ANY point during it.
REM
REM  Read-only network (yfinance public), local write only. No orders, no secrets.
REM  Log: data\snapshot_loop.log   ·  Status: python -X utf8 scripts\snapshot_estimates.py --status
REM  Korean guide: Server\README.md
REM ============================================================
chcp 65001 >nul
setlocal
set "INTERVAL=3600"
set "LIMIT=120"
pushd "%~dp0.."
if not exist "data" mkdir "data"
title DeGaJa ESTIMATE SNAPSHOT loop

:loop
echo ===== %DATE% %TIME%  estimate snapshot (limit %LIMIT%) =====
echo ===== %DATE% %TIME%  estimate snapshot (limit %LIMIT%) ===== >> "data\snapshot_loop.log"
python -X utf8 scripts\snapshot_estimates.py --limit %LIMIT% >> "data\snapshot_loop.log" 2>&1
echo    done %TIME% -- sleeping %INTERVAL%s (Ctrl+C to stop)
timeout /t %INTERVAL% /nobreak >nul
goto loop
