# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:33:56 2021

@author: Dohun
"""

import pymysql

conn = pymysql.connect(host="localhost", port=3307, user="scott", passwd="1234", db="classdb", charset="utf8")

cur = conn.cursor()
cur.execute("drop table items")
cur.execute("""
    CREATE TABLE ITEMS (
        item_id integer primary key auto_increment,
        name varchar(300),
        price integer
    )            
""")
data = [("바나나", 3000), ("망고", 30000), ("사과", 10000)]

for i in data:
    cur.execute("insert into items (name, price) values (%s, %s)", i)
conn.commit()

cur.execute("select * from items")
for row in cur.fetchall():
    print(type(row), row)
print()

print("가격이 3000 이상, 10000 이하인 레코드 조회 ==")
cur.execute("select * from items where price between %s and %s", (3000, 10000))
for row in cur.fetchall():
    print(type(row), row)

print("가격이 30000인 레코드 삭제 ==")
cur.execute("delete from items where price = %s", 30000)
conn.commit()
cur.execute("select * from items")
for row in cur.fetchall():
    print(type(row), row)
print()
    
cur.close()
conn.close()