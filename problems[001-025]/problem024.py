#! python3
"""What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
from itertools import permutations
from time import time


def self_permutations(it):
    l = len(it)
    for i in range(l):
        if l > 1:
            for p in self_permutations(it[:i] + it[i + 1:]):
                yield it[i] + p
        else:
            yield it[i]


t0 = time()
for a, i in enumerate(permutations("0123456789")):
    if a == 10 ** 6 - 1:
        print("".join(i))
        break
t1 = time()
for a, i in enumerate(self_permutations("0123456789")):
    if a == 10 ** 6 - 1:
        print(i)
        break
t2 = time()
print("Itertools took %.2f seconds. Mine took %.2f seconds" %
      (t1 - t0, t2 - t1))
print("And thats why itertools are so wonderful.")
