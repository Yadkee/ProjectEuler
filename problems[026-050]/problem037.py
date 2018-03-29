#! python3
"""Find the sum of the only eleven primes that are both truncatable from
left to right and right to left."""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import is_prime


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
