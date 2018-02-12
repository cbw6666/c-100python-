# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:40:46 2018
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
@author: dk
"""
import string
s=input("输入一个字符串：")
letters=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1
print("char=%d,space=%d,digit=%d,others=%d"%(letters,space,digit,others))
