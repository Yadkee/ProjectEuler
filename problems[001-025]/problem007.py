#! python3
"""What is the 10 001st prime number?"""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import prime_generator


def prime_n(n):
    for a, i in enumerate(prime_generator()):
        if a == n:
            return i

print(prime_n(10000))  # Arrays start at 0
