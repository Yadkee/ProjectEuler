#! python3
"""
    To import me do:
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import *
"""
from math import sqrt
from itertools import count
from functools import reduce
from operator import mul


def mult(l):
    return reduce(mul, l, 1)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


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


def primes_until(m):
    sieve = [True] * m
    for i in sixn(m):
        if sieve[i]:
            yield i
            for mult in range(i * i, m, i):
                sieve[mult] = False
