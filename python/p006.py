#!/usr/bin/env python3

# Sum square difference
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

s = 0
ss = 0

for i in range(1,101):
    s += i
    ss += i*i

result = s*s - ss
print(result)

# output: 25164150
