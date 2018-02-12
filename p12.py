# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:31:13 2018
利用条件运算符的嵌套来完成此题：学习成绩>=90 分的同学用 A 表示，60-
89 分之间的用 B 表示，
60 分以下的用 C 表示。

@author: dk
"""
score=int(input("输入分数："))
if score>=90:
    grade="A"
elif score>=60:
    grade="B"
else:
    grade="C"
print("%d 属于 %s"%(score,grade))    