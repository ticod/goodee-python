# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:39:48 2021

@author: Dohun

4. 화씨온도= (( 9 / 5) * 섭씨온도) + 32 인 경우 섭씨 -20 ~ 50 도까지를 화씨 온도로 변경하여 작성하기
"""

def toFa(temp):
    return ((9 / 5) * temp) + 32

for i in range(-20, 50 + 1):
    print(toFa(i))