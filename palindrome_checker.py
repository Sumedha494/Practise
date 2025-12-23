#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]  

word = "madam"
if is_palindrome(word):
    print(f"'{word}' Palindrome hai ✓")
else:
    print(f"'{word}' Palindrome nahi hai ✗")


# In[ ]:




