# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:49:08 2021

@author: Dohun

tryex2.py
"""

num1 = input("문자 1 입력: ")
num2 = input("문자 2 입력: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    while True:
        res = num1 / num2
        print(res)
except ValueError as e:
    print("문자를 숫자로 변환할 수 없습니다")
    print(e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다")
    print(e)
except KeyboardInterrupt as e:
    print("Ctrl + C가 눌렸습니다", e)
    # 에러 메세지 X
finally:
    print("프로그램 종료")