import os
import sys
import subprocess
import tkinter as tk

class Notifier:
    @staticmethod
    def send(title, message, duration='long'):
        """
        Send a desktop notification.
        """
        system = sys.platform

        if system == 'win32':
            try:
                from win11toast import toast
                toast(title, message, duration=duration)
            except ImportError:
                print(f"[Win Notification] {title}: {message}")

        elif system.startswith('linux'):
            try:
                # Use notify-send (common on most Linux DEs)
                # Ensure message is escaped or safe
                subprocess.Popen(['notify-send', title, message])
            except Exception as e:
                print(f"[Linux Notification Error] {e}")
                print(f"[{title}] {message}")

        else:
            # Fallback for Mac or others
            print(f"[{title}] {message}")

class ScreenInfo:
    @staticmethod
    def get_geometry(root: tk.Tk = None):
        """
        Returns (width, height, x, y) of the virtual screen.
        """
        system = sys.platform

        width, height, x, y = 0, 0, 0, 0

        if system == 'win32':
            try:
                import ctypes
                user32 = ctypes.windll.user32
                user32.SetProcessDPIAware()
                width = user32.GetSystemMetrics(78) # SM_CXVIRTUALSCREEN
                height = user32.GetSystemMetrics(79) # SM_CYVIRTUALSCREEN
                x = user32.GetSystemMetrics(76) # SM_XVIRTUALSCREEN
                y = user32.GetSystemMetrics(77) # SM_YVIRTUALSCREEN
                return width, height, x, y
            except Exception as e:
                print(f"Win32 Geometry Error: {e}")
                # Fallback to tkinter logic below

        # Cross-platform / Linux Fallback
        # This usually returns the geometry of the default screen or combined in some X11 configs
        if root:
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()
            # On Linux, root.winfo_x() usually is 0, but for multi-monitor,
            # we might just want to grab the main screen if we can't get the full virtual one easily without extra deps.
            # Improvement: To get full virtual screen on Linux usually requires xrandr or similar.
            # For "Lite" purposes, we will stick to primary screen or what Tkinter sees.
            return width, height, 0, 0

        return 1920, 1080, 0, 0
