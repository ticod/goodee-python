# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:58:21 2021

@author: Dohun

classex3.py
"""

class Car:
    color = ""
    speed = 0
    num = 0
    count = 0
    
    def __init__(self, color = ""):
        self.color = color
        self.speed = 0  # 인스턴스 변수
        Car.count += 1  # 클래스 변수(static)
        self.num = Car.count  # 인스턴스 변수 
    
    def printMessage(self):
        print("색상: %s, 속도: %dkm, 번호: %d, 생산 번호: %s" 
              % (self.color, self.speed, self.num, self.count), end = "")
        
myCar1, myCar2 = None, None  # null
myCar1 = Car()
myCar1.speed = 30
myCar1.printMessage()
print()
        
myCar2 = Car()
myCar2.speed = 50
myCar2.printMessage()
print()

# myCar1.count += 10  # 12, 2 => 인스턴스 변수로 들어감
Car.count += 10  # 12, 12 => 클래스 변수로 들어감 
print("생산 번호: %d" % (myCar1.count))
print("생산 번호: %d" % (myCar2.count))

myCar3 = Car("빨강")
myCar3.printMessage()