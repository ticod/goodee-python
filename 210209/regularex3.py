# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:34:07 2021

@author: Dohun
"""

import re

str = "The quick brown fox jumps over the lazy dog Te Thhe Thhhe."

str_list = str.split()
print(str_list)
pattern = re.compile("Th*e")
count = 0
for word in str_list:
    if pattern.search(word):
        count += 1
print("결과 1: {1:s}:{0:d} ".format(count, "갯수"))

pattern = re.compile("Th*e", re.I)  # re.I : 대소문자 구분 없이 
count = 0
for word in str_list:
    if pattern.search(word):
        count += 1
print("결과 2: {1:s}:{0:d} ".format(count, "갯수"))

print("결과 3: ", end = "")
for word in str_list:
    if pattern.search(word):
        print(word, end = " ")
print()

# (?P<match_word>Th*e) : 대소문자 구분 없이 Th*e 패턴을 match_word라는 패턴 그룹으로 저장 
pattern = re.compile("(?P<match_word>Th*e)", re.I)
print("결과 4: ", end = "")
for word in str_list:
    if pattern.search(word):
        print("{0}".format(pattern.search(word).group("match_word")), end = " ")
print()

#pattern.sub : 값 치환
#Th*e 패턴을 a로 치환
print("결과 5:", pattern.sub("a", str))