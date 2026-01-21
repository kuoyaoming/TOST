# Translategemma - 離線螢幕翻譯神器

[English](README.md)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/Model-Ollama-black)

專為隱私與效率設計的離線螢幕翻譯工具。框選螢幕任意區域，透過 Windows 原生通知即時獲得繁體中文翻譯。完全離線執行，資料不外流。

## 特色
- 🔒 **隱私優先**: 完全離線執行，資料不外流。
- 🚀 **輕量極速**: 使用 RapidOCR 進行快速文字辨識。
- 🤖 **AI 驅動**: 使用 Gemma (透過 Ollama) 進行自然語言翻譯。
- 🖥️ **Windows 11 原生整合**: 翻譯結果以優雅的系統通知呈現。
- ⌨️ **全域熱鍵**: 隨時按下 `Shift + Alt + Z` 即可觸發。
- 📸 **無限截圖**: 最佳化的常駐覆蓋引擎，連續截圖不卡頓。

## 安裝說明

### 前置需求
1.  **Ollama**: 請至 [ollama.com](https://ollama.com) 下載安裝。
2.  **模型**: 請至 [HuggingFace](https://huggingface.co/mradermacher/translategemma-4b-it-GGUF) 下載 `translategemma-4b-it-GGUF`。
    *   將 `.gguf` 檔案放入 `models/` 資料夾。

### 快速開始 (桌面版)
1.  下載 **獨立發行版** (ZIP)。
2.  解壓縮資料夾。
3.  執行 `setup.bat` 一次以匯入模型至 Ollama。
4.  執行 `Translategemma.exe`。

### 開發者設定 (原始碼)
若您想從原始碼執行：
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

## 使用方法
1.  執行應用程式 (`Translategemma.exe` 或 `src/app.py`)。
2.  等待主控台出現 **"Waiting for Hotkey"** 訊息。
3.  按下 **`Shift + Alt + Z`**。
4.  在螢幕上框選英文文字區域。
5.  透過 Windows 通知接收翻譯結果！

## 專案結構
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

## 授權

### 軟體授權
本應用程式原始碼採用 **MIT 授權**。詳細內容請參閱 [LICENSE](LICENSE)。

### 模型授權
**Translategemma** 模型受 **[Gemma 使用條款](https://ai.google.dev/gemma/terms)** 約束。
使用本應用程式及 Gemma 模型即表示您同意遵守這些條款。
請參閱 [NOTICE](NOTICE) 以取得強制性使用聲明。

### 第三方授權
本專案使用多個開源函式庫 (RapidOCR, Ollama 等)。
完整第三方授權與來源標示請參閱 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 致謝
- **[Google - Translategemma](https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/)**: 感謝 Google 的啟發以及強大的 Gemma 模型系列。
- **[mradermacher/translategemma-4b-it-GGUF](https://huggingface.co/mradermacher/translategemma-4b-it-GGUF)**: 感謝提供最佳化離線使用的 GGUF 量化模型。
- **[Antigravity](https://antigravity.google/)**: 感謝 Antigravity 的先進 AI 代理協助建構此專案。
