import shutil
import sys
from pathlib import Path
import os
from tkinter.ttk import Combobox
import fitz  # PyMuPDF
import time
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import win32print
import win32api

path_shablon_albums = 'D:\\!!__ПечатьПризыв\\!!АЛЬБОМЫ\\000\\шаблон_альбома.pdf'

mm = []
num_list = 1
dd = {}
mas_foto = []
with open('log.txt', 'r') as log:
    initialdir = log.readline()
    initialdir = initialdir.rstrip()
    print('initialdir = ' + initialdir)

    initialdir_foto = log.readline()
    initialdir_foto = initialdir_foto.rstrip()
    print('initialdir_foto = ' + initialdir_foto)
    print("_____________________________")

initialdir1 = "D:\\!!__ПечатьПризыв"
initialdir_foto1 = "D:\\!!!__АРМИЯ__!!!"


def create_new_window():
    root1 = Tk()
    root1.title("Образец Альбома")
    root1.geometry("1860x440")
    num_priz = combo_priz.get()
    sh_al = combo.get()
    sh = num_priz + '__' + sh_al

    frame = LabelFrame(root1, text=f"Образец Альбома {sh}", font='Helvetica 12 bold')
    frame.pack(ipadx=ipadx)
    frame.pack_propagate(0)
    frame.place(x=10, y=20)
    label_1 = Label(frame, width=430, height=9, text='')
    label_1.grid(row=1, column=0, padx=2, pady=2)

    frame_niz = LabelFrame(root1, text=f"Образец Альбома {sh}", font='Helvetica 12 bold')
    frame_niz.pack(ipadx=ipadx)
    frame_niz.pack_propagate(0)
    frame_niz.place(x=10, y=200)
    label_2 = Label(frame_niz, width=430, height=9, text='')
    label_2.grid(row=2, column=0, padx=2, pady=2)

    for i, st in enumerate(dd.values(), 1):

        if i <= 10:  # В какой фрейм вставлять фотки (верх, низ)
            frame = frame
        else:
            frame = frame_niz

        if os.path.isdir(st):  # если папка то...
            p = Path(st)
            pp = p.glob('*.jpg')
            for r in pp:
                our_img = Image.open(r)
                our_img = our_img.resize((180, 140), Image.Resampling.LANCZOS)
                our_img = ImageTk.PhotoImage(our_img, master=root1)
                our_lable = Label(frame, image=our_img)
                our_lable.image = our_img
                our_lable.pack(side=LEFT)
                break

        elif os.path.isfile(st):  # если просто фото
            our_img = Image.open(st)
            our_img = our_img.resize((180, 140), Image.Resampling.LANCZOS)
            our_img = ImageTk.PhotoImage(our_img, master=root1)
            our_lable = Label(frame, image=our_img)
            our_lable.image = our_img
            our_lable.pack(side=LEFT)

        else:  # если ни фото ни папка...
            our_img = Image.open(r'pusto.jpg')
            our_img = our_img.resize((180, 140), Image.Resampling.LANCZOS)
            our_img = ImageTk.PhotoImage(our_img, master=root1)
            our_lable = Label(frame, image=our_img)
            our_lable.image = our_img
            our_lable.pack(side=LEFT)


def restart():
    mm.clear()
    for ii in range(1, 41):
        knopki('', ii)


def add_img(arg):
    if os.path.isdir(arg):  # если папка то...
        p = Path(arg)
        pp = p.glob('*.jpg')
        for r in pp:
            our_img = Image.open(r)
            our_img = our_img.resize((85, 65), Image.Resampling.LANCZOS)
            our_img = ImageTk.PhotoImage(our_img)
            our_lable = Label(image=our_img)
            our_lable.image = our_img
            mas_foto.append(our_lable)
            break
    elif os.path.isfile(arg):  # если просто фото
        our_img = Image.open(arg)
        our_img = our_img.resize((85, 65), Image.Resampling.LANCZOS)
        our_img = ImageTk.PhotoImage(our_img)
        our_lable = Label(image=our_img)
        our_lable.image = our_img
    else:  # если ни фото ни папка...
        our_lable = add_img(r'pusto.jpg')
        our_lable.place(x=5, y=180)

    return our_lable


def save_papka():
    global initialdir, initialdir1

    initialdir = filedialog.askdirectory(initialdir=initialdir1)
    initialdir1 = initialdir


def save_foto_dir():
    global initialdir_foto, initialdir_foto1

    initialdir_foto = filedialog.askdirectory(initialdir=initialdir_foto1)
    initialdir_foto1 = initialdir_foto


def knopki(input_dir, arg):
    if arg == 1:
        label1.config(text=input_dir)
        dd[1] = input_dir  # добавление в словарь
        if not input_dir:
            label1.config(text='путь к файлу или папке')
            del dd[1]
            our_lable = add_img(r'pusto.jpg')  # отображение фотки
            our_lable.place(x=5, y=5)
            bt1.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)  # отображение фотки
        our_lable.place(x=5, y=5)
        bt1.config(bg='grey')  # менять цвет кнопки

    if arg == 3:
        label2.config(text=input_dir)
        dd[2] = input_dir
        if not input_dir:
            label2.config(text='путь к файлу или папке')
            del dd[2]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=5)
            bt3.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=5)
        bt3.config(bg='grey')

    if arg == 5:
        label3.config(text=input_dir)
        dd[3] = input_dir
        if not input_dir:
            label3.config(text='путь к файлу или папке')
            del dd[3]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=93)
            bt5.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=93)
        bt5.config(bg='grey')

    if arg == 7:
        label4.config(text=input_dir)
        dd[4] = input_dir
        if not input_dir:
            label4.config(text='путь к файлу или папке')
            del dd[4]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=93)
            bt7.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=93)
        bt7.config(bg='grey')

    if arg == 9:
        label5.config(text=input_dir)
        dd[5] = input_dir
        if not input_dir:
            label5.config(text='путь к файлу или папке')
            del dd[5]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=180)
            bt9.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=180)
        bt9.config(bg='grey')

    if arg == 11:
        label6.config(text=input_dir)
        dd[6] = input_dir
        if not input_dir:
            label6.config(text='путь к файлу или папке')
            del dd[6]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=180)
            bt11.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=180)
        bt11.config(bg='grey')

    if arg == 13:
        label7.config(text=input_dir)
        dd[7] = input_dir
        if not input_dir:
            label7.config(text='путь к файлу или папке')
            del dd[7]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=265)
            bt13.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=265)
        bt13.config(bg='grey')

    if arg == 15:
        label8.config(text=input_dir)
        dd[8] = input_dir
        if not input_dir:
            label8.config(text='путь к файлу или папке')
            del dd[8]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=265)
            bt15.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=265)
        bt15.config(bg='grey')

    if arg == 17:
        label9.config(text=input_dir)
        dd[9] = input_dir
        if not input_dir:
            label9.config(text='путь к файлу или папке')
            del dd[9]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=350)
            bt17.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=350)
        bt17.config(bg='grey')

    if arg == 19:
        label10.config(text=input_dir)
        dd[10] = input_dir
        if not input_dir:
            label10.config(text='путь к файлу или папке')
            del dd[10]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=350)
            bt19.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=350)
        bt19.config(bg='grey')

    if arg == 21:
        label11.config(text=input_dir)
        dd[11] = input_dir
        if not input_dir:
            label11.config(text='путь к файлу или папке')
            del dd[11]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=435)
            bt21.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=435)
        bt21.config(bg='grey')

    if arg == 23:
        label12.config(text=input_dir)
        dd[12] = input_dir
        if not input_dir:
            label12.config(text='путь к файлу или папке')
            del dd[12]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=435)
            bt23.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=435)
        bt23.config(bg='grey')

    if arg == 25:
        label13.config(text=input_dir)
        dd[13] = input_dir
        if not input_dir:
            label13.config(text='путь к файлу или папке')
            del dd[13]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=520)
            bt25.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=520)
        bt25.config(bg='grey')

    if arg == 27:
        label14.config(text=input_dir)
        dd[14] = input_dir
        if not input_dir:
            label14.config(text='путь к файлу или папке')
            del dd[14]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=520)
            bt27.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=520)
        bt27.config(bg='grey')

    if arg == 29:
        label15.config(text=input_dir)
        dd[15] = input_dir
        if not input_dir:
            label15.config(text='путь к файлу или папке')
            del dd[15]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=605)
            bt29.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=605)
        bt29.config(bg='grey')

    if arg == 31:
        label16.config(text=input_dir)
        dd[16] = input_dir
        if not input_dir:
            label16.config(text='путь к файлу или папке')
            del dd[16]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=605)
            bt31.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=605)
        bt31.config(bg='grey')

    if arg == 33:
        label17.config(text=input_dir)
        dd[17] = input_dir
        if not input_dir:
            label17.config(text='путь к файлу или папке')
            del dd[17]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=690)
            bt33.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=690)
        bt33.config(bg='grey')

    if arg == 35:
        label18.config(text=input_dir)
        dd[18] = input_dir
        if not input_dir:
            label18.config(text='путь к файлу или папке')
            del dd[18]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=690)
            bt35.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=690)
        bt35.config(bg='grey')

    if arg == 37:
        label19.config(text=input_dir)
        dd[19] = input_dir
        if not input_dir:
            label19.config(text='путь к файлу или папке')
            del dd[19]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=775)
            bt37.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=775)
        bt37.config(bg='grey')

    if arg == 39:
        label20.config(text=input_dir)
        dd[20] = input_dir
        if not input_dir:
            label20.config(text='путь к файлу или папке')
            del dd[20]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=775)
            bt39.config(bg='#f0f0f0')
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=775)
        bt39.config(bg='grey')

    if arg == 2:
        label1.config(text=input_dir)
        dd[1] = input_dir
        if not input_dir:
            label1.config(text='путь к файлу или папке')
            del dd[1]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=5)
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=5)
        bt1.config(bg='#f0f0f0')

    if arg == 4:
        label2.config(text=input_dir)
        dd[2] = input_dir
        if not input_dir:
            label2.config(text='путь к файлу или папке')
            del dd[2]
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=5)
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=5)
        bt3.config(bg='#f0f0f0')

    if arg == 6:
        label3.config(text=input_dir)
        dd[3] = input_dir
        if not input_dir:
            label3.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=93)
            del dd[3]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=93)
        bt5.config(bg='#f0f0f0')

    if arg == 8:

        label4.config(text=input_dir)
        dd[4] = input_dir
        if not input_dir:
            label4.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=93)
            del dd[4]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=93)
        bt7.config(bg='#f0f0f0')

    if arg == 10:
        label5.config(text=input_dir)
        dd[5] = input_dir
        if not input_dir:
            label5.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=180)
            del dd[5]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=180)
        bt9.config(bg='#f0f0f0')

    if arg == 12:
        label6.config(text=input_dir)
        dd[6] = input_dir
        if not input_dir:
            label6.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=180)
            del dd[6]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=180)
        bt11.config(bg='#f0f0f0')

    if arg == 14:
        label7.config(text=input_dir)
        dd[7] = input_dir
        if not input_dir:
            label7.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=265)
            del dd[7]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=265)
        bt13.config(bg='#f0f0f0')

    if arg == 16:
        label8.config(text=input_dir)
        dd[8] = input_dir
        if not input_dir:
            label8.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=265)
            del dd[8]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=265)
        bt15.config(bg='#f0f0f0')

    if arg == 18:
        label9.config(text=input_dir)
        dd[9] = input_dir
        if not input_dir:
            label9.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=350)
            del dd[9]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=350)
        bt17.config(bg='#f0f0f0')

    if arg == 20:
        label10.config(text=input_dir)
        dd[10] = input_dir
        if not input_dir:
            label10.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=350)
            del dd[10]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=350)
        bt19.config(bg='#f0f0f0')

    if arg == 22:
        label11.config(text=input_dir)
        dd[11] = input_dir
        if not input_dir:
            label11.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=435)
            del dd[11]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=435)
        bt21.config(bg='#f0f0f0')

    if arg == 24:
        label12.config(text=input_dir)
        dd[12] = input_dir
        if not input_dir:
            label12.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=435)
            del dd[12]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=435)
        bt23.config(bg='#f0f0f0')

    if arg == 26:
        label13.config(text=input_dir)
        dd[13] = input_dir
        if not input_dir:
            label13.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=520)
            del dd[13]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=520)
        bt25.config(bg='#f0f0f0')

    if arg == 28:
        label14.config(text=input_dir)
        dd[14] = input_dir
        if not input_dir:
            label14.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=520)
            del dd[14]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=520)
        bt27.config(bg='#f0f0f0')

    if arg == 30:
        label15.config(text=input_dir)
        dd[15] = input_dir
        if not input_dir:
            label15.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=605)
            del dd[15]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=605)
        bt29.config(bg='#f0f0f0')

    if arg == 32:
        label16.config(text=input_dir)
        dd[16] = input_dir
        if not input_dir:
            label16.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=605)
            del dd[16]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=605)
        bt31.config(bg='#f0f0f0')

    if arg == 34:
        label17.config(text=input_dir)
        dd[17] = input_dir
        if not input_dir:
            label17.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=690)
            del dd[17]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=690)
        bt33.config(bg='#f0f0f0')

    if arg == 36:
        label18.config(text=input_dir)
        dd[18] = input_dir
        if not input_dir:
            label18.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=690)
            del dd[18]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=690)
        bt35.config(bg='#f0f0f0')

    if arg == 38:
        label19.config(text=input_dir)
        dd[19] = input_dir
        if not input_dir:
            label19.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=5, y=775)
            del dd[19]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=5, y=775)
        bt37.config(bg='#f0f0f0')

    if arg == 40:
        label20.config(text=input_dir)
        dd[20] = input_dir
        if not input_dir:
            label20.config(text='путь к файлу или папке')
            our_lable = add_img(r'pusto.jpg')
            our_lable.place(x=1035, y=775)
            del dd[20]
            return input_dir
        our_lable = add_img(input_dir)
        our_lable.place(x=1035, y=775)
        bt39.config(bg='#f0f0f0')

    # print(dd)


def input_path(arg):
    global our_lable

    if arg == 1:
        input_dir1 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir1, arg)
    if arg == 3:
        input_dir3_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir3_ob, arg)
    if arg == 5:
        input_dir5 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir5, arg)
    if arg == 7:
        input_dir7_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir7_ob, arg)
    if arg == 9:
        input_dir9 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir9, arg)
    if arg == 11:
        input_dir11_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir11_ob, arg)
    if arg == 13:
        input_dir13 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir13, arg)
    if arg == 15:
        input_dir15_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir15_ob, arg)
    if arg == 17:
        input_dir17 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir17, arg)
    if arg == 19:
        input_dir19_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir19_ob, arg)
    if arg == 21:
        input_dir21 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir21, arg)
    if arg == 23:
        input_dir23_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir23_ob, arg)
    if arg == 25:
        input_dir25 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir25, arg)
    if arg == 27:
        input_dir27_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir27_ob, arg)
    if arg == 29:
        input_dir29 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir29, arg)
    if arg == 31:
        input_dir31_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir31_ob, arg)
    if arg == 33:
        input_dir33 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir33, arg)
    if arg == 35:
        input_dir35_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir35_ob, arg)
    if arg == 37:
        input_dir37 = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir37, arg)
    if arg == 39:
        input_dir39_ob = filedialog.askdirectory(initialdir=initialdir)
        knopki(input_dir39_ob, arg)

    # фото
    filetypes = (("Изображение", "*.jpg *.gif *.png"),)

    if arg == 2:
        input_file2 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file2, arg)
    if arg == 4:
        input_file4_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file4_ob, arg)
    if arg == 6:
        input_file6 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file6, arg)
    if arg == 8:
        input_file8_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file8_ob, arg)
    if arg == 10:
        input_file10 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file10, arg)
    if arg == 12:
        input_file12_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file12_ob, arg)
    if arg == 14:
        input_file14 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file14, arg)
    if arg == 16:
        input_file16_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file16_ob, arg)
    if arg == 18:
        input_file18 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file18, arg)
    if arg == 20:
        input_file20_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file20_ob, arg)
    if arg == 22:
        input_file22 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file22, arg)
    if arg == 24:
        input_file24_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file24_ob, arg)
    if arg == 26:
        input_file26 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file26, arg)
    if arg == 28:
        input_file28_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file28_ob, arg)
    if arg == 30:
        input_file30 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file30, arg)
    if arg == 32:
        input_file32_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file32_ob, arg)
    if arg == 34:
        input_file34 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file34, arg)
    if arg == 36:
        input_file36_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file36_ob, arg)
    if arg == 38:
        input_file38 = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file38, arg)
    if arg == 40:
        input_file40_ob = filedialog.askopenfilename(initialdir=initialdir_foto, filetypes=filetypes)
        knopki(input_file40_ob, arg)

    # print(dd)


def append_mm(arg):
    m = []
    p = Path(arg)
    pp = p.glob('*.jpg')
    for o in pp:
        m.append(o)
    mm.append(m)


def printer(path_save_pdf):
    global count
    # win32print.SetDefaultPrinter('C1100_Печать Альбомов')
    PRINTER_DEFAULTS = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}

    pHandle = win32print.OpenPrinter('KONICA MINOLTA C14000Series PS', PRINTER_DEFAULTS)
    # pHandle = win32print.OpenPrinter('KONICA MINOLTA C1070/C1060PS', PRINTER_DEFAULTS)
    properties = win32print.GetPrinter(pHandle, 2)
    pDevModeObj = properties["pDevMode"]

    if count == 2:
        pDevModeObj.Copies = int(kol_vo_listov)
    else:
        pDevModeObj.Copies = 1

    win32print.SetPrinter(pHandle, 2, properties, 0)
    win32api.ShellExecute(0, 'print', path_save_pdf, '.', '.', 0)

    # время засыпания указать в ручную в окошке
    times = int(time_sleep.get())
    kol_vo_min = kol_vo_pages
    if times == 0:
        if kol_vo_pages < 30:
            kol_vo_min = 20
        elif kol_vo_pages > 50 and count == 2:
            kol_vo_min = 20
        time.sleep(kol_vo_min)
        print(kol_vo_min)
    else:
        time.sleep(times)

    pDevModeObj.Copies = 1
    win32print.SetPrinter(pHandle, 2, properties, 0)

    count = 0

    return path_save_pdf


def foto_foto():
    global num_list, kol_vo_listov, count, ved, kol_vo_pages, na_num_vig

    # kol_vo_jpg = 1  # Количество фоток в папке
    for index in mm:
        kol_vo_jpg = len(index)
        if kol_vo_jpg > 1:
            d = index[0]  # вытаскиваем номер ведомости
            d = str(d)
            dd = d.split("\\")[-3]
            ved = dd.split('_')[0]  # номер ведомости
            print(f"{kol_vo_jpg} - количество jpg в посылке")
            break
        else:
            ved = '000'

    if kol_vo_jpg % 2 == 0:
        kol_vo_pages = kol_vo_jpg
    else:
        kol_vo_pages = kol_vo_jpg + 1

    kol_vo_listov = kol_vo_pages // 2
    kol_vo_listov = round(kol_vo_listov)
    print(f'{kol_vo_listov} - количество листов в pdf')
    print(20 * '#')

    count = 0
    for i_index, index in enumerate(mm, 1):

        kol_vo_jpg = len(index)
        print(f'{i_index} - проход')

        if i_index % 2 == 0:
            pages = 1  # оборот
        else:
            pdf = fitz.open(path_shablon_albums)
            for pages in range(1, kol_vo_pages):
                pdf.new_page(width=808.1, height=1133.8)
            pages = 0  # лицо

        # Юра 1
        if kol_vo_jpg > 1:
            count = 0

            verx = index[:kol_vo_listov]
            niz = index[kol_vo_listov:]
            print('verx - ' + str(verx))
            print('niz - ' + str(niz))

            # определить позицию (верх) Юра 1
            image_rectangle = fitz.Rect(0, 0, 808, 567.4)
            for jpg in verx:
                page = pdf[pages]
                page.insert_image(image_rectangle, filename=jpg)  # добавить изображение в pdf
                pages += 2

                if kol_vo_pages <= pages:
                    if i_index % 2 == 0:
                        pages = 1  # оборот
                    else:
                        pages = 0  # лицо

            # определить позицию (низ) Юра 1
            image_rectangle = fitz.Rect(0, 567, 808, 1135)
            for jpg in niz:
                page = pdf[pages]
                page.insert_image(image_rectangle, filename=jpg)  # добавить изображение в pdf
                pages += 2
                if kol_vo_jpg <= pages:
                    break

        # один лист !!!
        if kol_vo_jpg == 1:

            count = count + 1

            # определить позицию (верх-низ) один лист
            for jpg in index:
                for i in range(0, kol_vo_pages):
                    page = pdf[pages]
                    image_rectangle = fitz.Rect(0, 0, 808, 567.5)
                    page.insert_image(image_rectangle, filename=jpg)  # добавить изображение в pdf верх
                    image_rectangle = fitz.Rect(0, 567, 808, 1135)
                    page.insert_image(image_rectangle, filename=jpg)  # добавить изображение в pdf низ
                    pages += 2
                    if kol_vo_pages <= pages:
                        pages = 1
                        break

        # save_pdf
        if i_index % 2 == 0:

            try:
                path_save_pdf = f'd:\\!!__ПечатьПризыв\\!!АЛЬБОМЫ\\__{vig}_№_{ved}___00{num_list}лист.pdf'

                if count == 2:
                    if kol_vo_listov > 1:
                        _list = [0, 1]
                        pdf.select(_list)

                pdf.save(path_save_pdf)
                time.sleep(5)
                pdf.close()
                print(f'[INFO] __{vig}_№_{ved}___00{num_list}_save_pdf_ок')

                # отправка в печать
                if ismarried_print.get():
                    printer(path_save_pdf)

                num_list = num_list + 1
                count = 0

            except:
                print('**[ERROR]** открыт pdf либо проблема с именем файла')

    print("********** [INFO] Все готово!!! **********")
    print('__________________________________________')
    win32print.SetDefaultPrinter('KONICA MINOLTA C14000Series PS')
    # win32print.SetDefaultPrinter('KONICA MINOLTA C1070/C1060PS')


def proverka_verstki():
    # проверка верстальщиков, количество jpg в папках
    proverka = set()
    for t in mm:
        ss = len(t)
        proverka.add(ss)

    print(f'*[INFO]* - количество jpg в папках: {proverka}')

    if len(proverka) > 2:
        print('********** [ERROR-988] количестов фоток в папках не совпадают!! **********')
        messagebox.showinfo('Предупреждение', 'количестов фоток в папках не совпадают')
        sys.exit()


def zamena_vedomosti():
    global na_num_ved
    q = dd.values()
    # print(dd)
    count_arg = 1
    for t, r in enumerate(q, 1):

        if "Юра " in r:

            s_num_ved = r.split('/')[-2]

            if not ismarried_number_vedomosti.get():
                na_num_ved = zamena_na.get()

            if not na_num_ved == '':
                r = r.replace(f"{s_num_ved}", f"{na_num_ved}_A")
                dd[t] = r
                try:
                    knopki(r, count_arg)
                except:
                    pass

            # print(dd)
        count_arg = count_arg + 2
    return dd


def zamena_vigryzki():
    global na_num_ved
    q = dd.values()
    # print(dd)
    count_arg = 1
    for t, r in enumerate(q, 1):
        if "Юра " in r:

            s_num_vig = r.split('/')[-3]
            na_num_vig = zamena_na_vig.get()

            if not na_num_vig == '':
                r = r.replace(f"{s_num_vig}", f"Выгрузка {na_num_vig}")
                dd[t] = r
                try:
                    knopki(r, count_arg)
                except:
                    pass

            # print(dd)
        count_arg = count_arg + 2
    return dd


def shablon():
    num_priz = combo_priz.get()
    sh_al = combo.get()
    sh = num_priz + '__' + sh_al

    # num_priz = sh.split('__')[0]
    path = f'C:\\Users\\Yurius\\PycharmProjects\\PrintAlbums\\{num_priz}__шаблоны\\{sh}.txt'
    if os.path.isfile(path):
        with open(path, 'r') as shablon:
            for st in shablon:
                st = st.strip()
                st = st.split(' ', 1)
                knopki(st[1], int(st[0]))
    else:
        messagebox.showinfo('Предупреждение', f'{sh} нет макета')


def sbor_bez_podborki():

    folder = f"D:\\!!__ПечатьПризыв\\!!АЛЬБОМЫ\\sbor_bez_podborki\\"
    if len(folder) > 0:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)

            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    for k, z in dd.items():

        if os.path.isfile(z):
            path_jpg_pdf = z[:-7]
            # print(path_jpg_pdf)
            break

    doc = fitz.open()
    for j in os.listdir(path_jpg_pdf):

        if j.endswith(".jpg") or j.endswith("JPG"):
            file_path = os.path.join(path_jpg_pdf, j)
            picture = fitz.open(file_path)
            pdfbytes = picture.convert_to_pdf()
            imgpdf = fitz.open("pdf", pdfbytes)
            doc.insert_pdf(imgpdf)
    doc.save("some.pdf")
    doc.close()

    for k, z in dd.items():

        if os.path.isfile(z):
            continue
        else:
            list_jpg = os.listdir(z)
            break

    for lj in list_jpg:
        pdf = fitz.open("some.pdf")
        countt = -1
        for k, z in dd.items():
            countt = countt + 1

            if os.path.isfile(z):
                continue
            else:
                file_path_ = os.path.join(z, lj)

                # вставка фоток из массива
                image_rectangle = fitz.Rect(0, 0, 808, 565)

                page = pdf[countt]
                page.insert_image(image_rectangle, filename=file_path_)

        pdf.save(f"D:\\!!__ПечатьПризыв\\!!АЛЬБОМЫ\\sbor_bez_podborki\\{lj}.pdf")
        pdf.close()


def start():

    with open('log.txt', 'w') as log:
        log.write(initialdir + '\n')
        log.write(initialdir_foto + '\n')

    global num_list, vig

    mm.clear()
    num_list = 1

    messagebox.showinfo('Предупреждение', 'Закройте все pdf!')

    vig = zamena_na_vig.get()

    if ismarried_number_vedomosti.get():

        veds = vedomosti_and_id.get()
        veds = [str(veds) for veds in veds.split()]
        print(veds)

        global na_num_ved
        for na_num_ved in veds:

            mm.clear()
            num_list = 1

            zamena_vedomosti()

            d = sorted(dd.items(), key=lambda x: x[0])
            ddd = dict(d)

            # Добавляем массив в многомерный массив (mm)
            for q in ddd.values():
                if os.path.isfile(q):
                    mm.append([q])
                else:
                    append_mm(q)

            print(mm)
            print(zamena_na)

            proverka_verstki()

            foto_foto()

    else:

        d = sorted(dd.items(), key=lambda x: x[0])
        ddd = dict(d)

        # Добавляем массив в многомерный массив (mm)
        for q in ddd.values():
            if os.path.isfile(q):
                mm.append([q])
            else:
                append_mm(q)

        # print(mm)
        # print(ddd)

        proverka_verstki()

        if ismarried_bez_podbora.get():
            sbor_bez_podborki()
        else:
            foto_foto()

    messagebox.showinfo('Предупреждение', 'Все готово!!!')


# Дизайн окна
root = Tk()
root.title("Печать альбомов v 4.3")
root.geometry("1150x980")
root.resizable(width=False, height=False)

ipadx = 200  # длина фрейма

frame_1 = LabelFrame(text="1-лист", font='Helvetica 9 bold')
frame_1.pack(ipadx=ipadx)
frame_1.pack_propagate(0)

bt1 = Button(frame_1, text='1папка', width=8, height=1, command=lambda: input_path(1))
bt1.grid(row=0, column=0, padx=2, pady=2)
bt2 = Button(frame_1, text='2фото', width=8, height=1, command=lambda: input_path(2))
bt2.grid(row=1, column=0, padx=2, pady=2)
label1 = Label(frame_1, width=50, height=2, text='путь к файлу или папки')
label1.grid(row=0, column=1)

bt3 = Button(frame_1, text='3папка_об.', width=9, height=1, command=lambda: input_path(3))
bt3.grid(row=0, column=6, padx=2, pady=2)
bt4 = Button(frame_1, text='4фото_об.', width=9, height=1, command=lambda: input_path(4))
bt4.grid(row=1, column=6, padx=2, pady=2)
label2 = Label(frame_1, width=50, height=2, text='путь к файлу или папки')
label2.place(x=500, y=3)

frame_2 = LabelFrame(text="2-лист", font='Helvetica 9 bold')
frame_2.pack(ipadx=ipadx)
frame_2.pack_propagate(0)

bt5 = Button(frame_2, text='5папка', width=8, height=1, command=lambda: input_path(5))
bt5.grid(row=0, column=0, padx=2, pady=2)
bt6 = Button(frame_2, text='6фото', width=8, height=1, command=lambda: input_path(6))
bt6.grid(row=1, column=0, padx=2, pady=2)
label3 = Label(frame_2, width=50, height=2, text='путь к файлу или папки')
label3.grid(row=0, column=1)

bt7 = Button(frame_2, text='7папка_об.', width=9, height=1, command=lambda: input_path(7))
bt7.grid(row=0, column=6, padx=2, pady=2)
bt8 = Button(frame_2, text='8фото_об.', width=9, height=1, command=lambda: input_path(8))
bt8.grid(row=1, column=6, padx=2, pady=2)
label4 = Label(frame_2, width=50, height=2, text='путь к файлу или папки')
label4.place(x=500, y=3)

frame_3 = LabelFrame(text="3-лист", font='Helvetica 9 bold')
frame_3.pack(ipadx=ipadx)

bt9 = Button(frame_3, text='9папка', width=8, height=1, command=lambda: input_path(9))
bt9.grid(row=0, column=0, padx=2, pady=2)
bt10 = Button(frame_3, text='10фото', width=8, height=1, command=lambda: input_path(10))
bt10.grid(row=1, column=0, padx=2, pady=2)
label5 = Label(frame_3, width=50, height=2, text='путь к файлу или папки')
label5.grid(row=0, column=1)

bt11 = Button(frame_3, text='11папка_об.', width=9, height=1, command=lambda: input_path(11))
bt11.grid(row=0, column=6, padx=2, pady=2)
bt12 = Button(frame_3, text='12фото_об.', width=9, height=1, command=lambda: input_path(12))
bt12.grid(row=1, column=6, padx=2, pady=2)
label6 = Label(frame_3, width=50, height=2, text='путь к файлу или папки')
label6.place(x=500, y=3)

frame_4 = LabelFrame(text="4-лист", font='Helvetica 9 bold')
frame_4.pack(ipadx=ipadx)

bt13 = Button(frame_4, text='13папка', width=8, height=1, command=lambda: input_path(13))
bt13.grid(row=0, column=0, padx=2, pady=2)
bt14 = Button(frame_4, text='14фото', width=8, height=1, command=lambda: input_path(14))
bt14.grid(row=1, column=0, padx=2, pady=2)
label7 = Label(frame_4, width=50, height=2, text='путь к файлу или папки')
label7.grid(row=0, column=1)

bt15 = Button(frame_4, text='15папка_об.', width=9, height=1, command=lambda: input_path(15))
bt15.grid(row=0, column=6, padx=2, pady=2)
bt16 = Button(frame_4, text='16фото_об.', width=9, height=1, command=lambda: input_path(16))
bt16.grid(row=1, column=6, padx=2, pady=2)
label8 = Label(frame_4, width=50, height=2, text='путь к файлу или папки')
label8.place(x=500, y=3)

frame_5 = LabelFrame(text="5-лист", font='Helvetica 9 bold')
frame_5.pack(ipadx=ipadx)

bt17 = Button(frame_5, text='17папка', width=8, height=1, command=lambda: input_path(17))
bt17.grid(row=0, column=0, padx=2, pady=2)
bt18 = Button(frame_5, text='18фото', width=8, height=1, command=lambda: input_path(18))
bt18.grid(row=1, column=0, padx=2, pady=2)
label9 = Label(frame_5, width=50, height=2, text='путь к файлу или папки')
label9.grid(row=0, column=1)

bt19 = Button(frame_5, text='19папка_об.', width=9, height=1, command=lambda: input_path(19))
bt19.grid(row=0, column=6, padx=2, pady=2)
bt20 = Button(frame_5, text='20фото_об.', width=9, height=1, command=lambda: input_path(20))
bt20.grid(row=1, column=6, padx=2, pady=2)
label10 = Label(frame_5, width=50, height=2, text='путь к файлу или папки')
label10.place(x=500, y=3)

frame_6 = LabelFrame(text="6-лист", font='Helvetica 9 bold')
frame_6.pack(ipadx=ipadx)

bt21 = Button(frame_6, text='21папка', width=8, height=1, command=lambda: input_path(21))
bt21.grid(row=0, column=0, padx=2, pady=2)
bt22 = Button(frame_6, text='22фото', width=8, height=1, command=lambda: input_path(22))
bt22.grid(row=1, column=0, padx=2, pady=2)
label11 = Label(frame_6, width=50, height=2, text='путь к файлу или папки')
label11.grid(row=0, column=1)

bt23 = Button(frame_6, text='23папка_об.', width=9, height=1, command=lambda: input_path(23))
bt23.grid(row=0, column=6, padx=2, pady=2)
bt24 = Button(frame_6, text='24фото_об.', width=9, height=1, command=lambda: input_path(24))
bt24.grid(row=1, column=6, padx=2, pady=2)
label12 = Label(frame_6, width=50, height=2, text='путь к файлу или папки')
label12.place(x=500, y=3)

frame_7 = LabelFrame(text="7-лист", font='Helvetica 9 bold')
frame_7.pack(ipadx=ipadx)

bt25 = Button(frame_7, text='25папка', width=8, height=1, command=lambda: input_path(25))
bt25.grid(row=0, column=0, padx=2, pady=2)
bt26 = Button(frame_7, text='26фото', width=8, height=1, command=lambda: input_path(26))
bt26.grid(row=1, column=0, padx=2, pady=2)
label13 = Label(frame_7, width=50, height=2, text='путь к файлу или папки')
label13.grid(row=0, column=1)

bt27 = Button(frame_7, text='27папка_об.', width=9, height=1, command=lambda: input_path(27))
bt27.grid(row=0, column=6, padx=2, pady=2)
bt28 = Button(frame_7, text='28фото_об.', width=9, height=1, command=lambda: input_path(28))
bt28.grid(row=1, column=6, padx=2, pady=2)
label14 = Label(frame_7, width=50, height=2, text='путь к файлу или папки')
label14.place(x=500, y=3)

frame_8 = LabelFrame(text="8-лист", font='Helvetica 9 bold')
frame_8.pack(ipadx=ipadx)

bt29 = Button(frame_8, text='29папка', width=8, height=1, command=lambda: input_path(29))
bt29.grid(row=0, column=0, padx=2, pady=2)
bt30 = Button(frame_8, text='30фото', width=8, height=1, command=lambda: input_path(30))
bt30.grid(row=1, column=0, padx=2, pady=2)
label15 = Label(frame_8, width=50, height=2, text='путь к файлу или папки')
label15.grid(row=0, column=1)

bt31 = Button(frame_8, text='31папка_об.', width=9, height=1, command=lambda: input_path(31))
bt31.grid(row=0, column=6, padx=2, pady=2)
bt32 = Button(frame_8, text='32фото_об.', width=9, height=1, command=lambda: input_path(32))
bt32.grid(row=1, column=6, padx=2, pady=2)
label16 = Label(frame_8, width=50, height=2, text='путь к файлу или папки')
label16.place(x=500, y=3)

frame_9 = LabelFrame(text="9-лист", font='Helvetica 9 bold')
frame_9.pack(ipadx=ipadx)

bt33 = Button(frame_9, text='33папка', width=8, height=1, command=lambda: input_path(33))
bt33.grid(row=0, column=0, padx=2, pady=2)
bt34 = Button(frame_9, text='34фото', width=8, height=1, command=lambda: input_path(34))
bt34.grid(row=1, column=0, padx=2, pady=2)
label17 = Label(frame_9, width=50, height=2, text='путь к файлу или папки')
label17.grid(row=0, column=1)

bt35 = Button(frame_9, text='35папка_об.', width=9, height=1, command=lambda: input_path(35))
bt35.grid(row=0, column=6, padx=2, pady=2)
bt36 = Button(frame_9, text='36фото_об.', width=9, height=1, command=lambda: input_path(36))
bt36.grid(row=1, column=6, padx=2, pady=2)
label18 = Label(frame_9, width=50, height=2, text='путь к файлу или папки')
label18.place(x=500, y=3)

frame_10 = LabelFrame(text="10-лист", font='Helvetica 9 bold')
frame_10.pack(ipadx=ipadx)

bt37 = Button(frame_10, text='37папка', width=8, height=1, command=lambda: input_path(37))
bt37.grid(row=0, column=0, padx=2, pady=2)
bt38 = Button(frame_10, text='38фото', width=8, height=1, command=lambda: input_path(38))
bt38.grid(row=1, column=0, padx=2, pady=2)
label19 = Label(frame_10, width=50, height=2, text='путь к файлу или папки')
label19.grid(row=0, column=1)

bt39 = Button(frame_10, text='39папка_об.', width=9, height=1, command=lambda: input_path(39))
bt39.grid(row=0, column=6, padx=2, pady=2)
bt40 = Button(frame_10, text='40фото_об.', width=9, height=1, command=lambda: input_path(40))
bt40.grid(row=1, column=6, padx=2, pady=2)
label20 = Label(frame_10, width=50, height=2, text='путь к файлу или папки')
label20.place(x=500, y=3)

btn_start = Button(text='СТАРТ', width=11, height=3, font='Helvetica 11 bold', bg="green", fg="black", command=start)
btn_start.place(x=1000, y=860)

frame_z = LabelFrame(text="z", font='Helvetica 9 bold')
frame_z.pack(ipadx=ipadx)

btn_zamena = Button(text='Заменить \nведомость на:', width=12, height=2, command=zamena_vedomosti)
btn_zamena.place(x=50, y=864)

zamena_na = StringVar()
zamena_na = Entry(textvariable=zamena_na)
zamena_na.place(x=175, y=880, width=50, anchor="c")

btn_zamena_vig = Button(text='Заменить \nвыгрузку на:', width=12, height=2, command=zamena_vigryzki)
btn_zamena_vig.place(x=50, y=910)

zamena_na_vig = StringVar()
zamena_na_vig = Entry(textvariable=zamena_na_vig)
zamena_na_vig.place(x=175, y=930, width=50, anchor="c")

vedomosti_and_id = StringVar()
vedomosti_mes = Entry(textvariable=vedomosti_and_id)
vedomosti_mes.place(x=348, y=900, width=250, anchor="c")

ismarried_number_vedomosti = IntVar()
ismarried_number_vedomosti.set(False)
ismarried_vedomosti_but = Checkbutton(text="номера ведомостей", variable=ismarried_number_vedomosti)
ismarried_vedomosti_but.place(x=280, y=860)

ismarried_odratka_ID = IntVar()
ismarried_odratka_ID.set(False)
ismarried_obratka_but = Checkbutton(text="обратка, печать по ID", variable=ismarried_odratka_ID)
ismarried_obratka_but.place(x=280, y=915)

ismarried_bez_podbora = IntVar()
ismarried_bez_podbora.set(False)
ismarried_bez_podbora_but = Checkbutton(text="Собираем без подбора", variable=ismarried_bez_podbora)
ismarried_bez_podbora_but.place(x=280, y=940)

frame_11 = LabelFrame(text="запоминалка директорий", font='Helvetica 9 bold')
frame_11.pack()

btn_00 = Button(frame_11, text='выбор \nведомости', width=10, height=2, command=save_papka)
btn_00.grid(row=1, column=0, padx=2, pady=2)
btn_001 = Button(frame_11, text='выбор фото \nшаблона', width=10, height=2, command=save_foto_dir)
btn_001.grid(row=1, column=1, padx=2, pady=2)

time_sleep = StringVar()
time_sleep.set(0)
message_entry_2 = Entry(textvariable=time_sleep)
message_entry_2.place(x=940, y=900, width=40, anchor="c")
label_time_sek = Label(width=50, height=2, text='сек')
label_time_sek.place(x=980, y=899, width=40, anchor="c")
label_time_sleep = Label(width=50, height=2, text='time sleep')
label_time_sleep.place(x=940, y=870, width=70, anchor="c")

ismarried_print = IntVar()
ismarried_print.set(True)
ismarried_checkbutton_print = Checkbutton(text="Печатать...", variable=ismarried_print)
ismarried_checkbutton_print.place(x=1000, y=930)
# TODO
combo_priz = Combobox(root, state="readonly", width=4)
combo_priz['values'] = ("241", '232', '231', '222', "221", "212")
combo_priz.current(0)  # вариант по умолчанию
combo_priz.place(x=680, y=860)

combo = Combobox(root, state="readonly")
combo['values'] = ("ПТК", "ППЛС", "Североморск", "Северодвинск", "Княжево", "Знаменск", "Саратов", "Мулино(мсп)",
                   "Буньково", "Переславль", "Ковров(МСП)", "Остров", "Наро-Фоминск", "Острогожск",
                   "Северодвинск не присяга", "Ватутинки", "Пакино(пс)", "Пакино(тп)", "Северодвинск_Присяга",
                   'Выпуск', 'Выпуск_Переславль', "Выпуск_рвсн", "Выпуск_Княжево", "Выпуск_Буньково",
                   "Выпуск_Нарофоминск", "Выпуск_Ковров (тп)", "Выпуск_Ковров (мсп)", "Выпуск_Нарофоминск",
                   "Выпуск_Мулино", "Выпуск_Остров", "Выпуск_Знаменск", "Выпуск_Саратов", "Призыв")
combo.current(0)  # вариант по умолчанию
combo.place(x=740, y=860)

btn_combo = Button(text='загрузить шаблон', width=22, height=1, command=shablon)
btn_combo.place(x=710, y=890)

btn_res = Button(text='очистить', width=19, height=1, command=restart)
btn_res.place(x=710, y=920)

btn_priw = Button(text='просмотр', width=19, height=1, command=create_new_window)
btn_priw.place(x=710, y=950)

label_dir = Label(text='©Klyuchnikow 2021')
label_dir.place(x=10, y=955)

root.mainloop()
