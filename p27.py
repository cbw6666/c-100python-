# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 08:59:15 2018
对十个数进行排序
@author: dk
"""
if __name__=="__main__":
    n=10
    print("请输入十个数：\n")
    l=[]
    for i in range(n):
        l.append(int(input("input a number:\n")))
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if l[min]>l[j]:
                min=j
               # l[i],l[min]=l[min],l[i]
                l[i]=l[min]
                l[min]=l[i]
    for i in range(n):
        print(l[i])
            
    

