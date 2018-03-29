#! python3
"""Find the sum of all the primes below two million."""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import primes_until

print(sum(primes_until(2 * 10 ** 6)))
