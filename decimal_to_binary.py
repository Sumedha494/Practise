#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Method 1
num = int(input("Koi decimal number enter karein: "))

binary_num = bin(num)[2:]
print(f"{num} ka Binary roop hai: {binary_num}")


# In[ ]:


#Method 2
num = int(input("Koi decimal number enter karein: "))

binary_num = f"{num:b}"

print(f"Binary: {binary_num}")


# In[ ]:


#Method 3
def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary_str = ""
    while n > 0:
        remainder = n % 2    
        binary_str = str(remainder) + binary_str  
        n = n // 2          

    return binary_str

number = int(input("Number enter karein: "))
result = decimal_to_binary(number)

print(f"Logic se nikala gaya Binary: {result}")

