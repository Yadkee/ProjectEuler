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
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import is_prime


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

cache = {}  # To speed up a little bit (around 5 seconds)
t0 = time()
s = mul(*max(((a, b) for a in range(-999, 1000) for b in range(-1000, 1001)),
        key=lambda x: consecutive_primes(*x)))
print("%d in %.2f seconds" % (s, time() - t0))
