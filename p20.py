# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:09:51 2018
利用递归函数调用方式，将所输入的 5 个字符，以相反顺序打印出来。
@author: dk
"""
def palin(n):
     next=0
     if n<=1:
         next=input()
         print(next)
     else:
        next=input()
        palin(n-1)
        print(next)
i=5
palin(i)

         
         
