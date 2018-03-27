#! python3
"""How many are triangle words? (If the word value is a triangle number)"""
from os.path import join
from string import ascii_uppercase as ABC
from math import sqrt

with open(join("..", "files", "p042_words.txt")) as f:
    words = f.read().replace('"', "").split(",")


def value(word):
    return sum(ABC.index(i) for i in word) + len(word)

# t = n(n + 1) / 2  -->  n = (-1 + sqrt(1 + 8t)) / 2
# So if n is an integer then sqrt(1 + 8t) - 1 has gotta be even (and int)
print(sum(1 for i in words if (sqrt(1 + 8 * value(i)) - 1) % 2 == 0))
