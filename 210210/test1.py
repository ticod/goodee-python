# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:24:25 2021

@author: Dohun
"""

from tkinter import *


def toDisplay(value):
    display.insert(END, value)
        

def calculate():
    value = Entry.get(display)
    try:
        if value != "":
            result = eval(value)
            display.delete(0, END)
            display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR! Please press AC button!")


def clear():
    display.delete(0, END)


def calculatorButtonInit(buttonList):
    buttonList[0].configure(text = 7, command = lambda: toDisplay("7"))
    buttonList[1].configure(text = 8, command = lambda: toDisplay("8"))
    buttonList[2].configure(text = 9, command = lambda: toDisplay("9"))
    buttonList[3].configure(text = "/", command = lambda: toDisplay("/"))
    
    buttonList[4].configure(text = 4, command = lambda: toDisplay("4"))
    buttonList[5].configure(text = 5, command = lambda: toDisplay("5"))
    buttonList[6].configure(text = 6, command = lambda: toDisplay("6"))
    buttonList[7].configure(text = "*", command = lambda: toDisplay("*"))
    
    buttonList[8].configure(text = 1, command = lambda: toDisplay("1"))
    buttonList[9].configure(text = 2, command = lambda: toDisplay("2"))
    buttonList[10].configure(text = 3, command = lambda: toDisplay("3"))
    buttonList[11].configure(text = "+", command = lambda: toDisplay("+"))
    
    buttonList[12].configure(text = "AC", command = lambda: clear())
    buttonList[13].configure(text = 0, command = lambda: toDisplay("0"))
    buttonList[14].configure(text = "=", command = lambda: calculate())
    buttonList[15].configure(text = "-", command = lambda: toDisplay("-"))
    


window = Tk()
window.geometry("480x280")
window.title("Calculator")

# frame 분리
entryFrame = Frame(window)
entryFrame.pack()

buttonFrame = Frame(window)
buttonFrame.pack()

# display : 숫자, 계산 결과 창
display = Entry(entryFrame, width = 480)
display.pack(padx = 10, pady = 10)

# button 초기 설정
buttonInnerFrames = []
buttons = []

for i in range(0, 4):
    buttonInnerFrame = Frame(buttonFrame, width = 480, height = 3)
    buttonInnerFrame.pack()
    buttonInnerFrames.append(buttonInnerFrame)
    for j in range(0, 4):
        button = Button(buttonInnerFrame, text = str((i * 4) + j), width = 15, height = 3)
        button.pack(side = LEFT)
        buttons.append(button)
        
calculatorButtonInit(buttons)

window.mainloop()