# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:36 2021

@author: Dohun

exam2.py
"""

def calc(var1, var2, oper):
    if oper == "+":
        return var1 + var2
    elif oper == "-":
        return var1 - var2
    elif oper == "*":
        return var1 * var2
    elif oper == "/":
        return var1 / var2
    else:
        return 0

oper = input("연산자를 선택하세요:(+ - * /): ")
var1 = int(input("첫 번째 수: "))
var2 = int(input("두 번째 수: "))
res = calc(var1, var2, oper)

print("계산: %d %s %d = %d" % (var1, oper, var2, res))
print("계산:", var1, oper, var2, "=", res)