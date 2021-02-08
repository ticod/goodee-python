# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:01:14 2021

@author: Dohun

exam1.py

금액을 입력받아 동전 (500, 100, 50, 10, 1) 으로 바꿔주는 프로그램 작성
"""

money = int(input("금액 입력: "))

print("500원: ", money // 500)
money %= 500

print("100원: ", money // 100)
money %= 100

print("50원: ", money // 50)
money %= 50

print("10원: ", money // 10)
money %= 10

print("1원: ", money // 1)
