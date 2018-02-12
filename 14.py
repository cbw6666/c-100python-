# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:52:59 2018
求 s=a+aa+aaa+aaaa+aa...a 的值，其中 a 是一个数字。例如
2+22+222+2222+22222(此时
共有 5 个数相加)，几个数相加有键盘控制。
@author: dk
"""
from functools import reduce
tn=0
sn=[]
n=int(input("n=:\n"))
a=int(input("a=:\n"))
for count in range(n):
    tn=tn+a
    a=a*10
    sn.append(tn)
    print(tn)
sn=reduce(lambda x,y:x+y,sn)
print(sn)

