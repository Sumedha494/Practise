#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Method 1
base = int(input("Base number enter karein: "))
exponent = int(input("Power (exponent) enter karein: "))

result = base ** exponent

print(f"{base} ki power {exponent} hai: {result}")


# In[ ]:


#Method 2
base = int(input("Base: "))
exponent = int(input("Power: "))

result = pow(base, exponent)

print(f"Result: {result}")


# In[ ]:


#Method 3 
def power_recursive(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power_recursive(base, exp - 1)

b = int(input("Base: "))
e = int(input("Power: "))

ans = power_recursive(b, e)
print(f"Recursion se answer: {ans}")

