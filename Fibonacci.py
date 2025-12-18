#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


# In[2]:


fibonacci(10)


# In[3]:


def fib_list(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# In[4]:


print(fib_list(10))


# In[5]:


def nth_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# In[6]:


print(nth_fib(10))


# In[7]:


n = int(input("Kitne numbers chahiye? "))
print(fib_list(n))


# In[8]:


a, b = 0, 1
count = 0

while count < 10:
    print(a)
    a, b = b, a + b
    count += 1


# In[9]:


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


# In[10]:


for i in range(10):
    print(fib_recursive(i), end=" ")


# In[11]:


for i in range(10):
    print(fib_recursive(i), end=" ")


# In[ ]:


print(list(fib_gen(10)))

