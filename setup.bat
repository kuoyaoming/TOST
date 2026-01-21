@echo off
echo Setting up Translategemma in Ollama...

where ollama >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Ollama is not installed or not in PATH!
    echo Please download and install Ollama from https://ollama.com/
    pause
    exit /b 1
)

echo Creating model '%MODEL_NAME%' from Modelfile...
echo This may take a few moments...
echo.

rem Change to models directory where Modelfile and GGUF are located
pushd models
ollama create translategemma -f Modelfile
set EXIT_CODE=%errorlevel%
popd

if %EXIT_CODE% neq 0 (
    echo.
    echo Error creating model!
    echo Please ensure the Ollama server is running (try running 'ollama serve' in another window).
    pause
    exit /b 1
)

echo.
echo Model created successfully!
echo You can now run 'run.bat'.
pause
