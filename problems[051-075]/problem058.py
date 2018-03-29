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
for i in count(1):  # Takes around 13 seconds
    for j in range(4):
        v += 2 * i
        if is_prime(v):
            primes += 100
    if primes // (4 * i + 1) < 10:
        print(2 * i + 1, "in %.2f seconds" % (time() - t0))
        break
