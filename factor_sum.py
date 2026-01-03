#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("Konsa number check karna hai? "))


# In[2]:


factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)


# In[3]:


print(f"{num} ke factors hain: {factors}")


# In[4]:


total_sum = sum(factors)
print(f"Sabka jod (Sum) = {total_sum}")


# In[5]:


proper_sum = total_sum - num
print(f"Number ko chord kar sum = {proper_sum}")


# In[6]:


def get_factor_sum(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += i
    return s

print(get_factor_sum(12))
print(get_factor_sum(28))

