@echo off
echo ===============================================
echo Building Translategemma Standalone Distribution
echo ===============================================

rem Ensure PyInstaller is installed
where pyinstaller >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: pyinstaller not found. Installing...
    call .venv\Scripts\python.exe -m pip install pyinstaller
)

rem Clean previous build
if exist "dist\Translategemma" rmdir /s /q "dist\Translategemma"
if exist "build" rmdir /s /q "build"

echo.
echo Running PyInstaller...
rem --onedir: Create a folder (faster/easier)
rem --name: Output name
rem --windowed: No console? User wanted "background" but initially we had console for input.
rem app.py has input() loop! If we make it --windowed (noconsole), input() will crash or do nothing.
rem User's current workflow: Run run.bat (console), press hotkey.
rem The hotkey works in background.
rem However, app.py prints "Please type text...".
rem If we hide console, we lose the "interactive text translation" feature, only hotkey remains.
rem Given the request "run in background", hiding console is cleaner, BUT app.py code expects console interactions (input()).
rem Compromise: Keep console for now (--console) so user can see output/errors and use text mode.
rem If user wants purely background, they can minimize the console.

call .venv\Scripts\pyinstaller.exe ^
    --noconfirm ^
    --onedir ^
    --console ^
    --name "Translategemma" ^
    --clean ^
    --collect-all rapidocr_onnxruntime ^
    --collect-all win11toast ^
    --paths src ^
    src\app.py

echo.
echo Copying Resource Files...

rem Create models directory in dist
mkdir "dist\Translategemma\models"

rem Copy GGUF and Modelfile
copy "models\*" "dist\Translategemma\models\" >nul

rem Copy Setup script and Readme
copy "setup.bat" "dist\Translategemma\" >nul
copy "Readme.txt" "dist\Translategemma\" >nul

echo.
echo ===============================================
echo Build Complete!
echo Distribution is located at: dist\Translategemma
echo ===============================================
