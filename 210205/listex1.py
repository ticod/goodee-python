# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:48:10 2021

@author: Dohun

listex1.py

파이썬(자바 컬렉션)
list(List) : []
dictionary(Map) : {key, value}
set(Set) : {}
tuple : 
"""

a = [0, 0, 0, 0]
b = []
suma, sumb = 0, 0

print(b, len(b))

for i in range(0, len(a)):
    a[i] = int(input(str(i + 1) + "번째 값: "))
    suma += a[i]
    b.append(a[i])
    sumb += b[i]

print(a)
print(b, len(b))
print(suma)
print(sumb)