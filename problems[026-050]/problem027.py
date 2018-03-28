#! python3
"""Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for
consecutive values of n, starting with n=0.

Considering quadratics of the form:
    n^2+an+b
where |a|<1000 and |b|≤1000"""
from itertools import count
from operator import mul
from time import time


def sixn(m):
    """All primes are of the form 6n + 1 or 6n - 1"""
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


def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif (n + 1) % 6 != 0 and (n - 1) % 6 != 0:
        return False
    for i in sixn(n):
        if not n % i:
            return False
    return True


def consecutive_primes(a, b):
    for n in count():
        v = n ** 2 + a * n + b
        try:
            if not cache[v]:
                break
        except KeyError:
            s = is_prime(v)
            cache[v] = s
            if not s:
                break
    return n

cache = {}  # To speed up a little bit
t0 = time()
s = mul(*max(((a, b) for a in range(-999, 1000) for b in range(-1000, 1001)),
        key=lambda x: consecutive_primes(*x)))
print("%d in %.2f seconds" % (s, time() - t0))
