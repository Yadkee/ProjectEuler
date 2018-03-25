#! python3
"""If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used? (not hyphes or spaces)"""


units = ("zero", "one", "two", "three", "four", "five", 
         "six", "seven", "eight", "nine")
tens = ("", "ten", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety")
weirds = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
          15: "fifteen", 16: "sixteen", 17: "seventeen",
          18: "eighteen", 19: "nineteen"}
magnitudes = ((10 ** 12, "trillion"), (10 ** 9, "billion"),
              (10 ** 6, "million"), (10 ** 3, "thousand"), (100, "hundred"))


def pretty_join(l):
    """Like str.join() but with commas and 'and'"""
    if len(l) <= 1:
        return "".join(l)
    else:
        return ", ".join(l[:-1]) + " and " + l[-1]


def written(n):
    assert n < 10 ** 15
    if n == 0:
        return units[0]
    out = []
    for i, j in magnitudes:
        if n >= i:
            d, n = divmod(n, i)
            out.append(written(d) + " " + j)
    if n >= 10:
        try:
            out.append(weirds[n])
        except KeyError:
            d, n = divmod(n, 10)
            if n:
                out.append(tens[d] + "-" + units[n])
            else:
                out.append(tens[d])
    elif n:
        out.append(units[n])
    return pretty_join(out)

print(sum(len(written(i).replace(" ", "").replace("-", ""))
          for i in range(1, 1001)))
