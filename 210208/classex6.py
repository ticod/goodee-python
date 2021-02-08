# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:50:49 2021

@author: Dohun

classex6.py

추상 메서드 예제
"""

class SuperClass:
    def method(self):
        raise NotImplementedError  # 오버라이딩 안하면 예외 발생 
        
class SubClass1(SuperClass):
    def method(self):
        print("SubClass1 메서드 실행")
        
class Test(SubClass1, SuperClass):
    pass

subClass = SubClass1()
subClass.method()