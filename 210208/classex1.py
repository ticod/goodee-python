# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:33:43 2021

@author: Dohun

classex1.py

생성자 : __init__(self)
따로 구현하지 않으면 pass
self: 자바의 this (자기 참조 변수)
"""

class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -= value
        
myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0
        
myCar2 = Car()
myCar2.color = "노랑"
myCar2.speed = 0
        
myCar3 = Car()
myCar3.color = "파랑"
myCar3.speed = 0

print("자동차 1의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차 2의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(10)
print("자동차 3의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar3.color, myCar3.speed))