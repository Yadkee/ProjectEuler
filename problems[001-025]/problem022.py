#! python3
"""Begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.
What is the total of all the name scores in the file?"""
from os.path import join
from string import ascii_uppercase as ABC

with open(join("..", "files", "p022_names.txt")) as f:
    names = sorted(f.read().replace('"', "").split(","))


def value(word):
    return sum(ABC.index(i) for i in word) + len(word)

print(sum((a + 1) * value(i) for a, i in enumerate(names)))
