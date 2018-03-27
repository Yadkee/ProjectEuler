#! python
"""How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?"""
# Instead of using datetime module I wanted to create the function from scratch
DAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def date(day, month, year):
    """Returns the number of days since 1/1/1"""
    isLeap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    y = year - 1
    untilYear = y * 365 + y // 4 - y // 100 + y // 400
    untilMonth = sum(DAYS[:month]) + (month > 2 and isLeap)
    return untilYear + untilMonth + day


print(sum(date(1, j, i) % 7 == 0
          for i in range(1901, 2001)
          for j in range(1, 13)))
