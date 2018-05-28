#! python3
"""What is the smallest odd composite that cannot be written
as the sum of a prime and twice a square?"""
from itertools import count
from math import sqrt
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import is_prime

for i in count(3, 2):
    if not sqrt(i / 2) % 1 or is_prime(i):
        continue
    for j in range(1, i):
        if is_prime(i - 2 * j * j):
            break
    else:
        print(i)
        break
