# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:33:43 2021

@author: Dohun

classex2.py
"""

class Car:
    color = ""
    speed = 0
    
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    
    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -= value
        
myCar1 = Car("빨강", 0)
myCar2 = Car("노랑", 0)
myCar3 = Car("파랑", 0)

print("자동차 1의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차 2의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(10)
print("자동차 3의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar3.color, myCar3.speed))