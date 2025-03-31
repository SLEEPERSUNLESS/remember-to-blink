import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # if bundle
        base_path = sys._MEIPASS
    else:
        # if script
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def blink():
    if hasattr(blink, "is_open") and blink.is_open:
        eye_label.config(image=eye_closed_tk)
        blink.is_open = False
        root.after(150, blink)  # keep closed for 150ms
    else:
        eye_label.config(image=eye_open_tk)
        blink.is_open = True
        root.after(5000, blink)  # keep open for 5 seconds

root = tk.Tk()
root.title("Blinking Eye Icon")

# center it on the top of the screen
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 128
    window.geometry(f"{width}x{height}+{x}+{y}")

root.configure(bg="white")

try:
    eye_open_pil = Image.open(resource_path("img/eye-open.png"))
    eye_closed_pil = Image.open(resource_path("img/eye-closed.png"))
    
    eye_open_pil = eye_open_pil.resize((80, 80), Image.Resampling.LANCZOS)
    eye_closed_pil = eye_closed_pil.resize((80, 80), Image.Resampling.LANCZOS)
    
    eye_open_tk = ImageTk.PhotoImage(eye_open_pil)
    eye_closed_tk = ImageTk.PhotoImage(eye_closed_pil)
    
    # add label
    eye_label = tk.Label(root, image=eye_open_tk, bg="white")
    eye_label.pack(padx=10, pady=10)
    
    # center the window after adding content
    center_window(root)
    
    # set window properties
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)  # keep it on top
    root.wm_attributes("-transparentcolor", "white")  # transparent background
    
    # init blink state
    blink.is_open = False
    
    blink()
    
    root.mainloop()
    
except Exception as e:
    print(f"Error: {e}")
    root.destroy()