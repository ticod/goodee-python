# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:43:58 2021

@author: Dohun
"""

data = """
    park  800905-1234567
    kim   700905-1234567
    choi  850101-a123456
"""

result = []

for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        # isdigit() : 숫자인 경우 True
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + ("*" * 7)
        word_result.append(word)
    # join : list의 요소를 연결
    result.append(" ".join(word_result))
print("\n".join(result))

# 문자열에서 문자 종류 관련 함수
instr = "a123"
if instr.isdigit():
    print(instr, "=> 숫자입니다")
    
if instr.isalpha():
    print(instr, "=> 문자입니다")
    
if instr.isalnum():
    print(instr, "=> 문자 + 숫자입니다")
    
if instr.islower():
    print(instr, "=> 소문자입니다")
    
if instr.isupper():
    print(instr, "=> 대문자입니다")
    
if instr.isspace():
    print(instr, "=> 공백입니다")
