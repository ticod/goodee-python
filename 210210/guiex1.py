# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 09:32:12 2021

@author: Dohun
"""

from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")
    
window = Tk()  # 윈도우 생성
window.geometry("400x400")

photo = PhotoImage(file = "../gif/rabbit.gif")  # 이미지 메모리에 로드
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)  # 이벤트 등록: label1 객체를 클릭하면 clickImage 함수 호출

label1.pack(expand = 1, anchor = CENTER)  # label1 윈도우에 추가
window.mainloop()  # 화면에 출력 