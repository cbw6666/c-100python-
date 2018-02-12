# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 20:31:31 2018
求100内的素数
@author: dk
"""
for i in range(2,101):
    fg = 0
    for j in range(2,i-1):
        if i%j == 0:
            fg = 1
            break
    if fg == 0:
        print (i,end=" ")


    
    