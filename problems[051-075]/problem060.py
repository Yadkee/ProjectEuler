#! python3
"""Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime."""
from time import time
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import is_prime, prime_generator

t0 = time()
pairs = dict()
for i in map(str, prime_generator()):  # It takes ~45 seconds
    own = set(j for j in pairs if
              is_prime(int(i + j)) and is_prime(int(j + i)))
    for j in own:
        pj = pairs[j] & own
        for k in pj:
            pk = pairs[k] & pj
            for l in pk:
                print(".", end="", flush=True)
                for m in pairs[l] & pk:
                    print("\n\n")
                    print(i, j, k, l, m)
                    print(sum(map(int, (i, j, k, l, m))))
                    print("In %d seconds" % (time() - t0))
                    raise SystemExit
    pairs[i] = own
