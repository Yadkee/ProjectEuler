#! python3
"""Find the sum of all the numbers that can be written as the sum
of fifth powers of their digits."""


def sum_fifth_powers(n):
    return sum(int(i) ** 5 for i in str(n))

mn = 10  # We are told to ignore 1 digit numbers because it is not a sum
mx = 9 ** 5 * 6  # Since 9^5 * 7 is lower than 10 ** 7 we won't find values
print(sum(i for i in range(mn, mx) if sum_fifth_powers(i) == i))
