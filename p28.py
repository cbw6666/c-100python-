# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:27:35 2018
求3*3对角元素之和
@author: dk
"""
if __name__=="__main__":
    a=[]
    sum=0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("niput:\n")))
    for i in range(3):
        sum+=a[i][j]
         print(sum)
