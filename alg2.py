#!/usr/bin/env python
# coding: utf-8

# In[ ]:

num = int(input())
ar = []

if num > 0: 
    for i in range(1, num+1):
        if (num % i == 0):
            ar.append(i)
    print(ar)
elif num<0: 
    for i in range(-1, num-1, -1):
        if (num % i == 0):
            ar.append(i)
    print(ar)
    

