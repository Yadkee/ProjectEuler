#! python
"""Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit."""
from math import sqrt
from time import time
from itertools import cycle

# If it ends with 0 the squared must end with 0 too
# If (removing the 0s) it ends with 9 then the squared end must be 3 or 7
mn = int(sqrt(10203040506070809))
mx = int(sqrt(19293949596979899))
s = "123456789"


# This will return the correct value (138******0) in 5 seconds
t0 = time()
i = mn + mn % 3  # So the first value ends with 3
for t in cycle((4, 6)):  # ***3 -> ***7 -> ***3 -> ...
    if str(i * i)[::2] == s:
        print(i * 10, "in %d seconds" % int(time() - t0))
        break
    i += t
