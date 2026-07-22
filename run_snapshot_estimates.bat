@echo off
REM ============================================================
REM  DeGaJaFinance — daily analyst-estimate snapshot (dig D16).
REM
REM  WHY: yfinance eps_trend is a SNAPSHOT, not a time series. Without a daily
REM  store the revision-IC can never become a real panel — and the data is NOT
REM  retroactively recoverable: every day not stored is gone for good.
REM  Writes data\estimates\eps_YYYY-MM-DD.json (one file per date, idempotent).
REM
REM  Read-only + local write. No orders, no network writes, no secrets.
REM  Manual run: run_snapshot_estimates.bat        (or  ... 300  for 300 names)
REM  Status:     python -X utf8 scripts\snapshot_estimates.py --status
REM  Scheduled as Windows task "DeGaJa-EstimateSnapshot" (daily 08:10 KST).
REM ============================================================
chcp 65001 >nul
pushd "%~dp0"
if not exist "data\estimates" mkdir "data\estimates"
set LIMIT=%1
if "%LIMIT%"=="" set LIMIT=120
python -X utf8 "scripts\snapshot_estimates.py" --limit %LIMIT% >> "data\estimates\snapshot.log" 2>&1
popd
