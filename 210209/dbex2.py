# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:43:58 2021

@author: Dohun
"""

import sqlite3

con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""

con = sqlite3.connect("iddb")
cur = con.cursor()
cur.executescript('''
            drop table if exists usertable;
            create table usertable (id char(4) primary key,
                                    username char(15),
                                    email char(15),
                                    birthyear int)
            ''')
while True:
    data1 = input('사용자 ID => ')
    if data1 == "":
        break
    data2 = input("사용자 이름 => ")
    data3 = input("이메일 => ")
    data4 = input("출생년도 => ")
    sql = "insert into usertable values ('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")"
    cur.execute(sql)
    con.commit()
    
con.close() 
