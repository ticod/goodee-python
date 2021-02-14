# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:01:36 2021

@author: Dohun

sqlite db 사용하기
sqlite : 파이썬 내부에 존재하는 dbms로, 가벼움이 특징
안드로이드에서도 사용함 
"""

import sqlite3

dbPath = "test.sqlite"  # 데이터베이스 파일
conn = sqlite3.connect(dbPath)
cur = conn.cursor()  # SQL 구문 실행하기 위한 객체

# SQL 구문들 실행 
cur.executescript('''
drop table if exists items;
create table items (item_id integer primary key,
                    name text unique,
                    price integer);
insert into items (name, price) values ('Apple', 800);
insert into items (name, price) values ('Orange', 500);
insert into items (name, price) values ('Banana', 300);
''')
conn.commit()  # 물리적으로 데이터 저장 

cur = conn.cursor()
cur.execute("select * from items")
item_list = cur.fetchall()  # list 타입 리턴 

print(type(item_list))
for it in item_list:
    print(it)