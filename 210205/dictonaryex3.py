# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:58:09 2021

@author: Dohun

dictonaryex3.py
"""

import operator

dic, list = {}, []

dic = {
       "Thomas": "토마스",
       "Edward": "에드워드",
       "Henry": "헨리",
       "Gothen": "고든",
       "James": "제임스"
       }

list = sorted(dic.items(), key = operator.itemgetter(0), reverse = True)
print(list)

"""
sorted : 정렬 함수 
dic.items() : (키, 값) 쌍 객체 (tuple)를 list로
operator.itemgetter(0) : 정렬의 기준 객체 설정 
0 : 튜플의 첫 번째 객체로 설정
reverse = True : 내림차순 정렬 
"""

print("영문 이름으로 정렬하기 (오름차순)")
list = sorted(dic.items(), key = operator.itemgetter(0), reverse = False)
print(list)

print("한글 이름으로 정렬하기 (오름차순)")
list = sorted(dic.items(), key = operator.itemgetter(1))
print(list)

print("한글 이름으로 정렬하기 (내림차순)")
list = sorted(dic.items(), key = operator.itemgetter(1), reverse = True)
print(list)
