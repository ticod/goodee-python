# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:05:59 2021

@author: Dohun

listex3.py

"""

ss = "2021/02/05"

print("10년 전 연도 출력")
list = ss.split("/")
print("10년 전: ", int(list[0]) - 10)

ss = "(홍길동)"
for i in range(1, len(ss) - 1):
    print(ss[i], end="#")
print()

print(ss[-1:0:-1])

ss = "홍길동"
if ss.startswith("(") == False:
    print("(", end = "")
print(ss, end = "")
if ss.endswith(")") == False:
    print(")")
