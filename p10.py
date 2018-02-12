# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:44:52 2018
打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数
@author: dk
"""
for n in range(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i**3+j**3+k**3:
        print("%-5d"%n)

