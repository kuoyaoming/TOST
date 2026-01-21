import ollama
import sys
import time
import keyboard
import threading
import queue
import tkinter as tk
from snipper import ScreenSnipper
from ocr_handler import OCRHandler
from win11toast import toast

# Set stdout to handle UTF-8
sys.stdout.reconfigure(encoding='utf-8')

MODEL_NAME = "translategemma"

# Queue for handling main thread UI tasks (since tkinter needs main thread)
ui_queue = queue.Queue()

# Initialize OCR engine
ocr_engine = None

def get_ocr_engine():
    global ocr_engine
    if ocr_engine is None:
        print("正在初始化 OCR 引擎 (Initializing OCR)...")
        ocr_engine = OCRHandler()
    return ocr_engine

def get_translation(text):
    if not text or not text.strip():
        return None

    print(f"\n[識別文字] Detected Text: {text}")
    print("Translating...")
    
    full_prompt = (
        f"Translate the following English text to Traditional Chinese (繁體中文). "
        f"Output ONLY the translation. Do not add any conversational text or explanations.\n\n"
        f"Text: {text}"
    )

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{'role': 'user', 'content': full_prompt}],
            stream=False 
        )
        return response['message']['content']
    except Exception as e:
        print(f"Translation Error: {e}")
        return f"Error: {e}"

def run_translation_thread(img):
    """Running OCR and Translation in background thread"""
    try:
        print("截圖成功，正在辨識... (Processing...)")
        ocr = get_ocr_engine()
        text = ocr.extract_text(img)
        
        if text.strip():
            # Translate
            result = get_translation(text)
            print(f"結果 (Result): {result}")
            
            # Show Notification
            if result:
                toast('翻譯結果 (Translation)', result, duration='long')
        else:
            print("未偵測到文字 (No text detected).")
    except Exception as e:
        print(f"Thread Error: {e}")

def pipeline_task(root):
    """Runs the snipper (Main Thread) then offloads processing."""
    print("\n[Hotkey] Triggered! 準備截圖...")
    
    try:
        # Snipper blocks here using wait_window, but that's what we want for modal selection
        snipper = ScreenSnipper(root)
        img = snipper.run()
        
        if img:
            # Offload heavy OCR/Translation to another thread 
            # so we don't block the main loop (though main loop is hidden, 
            # win11toast or other things might depend on it not being frozen)
            t = threading.Thread(target=run_translation_thread, args=(img,))
            t.start()
        else:
            print("取消截圖 (Scan cancelled).")
            
    except Exception as e:
        print(f"Pipeline Error: {e}")

def hotkey_callback():
    """Callback from keyboard thread. Puts task in queue."""
    ui_queue.put("trigger")

def process_queue(root):
    """Check queue periodically in the main thread"""
    try:
        while True:
            # Non-blocking get
            task = ui_queue.get_nowait()
            if task == "trigger":
                pipeline_task(root)
    except queue.Empty:
        pass
    
    # Schedule next check (100ms)
    root.after(100, process_queue, root)

def main():
    print(f"\n=== Translategemma 背景翻譯神器 (Background Mode) ===")
    print(f"使用模型 (Model): {MODEL_NAME}")
    print("狀態: 等待熱鍵 (Status: Waiting for Hotkey)")
    print("熱鍵 (Hotkey): Shift + Alt + Z")
    print("  -> 觸發截圖 (Trigger Snipper)")
    print("  -> 自動翻譯 (Auto Translate)")
    print("  -> 顯示 Windows 通知 (Show Win11 Notification)")
    print("按 Ctrl+C 結束程式 (Press Ctrl+C to exit)")
    print("-" * 50)
    
    # Check if model exists (Warning only)
    try:
        models = ollama.list()
        available_models = [m.model for m in models.models]
        found = any(MODEL_NAME in m for m in available_models)
        if not found:
            print(f"警告: 找不到模型 '{MODEL_NAME}' (Warning: Model not found).")
            print("請先執行 'setup.bat' 來匯入模型。")
    except:
        pass

    # Register hotkey
    keyboard.add_hotkey('shift+alt+z', hotkey_callback)

    # Setup Persistent Root Window
    root = tk.Tk()
    root.withdraw() # Hide it completely
    
    # Start the queue processor loop
    root.after(100, process_queue, root)
    
    # Start Mainloop
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
