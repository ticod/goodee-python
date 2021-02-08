# -*- coding: utf-8 -*-
"""
    \""" : 여러줄 주석
    
    파이썬 특징
    1. 변수 선언 필요 없음
    2. {} 블럭이 없음 => 들여쓰기로 판단
"""

print("hello world")

sel = int(input("입력 진수 결정(16/10/8/2): "))
num = input("값 입력: ")

num10 = int(num, sel)

print(num10)
print(type(num))
print(type(num10))

# 값 변경 후 타입 확
num = num10
print(num)
print(type(num))

# 10진수를 각 진법으로 출력
print("16진수 => ", hex(num10))
print("8진수 => ", oct(num10))
print("2진수 => ", bin(num10))
