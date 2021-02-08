# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:13:03 2021

@author: Dohun
"""

def add(a, b):
    return a + b

def sub(a, b):
    return a - b


"""
직접 실행시 __name__에 __main__값이 저장된다 
"""
if __name__ == "__main__":  # 직접 실행시 조건 만족 
    print(add(3, 4))
    print(sub(4, 2))