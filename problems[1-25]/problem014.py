#! python3
"""Which starting number, under one million, produces the longest chain?"""


def chain_lenght(n):
    lenght = 1
    while n != 1:
        if n & 1:
            n = n + n + n + 1  # Python computes sums faster than mult
        else:
            n //= 2
        lenght += 1
    return lenght

print(max(range(2, 10 ** 6), key=chain_lenght))
