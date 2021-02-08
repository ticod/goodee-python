# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:50:37 2021

@author: Dohun

dictionaryex2.py

"""

foods = {"떡볶이" : "어묵", "짜장면": "단무지", "라면": "김치", "맥주": "치킨"}

for i in foods.keys():
    print("%s => %s" % (i, foods[i]))


inStr = input("음식 입력: ")

try:
    print(foods[inStr])
except:
    print("해당 음식이 없습니다")


if inStr in foods:
    print(foods[inStr])
else:
    print("해당 음식이 없습니다")
    yn = input("좋아하는 음식으로 등록하시겠습니까? (y/n) ")
    if yn == 'y' or yn == 'Y':
        food = input("궁합 음식을 등록하세요 ")
        foods[inStr] = food
        
print(foods)

print(foods.keys())
print(foods.values())
print(foods.items())
