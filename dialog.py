# Paolo Anzani <p.anzani@campus.unimib.it> 10-08-2021
import tkinter as tk
from tkinter import filedialog

# Folder picker dialog GUI

def get_folder():
    root = tk.Tk()
    root.withdraw()

    path = filedialog.askdirectory()
    print(path)

if __name__ == "__main__":
    get_folder()
