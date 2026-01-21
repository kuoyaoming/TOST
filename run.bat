@echo off
echo Starting Translategemma App...
rem Change to src directory so imports work naturally
pushd src
call ..\.venv\Scripts\python.exe app.py
popd
pause
