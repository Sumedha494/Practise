#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = 5

print(f"=== {number} ka Table ===")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


# In[2]:


number = int(input("Konse number ka table chahiye? "))

print(f"\n📊 {number} ka Multiplication Table:")
print("-" * 20)

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")


# In[3]:


for num in range(1, 11):
    print(f"\n📌 Table of {num}")
    print("=" * 15)
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


# In[8]:


# Matrix style multiplication table
print("    ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print("\n" + "-" * 45)

for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()


# In[9]:


import pandas as pd

data = {}
for i in range(1, 11):
    data[i] = [i * j for j in range(1, 11)]

df = pd.DataFrame(data, index=range(1, 11))
print("📊 Multiplication Table (1-10)")
df


# In[10]:


number = 7
i = 1

print(f"🔢 {number} ka Table (While Loop)")
while i <= 10:
    print(f"{number} × {i} = {number * i}")
    i += 1


# In[11]:


def multiplication_table(num, limit=10):
    """Kisi bhi number ka table print kare"""
    print(f"\n🎯 {num} ka Multiplication Table")
    print("=" * 25)
    for i in range(1, limit + 1):
        print(f"{num} × {i:2} = {num * i:3}")

multiplication_table(8)
multiplication_table(12, 15)  

