# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:01:45 2018

@author: dk
"""

import sys
for i in range(1,10):
    for j in range(1,i+1):
        sys.stdout.write('%d * %d = %-3d' % (j,i,i*j))
        sys.stdout.write(' ')
print("")
sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
print ('')
for i in range(1,11):
    for j in range(1,i):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
print('')