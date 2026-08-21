# AGENTS.md — AI Agent Guidance for TOST

> **Repository:** `Max97k/TOST`  
> **Default Branch:** `main`  
> **Primary Technology Stack:** Python 3.10+, RapidOCR ONNX Runtime, Ollama (Gemma LLM), Tkinter, PyInstaller  
> **Visibility:** Public  

---

## 1. Project Overview & Architecture

### 1.1 Purpose & Mission
**TOST** (Translate Offline Screen Text) is a lightweight, cross-platform, 100% offline screen capture, OCR, and AI-powered translation utility for Windows and Linux. It combines local Optical Character Recognition via RapidOCR with local Large Language Model inference via Ollama running a custom quantized Gemma 4B model (`translategemma-4b-it.Q2_K.gguf`) to translate on-screen English text into Traditional Chinese (繁體中文) with zero internet dependency and complete privacy.

### 1.2 System Architecture & Component Diagram
```
+-----------------------------------------------------------------------------+
|                                TOST Core Runtime                             |
+-----------------------------------------------------------------------------+
|  Global Hotkey (Shift+Alt+Z) / Pystray System Tray / Console Input Loop     |
+-----------------------------------------------------------------------------+
                                       |
                                       v
                     +-----------------------------------+
                     |           src/snipper.py          |
                     |  Transparent Fullscreen Overlay   |
                     |  Interactive Bounding Box Grabber |
                     +-----------------------------------+
                                       |
                                       v
                     +-----------------------------------+
                     |        src/ocr_handler.py         |
                     |  RapidOCR ONNX Runtime (Offline)  |
                     |  Image-to-Text & Text Formatting  |
                     +-----------------------------------+
                                       |
                                       v
                     +-----------------------------------+
                     |       Local Ollama Daemon         |
                     |  Model: translategemma (Gemma 4B) |
                     |  Prompt: Traditional Chinese EN->ZH|
                     +-----------------------------------+
                                       |
                                       v
                     +-----------------------------------+
                     |           src/utils.py            |
                     |  - Windows Toast (win11toast)     |
                     |  - Linux Desktop (notify-send)    |
                     |  - System Clipboard (pyperclip)   |
                     +-----------------------------------+
```

### 1.3 Key File & Directory Map
| Path | Purpose / Description |
|---|---|
| `src/app.py` | Main application entrypoint. Initializes Tkinter loop, Pystray tray icon, global hotkey hook (`keyboard`), and interactive CLI text mode. |
| `src/snipper.py` | Screen capture snip tool. Renders transparent canvas overlay and captures selected screen coordinates via Pillow. |
| `src/ocr_handler.py` | Offline OCR engine wrapping `rapidocr_onnxruntime` to parse cropped images into plain text. |
| `src/utils.py` | Cross-platform utilities: clipboard injection (`pyperclip`) and native OS notifications (`win11toast` / `notify-send`). |
| `models/Modelfile` | Ollama model configuration with system prompt instructions and stop tokens for Traditional Chinese translation. |
| `setup.bat` / `setup.sh` | Automated model initialization script executing `ollama create translategemma -f models/Modelfile`. |
| `build.bat` / `build.sh` | PyInstaller standalone packaging scripts bundling all dependencies and ONNX models into `dist/Translategemma`. |
| `run.bat` / `run.sh` | Virtual environment launcher scripts for quick startup. |
| `requirements.txt` | Python runtime dependencies. |

---

## 2. Development, Build & Verification Commands

### 2.1 Prerequisites & Environment Setup
- **Python:** Python 3.10 or higher.
- **Ollama:** Installed and running locally (`http://localhost:11434`).
- **Gemma GGUF:** Quantized model weights `translategemma-4b-it.Q2_K.gguf` placed in the repository root or `models/`.

```bash
# Clone and setup virtual environment
git clone https://github.com/Max97k/TOST.git
cd TOST

# Windows
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
setup.bat

# Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./setup.sh
```

### 2.2 Running & Testing Commands
```bash
# Run application directly from source
python src/app.py

# Syntax check all Python source files
python -m py_compile src/app.py src/snipper.py src/ocr_handler.py src/utils.py
```

### 2.3 Standalone Binary Packaging
```bash
# Windows PyInstaller build (generates dist/Translategemma)
build.bat

# Linux PyInstaller build
./build.sh
```

### 2.4 Clean & Reset
```bash
# Windows
rmdir /s /q build dist __pycache__ src\__pycache__

# Linux
rm -rf build dist __pycache__ src/__pycache__
```

---

## 3. Coding Standards & Conventions

### 3.1 Code Style & Idioms
- **Python 3 Idioms:** Follow PEP 8 style guidelines. Use explicit type hints where beneficial.
- **Cross-Platform Safety:** Guard OS-specific imports conditionally (e.g., `win11toast` under `if sys.platform == 'win32'`).
- **Clean Fallbacks:** When running on Linux/headless environments, handle missing GUI or keyboard hook permissions gracefully without crashing the main thread.

### 3.2 File & Module Organization
- Keep GUI overlay code in `src/snipper.py`, OCR parsing logic in `src/ocr_handler.py`, and notification/clipboard helpers in `src/utils.py`.
- Do not place business logic directly in `build.bat` or `setup.sh`; keep shell scripts strictly for automation and environment bootstrap.

### 3.3 State Management & Error Handling
- **Ollama Connection:** Handle `requests.exceptions.ConnectionError` or `ollama.ResponseError` gracefully when the local Ollama daemon is offline or the model is still loading.
- **OCR Failures:** If no text is detected in the cropped region, notify the user with a brief toast rather than raising an unhandled exception.
- **Resource Teardown:** Ensure Tkinter root and canvas windows are destroyed and keyboard hooks are unhooked when the application terminates.

---

## 4. Safety, Security & Resource Constraints

### 4.1 Secrets & Environment Management
- **Zero Cloud Leakage:** All OCR and LLM operations must remain 100% local. Do not send captured screen text or images to external third-party APIs.
- No API keys or credentials should be introduced into the repository.

### 4.2 Resource & Performance Constraints
- **Low Memory Overhead:** Keep ONNX Runtime threads and image processing buffers minimal.
- **Fast Response Time:** OCR execution should take < 300ms, and local Gemma inference should begin streaming or return translation promptly.

### 4.3 Git & Branch Workflow
- **Default Branch:** `main`.
- **Commit Standards:** Use conventional commit messages: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
