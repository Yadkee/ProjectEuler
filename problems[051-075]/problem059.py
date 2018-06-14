#! python3
"""Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum
of the ASCII values in the original text."""
from os.path import join
from string import ascii_lowercase
from collections import Counter

with open(join("..", "files", "p059_cipher.txt")) as f:
    data = [int(i) for i in f.read().split(",")]


TOP = set(map(ord, " etaoi"))  # https://en.wikipedia.org/wiki/Letter_frequency
answer = 0
for i in range(3):
    print("--%d--" % i)
    stream = data[i::3]
    for l in map(ord, ascii_lowercase):
        decrypted = [i ^ l for i in stream]
        most_common = {i[0] for i in Counter(decrypted).most_common(12)}
        if TOP & most_common == TOP:
            print(chr(l), "".join(map(chr, most_common)))
            answer += sum(decrypted)
print(answer)
