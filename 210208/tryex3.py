# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:03:12 2021

@author: Dohun

tryex3.py
"""

try:
    a = [1, 2]
    print(a[1])
    # 4 / 0
    b = int("a")
except (ZeroDivisionError, IndexError) as e:
    print(e)
except ValueError as e:
    print(e)