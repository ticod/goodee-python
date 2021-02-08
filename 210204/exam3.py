# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:01:34 2021

@author: Dohun

exam3.py

가로로 구구단 출력하기

"""

for i in range(2, 10):
    for j in range(2, 10):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print()