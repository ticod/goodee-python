# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:47:19 2021

@author: Dohun

3. 파일 명을 입력받아 파일을 복사하는 프로그램 작성하기

[결과]

원본파일의 이름을 입력하세요: test1.py

복사본파일의 이름을 입력하세요 : test1.bak

​

복사완료
"""

inFp, outFp = None, None
inStr = ""
inFile = input("원본 파일 이름 입력: ")
outFile = input("복사본 파일 이름 입력: ")

inFp = open(inFile, "r", encoding = "utf-8")
outFp = open(outFile, "w", encoding = "utf-8")

inList = inFp.readlines()  # text 모드에서만 사용 가능
for inStr in inList:
    outFp.writelines(inStr)

print()
    
inFp.close()
outFp.close()
print("복사 완료")
