# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:42:16 2021

@author: Dohun

mapex1.py

map : 리스트 각각의 요소 변경
"""

before = ["2021", "02", "08"]

print(type(before[0]))
print(before)

# before의 요소 각각을 int로 형변환 map으로 저장 후\
# 다시 list로 형변환
after = list(map(int, before))

print(type(after[0]))
print(after)

print(int("123"))
print(type(map(int, before)))