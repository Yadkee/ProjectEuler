#! python3
"""Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are relatively
prime to n. Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum."""
from time import time
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import mult, factors_until


def n_totient(n):
    f = factors[n]
    if f:
        return 1 / (mult(1 - 1 / i for i in f))
    return n / (n - 1)

t0 = time()
N = 10 ** 6 + 1
factors = factors_until(N)
print(max(range(2, N), key=n_totient))
print("In %d seconds" % (time() - t0))
