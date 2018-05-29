#! python3
"""The sequence of triangle numbers is generated by adding the natural numbers.
What is the value of the first triangle
number to have over five hundred divisors?"""
from itertools import accumulate
from itertools import count
from math import sqrt
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import sixn


def factors_n(n):
    fac = 1
    for i in sixn(int(sqrt(n)) + 1):
        x = 1
        while not n % i:
            x += 1
            n //= i
        fac *= x
    if n != 1:
        fac *= 2
    return fac


for i in accumulate(count()):
    if factors_n(i) > 500:
        print(i)
        break
