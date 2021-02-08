# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:29:50 2021

@author: Dohun

6. 컴퓨터가 임의의 서로다른 숫자 4개를 저장하고, 화면에서 서로다른 4자리 숫자를 입력받아 

   입력받은 숫자와 저장된 숫자를 비교하여 같은 숫자가 있는 경우 자리수가 맞으면 strike, 자리수가 틀리면 

   ball로 출력하는 프로그램 작성하기. 컴퓨터가 저장한 숫자를 몇번만에 맞췄는지 입력횟수를 출력하기

​

컴퓨터 저장 숫자 : [0, 2, 6, 7]  인경우

​

서로다른 4자리 숫자를 입력하세요: 1234

Strike: 1 Ball: 0

​

서로다른 4자리 숫자를 입력하세요: 5678

Strike: 0 Ball: 2

​

서로다른 4자리 숫자를 입력하세요: 1678

Strike: 0 Ball: 2

​

서로다른 4자리 숫자를 입력하세요: 5278

Strike: 1 Ball: 1

​

서로다른 4자리 숫자를 입력하세요: 0267

5 번만에 맞췄습니다.
"""
import random

key = []

while len(key) < 4:
    tempNum = random.randrange(0, 10)
    try:
        key.index(tempNum)
    except:
        key.append(tempNum)  
        
print("정답: ", key)
count = 0

while True:
    count += 1
    answer = input("서로 다른 4자리 숫자를 입력하세요: ")
    strike = 0
    ball = 0
    
    for i in range(0, 4):
        try:
            index = key.index(int(answer[i]))
            if i == index:
                strike += 1
            else:
                ball += 1
        except:
            pass
            
    if strike == 4:
        print("%d번 만에 맞췄습니다!" % count)
        break
    else:
        print("Strike: %d, Ball: %d" % (strike, ball))
    
