# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:54:25 2021

@author: Dohun
"""

import pymysql

conn = pymysql.connect(host="localhost", port=3307, user="scott", passwd="1234", db="classdb", charset="utf8")

try:
    cur = conn.cursor()
    cur.execute("select * from item")
    for row in cur.fetchall():
        print(type(row), row)
finally:
    cur.close()
    conn.close()