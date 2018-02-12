# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:31:48 2018
输入a,b,c三个数，按大小顺序输出
@author: dk
"""
if __name__=="__main__":
    n1=int(input("n1=:"))
    n2=int(input("n2=:"))
    n3=int(input("n3=:"))
    def swap(p1,p2):
        return p2,p1
    if n1>n2:n1,n2=swap(n1,n2)
    if n1>n3:n1,n3=swap(n1,n3)
    if n2>n3:n2,n3=swap(n2,n3)
    print(n1,n2,n3)