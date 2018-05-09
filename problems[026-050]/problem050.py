#! python3
"""Which prime, below one-million,
can be written as the sum of the most consecutive primes?"""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import primes_until

limit = 10 ** 6
primes = list(primes_until(limit))
primeSet = set(primes)
length = len(primes)
result = []

for i in range(0, length):
    for j in range(i + 2, length):
        v = sum(primes[i:j])
        if v > limit:
            break
        if v in primeSet:
            result.append((j - i, v))
print(max(result))
