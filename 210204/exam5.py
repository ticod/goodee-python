# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:43:03 2021

@author: Dohun

exam5.py

삼각형의 높이 입력, 삼각형 출력

"""

num = int(input("삼각형의 높이 입력: "))

for i in range(1, num + 1):
    print("*" * i)

for i in range(num, 0, -1):
    print("*" * i)
