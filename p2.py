# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:29:35 2018

@author: dk
一个整数，它加上 100 后是一个完全平方数，再加上 268 又是一个完全平方数，请
问该数是多少？
"""
import math
for e in range(10000):
    if int(math.sqrt(e+100))*int(math.sqrt(e+100))==e+100:
        if int(math.sqrt(e+268))*int(math.sqrt(e+268))==e+268:
            print(e)
            
