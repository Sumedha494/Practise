#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input("Enter number of terms: "))
a, b = 0, 1

for _ in range(n):
    print(a , end=" ")
    a, b = b, a + b

