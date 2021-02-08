# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:53:58 2021

@author: Dohun

exam3.py
"""

def getSum(list):
    """
    sum = 0
    for i in list:
        sum += i
    return sum
    """
    return sum(list)

def getMean(list):
    """
    mean = 0
    length = len(list)
    if length == 0:
        return 0
    return getSum(list) / length
    """
    return sum(list) / len(list) if len(list) > 0 else 0
    

list = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8]
print("list 값 합: ", getSum(list))
print("list 값 평균: ", getMean(list))

list2 = []
print("list2 값 합: ", getSum(list2))
print("list2 값 평균: ", getMean(list2))

tp = (2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8)
print("tp 값 합: ", getSum(tp))
print("tp 값 평균: ", getMean(tp))
