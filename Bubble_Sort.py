#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# In[2]:


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", numbers)


# In[3]:


sorted_list = bubble_sort(numbers.copy())
print("Sorted List:", sorted_list)


# In[4]:


user_input = input("Numbers enter karo (comma se): ")
my_list = [int(x) for x in user_input.split(",")]
print("Sorted:", bubble_sort(my_list))


# In[5]:


def bubble_sort_steps(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Pass {i+1}: {arr}")

    return arr


# In[6]:


test = [5, 1, 4, 2, 8]
bubble_sort_steps(test)


# In[7]:


def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# In[8]:


nums = [3, 7, 1, 9, 2]
print("Descending:", bubble_sort_desc(nums.copy()))


# In[ ]:




