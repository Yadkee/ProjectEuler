#! python3
from os.path import join
from math import log10

with open(join("..", "files", "p099_base_exp.txt")) as f:
    numbers = [i.split(",") for i in f.readlines()]

out = []
for a, i in enumerate(numbers):
    base, exp = map(int, i)
    out.append((exp * log10(base), a))
print(max(out)[1] + 1)  # "+1": indexes should start at 0 but here they do not.
