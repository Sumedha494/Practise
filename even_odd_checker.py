#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# In[ ]:


num = int(input("Enter a number: "))


# In[ ]:


result = check_even_odd(num)
print(f"{num} is {result}")


# In[ ]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numbers:
    print(f"{n} -> {check_even_odd(n)}")


# In[ ]:


check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(7))

