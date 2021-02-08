# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:32:09 2021

@author: Dohun

ifex1.py
"""

score = 50

if score >= 90:
    print("A 학점")
else :
    if score >= 80:
        print("B 학점")
    else:
        if score >= 70:
            print("C 학점")
        else:
            if score >= 60:
                print("D 학점")
            else:
                print("F 학점")
                
if score >= 90:
    print("A 학점")
elif score >= 80:
    print("B 학점")
elif score >= 70:
    print("C 학점")
elif score >= 60:
    print("D 학점")
else:
    print("F 학점")