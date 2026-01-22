import tkinter as tk
from PIL import ImageGrab
import sys
from utils import ScreenInfo

class ScreenSnipper:
    def __init__(self, root):
        self.root = root
        # Use Toplevel to avoid creating multiple Tk instances
        self.window = tk.Toplevel(root)
        
        # Get geometry
        self.screen_width, self.screen_height, self.screen_x, self.screen_y = ScreenInfo.get_geometry(root)

        self.window.geometry(f"{self.screen_width}x{self.screen_height}+{self.screen_x}+{self.screen_y}")
        self.window.overrideredirect(True)

        # Alpha transparency works differently on Windows vs Linux (compositor needed)
        # On Windows, -alpha works great. On Linux, it requires a compositor.
        # If no compositor, it might be black.
        try:
            self.window.attributes("-alpha", 0.3)
        except:
            pass

        self.window.configure(bg="black")
        self.window.attributes("-topmost", True)

        self.canvas = tk.Canvas(self.window, width=self.screen_width, height=self.screen_height, cursor="cross", bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.start_x = None
        self.start_y = None
        self.rect = None
        self.captured_image = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        # Escape to cancel
        self.window.bind("<Escape>", lambda e: self.window.destroy())
        
        # Ensure focus so Escape works
        self.window.focus_force()

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red", width=2)

    def on_move_press(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        
        # Minimize/Destroy before capture to avoid capturing the overlay itself
        self.window.withdraw() 
        # Wait a tiny bit for window to disappear
        self.root.after(100, self.capture_screen, self.start_x, self.start_y, cur_x, cur_y)

    def capture_screen(self, x1, y1, x2, y2):
        # Normalize coordinates
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        
        try:
            # Add screen_x/screen_y offsets
            abs_x1 = int(x1 + self.screen_x)
            abs_y1 = int(y1 + self.screen_y)
            abs_x2 = int(x2 + self.screen_x)
            abs_y2 = int(y2 + self.screen_y)
            
            width = abs_x2 - abs_x1
            height = abs_y2 - abs_y1
            
            if width > 10 and height > 10:
                # all_screens=True is valid for recent Pillow on Windows/macOS.
                # On Linux, it depends on the backend (xdisplay/scrot).
                # To be safe, we just pass the bbox.
                self.captured_image = ImageGrab.grab(bbox=(abs_x1, abs_y1, abs_x2, abs_y2), all_screens=True)
            
        except Exception as e:
            print(f"Capture Error: {e}")
        
        self.window.destroy()

    def run(self):
        self.window.wait_window(self.window)
        return self.captured_image

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    print("Select an area on screen...")
    snipper = ScreenSnipper(root)
    img = snipper.run()
    if img:
        print("Capture successful.")
    else:
        print("Capture cancelled.")
    root.destroy()
