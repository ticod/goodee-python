# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:14:04 2021

@author: Dohun

comprehensionex1.py
"""

numbers = []
for n in range(1, 11):
    numbers.append(n)
print(numbers)

print([x for x in range(1, 11)])
cList = [x for x in range(1, 11)]
print(cList)

print([x for x in range(2, 11, 2)])
print([x for x in range(1, 11) if x % 2 == 0])

print([x for x in range(1, 11) if x % 2 == 0 and x % 3 == 0])


matrix = [[1,2,3], [4,5,6], [7,8,9]]
list1 = [x for row in matrix for x in row]
print(list1)

colorList = ['black', 'white', 'blue']
sizeList = ['S', 'M', 'L']
dressList = ((c, s) for c in colorList for s in sizeList)  # tuple도 가능 
for d in dressList:
    print(d)