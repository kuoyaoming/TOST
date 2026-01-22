# Translategemma - 離線螢幕翻譯神器

[English](README.md)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-0078D6)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/Model-Ollama-black)

專為隱私與效率設計的離線螢幕翻譯工具。框選螢幕任意區域，透過系統原生通知即時獲得繁體中文翻譯。完全離線執行，資料不外流。
由 **Ollama** (AI) 與 **RapidOCR** (離線 OCR) 強力驅動。

## 特色
- 🔒 **隱私優先**: 完全離線執行，資料不外流。
- 🚀 **輕量極速**: 使用 RapidOCR 進行快速文字辨識。
- 🤖 **AI 驅動**: 使用 Gemma (透過 Ollama) 進行自然語言翻譯。
- 🖥️ **跨平台支援**: 支援 **Windows 11** (原生通知) 與 **Linux** (`notify-send`)。
- 📂 **系統匣常駐**: 縮小至 System Tray 背景執行，不佔用桌面空間。
- 📋 **自動複製**: 翻譯結果自動複製到剪貼簿。
- ⌨️ **全域熱鍵**: 隨時按下 `Shift + Alt + Z` 即可觸發。
- 📸 **無限截圖**: 最佳化的常駐覆蓋引擎，連續截圖不卡頓。

## 安裝說明

### 前置需求
1.  **Ollama**: 請至 [ollama.com](https://ollama.com) 下載安裝。
2.  **模型**: 請至 [HuggingFace](https://huggingface.co/mradermacher/translategemma-4b-it-GGUF) 下載 `translategemma-4b-it-GGUF`。
    *   將 `.gguf` 檔案放入 `models/` 資料夾。

### 快速開始 (桌面版)

#### Windows
1.  下載 **獨立發行版** (ZIP)。
2.  解壓縮資料夾。
3.  執行 `setup.bat` 一次以匯入模型至 Ollama。
4.  執行 `Translategemma.exe` 或 `run.bat`。

#### Linux
1.  確保已安裝 `python3` 與 `pip`。
2.  賦予腳本執行權限: `chmod +x *.sh`。
3.  執行 `./setup.sh` 以匯入模型。
4.  執行 `./build.sh` 編譯執行檔，或直接執行 `./run.sh` 啟動。

### 開發者設定 (原始碼)
若您想從原始碼執行：

```bash
# 1. Clone repo
git clone https://github.com/yourusername/translategemma.git
cd translategemma

# 2. Setup Env (跨平台)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux:
source .venv/bin/activate

# 3. Install Deps
pip install -r requirements.txt

# 4. Import Model
# Windows:
setup.bat
# Linux:
./setup.sh

# 5. Run
# Windows:
python src/app.py
# Linux:
python3 src/app.py
```

## 使用方法
1.  執行應用程式。
    *   **Windows**: `Translategemma.exe`
    *   **Linux**: `./dist/Translategemma/Translategemma` 或 `python3 src/app.py`
2.  程式將縮小至 **系統匣 (System Tray)**。
3.  按下 **`Shift + Alt + Z`**。
    *   *注意: 在 Linux 上若因權限問題無法觸發熱鍵，請對系統匣圖示按右鍵並選擇 "Snip" (截圖)。*
4.  在螢幕上框選英文文字區域。
5.  透過系統通知接收翻譯結果，並同時複製到剪貼簿！

## 專案結構
```
Translategemma/
├── src/
│   ├── app.py           # 主程式 (System Tray 常駐與邏輯)
│   ├── snipper.py       # 跨平台截圖工具
│   ├── utils.py         # 平台特定邏輯 (通知、螢幕座標)
│   └── ...
├── models/              # GGUF 模型與 Modelfile
├── dist/                # 預先編譯的執行檔
├── build.bat / .sh      # 建置腳本
├── setup.bat / .sh      # 安裝設定腳本
└── run.bat / .sh        # 啟動腳本
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
