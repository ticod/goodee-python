# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:58:54 2021

@author: Dohun
"""

from tkinter import *

window = None
canvas = None
XSIZE, YSIZE = 256, 256

window = Tk()
window.title("raw 파일 출력하기")
canvas = Canvas(window, height = YSIZE, width = XSIZE)

paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = 'normal')

fp = open("../gif/flower.raw", "rb")

for i in range(0, XSIZE):
    for k in range(0, YSIZE):
        data = int(ord(fp.read(1)))
        paper.put("#%02x%02x%02x" % (data, data, data), (k, i))
    
fp.close()
canvas.pack()
window.mainloop()