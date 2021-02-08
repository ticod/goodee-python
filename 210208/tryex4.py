# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:11:11 2021

@author: Dohun

tryex4.py

1. 에러 발생시 except: 구문 실행
    오류가 없는 경우 else 구문 실행
2. 오류 발생시 무시하고 싶은 경우
    pass 예약어 사용 
3. raise (java의 throw) : 예외 강제 발생 
"""

try:
    age = int(input("나이를 입력하세요: "))
except:
    print("나이가 아닙니다. 정확히 입력하세요")
else:
    if age <= 19:
        print("미성년저 입니다")
    else:
        print("성인입니다")
        
try:
    f = open("없는 파일", "r")
except FileNotFoundError:
    pass