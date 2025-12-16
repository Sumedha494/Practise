#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("🧮 Python Calculator")
print("Made by: Sumedha Sadaphal")


# In[ ]:


def add(a, b):
    return a + b

print("5 + 3 =", add(5, 3))


# In[ ]:


def subtract(a, b):
    return a - b

print("10 - 4 =", subtract(10, 4))


# In[ ]:


def multiply(a, b):
    return a * b

print("6 × 7 =", multiply(6, 7))


# In[ ]:


def divide(a, b):
    if b == 0:
        return "Error: Zero se divide nahi ho sakta!"
    return a / b

print("20 ÷ 4 =", divide(20, 4))
print("10 ÷ 0 =", divide(10, 0))


# In[ ]:


def power(a, b):
    return a ** b

print("2 ^ 5 =", power(2, 5))


# In[ ]:


def sqrt(a):
    if a < 0:
        return "Error: Negative number!"
    return a ** 0.5

print("√144 =", sqrt(144))
print("√81 =", sqrt(81))


# In[ ]:


def modulus(a, b):
    return a % b

print("17 % 5 =", modulus(17, 5))


# In[ ]:


print("="*30)
print("📊 All Operations Test")
print("="*30)

print(f"8 + 2 = {add(8, 2)}")
print(f"15 - 7 = {subtract(15, 7)}")
print(f"4 × 9 = {multiply(4, 9)}")
print(f"100 ÷ 5 = {divide(100, 5)}")
print(f"3 ^ 4 = {power(3, 4)}")
print(f"√225 = {sqrt(225)}")
print(f"23 % 7 = {modulus(23, 7)}")


# In[ ]:


print("🔢 Enter Your Numbers:")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print(f"\n📊 Results:")
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} × {num2} = {multiply(num1, num2)}")
print(f"{num1} ÷ {num2} = {divide(num1, num2)}")


# In[ ]:


print("\n🧮 CALCULATOR MENU")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("\nChoose (1-4): ")
a = float(input("First number: "))
b = float(input("Second number: "))

if choice == '1':
    print(f"Answer: {add(a, b)}")
elif choice == '2':
    print(f"Answer: {subtract(a, b)}")
elif choice == '3':
    print(f"Answer: {multiply(a, b)}")
elif choice == '4':
    print(f"Answer: {divide(a, b)}")
else:
    print("Invalid choice!")


# In[ ]:


print("\n" + "="*30)
print("✅ Calculator Complete!")
print("🌟 Thank You!")
print("="*30)

