#!/usr/bin/env python
# coding: utf-8

# In[5]:


num = int(input("Enter a number:"))
temp = num 
sum = 0 

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")


