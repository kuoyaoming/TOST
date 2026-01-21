# Translategemma - Offline Screen Translator

[繁體中文](README_zh-TW.md)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/Model-Ollama-black)

A powerful, lightweight, and completely privacy-focused screen translator. Select any area on your screen, and get instant Traditional Chinese translations via Windows native notifications. 
Powered by **Ollama** (AI) and **RapidOCR** (Offline OCR).

## Features
- 🔒 **Privacy First**: Everything runs locally. No data is sent to the cloud.
- 🚀 **Lightweight**: Uses RapidOCR for fast text extraction.
- 🤖 **AI Powered**: Uses Gemma (via Ollama) for natural translation.
- 🖥️ **Windows 11 Native**: Results appear as elegant system notifications.
- ⌨️ **Global Hotkey**: Press `Shift + Alt + Z` anytime to trigger.
- 📸 **Infinite Snipping**: Optimized persistent overlay engine.

## Installation

### Prerequisites
1.  **Ollama**: Download and install from [ollama.com](https://ollama.com).
2.  **Model**: Download `translategemma-4b-it-GGUF` from [HuggingFace](https://huggingface.co/mradermacher/translategemma-4b-it-GGUF).
    *   Place the `.gguf` file in the `models/` directory.

### Quick Start (Desktop App)
1.  Download the **Standalone Distribution** (ZIP).
2.  Extract the folder.
3.  Run `setup.bat` once to import the model into Ollama.
4.  Run `Translategemma.exe`.

### Developer Setup (Source Code)
If you want to run from source:
```bash
# 1. Clone repo
git clone https://github.com/yourusername/translategemma.git
cd translategemma

# 2. Setup Env
python -m venv .venv
.venv\Scripts\activate

# 3. Install Deps
pip install -r requirements.txt

# 4. Import Model
setup.bat

# 5. Run
python src/app.py
```

## Usage
1.  Run the application (`Translategemma.exe` or `src/app.py`).
2.  Wait for the **"Waiting for Hotkey"** message in the console.
3.  Press **`Shift + Alt + Z`**.
4.  Draw a rectangle around the English text on your screen.
5.  Receive the translation via Windows Notification!

## Project Structure
```
Translategemma/
├── src/
│   ├── app.py           # Main entry point (Persistent GUI & Logic)
│   ├── snipper.py       # Tkinter Screen Selection Tool
│   ├── ocr_handler.py   # RapidOCR Wrapper
│   └── ...
├── models/              # GGUF Model and Modelfile
├── dist/                # Pre-built executables (Excluded from Git)
├── build.bat            # PyInstaller Build Script
└── requirements.txt     # Python Dependencies
```

## License

### Application License
The source code of this application is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

### Model License
The **Translategemma** model is provided under and subject to the **[Gemma Terms of Use](https://ai.google.dev/gemma/terms)**.
By using this application with the Gemma model, you agree to comply with these terms.
See [NOTICE](NOTICE) for the mandatory use declaration.

### Third Party Licenses
This project uses several open-source libraries (RapidOCR, Ollama, etc.).
Please see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the full list of third-party licenses and attributions.

## Acknowledgements
- **[Google - Translategemma](https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/)**: For the inspiration and the powerful Gemma family of models.
- **[mradermacher/translategemma-4b-it-GGUF](https://huggingface.co/mradermacher/translategemma-4b-it-GGUF)**: For providing the quantized GGUF model optimized for offline use.
- **[Antigravity](https://antigravity.google/)**: For the advanced AI agent assistance in building this project.
