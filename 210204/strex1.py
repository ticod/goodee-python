# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:36:31 2021

@author: Dohun

strex1.py 
"""

print("안녕하세요")
print("안녕하세요"[0])
print("안녕하세요"[4])
print("안녕하세요"[-1])
print("안녕하세요"[-2])

# 슬라이싱
print("안녕하세요"[1:3])  # 1번 ~ 2번 인덱스
print("안녕하세요"[:3])  # 0번 ~ 2번
print("안녕하세요"[3:])  # 3번 ~ 끝
print("안녕하세요"[::2])  # 2칸씩
print("안녕하세요"[::-1])  # 역순
print("안녕하세요"[::-2])  # 역순 2칸씩 

print(len("안녕하세요"))
print(type(len("안녕하세요"))) 

# l 문자의 개수 출력 
a = "hello"
count = 0

for ch in a:
    if ch == "l":
        count += 1
print("'hello' 문자열 중 l 문자의 개수: ", count) 

# l 문자의 개수 출력 (함수) 
print("'hello' 문자열 중 l 문자의 개수: ", a.count("l")) 

# 인덱스 값
print("'hello' 문자열 중 l 문자의 인덱스: ", a.find("l"))
print("'hello' 문자열 중 l 문자의 인덱스: ", a.find("a"))

print("'hello' 문자열 중 l 문자의 인덱스: ", a.index("l"))
# print("'hello' 문자열 중 l 문자의 인덱스: ", a.index("a"))  # 에러 발생!

# 리스트 (배열)
arr = [10, 20, 30, 40, 50, 60, 70]
print(arr[:2])
print(arr[::2])
print(arr[1::2])
print(arr[::-1])
print(arr[::-2])
print(arr[-2::-2])

numSum = 0
for i in arr:
    numSum += i
print(numSum)
print(numSum / len(arr))