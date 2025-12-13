#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# In[2]:


arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target = 23

result = binary_search_iterative(arr, target)
print(f"Element {target} found at index: {result}")


# In[3]:


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


# In[4]:


arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target = 38

result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Element {target} found at index: {result}")


# In[5]:


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Array: {arr}")

target = int(input("Enter number to search: "))
result = binary_search_iterative(arr, target)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")


# In[6]:


import bisect

arr = [2, 5, 8, 12, 16, 23, 38, 45]
target = 16

index = bisect.bisect_left(arr, target)

if index < len(arr) and arr[index] == target:
    print(f"Found at index {index}")
else:
    print("Not found")


# In[7]:


def binary_search_visual(arr, target):
    left, right, step = 0, len(arr) - 1, 1

    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        step += 1

    return -1


# In[8]:


arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 13

result = binary_search_visual(arr, target)
print(f"\nResult: Index {result}")


# In[ ]:




