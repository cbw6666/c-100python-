# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:22:23 2018

@author: dk
"""

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j)and(i!=k)and(j!=k):
                print(i,j,k)