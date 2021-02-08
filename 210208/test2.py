# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:39:29 2021

@author: Dohun

2. 입력된 자연수가 홀수인지 짝수인지 판별해 주는 함수를 람다식을 이용하여 작성해 보자.
"""

print("홀수일까요? 짝수일까요?")
num = int(input("자연수 입력: "))

func = lambda num: num % 2 == 0

print(func(num))