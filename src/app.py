import ollama
import sys
import time
import keyboard
import threading
import queue
import tkinter as tk
from snipper import ScreenSnipper
from ocr_handler import OCRHandler
from utils import Notifier
import pyperclip
from PIL import Image
import pystray
from pystray import MenuItem as item

# Set stdout to handle UTF-8
sys.stdout.reconfigure(encoding='utf-8')

MODEL_NAME = "translategemma"

# Queue for handling main thread UI tasks
ui_queue = queue.Queue()

# Initialize OCR engine
ocr_engine = None

# Global state for icon
icon = None

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
            
            # Copy to clipboard
            try:
                pyperclip.copy(result)
            except Exception:
                pass

            # Show Notification
            if result:
                Notifier.send('翻譯結果 (Translation)', result, duration='long')
        else:
            print("未偵測到文字 (No text detected).")
            Notifier.send('提示', '未偵測到文字 (No text detected)')
    except Exception as e:
        print(f"Thread Error: {e}")

def pipeline_task(root):
    """Runs the snipper (Main Thread) then offloads processing."""
    print("\n[Action] Triggered! 準備截圖...")
    
    try:
        # Snipper blocks here using wait_window
        snipper = ScreenSnipper(root)
        img = snipper.run()
        
        if img:
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
            task = ui_queue.get_nowait()
            if task == "trigger":
                pipeline_task(root)
            elif task == "quit":
                root.quit()
    except queue.Empty:
        pass
    
    # Schedule next check
    root.after(100, process_queue, root)

def create_image():
    # Create a simple icon for the tray
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), color=(50, 50, 50))
    dc = Image.new('RGB', (width-10, height-10), color=(255, 255, 255))
    image.paste(dc, (5, 5))
    return image

def on_quit(icon, item):
    icon.stop()
    ui_queue.put("quit")

def on_snip(icon, item):
    ui_queue.put("trigger")

def setup_tray():
    global icon
    menu = (item('Snip (截圖翻譯)', on_snip), item('Quit (離開)', on_quit))
    icon = pystray.Icon("name", create_image(), "Translategemma", menu)
    icon.run_detached()

def main():
    print(f"\n=== Translategemma 背景翻譯神器 (Background Mode) ===")
    print(f"使用模型 (Model): {MODEL_NAME}")
    print("狀態: 等待熱鍵 (Status: Waiting for Hotkey)")
    print("熱鍵 (Hotkey): Shift + Alt + Z")
    print("  -> 觸發截圖 (Trigger Snipper)")
    print("  -> 自動翻譯 (Auto Translate)")
    print("  -> 顯示通知 (Show Notification)")
    print("  -> 複製到剪貼簿 (Copy to Clipboard)")
    print("System Tray: Right click icon for menu")
    print("-" * 50)
    
    # Check if model exists
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
    try:
        keyboard.add_hotkey('shift+alt+z', hotkey_callback)
    except ImportError:
        # Linux without root might fail here
        print("Warning: Could not register global hotkey (requires root on Linux).")
        print("Use the System Tray icon to trigger.")
    except Exception as e:
        print(f"Hotkey Error: {e}")

    # Setup Persistent Root Window
    root = tk.Tk()
    root.withdraw()
    
    # Start Tray Icon
    setup_tray()

    # Start the queue processor loop
    root.after(100, process_queue, root)
    
    # Start Mainloop
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass
    finally:
        if icon:
            icon.stop()

if __name__ == "__main__":
    main()
