# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:01:40 2021

@author: Dohun

5. 화면에서 주민등록번호를 000000-0000000 형태로 입력받는다.

 주민등록번호 뒷자리의  첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 조회하여

성별을 나타내는 숫자가 1,3 이면 남자로 2,4면 여자로 출력한다. 그외는 내국인아님으로 출력한다.
"""

num = input("주민 등록 번호 입력: ")

backNum = num.split("-")[1]

if backNum[0] == "1" or backNum[0] == "3":
    print("남자입니다")
elif backNum[0] == "2" or backNum[0] == "4":
    print("여자입니다")
else:
    print("내국인 아님")
    