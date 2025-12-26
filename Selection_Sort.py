#!/usr/bin/env python
# coding: utf-8

# In[1]:


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# In[2]:


arr = [64, 25, 12, 22, 11]
print("Original:", arr)


# In[3]:


sorted_arr = selection_sort(arr.copy())
print("Sorted:", sorted_arr)


# In[4]:


arr2 = [5, 1, 4, 2, 8]
print("Before:", arr2)
print("After:", selection_sort(arr2))


# In[5]:


names = ['Zara', 'Amit', 'Rahul', 'Priya']
print("Before:", names)
print("After:", selection_sort(names))


# In[6]:


def selection_sort_steps(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Pass {i+1}: {arr}")

    return arr


# In[7]:


data = [64, 25, 12, 22, 11]
print("Original:", data)
print()
selection_sort_steps(data)


# In[8]:


import random

random_arr = [random.randint(1, 100) for _ in range(10)]
print("Random:", random_arr)
print("Sorted:", selection_sort(random_arr.copy()))


# In[ ]:




