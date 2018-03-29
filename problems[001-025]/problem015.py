#! python3
"""How many such routes are there through a 20×20 grid?"""
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import fact

print(fact(2 * 20) // (fact(20) ** 2))  # 2n! / n!^2
