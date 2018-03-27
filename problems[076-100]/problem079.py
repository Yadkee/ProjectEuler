#! python3
"""Given that the three characters are always asked for in order,
analyse the file so as to determine the shortest possible
secret passcode of unknown length."""  # I'll suposse no repeated chars
from os.path import join

with open(join("..", "files", "p079_keylog.txt")) as f:
    logins = f.read().splitlines()

before = {}  # Store the characters that preced one
for login in logins:
    for i in range(3):
        try:
            before[login[i]]
        except KeyError:
            before[login[i]] = set()
        if i:
            before[login[i]].update(set(login[:i]))
# Sort based on the preceding chars
# e.g. 1st char is the one that has never been preceded in the file
#      2nd is the one that has only been preceded by 1, and so on.
print("".join(sorted(before, key=lambda x: before[x])))
