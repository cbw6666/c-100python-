# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:41:33 2018
给一个不多于 5 位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
@author: dk
"""
x=int(input("请输入一个数："))
a=x//10000
b=x%10000//1000
c=x%1000//100
d=x%100//10
e=x%10
if a!=0:
    print("5位",e,d,c,b,a)

    

