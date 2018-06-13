#! python3
"""It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100,
are greater than one-million?"""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import fact


def C(n, r):
    return fact(n) / (fact(r) * fact(n - r))

print(sum(1 for n in range(1, 101) for r in range(1, n) if C(n, r) > 10 ** 6))
