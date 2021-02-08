# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:39:36 2021

@author: Dohun

3. Rect 클래스 구현하기

   Rect 클래스는 가로,세로를 멤버변수로.  넓이와 둘레를 구하는 멤버 함수가진다.

   클래스의 객체를 print 시 : (가로,세로),넓이:xxx,둘레:xxx가 출력되도록 한다.

​

   두개의 Rect 객체 rect1,rect2를 생성한다.

   if rect1 > rect2 ...

   elif rect1 < rect2 ...

   elif rect1 == rect2 ... 구문이 가능하도록 Rect 클래스 구현하기 단 조건은 넓이를 기준으로한다.
"""

class Rect:
    width = 0
    height = 0
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def rectRound(self):
        return 2 * (self.width + self.height)
    
    def __repr__(self):
        return "(%d, %d), 넓이: %d, 둘레: %d"% (self.width, self.height, self.area(), self.rectRound())
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __gt__(self, other):
        return self.area() > other.area()
    
    def __eq__(self, other):
        return self.area() == other.area()
    
r1 = Rect(10, 10)
r2 = Rect(20, 5)

print(r1 > r2)
print(r1 == r2)
print(r1 < r2)
