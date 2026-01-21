# Translategemma - Offline Screen Translator (離線螢幕翻譯神器)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/Model-Ollama-black)

A powerful, lightweight, and completely privacy-focused screen translator. Select any area on your screen, and get instant Traditional Chinese translations via Windows native notifications. 
Powered by **Ollama** (AI) and **RapidOCR** (Offline OCR).

**專為隱私與效率設計的離線螢幕翻譯工具。框選螢幕任意區域，透過 Windows 原生通知即時獲得繁體中文翻譯。完全離線執行，資料不外流。**

## Features (特色)
- 🔒 **Privacy First**: Everything runs locally. No data is sent to the cloud. (完全離線，隱私安全)
- 🚀 **Lightweight**: Uses RapidOCR for fast text extraction. (輕量極速 OCR)
- 🤖 **AI Powered**: Uses Gemma (via Ollama) for natural translation. (AI 自然語言翻譯)
- 🖥️ **Windows 11 Native**: Results appear as elegant system notifications. (原生 Win11 通知整合)
- ⌨️ **Global Hotkey**: Press `Shift + Alt + Z` anytime to trigger. (全域熱鍵支援)
- 📸 **Infinite Snipping**: Optimized persistent overlay engine. (無限次連續截圖，不卡頓)

## Installation (安裝說明)

### Prerequisites (前置需求)
1.  **Ollama**: Download and install from [ollama.com](https://ollama.com).
2.  **Model**: This app uses `translategemma-4b-it`.

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

## Usage (使用方法)
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
