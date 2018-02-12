# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:02:25 2018
题目：两个乒乓球队进行比赛，各出三人。甲队为 a,b,c 三人，乙队为 x,y,z 三人。已抽签
决定比赛名单。有人向队员打听比赛的名单。a 说他不和 x 比，c 说他不和 x,z 比，请编程找出三队赛手的名单
ord()函数返回的是字母的ascii码
@author: dk
"""
for i in range(ord('x'),ord('z')+1):
    for j in range(ord('x'),ord('z')+1):
        if i!=j:
            for k in range(ord('x'),ord('z')+1):
                if (i!=k)and(j!=k):
                    if (i!=ord('x'))and(k!=ord('x'))and(k!=ord('z')):
                        print("a-%s\t b-%s\t c-%s"%(chr(i),chr(j),chr(k)))

