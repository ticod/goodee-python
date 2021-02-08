# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:14:02 2021

@author: Dohun

exam2.py

초를 입력받아 몇시간 몇분 몇초인지 출력하
"""

time = int(input("시간 입력: "))

print(time // 3600, "시간 ", end = "")
time %= 3600
print(time // 60, "분 ", time % 60, "초 ")



