#! python3
"""Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?"""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import factors

N = 4
i = 1
while True:
    i += 1
    for j in range(i, i + N):
        if len(set(factors(j))) != N:
            break
        i += 1
    else:
        print(i, j)
        break
