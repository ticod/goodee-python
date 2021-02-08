# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:49:24 2021

@author: Dohun

forex1.py
"""

i, j = 0, 0

for i in range(2, 10):
    print("%5d단" % i)
    for j in range(2, 10):
        print("%2dX%2d=%3d" % (i, j, (i * j)))
    print()