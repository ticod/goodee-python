# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:05:02 2021

@author: Dohun

lambdaex2.py
"""

myList = [1, 2, 3, 4, 5]

def add10(num):
    return num + 10

add10Lambda = lambda num : num + 10

for i in range(len(myList)):
    myList[i] = add10Lambda(myList[i])
    
print(myList)