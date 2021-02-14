# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:04:35 2021

@author: Dohun
"""

import re

data = '''
    park  800905-1234567
    kim   700905-1234567
    choi  850101-a123456
'''

pat = re.compile("(\d{6,7})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

"""
() : 그룹화
[] : 문자
{} : 갯수
{N, M} : N개 이상 M개 이하
\d : 숫자
\g<N> : N 번째 그룹
? : 0 OR 1
* : 0 이상
+ : 1 이상
"""