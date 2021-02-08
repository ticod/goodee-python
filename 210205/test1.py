# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:52:47 2021

@author: Dohun

test1.py
1. 피보나치 수열 출력하기

​

피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : 5

[0,1,1,2,3]

​

피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : 10

[0,1,1,2,3,5,8,13,21,34]
"""

fiboList = [0, 1]

def fibo(num):
    global fiboList
    if len(fiboList) >= num:
        return fiboList[num - 1]
    else:
        fiboList.append(fibo(num - 1) + fibo(num - 2))
        return fiboList[num - 1]
    
num = int(input("피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) :"))

fibo(num)
print(fiboList)