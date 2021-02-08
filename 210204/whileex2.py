# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:04:34 2021

@author: Dohun

whileex2.py

"""

import random

rnum = random.randrange(1, 100)

i = 0
"""
True, False : boolean형 예약어 
"""
while True:
    i += 1
    a = int(input("숫자를 입력하세요: "))
    if a > rnum:
        print("DOWN")
    elif a < rnum:
        print("UP")
    else:
        print("정답입니다! %d번만에 맞췄습니다!" % i)
        break