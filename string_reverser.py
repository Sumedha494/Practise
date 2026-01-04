#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Method 1
def reverse_slicing(string):
    return string[::-1]

text = "Hello World"
print(reverse_slicing(text))


# In[2]:


# Method 2
def reverse_loop(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

text = "Python"
print(reverse_loop(text))


# In[3]:


# Method 3
def reverse_function(string):
    return "".join(reversed(string))

text = "Jupyter"
print(reverse_function(text))


# In[4]:


# Method 4
def reverse_while(string):
    reversed_str = ""
    index = len(string) - 1

    while index >= 0:
        reversed_str += string[index]
        index -= 1

    return reversed_str

text = "Notebook"
print(reverse_while(text))


# In[5]:


# Method 5
def reverse_recursion(string):
    if len(string) == 0:
        return string
    else:
        return reverse_recursion(string[1:]) + string[0]

text = "Recursion"
print(reverse_recursion(text))


# In[6]:


# Method 6
def reverse_list(string):
    char_list = list(string)
    char_list.reverse()
    return "".join(char_list)

text = "Programming"
print(reverse_list(text))


# In[7]:


# Method 7
def reverse_stack(string):
    stack = []

    for char in string:
        stack.append(char)

    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str

text = "Stack"
print(reverse_stack(text))


# In[8]:


# Taking input from user
user_input = input("Enter a string to reverse: ")


# In[9]:


# Display results from all methods
print("=" * 50)
print(f"Original String  : {user_input}")
print("=" * 50)
print(f"Using Slicing    : {reverse_slicing(user_input)}")
print(f"Using Loop       : {reverse_loop(user_input)}")
print(f"Using reversed() : {reverse_function(user_input)}")
print(f"Using While      : {reverse_while(user_input)}")
print(f"Using Recursion  : {reverse_recursion(user_input)}")
print(f"Using List       : {reverse_list(user_input)}")
print(f"Using Stack      : {reverse_stack(user_input)}")
print("=" * 50)


# In[10]:


# Reverse words in a sentence (not characters)
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

sentence = "I love Python programming"
print(f"Original : {sentence}")
print(f"Reversed : {reverse_words(sentence)}")


# In[11]:


# Check if string is palindrome
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

words = ["madam", "radar", "hello", "level", "python"]

for word in words:
    result = "✅ Palindrome" if is_palindrome(word) else "❌ Not Palindrome"
    print(f"{word:10} -> {result}")


# In[12]:


# One-liner using lambda
reverse = lambda s: s[::-1]

print(reverse("Lambda Function"))

