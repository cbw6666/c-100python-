# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:30:27 2018
将一个正整数分解质因数。例如：输入 90,打印出 90=2*3*3*5。
@author: dk
"""
n=int(input("input number:\n"))
print("n=%d"%n)
for i in range(2,n+1):
    while n!=i:
        if n%i==0:
            print(str(i),end="")
            print("*",end="")
            n=n/i
        else:
            break
print("%d"%n,end="")

