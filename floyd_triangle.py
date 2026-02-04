#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Simple Floyd's Triangle for fix number of rows.
rows = 5
num = 1

print("🔺 Floyd's Triangle")
print("=" * 20)

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()  


# In[ ]:


# triangle from user input
rows = int(input("Kitni rows chahiye? "))
num = 1

print(f"\n🔺 Floyd's Triangle ({rows} rows)")
print("-" * 30)

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(f"{num:3}", end=" ") 
        num += 1
    print()


# In[ ]:


# While loop version of Floyd's Triangle
rows = 5
num = 1
i = 1

print("🔺 Floyd's Triangle (While Loop)")

while i <= rows:
    j = 1
    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1


# In[ ]:


# using Function
def floyds_triangle(rows):
    """Floyd's Triangle generate karta hai"""
    num = 1

    print(f"\n🔺 Floyd's Triangle - {rows} Rows")
    print("=" * (rows * 4))

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(f"{num:4}", end="")
            num += 1
        print()

    print(f"\nTotal Numbers: {num - 1}")

floyds_triangle(5)
floyds_triangle(8)


# In[ ]:


# Reverse/Inverted Floyd's Triangle
rows = 5

total = (rows * (rows + 1)) // 2
num = total

print("🔻 Reverse Floyd's Triangle")
print("=" * 25)

for i in range(rows, 0, -1):
    start = num - i + 1
    for j in range(i):
        print(f"{start + j:3}", end=" ")
    num = start - 1
    print()


# In[ ]:


# Alphabets Floyd's Triangle
rows = 5
char_code = 65  

print("🔤 Floyd's Triangle (Alphabets)")
print("=" * 25)

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(chr(char_code), end=" ")
        char_code += 1
    print()


# In[ ]:


# Stars pattern
rows = 5

print("⭐ Floyd's Triangle (Stars)")
print("=" * 20)

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# In[ ]:


# Binary Floyd's Triangle (0 and 1)
rows = 5

print("🔢 Binary Floyd's Triangle")
print("=" * 25)

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()


# In[ ]:


# One-liner approach
rows = 5
num = 1

print("🔺 Floyd's Triangle (List Comprehension)")

for i in range(1, rows + 1):
    row = [str(num + j) for j in range(i)]
    print(" ".join(row))
    num += i


# In[ ]:


# Centered Floyd's Triangle
rows = 5
num = 1
max_width = rows * 4

print("🔺 Centered Floyd's Triangle")
print("=" * max_width)

for i in range(1, rows + 1):
    row = ""
    for j in range(1, i + 1):
        row += f"{num:3} "
        num += 1
    print(row.center(max_width))

