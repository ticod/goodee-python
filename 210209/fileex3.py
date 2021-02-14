# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:40:12 2021

@author: Dohun
"""

import os.path


file = "nofile"
file = "regularex3.py"
file = "D:/goodee"

if os.path.isfile(file):
    print("Yes. It is a file")
elif os.path.isdir(file):
    print("Yes. It is a directory")

if os.path.exists(file):
    print("Something exist")
else:
    print("Nothing")