#!/usr/bin/env python
# coding: utf-8

# In[1]:


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


# In[2]:


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# In[3]:


arr = [64, 34, 25, 12, 22, 11, 90]
print("Original:", arr)
print("Sorted:", merge_sort(arr))


# In[4]:


arr = [-5, 3, -2, 8, -1, 0]
print("Original:", arr)
print("Sorted:", merge_sort(arr))


# In[5]:


arr = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original:", arr)
print("Sorted:", merge_sort(arr))


# In[6]:


import random
arr = random.sample(range(1, 100), 10)
print("Original:", arr)
print("Sorted:", merge_sort(arr))


# In[ ]:


arr = list(map(int, input("Enter numbers (space separated): ").split()))
print("Sorted:", merge_sort(arr))


# In[ ]:




