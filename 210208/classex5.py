# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:55:11 2021

@author: Dohun

classex5.py

파이썬의 클래스에서 사용되는 특별한 메서드 
"""

class Line:
    length = 0
    
    def __init__(self, length):
        self.length = length
        
    def __repr__(self):  # toString
        return "선의 길이: %d" % self.length
    
    def __add__(self, other):  # + 연산시 호출 
        return self.length + other.length
    
    def __lt__(self, other):  # < 연산시 호출
        return self.length < other.length
    
    def __gt__(self, other):  # > 연산시 호출
        return self.length > other.length
    
    def __eq__(self, other):  # == 연산시 호출
        return self.length == other.length
    
    def __del__(self):  # 소멸자 : 객체 제거시 호출되는 메서드 
        print(self.length, "길이 선이 제거되었습니다")
        
myLine1 = Line(200)
myLine2 = Line(100)

print(myLine1)
print(myLine2)

print("두 선의 길이의 합: %d" % (myLine1 + myLine2))

if myLine1 < myLine2:
    print("myLine2 선이 더 깁니다")
elif myLine1 == myLine2:
    print("myLine1, myLine2 선의 길이는 같습니다")
else:
    print("myLine1 선이 더 깁니다")
    
# 프로그램 종류시 생성된 모든 객체들이 제거됨
# 객체들이 제거됨과 동시에 소멸자 호출 