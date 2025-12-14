#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


# In[2]:


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Array:", arr)


# In[3]:


target = 50
result = binary_search(arr, target, 0, len(arr)-1)
print(f"Element {target} found at index: {result}")


# In[4]:


target = 25
result = binary_search(arr, target, 0, len(arr)-1)
print(f"Element {target} found at index: {result}")


# In[5]:


target = int(input("Enter element to search: "))
result = binary_search(arr, target, 0, len(arr)-1)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")


# In[6]:


test_cases = [10, 45, 90, 100]

for t in test_cases:
    res = binary_search(arr, t, 0, len(arr)-1)
    print(f"{t} → Index: {res}")


# In[ ]:




