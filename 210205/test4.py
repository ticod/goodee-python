# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:01:35 2021

@author: Dohun

4. 홍길동 씨의 주민등록번호는 881120-106234이다. 홍길동씨의 주민등록 번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.

881120

1068234
"""

hong = "881120-106234"

front = hong.split("-")[0]
back = hong.split("-")[1]

print(front)
print(back)
