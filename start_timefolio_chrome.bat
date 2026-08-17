@echo off
REM -- Timefolio mirror: launch Chrome with remote debugging on 9222 --
REM  Dedicated debug profile (keeps the login session) + opens the contest tab.
REM  If 9222 is already listening, skip launching (just reuse).
REM  Separate profile from normal browsing Chrome, so no conflict with a
REM  Chrome that is already running on the default profile (that one CANNOT
REM  expose the debug port after the fact - hence a dedicated user-data-dir).
REM  NOTE: keep this file ASCII-only and do NOT add `chcp` -- UTF-8 Korean
REM        comments get mangled under the OEM codepage in non-interactive
REM        shells and sent the original script into a runaway parse loop.

set "CHROME=C:\Program Files\Google\Chrome\Application\chrome.exe"
if not exist "%CHROME%" set "CHROME=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
set "PROFILE=C:\Users\fivep\chrome-debug-carmacro"
set "URL=https://contest.timefolio.net/"

netstat -ano | findstr /C:":9222" | findstr LISTENING >nul 2>&1
if %errorlevel%==0 (
  echo [start_timefolio_chrome] 9222 already listening - skip launch.
  goto :eof
)

echo [start_timefolio_chrome] launching Chrome on 9222 with profile %PROFILE%
start "" "%CHROME%" --remote-debugging-port=9222 --user-data-dir="%PROFILE%" --no-first-run --no-default-browser-check --restore-last-session=false "%URL%"

REM Wait up to ~20s for the CDP port to come up.
REM  (ping-based sleep - works non-interactively; `timeout` fails on stdin redirect)
set /a tries=0
:waitloop
ping 127.0.0.1 -n 3 >nul
netstat -ano | findstr /C:":9222" | findstr LISTENING >nul 2>&1
if %errorlevel%==0 (
  echo [start_timefolio_chrome] 9222 is up.
  goto :eof
)
set /a tries+=1
if %tries% LSS 10 goto :waitloop
echo [start_timefolio_chrome] WARNING: 9222 did not come up within timeout.
