# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:50:02 2018
有一对兔子，从出生后第 3 个月起每个月都生一对兔子，小兔子长到第
三个月
后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
@author: dk
"""
f1=1
f2=1
for i in range(1,21):
    print("%12d %12d" %(f1,f2))
    if i%2==0:
        print("")
    f1=f1+f2
    f2=f1+f2
