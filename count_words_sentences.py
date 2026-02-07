#!/usr/bin/env python
# coding: utf-8

# In[ ]:


text = "Python is a great programming language"

words = text.split()
word_count = len(words)

print(f"Text: {text}")
print(f"Words: {words}")
print(f"Total Words: {word_count}")


# In[ ]:


text = "Hello World. How are you? I am fine. Thank you!"

sentence_count = text.count('.') + text.count('?') + text.count('!')

print(f"Text: {text}")
print(f"Total Sentences: {sentence_count}")


# In[ ]:


text = input("Apna text enter karo: ")

words = text.split()
word_count = len(words)

sentences = text.count('.') + text.count('?') + text.count('!')

print(f"\n📊 Results:")
print(f"Words: {word_count}")
print(f"Sentences: {sentences}")


# In[ ]:


def text_analyzer(text):
    """Complete text analysis"""

    char_with_space = len(text)

    char_without_space = len(text.replace(" ", ""))

    words = text.split()
    word_count = len(words)

    sentence_count = text.count('.') + text.count('?') + text.count('!')

    paragraphs = text.split('\n\n')
    para_count = len([p for p in paragraphs if p.strip()])

    lines = text.split('\n')
    line_count = len([l for l in lines if l.strip()])

    print("=" * 40)
    print("📊 TEXT ANALYSIS REPORT")
    print("=" * 40)
    print(f"📝 Characters (with spaces)   : {char_with_space}")
    print(f"📝 Characters (without spaces): {char_without_space}")
    print(f"📖 Words                      : {word_count}")
    print(f"📄 Sentences                  : {sentence_count}")
    print(f"📑 Paragraphs                 : {para_count}")
    print(f"📃 Lines                      : {line_count}")
    print("=" * 40)

# Example
text = """Python is amazing. It is easy to learn.

Data Science uses Python. Machine Learning is fun!

Are you learning Python? Yes, I am!"""

text_analyzer(text)


# In[ ]:


text = "python is great python is easy python is fun"

words = text.lower().split()

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("📊 Word Frequency:")
print("-" * 20)
for word, count in word_freq.items():
    print(f"{word}: {count}")


# In[ ]:


from collections import Counter

text = "apple banana apple orange banana apple mango"

words = text.split()
word_counts = Counter(words)

print("📊 Word Frequency (Counter):")
print("-" * 25)

for word, count in word_counts.items():
    print(f"{word}: {count}")

print("\n🏆 Top 3 Words:")
for word, count in word_counts.most_common(3):
    print(f"{word}: {count}")


# In[ ]:


import re

text = "Hello! How are you? I'm doing great. Python is awesome!"

words = re.findall(r'\b\w+\b', text)
word_count = len(words)

sentences = re.split(r'[.!?]+', text)
sentences = [s for s in sentences if s.strip()]
sentence_count = len(sentences)

print(f"Text: {text}")
print(f"\n📊 Results (Regex Method):")
print(f"Words: {words}")
print(f"Word Count: {word_count}")
print(f"Sentence Count: {sentence_count}")


# In[ ]:


text = "Python is great. I love Python. Python is easy to learn."
search_word = "Python"

count_sensitive = text.split().count(search_word)

count_insensitive = text.lower().split().count(search_word.lower())

import re
words = re.findall(r'\b\w+\b', text.lower())
count_clean = words.count(search_word.lower())

print(f"Text: {text}")
print(f"\n🔍 Searching for: '{search_word}'")
print(f"Count (Case Sensitive): {count_sensitive}")
print(f"Count (Case Insensitive): {count_clean}")


# In[ ]:


def count_vowels_consonants(text):
    """Vowels aur consonants count karna"""
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count

# Example
text = "Hello World Python Programming"
vowels, consonants = count_vowels_consonants(text)

print(f"Text: {text}")
print(f"🔴 Vowels: {vowels}")
print(f"🔵 Consonants: {consonants}")


# In[ ]:


sample_text = """Python is a programming language.
It is easy to learn.
Data Science uses Python.
Machine Learning is fun!"""

with open('sample.txt', 'w') as f:
    f.write(sample_text)

with open('sample.txt', 'r') as f:
    content = f.read()

    words = content.split()
    word_count = len(words)

    sentences = content.count('.') + content.count('!') + content.count('?')

    lines = content.split('\n')
    line_count = len([l for l in lines if l.strip()])

print("📁 File Analysis:")
print(f"Words: {word_count}")
print(f"Sentences: {sentences}")
print(f"Lines: {line_count}")


# In[ ]:


class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = text.split()

    def word_count(self):
        return len(self.words)

    def sentence_count(self):
        return self.text.count('.') + self.text.count('?') + self.text.count('!')

    def char_count(self, include_spaces=True):
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(" ", ""))

    def average_word_length(self):
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return round(total_length / len(self.words), 2)

    def longest_word(self):
        if not self.words:
            return ""
        return max(self.words, key=len)

    def shortest_word(self):
        if not self.words:
            return ""
        return min(self.words, key=len)

    def full_report(self):
        print("=" * 45)
        print("📊 COMPLETE TEXT ANALYSIS REPORT")
        print("=" * 45)
        print(f"📝 Total Characters (with spaces)   : {self.char_count(True)}")
        print(f"📝 Total Characters (without spaces): {self.char_count(False)}")
        print(f"📖 Total Words                      : {self.word_count()}")
        print(f"📄 Total Sentences                  : {self.sentence_count()}")
        print(f"📏 Average Word Length              : {self.average_word_length()}")
        print(f"📐 Longest Word                     : {self.longest_word()}")
        print(f"📍 Shortest Word                    : {self.shortest_word()}")
        print("=" * 45)

# Usage
text = "Python programming is amazing. Learn it today! You will love it."
analyzer = TextAnalyzer(text)
analyzer.full_report()


# In[ ]:


while True:
    print("\n📝 TEXT ANALYZER MENU")
    print("=" * 30)
    print("1. Count Words")
    print("2. Count Sentences")
    print("3. Count Characters")
    print("4. Word Frequency")
    print("5. Full Analysis")
    print("6. Exit")

    choice = input("\nChoice (1-6): ")

    if choice == '6':
        print("Goodbye! 👋")
        break

    text = input("Enter text: ")

    if choice == '1':
        print(f"📖 Words: {len(text.split())}")

    elif choice == '2':
        count = text.count('.') + text.count('?') + text.count('!')
        print(f"📄 Sentences: {count}")

    elif choice == '3':
        print(f"📝 Characters: {len(text)}")

    elif choice == '4':
        from collections import Counter
        words = text.lower().split()
        freq = Counter(words)
        print("📊 Word Frequency:")
        for word, count in freq.most_common():
            print(f"  {word}: {count}")

    elif choice == '5':
        print(f"📖 Words: {len(text.split())}")
        print(f"📄 Sentences: {text.count('.') + text.count('?') + text.count('!')}")
        print(f"📝 Characters: {len(text)}")


# In[ ]:




