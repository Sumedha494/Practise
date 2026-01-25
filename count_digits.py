#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("Enter a number:"))
count = 0 

while num > 0:
    count += 1
    num //= 10

print("Digits: ",count)

