# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:22:21 2018
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前 20 项之和
@author: dk
"""
a=2.0
b=1.0
s=0
for n in range(1,21):
    s+=a/b
    t=a
    a=a+b
    b=t
print(s)
