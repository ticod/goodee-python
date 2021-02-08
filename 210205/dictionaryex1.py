# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:37:03 2021

@author: Dohun

dictionaryex1.py

"""

singer = {}
singer['이름'] = '트와이스'
singer['구성원 수'] = 9
singer['데뷔곡'] = '우아하게'
singer['소속사'] = 'JYP'

for i in singer.keys():
    print("%s => %s" % (i, singer[i]))
    
print("singer 자료형: ", type(singer))
print("singer: ", singer)
print("singer.keys() 자료형: ", type(singer.keys()))
print("singer.keys(): ", singer.keys())