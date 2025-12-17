#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# In[2]:


factorial(5)


# In[3]:


factorial(0)


# In[4]:


factorial(10)


# In[5]:


for i in range(6):
    print(f"{i}! = {factorial(i)}")


# In[6]:


for i in range(6):
    print(f"{i}! = {factorial(i)}")


# In[7]:


num = int(input("Number daalo: "))
print(f"{num}! = {factorial(num)}")


# In[8]:


num = int(input("Number daalo: "))

if num < 0:
    print("Negative number allowed nahi hai!")
else:
    print(f"{num}! = {factorial(num)}")


# In[ ]:




