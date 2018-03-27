#! python
"""Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit."""
from math import sqrt
from time import time

# If it ends with 0 the squared must end with 0 too
# If (removing the 0s) it ends with 9 then the squared end must be 3 or 7
mn = int(sqrt(10203040506070809))
mx = int(sqrt(19293949596979899))
s = "123456789"


def meets_condition(n):
    return str(n)[::2] == s

# This will return the correct value (138******0) in 10 seconds
t0 = time()
i = mn + 2  # So the first value ends with 3
t = 0  # Keeps track of whether we are on a 3 or a 7-ended number
while i < mx:
    if meets_condition(i ** 2):
        print(i * 10, "in %d seconds" % int(time() - t0))
        break
    if t:  # From ***7 to ***3
        i += 6
    else:  # From ***3 to ***7
        i += 4
    t = not t
