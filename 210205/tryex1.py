# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:12:10 2021

@author: Dohun

tryex1.py
"""

myStr = "파이썬 공부 중입니다. 파이썬을 열심히 공부합시다!"
strpos = []
index = 0

"""
while True:
    index = myStr.find("파이썬", index)
    if index == -1:
        break
    strpos.append(index)
    index += 1
"""

# 위 주석 코드와 동일 
while True:
    try:
        index = myStr.index("파이썬", index)
        strpos.append(index)
        index += 1
    except:
        break
    
    
print("파이썬 문자의 위치: ", strpos, "문자의 개수: ", len(strpos))