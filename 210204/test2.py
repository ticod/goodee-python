# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:41:40 2021

@author: Dohun

test2.py

소문자와 숫자로 이루어진 문자를 암호화 하고 복호화 하는 프로그램 작성하기

원래 문자 : a b c d e f g h i j k l m n o p q r s t u v w x y z 

암호 문자 : ` ~ ! @ # $ % ^ & * ( ) - _ + = | [ ] { } ; : , . /

​

원래 숫자 : 0 1 2 3 4 5 6 7 8 9 

암호 숫자 : q w e r t y u i o p

​

문자를 입력하세요 

원문 : abc123

암호문

`~!wer

복호화

abc123
"""

org = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
crypt = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","+","=","|","[","]","{","}",";",":",",",".","/","q","w","e","r","t","y","u","i","o","p"]

print("문자를 입력하세요")
str = input("원문: ")
orgStr = ""
changeStr = ""

for i in range(0, len(str)):
    index = org.index(str[i])
    changeStr += crypt[index]
    
print("암호문: ", changeStr)

for i in range(0, len(changeStr)):
    index = crypt.index(changeStr[i])
    orgStr += org[index]
    
print("복호문: ", orgStr)