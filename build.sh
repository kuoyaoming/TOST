#!/bin/bash

echo "==============================================="
echo "Building Translategemma Standalone Distribution (Linux)"
echo "==============================================="

# Ensure PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "Error: pyinstaller not found. Installing..."
    # Assuming user has python or python3 available
    python3 -m pip install pyinstaller
fi

# Clean previous build
if [ -d "dist/Translategemma" ]; then
    rm -rf "dist/Translategemma"
fi
if [ -d "build" ]; then
    rm -rf "build"
fi

echo ""
echo "Running PyInstaller..."

# Run PyInstaller
# Note: win11toast is excluded as it is Windows only.
pyinstaller \
    --noconfirm \
    --onedir \
    --console \
    --name "Translategemma" \
    --clean \
    --collect-all rapidocr_onnxruntime \
    --paths src \
    src/app.py

echo ""
echo "Copying Resource Files..."

# Create models directory in dist
mkdir -p "dist/Translategemma/models"

# Copy GGUF and Modelfile
# Suppress output for clean run
cp models/* "dist/Translategemma/models/" 2>/dev/null

# Copy Setup script and Readme
cp "setup.sh" "dist/Translategemma/" 2>/dev/null
# Try to copy README files if they exist
cp "README.md" "dist/Translategemma/" 2>/dev/null
cp "README_zh-TW.md" "dist/Translategemma/" 2>/dev/null

echo ""
echo "==============================================="
echo "Build Complete!"
echo "Distribution is located at: dist/Translategemma"
echo "To run, execute: ./dist/Translategemma/Translategemma"
echo "==============================================="
