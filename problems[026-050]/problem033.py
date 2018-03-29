#! python3
"""If the product of these four fractions is given in its lowest common terms,
find the value of the denominator."""
from functools import reduce
from operator import mul


def is_curious(a, b):  # is_curious
    if a // 10 == b % 10:
        return a / b == (a % 10) / (b // 10)
    if a % 10 == b // 10:
        return b / a == (b % 10) / (a // 10)


def lct(it):  # lowest_common_terms
    a, b = [reduce(mul, i, 1) for i in zip(*it)]  # reduce(mul, i, 1) = product
    for i in range(2, min(a, b)):
        while not (a % i or b % i):
            a //= i
            b //= i
    return (a, b)

print(lct((a, b) for a in range(10, 100) for b in range(a + 1, 100)
      if is_curious(a, b))[1])
