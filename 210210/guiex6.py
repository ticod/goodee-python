# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:03:11 2021

@author: Dohun
"""

import sqlite3
from tkinter import *
from tkinter import messagebox


def getEntryData():
    dataList = []
    dataList.append(edit1.get())
    dataList.append(edit2.get())
    dataList.append(edit3.get())
    dataList.append(edit4.get())
    return dataList

def insertData():
    data = tuple(getEntryData())
    print(data)
    sql = """
        insert into usertable
        (id, username, email, birthyear)
        values
        (?, ?, ?, ?)
    """
    
    try:
        con = sqlite3.connect("../db/iddb")
        cur = con.cursor()
        cur.execute(sql, data)
    except:
        messagebox.showerror("오류", "데이터 입력 오류 발생")
    else:
        messagebox.showinfo("성공", "데이터 입력 성공")
    finally:
        con.commit()
        con.close()

def selectData():
    dataList = [[], [], [], []]
    con = sqlite3.connect("../db/iddb")
    cur = con.cursor()
    
    cur.execute("select * from usertable")
    
    dataList[0].append("사용자 ID")
    dataList[1].append("이름")
    dataList[2].append("이메일")
    dataList[3].append("출생년도")
    
    for i in range(0, 4):
        dataList[i].append("----------")
    
    while True:
        row = cur.fetchone()
        if row == None:
            break
        for i in range(0, 4):
            dataList[i].append(row[i])
            
    listData1.delete(0, listData1.size() - 1)
    listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1)
    listData4.delete(0, listData4.size() - 1)
    
    for item1, item2, item3, item4 in \
            zip(dataList[0], dataList[1], dataList[2], dataList[3]):
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)
        listData4.insert(END, item4)
            
    con.commit()
    con.close()


window = Tk()
window.geometry("600x300")
window.title("GUI 데이터 입력")

edtFrame = Frame(window)
edtFrame.pack()

listFrame = Frame(window)
listFrame.pack(side = BOTTOM, fill = BOTH, expand = 1)

edit1 = Entry(edtFrame, width = 10)
edit1.pack(side = LEFT, padx = 10, pady = 10)
edit2 = Entry(edtFrame, width = 10)
edit2.pack(side = LEFT, padx = 10, pady = 10)
edit3 = Entry(edtFrame, width = 10)
edit3.pack(side = LEFT, padx = 10, pady = 10)
edit4 = Entry(edtFrame, width = 10)
edit4.pack(side = LEFT, padx = 10, pady = 10)

btnInsert = Button(edtFrame, text = "입력", command = insertData)
btnInsert.pack(side = LEFT, padx = 10, pady = 10)
btnSelect = Button(edtFrame, text = "조회", command = selectData)
btnSelect.pack(side = LEFT, padx = 10, pady = 10)

listData1 = Listbox(listFrame, bg="yellow")
listData1.pack(side = LEFT, fill = BOTH, expand = 1)
listData2 = Listbox(listFrame, bg="yellow")
listData2.pack(side = LEFT, fill = BOTH, expand = 1)
listData3 = Listbox(listFrame, bg="yellow")
listData3.pack(side = LEFT, fill = BOTH, expand = 1)
listData4 = Listbox(listFrame, bg="yellow")
listData4.pack(side = LEFT, fill = BOTH, expand = 1)

window.mainloop()