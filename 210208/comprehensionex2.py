# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:56:13 2021

@author: Dohun

comprehensionex2.py
"""

set1 = {x ** 2 for x in [1, 1, 2, 2, 3, 3]}
print(set1)

list1 = [x ** 2 for x in [1, 1, 2, 2, 3, 3]]
print(list1)

set2 = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print(set2)
print(sorted(set2))