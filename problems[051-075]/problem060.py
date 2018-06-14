#! python3
"""Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime."""
from functools import lru_cache
from time import time
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import is_prime, prime_generator
is_prime = lru_cache(maxsize=1 << 16)(is_prime)

# I am sorry for the spaghetti code
t0 = time()
primes = []
pairs = dict()
for i in map(str, prime_generator()):  # It can take almost a minute
    own = set()
    own.add(i)
    for j in primes:
        if is_prime(int(i + j)) and is_prime(int(j + i)):
            try:
                pairs[j].add(i)
            except KeyError:
                pairs[j] = set((j, i))
            own.add(j)
    for j in own:
        if j == i:
            continue
        for k in own - set((i, j)):
            for l in own - set((i, j, k)):
                inter = pairs[j] & pairs[k] & pairs[l] & own
                if len(inter) == 4:  # This is only to feel that sthg happens
                    print(".", end="", flush=True)
                elif len(inter) == 5:
                    print("\n\n\n\n", inter, sep="")
                    print(sum(map(int, inter)))
                    print("In %d seconds" % (time() - t0))
                    raise SystemExit
    pairs[i] = own
    primes.append(i)
