#! python3
"""What is the 10 001st prime number?"""
from itertools import count
from collections import deque


def sixn():
    """All primes are of the form 6n + 1 or 6n - 1"""
    yield 2
    yield 3
    for i in count(1):
        x = 6 * i + 1
        yield x - 2
        yield x


def prime_n(n):
    prevPrimes = deque()
    counter = 0
    for i in sixn():
        isPrime = True
        limit = int(i / 2 + 1)
        for j in prevPrimes:
            if j > limit:
                break
            if not i % j:
                isPrime = False
                break
        if isPrime:
            counter += 1
            prevPrimes.append(i)
            if counter == n:
                return i

print(prime_n(10001))
