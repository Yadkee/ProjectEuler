#! python3
"""Evaluate the sum of all the amicable numbers under 10000.

Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers."""
from time import time


def d(n):
    factors = [1]
    limit = int(n / 2 + 1)
    for i in range(2, limit):
        if n % i == 0:
            factors.append(i)
    return sum(factors)


def amicable_pair(n):
    dn = d(n)
    return d(dn) == n and dn != n, dn

t0 = time()
amicables = []
skip = set()
for i in range(1, 10 ** 4):
    if i in skip:
        continue
    a = amicable_pair(i)
    if a[0]:
        amicables.append(i)
        amicables.append(a[1])
    skip.add(a[1])
print(sum(amicables), "in %.2f seconds" % (time() - t0))
