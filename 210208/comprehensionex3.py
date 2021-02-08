# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:03:34 2021

@author: Dohun

comprehensionex3.py
"""

products = {"냉장고": 220, "건조기": 140, "TV": 130, "세탁기": 150, "오디오": 50}
print(products)

product1 = {}

for p, v in products.items():
    if v < 200:
        product1.update({p:v})
        
print(product1)

print({p:v for p, v in products.items() if v < 200})

