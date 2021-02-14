# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:35:02 2021

@author: Dohun
"""
import sqlite3

data = [
    ('test1', '테스트1', 'test1@aaa.bbb', 1991),
    ('test2', '테스트2', 'test2@aaa.bbb', 1992),
    ('test3', '테스트3', 'test3@aaa.bbb', 1993),
    ('test4', '테스트4', 'test4@aaa.bbb', 1994),
]

con = sqlite3.connect("iddb")
cur = con.cursor()

cur.executemany("""
    insert into usertable
    (id, username, email, birthyear)
    values
    (?, ?, ?, ?)
""", data)

con.commit()

# 데이터 확인 
cur.execute("select * from usertable")
userList = cur.fetchall()  # list 타입 리턴 
for user in userList:
    print(user)
print()

con.close()