# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:23:57 2018
数组逆序输出
@author: dk
"""
if __name__=="__main__":
    a=[9,6,5,4,1]
    n=len(a)
    for i in range(len(a)//2):
        a[i],a[n-i-1]=a[n-i-1],a[i]
    print(a)
