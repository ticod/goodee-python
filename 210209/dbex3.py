# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:07:15 2021

@author: Dohun
"""

import sqlite3

con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""

con = sqlite3.connect("iddb")
cur = con.cursor()
cur.execute("select * from usertable")
userList = cur.fetchall()  # list 타입 리턴 
for user in userList:
    print(user)
print()

cur.execute("select * from usertable")
row = None
while True:
    row = cur.fetchone()
    if row == None:
        break
    print("%5s %15s %15s %d" % (row[0], row[1], row[2], int(row[3])))
    print(type(row))
print()

con.close()