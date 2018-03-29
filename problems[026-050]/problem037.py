#! python3
"""Find the sum of the only eleven primes that are both truncatable from
left to right and right to left."""
from itertools import count


def sixn(m):
    """All primes are of the form 6n + 1 or 6n - 1"""
    for i in count(1):
        x = 6 * i + 1
        if x - 2 < m:
            yield x - 2
        else:
            break
        if x < m:
            yield x
        else:
            break


def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif (n + 1) % 6 and (n - 1) % 6:
        return False
    try:
        return cache[n]
    except KeyError:
        for i in sixn(n):
            if not n % i:
                cache[n] = False
                return False
        cache[n] = True
        return True


def is_left_truncable(s):
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            break
    else:
        return True


def generate_right_truncable():
    endings = "13579"
    lst = ["2", "3", "5", "7"]
    while True:
        level = []
        for value in lst:
            for end in endings:
                s = value + end
                if is_prime(int(s)):
                    yield(s)
                    level.append(s)
        if not level:
            break
        lst = level[:]

cache = {}
solutions = []
for i in generate_right_truncable():  # There are 83 right-truncatable primes
    if is_left_truncable(i):  # There are 4260 decimal left-truncatable primes
        solutions.append(i)
        if len(solutions) == 11:  # We are told there are exactly 11
            break
print(sum(int(i) for i in solutions))
