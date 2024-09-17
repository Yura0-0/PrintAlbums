import glob
import json
from pathlib import Path
import os
from tkinter.ttk import Combobox
import fitz  # PyMuPDF
import time
import datetime
from tkinter import *
import shutil
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import win32print
import win32api

# Дизайн окна
root = Tk()
root.title("Печать альбомов v 4.0")
root.geometry("200x200")
# root.resizable(width=False, height=False)

# ipadx = 5  # длина фрейма

frame_1 = Frame()
frame_1.pack(side=LEFT)

label1 = Label(frame_1, width=5, height=3, text='j')
label1.pack(side=LEFT)
root.mainloop()