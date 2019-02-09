#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = int(input())
ar = []
for i in range(1, num+1):
    if (num % i == 0):
        ar.append(i)
        
print(ar)
    

