#! python3
"""How many circular primes are there below one million?"""
from time import time
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import primes_until


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
