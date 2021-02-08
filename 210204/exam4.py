# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:15:53 2021

@author: Dohun

exam4.py

입력받은 수 까지의 합을 출력하기
+ 짝수 합 출력하기
"""

numSum, evenSum = 0, 0
num = int(input("수 입력: "))

for i in range(1, num + 1):
    numSum += i
    if (i % 2 == 0):
        evenSum += i
    
print("합: ", numSum)
print("짝수 합: ", evenSum)
    
