#! python3
"""How many different ways can one hundred be written as a sum of at least two
positive integers?"""
from functools import lru_cache


@lru_cache(maxsize=None)
def ways(n, p):
    if n <= 1:
        return 1
    return sum(ways(n - i, i) for i in range(1, min(n, p) + 1))

print(ways(100, 9999) - 1)
