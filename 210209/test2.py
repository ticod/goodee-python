# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:36:16 2021

@author: Dohun

​

2. Thread를 이용하여 

1~10000까지의 합을 5개의 스레드로 나눠서 각각의 구간 합을 

스레드 1 : 1 ~ 2000까지의 합

스레드 2 : 2001 ~ 4000까지의 합

스레드 3 : 4001 ~ 6000까지의 합

스레드 4 : 6001 ~ 8000까지의 합

스레드 5 : 8001 ~ 10000까지의 합

main에서 더하여 총합을 구하는 프로그램 작성하기

​

[결과]

50005000
"""
import threading

class Sum:
    start = 0
    end = 0
    sum = 0
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def getSum(self):
        for i in range(self.start, self.end + 1):
            self.sum += i
        return self.sum

if __name__ == "__main__":
    sumList = []
    thList = []
    
    for i in range(0, 5):
        sumList.append(Sum((i * 2000) + 1, (i + 1) * 2000))
        thList.append(threading.Thread(target = sumList[i].getSum()))
        thList[i].start()
        
    for th in thList:
        th.join()
        
    sum = 0
    for s in sumList:
        sum += s.sum
        
    print(sum)
