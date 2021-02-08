# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:13:00 2021

@author: Dohun

listex2.py
리스트 함수 
"""

myList = [30, 10, 20]

print("리스트: %s" % myList)

myList.append(40)

print("myList.append(40) 리스트: %s" % myList)

print("pop() 메서드 결과: %s" % myList.pop())
print("pop() 메서드 후 리스트: %s" % myList)

myList.sort()
print("myList.sort() 후 리스트: %s" % myList)
myList.reverse()
print("myList.reverse() 후 리스트: %s" % myList)

"""
중요!
list내에 값이 없다면 오류 발생
+ find 메서드는 없어서 사용 불가 
"""
print("20 값의 위치: %d" % myList.index(20))
myList.insert(2, 222)
print("myList.insert(2, 222) 후 리스트: %s" % myList)
myList.remove(222)
print("myList.remove(222) 후 리스트: %s" % myList)
myList.extend([77, 77, 99])
print("myList.extend([77, 77, 99]) 후 리스트: %s" % myList)
print("77 값의 개수: %d" % myList.count(77))