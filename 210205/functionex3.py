# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:39:22 2021

@author: Dohun

functionex3.py
"""

def multi(v1, v2):
    list = []
    res1 = v1 + v2
    res2 = v1 - v2
    list.append(res1)
    list.append(res2)
    return list

def multiParam(* p):  # * p : 가변 매개 변수 (개수가 가변)
    result = 0
    for i in p:
        result += i
    return result

hap, sub = 0, 0
list = multi(100, 200)
hap = list[0]
sub = list[1]
print("multi 함수의 리턴: %d, %d" % (hap, sub))

print("multiParam() = ", multiParam())
print("multiParam(10) = ", multiParam(10))
print("multiParam(10, 20) = ", multiParam(10, 20))
print("multiParam(10, 20, 30) = ", multiParam(10, 20, 30))
