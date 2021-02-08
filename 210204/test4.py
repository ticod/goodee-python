# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:59:56 2021

@author: Dohun

test4.py 

16진수를 입력하면 16진수 인지 아닌지 판단하여 16진수가 맞으면 10진수로 변경하는 프로그램을 작성하시오.

16진수가 아닌 경우 16진수 아님을 출력하기

​

16진수 입력 : ff

ff = 255

​

16진수 입력 : qw

qw 문자는 16진수 문자가 아닙니다
"""

inStr = input("16진수 입력: ")

try:
    print(inStr, " = ", int(inStr, 16))
except:
    print(inStr, " 문자는 16진수가 아닙니다")
    
arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
check = True

for ch in inStr:
    if arr.count(ch) == 0:
        check = False
        break;

if check:
    print(inStr, " = ", int(inStr, 16))
else:
    print(inStr, " 문자는 16진수가 아닙니다")