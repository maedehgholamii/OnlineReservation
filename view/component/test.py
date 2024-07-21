import tkinter as tk
from tkinter import ttk

def set_dark_mode(root):
    # تنظیم رنگ پس‌زمینه و پیش‌زمینه برای تمام ویجت‌های اصلی
    root.tk_setPalette(background='#2e2e2e', foreground='#ffffff', activeBackground='#444444', activeForeground='#ffffff')

    # تنظیم رنگ مخصوص ویجت‌های ttk
    style = ttk.Style(root)
    style.theme_use('default')
    style.configure('TButton', background='#444444', foreground='#ffffff')
    style.configure('TLabel', background='#2e2e2e', foreground='#ffffff')
    style.configure('TEntry', background='#333333', foreground='#ffffff')
    style.configure('TFrame', background='#2e2e2e', foreground='#ffffff')

root = tk.Tk()
root.title("Dark Mode Example")

# اعمال حالت تاریک
set_dark_mode(root)

# ساخت و قرار دادن ویجت‌ها
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="This is a dark mode example")
label.grid(row=0, column=0, padx=5, pady=5)

entry = ttk.Entry(frame)
entry.grid(row=1, column=0, padx=5, pady=5)

button = ttk.Button(frame, text="Click Me")
button.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()
