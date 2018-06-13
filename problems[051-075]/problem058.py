#! python3
"""What is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?"""
from itertools import count
from time import time
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import is_prime

t0 = time()
primes = 0
v = 1
for i in count(2, 2):  # Takes around 11 seconds
    for _ in range(4):
        v += i
        if is_prime(v):
            primes += 10
    if not primes // (i + i + 1):
        print(i + 1, "in %.2f seconds" % (time() - t0))
        break
