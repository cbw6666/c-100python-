# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:54:41 2018
求1+2!+3!+...+20!
@author: dk
"""
n=0
s=0
t=1
for n in range(1,21):
    t*=n
    s+=t
print("结果为：%d"%s)

