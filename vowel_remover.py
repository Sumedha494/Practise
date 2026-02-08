#!/usr/bin/env python
# coding: utf-8

# In[ ]:


text = "Hello World Python"
vowels = "aeiouAEIOU"

result = ""
for char in text:
    if char not in vowels:
        result += char

print(f"Original: {text}")
print(f"Without Vowels: {result}")


# In[ ]:


text = "Hello World Python"
vowels = "aeiouAEIOU"

result = "".join([char for char in text if char not in vowels])

print(f"Original: {text}")
print(f"Without Vowels: {result}")


# In[ ]:


text = "Hello World Python"

result = text
vowels = "aeiouAEIOU"

for vowel in vowels:
    result = result.replace(vowel, "")

print(f"Original: {text}")
print(f"Without Vowels: {result}")


# In[ ]:


text = "Hello World Python"
vowels = "aeiouAEIOU"

translator = str.maketrans("", "", vowels)
result = text.translate(translator)

print(f"Original: {text}")
print(f"Without Vowels: {result}")


# In[ ]:


import re

text = "Hello World Python"

# Method 1: Replace vowels with empty string
result = re.sub(r'[aeiouAEIOU]', '', text)

print(f"Original: {text}")
print(f"Without Vowels: {result}")

# Method 2: Case insensitive
result2 = re.sub(r'[aeiou]', '', text, flags=re.IGNORECASE)
print(f"Without Vowels (re.IGNORECASE): {result2}")


# In[ ]:


text = "Hello World Python"
vowels = "aeiouAEIOU"

result = "".join(filter(lambda char: char not in vowels, text))

print(f"Original: {text}")
print(f"Without Vowels: {result}")


# In[ ]:


def remove_vowels(text):
    """String se vowels remove karta hai"""
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char not in vowels:
            result += char

    return result

# Examples
texts = [
    "Hello World",
    "Python Programming",
    "I Love India",
    "AEIOU are vowels",
    "Jupyter Notebook"
]

print("📝 Vowel Remover Examples:")
print("=" * 50)

for text in texts:
    result = remove_vowels(text)
    print(f"{text:25} → {result}")


# In[ ]:


text = input("Enter your text: ")

vowels = "aeiouAEIOU"
result = "".join([char for char in text if char not in vowels])

print(f"\n📝 Original: {text}")
print(f"🚫 Without Vowels: {result}")
print(f"📊 Vowels Removed: {len(text) - len(result)}")


# In[ ]:


def remove_vowels_with_count(text):
    """Vowels remove karo aur count bhi batao"""
    vowels = "aeiouAEIOU"

    removed_vowels = []
    result = ""

    for char in text:
        if char in vowels:
            removed_vowels.append(char)
        else:
            result += char

    return result, removed_vowels

# Example
text = "Hello World Python"
result, removed = remove_vowels_with_count(text)

print(f"📝 Original: {text}")
print(f"🚫 Without Vowels: {result}")
print(f"📊 Removed Vowels: {removed}")
print(f"📈 Total Removed: {len(removed)}")


# In[ ]:


text = "Hello World PYTHON"

# Only lowercase vowels remove
lowercase_vowels = "aeiou"
result_lower = "".join([c for c in text if c not in lowercase_vowels])

# Only uppercase vowels remove
uppercase_vowels = "AEIOU"
result_upper = "".join([c for c in text if c not in uppercase_vowels])

# Both remove
all_vowels = "aeiouAEIOU"
result_all = "".join([c for c in text if c not in all_vowels])

print(f"📝 Original: {text}")
print(f"🔤 Remove lowercase vowels: {result_lower}")
print(f"🔠 Remove uppercase vowels: {result_upper}")
print(f"🚫 Remove all vowels: {result_all}")


# In[ ]:


sample_text = """Hello World
Python is amazing
I love programming"""

# Write to file
with open('sample.txt', 'w') as f:
    f.write(sample_text)

# Read and remove vowels
with open('sample.txt', 'r') as f:
    content = f.read()

vowels = "aeiouAEIOU"
result = "".join([c for c in content if c not in vowels])

print("📁 Original File Content:")
print(content)
print("\n🚫 After Removing Vowels:")
print(result)

# Save to new file
with open('no_vowels.txt', 'w') as f:
    f.write(result)
print("\n✅ Saved to 'no_vowels.txt'")


# In[ ]:


class VowelRemover:
    def __init__(self, text):
        self.original = text
        self.vowels = "aeiouAEIOU"

    def remove_all(self):
        """Sabhi vowels remove karo"""
        return "".join([c for c in self.original if c not in self.vowels])

    def remove_lowercase(self):
        """Sirf lowercase vowels remove karo"""
        return "".join([c for c in self.original if c not in "aeiou"])

    def remove_uppercase(self):
        """Sirf uppercase vowels remove karo"""
        return "".join([c for c in self.original if c not in "AEIOU"])

    def get_vowels(self):
        """Sirf vowels return karo"""
        return "".join([c for c in self.original if c in self.vowels])

    def vowel_count(self):
        """Vowels ki count"""
        return len([c for c in self.original if c in self.vowels])

    def full_report(self):
        """Complete analysis"""
        print("=" * 45)
        print("📊 VOWEL REMOVER REPORT")
        print("=" * 45)
        print(f"📝 Original Text    : {self.original}")
        print(f"🚫 Without Vowels   : {self.remove_all()}")
        print(f"🔤 Lowercase Removed: {self.remove_lowercase()}")
        print(f"🔠 Uppercase Removed: {self.remove_uppercase()}")
        print(f"📊 Vowels Found     : {self.get_vowels()}")
        print(f"📈 Vowel Count      : {self.vowel_count()}")
        print("=" * 45)

# Usage
text = "Hello World PYTHON Programming"
remover = VowelRemover(text)
remover.full_report()


# In[ ]:


def replace_vowels(text, symbol="*"):
    """Vowels ko symbol se replace karo"""
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char in vowels:
            result += symbol
        else:
            result += char

    return result

# Examples
text = "Hello World Python"

print(f"📝 Original: {text}")
print(f"⭐ Replace with *: {replace_vowels(text, '*')}")
print(f"🔴 Replace with _: {replace_vowels(text, '_')}")
print(f"🟢 Replace with #: {replace_vowels(text, '#')}")
print(f"🔵 Replace with @: {replace_vowels(text, '@')}")


# In[ ]:


while True:
    print("\n🔤 VOWEL REMOVER MENU")
    print("=" * 35)
    print("1. Remove All Vowels")
    print("2. Remove Lowercase Vowels")
    print("3. Remove Uppercase Vowels")
    print("4. Replace Vowels with Symbol")
    print("5. Extract Only Vowels")
    print("6. Count Vowels")
    print("7. Full Analysis")
    print("8. Exit")

    choice = input("\nChoice (1-8): ")

    if choice == '8':
        print("Goodbye! 👋")
        break

    text = input("Enter text: ")
    vowels = "aeiouAEIOU"

    if choice == '1':
        result = "".join([c for c in text if c not in vowels])
        print(f"🚫 Without Vowels: {result}")

    elif choice == '2':
        result = "".join([c for c in text if c not in "aeiou"])
        print(f"🔤 Result: {result}")

    elif choice == '3':
        result = "".join([c for c in text if c not in "AEIOU"])
        print(f"🔠 Result: {result}")

    elif choice == '4':
        symbol = input("Enter symbol: ")
        result = "".join([symbol if c in vowels else c for c in text])
        print(f"✨ Result: {result}")

    elif choice == '5':
        result = "".join([c for c in text if c in vowels])
        print(f"📊 Vowels: {result}")

    elif choice == '6':
        count = len([c for c in text if c in vowels])
        print(f"📈 Vowel Count: {count}")

    elif choice == '7':
        print(f"\n📊 Full Analysis:")
        print(f"  Original: {text}")
        print(f"  Without Vowels: {''.join([c for c in text if c not in vowels])}")
        print(f"  Only Vowels: {''.join([c for c in text if c in vowels])}")
        print(f"  Vowel Count: {len([c for c in text if c in vowels])}")


# In[ ]:


import time

text = "Hello World Python Programming " * 10000

# Method 1: For loop
start = time.time()
result1 = ""
for c in text:
    if c not in "aeiouAEIOU":
        result1 += c
time1 = time.time() - start

# Method 2: List comprehension
start = time.time()
result2 = "".join([c for c in text if c not in "aeiouAEIOU"])
time2 = time.time() - start

# Method 3: translate()
start = time.time()
translator = str.maketrans("", "", "aeiouAEIOU")
result3 = text.translate(translator)
time3 = time.time() - start

# Method 4: Regex
import re
start = time.time()
result4 = re.sub(r'[aeiouAEIOU]', '', text)
time4 = time.time() - start

print("⚡ Performance Comparison:")
print("=" * 35)
print(f"For Loop        : {time1:.6f} sec")
print(f"List Comprehension: {time2:.6f} sec")
print(f"translate()     : {time3:.6f} sec")
print(f"Regex           : {time4:.6f} sec")
print("\n🏆 Winner: translate() (Fastest!)")

