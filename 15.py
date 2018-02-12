# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:47:33 2018
一球从 100 米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
第 10 次落地时，共经过多少米？第 10 次反弹多高？
@author: dk
"""
sn=100
hn=sn/2
for n in range(2,11):
    sn+=2*hn
    hn/=2
print(sn)
print(hn)

