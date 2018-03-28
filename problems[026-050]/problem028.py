#! python3
"""What is the sum of the numbers on the diagonals
in a 1001 by 1001 spiral formed in the same way?"""

# I analyzed the problem a little bit:
# side s = 3 (3x3 spiral)
# corners c = 9   + 7         + 5          + 3  -->
#  --> c = s^2 + s^2-(s-1) + s^2-2(s-1) + s^2-3(s-1)
# You can notice the formula to get the corners c given the side s is:
# c(s) = 4s^2 - 6s + 6
# Since we have to sum this to the previous corners of smaller sizes:
# c(s) = 4s^2 - 6s + 6 + c(s-2)


def d(s):
    if s == 1:
        return 1
    return 4 * s ** 2 - 6 * s + 6 + d(s - 2)

print(d(1001))
