# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:44:01 2021

@author: Dohun

exam1.py

"""

aa, bb = [], []

i = 0
while len(aa) != 100:
    aa.append(i)
    i += 2
    
bb = aa[::-1]

print(aa[0:9])
print(bb[-1:-10:-1])