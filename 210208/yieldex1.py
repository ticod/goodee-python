# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:34:34 2021

@author: Dohun

yieldex1.py
"""
def genFun(num):
    for i in range(10, num + 10):
        yield i  # i 변수 값을 전달, 함수 종료 X
        print(i, "값 반환")

print(list(genFun(5)))

for data in genFun(5):
    print("main에서 출력: ", data)