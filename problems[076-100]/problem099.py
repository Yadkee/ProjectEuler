#! python3
"""Using base_exp.txt, a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest
numerical value."""
from os.path import join
from math import log10

with open(join("..", "files", "p099_base_exp.txt")) as f:
    numbers = (map(int, i.split(",")) for i in f.readlines())

out = ((exp * log10(base), a) for a, (base, exp) in enumerate(numbers))
print(max(out)[1] + 1)  # "+1": indexes should start at 0 but here they do not.
