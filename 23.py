# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:01:17 2018
一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同
@author: dk
"""
x=int(input("输入一个数字："))
x=str(x)
for i in range(len(x)//2):
    if x[i]!=x[-i-1]:
        print("no")
        break
print("yes")

