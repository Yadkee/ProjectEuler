#! python3
"""Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family."""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import is_prime, prime_generator

alreadyTested = set()
for i in prime_generator():
    alreadyTested.add(i)
    s = str(i)
    for l in set(s):
        if s.count(l) == 1:  # If there is only one there will exist a max of 7
            continue         # primes and the other 3 will be multiples of 3
        n = 0
        for p in range(s.startswith(l), 10):
            permutation = int(s.replace(l, str(p)))
            if is_prime(permutation):
                alreadyTested.add(permutation)
            n += permutation in alreadyTested
        if n == 8:
            break
    else:
        continue
    break
print(i)
