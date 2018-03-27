#! python3
"""A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.
Find the sum of all the positive integers which cannot
be written as the sum of two abundant numbers."""
mn, mx = 12, 28123


def sdivisors_until(m):
    """Sum of divisors generator"""
    yield 0
    yield 1
    sieve = [1] * m
    for i in range(2, m):
        yield sieve[i]
        for mul in range(i, m, i):
            sieve[mul] += i

divisors = tuple(sdivisors_until(mx))
abundant = tuple(i for i in range(mn, mx) if divisors[i] > i)
abundantSet = set(abundant)  # Sets are faster checking existance


def can_be_written(n):
    for i in abundant:
        if i > n:
            break
        if n - i in abundantSet:
            return True
    return False

print(sum(i for i in range(1, mx) if not can_be_written(i)))
