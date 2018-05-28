#! python3
"""We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?"""
from itertools import permutations
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import is_prime

for width in range(10, 1, -1):
    print(width - 1)
    rng = "".join(map(str, range(1, width)))
    gtr = (int("".join(i)) for i in permutations(rng))
    try:
        print(max(filter(is_prime, gtr)))
    except ValueError:
        pass
    else:
        break
