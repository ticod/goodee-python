# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:01:24 2021

@author: Dohun

2. 주어진 자연수 N에 대해 N이 짝수이면 N!을, 홀수이면 ΣN을 구하는 코드를 작성하기
"""

def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num - 1)
    
def sigma(num):
    if num == 1:
        return 1
    else:
        return num + sigma(num - 1)

num = int(input("자연수를 입력하세요: "))

if num % 2 == 0:
    print(fac(num))
else:
    print(sigma(num))