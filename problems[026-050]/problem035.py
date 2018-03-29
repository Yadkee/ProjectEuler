#! python3
"""How many circular primes are there below one million?"""
from itertools import count
from time import time


def sixn(m):
    yield 2
    yield 3
    for i in count(1):
        x = 6 * i + 1
        if x - 2 < m:
            yield x - 2
        else:
            break
        if x < m:
            yield x
        else:
            break


def primes_until(m):
    sieve = [True] * m
    for i in sixn(m):
        if sieve[i]:
            yield i
            for mult in range(i * i, m, i):
                sieve[mult] = False


def is_circular(n):
    if n in primes:
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:] + s[:i]) not in primes:
                break
        else:
            return True

t0 = time()
primes = set(primes_until(10 ** 6))  # Try using list or tuple to see the diff
solution = sum(1 for i in range(2, 10 ** 6) if is_circular(i))
print("%d in %.2f seconds" % (solution, time() - t0))
