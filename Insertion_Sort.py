#!/usr/bin/env python
# coding: utf-8

# In[1]:


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# In[2]:


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numbers)


# In[3]:


sorted_arr = insertion_sort(numbers.copy())
print("Sorted:", sorted_arr)


# In[4]:


words = ["banana", "apple", "cherry"]
print(insertion_sort(words))


# In[5]:


nums = [-5, 2, -8, 10, 0]
print(insertion_sort(nums))


# In[6]:


def insertion_sort_steps(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Step {i}: {arr}")
    return arr


# In[7]:


test = [5, 2, 4, 6, 1, 3]
insertion_sort_steps(test)


# In[8]:


import time

big_list = list(range(1000, 0, -1))
start = time.time()
insertion_sort(big_list)
end = time.time()
print(f"Time: {end-start:.4f} seconds")


# In[ ]:




