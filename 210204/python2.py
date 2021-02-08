# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:13:01 2021

@author: Dohun

python2.py
"""

a = int(input("값 1 입력: "))
b = int(input("값 2 입력: "))
result = a + b
print(a, "+", b, "=", result)
# print(a + "+" + b + "=" + result)
"""
오류 발생 이유 =
    문자열 + 숫자형 연산 불가
"""
print("안" + "녕")
"""
문자열 + 문자열 연산 가능
    (연산자 오버로딩)
"""

print("%d + %d = %d", (a, b, result))
print("안녕하세요", end="")  # 마지막 라인 넘김 X
print("홍길동 입니다.")
# end : 마지막 문자를 지정할 수 있다

# format 함수 사용
print("{0:d} {1:5d} {2:05d}".format(100, 200, 300))
print("{2:d} {1:5d} {0:05d}".format(100, 200, 300))

# * 연산자
print("abc"*3)

# """ 문자열 연결 출력
print("안녕하세요 홍길동입니다" 
      + "반갑습니다 어쩌구 저쩌구...")
print("""안녕하세요 홍길동입니다 
      반갑습니다 어쩌구 저쩌구...""")
print('''안녕하세요 홍길동입니다 
      반갑습니다 어쩌구 저쩌구...''')
