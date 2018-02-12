# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:28:40 2018
一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如 6=1＋2＋3.找出一千以内的所有完数
@author: dk
"""
for j in range(2,2001):
    k=[]
    n=-1
    s=j
    for i in range(1,j):
        if j%i==0:
            n+=1
            s-=i
            k.append(i)
    if s==0:
        print(j)
        for i in range(n+1):
            print(k[i])
            print(" ")
   #     print(k[n])
