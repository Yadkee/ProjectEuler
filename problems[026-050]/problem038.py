#! python3
"""What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?"""

objective = set("123456789")
# How to get an upper limit of 10 ** 4 (up to9999 included):
# n is at least 2 so I've got to test every number that
#  concatenated to itself multiplied by 2 has 9 digits
#  if a number is 5 digits then itself multiplied by 2
#  will always be equal or greater than 5 digits and
#  the total will exceed 9 digits.

out = []
for i in range(1, 10 ** 4):
    l = [str(i)]
    v = len(l[0])
    for j in range(2, 10):
        s = str(i * j)
        v += len(s)
        if v > 9:
            break
        l.append(s)
    concatenated = "".join(l)
    if set(concatenated) == objective:
        out.append(concatenated)
print(max(out))
