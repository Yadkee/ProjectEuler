#! python3
"""Find the value of d < 1000 for which 1/d contains the
longest recurring cycle in its decimal fraction part."""


def cycle_len(n):
    length = 0
    d = 1
    cycles = {}
    while d:
        d %= n
        try:  # Check if we've already had this remainder
            lastCycle = cycles[d]
            return length - lastCycle
        except KeyError:  # Add it to the remainders we've had
            cycles[d] = length
        d *= 10
        length += 1
    return 0

print(max(range(1, 1000), key=cycle_len))
