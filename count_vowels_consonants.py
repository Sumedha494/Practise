#!/usr/bin/env python
# coding: utf-8

# In[ ]:


VOWELS = "aeiouAEIOU"
CONSONANTS = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

print("Vowels:", VOWELS)
print("Consonants:", CONSONANTS)


# In[ ]:


# Method 1 
def count_using_loop(string):
    vowels = 0
    consonants = 0

    for char in string:
        if char in VOWELS:
            vowels += 1
        elif char in CONSONANTS:
            consonants += 1

    return vowels, consonants

text = "Hello World"
v, c = count_using_loop(text)
print(f"String: {text}")
print(f"Vowels: {v}")
print(f"Consonants: {c}")


# In[ ]:


# Method 2
def count_using_comprehension(string):
    vowels = len([char for char in string if char in VOWELS])
    consonants = len([char for char in string if char in CONSONANTS])

    return vowels, consonants

text = "Python Programming"
v, c = count_using_comprehension(text)
print(f"String: {text}")
print(f"Vowels: {v}")
print(f"Consonants: {c}")


# In[ ]:


# Method 3
def count_using_sum(string):
    vowels = sum(1 for char in string if char in VOWELS)
    consonants = sum(1 for char in string if char in CONSONANTS)

    return vowels, consonants

text = "Jupyter Notebook"
v, c = count_using_sum(text)
print(f"String: {text}")
print(f"Vowels: {v}")
print(f"Consonants: {c}")


# In[ ]:


# Method 4
def count_using_filter(string):
    vowels = len(list(filter(lambda x: x in VOWELS, string)))
    consonants = len(list(filter(lambda x: x in CONSONANTS, string)))

    return vowels, consonants

text = "Data Science"
v, c = count_using_filter(text)
print(f"String: {text}")
print(f"Vowels: {v}")
print(f"Consonants: {c}")


# In[ ]:


# Method 5
def count_using_dict(string):
    result = {
        'vowels': 0,
        'consonants': 0,
        'digits': 0,
        'spaces': 0,
        'special': 0
    }

    for char in string:
        if char in VOWELS:
            result['vowels'] += 1
        elif char in CONSONANTS:
            result['consonants'] += 1
        elif char.isdigit():
            result['digits'] += 1
        elif char.isspace():
            result['spaces'] += 1
        else:
            result['special'] += 1

    return result

text = "Hello World 123!"
result = count_using_dict(text)
print(f"String: {text}")
for key, value in result.items():
    print(f"{key.capitalize():12}: {value}")


# In[ ]:


# Method 6
import re

def count_using_regex(string):
    vowels = len(re.findall(r'[aeiouAEIOU]', string))
    consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', string))

    return vowels, consonants

# Test
text = "Regular Expression"
v, c = count_using_regex(text)
print(f"String: {text}")
print(f"Vowels: {v}")
print(f"Consonants: {c}")


# In[ ]:


# Method 7
def count_case_insensitive(string):
    string_lower = string.lower()

    vowels = sum(1 for char in string_lower if char in 'aeiou')
    consonants = sum(1 for char in string_lower if char in 'bcdfghjklmnpqrstvwxyz')

    return vowels, consonants

text = "HELLO world"
v, c = count_case_insensitive(text)
print(f"String: {text}")
print(f"Vowels: {v}")
print(f"Consonants: {c}")


# In[ ]:


# Find which vowels and consonants are present
def find_vowels_consonants(string):
    string_lower = string.lower()

    vowels_found = set()
    consonants_found = set()

    for char in string_lower:
        if char in 'aeiou':
            vowels_found.add(char)
        elif char in 'bcdfghjklmnpqrstvwxyz':
            consonants_found.add(char)

    return sorted(vowels_found), sorted(consonants_found)

text = "Hello World Python"
vowels, consonants = find_vowels_consonants(text)
print(f"String: {text}")
print(f"Vowels Found: {vowels}")
print(f"Consonants Found: {consonants}")


# In[ ]:


# Count each vowel separately
def count_each_vowel(string):
    string_lower = string.lower()

    vowel_count = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for char in string_lower:
        if char in vowel_count:
            vowel_count[char] += 1

    return vowel_count

text = "Education is Important"
result = count_each_vowel(text)
print(f"String: {text}")
print("\nVowel Count:")
for vowel, count in result.items():
    print(f"  '{vowel}' : {count}")
print(f"\nTotal Vowels: {sum(result.values())}")


# In[ ]:


# Taking input from user
user_input = input("Enter a string: ")


# In[ ]:


# Complete String Analysis
def complete_analysis(string):
    print("=" * 60)
    print(f"📝 Original String: {string}")
    print("=" * 60)

    # Count vowels and consonants
    v, c = count_using_loop(string)

    # Find which ones are present
    vowels_list, consonants_list = find_vowels_consonants(string)

    # Count each vowel
    vowel_details = count_each_vowel(string)

    # Display results
    print(f"\n📊 STATISTICS:")
    print(f"   Total Characters : {len(string)}")
    print(f"   Vowels           : {v}")
    print(f"   Consonants       : {c}")
    print(f"   Spaces           : {string.count(' ')}")
    print(f"   Digits           : {sum(1 for c in string if c.isdigit())}")

    print(f"\n🔤 VOWELS FOUND: {vowels_list}")
    print(f"🔤 CONSONANTS FOUND: {consonants_list}")

    print(f"\n📈 VOWEL BREAKDOWN:")
    for vowel, count in vowel_details.items():
        bar = "█" * count
        print(f"   {vowel.upper()} : {count:2} | {bar}")

    print("=" * 60)

# Run Analysis
complete_analysis(user_input)


# In[ ]:


# Visual representation using matplotlib
import matplotlib.pyplot as plt

def visualize_vowels(string):
    vowel_count = count_each_vowel(string)

    vowels = list(vowel_count.keys())
    counts = list(vowel_count.values())

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']

    plt.figure(figsize=(10, 5))
    plt.bar(vowels, counts, color=colors, edgecolor='black', linewidth=2)
    plt.xlabel('Vowels', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.title(f'Vowel Count in: "{string}"', fontsize=14)

    for i, count in enumerate(counts):
        plt.text(i, count + 0.1, str(count), ha='center', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.show()

# Test
text = "Artificial Intelligence"
visualize_vowels(text)


# In[ ]:


# Pie Chart for Vowels vs Consonants
def visualize_pie(string):
    v, c = count_using_loop(string)
    spaces = string.count(' ')
    digits = sum(1 for char in string if char.isdigit())
    special = len(string) - v - c - spaces - digits

    labels = ['Vowels', 'Consonants', 'Spaces', 'Digits', 'Special']
    sizes = [v, c, spaces, digits, special]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    explode = (0.1, 0, 0, 0, 0)

    # Remove zero values
    non_zero = [(l, s, c) for l, s, c in zip(labels, sizes, colors) if s > 0]
    if non_zero:
        labels, sizes, colors = zip(*non_zero)

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode[:len(sizes)], labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title(f'Character Distribution in: "{string}"', fontsize=14)
    plt.axis('equal')
    plt.show()

# Test
text = "Hello World 123!"
visualize_pie(text)


# In[ ]:


# Process multiple strings
def process_multiple_strings(strings_list):
    print(f"{'String':<30} {'Vowels':>8} {'Consonants':>12} {'Total':>8}")
    print("-" * 60)

    for string in strings_list:
        v, c = count_using_loop(string)
        print(f"{string:<30} {v:>8} {c:>12} {v+c:>8}")

# Test
strings = [
    "Hello World",
    "Python Programming",
    "Data Science",
    "Machine Learning",
    "Artificial Intelligence"
]

process_multiple_strings(strings)


# In[ ]:


# One-liner using lambda
count_v = lambda s: sum(1 for c in s.lower() if c in 'aeiou')
count_c = lambda s: sum(1 for c in s.lower() if c in 'bcdfghjklmnpqrstvwxyz')

# Test
text = "Lambda Function"
print(f"String: {text}")
print(f"Vowels: {count_v(text)}")
print(f"Consonants: {count_c(text)}")


# In[ ]:


# Object-Oriented Approach
class VowelConsonantCounter:
    VOWELS = 'aeiouAEIOU'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    def __init__(self, string):
        self.string = string
        self.vowel_count = 0
        self.consonant_count = 0
        self._count()

    def _count(self):
        for char in self.string:
            if char in self.VOWELS:
                self.vowel_count += 1
            elif char in self.CONSONANTS:
                self.consonant_count += 1

    def get_vowels(self):
        return self.vowel_count

    def get_consonants(self):
        return self.consonant_count

    def __str__(self):
        return f"String: '{self.string}' | Vowels: {self.vowel_count} | Consonants: {self.consonant_count}"

# Test
counter = VowelConsonantCounter("Object Oriented Programming")
print(counter)
print(f"Vowels: {counter.get_vowels()}")
print(f"Consonants: {counter.get_consonants()}")


# In[ ]:


# Complete Interactive Program
def main():
    print("╔════════════════════════════════════════════════════╗")
    print("║     VOWEL & CONSONANT COUNTER                     ║")
    print("╚════════════════════════════════════════════════════╝")

    while True:
        print("\n📌 OPTIONS:")
        print("1. Count Vowels & Consonants")
        print("2. Detailed Analysis")
        print("3. Count Each Vowel")
        print("4. Process Multiple Strings")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            text = input("Enter a string: ")
            v, c = count_using_loop(text)
            print(f"\n✅ Vowels: {v}")
            print(f"✅ Consonants: {c}")

        elif choice == '2':
            text = input("Enter a string: ")
            complete_analysis(text)

        elif choice == '3':
            text = input("Enter a string: ")
            result = count_each_vowel(text)
            print("\n📊 Vowel Count:")
            for v, c in result.items():
                print(f"   {v.upper()}: {c}")

        elif choice == '4':
            n = int(input("How many strings? "))
            strings = []
            for i in range(n):
                s = input(f"Enter string {i+1}: ")
                strings.append(s)
            process_multiple_strings(strings)

        elif choice == '5':
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice! Try again.")

# Run the program
main()

