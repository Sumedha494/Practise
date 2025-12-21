#!/usr/bin/env python
# coding: utf-8

# In[1]:


def linear_search(arr, target):
    """
    Performs linear search to find target in array

    Parameters:
    arr: List of elements to search
    target: Element to find

    Returns:
    Index of target if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1 


# In[2]:


my_list = [10, 25, 30, 45, 50, 65, 70]

target1 = 45
target2 = 100

result1 = linear_search(my_list, target1)
result2 = linear_search(my_list, target2)

if result1 != -1:
    print(f"✅ Element {target1} found at index {result1}")
else:
    print(f"❌ Element {target1} not found")

if result2 != -1:
    print(f"✅ Element {target2} found at index {result2}")
else:
    print(f"❌ Element {target2} not found")


# In[3]:


def linear_search_visual(arr, target):
    """
    Linear search with step-by-step visualization
    """
    print(f"🔍 Searching for {target} in {arr}")
    print("-" * 40)

    for i in range(len(arr)):
        print(f"Step {i+1}: Checking index {i} → value = {arr[i]}", end="")

        if arr[i] == target:
            print(" ✅ FOUND!")
            return i
        else:
            print(" ❌ Not a match")

    print("-" * 40)
    print("Element not found in the list")
    return -1

numbers = [5, 12, 8, 3, 17, 9]
linear_search_visual(numbers, 17)


# In[4]:


def linear_search_all(arr, target):
    """
    Find all occurrences of target in array
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

my_list = [1, 3, 5, 3, 7, 3, 9]
target = 3

result = linear_search_all(my_list, target)
print(f"Element {target} found at indices: {result}")
print(f"Total occurrences: {len(result)}")


# In[ ]:




