#! python3


def choose(sheets, chosen):
    new = sheets[:]
    new.remove(chosen)
    if chosen != 5:
        new.extend(range(chosen + 1, 6))
    return new


def f(sheets):
    if sheets == [5]:
        return 0
    total = len(sheets)
    out = total == 1
    for i in set(sheets):
        out += (sheets.count(i) / total) * f(choose(sheets, i))
    return out


value = f([2, 3, 4, 5])
print(round(value, 6))
