# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:08:55 2021

@author: Dohun

test5.py 
    년도를 입력받아 윤년인지 평년인지 출력하기

년도를 입력하세요 : 2100
2100 : 평년
​

년도를 입력하세요 : 2000
2000 : 윤년
​

년도를 입력하세요 : 2020
2020 : 윤년
​

년도를 입력하세요 : 2021
2021 : 평년
"""

num = int(input("년도를 입력하세요: "))
result = "평년"

"""
if (num % 4 == 0):
    if (num % 100 == 0):
        if (num % 400 == 0):
            result = "윤년"
    else:
        result = "윤년"    
"""
        

if (num % 400 == 0) or ((num % 4 == 0) and (num % 100 != 0)):
    result = "윤년"
    
print(num, ": ", result)