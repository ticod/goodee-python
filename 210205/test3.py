# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:01:28 2021

@author: Dohun

3. 나라와 수도를 등록하고 화면에 나라이름을 입력받아 해당 나라의 수도를 출력하기

등록된 나라가 아닌 경우 수도를 입력받아 등록하기.

나라 입력시 "종료" 입력되면 프로그램 종료.

종료시 등록된 모든 나라와 수도정보를 화면 출력하기. 
"""

info = {"대한민국": "서울", "일본": "도쿄", "중국": "베이징"}

while True:
    con = input("나라 입력: ")
    
    if con == "종료":
        print("프로그램 종료")
        print(info)
        break
    
    if con in info:
        print(info[con])
    else:
        cap = input("등록된 나라가 아닙니다. 수도 입력: ")
        info[con] = cap
