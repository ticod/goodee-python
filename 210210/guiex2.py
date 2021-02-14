# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:15:43 2021

@author: Dohun
"""

from tkinter import *
from time import *

fnameList = [
        "jeju1.gif", "jeju2.gif", "jeju3.gif",
        "jeju4.gif", "jeju5.gif", "jeju6.gif",
        "jeju7.gif", "jeju8.gif", "jeju9.gif"
    ]
filePath = "../gif/"
photoList = [None] * 9
num = 0

def clickNext():
    global num
    num = (num + 1) % len(fnameList)
    photo = PhotoImage(file = filePath + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def clickPrev():
    global num
    num -= 1
    if (num < 0):
        num = len(fnameList) - 1
    photo = PhotoImage(file = filePath + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

photo = PhotoImage(file = filePath + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()
