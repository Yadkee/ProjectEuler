#! python3
"""What is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?"""
from itertools import count
from math import sqrt
from time import time


def sixn(m):
    """All primes are of the form 6n + 1 or 6n - 1"""
    if 3 >= m:
        return
    yield 2
    if 3 >= m:
        return
    yield 3
    for i in count(1):
        x = 6 * i + 1
        if x - 2 >= m:
            break
        yield x - 2
        if x >= m:
            break
        yield x


def is_prime(n):
    if n < 2:
        return False
    return all(n % i for i in sixn(int(sqrt(n)) + 1))


t0 = time()
primes = 0
v = 1
for i in count(1):  # Takes around 13 seconds
    for j in range(4):
        v += 2 * i
        if is_prime(v):
            primes += 100
    if primes // (4 * i + 1) < 10:
        print(2 * i + 1, "in %.2f seconds" % (time() - t0))
        break
