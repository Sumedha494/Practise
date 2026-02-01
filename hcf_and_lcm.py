#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Method 1
import math

num1 = int(input("Pehla number enter karein: "))
num2 = int(input("Doosra number enter karein: "))

hcf = math.gcd(num1, num2)

lcm = math.lcm(num1, num2) 

print(f"--------------------------")
print(f"{num1} aur {num2} ka HCF hai: {hcf}")
print(f"{num1} aur {num2} ka LCM hai: {lcm}")


# In[ ]:


#Method 2
def find_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

def find_lcm(x, y):
    hcf = find_hcf(x, y)
    lcm = (x * y) // hcf 
    return lcm

try:
    a = int(input("Pehla number: "))
    b = int(input("Doosra number: "))

    my_hcf = find_hcf(a, b)
    my_lcm = find_lcm(a, b)

    print(f"\nResult:")
    print(f"HCF: {my_hcf}")
    print(f"LCM: {my_lcm}")

except ValueError:
    print("Kripya valid number enter karein.")

