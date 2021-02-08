# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:35:27 2021

@author: Dohun

tupleex1.py

"""

tp1 = (10, 20, 30)
print(tp1)

# tp1.append(40) # tuple은 append 불가 
list1 = list(tp1)
list1.append(40)
tp1 = tuple(list1)
print(tp1)
print("tp1의 크기", len(tp1))
print("tp[1:3]: ", tp1[1:3])
print("tp[:3]: ", tp1[:3])
print("tp[2:]: ", tp1[2:])
print("tp[::2]: ", tp1[::2])
print(tp1[0], tp1[1], tp1[2])

a, b, c, d = tp1  # tuple의 각 요소를 변수에 저장할 수 있다
print(a, b, c, d)