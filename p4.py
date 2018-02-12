# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:17:23 2018
输入三个整数 x,y,z，请把这三个数由小到大输出。
@author: dk
"""

l=[]
for i in range(3):
    x=input(("输入："))
    l.append(x)
l.sort()
print(l)
