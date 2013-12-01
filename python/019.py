# Counting Sundays
#
# How many Sundays fell on the first of the month during twentieth century
# (1 Jan 1901 to 31 Dec 2000)

SUNDAY = 6 # integer weekday representation of sunday
total = 0

from datetime import date

for year in range(1901,2001):
    for month in range(1,13):
        if date(year,month,1).weekday() == SUNDAY:
            total += 1

print(total)

# output: 171
