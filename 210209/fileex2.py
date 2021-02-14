# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:32:50 2021

@author: Dohun
"""

outfp = None
outfp = open("data.txt", "w", encoding="UTF8")
while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outfp.writelines(outStr + "\n")
    else:
        break
outfp.close()
print("프로그램 종료")