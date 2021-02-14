# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:24:30 2021

@author: Dohun
"""

from tkinter import *
import tkinter.font
    
def click():
    value = radioVar.get()
    photo = PhotoImage(file = filePath + fnameList[value])
    pLabel.configure(image = photo)
    pLabel.image = photo

fnameList = [
        "cat.gif", "dog.gif", "rabbit.gif",
    ]
filePath = "../gif/"

window = Tk()
window.geometry("480x440")
window.title("좋아하는 동물 선택하기")

label = Label(window, text = "좋아하는 동물 투표", font = ("궁서체", 30), fg = "blue")
label.pack(pady = 10)

radioVar = IntVar()
radios = []

for i in range(0, 3):
    radio = Radiobutton(window, text = str(i) + "번", value = i, variable = radioVar)
    radio.pack()
    radios.append(radio)
    
radios[0].select()
    
button = Button(window, text = "사진 보기", command = click)
button.pack(pady = 10)

photo = PhotoImage(file = filePath + fnameList[0])
pLabel = Label(window, image = photo)
pLabel.pack(pady = 20)

window.mainloop()