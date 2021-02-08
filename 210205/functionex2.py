# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:10:02 2021

@author: Dohun

functionex2.py
"""

def func1():
    # 지역 변수들 호출
    a = 20  # 전역 변수 a와 관계 X
    b = 1000
    global gval  # gval을 지역 변수가 아닌, 전역 변수 gval을 사용함 
    gval = 200  # 전역변수 gval의 값을 200으로 변경
    print("func1() 함수 호출", gval, a, b)
    
def func2():
    print("func2() 함수에서 func1()함수 호출")
    func1()
    print("전역 변수 gval 값 = ", gval, a)  # 전역 변수 값 출력
    # print(b)  # 오류 발생 
    
gval = 100
a = 10

if __name__ == "__main__":
    func2()

