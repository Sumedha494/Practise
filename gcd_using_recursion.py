#!/usr/bin/env python
# coding: utf-8

# In[1]:


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

try:
    num1 = int(input("Pehla number enter karein: "))
    num2 = int(input("Doosra number enter karein: "))

    result = gcd_recursive(num1, num2)

    print(f"GCD of {num1} and {num2} is: {result}")

except ValueError:
    print("Please valid numbers enter karein.")

