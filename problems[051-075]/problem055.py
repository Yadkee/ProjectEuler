#! python3
"""A number that never forms a palindrome through the reverse and add process
is called a Lychrel number. In addition you are given that for every number
below ten-thousand, it will either (i) become a palindrome in less than fifty
iterations, or, (ii) no one has managed to map it to a palindrome.
How many Lychrel numbers are there below ten-thousand?"""

lychrel = 0
for i in range(10 ** 4):
    for _ in range(50):
        i += int(str(i)[::-1])
        s = str(i)
        if s == s[::-1]:
            break
    else:
        lychrel += 1
print(lychrel)
