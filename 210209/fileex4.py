# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:51:38 2021

@author: Dohun
"""

import os.path
print("폴더 목록 보기: os.walk 모듈 사용")
for dirName, subDirList, fnames in os.walk("D:/goodee"):
    for fname in fnames:
        print(os.path.join(dirName, fname))
    print(type(subDirList))