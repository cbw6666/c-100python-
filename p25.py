# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 20:19:18 2018
函数调用练习
@author: dk
"""
def hello_world():
    print("hello world")
def three_hellos():
    for i in range(3):
        hello_world()
if __name__=="__main__":
    three_hellos()
        
    
