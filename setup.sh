#!/bin/bash

echo "Setting up Translategemma in Ollama..."

if ! command -v ollama &> /dev/null; then
    echo "Error: Ollama is not installed or not in PATH!"
    echo "Please download and install Ollama from https://ollama.com/"
    exit 1
fi

MODEL_NAME="translategemma"

echo "Creating model '$MODEL_NAME' from Modelfile..."
echo "This may take a few moments..."
echo ""

# Change to models directory where Modelfile and GGUF are located
cd models || exit 1
ollama create translategemma -f Modelfile
EXIT_CODE=$?
cd ..

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "Error creating model!"
    echo "Please ensure the Ollama server is running (try running 'ollama serve' in another terminal)."
    exit 1
fi

echo ""
echo "Model created successfully!"
echo "You can now run './run.sh'."
