#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input("Enter a number : "))
total = 0

for i in range(1,num):
    if num % i == 0:
        total += i

if total == num:
    print("Perfect Number")
else:
    print("Not Perfect")


# In[ ]:




