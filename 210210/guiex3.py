# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:01:14 2021

@author: Dohun
"""

from tkinter import *
from tkinter.filedialog import *


def funcOpen():
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", ("*.*"))))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def funcExit():
    window.quit()
    window.destroy()
    
window = Tk()
window.geometry("400x400")
window.title("gif 이미지 선택하여 보기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = funcOpen)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = funcExit)

window.mainloop()
