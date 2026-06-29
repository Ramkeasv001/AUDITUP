@echo off
REM Launches the ADITUP PWA on a local server so install/offline works.
where python >nul 2>nul
if %errorlevel%==0 (
  python serve.py
) else (
  where py >nul 2>nul
  if %errorlevel%==0 (
    py serve.py
  ) else (
    echo Python is required but was not found.
    echo Install Python 3 from https://www.python.org/downloads/ and try again.
    pause
  )
)
