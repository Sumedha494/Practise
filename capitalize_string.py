#!/usr/bin/env python
# coding: utf-8

# In[ ]:


text = "hello world python programming"

result = text.title()

print(f"Original: {text}")
print(f"Capitalized: {result}")


# In[ ]:


word = "python"

result = word.capitalize()

print(f"Original: {word}")
print(f"Capitalized: {result}")


# In[ ]:


import string

text = "hello world python programming"

result = string.capwords(text)

print(f"Original: {text}")
print(f"Capitalized: {result}")


# In[ ]:


text = "hello world python programming"

words = text.split()  # Split into words
capitalized_words = []

for word in words:
    capitalized_words.append(word.capitalize())

result = " ".join(capitalized_words)

print(f"Original: {text}")
print(f"Capitalized: {result}")


# In[ ]:


text = "hello world python programming"

result = " ".join([word.capitalize() for word in text.split()])

print(f"Original: {text}")
print(f"Capitalized: {result}")


# In[ ]:


# map() function use karke
text = "hello world python programming"

result = " ".join(map(str.capitalize, text.split()))

print(f"Original: {text}")
print(f"Capitalized: {result}")


# In[ ]:


text = "hello world python"

result = ""
capitalize_next = True

for char in text:
    if char == " ":
        result += char
        capitalize_next = True
    elif capitalize_next:
        result += char.upper()
        capitalize_next = False
    else:
        result += char.lower()

print(f"Original: {text}")
print(f"Capitalized: {result}")


# In[ ]:


text = input("Enter your text: ")

# Method 1: title()
result1 = text.title()

# Method 2: List comprehension
result2 = " ".join([w.capitalize() for w in text.split()])

print(f"\n📝 Original: {text}")
print(f"✨ Using title(): {result1}")
print(f"✨ Using capitalize(): {result2}")


# In[ ]:


def capitalize_words(text):
    """Har word ka first letter capital karta hai"""
    words = text.split()
    capitalized = [word.capitalize() for word in words]
    return " ".join(capitalized)

# Examples
texts = [
    "hello world",
    "python is awesome",
    "i love programming",
    "UPPERCASE TEXT",
    "mIxEd CaSe TeXt"
]

print("📝 Capitalize Words Examples:")
print("=" * 40)

for text in texts:
    result = capitalize_words(text)
    print(f"{text:20} → {result}")


# In[ ]:


import string

def smart_capitalize(text):
    """Special characters ke saath capitalize"""
    result = string.capwords(text)
    return result

# Examples with special characters
texts = [
    "hello-world",
    "python_programming",
    "hello.world",
    "it's a beautiful day"
]

print("📝 Special Characters Handling:")
print("=" * 45)

for text in texts:
    title_result = text.title()
    capwords_result = string.capwords(text)
    print(f"Original: {text}")
    print(f"  title(): {title_result}")
    print(f"  capwords(): {capwords_result}")
    print()


# In[ ]:


import re

def capitalize_all_separators(text):
    """Multiple separators ke saath capitalize"""
    # Split by multiple separators
    words = re.split(r'([\s\-_\.]+)', text)

    result = ""
    for part in words:
        if part and part[0].isalpha():
            result += part.capitalize()
        else:
            result += part

    return result

# Examples
texts = [
    "hello-world-python",
    "first_name_last_name",
    "hello.world.test",
    "mixed-case_text.example"
]

print("📝 Multiple Separators:")
print("=" * 50)

for text in texts:
    result = capitalize_all_separators(text)
    print(f"{text:30} → {result}")


# In[ ]:


text = "hello WORLD pyTHon"

print("📊 Methods Comparison:")
print("=" * 40)
print(f"Original       : {text}")
print(f"title()        : {text.title()}")
print(f"capitalize()   : {text.capitalize()}")
print(f"upper()        : {text.upper()}")
print(f"lower()        : {text.lower()}")
print(f"swapcase()     : {text.swapcase()}")


# In[ ]:


def capitalize_first_only(text):
    """Sirf first letter capital, baaki same"""
    words = text.split()
    result = []

    for word in words:
        if word:
            new_word = word[0].upper() + word[1:]
            result.append(new_word)

    return " ".join(result)

# Example
text = "hELLO wORLD pYTHON"

print(f"Original: {text}")
print(f"capitalize_first_only(): {capitalize_first_only(text)}")
print(f"title(): {text.title()}")


# In[ ]:


def sentence_case(text):
    """Sirf sentence ka first word capitalize"""
    sentences = text.split('. ')
    result = []

    for sentence in sentences:
        if sentence:
            result.append(sentence.capitalize())

    return '. '.join(result)

# Example
text = "hello world. how are you. i am fine."

print(f"Original: {text}")
print(f"Sentence Case: {sentence_case(text)}")


# In[ ]:


while True:
    print("\n🔤 STRING CAPITALIZATION MENU")
    print("=" * 35)
    print("1. Title Case (Each Word)")
    print("2. Sentence Case (First Word)")
    print("3. UPPERCASE")
    print("4. lowercase")
    print("5. Capitalize First Only")
    print("6. Compare All Methods")
    print("7. Exit")

    choice = input("\nChoice (1-7): ")

    if choice == '7':
        print("Goodbye! 👋")
        break

    text = input("Enter text: ")

    if choice == '1':
        print(f"✨ Result: {text.title()}")

    elif choice == '2':
        print(f"✨ Result: {text.capitalize()}")

    elif choice == '3':
        print(f"✨ Result: {text.upper()}")

    elif choice == '4':
        print(f"✨ Result: {text.lower()}")

    elif choice == '5':
        result = " ".join([w[0].upper() + w[1:] if w else "" for w in text.split()])
        print(f"✨ Result: {result}")

    elif choice == '6':
        print(f"\n📊 All Methods:")
        print(f"  Original    : {text}")
        print(f"  title()     : {text.title()}")
        print(f"  capitalize(): {text.capitalize()}")
        print(f"  upper()     : {text.upper()}")
        print(f"  lower()     : {text.lower()}")

