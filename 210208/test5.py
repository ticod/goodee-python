# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:39:52 2021

@author: Dohun

5. 1 부터 1000 까지의 홀수의 합계 계산시 최초로 1000이 넘는 숫자는 구하는 프로그램을 작성해 보자.
"""
total = 0

for i in range(1, 1000 + 1):
    total += i if i % 2 == 1 else 0
    if (total > 1000):
        print(total)
        break