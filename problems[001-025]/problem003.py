#! python3
"""What is the largest prime factor of the number 600851475143?"""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import factors

print(max(factors(600851475143)))
