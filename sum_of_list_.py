#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers = [1, 2, 3, 4, 5]

total = sum(numbers)

print(f"List: {numbers}")
print(f"Sum: {total}")


# In[2]:


numbers = [10, 20, 30, 40, 50]

total = 0
for num in numbers:
    total += num

print(f"List: {numbers}")
print(f"Sum: {total}")


# In[3]:


numbers = [5, 10, 15, 20, 25]

total = 0
i = 0

while i < len(numbers):
    total += numbers[i]
    i += 1

print(f"List: {numbers}")
print(f"Sum: {total}")


# In[8]:


n = int(input("Kitne numbers enter karna hai? "))

numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)

print(f"\n📊 List: {numbers}")
print(f"📈 Sum: {total}")


# In[9]:


from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print(f"List: {numbers}")
print(f"Sum: {total}")


# In[10]:


def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
total = recursive_sum(numbers)

print(f"List: {numbers}")
print(f"Sum (Recursive): {total}")


# In[11]:


import numpy as np

numbers = [10, 20, 30, 40, 50]

arr = np.array(numbers)
total = np.sum(arr)

print(f"List: {numbers}")
print(f"Sum (NumPy): {total}")


# In[12]:


numbers = [1, 2, 3, 4, 5]
initial_value = 100

total = sum(numbers, initial_value)

print(f"List: {numbers}")
print(f"Initial Value: {initial_value}")
print(f"Total Sum: {total}") 


# In[13]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num

even_sum_v2 = sum([num for num in numbers if num % 2 == 0])

print(f"List: {numbers}")
print(f"Even Numbers Sum: {even_sum}")
print(f"Even Numbers: {[n for n in numbers if n % 2 == 0]}")


# In[14]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_sum = sum([num for num in numbers if num % 2 != 0])

print(f"List: {numbers}")
print(f"Odd Numbers Sum: {odd_sum}")
print(f"Odd Numbers: {[n for n in numbers if n % 2 != 0]}")


# In[15]:


numbers = [10, -5, 20, -15, 30, -10, 40]

positive_sum = sum([n for n in numbers if n > 0])
negative_sum = sum([n for n in numbers if n < 0])
total_sum = sum(numbers)

print(f"List: {numbers}")
print(f"➕ Positive Sum: {positive_sum}")
print(f"➖ Negative Sum: {negative_sum}")
print(f"📊 Total Sum: {total_sum}")


# In[16]:


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0
for row in matrix:
    for num in row:
        total += num

total_v2 = sum(sum(row) for row in matrix)

total_v3 = sum([num for row in matrix for num in row])

print(f"Matrix:")
for row in matrix:
    print(f"  {row}")
print(f"\nTotal Sum: {total}")


# In[17]:


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

start_index = 2
end_index = 6

partial_sum = sum(numbers[start_index:end_index])

print(f"List: {numbers}")
print(f"Range [{start_index}:{end_index}]: {numbers[start_index:end_index]}")
print(f"Partial Sum: {partial_sum}")


# In[18]:


prices = [99.99, 149.50, 299.99, 49.99, 199.00]

total = sum(prices)

print(f"Prices: {prices}")
print(f"Total: ${total:.2f}")


# In[19]:


def list_calculator(numbers):
    """List ki complete calculation"""

    if not numbers:
        print("❌ Empty list!")
        return

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)

    even_sum = sum([n for n in numbers if n % 2 == 0])
    odd_sum = sum([n for n in numbers if n % 2 != 0])

    print("=" * 40)
    print("📊 LIST CALCULATOR REPORT")
    print("=" * 40)
    print(f"📝 List: {numbers}")
    print(f"📈 Sum: {total}")
    print(f"📏 Count: {count}")
    print(f"📊 Average: {average:.2f}")
    print(f"⬆️  Maximum: {maximum}")
    print(f"⬇️  Minimum: {minimum}")
    print(f"🔵 Even Sum: {even_sum}")
    print(f"🟢 Odd Sum: {odd_sum}")
    print("=" * 40)

numbers = [10, 25, 30, 45, 50, 65, 70, 85, 90]
list_calculator(numbers)


# In[20]:


scores = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "Hindi": 88,
    "Computer": 95
}

total = sum(scores.values())
average = total / len(scores)

print("📊 Subject Scores:")
for subject, score in scores.items():
    print(f"  {subject}: {score}")

print(f"\n📈 Total: {total}")
print(f"📊 Average: {average:.2f}")


# In[21]:


numbers = [1, 2, 3, 4, 5]

running_sum = []
total = 0

for num in numbers:
    total += num
    running_sum.append(total)

print(f"Original List: {numbers}")
print(f"Running Sum: {running_sum}")

print("\n📊 Step by Step:")
total = 0
for i, num in enumerate(numbers):
    total += num
    print(f"  Step {i+1}: {num} → Running Total: {total}")


# In[22]:


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

total = sum(list1) + sum(list2) + sum(list3)

element_wise = [a + b + c for a, b, c in zip(list1, list2, list3)]

print(f"List 1: {list1} → Sum: {sum(list1)}")
print(f"List 2: {list2} → Sum: {sum(list2)}")
print(f"List 3: {list3} → Sum: {sum(list3)}")
print(f"\n📊 Total Sum: {total}")
print(f"📈 Element-wise Sum: {element_wise}")


# In[23]:


while True:
    print("\n🔢 LIST SUM CALCULATOR")
    print("=" * 30)
    print("1. Sum of All Elements")
    print("2. Sum of Even Numbers")
    print("3. Sum of Odd Numbers")
    print("4. Sum of Positive Numbers")
    print("5. Sum of Negative Numbers")
    print("6. Sum of Range")
    print("7. Full Analysis")
    print("8. Exit")

    choice = input("\nChoice (1-8): ")

    if choice == '8':
        print("Goodbye! 👋")
        break

    # List input
    nums = input("Enter numbers (space separated): ")
    numbers = list(map(int, nums.split()))

    if choice == '1':
        print(f"📈 Sum: {sum(numbers)}")

    elif choice == '2':
        result = sum([n for n in numbers if n % 2 == 0])
        print(f"🔵 Even Sum: {result}")

    elif choice == '3':
        result = sum([n for n in numbers if n % 2 != 0])
        print(f"🟢 Odd Sum: {result}")

    elif choice == '4':
        result = sum([n for n in numbers if n > 0])
        print(f"➕ Positive Sum: {result}")

    elif choice == '5':
        result = sum([n for n in numbers if n < 0])
        print(f"➖ Negative Sum: {result}")

    elif choice == '6':
        start = int(input("Start index: "))
        end = int(input("End index: "))
        result = sum(numbers[start:end])
        print(f"📊 Range Sum: {result}")

    elif choice == '7':
        print(f"\n📊 Full Analysis:")
        print(f"  List: {numbers}")
        print(f"  Total Sum: {sum(numbers)}")
        print(f"  Average: {sum(numbers)/len(numbers):.2f}")
        print(f"  Max: {max(numbers)}")
        print(f"  Min: {min(numbers)}")


# In[ ]:




