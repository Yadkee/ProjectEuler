#! python3
"""What is the largest prime factor of the number 600851475143?"""
from itertools import count


def sixn():
    """All primes are of the form 6n + 1 or 6n - 1"""
    yield 2
    yield 3
    for i in count(1):
        x = 6 * i + 1
        yield x - 2
        yield x


def largest_factor(n):
    factors = []
    limit = int(n / 2 + 1)
    for i in sixn():
        if i > limit:
            break
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
