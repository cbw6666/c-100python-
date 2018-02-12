# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 20:03:08 2018
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
@author: dk
"""
from sys import stdin
letter=stdin.read(1)
stdin.flush()
while letter!="Y":
    if letter=="s":
        print("请输入第二个letter")
        letter=stdin.read()
        stdin.flush()
        if letter=="a":
            print("saturday")
        elif letter=="u":
            print("sunday")
        else:
            print("error data")
            break