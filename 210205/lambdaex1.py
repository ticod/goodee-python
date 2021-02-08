# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:51:00 2021

@author: Dohun

lambdaex1.py
"""

def hap1(num1, num2):
    return num1 + num2

print(hap1(10, 20))

hap2 = lambda num1, num2: num1 + num2
print(hap2(10, 20))

mul = lambda num1, num2: num1 * num2
print(mul(10, 20))

# 매개 변수의 기본 값 설정
hap3 = lambda num1 = 0, num2 = 1: num1 + num2
print(hap3())
print(hap3(100))
print(hap3(100, 200))
