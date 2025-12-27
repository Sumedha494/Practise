#!/usr/bin/env python
# coding: utf-8

# In[1]:


def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15


# In[2]:


celsius = 37
fahrenheit = c_to_f(celsius)
print(f"{celsius}°C = {fahrenheit}°F")


# In[3]:


fahrenheit = 98.6
celsius = f_to_c(fahrenheit)
print(f"{fahrenheit}°F = {celsius:.2f}°C")


# In[4]:


celsius = 100
kelvin = c_to_k(celsius)
print(f"{celsius}°C = {kelvin}K")


# In[5]:


kelvin = 373.15
celsius = k_to_c(kelvin)
print(f"{kelvin}K = {celsius}°C")


# In[7]:


temp = float(input("Temperature enter karo: "))
unit = input("Unit (C/F/K): ").upper()

if unit == 'C':
    print(f"Fahrenheit: {c_to_f(temp):.2f}°F")
    print(f"Kelvin: {c_to_k(temp):.2f}K")
elif unit == 'F':
    print(f"Celsius: {f_to_c(temp):.2f}°C")
elif unit == 'K':
    print(f"Celsius: {k_to_c(temp):.2f}°C")


# In[9]:


print("C\t|\tF\t|\tK")
print("-" * 30)
for c in [0, 10, 20, 30, 37, 100]:
    print(f"{c}\t|\t{c_to_f(c)}\t|\t{c_to_k(c)}")


# In[ ]:




