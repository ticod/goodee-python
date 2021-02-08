# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:58:21 2021

@author: Dohun

classex4.py : 상속 예제, 오버라이딩 예제

파이썬은 다중 상속이 가능하다 
"""

class Car:
    speed = 0
    door = 3
    
    def upSpeed(self, value):
        self.speed += value
        print("현재 속도 (부모 클래스): %d" % self.speed)
        
class Sedan(Car):
    pass
    
class Truck(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(자손 클래스): %d" % self.speed)  # 오버라이딩 
        
class Container:
    room = 1
    
class MovingCar(Container, Car):  # 다중 상속 
    pass


truck1 = Truck()
print("트럭: ", end = "")
truck1.upSpeed(200)

sedan1 = Sedan()
print("승용차: ", end = "")
sedan1.upSpeed(200)

mCar = MovingCar()
print("이동 차량: ", end = "")
mCar.upSpeed(60)
print("이동 차량의 방 개수: ", mCar.room, ", 문의 개수: ", mCar.door)