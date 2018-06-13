#! python3
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
