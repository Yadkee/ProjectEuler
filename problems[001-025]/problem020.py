#! python3
"""Find the sum of the digits in the number 100!"""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import fact

print(sum(int(i) for i in str(fact(100))))
