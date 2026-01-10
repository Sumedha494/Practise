#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = int(input("Enter a number: "))

if number > 0:
    print("✅ Positive Number")
elif number < 0:
    print("❌ Negative Number")
else:
    print("⭕ Zero")


# In[2]:


def check_number(num):
    """Number positive, negative ya zero check karo"""

    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(10))   # Positive
print(check_number(-5))   # Negative
print(check_number(0))    # Zero


# In[3]:


def check_number_emoji(num):
    """Number check with emoji"""

    if num > 0:
        return f"✅ {num} is Positive"
    elif num < 0:
        return f"❌ {num} is Negative"
    else:
        return f"⭕ {num} is Zero"

print(check_number_emoji(25))
print(check_number_emoji(-10))
print(check_number_emoji(0))


# In[4]:


try:
    number = float(input("Enter a number: "))

    if number > 0:
        print(f"✅ {number} is a POSITIVE number")
    elif number < 0:
        print(f"❌ {number} is a NEGATIVE number")
    else:
        print(f"⭕ {number} is ZERO")

except ValueError:
    print("❌ Error: Please enter a valid number!")


# In[5]:


numbers = [10, -5, 0, 25, -100, 0, 7, -3]

print("📊 Number Analysis:")
print("-" * 30)

for num in numbers:
    if num > 0:
        status = "✅ Positive"
    elif num < 0:
        status = "❌ Negative"
    else:
        status = "⭕ Zero"

    print(f"   {num:>5} → {status}")

print("-" * 30)


# In[6]:


numbers = [10, -5, 0, 25, -100, 0, 7, -3, 15, -8, 0]

positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print("📊 Count Summary:")
print("-" * 30)
print(f"   ✅ Positive Numbers: {positive_count}")
print(f"   ❌ Negative Numbers: {negative_count}")
print(f"   ⭕ Zero Count      : {zero_count}")
print(f"   📋 Total Numbers   : {len(numbers)}")
print("-" * 30)


# In[7]:


numbers = [10, -5, 0, 25, -100, 0, 7, -3, 15, -8, 0, 50, -20]

positive_list = []
negative_list = []
zero_list = []

for num in numbers:
    if num > 0:
        positive_list.append(num)
    elif num < 0:
        negative_list.append(num)
    else:
        zero_list.append(num)

print("📋 Separated Lists:")
print("-" * 40)
print(f"   ✅ Positive: {positive_list}")
print(f"   ❌ Negative: {negative_list}")
print(f"   ⭕ Zero    : {zero_list}")
print("-" * 40)


# In[8]:


numbers = [10, -5, 0, 25, -100, 0, 7, -3, 15, -8]

positive = [x for x in numbers if x > 0]
negative = [x for x in numbers if x < 0]
zeros = [x for x in numbers if x == 0]

print("📋 Using List Comprehension:")
print(f"   ✅ Positive: {positive}")
print(f"   ❌ Negative: {negative}")
print(f"   ⭕ Zeros   : {zeros}")


# In[9]:


numbers = [10, -5, 0, 25, -100, 0, 7, -3, 15, -8]

positive_sum = sum(x for x in numbers if x > 0)
negative_sum = sum(x for x in numbers if x < 0)
total_sum = sum(numbers)

print("📊 Sum Analysis:")
print("-" * 35)
print(f"   ✅ Sum of Positive: {positive_sum}")
print(f"   ❌ Sum of Negative: {negative_sum}")
print(f"   📋 Total Sum      : {total_sum}")
print("-" * 35)


# In[10]:


print("="*40)
print("   POSITIVE NEGATIVE ZERO CHECKER")
print("="*40)

n = int(input("\nHow many numbers? "))

positive_count = 0
negative_count = 0
zero_count = 0

print("\nEnter the numbers:")
for i in range(n):
    num = float(input(f"   Number {i+1}: "))

    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print("\n" + "="*40)
print("   📊 RESULTS")
print("="*40)
print(f"   ✅ Positive: {positive_count}")
print(f"   ❌ Negative: {negative_count}")
print(f"   ⭕ Zero    : {zero_count}")
print("="*40)


# In[11]:


numbers = [10, -5, 0, 25, -100, 0, 7, -3, 15, -8, 0]

positive = len([x for x in numbers if x > 0])
negative = len([x for x in numbers if x < 0])
zeros = len([x for x in numbers if x == 0])

print("📊 Visual Representation:")
print("-" * 40)
print(f"   Positive : {'█' * positive} ({positive})")
print(f"   Negative : {'█' * negative} ({negative})")
print(f"   Zero     : {'█' * zeros} ({zeros})")
print("-" * 40)


# In[12]:


import matplotlib.pyplot as plt

numbers = [10, -5, 0, 25, -100, 0, 7, -3, 15, -8, 0, 50]

positive = len([x for x in numbers if x > 0])
negative = len([x for x in numbers if x < 0])
zeros = len([x for x in numbers if x == 0])

labels = ['Positive', 'Negative', 'Zero']
sizes = [positive, negative, zeros]
colors = ['#4CAF50', '#f44336', '#2196F3']
explode = (0.05, 0.05, 0.05)

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Positive vs Negative vs Zero Distribution')
plt.axis('equal')
plt.show()


# In[13]:


import matplotlib.pyplot as plt

numbers = [10, -5, 0, 25, -100, 0, 7, -3, 15, -8, 0, 50]

positive = len([x for x in numbers if x > 0])
negative = len([x for x in numbers if x < 0])
zeros = len([x for x in numbers if x == 0])

categories = ['Positive', 'Negative', 'Zero']
counts = [positive, negative, zeros]
colors = ['green', 'red', 'blue']

plt.figure(figsize=(8, 5))
bars = plt.bar(categories, counts, color=colors)

for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             str(count), ha='center', fontsize=12, fontweight='bold')

plt.title('Count of Positive, Negative and Zero Numbers')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()


# In[14]:


class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.analyze()

    def analyze(self):
        self.positive = [x for x in self.numbers if x > 0]
        self.negative = [x for x in self.numbers if x < 0]
        self.zeros = [x for x in self.numbers if x == 0]

    def get_counts(self):
        return {
            'positive': len(self.positive),
            'negative': len(self.negative),
            'zero': len(self.zeros)
        }

    def get_sums(self):
        return {
            'positive_sum': sum(self.positive),
            'negative_sum': sum(self.negative),
            'total_sum': sum(self.numbers)
        }

    def display_report(self):
        counts = self.get_counts()
        sums = self.get_sums()

        print("="*45)
        print("        📊 NUMBER ANALYSIS REPORT")
        print("="*45)
        print(f"\n📋 Input Numbers: {self.numbers}")
        print(f"\n✅ Positive Numbers: {self.positive}")
        print(f"❌ Negative Numbers: {self.negative}")
        print(f"⭕ Zeros: {self.zeros}")
        print(f"\n📊 Counts:")
        print(f"   Positive: {counts['positive']}")
        print(f"   Negative: {counts['negative']}")
        print(f"   Zero: {counts['zero']}")
        print(f"\n📈 Sums:")
        print(f"   Positive Sum: {sums['positive_sum']}")
        print(f"   Negative Sum: {sums['negative_sum']}")
        print(f"   Total Sum: {sums['total_sum']}")
        print("="*45)

nums = [10, -5, 0, 25, -100, 0, 7, -3, 15, -8]
analyzer = NumberAnalyzer(nums)
analyzer.display_report()


# In[15]:


numbers = [10, -5, 0, 25, -100, 0, 7, -3]

is_positive = lambda x: x > 0
is_negative = lambda x: x < 0
is_zero = lambda x: x == 0

positive = list(filter(is_positive, numbers))
negative = list(filter(is_negative, numbers))
zeros = list(filter(is_zero, numbers))

print(f"✅ Positive: {positive}")
print(f"❌ Negative: {negative}")
print(f"⭕ Zero: {zeros}")


# In[16]:


def check_ternary(num):
    return "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")

numbers = [10, -5, 0, 25, -100]

for num in numbers:
    result = check_ternary(num)
    print(f"{num:>5} → {result}")

