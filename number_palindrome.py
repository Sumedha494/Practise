#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

