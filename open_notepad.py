import tkinter as tk
from tkinter import messagebox
import time
import pyautogui
import webbrowser
import os

# popup first
root = tk.Tk()
root.withdraw()

answer = messagebox.askyesno("Question", "Would you like to continue?")

if answer:
    # open notepad
    os.startfile("notepad.exe")

    time.sleep(1.5)  # wait for notepad to open

    # slow typing effect
    message = "hello :)"

    for char in message:
        pyautogui.write(char)
        time.sleep(0.1)

    # open YouTube after
    webbrowser.open("https://www.youtube.com")

else:
    print("User cancelled")