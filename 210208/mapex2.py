# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:48:57 2021

@author: Dohun

mapex2.py
"""

myList = [1,2,3,4,5]

add = lambda num: num + 10

myList = list(map(add, myList))

print(myList)

myList = list(map(lambda num: num - 10, myList))
print(myList)
myList = list(map(lambda num: num * 10, myList))
print(myList)

list1 = [1,2,3,4]
list2 = [10,20,30,40]

hap = lambda n1, n2: n1 + n2
hapList = list(map(hap, list1, list2))
print(hapList)

list1.append(0)
list2.append(0)
hapList = list(map(hap, list1, list2))
print(hapList)