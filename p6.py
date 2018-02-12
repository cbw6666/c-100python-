# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:40:06 2018
输出 9*9 口诀
@author: dk 
"""
for i in range(1,10):
   for j in range(1,10):
        result=i*j
        print("%d * %d=% -3d" % (i,j,result))
"""
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print ('%d * %d = % -3d' % (i,j,result))
"""