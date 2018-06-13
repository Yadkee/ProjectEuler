#! python3
"""
    To import me do:
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import *
"""
from math import sqrt
from functools import reduce
from operator import mul
from collections import deque
from itertools import cycle
from time import time


def mult(l):
    """Same as sum() but using multiplication.
    mult([5, 4, 3, 2, 1]) = 120"""
    return reduce(mul, l, 1)


def fact(n):
    """Factorial. fact(5) = 5! = 5 * 4! = 5 * 4 * 3 * 2 * 1 = 120"""
    if n == 1:
        return 1
    return n * fact(n - 1)


def sixn(m):
    """All primes are of the form 6n + 1 or 6n - 1"""
    yield from range(2, min(m, 4))
    i = 0
    for i in range(6, m - 1, 6):
        yield from (i - 1, i + 1)
    if i + 5 < m:
        yield i + 5


def is_prime(n):
    """all() returns True if all the values are True"""
    return n > 1 and all(n % i for i in sixn(int(sqrt(n)) + 1))


def primes_until(m):
    """(https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)"""
    sieve = [True] * m
    for i in sixn(int(sqrt(m)) + 1):
        if sieve[i]:
            for mult in range(i * i, m, i):
                sieve[mult] = False
    yield from (i for i in sixn(m) if sieve[i])


def prime_generator():
    prevPrimes = deque([2, 3])
    yield from prevPrimes
    x = 5
    for i in cycle((2, 4)):
        isPrime = True
        limit = int(sqrt(x)) + 1
        for j in prevPrimes:
            if j > limit:
                break
            if not x % j:
                isPrime = False
                break
        if isPrime:
            prevPrimes.append(x)
            yield x
        x += i


def factors(n):
    fac = []
    for i in sixn(int(sqrt(n)) + 1):
        while not n % i:
            fac.append(i)
            n //= i
    if n != 1:
        fac.append(n)
    return fac
