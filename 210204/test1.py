# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:37:44 2021

@author: Dohun

test1.py

삼각형의 높이를 입력받은 후 삼각형을 출력하는 프로그램을 작성

삼각형의 높이를 입력하세요 : 5


    *

   **

  ***

 ****

*****
​

    *  

   ***

  *****

 *******

*********
"""

num = int(input("삼각형의 높이를 입력하세요: "))

for i in range(1, num + 1):
    print(" " * (num - i), end = "")
    print("*" * i)
    
print()

for i in range(0, num):
    print(" " * (num - i - 1), end = "")
    print("*" * (i * 2 + 1))