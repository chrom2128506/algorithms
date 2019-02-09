#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np 

f = open('zerosones.txt', 'r')
s = f.read()
#print(s)
#print(len(s))
length = 0
for i in range(len(s)): 
    if s[i] == '1':
        for j in range(i, len(s)):
            if s[j] == '0':
                length = j - i
                if(prev_length > length):
                    length = prev_length
                break
    prev_length = length
    
print(length)
f.close()


# In[ ]:





# In[ ]:





# In[ ]:




