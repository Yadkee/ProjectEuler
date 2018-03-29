#! python3
"""What is the largest prime factor of the number 600851475143?"""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import sixn


def largest_factor(n):
    factors = []
    for i in sixn(int(n / 2 + 1)):
        while n != 1:
            d, m = divmod(n, i)
            if m:
                break
            else:
                n = d
                factors.append(i)
        else:
            break
    return max(factors)

print(largest_factor(600851475143))
