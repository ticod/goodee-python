# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:37:13 2021

@author: Dohun
"""

from tkinter import *


def fa():
    temp = ((9 / 5) * int(e1.get())) + 32
    e2.delete(0, len(e2.get()))
    e2.insert(0, "%.2f" % temp)
    
def ca():
    temp = (int(e2.get()) - 32) / (9 / 5)
    e1.delete(0, len(e1.get()))
    e1.insert(0, "%.2f" % temp)


window = Tk()
window.title("섭씨를 화씨로 변경")
window.geometry("500x200")
window.resizable(False, False)

l1 = Label(window, text="섭씨")
l2 = Label(window, text="화씨")

l1.pack()
l2.pack()
l1.place(x = 100, y = 0)
l2.place(x = 100, y = 20)

e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()

b1 = Button(window, text = "섭씨 -> 화씨", command = fa)
b2 = Button(window, text = "화씨 -> 섭씨", command = ca)
b1.pack()
b2.pack()

window.mainloop()