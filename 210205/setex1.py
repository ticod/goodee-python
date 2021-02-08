# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:48:23 2021

@author: Dohun

setex1.py

"""

set1 = {1, 2, 3, 4, 5}
print(set1)

set2 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(set2)

set3 = {5, 6, 7, 8}
print(set3)

print("set1, set3 교집합")
print(set1 & set3)
print(set1.intersection(set3))

print("set1, set3 합집합")
print(set1 | set3)
print(set1.union(set3))