#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_prime(n):
    """
    Checks if a number is prime.

    Parameters:
    n (int): The number to check

    Returns:
    bool: True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# In[ ]:


def generate_primes_up_to(limit):
    """
    Generates a list of all prime numbers up to (and including) a given limit.

    Parameters:
    limit (int): Upper bound to search for primes

    Returns:
    list: List of prime numbers
    """
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes


# In[ ]:


def sieve_of_eratosthenes(limit):
    """
    Implements the Sieve of Eratosthenes algorithm.
    Returns a list of all primes <= limit.

    Parameters:
    limit (int): Upper bound

    Returns:
    list: List of prime numbers
    """
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:

            for multiple in range(i*i, limit + 1, i):
                is_prime[multiple] = False

    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes


# In[ ]:


print("--- Checking single numbers ---")

numbers_to_check = [1, 2, 3, 4, 5, 17, 20, 29, 100]

for num in numbers_to_check:
    print(f"{num} is prime? {is_prime(num)}")

print("\n--- Generating primes up to a limit ---")

limit = 50
primes_up_to_50 = generate_primes_up_to(limit)
print(f"Primes up to {limit}: {primes_up_to_50}")

print("\n--- Using Sieve of Eratosthenes ---")
primes_sieve = sieve_of_eratosthenes(limit)
print(f"Primes up to {limit} (Sieve): {primes_sieve}")

print("\n--- Larger example (primes up to 200) ---")
limit_large = 200
primes_200 = sieve_of_eratosthenes(limit_large)
print(f"Number of primes up to {limit_large}: {len(primes_200)}")
print(f"First 20 primes up to {limit_large}: {primes_200[:20]}")

