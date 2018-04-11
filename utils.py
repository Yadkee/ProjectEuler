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
    yield from (2, 3)
    for i in range(6, m - 1, 6):
        yield i - 1
        yield i + 1


def is_prime(n):
    """all() returns True if all the values are True"""
    return n > 1 and (n < 4 or all(n % i for i in sixn(int(sqrt(n)) + 1)))


def primes_until(m):
    """(https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)"""
    assert m > 3, "m must be greater than 3"
    sieve = [True] * m
    for i in sixn(m):
        if sieve[i]:
            yield i
            for mult in range(i * i, m, i):
                sieve[mult] = False
