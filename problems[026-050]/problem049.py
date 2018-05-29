#! python3
"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways:
(i) each of the three terms are prime.
(ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating
the three terms in this sequence?"""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import is_prime

for i in range(1000, 3330):
    if not is_prime(i):
        continue
    chars = set(str(i))
    for j in range(i + 3330, 10000, 3330):
        if not is_prime(j) or set(str(j)) != chars:
            break
    else:
        if i != 1487:
            print(*range(i, 10000, 3330), sep="")
            break
