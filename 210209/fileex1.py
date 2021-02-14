# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:06:01 2021

@author: Dohun
"""

infp = None
inStr = ""
"""
open(파일 이름, 파일 모드, [인코딩 방식])

r : 읽기
w : 쓰기, 기존 파일 존재시 변경
a : 쓰기, 기존 파일 존재시 추가

t : 텍스트
b : 바이너리
"""
infp = open("regularex3.py", "rt", encoding="UTF8")
while True:
    inStr = infp.readline()  # 한 줄 읽기
    if inStr == None or inStr == "":  # EOF 체크 
        break
    print(inStr, end = "")  # 파일에 \n 존재함 
infp.close()