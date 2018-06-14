#! python3
"""A number chain is created by continuously adding the square of the digits in
a number to form a new number until it has been seen before.
How many starting numbers below ten million will arrive at 89?"""
from functools import lru_cache
from time import time


@lru_cache(maxsize=None)
def arrives(n):
    if n == 1:
        return False
    if n == 89:
        return True
    return arrives(sum(square[i] for i in str(n)))

t0 = time()
square = dict((str(i), i * i) for i in range(10))
print(sum(map(arrives, range(1, 10 ** 7))))  # Takes ~30 seconds
print("In %d seconds" % (time() - t0))
