#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('hi,%s' % 'cbw')
a=len('cbw')
print(a)
if a>0:
    print(a)
else:
    print(0)
print(abs(-10)) 
b={'chenbenwei':100,'chenbenyou':95}
print(b['chenbenwei'])
b['cby']=50
print(b['cby'])
3+8
x="a"
y="b"
print(x,end="")
print(y,end="")

import re
re.match(r"^\d{3}\-\d{3,8}$","010-12345")
if re.match(r"^\d{3}\-\d{3,8}$","010-12345"):
    print("ok")
else:
    print("failed")
print(re.split(r"\s\+","a,b,c  d"))
m=re.match(r"^(\d{3})-(\d{3,8})$","010-12345")
print(m)
print(m.group(1))
print(m.group(2))
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
      print('%s: %s' % (k, v))
print('Data:', data.decode('utf-8'))
