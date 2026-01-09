#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string


# In[ ]:


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = string.punctuation

print("📝 Available Character Sets:")
print(f"   🔤 Lowercase : {lowercase}")
print(f"   🔠 Uppercase : {uppercase}")
print(f"   🔢 Digits    : {digits}")
print(f"   🔣 Special   : {special}")


# In[ ]:


def generate_simple_password(length=12):
    """Simple password generate karo"""
    all_characters = lowercase + uppercase + digits + special
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

password = generate_simple_password(12)
print(f"🔐 Generated Password: {password}")


# In[ ]:


def generate_custom_password(
    length=12,
    use_lowercase=True,
    use_uppercase=True,
    use_digits=True,
    use_special=True
):
    """Custom options ke saath password generate karo"""

    characters = ""

    if use_lowercase:
        characters += lowercase
    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_special:
        characters += special

    if not characters:
        return "❌ Error: At least one character type select karo!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_custom_password(
    length=16,
    use_lowercase=True,
    use_uppercase=True,
    use_digits=True,
    use_special=True
)
print(f"🔐 Custom Password: {password}")


# In[ ]:


def generate_strong_password(length=16):
    """Strong password with guaranteed character mix"""

    if length < 4:
        return "❌ Password length should be at least 4!"

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    all_characters = lowercase + uppercase + digits + special
    password += [random.choice(all_characters) for _ in range(length - 4)]

    random.shuffle(password)

    return ''.join(password)

password = generate_strong_password(16)
print(f"💪 Strong Password: {password}")


# In[ ]:


def generate_multiple_passwords(count=5, length=12):
    """Multiple passwords generate karo"""

    passwords = []
    for i in range(count):
        pwd = generate_strong_password(length)
        passwords.append(pwd)

    return passwords

print("🔐 Generated Passwords:")
print("-" * 40)
passwords = generate_multiple_passwords(count=5, length=14)
for i, pwd in enumerate(passwords, 1):
    print(f"   {i}. {pwd}")
print("-" * 40)


# In[ ]:


def check_password_strength(password):
    """Password ki strength check karo"""

    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ Length should be at least 8 characters")

    if len(password) >= 12:
        strength += 1

    if len(password) >= 16:
        strength += 1

    if any(c in lowercase for c in password):
        strength += 1
    else:
        feedback.append("❌ Add lowercase letters")

    if any(c in uppercase for c in password):
        strength += 1
    else:
        feedback.append("❌ Add uppercase letters")

    if any(c in digits for c in password):
        strength += 1
    else:
        feedback.append("❌ Add numbers")

    if any(c in special for c in password):
        strength += 1
    else:
        feedback.append("❌ Add special characters")

    if strength <= 2:
        level = "🔴 Weak"
    elif strength <= 4:
        level = "🟡 Medium"
    elif strength <= 5:
        level = "🟢 Strong"
    else:
        level = "💪 Very Strong"

    return {
        "score": strength,
        "max_score": 7,
        "level": level,
        "feedback": feedback
    }

test_password = "MyP@ssw0rd123!"
result = check_password_strength(test_password)

print(f"🔐 Password: {test_password}")
print(f"📊 Score: {result['score']}/{result['max_score']}")
print(f"💪 Strength: {result['level']}")
if result['feedback']:
    print("📝 Suggestions:")
    for tip in result['feedback']:
        print(f"   {tip}")


# In[ ]:


print("="*50)
print("       🔐 PASSWORD GENERATOR")
print("="*50)

length = int(input("\n📏 Enter password length (8-50): "))
count = int(input("🔢 How many passwords? (1-10): "))

use_lower = input("🔤 Include lowercase? (y/n): ").lower() == 'y'
use_upper = input("🔠 Include uppercase? (y/n): ").lower() == 'y'
use_digit = input("🔢 Include digits? (y/n): ").lower() == 'y'
use_special = input("🔣 Include special chars? (y/n): ").lower() == 'y'

length = max(4, min(50, length))
count = max(1, min(10, count))

print("\n" + "="*50)
print("       📋 GENERATED PASSWORDS")
print("="*50)

for i in range(count):
    pwd = generate_custom_password(
        length=length,
        use_lowercase=use_lower,
        use_uppercase=use_upper,
        use_digits=use_digit,
        use_special=use_special
    )
    strength = check_password_strength(pwd)
    print(f"\n  {i+1}. {pwd}")
    print(f"     Strength: {strength['level']}")

print("\n" + "="*50)


# In[ ]:


def generate_memorable_password():
    """Yaad rakhne mein aasan password"""

    words = [
        "apple", "banana", "cherry", "dragon", "eagle",
        "forest", "galaxy", "harmony", "island", "jungle",
        "knight", "lemon", "mountain", "night", "ocean",
        "phoenix", "queen", "river", "storm", "tiger",
        "umbrella", "violet", "winter", "yellow", "zebra"
    ]

    selected_words = random.sample(words, 3)

    password_parts = []
    for word in selected_words:
        # Random capitalization
        if random.choice([True, False]):
            word = word.capitalize()
        password_parts.append(word)

    password_parts.append(str(random.randint(10, 99)))

    special_chars = "!@#$%&*"
    password_parts.append(random.choice(special_chars))

    separators = ["-", "_", ".", ""]
    separator = random.choice(separators)

    password = separator.join(password_parts)
    return password

print("🧠 Memorable Passwords:")
print("-" * 40)
for i in range(5):
    pwd = generate_memorable_password()
    print(f"   {i+1}. {pwd}")
print("-" * 40)


# In[ ]:


def generate_pin(length=4):
    """Numeric PIN generate karo"""
    return ''.join(random.choice(digits) for _ in range(length))

print("🔢 PIN Codes:")
print("-" * 30)
print(f"   4-digit PIN : {generate_pin(4)}")
print(f"   6-digit PIN : {generate_pin(6)}")
print(f"   8-digit PIN : {generate_pin(8)}")
print("-" * 30)


# In[ ]:


try:
    import pyperclip

    password = generate_strong_password(16)
    pyperclip.copy(password)

    print(f"🔐 Password: {password}")
    print("✅ Password copied to clipboard!")

except ImportError:
    print("⚠️ pyperclip not installed!")
    print("   Install: pip install pyperclip")
    password = generate_strong_password(16)
    print(f"🔐 Password: {password}")

